"""Figures for the Q15.3 artifact page.

TWO panels, and between them they carry the page's one idea: the theorem
guarantees that the extremes EXIST and says nothing about where.

  PANEL A  f(x) = 1/(x^2+1) on [-1,1] and NOWHERE ELSE, with the three
           candidates marked and a dashed level line at y = 1/2 running
           the width of the frame. The two minimum markers sit at the
           SAME height at the two ends of the interval, which is the
           run's headline finding drawn rather than asserted: the
           minimum happens twice, so each endpoint is its twin's backup
           and neither omission can be caught from the answer.

  PANEL B  THREE sub-panels, each the SAME function with exactly ONE of
           the theorem's hypotheses dropped, and each losing exactly one
           extreme. A hollow marker is an extreme that is approached and
           never attained; a filled one is attained.

Rules this file obeys, each from the carryover:

  - CLASSES ONLY. No fill=, stroke=, font-size= or var() ever reaches a
    presentation attribute; var() does not resolve in one, and an
    upstream CSS rule beats one anyway. Asserted in __main__.
  - every class ENDS with the 153 suffix, except `lab`, the svg-labels
    hook. The suffix goes LAST without exception.
  - a line that must be EXEMPT from svg-labels is named grid*153, which
    matches /grid|axis/ without inheriting `gridl`'s upstream paint.
  - the curve is plotted over the INTERVAL, never the padded range, and
    every plotted point is asserted inside the panel frame.
  - every legend line is asserted at most 90 characters after entity
    decoding, and the longest is asserted to end inside the frame.
"""
import math

# ---- the mathematics, computed here and nowhere typed -------------------
A_LO, A_HI = -1.0, 1.0


def F(x):
    return 1.0 / (x * x + 1.0)


F_MAX = F(0.0)                      # 1
F_MIN = F(1.0)                      # 1/2
X_INFL = 1.0 / math.sqrt(3.0)       # 0.5773502692
F_INFL = F(X_INFL)                  # 3/4


def esc(s):
    return (s.replace("&", "&" + "amp;").replace("<", "&" + "lt;")
             .replace(">", "&" + "gt;"))


def fm(v):
    """Trim a float for an SVG coordinate."""
    return ("%.2f" % v).rstrip("0").rstrip(".")


# =======================================================================
# PANEL A - the exam question, drawn only on its own interval
# =======================================================================
AW, AH = 720.0, 408.0
AL, AR, AT, AB = 86.0, 690.0, 26.0, 246.0
# the PADDED coordinate range, so the endpoint markers are not on the
# frame; the CURVE is still plotted only on [-1,1].
PX = 1.18
Y0, Y1 = 0.40, 1.15   # 1.07 left only 23px of headroom above the crown,
                      # so the MAX callout could not clear the curve
A_TICKROW = 282.0    # moved down 16px: the interval bar now sits
                     # in the band between the frame and the ticks
A_YLAB = 4.0
A_IVLROW = 254.0     # the interval bar, OUTSIDE the plotting box
A_LEG0 = 317.0       # 35px below the tick baseline
A_LEGSTEP = 22.0


def ax(x):
    return AL + ((x + PX) / (2.0 * PX)) * (AR - AL)


def ay(y):
    return AB - ((y - Y0) / (Y1 - Y0)) * (AB - AT)


