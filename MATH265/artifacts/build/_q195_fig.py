"""Figures for the Q19.5 artifact.

Two figures, both about the same idea:

  fig1  the force-extension plot: the work IS the triangle, and the naive
        "force times distance" is the whole box, exactly twice as big.
  fig2  the mirror: the chain's constant force with varying distances beside
        the spring's varying force with a constant dx.

Guards, all of them because a previous run shipped the defect they catch:
  - BOUNDS      every drawn coordinate inside the viewBox (carryover 15.6);
  - CONTAIN     the drawn shaded polygon must actually CONTAIN sample points of
                the region it claims to be, with a control point that is
                outside and must be rejected (29.9);
  - TICKS       the label placer must not move an axis tick (28.9);
  - COLLIDE     no label overlaps a tick label or another label;
  - RECTEDGE    svg-labels samples only line/polyline, so a stroked <rect>
                border is a STRUCTURAL BLIND SPOT - its four edges are turned
                into segments here and tested against every label;
  - CONTENT     every label named in MUST_APPEAR is actually drawn (28.8).
"""
import math

W1, H1 = 760, 392
W2, H2 = 760, 340

LOG = []
K = 40.0
AEND = 2.0

# ---------------------------------------------------------------- fig 1 frame
PADL, PADR, PADT, PADB = 62, 150, 34, 46
X0, X1 = 0.0, 2.4          # feet of extension
Y0, Y1 = 0.0, 104.0        # pounds of force


def sx(x):
    return PADL + (x - X0) / (X1 - X0) * (W1 - PADL - PADR)


def sy(y):
    return H1 - PADB - (y - Y0) / (Y1 - Y0) * (H1 - PADT - PADB)


def _fmt(v):
    return ("%.2f" % v).rstrip("0").rstrip(".")


# label geometry is estimated, not measured: svg-labels.mjs does the real
# getBBox pass in the browser.  This layer is the cheap one that runs at build
# time, and its estimate is deliberately generous.
CHW = {10: 6.4, 11: 7.0, 11.5: 7.3, 12: 7.6}


def bbox(text, x, y, size=11, anchor="start"):
    w = len(text) * CHW.get(size, 7.0)
    h = size * 1.25
    if anchor == "middle":
        x -= w / 2.0
    elif anchor == "end":
        x -= w
    return (x, y - size, x + w, y - size + h)


def overlap(a, b, pad=3.0):
    return not (a[2] + pad < b[0] or b[2] + pad < a[0]
                or a[3] + pad < b[1] or b[3] + pad < a[1])


def seg_hits_box(p, q, box, pad=3.0):
    """Sample a segment and report whether any sample lands in the padded box."""
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


