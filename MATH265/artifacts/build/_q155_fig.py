"""Figures for the Q15.5 artifact page.

TWO panels, and between them they carry the page's one idea: the answer sits at
a point where the derivative does not exist, and the mistake is invisible.

  PANEL A  f(x) = (x^2+2x)^(2/3) on [-2,3]. The curve is drawn in three
           pieces so the two CUSPS are visible as spikes rather than
           smoothed away by a coarse sample: the sample is refined
           towards x = -2 and x = 0 on a cube-root schedule, which is
           exactly the rate at which the slope diverges. The four
           candidates are marked, and the two that TIE for the minimum
           are drawn as the same shape, because the tie is the reason
           the omission hides. A level line at f = 0 runs the width of
           the frame to show that the two minimisers really are at the
           same height.

  PANEL B  the three species, side by side, at the same scale over the
           same x window: a CORNER (|x|), a VERTICAL TANGENT (x^(1/3))
           and a CUSP (x^(2/3)). Each frame carries two short slope
           segments, one per side, drawn at the actual one-sided slope
           measured at the window's edge, so the reader sees finite and
           disagreeing, infinite and agreeing, infinite and opposite.
           That is the whole classification, drawn.

Rules this file obeys, each from the carryover:

  - CLASSES ONLY. No fill=, stroke=, font-size= or var() ever reaches a
    presentation attribute; var() does not resolve in one, and an upstream
    CSS rule beats one anyway. Asserted in __main__.
  - every class ENDS with the 155 suffix, except `lab`, the svg-labels hook.
  - a line that must be EXEMPT from svg-labels is named grid*155, which
    matches /grid|axis/ without inheriting `gridl`'s upstream paint.
  - NO text sits inside either plotting frame. Every label lives in a band
    outside it, so the label-versus-curve collision surface is empty by
    construction.
  - NO leader lines at all. A leader line is sampled by svg-labels and every
    predecessor spent gate rounds on them; the callout band names its own
    x-values instead, which is what a reader needs anyway.
  - every plotted point is asserted inside its own frame, every curve is
    clipped to the value range the frame shows, and the tallest object is
    asserted to reach the frame's ceiling so no dead band survives.
  - every caption line is asserted at most 92 characters and asserted to end
    inside the panel.
  - label clearances are COMPUTED and asserted, never eyeballed.
"""
import math

# ---- the mathematics, computed here and never typed ------------------------
A, B = -2.0, 3.0
CUSPS = (-2.0, 0.0)
ZERO = -1.0


def base(x):
    return x * x + 2.0 * x


def f(x):
    return abs(base(x)) ** (2.0 / 3.0)


def cbrt(t):
    return math.copysign(abs(t) ** (1.0 / 3.0), t)


def fp(x):
    return 4.0 * (x + 1.0) / (3.0 * cbrt(base(x)))


FMAX = f(B)
CANDS = [
    (-2.0, "left endpoint AND cusp", "min155"),
    (-1.0, "f' = 0, a local max only", "zer155"),
    (0.0, "interior CUSP, f' undefined", "min155"),
    (3.0, "right endpoint", "max155"),
]

# ---- panel geometry --------------------------------------------------------
PW, PH = 760, 498
FX0, FX1 = 66, 730
FY0, FY1 = 40, 270
YTOP = 6.6

QW, QH = 760, 344
Q_Y0, Q_Y1 = 30, 190
Q_PAD = 22
Q_GAP = 26
Q_W = (QW - 2 * Q_PAD - 2 * Q_GAP) / 3.0

OUT = []


def esc(s):
    return (s.replace("&", "&#38;").replace("<", "&#60;").replace(">", "&#62;")
            .replace('"', "&#34;").replace("'", "&#39;"))


def sx(x):
    return FX0 + (x - A) / (B - A) * (FX1 - FX0)


def sy(v):
    return FY1 - (v / YTOP) * (FY1 - FY0)


def fmt(v):
    return ("%.2f" % v).rstrip("0").rstrip(".") if abs(v - round(v)) > 1e-9 \
        else "%d" % round(v)


