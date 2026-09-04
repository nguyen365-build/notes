"""Figures for the Q19.6 artifact.

Two figures, each drawing a MECHANISM rather than a set of magnitudes.

  fig1  the equal-area rectangle.  T = 3x on [0,6] with the triangle under it
        shaded, and the 6-by-9 rectangle drawn on top.  The two leftover wedges
        are CONGRUENT right triangles of area 13.5 each, and that congruence is
        the whole reason the rectangle has the same area as the triangle.  The
        line crosses the rectangle's top edge at c = 3, which is the Mean Value
        Theorem point.
  fig2  why the endpoint mean coincides here and nowhere else.  Three panels
        on [0,1]: affine, convex, concave.  The chord's mean and the true
        average are drawn as two levels; they land on the same line only in the
        affine panel.

Guards, every one of them because some run in this queue shipped the defect it
catches:
  - BOUNDS      every drawn coordinate inside the viewBox (15.6);
  - CONTAIN     the drawn shaded polygon must actually CONTAIN samples of the
                region it claims to be, with an outside control that is
                rejected (29.9);
  - CONGRUENT   the two leftover wedges must have EQUAL area, computed from the
                drawn polygons by the shoelace formula, not from the data;
  - TICKS       the placer must not move an axis tick, compared at the
                precision the SVG is written at (30.8);
  - COLLIDE     no label overlaps a tick label or another label (27.9);
  - RECTEDGE    svg-labels samples only line/polyline, so a stroked <rect>
                border is a structural blind spot; its four edges become
                segments here and are tested against every label box (30.8);
  - LABELFIT    the widest estimated label box must fit, and the right margin
                must not be mostly empty (30.8);
  - DEADSPACE   the drawn content must fill most of the panel (18.7);
  - CONTENT     every label named in MUST_APPEAR is actually drawn (28.8).
"""
import re as _re

W1, H1 = 760, 412
W2, H2 = 760, 318

LOG = []
SLOPE = 3.0
LEN = 6.0
AVG = 9.0
CPT = 3.0

# ---------------------------------------------------------------- fig 1 frame
PADL, PADR, PADT, PADB = 64, 154, 34, 54
X0, X1 = 0.0, 6.6
Y0, Y1 = 0.0, 19.8


def sx(x):
    return PADL + (x - X0) / (X1 - X0) * (W1 - PADL - PADR)


def sy(y):
    return H1 - PADB - (y - Y0) / (Y1 - Y0) * (H1 - PADT - PADB)


def _fmt(v):
    return ("%.2f" % v).rstrip("0").rstrip(".")


# Estimated label geometry.  svg-labels.mjs does the real getBBox pass in the
# browser; this build-time layer is deliberately generous.
CHW = {10: 6.4, 11: 7.0, 11.5: 7.3, 12: 7.6}


def bbox(text, x, y, size=11, anchor="start"):
    w = len(text) * CHW.get(size, 7.0)
    h = size * 1.25
    if anchor == "middle":
        x -= w / 2.0
    elif anchor == "end":
        x -= w
    return (x, y - size, x + w, y - size + h)


def overlap(a, b, pad=6.0):
    return not (a[2] + pad < b[0] or b[2] + pad < a[0]
                or a[3] + pad < b[1] or b[3] + pad < a[1])


def seg_hits_box(p, q, box, pad=3.0):
    x0, y0, x1, y1 = box
    x0 -= pad
    y0 -= pad
    x1 += pad
    y1 += pad
    n = 64
    for i in range(n + 1):
        t = i / float(n)
        x = p[0] + (q[0] - p[0]) * t
        y = p[1] + (q[1] - p[1]) * t
        if x0 <= x <= x1 and y0 <= y <= y1:
            return True
    return False


def point_in_poly(pt, poly):
    x, y = pt
    inside = False
    n = len(poly)
    for i in range(n):
        ax, ay = poly[i]
        bx, by = poly[(i + 1) % n]
        if (ay > y) != (by > y):
            xint = ax + (y - ay) * (bx - ax) / (by - ay)
            if x < xint:
                inside = not inside
    return inside


def shoelace(poly):
    s = 0.0
    n = len(poly)
    for i in range(n):
        x0, y0 = poly[i]
        x1, y1 = poly[(i + 1) % n]
        s += x0 * y1 - x1 * y0
    return abs(s) / 2.0


