"""The Q10.2 figure: the whole curve, the tangent at (1,1), and every special point.

The curve y^3 + y x^2 + x^2 = 3 y^2 is drawn from its EXPLICIT branch
    x = +- y sqrt((3-y)/(1+y)),   -1 < y <= 3
which is exact, so no root-finding is needed and no sample point can drift off
the curve.  Every plotted point therefore satisfies the relation by construction.

Markup contract for Work\\knowledge\\tools\\artifact-lint\\svg-labels.mjs:
  - the wrapper carries class "figbox"
  - every <text> to be checked carries class "lab"
  - every grid <line> carries class="gridl" (a bare <line> reports tagName
    "line", which does NOT match the gate's /grid|axis/ exemption)
"""
import io
import math
import os

W, H = 780, 570
L, R, T, B = 62, 22, 20, 48
X0, X1 = -2.75, 2.75
Y0, Y1 = -2.35, 3.75


def sx(x):
    return L + (x - X0) / (X1 - X0) * (W - L - R)


def sy(y):
    return T + (Y1 - y) / (Y1 - Y0) * (H - T - B)


def f(v):
    return ("%.2f" % v).rstrip("0").rstrip(".")


def xb(y, s):
    """The exact branch. Returns None outside the domain."""
    d = 1.0 + y
    if d <= 1e-12 or y > 3.0:
        return None
    u = (3.0 - y) / d
    if u < 0:
        return None
    return s * abs(y) * math.sqrt(u)


SEGS = []          # every line the label gate will sample, in screen coords


def seg(x1, y1, x2, y2):
    SEGS.append((x1, y1, x2, y2))


def poly(lo, hi, s, n=460):
    """Sample one branch over y in (lo, hi], clipped to the plot box."""
    pts = []
    for i in range(n + 1):
        y = lo + (hi - lo) * i / n
        x = xb(y, s)
        if x is None or not (X0 - 0.4 <= x <= X1 + 0.4) or not (Y0 - 0.4 <= y <= Y1 + 0.4):
            if pts:
                yield pts
                pts = []
            continue
        pts.append("%.1f,%.1f" % (sx(x), sy(y)))
    if pts:
        yield pts


def _rec(pts):
    for i in range(len(pts) - 1):
        x1, y1 = (float(v) for v in pts[i].split(","))
        x2, y2 = (float(v) for v in pts[i + 1].split(","))
        seg(x1, y1, x2, y2)


o = []
a = o.append
a('<div class="figbox">')
a('<svg viewBox="0 0 %d %d" width="100%%" role="img" '
  'aria-label="The curve y cubed plus y x squared plus x squared equals 3 y squared, '
  'with its tangent line at the point (1,1)">' % (W, H))

# ---- grid ------------------------------------------------------------------
a('<g stroke="var(--line)" stroke-width="1">')
gx = -2
while gx <= 2.5:
    if abs(gx) > 1e-9:
        a('<line class="gridl" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>'
          % (sx(gx), T, sx(gx), H - B))
    gx += 1
gy = -2
while gy <= 3.5:
    if abs(gy) > 1e-9:
        a('<line class="gridl" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>'
          % (L, sy(gy), W - R, sy(gy)))
    gy += 1
a("</g>")

# ---- axes ------------------------------------------------------------------
a('<g stroke="var(--ink3)" stroke-width="1.3">')
a('<line class="axis" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>' % (L, sy(0), W - R, sy(0)))
a('<line class="axis" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>' % (sx(0), T, sx(0), H - B))
a("</g>")

# ---- axis ticks ------------------------------------------------------------
a('<g class="tick" fill="var(--ink3)" font-size="11.5" text-anchor="middle">')
for v in (-2, -1, 1, 2):
    a('<text x="%.1f" y="%.1f">%s</text>' % (sx(v), sy(0) + 15, v))
a("</g>")
a('<g class="tick" fill="var(--ink3)" font-size="11.5" text-anchor="end">')
for v in (-2, -1, 1, 2, 3):
    a('<text x="%.1f" y="%.1f">%s</text>' % (sx(0) - 7, sy(v) + 4, v))
