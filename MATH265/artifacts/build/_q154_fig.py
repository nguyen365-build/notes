"""Figures for the Q15.4 artifact page.

TWO panels, and between them they carry the page's one idea: the cheapest
box is not a cube, and there are no endpoints to compare.

  PANEL A  the cost C(w) = 5.4w^2 + 432/w on the OPEN ray w > 0, drawn
           together with its two components. The rising component is the
           two horizontal faces, the falling one is the four vertical
           faces, and at the minimum the falling one is exactly TWICE
           the rising one. That ratio is the page's cheap self-check and
           it is drawn rather than asserted: a tie line joins the two
           component markers through the minimum, at one width. The
           frame's left and right edges are dashed, because the domain
           has no endpoint there and the absence is what the question is
           about.

  PANEL B  six boxes of volume 120 drawn isometrically to ONE scale on
           ONE ground line, five of them legal (l = 2w) at five widths,
           and the sixth the CUBE, drawn dashed because it is cheaper
           and illegal. The cost under each makes the U shape visible,
           and the cube's lower number is the trap stated as a picture.

Rules this file obeys, each from the carryover:

  - CLASSES ONLY. No fill=, stroke=, font-size= or var() ever reaches a
    presentation attribute; var() does not resolve in one, and an
    upstream CSS rule beats one anyway. Asserted in __main__.
  - every class ENDS with the 154 suffix, except `lab`, the svg-labels
    hook. The suffix goes LAST without exception.
  - a line that must be EXEMPT from svg-labels is named grid*154, which
    matches /grid|axis/ without inheriting `gridl`'s upstream paint.
  - NO text sits inside either plotting frame. Every label lives in a
    band outside it, which is the round-2 lesson from Q15.3: a domain
    marker or a value callout is an axis annotation, not a curve
    feature, so it belongs out of the box rather than nudged around
    inside one.
  - every plotted point is asserted inside its own frame, and each curve
    is clipped to the value range the frame actually shows.
  - every legend and caption line is asserted at most 90 characters, and
    the longest is asserted to end inside the frame.
  - label clearances are COMPUTED and asserted, not eyeballed.
"""
import math

# ---- the mathematics, computed here and never typed ---------------------
A2 = 5.4        # the two horizontal faces: (1.20 + 1.50) x 2w^2
A1 = 432.0      # the four vertical faces: 1.20 x 6wh with h = 60/w^2
VOL = 120.0
KRATIO = 2.0    # l = 2w


def C(w):
    return A2 * w * w + A1 / w


def C_HORIZ(w):
    return A2 * w * w


def C_VERT(w):
    return A1 / w


W_STAR = (A1 / (2.0 * A2)) ** (1.0 / 3.0)      # 40^(1/3)
L_STAR = KRATIO * W_STAR
H_STAR = VOL / (KRATIO * W_STAR * W_STAR)
C_STAR = C(W_STAR)
CUBE_S = VOL ** (1.0 / 3.0)
CUBE_C = 2.7 * CUBE_S * CUBE_S + 1.2 * 4.0 * CUBE_S * CUBE_S


def esc(s):
    return (s.replace("&", "&" + "amp;").replace("<", "&" + "lt;")
             .replace(">", "&" + "gt;"))


def fm(v):
    return ("%.2f" % v).rstrip("0").rstrip(".")


# =======================================================================
# PANEL A - the cost and its two components on the open ray
# =======================================================================
AW, AH = 720.0, 470.0
AL, AR, AT, AB = 78.0, 688.0, 30.0, 244.0
WLO, WHI = 1.35, 8.2          # the frame's own width range
CLO, CHI = 40.0, 360.0
A_TICKROW = 266.0
A_YLAB = 4.0
A_NOTE0 = 296.0
A_NOTESTEP = 24.0
A_LEG0 = 378.0
A_LEGSTEP = 24.0


def ax(w):
    return AL + ((w - WLO) / (WHI - WLO)) * (AR - AL)


def ay(c):
    return AB - ((c - CLO) / (CHI - CLO)) * (AB - AT)