def rect_segs(x, y, w, h):
    return [((x, y), (x + w, y)), ((x + w, y), (x + w, y + h)),
            ((x + w, y + h), (x, y + h)), ((x, y + h), (x, y))]


def fig1():
    e = []
    a = e.append
    labels = []
    segs = []

    a('<svg viewBox="0 0 %d %d" width="100%%" role="img" '
      'aria-label="Temperature against position along the rod. The shaded '
      'triangle under T equals 3x has area 54. The rectangle 6 wide and 9 tall '
      'has the same area, so 9 is the average temperature. The two leftover '
      'wedges are congruent, each of area 13.5, which is why the areas '
      'match.">' % (W1, H1))
    a('<rect x="0" y="0" width="%d" height="%d" class="plotbg196"/>' % (W1, H1))

    xticks = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
    yticks = [0.0, 3.0, 6.0, 9.0, 12.0, 15.0, 18.0]
    for xv in xticks:
        a('<line class="gridl" x1="%.2f" y1="%.2f" x2="%.2f" y2="%.2f"/>'
          % (sx(xv), sy(Y0), sx(xv), sy(Y1)))
    for yv in yticks:
        a('<line class="gridl" x1="%.2f" y1="%.2f" x2="%.2f" y2="%.2f"/>'
          % (sx(X0), sy(yv), sx(X1), sy(yv)))

    # DRAW ORDER IS CONTENT.  The triangle under the line goes down first, then
    # the rectangle on top of it.  What is left over is two wedges, and the
    # figure's one idea is that those two wedges are the SAME SIZE.
    tri = [(sx(0.0), sy(0.0)), (sx(LEN), sy(0.0)), (sx(LEN), sy(SLOPE * LEN))]
    a('<polygon class="fill196" points="%s"/>'
      % " ".join("%.2f,%.2f" % p for p in tri))

    rx, ry = sx(0.0), sy(AVG)
    rw, rh = sx(LEN) - sx(0.0), sy(0.0) - sy(AVG)
    a('<rect class="rectbox196" x="%.2f" y="%.2f" width="%.2f" height="%.2f"/>'
      % (rx, ry, rw, rh))
    segs.extend(rect_segs(rx, ry, rw, rh))

    # the two leftover wedges, each drawn as its own polygon so the congruence
    # can be measured off the DRAWN shapes rather than off the data
    wedge_lo = [(sx(0.0), sy(0.0)), (sx(CPT), sy(AVG)), (sx(0.0), sy(AVG))]
    wedge_hi = [(sx(CPT), sy(AVG)), (sx(LEN), sy(AVG)), (sx(LEN), sy(SLOPE * LEN))]
    a('<polygon class="wedgeA196" points="%s"/>'
      % " ".join("%.2f,%.2f" % p for p in wedge_lo))
    a('<polygon class="wedgeB196" points="%s"/>'
      % " ".join("%.2f,%.2f" % p for p in wedge_hi))

    # the temperature line itself, across the whole panel
    a('<line class="tline196" x1="%.2f" y1="%.2f" x2="%.2f" y2="%.2f"/>'
      % (sx(0.0), sy(0.0), sx(X1), sy(SLOPE * X1)))
    segs.append(((sx(0.0), sy(0.0)), (sx(X1), sy(SLOPE * X1))))

    # the average level, and the vertical through the MVT point
    a('<line class="avg196" x1="%.2f" y1="%.2f" x2="%.2f" y2="%.2f"/>'
      % (sx(0.0), sy(AVG), sx(X1), sy(AVG)))
    segs.append(((sx(0.0), sy(AVG)), (sx(X1), sy(AVG))))
    a('<line class="cline196" x1="%.2f" y1="%.2f" x2="%.2f" y2="%.2f"/>'
      % (sx(CPT), sy(0.0), sx(CPT), sy(AVG)))
    segs.append(((sx(CPT), sy(0.0)), (sx(CPT), sy(AVG))))
    a('<circle class="cdot196" cx="%.2f" cy="%.2f" r="4"/>' % (sx(CPT), sy(AVG)))

    a('<line class="axis" x1="%.2f" y1="%.2f" x2="%.2f" y2="%.2f"/>'
      % (sx(X0), sy(Y0), sx(X1), sy(Y0)))
    a('<line class="axis" x1="%.2f" y1="%.2f" x2="%.2f" y2="%.2f"/>'
      % (sx(X0), sy(Y0), sx(X0), sy(Y1)))

    ticklabs = []
    for xv in xticks:
        ticklabs.append((_fmt(xv), sx(xv), sy(Y0) + 18.0, 10, "middle"))
    for yv in yticks:
        ticklabs.append((_fmt(yv), sx(X0) - 9.0, sy(yv) + 3.5, 10, "end"))
    # 30.8: compare at the precision the file is actually written at.
    TICKS_BEFORE = [(t, "%.2f" % x, "%.2f" % y) for t, x, y, _s, _an in ticklabs]
    for t, x, y, s, an in ticklabs:
        a('<text class="tick196" x="%.2f" y="%.2f" text-anchor="%s">%s</text>'
          % (x, y, an, t))

    # both axis names on ONE horizontal caption.  A rotated y-axis title lands
    # in svg-labels' outsideBox, so it is folded in here instead.
    AXCAP = "POSITION x IN METRES, ACROSS - TEMPERATURE T IN DEGREES C, UP"
    a('<text class="lab" x="%.2f" y="%.2f" text-anchor="middle">%s</text>'
      % ((sx(X0) + sx(X1)) / 2.0, H1 - 12.0, AXCAP))
    labels.append((AXCAP, (sx(X0) + sx(X1)) / 2.0, H1 - 12.0, 11, "middle"))

    RX = sx(X1) + 12.0
    calls = [
        ("T(x) = 3x", RX, sy(19.0), 11, "start", "tlab196"),
        ("TOTAL = 54", RX, sy(16.4), 11, "start", "arealab196"),
        ("AREA UNDER THE LINE", RX, sy(14.9), 10, "start", "tick196"),
        ("AVERAGE = 9", RX, sy(11.6), 11, "start", "avgl196"),
        ("RECTANGLE 6 BY 9", RX, sy(10.1), 10, "start", "tick196"),
        ("SAME AREA, 54", RX, sy(8.6), 10, "start", "tick196"),
        ("c = 3 m", RX, sy(5.2), 11, "start", "clab196"),
        ("T(3) = 9 EXACTLY", RX, sy(3.7), 10, "start", "tick196"),
    ]
    for t, x, y, s, an, cls in calls:
        a('<text class="lab %s" x="%.2f" y="%.2f" text-anchor="%s" '
          'style="font-size:%gpx">%s</text>' % (cls, x, y, an, s, t))
        labels.append((t, x, y, s, an))

    # In-panel identification of the two wedges.  Both are 13.5, and saying so
    # IS the figure's argument - a content guard proves a label exists, never
    # that it is true, so the CONGRUENT guard below measures the two areas.
    a('<text class="lab wedgeAl196" x="%.2f" y="%.2f" text-anchor="middle">'
      '13.5</text>' % (sx(0.95), sy(6.6)))
    labels.append(("13.5", sx(0.95), sy(6.6), 11, "middle"))
    a('<text class="lab wedgeBl196" x="%.2f" y="%.2f" text-anchor="middle">'
      '13.5</text>' % (sx(5.05), sy(12.1)))
    labels.append(("13.5", sx(5.05), sy(12.1), 11, "middle"))

    a("</svg>")
    svg = "".join(e)

    # ---------------------------------------------------------------- guards
    nums = [float(v) for v in
            _re.findall(r'(?:x|y|x1|y1|x2|y2|cx|cy|width|height)="(-?[\d.]+)"',
                        svg)]
    assert nums, "bounds guard parsed nothing"
    assert min(nums) >= -1.0, "fig1 has a negative coordinate"
    assert max(nums) <= max(W1, H1) + 1.0, "fig1 overflows its viewBox"
    LOG.append("fig1 BOUNDS %d coords, min %.1f max %.1f"
               % (len(nums), min(nums), max(nums)))

    widest = max(bbox(t, x, y, s, an)[2] for t, x, y, s, an in labels)
    assert widest <= W1 - 4, "fig1 a label box reaches %.1f of %d" % (widest, W1)
    used = (widest - (sx(X1) + 12.0)) / float(PADR - 12.0)
    assert used > 0.6, ("fig1 right margin is %.0f percent empty; PADR is "
                        "oversized" % (100.0 * (1.0 - used)))
    LOG.append("fig1 LABELFIT widest label box ends at %.1f of %d, right margin "
               "%.0f percent used" % (widest, W1, 100.0 * used))

    # CONTAIN: every sample strictly under the line must sit in the drawn
    # triangle, and a control point above the line must be rejected.
    hits = 0
    tot = 0
    for i in range(1, 24):
        xv = LEN * i / 24.0
        for j in range(1, 6):
            yv = SLOPE * xv * j / 6.0
            tot += 1
            if point_in_poly((sx(xv), sy(yv)), tri):
                hits += 1
    assert hits == tot, ("fig1 shaded shape misses %d of %d interior samples"
                         % (tot - hits, tot))
    LOG.append("fig1 CONTAIN %d/%d interior samples inside the drawn triangle"
               % (hits, tot))
    ctl = (sx(1.0), sy(12.0))
    assert not point_in_poly(ctl, tri), \
        "fig1 CONTAIN control point above the line was ACCEPTED"
    LOG.append("fig1 CONTAIN control above the line correctly REJECTED")

    # CONGRUENT: measure the two wedges off the DRAWN polygons.
    aA = shoelace(wedge_lo)
    aB = shoelace(wedge_hi)
    assert abs(aA - aB) < 1e-6, ("the drawn wedges are NOT equal in area: "
                                 "%.4f vs %.4f" % (aA, aB))
    aTri = shoelace(tri)
    aRect = rw * rh
    assert abs(aTri - aRect) < 1e-6, ("the drawn triangle and rectangle differ "
                                      "in area: %.4f vs %.4f" % (aTri, aRect))
    LOG.append("fig1 CONGRUENT drawn wedges %.2f and %.2f px2 (equal); drawn "
               "triangle %.2f px2 equals drawn rectangle %.2f px2"
               % (aA, aB, aTri, aRect))
    # the guard must be shown to bite: shift the crossing off c and re-measure
    badA = [(sx(0.0), sy(0.0)), (sx(2.0), sy(AVG)), (sx(0.0), sy(AVG))]
    badB = [(sx(2.0), sy(AVG)), (sx(LEN), sy(AVG)), (sx(LEN), sy(SLOPE * LEN))]
    assert abs(shoelace(badA) - shoelace(badB)) > 1.0, \
        "the CONGRUENT guard cannot see a crossing moved off the MVT point"
    LOG.append("fig1 CONGRUENT CONTROL moving the crossing to x=2 gives "
               "%.2f vs %.2f px2, correctly REPORTED as unequal"
               % (shoelace(badA), shoelace(badB)))

    # TICKS
    TICKRE = (r'<text class="tick196" x="([\d.-]+)" y="([\d.-]+)"[^>]*>'
              r'([^<]*)</text>')

    def read_ticks(s):
        return [(m.group(3), m.group(1), m.group(2))
                for m in _re.finditer(TICKRE, s)]

    ticks_after = read_ticks(svg)
    assert ticks_after == TICKS_BEFORE, "the placer moved an axis tick"
    LOG.append("fig1 TICKS %d axis ticks, none moved" % len(ticks_after))
    one = ticklabs[0]
    moved = svg.replace('<text class="tick196" x="%.2f" y="%.2f"'
                        % (one[1], one[2]),
                        '<text class="tick196" x="%.2f" y="%.2f"'
                        % (one[1], one[2] + 9.0), 1)
    assert moved != svg, "the TICKS control did not mutate the svg"
    assert read_ticks(moved) != TICKS_BEFORE, \
        "the TICKS guard cannot see a moved tick"
    LOG.append("fig1 TICKS CONTROL a 9px nudge of one tick is REPORTED")

    # COLLIDE
    lb = [bbox(t, x, y, s, an) for t, x, y, s, an in labels]
    tb = [bbox(t, x, y, s, an) for t, x, y, s, an in ticklabs]
    coll = []
    for i, A in enumerate(lb):
        for j, B in enumerate(tb):
            if overlap(A, B):
                coll.append((labels[i][0], ticklabs[j][0]))
        for j in range(i + 1, len(lb)):
            if overlap(A, lb[j]):
                coll.append((labels[i][0], labels[j][0]))
    assert not coll, "fig1 label collisions: %s" % coll[:4]
    LOG.append("fig1 COLLIDE %d labels vs %d tick labels, 0 overlaps"
               % (len(lb), len(tb)))

    # RECTEDGE
    edge_hits = []
    for t, x, y, s, an in labels:
        B = bbox(t, x, y, s, an)
        for p, qq in segs:
            if seg_hits_box(p, qq, B):
                edge_hits.append(t)
                break
    assert not edge_hits, "fig1 labels crossed by a stroked edge: %s" % edge_hits
    LOG.append("fig1 RECTEDGE %d stroked segments (4 of them a rect border), "
               "0 crossing a label" % len(segs))

    MUST = ["T(x) = 3x", "TOTAL = 54", "AREA UNDER THE LINE", "AVERAGE = 9",
            "RECTANGLE 6 BY 9", "SAME AREA, 54", "c = 3 m", "T(3) = 9 EXACTLY",
            AXCAP, ">13.5<"]
    missing = [m for m in MUST if m not in svg]
    assert not missing, "fig1 must-appear labels never drawn: %s" % missing
    assert svg.count(">13.5<") == 2, "both wedge labels must be drawn"
    LOG.append("fig1 CONTENT all %d must-appear labels drawn, both wedge "
               "labels present" % len(MUST))
    return svg


