"""Figures for the Q15.2 artifact page.

TWO panels, and between them they carry the page's one idea.

  PANEL A  the objective P(w) = 2w + 440/w with its two component terms.
           The curve LEAVES THE TOP of the frame at the left and keeps
           climbing at the right, and there are deliberately NO endpoint
           markers anywhere, because there are no endpoints. The two
           dashed terms cross exactly under the minimum, which is the
           self-check from section 06 drawn rather than asserted.

  PANEL B  five rectangles of area 220 drawn TO SCALE on one baseline,
           with their perimeters. The list is symmetric about the square
           because P(w) = P(220/w), so the square is the fixed point of
           that involution.

Rules this file obeys, each from the carryover:

  - CLASSES ONLY. No fill=, stroke=, font-size= or var() ever reaches a
    presentation attribute; var() does not resolve in one and an
    upstream CSS rule beats one anyway. Asserted in __main__.
  - every class ENDS with the 152 suffix, except `lab`, which is the
    svg-labels hook.
  - a line that must be EXEMPT from svg-labels is named grid*152, which
    matches /grid|axis/ without inheriting `gridl`'s upstream paint.
  - every plotted point is asserted INSIDE the panel frame, so a padded
    range cannot draw the curve outside the box.
  - every legend line is asserted at most 90 characters after entity
    decoding, and the longest is asserted to end inside the frame.
"""
import math

# ---- the mathematics, computed here and nowhere typed -------------------
AREA = 220.0
W_STAR = math.sqrt(AREA)
P_STAR = 4.0 * math.sqrt(AREA)


def P(w):
    return 2.0 * w + 2.0 * AREA / w


def esc(s):
    return (s.replace("&", "&" + "amp;").replace("<", "&" + "lt;")
             .replace(">", "&" + "gt;"))


def f(v):
    """Trim a float for an SVG coordinate."""
    return ("%.2f" % v).rstrip("0").rstrip(".")


# =======================================================================
# PANEL A
# =======================================================================
AW, AH = 720.0, 370.0
AL, AR, AT, AB = 78.0, 690.0, 26.0, 250.0
WMAX = 56.0
YMAX = 140.0
A_TICKROW = 266.0
A_LEG0 = 301.0
A_LEGSTEP = 22.0


def ax(w):
    return AL + (w / WMAX) * (AR - AL)


def ay(y):
    return AB - (y / YMAX) * (AB - AT)


