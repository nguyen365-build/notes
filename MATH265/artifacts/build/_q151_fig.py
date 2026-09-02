"""Figure generator for the Q15.1 artifact.

Two stacked panels, one per part of the exam question. The figure's single job
is the page's single idea: THREE of the four absolute extremes sit at an
ENDPOINT, so the ends of the interval are where you look first.

Contract, enforced by this module's own __main__ check:
  - EMIT CLASSES ONLY. No fill=, stroke=, font-size= or var(--...) ever
    reaches an SVG presentation attribute, because var() does not resolve
    there and an upstream CSS rule beats an attribute anyway.
  - Any line that must be exempt from svg-labels' collision test gets a class
    matching /grid|axis/ that is NOT 'gridl' or 'axis', since 'gridl' carries
    upstream PAINT and would silently repaint an annotation as a gridline.
  - Every <text> to be checked carries class 'lab'.
  - Non-ASCII goes out as HTML entities; a local file:// render has no charset.
"""
import sys

sys.dont_write_bytecode = True

import math

PI = math.pi

W = 760
X0, Y0 = 54.0, 34.0
PW, PH = 666.0, 214.0
X1, Y1 = X0 + PW, Y0 + PH
LEG_TOP = Y1 + 52.0   # 35px below the tick baseline; svg-labels PADS its boxes
CHARW = 6.6           # IBM Plex Mono advance at 11px
LEGX = 78.0           # where legend text starts
CHAR_BUDGET = 90      # measured: the gate reports outsideBox from about 96
ROW = 22.0


def cbrt(x):
    return math.copysign(abs(x) ** (1.0 / 3.0), x)


def fa(x):
    c = cbrt(x)
    return 2 * c ** 5 - 5 * c ** 4


def fb(x):
    return x + math.cos(x)


def esc(s):
    return s


class Panel(object):
    def __init__(self, xlo, xhi, ylo, yhi):
        self.xlo, self.xhi, self.ylo, self.yhi = xlo, xhi, ylo, yhi

    def px(self, x):
        return X0 + (x - self.xlo) / (self.xhi - self.xlo) * PW

    def py(self, y):
        return Y1 - (y - self.ylo) / (self.yhi - self.ylo) * PH


def poly(p, f, lo, hi, n=900, cls="curve151"):
    """Plot ONLY over the closed interval the question names. The panel's x
    range is padded so the endpoint markers are not on the frame, but drawing
    the function past the endpoint contradicts the page's whole point - and it
    is what pushed part (a)'s curve out of the top of the box."""
    pts = []
    for i in range(n + 1):
        x = lo + (hi - lo) * i / n
        pts.append("%.2f,%.2f" % (p.px(x), p.py(f(x))))
    return '<polyline class="%s" points="%s"></polyline>' % (cls, " ".join(pts))


def frame(p):
    out = ['<rect class="pbox151" x="%.1f" y="%.1f" width="%.1f" '
           'height="%.1f"></rect>' % (X0, Y0, PW, PH)]
    return out


def xticks(p, vals, labels):
    out = []
    for v, t in zip(vals, labels):
        x = p.px(v)
        out.append('<line class="gridv151" x1="%.2f" y1="%.1f" x2="%.2f" '
                   'y2="%.1f"></line>' % (x, Y0, x, Y1))
        out.append('<text class="lab tick151" x="%.2f" y="%.1f">%s</text>'
                   % (x, Y1 + 17, t))
    return out


def yticks(p, vals, labels):
    out = []
    for v, t in zip(vals, labels):
        y = p.py(v)
        out.append('<line class="gridh151" x1="%.1f" y1="%.2f" x2="%.1f" '
                   'y2="%.2f"></line>' % (X0, y, X1, y))
        out.append('<text class="lab ytick151" x="%.1f" y="%.2f">%s</text>'
                   % (X0 - 8, y + 3.6, t))
    return out


def dot(p, x, y, cls):
    return ('<circle class="%s" cx="%.2f" cy="%.2f" r="5.2"></circle>'
            % (cls, p.px(x), p.py(y)))


def sq(p, x, y, cls):
    return ('<rect class="%s" x="%.2f" y="%.2f" width="10.4" '
            'height="10.4"></rect>' % (cls, p.px(x) - 5.2, p.py(y) - 5.2))


def ring(p, x, y):
    return ('<circle class="win151" cx="%.2f" cy="%.2f" r="10.5"></circle>'
            % (p.px(x), p.py(y)))