# ---------------------------------------------------------------- fig 2 frame
PANW, PANH = 226, 186
PANY = 58
PANX = [30, 268, 506]


def fig2():
    e = []
    a = e.append
    labels = []
    segs = []

    a('<svg viewBox="0 0 %d %d" width="100%%" role="img" '
      'aria-label="Three panels on the interval zero to one. In the affine '
      'panel the true average and the mean of the two endpoint values land on '
      'the same level. In the convex panel the endpoint mean sits above the '
      'true average, and in the concave panel it sits below.">' % (W2, H2))
    a('<rect x="0" y="0" width="%d" height="%d" class="plotbg196"/>' % (W2, H2))

    a('<text class="lab" x="30" y="20">WHY THE ENDPOINT MEAN IS RIGHT HERE '
      'AND WRONG ALMOST EVERYWHERE</text>')
    labels.append(("WHY THE ENDPOINT MEAN IS RIGHT HERE AND WRONG ALMOST "
                   "EVERYWHERE", 30, 20, 11, "start"))

    panels = [
        ("AFFINE  f = x", lambda t: t, 0.5, "0.50 = 0.50", "COINCIDE", "same196"),
        ("CONVEX  f = x^2", lambda t: t * t, 1.0 / 3.0, "0.33 vs 0.50",
         "MEAN TOO HIGH", "hi196"),
        ("CONCAVE  f = root x", lambda t: t ** 0.5, 2.0 / 3.0, "0.67 vs 0.50",
         "MEAN TOO LOW", "lo196"),
    ]
    fills = []
    for pi, (title, fn, true_av, vlab, verdict, vcls) in enumerate(panels):
        px = PANX[pi]

        def gx(u, px=px):
            return px + u * PANW

        def gy(v):
            return PANY + PANH - v * PANH

        a('<rect class="panel196" x="%d" y="%d" width="%d" height="%d"/>'
          % (px, PANY, PANW, PANH))
        segs.extend(rect_segs(px, PANY, PANW, PANH))

        # the curve
        pts = []
        for i in range(0, 61):
            u = i / 60.0
            pts.append((gx(u), gy(fn(u))))
        a('<polyline class="curve196" points="%s"/>'
          % " ".join("%.1f,%.1f" % p for p in pts))
        for i in range(len(pts) - 1):
            segs.append((pts[i], pts[i + 1]))

        # the chord from (0, f(0)) to (1, f(1)) - always the same line here,
        # because all three functions agree at both endpoints
        a('<line class="chord196" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>'
          % (gx(0.0), gy(fn(0.0)), gx(1.0), gy(fn(1.0))))
        segs.append(((gx(0.0), gy(fn(0.0))), (gx(1.0), gy(fn(1.0)))))

        # the two levels.  In the affine panel they are the same line, so the
        # endpoint level is drawn first and the true level over it.
        ep = 0.5 * (fn(0.0) + fn(1.0))
        a('<line class="eplev196" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>'
          % (gx(0.0), gy(ep), gx(1.0), gy(ep)))
        segs.append(((gx(0.0), gy(ep)), (gx(1.0), gy(ep))))
        a('<line class="avglev196" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>'
          % (gx(0.0), gy(true_av), gx(1.0), gy(true_av)))
        segs.append(((gx(0.0), gy(true_av)), (gx(1.0), gy(true_av))))
        fills.append(max(fn(u) for u in (0.0, 0.5, 1.0)))

        a('<text class="lab %s" x="%d" y="%d">%s</text>'
          % ("panl196", px, PANY - 8, title))
        labels.append((title, px, PANY - 8, 11, "start"))
        a('<text class="lab %s" x="%d" y="%d" style="font-size:10px">%s</text>'
          % (vcls, px, PANY + PANH + 22, vlab))
        labels.append((vlab, px, PANY + PANH + 22, 10, "start"))
        a('<text class="lab %s" x="%d" y="%d" style="font-size:10px">%s</text>'
          % (vcls, px, PANY + PANH + 46, verdict))
        labels.append((verdict, px, PANY + PANH + 46, 10, "start"))

    a("</svg>")
    svg = "".join(e)

    nums = [float(v) for v in
            _re.findall(r'(?:x|y|x1|y1|x2|y2|width|height)="(-?[\d.]+)"', svg)]
    assert min(nums) >= -1.0, "fig2 has a negative coordinate"
    assert max(nums) <= max(W2, H2) + 1.0, "fig2 overflows its viewBox"
    LOG.append("fig2 BOUNDS %d coords, min %.1f max %.1f"
               % (len(nums), min(nums), max(nums)))

    # DEADSPACE: each curve must reach the top of its panel, and the three
    # panels must together fill most of the width.
    assert min(fills) >= 1.0 - 1e-9, "a panel curve does not reach its top"
    span = (PANX[-1] + PANW - PANX[0]) / float(W2)
    assert span > 0.7, "fig2 panels fill only %.0f percent of the width" % (
        100.0 * span)
    LOG.append("fig2 DEADSPACE every curve reaches the panel top; the three "
               "panels span %.0f percent of the figure width" % (100.0 * span))

    lb = [bbox(t, x, y, s, an) for t, x, y, s, an in labels]
    coll = []
    for i, A in enumerate(lb):
        for j in range(i + 1, len(lb)):
            if overlap(A, lb[j]):
                coll.append((labels[i][0], labels[j][0]))
    assert not coll, "fig2 label collisions: %s" % coll[:4]
    LOG.append("fig2 COLLIDE %d labels, 0 overlaps" % len(lb))

    edge_hits = []
    for t, x, y, s, an in labels:
        B = bbox(t, x, y, s, an)
        for p, qq in segs:
            if seg_hits_box(p, qq, B):
                edge_hits.append(t)
                break
    assert not edge_hits, "fig2 labels crossed by a stroked edge: %s" % edge_hits
    LOG.append("fig2 RECTEDGE %d stroked segments (12 of them panel borders), "
               "0 crossing a label" % len(segs))

    MUST = ["AFFINE  f = x", "CONVEX  f = x^2", "CONCAVE  f = root x",
            "0.50 = 0.50", "0.33 vs 0.50", "0.67 vs 0.50", "COINCIDE",
            "MEAN TOO HIGH", "MEAN TOO LOW"]
    missing = [m for m in MUST if m not in svg]
    assert not missing, "fig2 must-appear labels never drawn: %s" % missing
    LOG.append("fig2 CONTENT all %d must-appear labels drawn" % len(MUST))
    return svg


