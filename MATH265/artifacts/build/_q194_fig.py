"""Figures for the Q19.4 artifact.

Two figures, both load-bearing:

  FIG 1  the chain before and after.  This is the modelling picture - the whole
         question is "which slice travels how far", and the picture has to SHOW
         that the top 6 m moves and the bottom 4 m does not.
  FIG 2  the same work computed from two different slicing variables, drawn as
         two areas that are equal.  This is the verification picture.

Guards carried, each for a defect no gate caught in an earlier run:
  - CONTAINMENT: the drawn hanging segment must span exactly heights 0..H and
    the grounded segment exactly L-H metres, checked against the scale.
  - RECT BORDERS ARE GEOMETRY (28.8): every stroked rect's four edges are
    registered, because svg-labels samples only line/polyline.
  - TICKS ARE GEOMETRY (27.9, 26.6): tick labels are registered as obstacles and
    are never moved, because svg-labels measures only text.lab.
  - CONTENT: every label that must appear is asserted present in the output.
  - CH is OVER-estimated (28.8) at 6.80, because the browser's real mono advance
    is nearer 6.6 and the gate measures the real one.
"""

CH = 6.80          # over-estimate of the mono advance width at 11px
LINEH = 13.0


class Geom(object):
    """Everything drawn, so a label can be checked against all of it."""

    def __init__(self):
        self.segs = []          # (x1,y1,x2,y2)
        self.boxes = []         # (x,y,w,h,name)  text boxes already placed

    def seg(self, x1, y1, x2, y2):
        self.segs.append((float(x1), float(y1), float(x2), float(y2)))

    def poly(self, pts):
        for i in range(len(pts) - 1):
            self.seg(pts[i][0], pts[i][1], pts[i + 1][0], pts[i + 1][1])

    def rect_border(self, x, y, w, h):
        """28.8: a stroked <rect> is invisible to svg-labels, so register it."""
        self.poly([(x, y), (x + w, y), (x + w, y + h), (x, y + h), (x, y)])

    def box(self, x, y, w, h, name):
        self.boxes.append((x, y, w, h, name))

    # ---- clearance --------------------------------------------------------
    @staticmethod
    def _pt_seg(px, py, x1, y1, x2, y2):
        dx, dy = x2 - x1, y2 - y1
        d2 = dx * dx + dy * dy
        if d2 == 0.0:
            return ((px - x1) ** 2 + (py - y1) ** 2) ** 0.5
        t = max(0.0, min(1.0, ((px - x1) * dx + (py - y1) * dy) / d2))
        cx, cy = x1 + t * dx, y1 + t * dy
        return ((px - cx) ** 2 + (py - cy) ** 2) ** 0.5

    def clearance(self, x, y, w, h):
        """Smallest distance from the box's perimeter to any drawn segment."""
        best = 1e9
        n = 12
        pts = []
        for i in range(n + 1):
            pts.append((x + w * i / n, y))
            pts.append((x + w * i / n, y + h))
            pts.append((x, y + h * i / n))
            pts.append((x + w, y + h * i / n))
        for (px, py) in pts:
            for s in self.segs:
                d = self._pt_seg(px, py, *s)
                if d < best:
                    best = d
        # a box that straddles a segment has zero clearance, not a positive one
        for s in self.segs:
            if self._crosses(x, y, w, h, s):
                return 0.0
        return best

    @staticmethod
    def _crosses(x, y, w, h, s):
        x1, y1, x2, y2 = s
        # cheap: sample the segment and test containment in the box
        for i in range(41):
            t = i / 40.0
            px, py = x1 + t * (x2 - x1), y1 + t * (y2 - y1)
            if x <= px <= x + w and y <= py <= y + h:
                return True
        return False

    def box_overlap(self, x, y, w, h):
        for (bx, by, bw, bh, nm) in self.boxes:
            if not (x + w < bx or bx + bw < x or y + h < by or by + bh < y):
                return nm
        return None


def label(G, out, x, y, text, cls="lab", anchor="start", need=11.0,
          lines=None, register=True, check=True, why=""):
    """Emit one <text>.  A multi-line label is ONE <text> with <tspan> children
    (28.8), so svg-labels measures one box instead of reporting a label's own
    lines as an overlapping pair."""
    rows = lines if lines else [text]
    w = max(len(r) for r in rows) * CH
    h = LINEH * len(rows) + 3.0
    if anchor == "middle":
        bx = x - w / 2.0
    elif anchor == "end":
        bx = x - w
    else:
        bx = x
    by = y - LINEH + 2.0
    if check:
        c = G.clearance(bx, by, w, h)
        assert c >= need, ("label %r clearance %.2f < %.2f %s" % (rows[0], c, need, why))
        ov = G.box_overlap(bx, by, w, h)
        assert ov is None, "label %r overlaps label %r" % (rows[0], ov)
    if register:
        G.box(bx, by, w, h, rows[0])
    a = ' text-anchor="%s"' % anchor if anchor != "start" else ""
    if lines:
        inner = "".join('<tspan x="%g" dy="%g">%s</tspan>'
                        % (x, 0 if i == 0 else LINEH, r)
                        for i, r in enumerate(rows))
    else:
        inner = text
    out.append('<text class="%s" x="%g" y="%g"%s>%s</text>' % (cls, x, y, a, inner))
    return (bx, by, w, h)