def legend(rows):
    """rows: list of (swatch-kind, class, text). Swatch is drawn the way the
    thing it names is drawn - a key that contradicts its own plot is a bug."""
    out = ['<line class="gridrule151" x1="%.1f" y1="%.1f" x2="%.1f" '
           'y2="%.1f"></line>' % (X0, LEG_TOP - 24, X1, LEG_TOP - 24)]
    for i, (kind, cls, text) in enumerate(rows):
        y = LEG_TOP + i * ROW
        cx = X0 + 8
        if kind == "dot":
            out.append('<circle class="%s" cx="%.1f" cy="%.1f" r="5.2">'
                       '</circle>' % (cls, cx, y - 4))
        elif kind == "sq":
            out.append('<rect class="%s" x="%.1f" y="%.1f" width="10.4" '
                       'height="10.4"></rect>' % (cls, cx - 5.2, y - 9.2))
        elif kind == "ring":
            out.append('<circle class="win151" cx="%.1f" cy="%.1f" r="7.5">'
                       '</circle>' % (cx, y - 4))
        elif kind == "flat":
            out.append('<line class="flat151" x1="%.1f" y1="%.1f" x2="%.1f" '
                       'y2="%.1f"></line>' % (cx - 8, y - 4, cx + 8, y - 4))
        elif kind == "lev":
            out.append('<line class="lev151" x1="%.1f" y1="%.1f" x2="%.1f" '
                       'y2="%.1f"></line>' % (cx - 8, y - 4, cx + 8, y - 4))
        out.append('<text class="lab leg151" x="%.1f" y="%.1f">%s</text>'
                   % (cx + 16, y, text))
    return out


def panel_a():
    p = Panel(-1.6, 20.6, -19.5, 26.5)
    o = []
    o += frame(p)
    o += yticks(p, [-16, -8, 0, 8, 16], ["-16", "-8", "0", "8", "16"])
    o += xticks(p, [-1, 0, 4, 8, 12, 16, 20],
                ["-1", "0", "4", "8", "12", "16", "20"])
    # the level of the winning maximum, drawn full strength so it is not
    # mistaken for a gridline
    ym = fa(20.0)
    o.append('<line class="lev151" x1="%.1f" y1="%.2f" x2="%.1f" y2="%.2f">'
             '</line>' % (X0, p.py(ym), X1, p.py(ym)))
    o.append(poly(p, fa, -1.0, 20.0))
    # candidates: squares for endpoints, circles for interior critical points
    o.append(ring(p, 20.0, ym))
    o.append(ring(p, 8.0, -16.0))
    o.append(sq(p, -1.0, -7.0, "endp151"))
    o.append(sq(p, 20.0, ym, "endp151"))
    o.append(dot(p, 0.0, 0.0, "crit151"))
    o.append(dot(p, 8.0, -16.0, "crit151"))
    o.append('<text class="lab ph151" x="%.1f" y="%.1f">PART (a) &#160; '
             '2x^(5/3) &#8722; 5x^(4/3) &#160;ON&#160; [&#8722;1, 20] &#160;'
             '&#183;&#160; x ACROSS, f(x) UP</text>' % (X0, 20))
    o += legend([
        ("sq", "endp151", "ENDPOINT CANDIDATE &#183; f(&#8722;1) = &#8722;7, "
                          "f(20) = 23.2808"),
        ("dot", "crit151", "INTERIOR CRITICAL POINT &#183; f(0) = 0 a local "
                           "max, f(8) = &#8722;16"),
        ("ring", "", "THE WINNER &#183; max at the RIGHT ENDPOINT, min at the "
                     "interior point x = 8"),
        ("lev", "", "THE LEVEL OF THE MAXIMUM &#183; nothing on the curve "
                    "reaches it before x = 20"),
    ])
    h = LEG_TOP + 4 * ROW + 6
    return ('<svg class="fig151" viewBox="0 0 %d %.0f" '
            'preserveAspectRatio="xMidYMid meet" role="img" '
            'aria-label="Part (a) plotted on the interval negative one to '
            'twenty, with the four candidate points marked and the maximum '
            'level drawn across the panel.">%s</svg>' % (W, h, "".join(o)))


