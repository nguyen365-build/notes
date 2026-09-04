"""Figures for the Q19.3 artifact.

Rules carried from the carryover, each for a defect no gate caught:
  - a figure illustrating an area identity must have its drawn shape CONTAIN the
    region, not merely match its area (26.5);
  - the label placer must NOT move axis ticks - ticks live in reserved gutters at
    positions set by the scale, and are registered with the placer as obstacles (26.6);
  - tick labels need their own collision check, because svg-labels measures text.lab
    only and structurally cannot see them (27.9).
"""
import math

BS = chr(92)


# ---------------------------------------------------------------- placer
class Placer:
    """rasterise every drawn segment into a spatial hash, then search outward from an
    anchor for the nearest spot clearing CLEAR px of geometry and of placed labels."""

    def __init__(self, cell=2.0, clear=22.0):
        self.cell = cell
        self.clear = clear
        self.grid = {}
        self.boxes = []

    def _key(self, x, y):
        return (int(x // self.cell), int(y // self.cell))

    def add_point(self, x, y):
        self.grid[self._key(x, y)] = True

    def add_seg(self, x1, y1, x2, y2):
        n = max(2, int(math.hypot(x2 - x1, y2 - y1) / (self.cell * 0.5)) + 1)
        for i in range(n + 1):
            t = i / n
            self.add_point(x1 + (x2 - x1) * t, y1 + (y2 - y1) * t)

    def add_poly(self, pts):
        for i in range(len(pts) - 1):
            self.add_seg(pts[i][0], pts[i][1], pts[i + 1][0], pts[i + 1][1])

    def add_box(self, x, y, w, h):
        self.boxes.append((x, y, w, h))

    def _geo_clear(self, x, y, w, h):
        r = self.clear
        best = 1e9
        x0, y0, x1, y1 = x - r, y - r, x + w + r, y + h + r
        for gx in range(int(x0 // self.cell), int(x1 // self.cell) + 1):
            for gy in range(int(y0 // self.cell), int(y1 // self.cell) + 1):
                if (gx, gy) not in self.grid:
                    continue
                px, py = (gx + 0.5) * self.cell, (gy + 0.5) * self.cell
                dx = max(x - px, 0, px - (x + w))
                dy = max(y - py, 0, py - (y + h))
                best = min(best, math.hypot(dx, dy))
        return best

    def _box_clear(self, x, y, w, h):
        best = 1e9
        for (bx, by, bw, bh) in self.boxes:
            dx = max(bx - (x + w), x - (bx + bw), 0)
            dy = max(by - (y + h), y - (by + bh), 0)
            best = min(best, math.hypot(dx, dy))
        return best

    def place(self, ax, ay, w, h, bounds, prefer=(0, -1)):
        """return (x, y, achieved_clearance) for a w x h label anchored near (ax, ay)"""
        bx0, by0, bx1, by1 = bounds
        best = None
        for r in [0] + [4 * k for k in range(1, 40)]:
            cands = []
            if r == 0:
                cands = [(ax + prefer[0] * 6 - w / 2, ay + prefer[1] * 14 - h / 2)]
            else:
                for a in range(0, 360, 10):
                    th = math.radians(a)
                    cands.append((ax + r * math.cos(th) - w / 2,
                                  ay + r * math.sin(th) - h / 2))
            for (cx, cy) in cands:
                if cx < bx0 or cy < by0 or cx + w > bx1 or cy + h > by1:
                    continue
                gc = self._geo_clear(cx, cy, w, h)
                bc = self._box_clear(cx, cy, w, h)
                cl = min(gc, bc)
                if cl >= self.clear:
                    self.add_box(cx, cy, w, h)
                    return cx, cy, cl
                if best is None or cl > best[2]:
                    best = (cx, cy, cl)
            if best is not None and r > 60 and best[2] > self.clear * 0.8:
                break
        cx, cy, cl = best
        self.add_box(cx, cy, w, h)
        return cx, cy, cl


def _connector_start(cx, cy, w, h, ax, ay, gap=15.0):
    """Start the connector GAP px outside the label box, so the line never crosses the
    label it belongs to.  Returns (None, None) when there is no room left to draw."""
    lx, ly = cx + w / 2.0, cy + h / 2.0
    dx, dy = ax - lx, ay - ly
    d = math.hypot(dx, dy)
    if d < 1e-6:
        return None, None
    ux, uy = dx / d, dy / d
    # walk out from the label centre until we are gap px clear of the box
    step = 0.5
    t = 0.0
    while t < d:
        px, py = lx + ux * t, ly + uy * t
        ox = max(cx - px, 0.0, px - (cx + w))
        oy = max(cy - py, 0.0, py - (cy + h))
        if math.hypot(ox, oy) >= gap:
            break
        t += step
    if d - t < 10.0:
        return None, None
    return lx + ux * t, ly + uy * t


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def txt(x, y, s, cls="lab", anchor="start", size=11.5, weight="500", fill="var(--ink2)"):
    return ('<text class="%s" x="%.2f" y="%.2f" text-anchor="%s" font-size="%.1f" '
            'font-weight="%s" fill="%s">%s</text>'
            % (cls, x, y, anchor, size, weight, fill, esc(s)))


def mtxt(x, y, lines, dy=14.5, cls="lab", anchor="start", size=11.0,
         weight="500", fill="var(--ink2)"):
    """A multi-line label as ONE <text>.  Emitting each line as its own <text
    class="lab"> made svg-labels report a label's two own lines as an overlapping
    pair - a false positive created by the markup, not by the layout."""
    sp = "".join('<tspan x="%.2f" dy="%.2f">%s</tspan>'
                 % (x, 0.0 if i == 0 else dy, esc(s)) for i, s in enumerate(lines))
    return ('<text class="%s" x="%.2f" y="%.2f" text-anchor="%s" font-size="%.1f" '
            'font-weight="%s" fill="%s">%s</text>'
            % (cls, x, y, anchor, size, weight, fill, sp))


# =================================================================== FIGURE 1
# The rate r(t) = 180 - 6t over the stem's whole stated domain [0,50].
# The area under [0,15] IS the answer; the sign change at t=30 is drawn, because
# that is where the net-versus-total distinction lives and why it is invisible
# on the asked interval.

W1, H1 = 780, 400
L1, R1, T1, B1 = 76, 30, 34, 66          # reserved gutters: left for y ticks, bottom for x
PX0, PY0, PX1, PY1 = L1, T1, W1 - R1, H1 - B1
XA, XB = 0.0, 50.0
YA, YB = -140.0, 200.0


def r(t):
    return 180.0 - 6.0 * t


def sx(t):
    return PX0 + (t - XA) / (XB - XA) * (PX1 - PX0)


def sy(v):
    return PY1 - (v - YA) / (YB - YA) * (PY1 - PY0)


def invx(px):
    return XA + (px - PX0) / (PX1 - PX0) * (XB - XA)


def invy(py):
    return YA + (PY1 - py) / (PY1 - PY0) * (YB - YA)


def figure1():
    P = Placer(cell=2.0, clear=22.0)
    o = []
    o.append('<svg viewBox="0 0 %d %d" role="img" '
             'aria-label="The outflow rate r(t) = 180 minus 6t over 0 to 50 minutes. '
             'The shaded area over the first 15 minutes is the 2025 litre answer. '
             'The rate crosses zero at 30 minutes.">' % (W1, H1))

    # plot ground
    o.append('<rect class="plotbg193" x="%.1f" y="%.1f" width="%.1f" height="%.1f" '
             'fill="var(--surface)" stroke="var(--line)" stroke-width="1"/>'
             % (PX0, PY0, PX1 - PX0, PY1 - PY0))

    # gridlines, exempted from svg-labels by their class
    for v in (-120, -60, 0, 60, 120, 180):
        y = sy(v)
        o.append('<line class="gridl" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" '
                 'stroke="var(--grid)" stroke-width="1"/>' % (PX0, y, PX1, y))
    for t in (0, 10, 20, 30, 40, 50):
        x = sx(t)
        o.append('<line class="gridl" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" '
                 'stroke="var(--grid)" stroke-width="1"/>' % (x, PY0, x, PY1))

    # the zero line, drawn stronger because the sign change is the point
    yz = sy(0.0)
    o.append('<line class="axist" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" '
             'stroke="var(--ink3)" stroke-width="1.3"/>' % (PX0, yz, PX1, yz))

    # ---- the three shaded bands, built as polygons that CONTAIN their region ----
    def band(t0, t1, cls, fill, opacity):
        pts = []
        n = 96
        for i in range(n + 1):
            t = t0 + (t1 - t0) * i / n
            pts.append((sx(t), sy(r(t))))
        pts.append((sx(t1), yz))
        pts.append((sx(t0), yz))
        s = " ".join("%.2f,%.2f" % p for p in pts)
        return ('<polygon class="%s" points="%s" fill="%s" fill-opacity="%.2f" '
                'stroke="%s" stroke-width="1"/>' % (cls, s, fill, opacity, fill)), pts

    b1, p1 = band(0.0, 15.0, "band193", "var(--accent)", 0.55)
    b2, p2 = band(15.0, 30.0, "band193", "var(--chn)", 0.40)
    b3, p3 = band(30.0, 50.0, "band193", "var(--los)", 0.42)
    o.extend([b1, b2, b3])

    # ---- the rate line itself ----
    line = [(sx(t), sy(r(t))) for t in (XA, XB)]
    o.append('<polyline class="rate193" points="%s" fill="none" stroke="var(--ink)" '
             'stroke-width="2"/>' % " ".join("%.2f,%.2f" % p for p in line))
    P.add_poly(line)
    for pts in (p1, p2, p3):
        P.add_poly(pts)

    # ---- ticks, placed BY THE SCALE in the reserved gutters, never by the placer ----
    ticks = []
    for t in (0, 10, 20, 30, 40, 50):
        x = sx(t)
        ticks.append(txt(x, PY1 + 18, str(t), cls="tick193", anchor="middle",
                         size=10.5, weight="500", fill="var(--plotlab)"))
        P.add_box(x - 10, PY1 + 6, 20, 15)
    ticks.append(txt((PX0 + PX1) / 2, PY1 + 40, "t, MINUTES", cls="tick193",
                     anchor="middle", size=10.0, weight="600",
                     fill="var(--ink3)"))
    P.add_box((PX0 + PX1) / 2 - 40, PY1 + 30, 80, 14)
    for v in (-120, -60, 0, 60, 120, 180):
        y = sy(v)
        ticks.append(txt(PX0 - 9, y + 3.6, str(v), cls="tick193", anchor="end",
                         size=10.5, weight="500", fill="var(--plotlab)"))
        P.add_box(PX0 - 9 - 30, y - 7, 30, 14)
    # the y axis needs its unit, and it goes in the gutter above the top tick rather
    # than as a rotated axis title, which collided with the ticks in every prior run
    ticks.append(txt(PX0 - 9, PY0 - 8, "r, L/min", cls="tick193", anchor="end",
                     size=10.0, weight="600", fill="var(--ink3)"))
    P.add_box(PX0 - 9 - 52, PY0 - 20, 52, 15)
    o.extend(ticks)

    # ---- freely placed annotations ----
    CH = 6.80          # measured over-estimate; 6.35 let a label cross the viewBox
    rep = []

    def lab(ax, ay, lines, fill="var(--ink2)", prefer=(0, -1)):
        w = max(len(s) for s in lines) * CH + 8
        h = 14.5 * len(lines) + 6
        cx, cy, cl = P.place(ax, ay, w, h, (8, 8, W1 - 8, H1 - 8), prefer)
        o.append(mtxt(cx + 4, cy + 15, lines, fill=fill))
        sx_, sy_ = _connector_start(cx, cy, w, h, ax, ay, gap=15.0)
        if sx_ is not None:
            o.append('<line class="conn193" x1="%.2f" y1="%.2f" x2="%.2f" y2="%.2f" '
                     'stroke="var(--line)" stroke-width="1"/>' % (sx_, sy_, ax, ay))
        rep.append((lines[0], cl))
        return cx, cy

    lab(sx(7.5), sy(r(7.5) * 0.45), ["2025 L", "the answer"],
        fill="var(--accent)", prefer=(0, 0))
    # One line, anchored on the curve at t=22 with the preference UPWARD: the
    # two-line version could not fit inside the 15-to-30 band and the placer put it
    # BELOW the axis, where it appeared to label the rust region instead.  A label
    # in the wrong band is worse than no label, and no gate can see it.
    lab(sx(22), sy(r(22)), ["675 L more"], fill="var(--chn)", prefer=(0, -1))
    # one line, not two: the two-line version could only reach 18.1px of clearance
    # in this band, and shortening a label is a legitimate fix (carryover, 4).
    lab(sx(41), sy(-60), ["1200 L flows IN"], fill="var(--los)", prefer=(0, 1))
    lab(sx(30), yz, ["r = 0 at t = 30"], fill="var(--ink2)", prefer=(1, -1))
    lab(sx(3), sy(r(3)), ["r(t) = 180 - 6t"], fill="var(--ink)", prefer=(1, -1))
    lab(sx(15), sy(90), ["r(15) = 90"], fill="var(--ink2)", prefer=(1, -1))

    o.append("</svg>")
    return "\n".join(o), rep


# =================================================================== FIGURE 2
# The wrong-answer census on a value axis, with the magnitude bracket drawn.
# The point of the picture: three dots stack exactly on 2025, and the bracket
# band is the widest net any eight-second check casts.

# the panel is sized to its content: the first draft was 330 tall and its top
# third was empty, which reads as a layout accident rather than a choice
W2, H2 = 780, 218
L2, R2, T2, B2 = 60, 34, 26, 32
QX0, QY0, QX1, QY1 = L2, T2, W2 - R2, H2 - B2
VA, VB = 0.0, 4100.0

CENSUS = [
    (2025.0, "right", "the answer"),
    (2025.0, "hide", "midpoint rate"),
    (2025.0, "hide", "no lower limit"),
    (2700.0, "wrong", "r(0) x 15"),
    (2700.0, "wrong", "int over [0,30]"),
    (1350.0, "wrong", "r(15) x 15"),
    (1350.0, "wrong", "180t - 6t^2"),
    (1500.0, "wrong", "int over [0,50]"),
    (2587.5, "wrong", "dropped the 6"),
    (3900.0, "wrong", "total moved"),
    (180.0, "wrong", "r(0), a rate"),
    (90.0, "wrong", "r(15), a rate"),
]
NEGATIVES = [-6.0, -90.0, -525.0, -2025.0, -7425.0]
BLO, BHI = 1350.0, 2700.0


def vx(v):
    return QX0 + (v - VA) / (VB - VA) * (QX1 - QX0)


def figure2():
    P = Placer(cell=2.0, clear=22.0)
    o = []
    o.append('<svg viewBox="0 0 %d %d" role="img" '
             'aria-label="The seventeen candidate answers on a value axis. Three sit '
             'exactly on 2025. The magnitude bracket from 1350 to 2700 is shaded.">'
             % (W2, H2))
    o.append('<rect class="plotbg193" x="%.1f" y="%.1f" width="%.1f" height="%.1f" '
             'fill="var(--surface)" stroke="var(--line)" stroke-width="1"/>'
             % (QX0, QY0, QX1 - QX0, QY1 - QY0))

    # the magnitude bracket band.  Its stroked border is a <rect>, which svg-labels
    # structurally cannot sample (it looks at line and polyline only), so the first
    # draft had a note running straight through the dashed edge with every gate
    # clean.  Register the four edges with the placer explicitly.
    # the band wraps the DOT STRIP only, not the whole panel, so the upper half of
    # the plot stays free for labels; with the band spanning the full height the
    # placer could only reach 16.4px of clearance
    bx, by = vx(BLO), QY1 - 26 - 60
    bw, bh = vx(BHI) - vx(BLO), 68.0
    o.append('<rect class="brk193" x="%.1f" y="%.1f" width="%.1f" height="%.1f" '
             'fill="var(--fam)" fill-opacity="0.13" stroke="var(--fam)" '
             'stroke-width="1" stroke-dasharray="3 3"/>' % (bx, by, bw, bh))
    P.add_poly([(bx, by), (bx + bw, by), (bx + bw, by + bh), (bx, by + bh), (bx, by)])

    base = QY1 - 26
    o.append('<line class="axist" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" '
             'stroke="var(--ink3)" stroke-width="1.2"/>' % (QX0 + 6, base, QX1 - 6, base))

    for v in (0, 1000, 2000, 3000, 4000):
        x = vx(v)
        o.append('<line class="gridl" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" '
                 'stroke="var(--grid)" stroke-width="1"/>' % (x, QY0, x, base))

    # dots, stacked when values coincide
    COL = {"right": "var(--accent)", "hide": "var(--los)", "wrong": "var(--ink3)"}
    seen = {}
    dots = []
    for (v, kind, name) in CENSUS:
        k = round(v, 6)
        n = seen.get(k, 0)
        seen[k] = n + 1
        cx, cy = vx(v), base - 11 - n * 15
        rr = 5.4 if kind == "right" else 4.6
        o.append('<circle class="dot193" cx="%.2f" cy="%.2f" r="%.1f" fill="%s" '
                 'stroke="var(--surface)" stroke-width="1.2"/>'
                 % (cx, cy, rr, COL[kind]))
        P.add_box(cx - rr, cy - rr, 2 * rr, 2 * rr)
        dots.append((cx, cy, kind, name))

    # ticks in the reserved bottom gutter, placed by the scale
    ticks = []
    for v in (0, 1000, 2000, 3000, 4000):
        x = vx(v)
        ticks.append(txt(x, base + 19, str(v), cls="tick193", anchor="middle",
                         size=10.5, weight="500", fill="var(--plotlab)"))
        P.add_box(x - 17, base + 7, 34, 15)
    ticks.append(txt((QX0 + QX1) / 2, base + 41, "CANDIDATE ANSWER, LITRES",
                     cls="tick193", anchor="middle", size=10.0, weight="600",
                     fill="var(--ink3)"))
    P.add_box((QX0 + QX1) / 2 - 78, base + 31, 156, 14)
    o.extend(ticks)

    CH = 6.80          # measured over-estimate; 6.35 let a label cross the viewBox
    rep = []

    def lab(ax, ay, lines, fill="var(--ink2)", prefer=(0, -1)):
        w = max(len(s) for s in lines) * CH + 8
        h = 14.5 * len(lines) + 6
        cx, cy, cl = P.place(ax, ay, w, h, (8, 8, W2 - 8, H2 - 8), prefer)
        o.append(mtxt(cx + 4, cy + 15, lines, fill=fill))
        s1, s2 = _connector_start(cx, cy, w, h, ax, ay, gap=15.0)
        if s1 is not None:
            o.append('<line class="conn193" x1="%.2f" y1="%.2f" x2="%.2f" y2="%.2f" '
                     'stroke="var(--line)" stroke-width="1"/>' % (s1, s2, ax, ay))
        rep.append((lines[0], cl))

    # one anchor gets ONE connector (27.8), so label the stack once, at its top dot
    top2025 = min((d for d in dots if abs(d[0] - vx(2025.0)) < 0.5), key=lambda d: d[1])
    lab(top2025[0], top2025[1],
        ["THREE routes land here:", "the right one and two wrong"],
        fill="var(--los)", prefer=(0, -1))
    lab(vx(BHI), QY0 + 26, ["the magnitude bracket,", "1350 to 2700"],
        fill="var(--fam)", prefer=(1, 1))
    lab(vx(3900.0), base - 11, ["total moved, [0,50]"], fill="var(--ink2)",
        prefer=(-1, -1))
    lab(vx(90.0), base - 11, ["two RATES, caught by units"], fill="var(--ink2)",
        prefer=(1, -1))

    # The five negative candidates are stated in the CAPTION rather than drawn.
    # In the plot they needed a broken scale, and as a static note they crossed the
    # band's dashed edge.  Deleting a label is a legitimate fix.

    o.append("</svg>")
    return "\n".join(o), rep