# =========================================================== FIGURE 1
def fig1():
    L, H = 10.0, 6.0
    W, HT = 760.0, 322.0
    PPM = 27.0                      # pixels per metre
    GY = 268.0                      # ground line, y
    AX0, AX1 = 34.0, 726.0
    G = Geom()
    o = []

    o.append('<svg viewBox="0 0 %g %g" width="100%%" '
             'preserveAspectRatio="xMidYMid meet" role="img" '
             'aria-label="The chain before and after one end is raised">'
             % (W, HT))

    # panel background
    o.append('<rect class="plotbg194" x="0" y="0" width="%g" height="%g"/>' % (W, HT))

    # ---- the ground, drawn once across both panels
    o.append('<line class="ground194" x1="%g" y1="%g" x2="%g" y2="%g"/>'
             % (AX0, GY, AX1, GY))
    G.seg(AX0, GY, AX1, GY)

    # ---- LEFT: before
    bx0 = 52.0
    bx1 = bx0 + L * PPM
    o.append('<line class="chain194" x1="%g" y1="%g" x2="%g" y2="%g"/>'
             % (bx0, GY - 3, bx1, GY - 3))
    G.seg(bx0, GY - 3, bx1, GY - 3)
    # end markers
    for xx in (bx0, bx1):
        o.append('<circle class="knot194" cx="%g" cy="%g" r="3.4"/>' % (xx, GY - 3))
        G.seg(xx - 3.4, GY - 3, xx + 3.4, GY - 3)

    # ---- RIGHT: after.  vertical part spans EXACTLY heights 0..H
    ax = 452.0
    top = GY - H * PPM
    o.append('<line class="chainhi194" x1="%g" y1="%g" x2="%g" y2="%g"/>'
             % (ax, GY, ax, top))
    G.seg(ax, GY, ax, top)
    gx1 = ax + (L - H) * PPM
    o.append('<line class="chainlo194" x1="%g" y1="%g" x2="%g" y2="%g"/>'
             % (ax, GY - 3, gx1, GY - 3))
    G.seg(ax, GY - 3, gx1, GY - 3)
    o.append('<circle class="knothi194" cx="%g" cy="%g" r="4"/>' % (ax, top))
    o.append('<circle class="knot194" cx="%g" cy="%g" r="3.4"/>' % (gx1, GY - 3))
    G.seg(gx1 - 3.4, GY - 3, gx1 + 3.4, GY - 3)

    # CONTAINMENT: the drawn shapes must be the regions they claim to be
    assert abs((GY - top) / PPM - H) < 1e-9, "hanging segment is not H metres"
    assert abs((gx1 - ax) / PPM - (L - H)) < 1e-9, "grounded segment is not L-H metres"
    assert abs(((bx1 - bx0) / PPM) - L) < 1e-9, "the before-chain is not L metres"
    assert abs(((GY - top) + (gx1 - ax)) / PPM - L) < 1e-9, "the after-chain is not L long"

    # ---- height axis on the right of the after panel
    axx = 690.0
    o.append('<line class="axis" x1="%g" y1="%g" x2="%g" y2="%g"/>'
             % (axx, GY, axx, GY - H * PPM - 12))
    G.seg(axx, GY, axx, GY - H * PPM - 12)
    for m in (0, 2, 4, 6):
        yy = GY - m * PPM
        o.append('<line class="gridl" x1="%g" y1="%g" x2="%g" y2="%g"/>'
                 % (axx - 5, yy, axx + 5, yy))
        G.seg(axx - 5, yy, axx + 5, yy)
        # ticks are placed by hand and NEVER moved (26.6); register them so
        # freely-placed labels treat them as obstacles
        t = "%d" % m
        o.append('<text class="tick194" x="%g" y="%g">%s</text>'
                 % (axx + 9, yy + 3.6, t))
        G.box(axx + 9, yy - 8, len(t) * CH, 12, "tick " + t)
    label(G, o, axx + 9, GY - H * PPM - 18, "y (m)", cls="tick194", need=6.0)

    # ---- the rise arrow: one slice, from the ground to height 3 m
    sy = GY - 3.0 * PPM
    o.append('<line class="rise194" x1="%g" y1="%g" x2="%g" y2="%g" '
             'marker-end="url(#a194)"/>' % (ax - 46, GY, ax - 46, sy + 4))
    G.seg(ax - 46, GY, ax - 46, sy + 4)
    o.append('<line class="tie194" x1="%g" y1="%g" x2="%g" y2="%g"/>'
             % (ax - 46, sy, ax, sy))
    G.seg(ax - 46, sy, ax, sy)
    o.append('<rect class="slice194" x="%g" y="%g" width="%g" height="%g"/>'
             % (ax - 5, sy - 4, 10, 8))
    G.rect_border(ax - 5, sy - 4, 10, 8)

    # ---- labels
    label(G, o, (bx0 + bx1) / 2.0, GY + 26, "10 m LYING FLAT, 80 kg",
          anchor="middle", need=9.0)
    label(G, o, (bx0 + bx1) / 2.0, 44, "BEFORE", anchor="middle", need=9.0)
    label(G, o, 452.0 + 30, 44, "AFTER", anchor="start", need=9.0)

    # 28.9: a three-line label could not fit beside the arrow without crossing
    # the chain, and the clearance guard said so.  Shortened to one line and
    # anchored to the arrow's own end rather than pushed somewhere it fits.
    label(G, o, ax - 60, GY - 3.0 * PPM - 1, "ONE SLICE, RAISED THROUGH y",
          anchor="end", need=8.0, why="rise arrow")
    label(G, o, ax + 16, GY - H * PPM + 30, "",
          lines=["6 m NOW HANGING", "48 kg MOVES"], cls="lab movl194", need=9.0)
    label(G, o, gx1 + 12, GY + 26, "",
          lines=["4 m STILL DOWN", "32 kg NEVER MOVES"], cls="lab stayl194",
          anchor="end", need=9.0)

    o.append('<defs><marker id="a194" viewBox="0 0 10 10" refX="9" refY="5" '
             'markerWidth="6" markerHeight="6" orient="auto-start-reverse">'
             '<path d="M0,0 L10,5 L0,10 z" class="arrowh194"/></marker></defs>')
    o.append("</svg>")
    svg = "".join(o)

    # CONTENT GUARD (28.8): assert every label that must appear is drawn
    for must in ("BEFORE", "AFTER", "ONE SLICE, RAISED THROUGH y", "48 kg MOVES",
                 "32 kg NEVER MOVES", "10 m LYING FLAT, 80 kg", "y (m)"):
        assert must in svg, "figure 1 never draws %r" % must
    assert svg.count('class="lab') + svg.count('class="tick194"') >= 10
    return svg