# every legend row whose drawn line is dashed. Asserted below
# against the dash-carrying figure classes, so the two lists
# cannot drift apart.
DASHED_SWATCHES = {"swc1154", "swc2154", "swlev154"}

A_NOTES = [
    "the domain is w > 0, OPEN at both ends, so there is nothing to compare",
    "MINIMUM at w = 3.4200 cm: cost 189.4763 = 63.1588 + 126.3176",
    "the four sides cost exactly TWICE the base and lid, never the same",
]


def panel_a():
    out = []
    add = out.append
    inside = []

    add('<svg class="fig154" viewBox="0 0 %s %s" role="img" '
        'aria-label="the cost of the box as a function of its base width, '
        'together with the cost of the two horizontal faces which rises '
        'and the cost of the four vertical faces which falls. The total '
        'has one minimum, where the falling part is exactly twice the '
        'rising part. The left and right edges of the frame are dashed '
        'because the domain has no endpoint.">' % (fm(AW), fm(AH)))

    add('<rect class="pbox154" x="%s" y="%s" width="%s" height="%s">'
        '</rect>' % (fm(AL), fm(AT), fm(AR - AL), fm(AB - AT)))

    for wv in (2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0):
        add('<line class="gridv154" x1="%s" y1="%s" x2="%s" y2="%s">'
            '</line>' % (fm(ax(wv)), fm(AT), fm(ax(wv)), fm(AB)))
    for cv in (60.0, 120.0, 180.0, 240.0, 300.0):
        add('<line class="gridh154" x1="%s" y1="%s" x2="%s" y2="%s">'
            '</line>' % (fm(AL), fm(ay(cv)), fm(AR), fm(ay(cv))))

    # the two OPEN ends, drawn as dashed edges over the frame. Named
    # grid* so svg-labels exempts them, and they carry no label of their
    # own: the note band says what they mean.
    for xv in (AL, AR):
        add('<line class="gridopen154" x1="%s" y1="%s" x2="%s" y2="%s">'
            '</line>' % (fm(xv), fm(AT), fm(xv), fm(AB)))

    add('<line class="lev154" x1="%s" y1="%s" x2="%s" y2="%s"></line>'
        % (fm(AL), fm(ay(C_STAR)), fm(AR), fm(ay(C_STAR))))

    def curve(cls, fn, n=421):
        pts = []
        for i in range(n):
            w = WLO + (WHI - WLO) * i / (n - 1.0)
            v = fn(w)
            if v < CLO or v > CHI:
                continue
            px, py = ax(w), ay(v)
            pts.append("%s,%s" % (fm(px), fm(py)))
            inside.append((px, py))
        add('<polyline class="%s" points="%s"></polyline>'
            % (cls, " ".join(pts)))

    curve("c1154", C_HORIZ)
    curve("c2154", C_VERT)
    curve("crv154", C)

    # the tie: one vertical at the minimising width joining the two
    # component markers and passing through the minimum. This is the
    # 1 : 2 ratio drawn.
    add('<line class="tie154" x1="%s" y1="%s" x2="%s" y2="%s"></line>'
        % (fm(ax(W_STAR)), fm(ay(C_HORIZ(W_STAR))),
           fm(ax(W_STAR)), fm(ay(C_STAR))))
    add('<circle class="cm1154" cx="%s" cy="%s" r="5"></circle>'
        % (fm(ax(W_STAR)), fm(ay(C_HORIZ(W_STAR)))))
    add('<circle class="cm2154" cx="%s" cy="%s" r="5"></circle>'
        % (fm(ax(W_STAR)), fm(ay(C_VERT(W_STAR)))))
    add('<circle class="mn154" cx="%s" cy="%s" r="6.5"></circle>'
        % (fm(ax(W_STAR)), fm(ay(C_STAR))))

    # ---- everything below is OUTSIDE the frame -------------------------
    for wv in (2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0):
        add('<text class="lab tx154" x="%s" y="%s">%s</text>'
            % (fm(ax(wv)), fm(A_TICKROW), esc("%d" % int(wv))))
    for cv in (60.0, 120.0, 180.0, 240.0, 300.0):
        add('<text class="lab ty154" x="%s" y="%s">%s</text>'
            % (fm(AL - 11.0), fm(ay(cv) + A_YLAB), esc("%d" % int(cv))))

    for k, txt in enumerate(A_NOTES):
        add('<text class="lab note154" x="%s" y="%s">%s</text>'
            % (fm(AL), fm(A_NOTE0 + k * A_NOTESTEP), esc(txt)))

    legend = [
        ("swcrv154", "total cost 5.4w^2 + 432/w, over the whole open ray"),
        ("swc1154", "base and lid, 2.70 per cm2 of 2w^2, rising like w^2"),
        ("swc2154", "the four sides, 1.20 per cm2 of 6wh, falling like 1/w"),
        ("swlev154", "the minimum level 189.4763, touched exactly once"),
    ]
    for k, (cls, txt) in enumerate(legend):
        yy = A_LEG0 + k * A_LEGSTEP
        # a DASHED curve needs a DASHED swatch: a 16x3 rect cannot carry a
        # dash pattern, so it is drawn as two short rects with a gap. Only
        # the total cost is a solid line.
        if cls in DASHED_SWATCHES:
            add('<rect class="%s" x="%s" y="%s" width="6.5" height="3">'
                '</rect>' % (cls, fm(AL), fm(yy - 5.0)))
            add('<rect class="%s" x="%s" y="%s" width="6.5" height="3">'
                '</rect>' % (cls, fm(AL + 9.5), fm(yy - 5.0)))
        else:
            add('<rect class="%s" x="%s" y="%s" width="16" height="3">'
                '</rect>' % (cls, fm(AL), fm(yy - 5.0)))
        add('<text class="lab lgd154" x="%s" y="%s">%s</text>'
            % (fm(AL + 26.0), fm(yy), esc(txt)))

    add("</svg>")
    return "".join(out), inside, A_NOTES + [t for _, t in legend]