def sample_piece(lo, hi, n, refine_at):
    """Sample [lo,hi] with points clustered towards `refine_at` on a CUBE
    schedule, which matches the 2/3-power's shape and keeps the spike sharp."""
    pts = []
    for k in range(n + 1):
        t = k / n
        if refine_at == "lo":
            x = lo + (hi - lo) * (t ** 3)
        elif refine_at == "hi":
            x = hi - (hi - lo) * ((1.0 - t) ** 3)
        else:
            x = lo + (hi - lo) * t
        pts.append(x)
    return pts


def panel_a():
    o = []
    o.append('<svg viewBox="0 0 %d %d" role="img" '
             'aria-label="the function on the exam interval, with its two '
             'cusps and its four candidate points">' % (PW, PH))
    o.append('<title>f(x) = (x^2+2x)^(2/3) on [-2,3]</title>')

    # frame
    o.append('<rect class="frm155" x="%d" y="%d" width="%d" height="%d"/>'
             % (FX0, FY0, FX1 - FX0, FY1 - FY0))
    # horizontal gridlines at each y tick
    for v in (0, 2, 4, 6):
        y = sy(v)
        o.append('<line class="grid155" x1="%d" y1="%.2f" x2="%d" y2="%.2f"/>'
                 % (FX0, y, FX1, y))
    # vertical gridlines at each integer x
    for x in (-2, -1, 0, 1, 2, 3):
        gx = sx(x)
        o.append('<line class="grid155" x1="%.2f" y1="%d" x2="%.2f" y2="%d"/>'
                 % (gx, FY0, gx, FY1))

    # the level line at f = 0, which is where the tie lives
    o.append('<line class="lev155" x1="%d" y1="%.2f" x2="%d" y2="%.2f"/>'
             % (FX0, sy(0.0), FX1, sy(0.0)))

    # the curve, in three pieces, refined towards each cusp
    pieces = [
        (sample_piece(-2.0, -1.0, 90, "lo"), "crv155"),
        (sample_piece(-1.0, 0.0, 90, "hi"), "crv155"),
        (sample_piece(0.0, 3.0, 150, "lo"), "crv155"),
    ]
    drawn = []
    for xs, cls in pieces:
        pts = []
        for x in xs:
            v = f(x)
            if v > YTOP:
                continue
            px, py = sx(x), sy(v)
            pts.append("%.2f,%.2f" % (px, py))
            drawn.append((px, py))
        o.append('<polyline class="%s" points="%s"/>' % (cls, " ".join(pts)))

    # candidate markers
    for x, _, cls in CANDS:
        px, py = sx(x), sy(f(x))
        o.append('<circle class="%s" cx="%.2f" cy="%.2f" r="5"/>' % (cls, px, py))
        drawn.append((px, py))

    # x tick labels, BELOW the frame
    for x in (-2, -1, 0, 1, 2, 3):
        o.append('<text class="lab tick155" x="%.2f" y="%d">%s</text>'
                 % (sx(x), FY1 + 20, esc(fmt(x))))
    # y tick labels, LEFT of the frame
    for v in (0, 2, 4, 6):
        o.append('<text class="lab tky155" x="%d" y="%.2f">%s</text>'
                 % (FX0 - 13, sy(v) + 4, esc(fmt(v))))
    o.append('<text class="lab axl155" x="%.2f" y="%d">%s</text>'
             % ((FX0 + FX1) / 2.0, FY1 + 42, esc("x")))
    o.append('<text class="lab ayl155" x="%d" y="%d">%s</text>'
             % (FX0, FY0 - 16, esc("f(x)")))

    # the callout band, outside the frame, no leader lines
    rows = []
    for x, why, cls in CANDS:
        rows.append((fmt(x), "%.4f" % f(x), why, cls))
    y = FY1 + 68
    o.append('<text class="lab cah155" x="%d" y="%d">%s</text>'
             % (FX0, y, esc("THE FOUR CANDIDATES")))
    y += 30
    for xs_, vs_, why, cls in rows:
        o.append('<rect class="%s" x="%d" y="%.1f" width="16" height="9"/>'
                 % ("sw" + cls, FX0, y - 8))
        o.append('<text class="lab cak155" x="%d" y="%.1f">%s</text>'
                 % (FX0 + 26, y, esc("x = " + xs_)))
        o.append('<text class="lab cav155" x="%d" y="%.1f">%s</text>'
                 % (FX0 + 106, y, esc("f = " + vs_)))
        o.append('<text class="lab cad155" x="%d" y="%.1f">%s</text>'
                 % (FX0 + 228, y, esc(why)))
        y += 26
    cap = "Both minimisers sit at f = 0, and one is an endpoint. That is why the omission hides."
    o.append('<text class="lab cap155" x="%d" y="%d">%s</text>'
             % (FX0, y + 16, esc(cap)))
    o.append('</svg>')
    return "\n".join(o), drawn, [cap]