def panel_a():
    out = []
    add = out.append
    inside = []

    add('<svg class="fig153" viewBox="0 0 %s %s" role="img" '
        'aria-label="one over x squared plus one, drawn only on the '
        'closed interval from minus one to one, with its maximum marked '
        'at the interior point zero and its minimum marked at both '
        'endpoints at the same height">' % (fm(AW), fm(AH)))

    add('<rect class="pbox153" x="%s" y="%s" width="%s" height="%s">'
        '</rect>' % (fm(AL), fm(AT), fm(AR - AL), fm(AB - AT)))

    for xv in (-1.0, -0.5, 0.0, 0.5, 1.0):
        add('<line class="gridv153" x1="%s" y1="%s" x2="%s" y2="%s">'
            '</line>' % (fm(ax(xv)), fm(AT), fm(ax(xv)), fm(AB)))
    for yv in (0.5, 0.75, 1.0):
        add('<line class="gridh153" x1="%s" y1="%s" x2="%s" y2="%s">'
            '</line>' % (fm(AL), fm(ay(yv)), fm(AR), fm(ay(yv))))

    # the interval, as a heavy bar in the band BETWEEN the frame and
    # the tick row, so the domain is a drawn object rather than an
    # implication. It was first drawn ON the frame floor, where
    # svg-labels correctly reported it crossing all three of the MIN
    # callouts; a domain marker is an axis annotation, not a curve
    # feature, so moving it out of the plotting box is the fix rather
    # than nudging the labels.
    add('<line class="ivl153" x1="%s" y1="%s" x2="%s" y2="%s"></line>'
        % (fm(ax(A_LO)), fm(A_IVLROW), fm(ax(A_HI)), fm(A_IVLROW)))

    # the minimum level, all the way across, which is what makes the tie
    # visible rather than inferable
    add('<line class="lev153" x1="%s" y1="%s" x2="%s" y2="%s"></line>'
        % (fm(AL), fm(ay(F_MIN)), fm(AR), fm(ay(F_MIN))))

    # the curve, on [-1,1] ONLY
    pts = []
    N = 361
    for i in range(N):
        x = A_LO + (A_HI - A_LO) * i / (N - 1)
        px, py = ax(x), ay(F(x))
        pts.append("%s,%s" % (fm(px), fm(py)))
        inside.append((px, py))
    add('<polyline class="crv153" points="%s"></polyline>' % " ".join(pts))

    # the same function OUTSIDE the interval, drawn faintly, so it is
    # clear the interval is a choice and not where the function stops
    for lo, hi in ((-PX, A_LO), (A_HI, PX)):
        gp = []
        for i in range(61):
            x = lo + (hi - lo) * i / 60.0
            gp.append("%s,%s" % (fm(ax(x)), fm(ay(F(x)))))
        add('<polyline class="ghost153" points="%s"></polyline>'
            % " ".join(gp))

    # inflection ticks at 3/4, which is where the curve stops steepening
    for xv in (-X_INFL, X_INFL):
        add('<line class="inf153" x1="%s" y1="%s" x2="%s" y2="%s"></line>'
            % (fm(ax(xv)), fm(ay(F_INFL) - 7.0), fm(ax(xv)),
               fm(ay(F_INFL) + 7.0)))

    # the three candidates
    add('<circle class="mx153" cx="%s" cy="%s" r="6.5"></circle>'
        % (fm(ax(0.0)), fm(ay(F_MAX))))
    for xv in (A_LO, A_HI):
        add('<circle class="mn153" cx="%s" cy="%s" r="6.5"></circle>'
            % (fm(ax(xv)), fm(ay(F_MIN))))

    # callout for the maximum, CENTRED ABOVE the crown. Placed to the
    # RIGHT at the crown's own height it ran straight through the curve,
    # because f is nearly horizontal near a smooth maximum - a real
    # svg-labels finding on this exact page. The offset is 26px, and the
    # curve under the label's whole x span stays 22px below its box.
    add('<text class="lab labmx153" x="%s" y="%s">%s</text>'
        % (fm(ax(0.0)), fm(ay(F_MAX) - 26.0),
           esc("MAX  f(0) = 1   an INTERIOR critical point")))

    # callouts for the two minima, one left one right, BELOW the level
    add('<text class="lab labl153" x="%s" y="%s">%s</text>'
        % (fm(ax(A_LO) + 12.0), fm(ay(F_MIN) + 24.0),
           esc("MIN  f(-1) = 1/2")))
    add('<text class="lab labr153" x="%s" y="%s">%s</text>'
        % (fm(ax(A_HI) - 12.0), fm(ay(F_MIN) + 24.0),
           esc("MIN  f(1) = 1/2")))
    add('<text class="lab labtie153" x="%s" y="%s">%s</text>'
        % (fm(0.5 * (AL + AR)), fm(ay(F_MIN) + 24.0),
           esc("the SAME value, at BOTH ends")))

    # x ticks
    for xv, tx in ((-1.0, "-1"), (-0.5, "-1/2"), (0.0, "0"),
                   (0.5, "1/2"), (1.0, "1")):
        add('<text class="lab tx153" x="%s" y="%s">%s</text>'
            % (fm(ax(xv)), fm(A_TICKROW), esc(tx)))
    # y ticks
    for yv, ty in ((0.5, "1/2"), (0.75, "3/4"), (1.0, "1")):
        add('<text class="lab ty153" x="%s" y="%s">%s</text>'
            % (fm(AL - 12.0), fm(ay(yv) + A_YLAB), esc(ty)))

    legend = [
        ("swcrv153", "f(x) = 1/(x^2+1), plotted ONLY on the interval"),
        ("swghost153", "the same f outside [-1,1] - the interval is a choice"),
        ("swlev153", "the minimum level 1/2, reached at BOTH endpoints"),
        ("swinf153", "inflection at x = +-1/sqrt3, where f = 3/4"),
    ]
    for k, (cls, txt) in enumerate(legend):
        yy = A_LEG0 + k * A_LEGSTEP
        if cls == "swlev153":
            add('<rect class="%s" x="%s" y="%s" width="6.5" height="3">'
                '</rect>' % (cls, fm(AL), fm(yy - 5.0)))
            add('<rect class="%s" x="%s" y="%s" width="6.5" height="3">'
                '</rect>' % (cls, fm(AL + 9.5), fm(yy - 5.0)))
        else:
            add('<rect class="%s" x="%s" y="%s" width="16" height="3">'
                '</rect>' % (cls, fm(AL), fm(yy - 5.0)))
        add('<text class="lab lgd153" x="%s" y="%s">%s</text>'
            % (fm(AL + 26.0), fm(yy), esc(txt)))

    add("</svg>")
    return "".join(out), inside, [t for _, t in legend]