a("</g>")

# ---- the curve -------------------------------------------------------------
# The closed loop is y in [0,3]; the two unbounded arms are y in (-1,0).
a('<g fill="none" stroke="var(--chn)" stroke-width="2.4" stroke-linecap="round">')
for s in (+1, -1):
    for sg in poly(0.0, 3.0, s):
        a('<polyline class="curve" points="%s"/>' % " ".join(sg))
        _rec(sg)
a("</g>")
a('<g fill="none" stroke="var(--chn)" stroke-width="2.4" stroke-linecap="round" '
  'stroke-opacity="0.85">')
for s in (+1, -1):
    for sg in poly(-0.985, 0.0, s):
        a('<polyline class="curve" points="%s"/>' % " ".join(sg))
        _rec(sg)
a("</g>")

# ---- the tangent line y = 2x - 1 -------------------------------------------
tx0, tx1 = -0.62, 1.72
a('<line class="tang" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" '
  'stroke="var(--rul)" stroke-width="2.4"/>'
  % (sx(tx0), sy(2 * tx0 - 1), sx(tx1), sy(2 * tx1 - 1)))
seg(sx(tx0), sy(2 * tx0 - 1), sx(tx1), sy(2 * tx1 - 1))

# ---- vertical-tangent markers ----------------------------------------------
r3 = math.sqrt(3.0)
xv = xb(r3, +1)
a('<g stroke="var(--los)" stroke-width="1.4" stroke-dasharray="5 4">')
for s in (+1, -1):
    a('<line class="vert" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>'
      % (sx(s * xv), sy(0.62), sx(s * xv), sy(2.72)))
    seg(sx(s * xv), sy(0.62), sx(s * xv), sy(2.72))
a("</g>")

# ---- points ----------------------------------------------------------------
def dot(x, y, cls, r=5.2):
    a('<circle class="%s" cx="%.1f" cy="%.1f" r="%.1f"/>' % (cls, sx(x), sy(y), r))


a('<g fill="var(--rul)" stroke="var(--surface)" stroke-width="2">')
dot(1, 1, "pt-main", 6.4)
a("</g>")
a('<g fill="var(--num)" stroke="var(--surface)" stroke-width="2">')
dot(0.4, -0.2, "pt-again")
a("</g>")
a('<g fill="var(--fam)" stroke="var(--surface)" stroke-width="2">')
dot(0, 3, "pt-horiz")
a("</g>")
a('<g fill="var(--los)" stroke="var(--surface)" stroke-width="2">')
dot(xv, r3, "pt-vert")
dot(-xv, r3, "pt-vert")
a("</g>")
a('<g fill="var(--ink2)" stroke="var(--surface)" stroke-width="2">')
dot(0, 0, "pt-sing")
a("</g>")

# ---- labels.  Keep ~14px clear of any line the gate samples. ---------------
a('<g class="labs" font-size="12.5" font-weight="500">')
print("label placement (measured against every drawn segment):")


CW, ASC, DESC, CLEAR = 7.15, 10.0, 4.0, 15.0   # char width, ascent, descent, required gap
CELL = 8.0