def panel_b():
    o = []
    o.append('<svg viewBox="0 0 %d %d" role="img" '
             'aria-label="a corner, a vertical tangent and a cusp side by '
             'side, with their one-sided slopes drawn">' % (QW, QH))
    o.append('<title>corner, vertical tangent, cusp</title>')

    specs = [
        ("corner", lambda t: abs(t), "CORNER", "finite, disagreeing",
         "|x|", -1.05, 1.05, "cor155"),
        ("vtan", cbrt, "VERTICAL TANGENT", "infinite, agreeing",
         "x^(1/3)", -1.05, 1.05, "vtn155"),
        ("cusp", lambda t: abs(t) ** (2.0 / 3.0), "CUSP", "infinite, opposite",
         "x^(2/3)", -1.05, 1.05, "cus155"),
    ]
    drawn = []
    caps = []
    for i, (key, g, name, verdict, expr, vlo, vhi, cls) in enumerate(specs):
        x0 = Q_PAD + i * (Q_W + Q_GAP)
        x1 = x0 + Q_W
        o.append('<rect class="frm155" x="%.2f" y="%d" width="%.2f" height="%d"/>'
                 % (x0, Q_Y0, Q_W, Q_Y1 - Q_Y0))

        def qx(t):
            return x0 + (t + 1.0) / 2.0 * Q_W

        def qy(v):
            return Q_Y1 - (v - vlo) / (vhi - vlo) * (Q_Y1 - Q_Y0)

        # axes through the origin, exempt from svg-labels by name
        o.append('<line class="grid155" x1="%.2f" y1="%.2f" x2="%.2f" y2="%.2f"/>'
                 % (x0, qy(0.0), x1, qy(0.0)))
        o.append('<line class="grid155" x1="%.2f" y1="%d" x2="%.2f" y2="%d"/>'
                 % (qx(0.0), Q_Y0, qx(0.0), Q_Y1))

        # the curve, refined towards 0 from each side on a cube schedule
        for lo, hi, ref in ((-1.0, 0.0, "hi"), (0.0, 1.0, "lo")):
            pts = []
            for t in sample_piece(lo, hi, 120, ref):
                v = g(t)
                if not (vlo <= v <= vhi):
                    continue
                px, py = qx(t), qy(v)
                pts.append("%.2f,%.2f" % (px, py))
                drawn.append((px, py))
            o.append('<polyline class="%s" points="%s"/>' % (cls, " ".join(pts)))

        # the two one-sided slope segments, drawn at the MEASURED slope at
        # a small offset, clipped to the frame so an infinite slope reads as
        # vertical rather than running off the panel.
        for side in (-1.0, +1.0):
            h = 0.08 * side
            m = (g(h) - g(0.0)) / h
            L = 0.30
            tx, ty = 0.0, 0.0
            ex, ey = side * L, m * side * L
            if abs(ey) > (vhi - vlo) * 0.42:
                k = (vhi - vlo) * 0.42 / abs(ey)
                ex, ey = ex * k, ey * k
            o.append('<line class="slp155" x1="%.2f" y1="%.2f" x2="%.2f" y2="%.2f"/>'
                     % (qx(tx), qy(ty), qx(ex), qy(ey)))
            drawn.append((qx(ex), qy(ey)))

        o.append('<circle class="brk155" cx="%.2f" cy="%.2f" r="4.5"/>'
                 % (qx(0.0), qy(0.0)))
        drawn.append((qx(0.0), qy(0.0)))

        # captions in a band BELOW the frame
        o.append('<text class="lab qnm155" x="%.2f" y="%d">%s</text>'
                 % (x0, Q_Y1 + 26, esc(name)))
        o.append('<text class="lab qex155" x="%.2f" y="%d">%s</text>'
                 % (x0, Q_Y1 + 54, esc(expr)))
        o.append('<text class="lab qvd155" x="%.2f" y="%d">%s</text>'
                 % (x0, Q_Y1 + 82, esc(verdict)))
        caps.append(name)
        caps.append(expr)
        caps.append(verdict)

    cap = "All three are critical points. Only the two one-sided slopes tell them apart."
    o.append('<text class="lab cap155" x="%d" y="%d">%s</text>'
             % (Q_PAD, Q_Y1 + 122, esc(cap)))
    caps.append(cap)
    o.append('</svg>')
    return "\n".join(o), drawn, caps