# =======================================================================
# PANEL B - one hypothesis dropped per sub-panel
# =======================================================================
BW, BH = 720.0, 300.0
BPAD = 14.0
BCOLS = 3
BSW = (BW - 2.0 * BPAD - 2.0 * 18.0) / BCOLS      # sub-panel width
BT, BB = 52.0, 214.0
B_TITLE = 34.0
B_CAP0 = 240.0
B_CAPSTEP = 19.0


def panel_b():
    out = []
    add = out.append
    inside = []

    add('<svg class="fig153" viewBox="0 0 %s %s" role="img" '
        'aria-label="three sub-panels, each the same function with one '
        'of the theorem hypotheses dropped: an open interval loses the '
        'minimum, an unbounded interval loses the minimum by a limit at '
        'infinity, and a puncture at the peak loses the maximum. A '
        'hollow marker is an extreme that is never attained.">'
        % (fm(BW), fm(BH)))

    CASES = [
        # label, x range plotted, hypothesis dropped, caption lines
        ("(-1, 1)  OPEN", "closed",
         ["min 1/2 LOST", "the minimisers WERE", "the endpoints"]),
        ("[0, inf)  UNBOUNDED", "bounded",
         ["inf 0 LOST", "a limit at infinity,", "never a value"]),
        ("[-1,1], h(0) = 1/2", "continuous",
         ["max 1 LOST", "the peak is punctured,", "so 1 is approached"]),
    ]

    for ci, (title, dropped, cap) in enumerate(CASES):
        x0 = BPAD + ci * (BSW + 18.0)
        x1 = x0 + BSW

        def sx(t, lo, hi, x0=x0, x1=x1):
            return x0 + ((t - lo) / (hi - lo)) * (x1 - x0)

        def sy(v):
            # padded BELOW zero, so a level line at v=0 (sub-panel 2's
            # infimum) does not land exactly on the frame's bottom edge,
            # where it was indistinguishable from the border.
            return BB - ((v + 0.10) / 1.22) * (BB - BT)

        add('<rect class="pbox153" x="%s" y="%s" width="%s" '
            'height="%s"></rect>'
            % (fm(x0), fm(BT), fm(x1 - x0), fm(BB - BT)))
        add('<text class="lab sub153" x="%s" y="%s">%s</text>'
            % (fm(x0), fm(B_TITLE), esc(title)))

        if ci == 0:
            lo, hi = -1.30, 1.30
            pts = []
            for i in range(121):
                t = -1.0 + 2.0 * i / 120.0
                px, py = sx(t, lo, hi), sy(F(t))
                pts.append("%s,%s" % (fm(px), fm(py)))
                inside.append((px, py))
            add('<polyline class="crv153" points="%s"></polyline>'
                % " ".join(pts))
            add('<line class="lev153" x1="%s" y1="%s" x2="%s" y2="%s">'
                '</line>' % (fm(x0), fm(sy(0.5)), fm(x1), fm(sy(0.5))))
            add('<circle class="mx153" cx="%s" cy="%s" r="5.5"></circle>'
                % (fm(sx(0.0, lo, hi)), fm(sy(1.0))))
            for t in (-1.0, 1.0):
                add('<circle class="opn153" cx="%s" cy="%s" r="5.5">'
                    '</circle>' % (fm(sx(t, lo, hi)), fm(sy(0.5))))
        elif ci == 1:
            # widened from -0.35: at that padding the marker at x=0 sat
            # half outside the frame's left edge.
            lo, hi = -0.62, 6.4
            pts = []
            for i in range(181):
                t = 0.0 + 6.0 * i / 180.0
                px, py = sx(t, lo, hi), sy(F(t))
                pts.append("%s,%s" % (fm(px), fm(py)))
                inside.append((px, py))
            add('<polyline class="crv153" points="%s"></polyline>'
                % " ".join(pts))
            add('<line class="lev153" x1="%s" y1="%s" x2="%s" y2="%s">'
                '</line>' % (fm(x0), fm(sy(0.0)), fm(x1), fm(sy(0.0))))
            add('<circle class="mx153" cx="%s" cy="%s" r="5.5"></circle>'
                % (fm(sx(0.0, lo, hi)), fm(sy(1.0))))
            add('<circle class="opn153" cx="%s" cy="%s" r="5.5"></circle>'
                % (fm(x1 - 16.0), fm(sy(0.0))))
            add('<text class="lab arw153" x="%s" y="%s">%s</text>'
                % (fm(x1 - 38.0), fm(sy(0.0) - 14.0), esc("to 0")))
        else:
            lo, hi = -1.30, 1.30
            for seg in ((-1.0, -0.012), (0.012, 1.0)):
                pts = []
                for i in range(61):
                    t = seg[0] + (seg[1] - seg[0]) * i / 60.0
                    px, py = sx(t, lo, hi), sy(F(t))
                    pts.append("%s,%s" % (fm(px), fm(py)))
                    inside.append((px, py))
                add('<polyline class="crv153" points="%s"></polyline>'
                    % " ".join(pts))
            add('<line class="lev153" x1="%s" y1="%s" x2="%s" y2="%s">'
                '</line>' % (fm(x0), fm(sy(0.5)), fm(x1), fm(sy(0.5))))
            add('<circle class="opn153" cx="%s" cy="%s" r="5.5"></circle>'
                % (fm(sx(0.0, lo, hi)), fm(sy(1.0))))
            for t in (-1.0, 0.0, 1.0):
                add('<circle class="mn153" cx="%s" cy="%s" r="5.5">'
                    '</circle>' % (fm(sx(t, lo, hi)), fm(sy(0.5))))

        for k, line in enumerate(cap):
            add('<text class="lab cap153" x="%s" y="%s">%s</text>'
                % (fm(x0), fm(B_CAP0 + k * B_CAPSTEP), esc(line)))

    add("</svg>")
    return "".join(out), inside