def panel_b():
    p = Panel(-PI - 0.45, 2 * PI + 0.45, -5.4, 9.0)
    o = []
    o += frame(p)
    o += yticks(p, [-4, 0, 4, 8], ["-4", "0", "4", "8"])
    o += xticks(p, [-PI, -PI / 2, 0, PI / 2, PI, 3 * PI / 2, 2 * PI],
                ["-&#960;", "-&#960;/2", "0", "&#960;/2", "&#960;",
                 "3&#960;/2", "2&#960;"])
    o.append(poly(p, fb, -PI, 2 * PI))
    # the flat tangent at pi/2, drawn as a short horizontal segment
    yv = fb(PI / 2)
    o.append('<line class="flat151" x1="%.2f" y1="%.2f" x2="%.2f" y2="%.2f">'
             '</line>' % (p.px(PI / 2 - 0.95), p.py(yv),
                          p.px(PI / 2 + 0.95), p.py(yv)))
    o.append(ring(p, 2 * PI, fb(2 * PI)))
    o.append(ring(p, -PI, fb(-PI)))
    o.append(sq(p, -PI, fb(-PI), "endp151"))
    o.append(sq(p, 2 * PI, fb(2 * PI), "endp151"))
    o.append(dot(p, PI / 2, yv, "crit151"))
    o.append('<text class="lab ph151" x="%.1f" y="%.1f">PART (b) &#160; '
             'x + cos x &#160;ON&#160; [&#8722;&#960;, 2&#960;] &#160;&#183;'
             '&#160; x ACROSS, f(x) UP</text>' % (X0, 20))
    o += legend([
        ("sq", "endp151", "ENDPOINT CANDIDATE &#183; f(&#8722;&#960;) = "
                          "&#8722;4.1416, f(2&#960;) = 7.2832"),
        ("dot", "crit151", "INTERIOR CRITICAL POINT &#183; f(&#960;/2) = "
                           "1.5708, and it wins NOTHING"),
        ("ring", "", "THE WINNER &#183; BOTH extremes are endpoints here"),
        ("flat", "", "THE HORIZONTAL TANGENT &#183; f' touches zero WITHOUT "
                     "changing sign"),
    ])
    h = LEG_TOP + 4 * ROW + 6
    return ('<svg class="fig151" viewBox="0 0 %d %.0f" '
            'preserveAspectRatio="xMidYMid meet" role="img" '
            'aria-label="Part (b) plotted on the interval negative pi to two '
            'pi, rising throughout, with a horizontal tangent marked at pi '
            'over two and both extremes at the endpoints.">%s</svg>'
            % (W, h, "".join(o)))


CLASSES = ["curve151", "pbox151", "gridv151", "gridh151",
           "gridrule151", "tick151", "ytick151", "endp151", "crit151",
           "win151", "lev151", "flat151", "leg151", "ph151", "fig151"]


def build():
    return panel_a(), panel_b()


if __name__ == "__main__":
    import re
    a, b = build()
    both = a + b
    for bad in ("fill=", "stroke=", "font-size=", "var(--"):
        assert bad not in both, "PRESENTATION ATTRIBUTE LEAKED: " + bad
    assert "gridl" not in both, "'gridl' carries upstream paint, do not use it"
    assert 'class="axis"' not in both
    emitted = set()
    for m in re.finditer(r'class="([^"]+)"', both):
        for c in m.group(1).split():
            emitted.add(c)
    extra = emitted - set(CLASSES) - {"lab"}
    assert not extra, "class emitted but not declared: " + repr(sorted(extra))
    missing = set(CLASSES) - emitted
    assert not missing, "declared but never emitted: " + repr(sorted(missing))
    for c in emitted:
        if c.startswith("gridref"):
            assert re.search(r"grid|axis", c), c + " will not be exempt"
    # WIDTH BUDGET: svg-labels reports outsideBox from about 96 monospace
    # characters at 11px starting from x=78. Assert the budget rather than
    # eyeballing it, and keep 6 characters of margin.
    ENT = {"&#183;": ".", "&#8722;": "-", "&#160;": " ", "&#960;": "p"}
    for m in re.finditer(r'class="lab leg151"[^>]*>([^<]*)<', both):
        s = m.group(1)
        for k, v in ENT.items():
            s = s.replace(k, v)
        assert len(s) <= CHAR_BUDGET, ("legend line is %d chars, budget is %d: %r"
                                       % (len(s), CHAR_BUDGET, s[:60]))
    longest = 0
    for m in re.finditer(r'class="lab leg151"[^>]*>([^<]*)<', both):
        s = m.group(1)
        for k, v in ENT.items():
            s = s.replace(k, v)
        longest = max(longest, len(s))
    assert LEGX + longest * CHARW < X1 - 4, "longest legend line overruns"
    # BOUNDS CHECK: every plotted point must sit inside the panel frame.
    # A curve drawn past the interval is what caused the overflow, so assert
    # containment rather than trusting the y range.
    for m in re.finditer(r'class="curve151" points="([^"]+)"', both):
        for pair in m.group(1).split():
            xx, yy = (float(v) for v in pair.split(","))
            assert X0 - 0.5 <= xx <= X1 + 0.5, "curve x out of frame: %.2f" % xx
            assert Y0 - 0.5 <= yy <= Y1 + 0.5, "curve y out of frame: %.2f" % yy
    nonascii = [ch for ch in both if ord(ch) > 127]
    assert not nonascii, "non-ASCII in svg: " + repr(nonascii[:6])
    print("fig OK: %d classes, %d bytes, 0 presentation attributes, "
          "0 non-ASCII" % (len(emitted), len(both)))
    print("        longest legend line %d chars of a %d budget, "
          "ending at x=%.0f of %.0f"
          % (longest, CHAR_BUDGET, LEGX + longest * CHARW, X1))
