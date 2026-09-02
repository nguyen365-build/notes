"""Q12.2 figures.

FIG 1, two panels, and the page's whole argument:
  A  THE TWO STEPS, DRAWN TO SCALE.  The tangent at 60 degrees, walked
     pi/90 radians (the correct step, invisible at this scale) and walked
     2 radians (the blunder, which lands 114.6 degrees further on and at a
     height of 1.866 - off the top of a sine's range entirely).
  B  THE ERROR ITSELF, PLOTTED.  The residual L(x) - sin(x) over 59 to 63
     degrees: zero at the anchor, positive on both sides, quadratic.

FIG 2  THE ANCHOR CENSUS.  Nine legal exact anchors, error on a log scale,
     ordered by distance from 62 degrees - so the two bars that break the
     ordering (30 beating 90, 0 beating 120) read as inversions.

Every plotted number is computed here, never typed.

Label policy, from the queue carryover: free-floating callouts beside a
sloped line are crossed as soon as they are long enough, and three
repositionings is the sign to stop.  Both panels therefore carry a LEGEND
in a measured-empty region instead, and the long explanatory sentences live
in the page caption rather than inside the SVG.  Stacked text is spaced 22px.

Class names lab / hd / sm / tk / am / vsn / gridl / axis / curve / dot are
DELIBERATELY the series names, because svg-labels.mjs selects text.lab and
exempts /grid|axis/.  Everything else is page-own and guarded at build time.
"""
import math

D = math.pi / 180.0
A = math.pi / 3.0                       # the anchor, 60 degrees
FA = math.sin(A)
FPA = math.cos(A)
ROW = 22                                # stacked-text spacing, per the carryover


def tang(x):
    return FA + FPA * (x - A)


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def txt(x, y, s, cls="lab", anchor="start"):
    return ('<text class="%s" x="%.1f" y="%.1f" text-anchor="%s">%s</text>'
            % (cls, x, y, anchor, esc(s)))


def legend(x, y, rows):
    """swatch + text rows, 22px apart, no leader lines to be crossed"""
    o = []
    for i, (cls, label) in enumerate(rows):
        yy = y + i * ROW
        if cls.startswith("line:"):
            o.append('<line class="%s" x1="%.1f" y1="%.1f" x2="%.1f" '
                     'y2="%.1f"/>' % (cls[5:], x, yy - 4, x + 16, yy - 4))
        elif cls.startswith("dot:"):
            o.append('<circle class="%s" cx="%.1f" cy="%.1f" r="4.4"/>'
                     % (cls[4:], x + 8, yy - 4))
        elif cls.startswith("box:"):
            o.append('<rect class="%s" x="%.1f" y="%.1f" width="16" '
                     'height="10"/>' % (cls[4:], x, yy - 9))
        o.append(txt(x + 24, yy, label, "lab sm"))
    return "".join(o)


