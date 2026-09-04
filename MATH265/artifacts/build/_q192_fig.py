"""Figures for the Q19.2 artifact.

Two rules carried from the carryover, each for a defect no gate caught:
  - a figure that illustrates an area identity must have its drawn shape CONTAIN the
    region, not merely match its area (26.5);
  - the label placer must NOT move axis ticks - ticks live in reserved gutters at
    positions set by the scale, and are registered with the placer as obstacles (26.6).
"""
import math

pi, sq, acos = math.pi, math.sqrt, math.acos
S2 = sq(2.0)
C = 1.0 / S2
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


# =================================================================== FIGURE 1
def figure1():
    W, H = 760, 400
    L, R, T, B = 78, 34, 40, 62          # reserved gutters: left for y ticks, bottom for x
    px0, py0, px1, py1 = L, T, W - R, H - B
    xa, xb = -pi / 2, pi / 2
    ya, yb = -0.10, 1.14

    def X(x):
        return px0 + (x - xa) / (xb - xa) * (px1 - px0)

    def Y(y):
        return py1 - (y - ya) / (yb - ya) * (py1 - py0)

    out = []
    out.append('<svg viewBox="0 0 %d %d" width="100%%" role="img" '
               'aria-label="cos x against the line y = 1 over root 2 on minus pi over 2 to '
               'pi over 2, with the three pieces of the region shaded">' % (W, H))
    out.append('<rect x="0" y="0" width="%d" height="%d" fill="var(--surface)"/>' % (W, H))
    out.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="var(--surface)" '
               'stroke="var(--line)" stroke-width="1"/>'
               % (px0, py0, px1 - px0, py1 - py0))

    P = Placer(cell=2.0, clear=20.0)

    # ---- gridlines (class matches /grid/ so svg-labels exempts them) ----
    xticks = [(-pi / 2, "-pi/2"), (-pi / 4, "-pi/4"), (0.0, "0"),
              (pi / 4, "pi/4"), (pi / 2, "pi/2")]
    yticks = [(0.0, "0"), (C, "0.707"), (1.0, "1")]
    for xv, _lab in xticks:
        out.append('<line class="gridl" x1="%.2f" y1="%.1f" x2="%.2f" y2="%.1f" '
                   'stroke="var(--line)" stroke-width="1" stroke-dasharray="2 4"/>'
                   % (X(xv), py0, X(xv), py1))
    for yv, _lab in yticks:
        out.append('<line class="gridl" x1="%.1f" y1="%.2f" x2="%.1f" y2="%.2f" '
                   'stroke="var(--line)" stroke-width="1" stroke-dasharray="2 4"/>'
                   % (px0, Y(yv), px1, Y(yv)))

    # ---- the three shaded pieces: the ACTUAL region, so containment is by construction
    def band(a, b, fill):
        pts = []
        n = 160
        for i in range(n + 1):
            x = a + (b - a) * i / n
            pts.append((X(x), Y(math.cos(x))))
        for i in range(n + 1):
            x = b - (b - a) * i / n
            pts.append((X(x), Y(C)))
        d = " ".join("%.2f,%.2f" % p for p in pts)
        return ('<polygon class="band192" points="%s" fill="%s" fill-opacity="0.55" '
                'stroke="%s" stroke-width="0.8" stroke-opacity="0.9"/>' % (d, fill, fill))

    out.append(band(-pi / 2, -pi / 4, "var(--los)"))
    out.append(band(-pi / 4, pi / 4, "var(--fam)"))
    out.append(band(pi / 4, pi / 2, "var(--los)"))

    # ---- the line and the curve, clipped to the plot rect by construction ----
    out.append('<line class="lin192" x1="%.2f" y1="%.2f" x2="%.2f" y2="%.2f" '
               'stroke="var(--accent)" stroke-width="2"/>' % (px0, Y(C), px1, Y(C)))
    cpts = [(X(xa + (xb - xa) * i / 400), Y(math.cos(xa + (xb - xa) * i / 400)))
            for i in range(401)]
    out.append('<polyline class="cos192" points="%s" fill="none" stroke="var(--ink)" '
               'stroke-width="2.4"/>' % " ".join("%.2f,%.2f" % p for p in cpts))
    P.add_poly(cpts)
    P.add_seg(px0, Y(C), px1, Y(C))

    # ---- crossing dots ----
    for xv in (-pi / 4, pi / 4):
        out.append('<circle class="dot192" cx="%.2f" cy="%.2f" r="4.5" '
                   'fill="var(--surface)" stroke="var(--ink)" stroke-width="2"/>'
                   % (X(xv), Y(C)))
        P.add_point(X(xv), Y(C))

    # ---- TICKS: fixed positions in the reserved gutters, registered as obstacles ----
    for xv, lab in xticks:
        out.append('<line class="axist" x1="%.2f" y1="%.1f" x2="%.2f" y2="%.1f" '
                   'stroke="var(--ink3)" stroke-width="1"/>' % (X(xv), py1, X(xv), py1 + 5))
        out.append(txt(X(xv), py1 + 19, lab, cls="tick192", anchor="middle", size=10.5,
                       fill="var(--ink3)"))
        P.add_box(X(xv) - 26, py1 + 8, 52, 14)
    for yv, lab in yticks:
        out.append('<line class="axist" x1="%.1f" y1="%.2f" x2="%.1f" y2="%.2f" '
                   'stroke="var(--ink3)" stroke-width="1"/>' % (px0 - 5, Y(yv), px0, Y(yv)))
        out.append(txt(px0 - 10, Y(yv) + 3.5, lab, cls="tick192", anchor="end", size=10.5,
                       fill="var(--ink3)"))
        P.add_box(px0 - 52, Y(yv) - 8, 46, 16)
    out.append(txt(px0, py1 + 40, "x  IN RADIANS", cls="tick192", anchor="start", size=9.5,
                   fill="var(--ink3)"))
    P.add_box(px0, py1 + 30, 110, 14)

    # ---- freely placed annotations ----
    bounds = (6, 6, W - 6, py1 - 2)
    LABELS = [
        (X(0), Y(0.86), "COSINE ON TOP", 100, 14, "var(--fam)", (0, -1)),
        (X(-3 * pi / 8), Y(0.55), "LINE ON TOP", 84, 14, "var(--los)", (-1, -1)),
        (X(3 * pi / 8), Y(0.55), "LINE ON TOP", 84, 14, "var(--los)", (1, -1)),
        (X(-pi / 4), Y(C), "x = -pi/4", 62, 14, "var(--ink)", (-1, 1)),
        (X(pi / 4), Y(C), "x = pi/4", 56, 14, "var(--ink)", (1, 1)),
        (X(-pi / 2 + 0.28), Y(math.cos(-pi / 2 + 0.28)), "y = cos x", 62, 14,
         "var(--ink)", (0, 1)),
        (X(pi / 2 - 0.16), Y(C), "y = 1/sqrt2", 72, 14, "var(--accent)", (0, 1)),
    ]
    clear_report = []
    for (ax, ay, s, w, h, fill, pref) in LABELS:
        cx, cy, cl = P.place(ax, ay, w, h, bounds, pref)
        out.append(txt(cx, cy + h - 3.5, s, cls="lab", anchor="start", size=10.5,
                       weight="600", fill=fill))
        clear_report.append((s, cl))
        # connector, sampled by the gate (its class matches neither grid nor axis)
        sx, sy = _connector_start(cx, cy, w, h, ax, ay)
        if sx is not None:
            out.append('<line class="conn192" x1="%.2f" y1="%.2f" x2="%.2f" y2="%.2f" '
                       'stroke="var(--ink3)" stroke-width="1" stroke-dasharray="2 3"/>'
                       % (sx, sy, ax, ay))

    out.append('</svg>')
    return "\n".join(out), clear_report, (X, Y, px0, py0, px1, py1)