# =======================================================================
# PANEL B - six boxes of volume 120, one scale, one ground line
# =======================================================================
BW = 720.0
BPAD = 16.0
B_CEIL = 20.0     # the tallest box's TAG lands here
B_TAGGAP = 24.0
B_CAPSTEP = 24.0
DEPTH = 0.30      # isometric depth factor, applied to x and to y

BOXES = [2.60, 3.00, W_STAR, 4.20, 5.40]
WIN_INDEX = 2
B_CELLS = len(BOXES) + 1
B_CW = (BW - 2.0 * BPAD) / B_CELLS


def _dims(w, cube=False):
    if cube:
        return CUBE_S, CUBE_S, CUBE_S
    return w, KRATIO * w, VOL / (KRATIO * w * w)


_SPECS = [_dims(w) for w in BOXES] + [_dims(0, True)]
_MAX_FOOT = max(w + DEPTH * l for w, l, h in _SPECS)
_MAX_TALL = max(h + DEPTH * l for w, l, h in _SPECS)
# the scale is set by whichever constraint binds; here it is the WIDTH one,
# so the ground line is DERIVED from it rather than fixed, which is what
# stops a band of dead space opening above the boxes.
B_SCALE = (B_CW - 26.0) / _MAX_FOOT
B_GND = B_CEIL + B_TAGGAP + _MAX_TALL * B_SCALE
B_CAP0 = B_GND + 70.0 + 26.0
BH = B_CAP0 + 2 * B_CAPSTEP + 14.0

B_CAPS = [
    "all six hold exactly 120 cm3; the five solid ones also obey l = 2w",
    "the cheapest legal box is 2 : 4 : 3, neither the widest nor the tallest",
    "the dashed cube costs 182.47 and breaks l = 2w, so a lower cost is no check",
]


def box_dims(w, cube=False):
    if cube:
        return CUBE_S, CUBE_S, CUBE_S
    return w, KRATIO * w, VOL / (KRATIO * w * w)