def build():
    W, H = 780, 518
    o = ['<svg viewBox="0 0 %d %d" width="%d" height="%d" '
         'xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="Two panels: the correct radian step and the '
         'unconverted degree step drawn to scale, and the overestimate gap '
         'at 62 degrees">' % (W, H, W, H)]

    # ================= PANEL A =================================
    ax0, ay0, aw, ah = 46, 76, 320, 286
    xa0, xa1 = 0.0, 180.0
    ya0, ya1 = -0.06, 1.99

    def AX(d):
        return ax0 + (d - xa0) / (xa1 - xa0) * aw

    def AY(v):
        return ay0 + ah - (v - ya0) / (ya1 - ya0) * ah

    o.append(txt(ax0, 30, "A / THE TWO STEPS, TO SCALE", "lab hd"))
    o.append(txt(ax0, 30 + ROW, "sin x over 0 to 180 degrees, one tangent",
                 "lab sm"))
    for v in (0.0, 1.0, 2.0):
        if ya0 <= v <= ya1:
            o.append('<line class="gridl" x1="%.1f" y1="%.1f" x2="%.1f" '
                     'y2="%.1f"/>' % (ax0, AY(v), ax0 + aw, AY(v)))
    o.append('<line class="axis" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>'
             % (ax0, AY(0), ax0 + aw, AY(0)))
    o.append('<line class="axis" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>'
             % (ax0, ay0, ax0, ay0 + ah))
    o.append('<polyline class="curve" points="%s"/>'
             % " ".join("%.2f,%.2f" % (AX(d), AY(math.sin(d * D)))
                        for d in [i * 0.5 for i in range(361)]))
    t_lo, t_hi = 22.0, 178.0
    o.append('<line class="tanl122" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>'
             % (AX(t_lo), AY(tang(t_lo * D)), AX(t_hi), AY(tang(t_hi * D))))
    for v, s in [(2.0, "2"), (1.0, "1"), (0.0, "0")]:
        o.append(txt(ax0 - 8, AY(v) + 4, s, "lab tk", "end"))
    for d in (0, 60, 120, 180):
        o.append(txt(AX(d), ay0 + ah + 20, str(d), "lab tk", "middle"))
    o.append(txt(ax0 + aw / 2, ay0 + ah + 20 + ROW, "x IN DEGREES",
                 "lab hd", "middle"))

    o.append('<circle class="dot" cx="%.1f" cy="%.1f" r="4.6"/>'
             % (AX(60), AY(FA)))
    o.append('<circle class="gdot122" cx="%.1f" cy="%.1f" r="3.2"/>'
             % (AX(62), AY(math.sin(62 * D))))
    bad_deg = 60.0 + 2.0 / D
    bad_y = tang(bad_deg * D)
    o.append('<line class="leadr122" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>'
             % (AX(bad_deg), AY(bad_y), AX(bad_deg), AY(math.sin(bad_deg * D))))
    o.append('<circle class="gdot122" cx="%.1f" cy="%.1f" r="3.2"/>'
             % (AX(bad_deg), AY(math.sin(bad_deg * D))))
    o.append('<circle class="bdot122" cx="%.1f" cy="%.1f" r="5.4"/>'
             % (AX(bad_deg), AY(bad_y)))


    # ================= PANEL B =================================
    # The gap at 62 degrees is 5.31e-4 against y values near 0.88, so drawing
    # both curves and hoping to SEE the difference fails: at any zoom that
    # keeps both on screen the gap is thinner than the strokes.  Plot the
    # RESIDUAL instead - L(x) minus sin(x) - which is the honest way to show
    # a quantity three orders of magnitude below the values it comes from,
    # and which teaches more: it is zero at the anchor, positive on BOTH
    # sides (so the overestimate does not depend on the direction of dx),
    # and quadratic.
    bx0, by0, bw, bh = 452, 76, 296, 286
    xb0, xb1 = 59.0, 63.0

    def resid(d):
        return tang(d * D) - math.sin(d * D)

    yb1 = resid(xb1) * 1.10
    yb0 = -yb1 * 0.10

    def BX(d):
        return bx0 + (d - xb0) / (xb1 - xb0) * bw

    def BY(v):
        return by0 + bh - (v - yb0) / (yb1 - yb0) * bh

    o.append(txt(bx0, 30, "B / THE ERROR ITSELF, PLOTTED", "lab hd"))
    o.append(txt(bx0, 30 + ROW, "tangent minus curve, in units of 1e-4",
                 "lab sm"))
    o.append('<line class="axis" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>'
             % (bx0, by0, bx0, by0 + bh))
    o.append('<line class="axis" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>'
             % (bx0, BY(0.0), bx0 + bw, BY(0.0)))
    for d in (59, 60, 61, 62, 63):
        o.append('<line class="gridl" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>'
                 % (BX(d), by0, BX(d), by0 + bh))
        o.append(txt(BX(d), by0 + bh + 20, str(d), "lab tk", "middle"))
    o.append(txt(bx0 + bw / 2, by0 + bh + 20 + ROW, "x IN DEGREES",
                 "lab hd", "middle"))
    for v in (0.0, 5e-4, 10e-4):
        if yb0 <= v <= yb1:
            o.append('<line class="gridl" x1="%.1f" y1="%.1f" x2="%.1f" '
                     'y2="%.1f"/>' % (bx0, BY(v), bx0 + bw, BY(v)))
            o.append(txt(bx0 - 8, BY(v) + 4, "%.0f" % (v * 1e4),
                         "lab tk", "end"))

    n = 200
    xs = [xb0 + i * (xb1 - xb0) / n for i in range(n + 1)]
    o.append('<polygon class="gapfill122" points="%s"/>'
             % " ".join("%.2f,%.2f" % p for p in
                        [(BX(d), BY(resid(d))) for d in xs]
                        + [(BX(xb1), BY(0.0)), (BX(xb0), BY(0.0))]))
    o.append('<polyline class="curve" points="%s"/>'
             % " ".join("%.2f,%.2f" % (BX(d), BY(resid(d))) for d in xs))
    e_est = tang(62 * D)
    e_true = math.sin(62 * D)
    o.append('<line class="gapline122" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>'
             % (BX(62), BY(0.0), BX(62), BY(resid(62))))
    o.append('<circle class="bdot122" cx="%.1f" cy="%.1f" r="4.4"/>'
             % (BX(62), BY(resid(62))))
    o.append('<circle class="dot" cx="%.1f" cy="%.1f" r="4.6"/>'
             % (BX(60), BY(0.0)))

    # ---- SHARED LEGEND STRIP -------------------------------------------
    # svg-labels.mjs measures a <line> by its BOUNDING BOX, and a diagonal's
    # bbox is the whole rectangle it spans - so any label placed inside a
    # panel is reported as crossed no matter where in the wedge it sits.
    # Both tangent bboxes end at y = 351, so the strip goes below that.
    ly = ay0 + ah + 20 + 2 * ROW + 14
    o.append('<line class="gridl" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>'
             % (ax0, ly - 16, W - 32, ly - 16))
    o.append(legend(ax0, ly + 8, [
        ("line:tanl122", "the tangent at 60 degrees, i.e. the estimate"),
        ("line:curve", "sin x, the truth"),
        ("dot:dot", "the anchor, and the correct step of pi/90 rad"),
    ]))
    o.append(legend(bx0, ly + 8, [
        ("dot:bdot122", "a step of 2 rad lands at y = %.3f" % bad_y),
        ("box:gapfill122", "the error at 62 deg is %.2e" % (e_est - e_true)),
        ("", "zero at the anchor, positive both ways"),
    ]))

    o.append("</svg>")
    return "".join(o)