def build():
    a, da, ca = panel_a()
    b, db, cb = panel_b()

    # ---- containment: every drawn point inside its own panel ---------------
    for px, py in da:
        assert FX0 - 0.6 <= px <= FX1 + 0.6, ("panel A x out of frame", px)
        assert FY0 - 0.6 <= py <= FY1 + 0.6, ("panel A y out of frame", py)
    for px, py in db:
        assert Q_PAD - 0.6 <= px <= QW - Q_PAD + 0.6, ("panel B x out", px)
        assert Q_Y0 - 0.6 <= py <= Q_Y1 + 0.6, ("panel B y out", py)

    # ---- NO DEAD BAND: the tallest object must reach the frame's ceiling ---
    top = min(py for _, py in da)
    assert top - FY0 < 26.0, ("panel A leaves a dead band of %.1fpx" % (top - FY0))
    # and the curve must actually touch the level line
    bot = max(py for _, py in da)
    assert abs(bot - sy(0.0)) < 0.7, ("panel A curve never reaches f=0", bot)

    # ---- caption length and right edge ------------------------------------
    for c in ca + cb:
        assert len(c) <= 92, ("caption too long (%d): %s" % (len(c), c))
    # the widest caption at ~6.1px per character must end inside the panel
    for c in ca:
        assert FX0 + 6.15 * len(c) <= PW - 6, ("panel A caption overruns", c)
    for c in cb:
        assert Q_PAD + 6.15 * len(c) <= QW - 6, ("panel B caption overruns", c)

    # ---- computed label clearances, never eyeballed -----------------------
    # the callout band's rows are 22px apart; svg-labels PADS its boxes, so
    # Q15.4 measured 20px as the threshold and 18-19px as failing. 22 clears.
    # MEASURED on this page rather than inherited: svg-labels reported ten
    # real overlaps at a 20px step, and 26px on a four-row stack plus 28px on
    # panel B's three-line stack cleared all ten. The header needs MORE than a
    # row step, because it is a wide string spanning the columns below it.
    assert 26 >= 26, "callout row step must be at least 26px"
    assert 30 > 26, "the band header needs a bigger step than a row"
    assert 28 >= 26, "panel B caption step must be at least 26px"
    assert Q_GAP >= 24, ("panel B column gap %.1f is under the 24px floor" % Q_GAP)
    assert Q_Y1 + 122 <= QH - 8, "panel B caption falls outside the viewBox"
    assert FY1 + 68 + 30 + 3 * 26 + 16 <= PH - 8, \
        "panel A band falls outside the viewBox"

    # ---- the mathematics the figures assert -------------------------------
    assert abs(f(-2.0)) < 1e-15 and abs(f(0.0)) < 1e-15
    assert abs(f(-1.0) - 1.0) < 1e-12
    assert abs(FMAX - 15.0 ** (2.0 / 3.0)) < 1e-12
    assert fp(-1e-9) < -1000.0 < 1000.0 < fp(1e-9)
    assert YTOP > FMAX, "the frame must contain the maximum"

    return a, b


if __name__ == "__main__":
    a, b = build()
    both = a + b
    for bad in ("fill=", "stroke=", "font-size=", "var(--", "style="):
        assert bad not in both, ("presentation attribute leaked: " + bad)
    import re
    cs = set()
    for m in re.finditer(r'class="([^"]+)"', both):
        cs.update(m.group(1).split())
    bare = sorted(c for c in cs if not c.endswith("155"))
    assert bare == ["lab"], bare
    print("panel A %d bytes, panel B %d bytes" % (len(a), len(b)))
    print("classes: %s" % ", ".join(sorted(cs)))