# =================================================================== FIGURE 2
def Ac(c):
    return 4 * sq(max(0.0, 1 - c * c)) - 4 * c * acos(min(1.0, max(-1.0, c))) + pi * c - 2


def figure2():
    W, H = 760, 360
    L, R, T, B = 78, 34, 34, 62
    px0, py0, px1, py1 = L, T, W - R, H - B
    xa, xb = 0.0, 1.0
    ya, yb = 0.70, 2.10

    def X(x):
        return px0 + (x - xa) / (xb - xa) * (px1 - px0)

    def Y(y):
        return py1 - (y - ya) / (yb - ya) * (py1 - py0)

    out = []
    out.append('<svg viewBox="0 0 %d %d" width="100%%" role="img" '
               'aria-label="the area as a function of the line height c, falling to a '
               'minimum at c = 1 over root 2 and rising again">' % (W, H))
    out.append('<rect x="0" y="0" width="%d" height="%d" fill="var(--surface)"/>' % (W, H))
    out.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="var(--surface)" '
               'stroke="var(--line)" stroke-width="1"/>'
               % (px0, py0, px1 - px0, py1 - py0))

    P = Placer(cell=2.0, clear=20.0)
    # 0.25 and 0.75 were dropped: 0.75 sits 0.043 from 1/sqrt2 and the two tick labels
    # collided.  svg-labels measures text.lab only, so it cannot see a TICK collision.
    xticks = [(0.0, "0"), (0.5, "0.5"), (C, "1/sqrt2"), (1.0, "1")]
    yticks = [(0.8284271247461903, "0.828"), (1.0, "1.0"), (1.5, "1.5"), (2.0, "2.0")]
    for xv, _l in xticks:
        out.append('<line class="gridl" x1="%.2f" y1="%.1f" x2="%.2f" y2="%.1f" '
                   'stroke="var(--line)" stroke-width="1" stroke-dasharray="2 4"/>'
                   % (X(xv), py0, X(xv), py1))
    for yv, _l in yticks:
        out.append('<line class="gridl" x1="%.1f" y1="%.2f" x2="%.1f" y2="%.2f" '
                   'stroke="var(--line)" stroke-width="1" stroke-dasharray="2 4"/>'
                   % (px0, Y(yv), px1, Y(yv)))

    # the A(c) = 1 level, and the two points where the curve meets it
    out.append('<line class="lev192" x1="%.1f" y1="%.2f" x2="%.1f" y2="%.2f" '
               'stroke="var(--accent)" stroke-width="1.6" stroke-dasharray="5 4"/>'
               % (px0, Y(1.0), px1, Y(1.0)))
    P.add_seg(px0, Y(1.0), px1, Y(1.0))

    apts = [(X(i / 500.0), Y(Ac(i / 500.0))) for i in range(501)]
    apts = [(x, y) for (x, y) in apts if py0 - 2 <= y <= py1 + 2]
    out.append('<polyline class="acurve192" points="%s" fill="none" stroke="var(--ink)" '
               'stroke-width="2.4"/>' % " ".join("%.2f,%.2f" % p for p in apts))
    P.add_poly(apts)

    def solve(t, lo, hi):
        flo = Ac(lo) - t
        for _ in range(200):
            m = 0.5 * (lo + hi)
            fm = Ac(m) - t
            if flo * fm <= 0:
                hi = m
            else:
                lo, flo = m, fm
        return 0.5 * (lo + hi)

    c1, c2 = solve(1.0, 0.0, C), solve(1.0, C, 1.0)
    for cv, col in ((c1, "var(--los)"), (c2, "var(--los)")):
        out.append('<circle class="dot192" cx="%.2f" cy="%.2f" r="4.5" fill="%s" '
                   'stroke="var(--surface)" stroke-width="1.5"/>' % (X(cv), Y(1.0), col))
        P.add_point(X(cv), Y(1.0))
    out.append('<circle class="dot192" cx="%.2f" cy="%.2f" r="5" fill="var(--fam)" '
               'stroke="var(--surface)" stroke-width="1.5"/>' % (X(C), Y(Ac(C))))
    P.add_point(X(C), Y(Ac(C)))

    for xv, lab in xticks:
        out.append('<line class="axist" x1="%.2f" y1="%.1f" x2="%.2f" y2="%.1f" '
                   'stroke="var(--ink3)" stroke-width="1"/>' % (X(xv), py1, X(xv), py1 + 5))
        out.append(txt(X(xv), py1 + 19, lab, cls="tick192", anchor="middle", size=10.5,
                       fill="var(--ink3)"))
        P.add_box(X(xv) - 30, py1 + 8, 60, 14)
    for yv, lab in yticks:
        out.append('<line class="axist" x1="%.1f" y1="%.2f" x2="%.1f" y2="%.2f" '
                   'stroke="var(--ink3)" stroke-width="1"/>' % (px0 - 5, Y(yv), px0, Y(yv)))
        out.append(txt(px0 - 10, Y(yv) + 3.5, lab, cls="tick192", anchor="end", size=10.5,
                       fill="var(--ink3)"))
        P.add_box(px0 - 52, Y(yv) - 8, 46, 16)
    out.append(txt(px0, py1 + 40, "c  THE LINE HEIGHT", cls="tick192", anchor="start",
                   size=9.5, fill="var(--ink3)"))
    P.add_box(px0, py1 + 30, 140, 14)
    out.append(txt(px1, py1 + 40, "AREA ON THE VERTICAL", cls="tick192", anchor="end",
                   size=9.5, fill="var(--ink3)"))
    P.add_box(px1 - 150, py1 + 30, 150, 14)

    bounds = (6, 6, W - 6, py1 - 2)
    LABELS = [
        (X(C), Y(Ac(C)), "MINIMUM AT c = 1/sqrt2", 148, 14, "var(--fam)", (0, 1)),
        (X(C), Y(Ac(C)), "AREA = 2 sqrt2 - 2 = 0.8284", 168, 14, "var(--fam)", (0, 1)),
        (X(c1), Y(1.0), "c = 0.4489", 68, 14, "var(--los)", (-1, -1)),
        (X(c2), Y(1.0), "c = 0.9349", 68, 14, "var(--los)", (1, -1)),
        (X(0.30), Y(1.0), "AREA = 1 IS MET TWICE", 140, 14, "var(--accent)", (0, -1)),
        (X(0.06), Y(Ac(0.06)), "A(0) = 2", 56, 14, "var(--ink)", (1, 0)),
        (X(0.985), Y(Ac(0.985)), "A(1) = pi - 2", 78, 14, "var(--ink)", (-1, 0)),
    ]
    clear_report = []
    seen_anchors = []
    for (ax, ay, s, w, h, fill, pref) in LABELS:
        cx, cy, cl = P.place(ax, ay, w, h, bounds, pref)
        out.append(txt(cx, cy + h - 3.5, s, cls="lab", anchor="start", size=10.5,
                       weight="600", fill=fill))
        clear_report.append((s, cl))
        # one anchor gets ONE connector: a second line to the same point would have to
        # cross the first label to get there, which svg-labels correctly reports
        dup = any(math.hypot(ax - qx, ay - qy) < 3.0 for (qx, qy) in seen_anchors)
        seen_anchors.append((ax, ay))
        if dup:
            continue
        sx, sy = _connector_start(cx, cy, w, h, ax, ay)
        if sx is not None:
            out.append('<line class="conn192" x1="%.2f" y1="%.2f" x2="%.2f" y2="%.2f" '
                       'stroke="var(--ink3)" stroke-width="1" stroke-dasharray="2 3"/>'
                       % (sx, sy, ax, ay))
    out.append('</svg>')
    return "\n".join(out), clear_report


if __name__ == "__main__":
    s1, r1, geo = figure1()
    s2, r2 = figure2()
    print("figure 1 labels placed: %d" % len(r1))
    for s, cl in r1:
        print("   %-28s clearance %.1f px" % (s, cl))
    print("figure 2 labels placed: %d" % len(r2))
    for s, cl in r2:
        print("   %-28s clearance %.1f px" % (s, cl))
    print("min clearance fig1 %.1f, fig2 %.1f"
          % (min(c for _s, c in r1), min(c for _s, c in r2)))