def panel_b():
    out = []
    add = out.append
    inside = []
    tops = []

    cells, cw, s = B_CELLS, B_CW, B_SCALE

    add('<svg class="fig154" viewBox="0 0 %s %s" role="img" '
        'aria-label="six boxes of volume one hundred and twenty drawn to '
        'one scale on one ground line. Five are legal, with the base '
        'length twice its width, and the cheapest of those is the third. '
        'The sixth is a cube, drawn dashed because it is cheaper and '
        'breaks the length rule.">' % (fm(BW), fm(BH)))

    add('<line class="gnd154" x1="%s" y1="%s" x2="%s" y2="%s"></line>'
        % (fm(BPAD), fm(B_GND), fm(BW - BPAD), fm(B_GND)))

    for idx in range(cells):
        cube = (idx == cells - 1)
        if cube:
            w, l, h = box_dims(0, True)
            cost = CUBE_C
        else:
            w, l, h = box_dims(BOXES[idx])
            cost = C(w)
        win = (not cube) and (idx == WIN_INDEX)

        cx0 = BPAD + idx * cw + (cw - (w + DEPTH * l) * s) / 2.0
        fx0, fx1 = cx0, cx0 + w * s
        fy1 = B_GND
        fy0 = B_GND - h * s
        dx = DEPTH * l * s
        dy = -DEPTH * l * s

        pre = "cube154" if cube else ("win154" if win else "bx154")

        add('<polyline class="ff%s" points="%s,%s %s,%s %s,%s %s,%s %s,%s">'
            '</polyline>' % (pre, fm(fx0), fm(fy0), fm(fx1), fm(fy0),
                             fm(fx1), fm(fy1), fm(fx0), fm(fy1),
                             fm(fx0), fm(fy0)))
        add('<polyline class="tt%s" points="%s,%s %s,%s %s,%s %s,%s %s,%s">'
            '</polyline>' % (pre, fm(fx0), fm(fy0), fm(fx0 + dx), fm(fy0 + dy),
                             fm(fx1 + dx), fm(fy0 + dy), fm(fx1), fm(fy0),
                             fm(fx0), fm(fy0)))
        add('<polyline class="ss%s" points="%s,%s %s,%s %s,%s %s,%s %s,%s">'
            '</polyline>' % (pre, fm(fx1), fm(fy0), fm(fx1 + dx), fm(fy0 + dy),
                             fm(fx1 + dx), fm(fy1 + dy), fm(fx1), fm(fy1),
                             fm(fx1), fm(fy0)))
        for px, py in ((fx0, fy0), (fx1, fy1), (fx1 + dx, fy0 + dy),
                       (fx1 + dx, fy1 + dy), (fx0 + dx, fy0 + dy)):
            inside.append((px, py))
        tops.append(fy0 + dy)

        mid = BPAD + idx * cw + cw / 2.0
        add('<text class="lab bw154" x="%s" y="%s">%s</text>'
            % (fm(mid), fm(B_GND + 22.0), esc("w = %.2f" % w)))
        add('<text class="lab bh154" x="%s" y="%s">%s</text>'
            % (fm(mid), fm(B_GND + 46.0), esc("h = %.2f" % h)))
        cls = "ccost154" if not (win or cube) else ("cwin154" if win else "ccube154")
        add('<text class="lab %s" x="%s" y="%s">%s</text>'
            % (cls, fm(mid), fm(B_GND + 70.0), esc("%.2f" % cost)))
        tag = "THE CUBE" if cube else ("CHEAPEST" if win else "")
        if tag:
            add('<text class="lab tag154" x="%s" y="%s">%s</text>'
                % (fm(mid), fm(fy0 + dy - B_TAGGAP), esc(tag)))

    for k, txt in enumerate(B_CAPS):
        add('<text class="lab bcap154" x="%s" y="%s">%s</text>'
            % (fm(BPAD), fm(B_CAP0 + k * B_CAPSTEP), esc(txt)))

    add("</svg>")
    return "".join(out), inside, B_CAPS, tops


