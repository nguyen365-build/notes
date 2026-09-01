"""Geometry for the Q10.1 artifact figure, computed from the real curve.

One figure, one argument: above a single x the curve has TWO points with TWO
different slopes, so no formula in x alone could report both.  That is the
whole case for keeping y in the answer.
"""
import math, io, os

def branch(x, s):
    b = x**3 - 4*x
    D = b*b + 28*x
    return (-b + s*math.sqrt(D)) / (2*x)

def dydx(x, y):
    return y*(4 - 3*x*x - y) / (x*(x*x + 2*y - 4))

# ---- plot window -----------------------------------------------------------
X0, X1 = 0.42, 3.30
Y0, Y1 = -7.2, 8.6
W, H = 720.0, 400.0
L, R, T, B = 46.0, 16.0, 16.0, 34.0     # margins
PW, PH = W - L - R, H - T - B

def sx(x):
    return L + (x - X0) / (X1 - X0) * PW

def sy(y):
    return T + (Y1 - y) / (Y1 - Y0) * PH

def poly(s, n=340):
    pts = []
    for i in range(n + 1):
        x = X0 + (X1 - X0) * i / n
        y = branch(x, s)
        if Y0 - 3 <= y <= Y1 + 3:
            pts.append("%.2f,%.2f" % (sx(x), sy(y)))
    return " ".join(pts)

up = poly(+1)
lo = poly(-1)

# ---- the two points above x = 2 -------------------------------------------
XP = 2.0
yA, yB = branch(XP, +1), branch(XP, -1)
mA, mB = dydx(XP, yA), dydx(XP, yB)

def tangent(x0, y0, m, half=0.62):
    a = (x0 - half, y0 - m*half)
    b = (x0 + half, y0 + m*half)
    return "%.2f,%.2f %.2f,%.2f" % (sx(a[0]), sy(a[1]), sx(b[0]), sy(b[1]))

tA = tangent(XP, yA, mA)
tB = tangent(XP, yB, mB)

# ---- axes and ticks --------------------------------------------------------
xt = [1, 2, 3]
yt = [-6, -4, -2, 0, 2, 4, 6, 8]

out = []
A = out.append
A('<svg viewBox="0 0 %g %g" width="100%%" style="max-width:%gpx;height:auto" '
  'role="img" aria-label="The curve x cubed y plus x y squared equals 4xy plus 7. '
  'Above x = 2 the curve has two points, at y = plus and minus root 14 over 2, with '
  'two different tangent slopes.">' % (W, H, W))

# grid
for v in yt:
    A('<line class="gridl" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>'
      % (L, sy(v), L + PW, sy(v)))
for v in xt:
    A('<line class="gridl" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>'
      % (sx(v), T, sx(v), T + PH))

# axes
A('<line class="axis" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>' % (L, sy(0), L + PW, sy(0)))
A('<line class="axis" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>' % (L, T, L, T + PH))

# tick labels
for v in xt:
    A('<text class="tl lab" x="%.1f" y="%.1f" text-anchor="middle">%d</text>'
      % (sx(v), T + PH + 14, v))
for v in yt:
    if v == 0:
        continue
    A('<text class="tl lab" x="%.1f" y="%.1f" text-anchor="end">%d</text>'
      % (L - 6, sy(v) + 3.4, v))
A('<text class="tl lab" x="%.1f" y="%.1f" text-anchor="end">0</text>' % (L - 6, sy(0) + 3.4))
A('<text class="tl lab" x="%.1f" y="%.1f" text-anchor="middle">x</text>' % (L + PW, T + PH + 28))
A('<text class="tl lab" x="%.1f" y="%.1f" text-anchor="middle">y</text>' % (L - 30, T + 8))

# the vertical cut at x = 2
A('<line class="lev" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>'
  % (sx(XP), sy(yA) - 4, sx(XP), T + PH - 26))

# the two branches
A('<polyline class="curve" points="%s"/>' % up)
A('<polyline class="curve" points="%s"/>' % lo)

# tangents
A('<polyline class="tang" points="%s"/>' % tA)
A('<polyline class="tang" points="%s"/>' % tB)

# points
A('<circle class="dot" cx="%.2f" cy="%.2f" r="4.2"/>' % (sx(XP), sy(yA)))
A('<circle class="dot" cx="%.2f" cy="%.2f" r="4.2"/>' % (sx(XP), sy(yB)))

# annotations, placed clear of the curve
A('<text class="al lab" x="%.1f" y="%.1f" fill="var(--rul)">slope %.4f</text>'
  % (sx(XP) + 14, sy(yA) - 12, mA))
# the lower branch descends steeply to the right of x=2, so this label goes
# down-and-LEFT into the empty wedge under the branch's flat stretch.
A('<text class="al lab" x="%.1f" y="%.1f" text-anchor="end" fill="var(--rul)">slope %.4f</text>'
  % (sx(XP) - 16, sy(yB) + 30, mB))
A('<text class="al lab" x="%.1f" y="%.1f" fill="var(--ink3)">upper branch</text>'
  % (sx(2.72), sy(branch(2.72, +1)) - 14))
A('<text class="al lab" x="%.1f" y="%.1f" text-anchor="end" fill="var(--ink3)">lower branch</text>'
  % (sx(1.35), sy(branch(1.35, -1)) + 22))
A('<text class="al lab" x="%.1f" y="%.1f" text-anchor="middle" fill="var(--los)">'
  'one x, two slopes</text>' % (sx(XP), T + PH - 4))
A('</svg>')

svg = "".join(out)
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_q101_fig.svg")
io.open(path, "w", encoding="utf-8", newline="\n").write(svg)

print("y(2)  = %+.7f and %+.7f" % (yA, yB))
print("y'(2) = %+.7f and %+.7f" % (mA, mB))
print("exact check: -2 - sqrt14/8 = %+.7f ; -2 + sqrt14/8 = %+.7f"
      % (-2 - math.sqrt(14)/8, -2 + math.sqrt(14)/8))
print("upper branch spans y in [%.2f, %.2f] over the window"
      % (branch(X1, +1), branch(X0, +1)))
print("lower branch spans y in [%.2f, %.2f] over the window"
      % (branch(X0, -1), branch(X1, -1)))
print("svg bytes:", len(svg), "->", path)
print("non-ascii bytes in svg:", sum(1 for c in svg if ord(c) > 126))