def build_census():
    """FIG 2 - nine legal exact anchors, ordered by distance from 62 deg."""
    tgt = 62 * D
    true = math.sin(tgt)
    rows = []
    for ad in [60, 45, 90, 30, 120, 0, 135, 150, 180]:
        a = ad * D
        err = abs((math.sin(a) + math.cos(a) * (tgt - a)) - true)
        rows.append((ad, abs(ad - 62), err))
    best = min(r[2] for r in rows)

    W, H = 780, 244
    o = ['<svg viewBox="0 0 %d %d" width="%d" height="%d" '
         'xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="Bar chart of the linearization error from nine exact '
         'anchors, ordered by distance from 62 degrees">' % (W, H, W, H)]
    x0, y0, w, h = 108, 78, 624, 96
    o.append(txt(46, 30, "THE ANCHOR CENSUS / ERROR ON A LOG SCALE", "lab hd"))
    o.append(txt(46, 30 + ROW,
                 "ordered by distance from 62 degrees, shown above each bar",
                 "lab sm"))
    lo = math.log10(best)
    hi = math.log10(max(r[2] for r in rows))
    span = hi - lo

    def BH(e):
        return 7 + (math.log10(e) - lo) / span * (h - 7)

    o.append('<line class="axis" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>'
             % (x0 - 10, y0 + h, x0 + w, y0 + h))
    bw = w / len(rows) * 0.54
    for i, (ad, dist, err) in enumerate(rows):
        cx = x0 + (i + 0.5) * w / len(rows)
        bh = BH(err)
        cls = "barbest122" if err == best else "bar122"
        o.append('<rect class="%s" x="%.1f" y="%.1f" width="%.1f" '
                 'height="%.1f" rx="1.5"/>'
                 % (cls, cx - bw / 2, y0 + h - bh, bw, bh))
        o.append(txt(cx, y0 + h - bh - 10, "%d" % dist, "lab sm", "middle"))
        o.append(txt(cx, y0 + h + 20, "%d" % ad, "lab tk", "middle"))
        o.append(txt(cx, y0 + h + 20 + ROW,
                     "best" if err == best else "%dx" % round(err / best),
                     "lab tk", "middle"))
    o.append(txt(x0 - 20, y0 + h + 20, "ANCHOR", "lab hd", "end"))
    o.append(txt(x0 - 20, y0 + h + 20 + ROW, "COST", "lab hd", "end"))
    o.append("</svg>")
    return "".join(o)