# =========================================================== FIGURE 2
def fig2():
    """The same work from two slicing variables.  Two panels, equal areas."""
    W, HT = 760.0, 268.0
    G = Geom()
    o = []
    o.append('<svg viewBox="0 0 %g %g" width="100%%" '
             'preserveAspectRatio="xMidYMid meet" role="img" '
             'aria-label="The same total work from two different slicing '
             'variables">' % (W, HT))
    o.append('<rect class="plotbg194" x="0" y="0" width="%g" height="%g"/>' % (W, HT))

    PY0, PY1 = 216.0, 58.0          # y for rise = 0 and rise = 6
    def ry(v):
        return PY0 + (PY1 - PY0) * (v / 6.0)

    panels = [
        # (x0, x1, xmax, rise fn, title lines, x label, tick values)
        (56.0, 320.0, 6.0, lambda u: u,
         "ROUTE A - SLICE BY HEIGHT y", "y, height above the ground (m)",
         (0, 2, 4, 6)),
        (438.0, 702.0, 10.0, lambda u: max(6.0 - u, 0.0),
         "ROUTE B - SLICE BY ARCLENGTH s", "s, distance from the raised end (m)",
         (0, 2, 4, 6, 8, 10)),
    ]

    for (X0, X1, XMAX, f, title, xlab, ticks) in panels:
        def rx(u, X0=X0, X1=X1, XMAX=XMAX):
            return X0 + (X1 - X0) * (u / XMAX)

        # axes
        o.append('<line class="axis" x1="%g" y1="%g" x2="%g" y2="%g"/>'
                 % (X0, PY0, X1 + 8, PY0))
        G.seg(X0, PY0, X1 + 8, PY0)
        o.append('<line class="axis" x1="%g" y1="%g" x2="%g" y2="%g"/>'
                 % (X0, PY0, X0, PY1 - 10))
        G.seg(X0, PY0, X0, PY1 - 10)

        # horizontal gridlines at rise = 2, 4, 6
        for v in (2, 4, 6):
            o.append('<line class="gridl" x1="%g" y1="%g" x2="%g" y2="%g"/>'
                     % (X0, ry(v), X1 + 8, ry(v)))
            G.seg(X0, ry(v), X1 + 8, ry(v))
            t = "%d" % v
            o.append('<text class="tick194" x="%g" y="%g" text-anchor="end">%s</text>'
                     % (X0 - 7, ry(v) + 3.6, t))
            G.box(X0 - 7 - len(t) * CH, ry(v) - 8, len(t) * CH, 12, "ytick" + str(X0) + t)

        # the shaded region under the rise curve = the integral
        N = 240
        pts = [(rx(XMAX * i / N), ry(f(XMAX * i / N))) for i in range(N + 1)]
        d = "M %g %g " % (X0, PY0)
        d += " ".join("L %g %g" % p for p in pts)
        d += " L %g %g Z" % (rx(XMAX), PY0)
        o.append('<path class="fill194" d="%s"/>' % d)

        # the rise curve itself
        o.append('<polyline class="rise2194" points="%s"/>'
                 % " ".join("%g,%g" % p for p in pts))
        G.poly(pts)

        # x ticks
        for v in ticks:
            xx = rx(v)
            o.append('<line class="gridl" x1="%g" y1="%g" x2="%g" y2="%g"/>'
                     % (xx, PY0, xx, PY0 + 5))
            G.seg(xx, PY0, xx, PY0 + 5)
            t = "%d" % v
            o.append('<text class="tick194" x="%g" y="%g" text-anchor="middle">%s</text>'
                     % (xx, PY0 + 18, t))
            G.box(xx - len(t) * CH / 2.0, PY0 + 8, len(t) * CH, 12, "xt%g%s" % (X0, t))

        label(G, o, X0, 32, title, need=8.0)
        label(G, o, (X0 + X1) / 2.0, PY0 + 40, xlab, anchor="middle", need=7.0)

    # The equal-area statement, one per panel.  28.9: a label whose meaning is
    # "this region" must be asserted INSIDE that region, not merely clear of
    # everything - a placer optimising clearance will happily park it outside.
    AREA_A = label(G, o, 150.0, 189.0, "", lines=["AREA = 18", "x 78.4 N/m"],
                   cls="lab areal194", need=8.0, why="inside panel A's shaded region")
    AREA_B = label(G, o, 460.0, 183.0, "", lines=["AREA = 18", "x 78.4 N/m"],
                   cls="lab areal194", need=8.0, why="inside panel B's shaded region")
    label(G, o, 610.0, 186.0, "", lines=["THIS 4 m ADDS", "NOTHING"],
          cls="lab stayl194", need=8.0)
    _contain(AREA_A, 56.0, 320.0, 6.0, lambda u: u, PY0, ry, "A")
    _contain(AREA_B, 438.0, 702.0, 10.0, lambda u: max(6.0 - u, 0.0), PY0, ry, "B")
    o.append("</svg>")
    svg = "".join(o)

    for must in ("ROUTE A - SLICE BY HEIGHT y", "ROUTE B - SLICE BY ARCLENGTH s",
                 "AREA = 18", "THIS 4 m ADDS", "y, height above the ground (m)",
                 "s, distance from the raised end (m)"):
        assert must in svg, "figure 2 never draws %r" % must
    return svg