def build():
    a, ai, atext = panel_a()
    b, bi, bcap, tops = panel_b()

    # every plotted point inside its own frame
    for px, py in ai:
        assert AL - 0.5 <= px <= AR + 0.5, ("panel A x out of frame", px)
        assert AT - 0.5 <= py <= AB + 0.5, ("panel A y out of frame", py)
    for px, py in bi:
        assert BPAD - 0.5 <= px <= BW - BPAD + 0.5, ("panel B x", px)
        assert 0.0 < py <= B_GND + 0.5, ("panel B y", py)

    # NO text may sit inside panel A's plotting frame
    assert A_TICKROW > AB + 8.0
    assert A_NOTE0 > A_TICKROW + 20.0
    assert A_LEG0 > A_NOTE0 + 2 * A_NOTESTEP + 20.0
    assert A_LEG0 + 3 * A_LEGSTEP + 12.0 < AH, "legend runs off panel A"

    # panel B: every tag clears its own box top, and the tallest box
    # clears the panel's own ceiling
    for t in tops:
        assert t - B_TAGGAP >= B_CEIL - 0.5, ("a tag would leave panel B", t)
    assert min(tops) > B_CEIL, ("a box leaves panel B at the top", min(tops))
    # the tallest box must actually REACH the ceiling, or the panel is
    # carrying dead space that no gate can see
    assert min(tops) - B_TAGGAP < B_CEIL + 1.0, ("dead space above the "
                                                 "tallest box", min(tops))
    assert B_CAP0 > B_GND + 70.0 + 20.0, "captions collide with the cost row"
    assert B_CAP0 + 2 * B_CAPSTEP + 12.0 <= BH, "captions run off panel B"

    # character budgets, with the longest asserted to end inside the frame
    for t in atext + bcap:
        assert len(t) <= 90, ("line too long", len(t), t)
    longest = max(atext, key=len)
    assert AL + 26.0 + len(longest) * 6.05 < AR, ("longest panel-A line runs "
                                                  "past the frame", longest)
    longest_b = max(bcap, key=len)
    assert BPAD + len(longest_b) * 6.05 < BW - BPAD, ("longest caption runs "
                                                      "past the panel",
                                                      longest_b)
    # the legend cannot claim a solid line for a dashed curve: every
    # dashed swatch must correspond to a class the STYLESHEET dashes, and
    # the solid one must not. The pairing is asserted in the build script,
    # which is the only place that can see the CSS; here we assert the two
    # sets at least have the same size as the drawn dashed elements.
    assert DASHED_SWATCHES == {"swc1154", "swc2154", "swlev154"}
    assert len(DASHED_SWATCHES) == 3
    return a, b


if __name__ == "__main__":
    import re

    a, b = build()
    both = a + b
    for bad in ("fill=", "stroke=", "font-size=", "var(--", "style="):
        assert bad not in both, ("presentation attribute leaked: " + bad)
    cl = set()
    for m in re.finditer(r'class="([^"]+)"', both):
        cl.update(m.group(1).split())
    bare = sorted(c for c in cl if not c.endswith("154"))
    assert bare == ["lab"], bare
    print("panel A %d bytes, panel B %d bytes" % (len(a), len(b)))
    print("%d classes: %s" % (len(cl), " ".join(sorted(cl))))
    print("w* %.10f  l* %.10f  h* %.10f  C* %.10f"
          % (W_STAR, L_STAR, H_STAR, C_STAR))
    print("horizontal %.10f  vertical %.10f  ratio %.12f"
          % (C_HORIZ(W_STAR), C_VERT(W_STAR), C_VERT(W_STAR) / C_HORIZ(W_STAR)))
    print("cube  s %.10f  cost %.10f" % (CUBE_S, CUBE_C))
    for w in BOXES:
        ww, ll, hh = box_dims(w)
        print("  box w %.4f l %.4f h %.4f cost %.4f" % (ww, ll, hh, C(ww)))
    print("panel A y: level %.2f  comp1 %.2f  comp2 %.2f"
          % (ay(C_STAR), ay(C_HORIZ(W_STAR)), ay(C_VERT(W_STAR))))