def build():
    a, ia, leg = panel_a()
    b, ib = panel_b()
    return a, b


if __name__ == "__main__":
    a, ia, leg = panel_a()
    b, ib = panel_b()
    both = a + b

    for bad in ("fill=", "stroke=", "font-size=", "var(--", "style="):
        assert bad not in both, "presentation attribute leaked: " + bad

    classes = set()
    import re
    for m in re.finditer(r'class="([^"]+)"', both):
        classes.update(m.group(1).split())
    bare = sorted(c for c in classes if not c.endswith("153"))
    assert bare == ["lab"], "bare classes: %r" % bare
    for c in classes:
        if c.startswith("grid"):
            assert re.search(r"grid|axis", c), c
    assert "gridl" not in classes and "axis" not in classes

    # every plotted point inside its frame
    for px, py in ia:
        assert AL - 0.5 <= px <= AR + 0.5, "panel A x out of frame: %f" % px
        assert AT - 0.5 <= py <= AB + 0.5, "panel A y out of frame: %f" % py
    for px, py in ib:
        assert BPAD - 0.5 <= px <= BW - BPAD + 0.5, \
            "panel B x out of frame: %f" % px
        assert BT - 0.5 <= py <= BB + 0.5, "panel B y out of frame: %f" % py

    # legend character budget
    for t in leg:
        assert len(t) <= 90, "legend line over 90 chars: %d" % len(t)
    longest = max(leg, key=len)
    end_x = AL + 26.0 + len(longest) * 6.1
    assert end_x < AR, "longest legend line ends at %.1f of %.1f" % (end_x, AR)

    print("panel A %d bytes, panel B %d bytes" % (len(a), len(b)))
    print("classes: %d, bare: %r" % (len(classes), bare))
    print("panel A plotted points: %d, all inside the frame" % len(ia))
    print("panel B plotted points: %d, all inside the frame" % len(ib))
    print("longest legend line: %d chars, ends at x=%.1f of %.1f"
          % (len(longest), end_x, AR))
    print("f(0)=%.10f  f(1)=%.10f  1/sqrt3=%.10f  f(1/sqrt3)=%.10f"
          % (F_MAX, F_MIN, X_INFL, F_INFL))