def contain_control():
    """Prove the containment guard REJECTS a shape that does not contain the
    region, rather than trusting that it accepted the real one."""
    bad = [(sx(0.0), sy(0.0)), (sx(3.0), sy(0.0)), (sx(3.0), sy(SLOPE * 3.0))]
    misses = 0
    for i in range(1, 24):
        xv = LEN * i / 24.0
        for j in range(1, 6):
            yv = SLOPE * xv * j / 6.0
            if not point_in_poly((sx(xv), sy(yv)), bad):
                misses += 1
    LOG.append("CONTAIN CONTROL a half-width triangle misses %d of 115 samples"
               % misses)
    return misses > 0


def rectedge_control():
    """Prove RECTEDGE bites: put a label on the rectangle's own top edge."""
    y = sy(AVG)
    B = bbox("SEEDED", sx(2.0), y + 3.0, 11, "middle")
    hit = seg_hits_box((sx(0.0), y), (sx(LEN), y), B)
    LOG.append("RECTEDGE CONTROL a label seeded on the rectangle's top edge "
               "is %s" % ("REPORTED" if hit else "MISSED"))
    return hit


def tick_control():
    return any("TICKS CONTROL" in line for line in LOG)


def congruent_control():
    return any("CONGRUENT CONTROL" in line for line in LOG)


if __name__ == "__main__":
    s1 = fig1()
    s2 = fig2()
    assert contain_control()
    assert rectedge_control()
    assert tick_control()
    assert congruent_control()
    for line in LOG:
        print(line)
    print("fig1 %d bytes, fig2 %d bytes" % (len(s1), len(s2)))