def panel_a():
    out = []
    add = out.append
    inside = []

    add('<svg class="fig152" viewBox="0 0 %s %s" role="img" '
        'aria-label="the objective 2w + 440 over w, its two component '
        'terms, and the minimum level drawn across the whole panel">'
        % (f(AW), f(AH)))

    # frame
    add('<rect class="pbox152" x="%s" y="%s" width="%s" height="%s"></rect>'
        % (f(AL), f(AT), f(AR - AL), f(AB - AT)))

    # gridlines
    for wv in (10, 20, 30, 40, 50):
        add('<line class="gridv152" x1="%s" y1="%s" x2="%s" y2="%s"></line>'
            % (f(ax(wv)), f(AT), f(ax(wv)), f(AB)))
    for yv in (20, 40, 60, 80, 100, 120):
        add('<line class="gridh152" x1="%s" y1="%s" x2="%s" y2="%s"></line>'
            % (f(AL), f(ay(yv)), f(AR), f(ay(yv))))

    # the two component terms, clipped to the frame
    # 2w is a straight line, so two points is the whole of it
    pts = [(ax(0.0), ay(0.0)), (ax(WMAX), ay(2.0 * WMAX))]
    assert 2.0 * WMAX <= YMAX, "the 2w line would leave the frame"
    inside.extend(pts)
    add('<polyline class="termlin152" points="%s"></polyline>'
        % " ".join("%s,%s" % (f(a), f(b)) for a, b in pts))

    pts = []
    for i in range(1, 761):
        w = WMAX * i / 760.0
        y = 2.0 * AREA / w
        if 0.0 <= y <= YMAX:
            pts.append((ax(w), ay(y)))
    inside.extend(pts)
    add('<polyline class="termhyp152" points="%s"></polyline>'
        % " ".join("%s,%s" % (f(a), f(b)) for a, b in pts))

    # the objective itself
    pts = []
    for i in range(1, 1101):
        w = WMAX * i / 1100.0
        y = P(w)
        if 0.0 <= y <= YMAX:
            pts.append((ax(w), ay(y)))
    inside.extend(pts)
    add('<polyline class="curveP152" points="%s"></polyline>'
        % " ".join("%s,%s" % (f(a), f(b)) for a, b in pts))

    # the minimum level, drawn all the way across. EXEMPT class.
    add('<line class="gridlev152" x1="%s" y1="%s" x2="%s" y2="%s"></line>'
        % (f(AL), f(ay(P_STAR)), f(AR), f(ay(P_STAR))))
    # the drop line to the axis, also exempt
    add('<line class="gridrop152" x1="%s" y1="%s" x2="%s" y2="%s"></line>'
        % (f(ax(W_STAR)), f(ay(P_STAR)), f(ax(W_STAR)), f(AB)))

    # markers
    add('<circle class="minm152" cx="%s" cy="%s" r="4.6"></circle>'
        % (f(ax(W_STAR)), f(ay(P_STAR))))
    add('<circle class="crossm152" cx="%s" cy="%s" r="3.4"></circle>'
        % (f(ax(W_STAR)), f(ay(P_STAR / 2.0))))
    inside.append((ax(W_STAR), ay(P_STAR)))
    inside.append((ax(W_STAR), ay(P_STAR / 2.0)))

    # ticks
    add('<text class="lab ph152" x="%s" y="16">%s</text>'
        % (f(AL), esc("THE OBJECTIVE 2w + 440/w - P AND w BOTH IN cm")))
    for wv in (0, 10, 20, 30, 40, 50):
        add('<text class="lab tick152" x="%s" y="%s">%d</text>'
            % (f(ax(wv)), f(A_TICKROW), wv))
    for yv in (20, 40, 60, 80, 100, 120, 140):
        add('<text class="lab ytick152" x="%s" y="%s">%d</text>'
            % (f(AL - 8.0), f(ay(yv) + 3.5), yv))

    # The level's own label. It started on the LEFT above the line, where
    # svg-labels found the hyperbola AND the curve running through it -
    # both are steep there. It now sits BELOW the level line at the right
    # end, right-anchored, in a band where the curve is far above, the 2w
    # line is far above and the hyperbola is far below.
    add('<text class="lab levlab152" x="%s" y="%s">%s</text>'
        % (f(AR - 10.0), f(ay(P_STAR) + 15.0),
           esc("MINIMUM LEVEL P = %.4f" % P_STAR)))

    # The callout. It started in the upper RIGHT, where svg-labels found
    # the 2w line and the curve crossing it, because that wedge narrows
    # as the curve climbs. The band x 170 to 421, y 52 to 96 is genuinely
    # empty: across it the curve never rises above y = 125, the 2w line
    # never above 149 and the hyperbola never above 166.
    for k, s in enumerate(["MINIMUM %.4f cm" % P_STAR,
                           "AT w = %.4f cm" % W_STAR,
                           "PROVED BY CONVEXITY, NOT BY COMPARISON"]):
        add('<text class="lab callo152" x="170" y="%s">%s</text>'
            % (f(52.0 + 22.0 * k), esc(s)))

    # Legend. Three rows, and every swatch is drawn the way the thing it
    # names is drawn: a SOLID swatch for the solid curve, and a swatch
    # split into two segments for each dashed line. A fourth row that
    # named no drawn element at all was removed - a swatch keyed to
    # nothing is a legend contradicting its own figure, which is the rule
    # the carryover records one tier up.
    legend = [
        ("swpl152", False,
         "P(w) = 2w + 440/w, the objective after eliminating l"),
        ("swtm152", True,
         "2w and 440/w, the two terms, EQUAL under the minimum"),
        ("swlv152", True,
         "the minimum level %.4f, drawn all the way across" % P_STAR),
    ]
    for k, (cls, dashed, txt) in enumerate(legend):
        y = A_LEG0 + A_LEGSTEP * k
        if dashed:
            add('<rect class="%s" x="%s" y="%s" width="6.5" height="3">'
                '</rect>' % (cls, f(AL), f(y - 4.0)))
            add('<rect class="%s" x="%s" y="%s" width="6.5" height="3">'
                '</rect>' % (cls, f(AL + 9.5), f(y - 4.0)))
        else:
            add('<rect class="%s" x="%s" y="%s" width="16" height="3">'
                '</rect>' % (cls, f(AL), f(y - 4.0)))
        add('<text class="lab leg152" x="%s" y="%s">%s</text>'
            % (f(AL + 24.0), f(y), esc(txt)))
    add("</svg>")

    return "".join(out), inside, [t for _, _d, t in legend]