CONTAIN_LOG = []


def _contain(box, X0, X1, XMAX, f, PY0, ry, name):
    """28.9 + 26.5: assert every corner of an "in this region" label lies inside
    the region the label names - between the rise curve and the axis.  The scale
    is passed in from the drawing code, never retyped, so the guard cannot drift
    away from the geometry it guards (28.14)."""
    bx, by, w, h = box
    bad = []
    for (px, py) in ((bx, by), (bx + w, by), (bx, by + h), (bx + w, by + h)):
        u = (px - X0) / (X1 - X0) * XMAX
        cy = ry(f(u))
        if not (cy <= py <= PY0):
            bad.append("(%.1f,%.1f) curve %.1f axis %.1f" % (px, py, cy, PY0))
    CONTAIN_LOG.append("panel %s: %d of 4 corners inside the shaded region"
                       % (name, 4 - len(bad)))
    assert not bad, "panel %s AREA label escapes its region: %s" % (name, "; ".join(bad))


def contain_control():
    """The guard must REJECT a box deliberately placed outside the region."""
    PY0 = 216.0

    def ry(v):
        return PY0 + (58.0 - PY0) * (v / 6.0)

    try:
        _contain((150.0, 60.0, 74.8, 29.0), 56.0, 320.0, 6.0,
                 lambda u: u, PY0, ry, "CONTROL")
    except AssertionError:
        return True
    return False


if __name__ == "__main__":
    a, b = fig1(), fig2()
    print("fig1 %d bytes, fig2 %d bytes" % (len(a), len(b)))
    for line in CONTAIN_LOG:
        print(line)
    print("containment CONTROL rejects an outside box:", contain_control())