# Rasterise every drawn segment into a spatial hash once, then every candidate
# placement is a constant-time lookup instead of a scan over ~1800 segments.
INK = {}
for (x1, y1, x2, y2) in SEGS:
    n = max(2, int(math.hypot(x2 - x1, y2 - y1) / 1.5) + 1)
    for i in range(n + 1):
        u = i / n
        px, py = x1 + u * (x2 - x1), y1 + u * (y2 - y1)
        INK.setdefault((int(px // CELL), int(py // CELL)), []).append((px, py))


def _box(cx, cy, txt, anchor):
    w = CW * len(txt)
    x0 = cx if anchor == "start" else (cx - w if anchor == "end" else cx - w / 2)
    return x0, cy - ASC, x0 + w, cy + DESC


def clearance(cx, cy, txt, anchor):
    """Smallest distance from the label's box to any inked pixel, capped at CLEAR."""
    bx0, by0, bx1, by1 = _box(cx, cy, txt, anchor)
    if bx0 < L + 2 or bx1 > W - R - 2 or by0 < T + 2 or by1 > H - B - 2:
        return -1.0
    best = 1e9
    c0, c1 = int((bx0 - CLEAR) // CELL), int((bx1 + CLEAR) // CELL)
    r0, r1 = int((by0 - CLEAR) // CELL), int((by1 + CLEAR) // CELL)
    for cc in range(c0, c1 + 1):
        for rr in range(r0, r1 + 1):
            for (px, py) in INK.get((cc, rr), ()):
                dx = 0.0 if bx0 <= px <= bx1 else min(abs(px - bx0), abs(px - bx1))
                dy = 0.0 if by0 <= py <= by1 else min(abs(py - by0), abs(py - by1))
                d = math.hypot(dx, dy)
                if d < best:
                    best = d
                    if best <= 0:
                        return 0.0
    return best


PLACED = []


def place(ax, ay, txt, fill, prefer=(1, -1)):
    """Put txt near the data point (ax,ay), at the nearest spot clearing every line."""
    px, py = sx(ax), sy(ay)
    best = None
    for rad in range(14, 210, 4):
        for ang in range(0, 360, 5):
            th = math.radians(ang)
            ox, oy = rad * math.cos(th), -rad * math.sin(th)
            if prefer[0] * ox < -20 or prefer[1] * oy < -20:
                continue
            for anchor in ("start", "end", "middle"):
                cx, cy = px + ox, py + oy
                if clearance(cx, cy, txt, anchor) < CLEAR:
                    continue
                bx0, by0, bx1, by1 = _box(cx, cy, txt, anchor)
                if any(not (bx1 + 8 < q[0] or bx0 - 8 > q[2]
                            or by1 + 6 < q[1] or by0 - 6 > q[3]) for q in PLACED):
                    continue
                if best is None or rad < best[0]:
                    best = (rad, cx, cy, anchor)
        if best is not None:
            break
    assert best is not None, "no clear placement for %r" % txt
    _, cx, cy, anchor = best
    PLACED.append(_box(cx, cy, txt, anchor))
    a('<text class="lab" x="%.1f" y="%.1f" text-anchor="%s" fill="%s">%s</text>'
      % (cx, cy, anchor, fill, txt))
    print("  %-26s at (%3.0f,%3.0f) anchor=%-6s clearance %.1fpx, %dpx from its point"
          % (txt, cx, cy, anchor, clearance(cx, cy, txt, anchor), best[0]))


place(1, 1, "(1, 1)", "var(--rul)", prefer=(-1, -1))
place(1.72, 2 * 1.72 - 1, "y = 2x - 1", "var(--rul)", prefer=(1, 1))
place(0, 3, "(0, 3) horizontal tangent", "var(--fam)", prefer=(1, -1))
place(xv, r3, "vertical tangent", "var(--los)", prefer=(1, 1))
place(-xv, r3, "vertical tangent", "var(--los)", prefer=(-1, 1))
place(0.4, -0.2, "(2/5, -1/5)", "var(--num)", prefer=(1, 1))
place(0, 0, "(0, 0) singular", "var(--ink2)", prefer=(-1, 1))
a("</g>")

a("</svg>")
a("</div>")

svg = "\n".join(o)
bad = [hex(ord(c)) for c in svg if ord(c) < 32 and c not in "\n\r\t"]
assert not bad, "control characters: %s" % bad
assert all(ord(c) < 127 for c in svg), sorted({c for c in svg if ord(c) > 126})
assert svg.count("<svg") == 1
assert 'class="gridl"' in svg and 'class="lab"' in svg and 'class="figbox"' in svg

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_q102_fig.svg")
io.open(out, "w", encoding="utf-8", newline="\n").write(svg)
print("wrote", out, len(svg), "bytes")
print("vertical tangent at x = %.6f, y = %.6f" % (xv, r3))
print("polylines:", svg.count("<polyline"))