# =======================================================================
# PANEL B
# =======================================================================
BW, BH = 720.0, 312.0
BL, BR, BT, BB = 78.0, 690.0, 26.0, 286.0
SCALE = 3.2
BASE = 250.0
B_DIMROW = 36.0
B_PROW = 272.0
GAP = 56.0
X0 = 96.0

# the five rectangles, all of area 220, symmetric about the square
RECTS = [4.0, 8.0, W_STAR, 27.5, 55.0]


def panel_b():
    out = []
    add = out.append
    inside = []

    add('<svg class="fig152" viewBox="0 0 %s %s" role="img" '
        'aria-label="five rectangles of area 220 square centimetres drawn '
        'to scale on one baseline, with the square in the middle carrying '
        'the smallest perimeter">' % (f(BW), f(BH)))
    add('<rect class="pbox152" x="%s" y="%s" width="%s" height="%s">'
        '</rect>' % (f(BL), f(BT), f(BR - BL), f(BB - BT)))
    add('<line class="gridbase152" x1="%s" y1="%s" x2="%s" y2="%s">'
        '</line>' % (f(BL), f(BASE), f(BR), f(BASE)))

    add('<text class="lab ph152" x="%s" y="16">%s</text>'
        % (f(BL), esc("EVERY RECTANGLE HAS AREA 220 SQUARE cm, DRAWN TO SCALE")))

    x = X0
    for w in RECTS:
        l = AREA / w
        pw = w * SCALE
        ph = l * SCALE
        top = BASE - ph
        is_sq = abs(w - W_STAR) < 1e-9
        add('<rect class="%s" x="%s" y="%s" width="%s" height="%s">'
            '</rect>' % ("sqbox152" if is_sq else "rbox152",
                         f(x), f(top), f(pw), f(ph)))
        inside.append((x, top))
        inside.append((x + pw, BASE))
        cx = x + pw / 2.0
        if is_sq:
            dim = "%.2f x %.2f" % (w, l)
            per = "P = %.4f" % (2.0 * w + 2.0 * l)
        else:
            dim = ("%g x %g" % (w, l))
            per = "P = %g" % (2.0 * w + 2.0 * l)
        add('<text class="lab dim152" x="%s" y="%s">%s</text>'
            % (f(cx), f(B_DIMROW), esc(dim)))
        add('<text class="lab %s" x="%s" y="%s">%s</text>'
            % ("perwin152" if is_sq else "per152", f(cx), f(B_PROW),
               esc(per)))
        x += pw + GAP
    right_edge = x - GAP

    add("</svg>")
    return "".join(out), inside, right_edge


# =======================================================================
def build():
    a, a_inside, a_leg = panel_a()
    b, b_inside, b_right = panel_b()

    # ---- every plotted point inside the panel frame ------------------
    for px, py in a_inside:
        assert AL - 0.01 <= px <= AR + 0.01, "panel A point outside x: %r" % px
        assert AT - 0.01 <= py <= AB + 0.01, "panel A point outside y: %r" % py
    for px, py in b_inside:
        assert BL - 0.01 <= px <= BR + 0.01, "panel B point outside x: %r" % px
        assert BT - 0.01 <= py <= BB + 0.01, "panel B point outside y: %r" % py
    assert b_right <= BR - 12.0, \
        "panel B's rectangles reach %r, too close to the frame %r" \
        % (b_right, BR)

    # ---- legend character budget --------------------------------------
    for t in a_leg:
        assert len(t) <= 90, "legend line too long (%d): %r" % (len(t), t)
    longest = max(a_leg, key=len)
    end_x = AL + 24.0 + 6.6 * len(longest)
    assert end_x <= AR, \
        "the longest legend line ends at %r, outside the frame %r" \
        % (end_x, AR)

    return a, b


if __name__ == "__main__":
    a, b = build()
    both = a + b
    for bad in ("fill=", "stroke=", "font-size=", "var(--", "style="):
        assert bad not in both, "presentation attribute leaked: " + bad
    import re
    classes = set()
    for m in re.finditer(r'class="([^"]+)"', both):
        classes.update(m.group(1).split())
    bare = sorted(c for c in classes if not c.endswith("152"))
    assert bare == ["lab"], "bare classes: %r" % bare
    print("panel A %d bytes, panel B %d bytes" % (len(a), len(b)))
    print("classes: %s" % ", ".join(sorted(classes)))
    print("panel B rectangles end at x = %.2f, frame at %.0f"
          % (panel_b()[2], BR))
    print("longest legend line: %d chars" % max(len(t) for t in
                                                panel_a()[2]))
    print("min at (%.2f, %.2f) px" % (ax(W_STAR), ay(P_STAR)))
    print("all figure assertions passed")