def fig1():
    e = []
    a = e.append
    labels = []          # (text, x, y, size, anchor)
    segs = []            # ((x,y),(x,y)) for every stroked edge, rects included

    a('<svg viewBox="0 0 %d %d" width="100%%" role="img" '
      'aria-label="Force against extension. The work is the shaded triangle; '
      'force at the far end times the distance is the whole box, twice as big.">'
      % (W1, H1))
    a('<rect x="0" y="0" width="%d" height="%d" class="plotbg195"/>' % (W1, H1))

    # gridlines and ticks
    xticks = [0.0, 0.5, 1.0, 1.5, 2.0]
    yticks = [0.0, 20.0, 40.0, 60.0, 80.0, 100.0]
    for xv in xticks:
        a('<line class="gridl" x1="%.2f" y1="%.2f" x2="%.2f" y2="%.2f"/>'
          % (sx(xv), sy(Y0), sx(xv), sy(Y1)))
    for yv in yticks:
        a('<line class="gridl" x1="%.2f" y1="%.2f" x2="%.2f" y2="%.2f"/>'
          % (sx(X0), sy(yv), sx(X1), sy(yv)))

    # DRAW ORDER MATTERS.  The naive box goes down FIRST with a wash, then the
    # work triangle on top of it, so the two regions read as nested and the
    # leftover rust wedge above the line IS the factor-of-two error.  A first
    # draft drew the triangle first with --fam-soft, which is 10 percent alpha,
    # and the shaded region was invisible in dark mode - only the screenshot
    # showed it.
    bx0, by0 = sx(0.0), sy(K * AEND)
    bw, bh = sx(AEND) - sx(0.0), sy(0.0) - sy(K * AEND)
    a('<rect class="naivebox195" x="%.2f" y="%.2f" width="%.2f" height="%.2f"/>'
      % (bx0, by0, bw, bh))

    # THE WORK: the triangle under F = 40x from 0 to 2
    tri = [(sx(0.0), sy(0.0)), (sx(AEND), sy(0.0)), (sx(AEND), sy(K * AEND))]
    a('<polygon class="fill195" points="%s"/>'
      % " ".join("%.2f,%.2f" % p for p in tri))
    for p, q in (((bx0, by0), (bx0 + bw, by0)),
                 ((bx0 + bw, by0), (bx0 + bw, by0 + bh)),
                 ((bx0 + bw, by0 + bh), (bx0, by0 + bh)),
                 ((bx0, by0 + bh), (bx0, by0))):
        segs.append((p, q))

    # the average-force level, which cuts the box in half
    a('<line class="avg195" x1="%.2f" y1="%.2f" x2="%.2f" y2="%.2f"/>'
      % (sx(0.0), sy(K), sx(AEND), sy(K)))
    segs.append(((sx(0.0), sy(K)), (sx(AEND), sy(K))))

    # Hooke's line itself, drawn across the whole panel
    a('<line class="force195" x1="%.2f" y1="%.2f" x2="%.2f" y2="%.2f"/>'
      % (sx(0.0), sy(0.0), sx(X1), sy(K * X1)))
    segs.append(((sx(0.0), sy(0.0)), (sx(X1), sy(K * X1))))

    # axes
    a('<line class="axis" x1="%.2f" y1="%.2f" x2="%.2f" y2="%.2f"/>'
      % (sx(X0), sy(Y0), sx(X1), sy(Y0)))
    a('<line class="axis" x1="%.2f" y1="%.2f" x2="%.2f" y2="%.2f"/>'
      % (sx(X0), sy(Y0), sx(X0), sy(Y1)))

    # tick labels.  Their coordinates are recorded so the placer can be proved
    # not to have moved them.
    ticklabs = []
    for xv in xticks:
        t = _fmt(xv)
        ticklabs.append((t, sx(xv), sy(Y0) + 17.0, 10, "middle"))
    for yv in yticks:
        t = _fmt(yv)
        ticklabs.append((t, sx(X0) - 9.0, sy(yv) + 3.5, 10, "end"))
    # compare at the precision the SVG is actually WRITTEN at.  A first draft
    # kept 3 decimals here while emitting 2, so the guard fired on its own
    # rounding rather than on a moved tick.
    TICKS_BEFORE = [(t, "%.2f" % x, "%.2f" % y) for t, x, y, _s, _an in ticklabs]

    for t, x, y, s, an in ticklabs:
        a('<text class="tick195" x="%.2f" y="%.2f" text-anchor="%s">%s</text>'
          % (x, y, an, t))

    # Both axis names go on ONE horizontal caption.  A rotated y-axis title was
    # drawn first and svg-labels reported it in outsideBox, because a rotate()
    # transform puts the measured box outside the figure's own rect.  Folding
    # the units into a single header is 25.x's fix, and it reads better at
    # 10px anyway.
    AXCAP = "EXTENSION x IN FEET, ACROSS - FORCE F IN POUNDS, UP"
    a('<text class="lab" x="%.2f" y="%.2f" text-anchor="middle">%s</text>'
      % ((sx(X0) + sx(X1)) / 2.0, H1 - 12.0, AXCAP))
    labels.append((AXCAP, (sx(X0) + sx(X1)) / 2.0, H1 - 12.0, 11, "middle"))

    # the four callouts, anchored to the right margin so nothing crosses a line
    RX = sx(X1) + 12.0
    calls = [
        ("F(x) = 40x", RX, sy(96.0), 11, "start", "flab195"),
        ("WORK = 80 ft-lb", RX, sy(72.0), 11, "start", "movl195"),
        ("the TRIANGLE", RX, sy(63.0), 10, "start", "tick195"),
        ("F(2) x 2 = 160", RX, sy(44.0), 11, "start", "stayl195"),
        ("the WHOLE BOX", RX, sy(35.0), 10, "start", "tick195"),
        ("AVERAGE FORCE 40 lb", RX, sy(16.0), 10, "start", "avgl195"),
    ]
    for t, x, y, s, an, cls in calls:
        a('<text class="lab %s" x="%.2f" y="%.2f" text-anchor="%s" '
          'style="font-size:%gpx">%s</text>' % (cls, x, y, an, s, t))
        labels.append((t, x, y, s, an))

    # In-panel identification of the two regions.  The upper wedge is NOT 160 -
    # 160 is the whole box.  A first draft labelled the wedge "160", which was
    # a factual error the callout on the right then contradicted.  The box is
    # two equal triangles, so the honest labels are 80 and 80 MORE.
    a('<text class="lab areal195" x="%.2f" y="%.2f" text-anchor="middle">'
      '80</text>' % (sx(1.55), sy(18.0)))
    labels.append(("80", sx(1.55), sy(18.0), 11, "middle"))
    a('<text class="lab stayl195" x="%.2f" y="%.2f" text-anchor="middle">'
      '80 MORE</text>' % (sx(0.62), sy(64.0)))
    labels.append(("80 MORE", sx(0.62), sy(64.0), 11, "middle"))

    a("</svg>")
    svg = "".join(e)

    # ---------------------------------------------------------------- guards
    # BOUNDS
    import re as _re
    nums = [float(v) for v in _re.findall(r'(?:x|y|x1|y1|x2|y2|cx|cy)="(-?[\d.]+)"', svg)]
    assert nums, "bounds guard parsed nothing"
    LOG.append("fig1 BOUNDS %d coords, min %.1f max %.1f"
               % (len(nums), min(nums), max(nums)))
    assert min(nums) >= -1.0, "fig1 has a negative coordinate"
    assert max(nums) <= max(W1, H1) + 1.0, "fig1 overflows its viewBox"
    # a coordinate scan cannot see a LABEL running off the right edge, because
    # only its anchor is an attribute.  18.7's dead-space rule in the direction
    # that actually bites: assert the widest label BOX still fits, and that the
    # right margin is not mostly empty.
    widest = max(bbox(t, x, y, s, an)[2] for t, x, y, s, an in labels)
    assert widest <= W1 - 4, ("fig1 a label box reaches %.1f of %d"
                              % (widest, W1))
    used = (widest - (sx(X1) + 12.0)) / float(PADR - 12.0)
    assert used > 0.6, ("fig1 right margin is %.0f percent empty; PADR is "
                        "oversized" % (100.0 * (1.0 - used)))
    LOG.append("fig1 LABELFIT widest label box ends at %.1f of %d, right margin "
               "%.0f percent used" % (widest, W1, 100.0 * used))

    # CONTAIN: sample the TRUE region (under F = 40x, 0 < x < 2) and require the
    # drawn polygon to contain each sample.  Then a control point that is inside
    # the box but ABOVE the line, which must be rejected.
    inside_hits = 0
    for i in range(1, 20):
        xv = AEND * i / 20.0
        for j in range(1, 6):
            yv = K * xv * j / 6.0
            if point_in_poly((sx(xv), sy(yv)), tri):
                inside_hits += 1
    total = 19 * 5
    assert inside_hits == total, ("fig1 shaded shape misses %d of %d interior "
                                 "samples" % (total - inside_hits, total))
    LOG.append("fig1 CONTAIN %d/%d interior samples inside the drawn triangle"
               % (inside_hits, total))
    ctl = (sx(0.5), sy(60.0))       # above the line, inside the box
    assert not point_in_poly(ctl, tri), \
        "fig1 CONTAIN control point above the line was accepted"
    LOG.append("fig1 CONTAIN control above the line correctly REJECTED")

    # TICKS: unchanged after all placement
    TICKRE = (r'<text class="tick195" x="([\d.-]+)" y="([\d.-]+)"[^>]*>'
              r'([^<]*)</text>')

    def read_ticks(s):
        return [(m.group(3), m.group(1), m.group(2))
                for m in _re.finditer(TICKRE, s)]

    ticks_after = read_ticks(svg)
    assert ticks_after == TICKS_BEFORE, ("the placer moved an axis tick: %s"
                                        % [(a, b) for a, b in
                                           zip(ticks_after, TICKS_BEFORE)
                                           if a != b][:3])
    LOG.append("fig1 TICKS %d axis ticks, none moved" % len(ticks_after))
    # prove the guard bites, on THIS svg: nudge one tick and re-read it
    one = ticklabs[0]
    moved = svg.replace('<text class="tick195" x="%.2f" y="%.2f"'
                        % (one[1], one[2]),
                        '<text class="tick195" x="%.2f" y="%.2f"'
                        % (one[1], one[2] + 9.0), 1)
    assert read_ticks(moved) != TICKS_BEFORE, \
        "the TICKS guard cannot see a moved tick"
    LOG.append("fig1 TICKS CONTROL a 9px nudge of one tick is REPORTED")

    # COLLIDE: labels against tick labels and against each other
    lb = [bbox(t, x, y, s, an) for t, x, y, s, an in labels]
    tb = [bbox(t, x, y, s, an) for t, x, y, s, an in ticklabs]
    hits = []
    for i, A in enumerate(lb):
        for j, B in enumerate(tb):
            if overlap(A, B):
                hits.append((labels[i][0], ticklabs[j][0]))
        for j in range(i + 1, len(lb)):
            if overlap(A, lb[j]):
                hits.append((labels[i][0], labels[j][0]))
    assert not hits, "fig1 label collisions: %s" % hits[:4]
    LOG.append("fig1 COLLIDE %d labels vs %d ticks, 0 overlaps"
               % (len(lb), len(tb)))

    # RECTEDGE: the blind spot.  Every stroked edge, the rect's four included,
    # tested against every label box.
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

    # CONTENT
    MUST = ["F(x) = 40x", "WORK = 80 ft-lb", "F(2) x 2 = 160",
            "AVERAGE FORCE 40 lb", "the TRIANGLE", "the WHOLE BOX",
            AXCAP, ">80<", ">80 MORE<"]
    missing = [m for m in MUST if m not in svg]
    assert not missing, "fig1 must-appear labels never drawn: %s" % missing
    LOG.append("fig1 CONTENT all %d must-appear labels drawn" % len(MUST))
    return svg


# ---------------------------------------------------------------- fig 2 frame
def fig2():
    e = []
    a = e.append
    labels = []
    segs = []

    a('<svg viewBox="0 0 %d %d" width="100%%" role="img" '
      'aria-label="The mirror. On the left a chain, where every slice needs the '
      'same force and travels a different distance. On the right a spring, '
      'where every element travels the same distance and needs a different '
      'force.">' % (W2, H2))
    a('<rect x="0" y="0" width="%d" height="%d" class="plotbg195"/>' % (W2, H2))
    a('<line class="axis" x1="%d" y1="30" x2="%d" y2="%d"/>'
      % (W2 // 2, W2 // 2, H2 - 34))

    # ---- left panel: the chain.  Equal-thickness slices, arrows of different
    # lengths.  The VARYING factor is the arrow.
    # panel headers are NEUTRAL: neither side is right or wrong, so neither may
    # borrow the teal/rust pair, which means correct/incorrect everywhere else.
    a('<text class="lab" x="30" y="26">CHAIN - SAME FORCE, '
      'DIFFERENT DISTANCES</text>')
    labels.append(("CHAIN - SAME FORCE, DIFFERENT DISTANCES", 30, 26, 11, "start"))
    base = H2 - 52
    for i in range(6):
        y = base - i * 36.0
        a('<rect class="slice195" x="46" y="%.1f" width="34" height="9"/>'
          % (y - 9))
        for p, qq in (((46, y - 9), (80, y - 9)), ((80, y - 9), (80, y)),
                      ((80, y), (46, y)), ((46, y), (46, y - 9))):
            segs.append((p, qq))
        L = 24.0 + i * 46.0
        a('<line class="rise195" x1="88" y1="%.1f" x2="%.1f" y2="%.1f"/>'
          % (y - 4.5, 88 + L, y - 4.5))
        segs.append(((88, y - 4.5), (88 + L, y - 4.5)))
        a('<polygon class="arrowh195" points="%.1f,%.1f %.1f,%.1f %.1f,%.1f"/>'
          % (88 + L, y - 4.5, 88 + L - 7, y - 9, 88 + L - 7, y))
    a('<text class="lab tick195" x="46" y="%d">EACH SLICE: 78.4 dy NEWTONS'
      '</text>' % (H2 - 34))
    labels.append(("EACH SLICE: 78.4 dy NEWTONS", 46, H2 - 34, 10, "start"))
    a('<text class="lab varl195" x="46" y="%d">THE DISTANCE VARIES</text>'
      % (H2 - 12))
    labels.append(("THE DISTANCE VARIES", 46, H2 - 12, 10, "start"))

    # ---- right panel: the spring.  Equal-width steps, bars of different height.
    RX0 = W2 // 2 + 46
    a('<text class="lab" x="%d" y="26">SPRING - SAME DISTANCE, '
      'DIFFERENT FORCES</text>' % RX0)
    labels.append(("SPRING - SAME DISTANCE, DIFFERENT FORCES", RX0, 26, 11, "start"))
    bw = 28.0
    for i in range(6):
        x = RX0 + i * bw
        h = 30.0 + i * 40.0
        a('<rect class="bar195" x="%.1f" y="%.1f" width="%.1f" height="%.1f"/>'
          % (x, base - h, bw - 3.0, h))
        for p, qq in (((x, base - h), (x + bw - 3.0, base - h)),
                      ((x + bw - 3.0, base - h), (x + bw - 3.0, base)),
                      ((x + bw - 3.0, base), (x, base)),
                      ((x, base), (x, base - h))):
            segs.append((p, qq))
    a('<line class="axis" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>'
      % (RX0 - 6, base, RX0 + 6 * bw + 4, base))
    a('<text class="lab tick195" x="%d" y="%d">EACH STEP: THE SAME dx</text>'
      % (RX0, H2 - 34))
    labels.append(("EACH STEP: THE SAME dx", RX0, H2 - 34, 10, "start"))
    a('<text class="lab varl195" x="%d" y="%d">THE FORCE VARIES</text>'
      % (RX0, H2 - 12))
    labels.append(("THE FORCE VARIES", RX0, H2 - 12, 10, "start"))

    a("</svg>")
    svg = "".join(e)

    import re as _re
    nums = [float(v) for v in
            _re.findall(r'(?:x|y|x1|y1|x2|y2|width|height)="(-?[\d.]+)"', svg)]
    LOG.append("fig2 BOUNDS %d coords, min %.1f max %.1f"
               % (len(nums), min(nums), max(nums)))
    assert min(nums) >= -1.0, "fig2 has a negative coordinate"
    assert max(nums) <= max(W2, H2) + 1.0, "fig2 overflows its viewBox"

    # 18.7: a figure's DEAD SPACE is invisible to every gate.  Assert that the
    # tallest bar and the longest arrow actually reach most of the space each
    # has, so the panels are not two small drawings in a large box.
    tall = base - (base - (30.0 + 5 * 40.0))
    vfill = tall / float(base - 34.0)
    longest = 88.0 + (24.0 + 5 * 46.0)
    hfill = (longest - 88.0) / float(W2 // 2 - 12 - 88)
    assert vfill > 0.7, "fig2 right panel is %.0f percent empty vertically" \
        % (100.0 * (1.0 - vfill))
    assert hfill > 0.7, "fig2 left panel is %.0f percent empty horizontally" \
        % (100.0 * (1.0 - hfill))
    LOG.append("fig2 DEADSPACE tallest bar fills %.0f percent of its height, "
               "longest arrow %.0f percent of its width"
               % (100.0 * vfill, 100.0 * hfill))

    lb = [bbox(t, x, y, s, an) for t, x, y, s, an in labels]
    hits = []
    for i, A in enumerate(lb):
        for j in range(i + 1, len(lb)):
            if overlap(A, lb[j]):
                hits.append((labels[i][0], labels[j][0]))
    assert not hits, "fig2 label collisions: %s" % hits[:4]
    LOG.append("fig2 COLLIDE %d labels, 0 overlaps" % len(lb))

    edge_hits = []
    for t, x, y, s, an in labels:
        B = bbox(t, x, y, s, an)
        for p, qq in segs:
            if seg_hits_box(p, qq, B):
                edge_hits.append(t)
                break
    assert not edge_hits, "fig2 labels crossed by a stroked edge: %s" % edge_hits
    LOG.append("fig2 RECTEDGE %d stroked segments (all rect borders and arrows), "
               "0 crossing a label" % len(segs))

    MUST = ["CHAIN - SAME FORCE, DIFFERENT DISTANCES",
            "SPRING - SAME DISTANCE, DIFFERENT FORCES",
            "EACH SLICE: 78.4 dy NEWTONS", "EACH STEP: THE SAME dx",
            "THE DISTANCE VARIES", "THE FORCE VARIES"]
    missing = [m for m in MUST if m not in svg]
    assert not missing, "fig2 must-appear labels never drawn: %s" % missing
    LOG.append("fig2 CONTENT all %d must-appear labels drawn" % len(MUST))
    return svg


def contain_control():
    """Prove the containment guard REJECTS a shape that does not contain the
    region, rather than trusting that it accepted the real one."""
    bad = [(sx(0.0), sy(0.0)), (sx(1.0), sy(0.0)), (sx(1.0), sy(K * 1.0))]
    misses = 0
    for i in range(1, 20):
        xv = AEND * i / 20.0
        for j in range(1, 6):
            yv = K * xv * j / 6.0
            if not point_in_poly((sx(xv), sy(yv)), bad):
                misses += 1
    LOG.append("CONTAIN CONTROL a half-width triangle misses %d of 95 samples"
               % misses)
    return misses > 0


def rectedge_control():
    """Prove the RECTEDGE guard bites: place a label on the naive box's own top
    edge and require it to be reported."""
    y = sy(K * AEND)
    B = bbox("SEEDED", sx(1.0), y + 3.0, 11, "middle")
    seg = ((sx(0.0), y), (sx(AEND), y))
    hit = seg_hits_box(seg[0], seg[1], B)
    LOG.append("RECTEDGE CONTROL a label seeded on the rect's top edge is %s"
               % ("REPORTED" if hit else "MISSED"))
    return hit


def tick_control():
    """The TICKS guard's liveness is proved INSIDE fig1, against that figure's
    own emitted SVG, rather than against two lists typed here.  This function
    only reports that the in-figure control ran."""
    return any("TICKS CONTROL" in line for line in LOG)


if __name__ == "__main__":
    s1 = fig1()
    s2 = fig2()
    assert contain_control()
    assert rectedge_control()
    assert tick_control()
    for line in LOG:
        print(line)
    print("fig1 %d bytes, fig2 %d bytes" % (len(s1), len(s2)))
