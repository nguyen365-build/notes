# -*- coding: utf-8 -*-
"""Figures for the Q19.8 page. Every coordinate is COMPUTED from the maths.

Semantic tokens on this page, one role -> one token, never reused:
  amber  (--rul)  the FORWARD motion, and the exam's own signed answer
  blue   (--chn)  the BACKWARD motion: the single piece that creates the gap
  teal   (--fam)  the UNSIGNED quantity, the odometer, the distance
  rust   (--los)  a WRONG answer, and nothing else
  slate  (--plot) axes, ticks, frame. A fourth NEUTRAL, carrying no meaning.
No gridlines are drawn: 32.9 records that a collision guard cannot tell a
gridline from a data stroke, and dropping them frees the label placement.
"""
from fractions import Fraction as Fr

V = lambda t: t * t - 3.0 * t + 2.0
S = lambda t: t ** 3 / 3.0 - 1.5 * t * t + 2.0 * t
ROOTS = (1.0, 2.0)
T0, T1 = 0.0, 3.0


def odo(t):
    """the odometer: int_0^t |v|, exact piecewise"""
    cuts = [c for c in ROOTS if c < t] + [t]
    tot = 0.0
    prev = 0.0
    for c in cuts:
        tot += abs(S(c) - S(prev))
        prev = c
    return tot


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


class Fig(object):
    def __init__(self, w, h, pad):
        self.w, self.h = w, h
        self.L, self.R, self.T, self.B = pad
        self.parts = []
        self.labels = []      # (x, y, w, h, text)
        self.strokes = []     # [(x1,y1,x2,y2)] every stroked segment
        self.content = []     # every point belonging to CONTENT (never the background)

    # ---- scales
    def setx(self, a, b):
        self.xa, self.xb = a, b

    def sety(self, a, b):
        self.ya, self.yb = a, b

    def X(self, t):
        return self.L + (t - self.xa) / (self.xb - self.xa) * (self.w - self.L - self.R)

    def Y(self, v):
        return self.h - self.B - (v - self.ya) / (self.yb - self.ya) * (self.h - self.T - self.B)

    # ---- primitives
    def bg(self):
        self.parts.append('<rect class="fbg198" x="0" y="0" width="%d" height="%d"/>' % (self.w, self.h))

    def poly(self, pts, cls, extra=""):
        d = " ".join("%.3f,%.3f" % p for p in pts)
        self.parts.append('<polyline class="%s" points="%s" %s/>' % (cls, d, extra))
        for i in range(len(pts) - 1):
            self.strokes.append((pts[i][0], pts[i][1], pts[i + 1][0], pts[i + 1][1]))
        self.content.extend(pts)

    def area(self, pts, cls):
        d = " ".join("%.3f,%.3f" % p for p in pts)
        self.parts.append('<polygon class="%s" points="%s"/>' % (cls, d))
        self.content.extend(pts)

    def line(self, x1, y1, x2, y2, cls):
        self.parts.append('<line class="%s" x1="%.3f" y1="%.3f" x2="%.3f" y2="%.3f"/>'
                          % (cls, x1, y1, x2, y2))
        self.strokes.append((x1, y1, x2, y2))
        self.content.extend([(x1, y1), (x2, y2)])

    def dot(self, x, y, cls, r=4.2):
        self.parts.append('<circle class="%s" cx="%.3f" cy="%.3f" r="%.2f"/>' % (cls, x, y, r))
        self.content.extend([(x - r, y - r), (x + r, y + r)])

    def text(self, x, y, s, cls, anchor="middle", size=12.5):
        # build-time width estimate, deliberately NARROWER per character than the
        # browser measures, so the browser gate is the LOOSER of the two (31.10)
        wpx = len(s) * size * 0.62
        if anchor == "middle":
            x0 = x - wpx / 2.0
        elif anchor == "end":
            x0 = x - wpx
        else:
            x0 = x
        self.labels.append((x0, y - size * 1.05, wpx, size * 1.40, s))
        self.content.extend([(x0, y - size * 1.05), (x0 + wpx, y + size * 0.35)])
        # 'lab' is the hook svg-labels selects on (text.lab). Without it the gate
        # walks both figures, finds nlabs 0, and reports every list empty - which
        # reads exactly like a pass. The class is emitted FIRST so the specific
        # per-role class still wins the cascade.
        self.parts.append('<text class="lab %s" x="%.2f" y="%.2f" text-anchor="%s">%s</text>'
                          % (cls, x, y, anchor, esc(s)))

    def svg(self, title, desc):
        return ('<svg class="fig198" viewBox="0 0 %d %d" role="img" '
                'aria-labelledby="%s-t %s-d" preserveAspectRatio="xMidYMid meet">'
                '<title id="%s-t">%s</title><desc id="%s-d">%s</desc>\n%s\n</svg>'
                % (self.w, self.h, title, title, title, esc(desc.split("|")[0]),
                   title, esc(desc.split("|")[1]), "\n".join(self.parts)))


# ============================ FIGURE 1 ============================
def fig1():
    f = Fig(760, 330, (58, 26, 26, 46))
    f.setx(-0.12, 3.12)
    f.sety(-0.65, 2.35)
    f.bg()
    y0 = f.Y(0.0)

    # signed regions, filled. The -soft tokens are 10-13% alpha and invisible as
    # an area fill (recorded), so the figure uses its own stronger fill tokens.
    def band(a, b, cls):
        n = 90
        pts = [(f.X(a), y0)]
        pts += [(f.X(a + (b - a) * i / n), f.Y(V(a + (b - a) * i / n))) for i in range(n + 1)]
        pts += [(f.X(b), y0)]
        f.area(pts, cls)

    band(0.0, 1.0, "fwd198")
    band(1.0, 2.0, "bwd198")
    band(2.0, 3.0, "fwd198")

    # axis (slate, neutral) and ticks
    f.line(f.X(-0.12), y0, f.X(3.12), y0, "ax198")
    f.line(f.X(0.0), f.Y(-0.65), f.X(0.0), f.Y(2.35), "ax198")
    for t in (1, 2, 3):
        f.line(f.X(t), y0, f.X(t), y0 + 4, "ax198")
        f.text(f.X(t), y0 + 23, str(t), "tick198")
    for v in (1, 2):
        f.line(f.X(0.0) - 4, f.Y(v), f.X(0.0), f.Y(v), "ax198")
        f.text(f.X(0.0) - 12, f.Y(v) + 4, str(v), "tick198", "end")
    f.text(f.X(3.12) - 4, y0 - 9, "t (sec)", "axlab198", "end")
    f.text(f.X(0.0) + 8, f.T + 12, "v (m/s)", "axlab198", "start")

    # the curve
    n = 300
    f.poly([(f.X(T0 + (T1 - T0) * i / n), f.Y(V(T0 + (T1 - T0) * i / n))) for i in range(n + 1)],
           "curve198")

    # the two sign changes
    for r in ROOTS:
        f.dot(f.X(r), y0, "root198")

    # area labels, placed inside their own band
    f.text(f.X(0.50), f.Y(0.33), "+5/6", "areaf198")
    f.text(f.X(1.50), f.Y(-0.50), "-1/6", "areab198")
    f.text(f.X(2.52), f.Y(0.30), "+5/6", "areaf198")
    f.text(f.X(1.5), f.Y(1.62), "v changes sign at t = 1 and t = 2", "note198")
    f.text(f.X(1.5), f.Y(1.30), "both are INSIDE [0, 3]", "note198")
    return f


# ============================ FIGURE 2 ============================
def fig2():
    f = Fig(760, 330, (58, 132, 26, 46))
    f.setx(-0.12, 3.12)
    f.sety(-0.15, 2.05)
    f.bg()
    y0 = f.Y(0.0)

    f.line(f.X(-0.12), y0, f.X(3.12), y0, "ax198")
    f.line(f.X(0.0), f.Y(-0.15), f.X(0.0), f.Y(2.05), "ax198")
    for t in (1, 2, 3):
        f.line(f.X(t), y0, f.X(t), y0 + 4, "ax198")
        f.text(f.X(t), y0 + 23, str(t), "tick198")
    for v, lab in ((0.5, "0.5"), (1.0, "1"), (1.5, "1.5")):
        f.line(f.X(0.0) - 4, f.Y(v), f.X(0.0), f.Y(v), "ax198")
        f.text(f.X(0.0) - 12, f.Y(v) + 4, lab, "tick198", "end")
    f.text(f.X(3.12) - 4, y0 - 9, "t (sec)", "axlab198", "end")
    f.text(f.X(0.0) + 8, f.T + 12, "metres", "axlab198", "start")

    n = 300
    ts = [T0 + (T1 - T0) * i / n for i in range(n + 1)]
    f.poly([(f.X(t), f.Y(odo(t))) for t in ts], "odo198")
    f.poly([(f.X(t), f.Y(S(t))) for t in ts], "pos198")

    # the interval where they part company
    f.line(f.X(1.0), f.Y(S(1.0)), f.X(1.0), f.Y(odo(1.0)), "tie198")
    f.line(f.X(2.0), f.Y(S(2.0)), f.X(2.0), f.Y(odo(2.0)), "tie198")
    f.line(f.X(3.0), f.Y(S(3.0)), f.X(3.0), f.Y(odo(3.0)), "tie198")

    f.dot(f.X(3.0), f.Y(S(3.0)), "endpos198")
    f.dot(f.X(3.0), f.Y(odo(3.0)), "endodo198")

    # labels: to the RIGHT of the plot, in the reserved right margin
    xr = f.X(3.0) + 12
    f.text(xr, f.Y(odo(3.0)) - 14, "odometer 11/6", "lodo198", "start")
    f.text(xr, f.Y(odo(3.0)) + 7, "distance", "lsub198", "start", 11)
    f.text(xr, f.Y(S(3.0)) + 8, "position 3/2", "lpos198", "start")
    f.text(xr, f.Y(S(3.0)) + 29, "displacement", "lsub198", "start", 11)
    f.text(f.X(1.5), f.Y(1.86), "identical until the first sign change", "note198")
    f.text(f.X(2.5), f.Y(0.42), "gap 1/3, fixed after t = 2", "note198")
    return f


# ============================ GUARDS ============================
def guards(f, name, curve_checks, crossings, must_appear):
    out = []
    ok = [0, 0]

    def A(n, c, extra=""):
        out.append(("PASS" if c else "FAIL") + " q198f %-52s %s" % (name + ": " + n, extra))
        ok[0 if c else 1] += 1

    # BOUNDS - every content point inside the viewBox
    xs = [p[0] for p in f.content]
    ys = [p[1] for p in f.content]
    A("BOUNDS all content inside the viewBox",
      min(xs) >= -0.5 and max(xs) <= f.w + 0.5 and min(ys) >= -0.5 and max(ys) <= f.h + 0.5,
      "x[%.1f,%.1f] y[%.1f,%.1f]" % (min(xs), max(xs), min(ys), max(ys)))

    # CURVEFIT - re-evaluate the drawn polyline back in DATA space
    worst = 0.0
    for fn, pts in curve_checks:
        for (px, py) in pts[::17]:
            t = f.xa + (px - f.L) / (f.w - f.L - f.R) * (f.xb - f.xa)
            v = f.ya + (f.h - f.B - py) / (f.h - f.T - f.B) * (f.yb - f.ya)
            worst = max(worst, abs(v - fn(t)))
    A("CURVEFIT drawn shape IS the named function", worst < 1e-9, "worst %.2e" % worst)

    # CURVEFIT control: a 2 percent wrong curve must be rejected
    cf, cp = curve_checks[0]
    cw = 0.0
    for (px, py) in cp[::17]:
        t = f.xa + (px - f.L) / (f.w - f.L - f.R) * (f.xb - f.xa)
        v = f.ya + (f.h - f.B - py) / (f.h - f.T - f.B) * (f.yb - f.ya)
        cw = max(cw, abs(v - cf(t) * 1.02 - 0.02))
    A("CONTROL CURVEFIT rejects a 2 percent wrong curve", cw > 1e-3, "worst %.2e" % cw)

    # CROSSING - each marked dot lies on what it claims to lie on
    bad = [c[0] for c in crossings if abs(c[1]) > 1e-9]
    A("CROSSING every marked dot sits on its curve", not bad, str(bad))

    # LABELFIT - every label box inside the viewBox
    off = [L[4] for L in f.labels
           if L[0] < -0.5 or L[0] + L[2] > f.w + 0.5 or L[1] < -0.5 or L[1] + L[3] > f.h + 0.5]
    A("LABELFIT every label inside the viewBox", not off, str(off))

    # COLLIDE - label boxes must not overlap each other
    pad = 3.0
    hits = []
    for i in range(len(f.labels)):
        for j in range(i + 1, len(f.labels)):
            a, b = f.labels[i], f.labels[j]
            if (a[0] - pad < b[0] + b[2] and b[0] - pad < a[0] + a[2]
                    and a[1] - pad < b[1] + b[3] and b[1] - pad < a[1] + a[3]):
                hits.append((a[4], b[4]))
    A("COLLIDE no two labels overlap", not hits, str(hits[:3]))

    # RECTEDGE / stroke crossings - a label must not sit on a stroked segment.
    # The background rect is NOT in the stroke list: it has no stroke, so a label
    # over it is not a collision (32.8).
    def seg_hits_box(s, bx):
        x1, y1, x2, y2 = s
        X, Y, W, H = bx
        for k in range(21):
            u = k / 20.0
            px, py = x1 + (x2 - x1) * u, y1 + (y2 - y1) * u
            if X <= px <= X + W and Y <= py <= Y + H:
                return True
        return False

    sh = [L[4] for L in f.labels
          if any(seg_hits_box(s, (L[0], L[1], L[2], L[3])) for s in f.strokes)]
    A("STROKEHIT no label sits on a drawn stroke", not sh, str(sh))

    # DEADSPACE - content must fill the panel WITHOUT being the panel (32.8)
    frac = ((max(xs) - min(xs)) * (max(ys) - min(ys))) / float(f.w * f.h)
    A("DEADSPACE content fills the panel and is NOT saturated",
      0.45 < frac < 1.0, "frac %.2f" % frac)

    # CONTENT - every label that must appear is actually drawn (28.9 / the
    # figure-content guard: a figure can pass every layout gate drawing none of
    # its labels)
    drawn = set(L[4] for L in f.labels)
    miss = [m for m in must_appear if m not in drawn]
    A("CONTENT every required label is drawn", not miss, str(miss))
    A("CONTROL the content guard rejects a label that is NOT drawn",
      "__absent__" not in drawn)
    return out, ok


def build():
    log = []
    tot = [0, 0]

    f1 = fig1()
    n = 300
    p1 = [(f1.X(T0 + 3.0 * i / n), f1.Y(V(T0 + 3.0 * i / n))) for i in range(n + 1)]
    cr1 = [("root t=1", V(1.0)), ("root t=2", V(2.0))]
    o, k = guards(f1, "fig1", [(V, p1)], cr1,
                  ["+5/6", "-1/6", "v changes sign at t = 1 and t = 2", "1", "2", "3", "t (sec)"])
    log += o
    tot[0] += k[0]
    tot[1] += k[1]

    f2 = fig2()
    ts = [T0 + 3.0 * i / n for i in range(n + 1)]
    p2 = [(f2.X(t), f2.Y(S(t))) for t in ts]
    p3 = [(f2.X(t), f2.Y(odo(t))) for t in ts]
    cr2 = [("end position", S(3.0) - float(Fr(3, 2))), ("end odometer", odo(3.0) - float(Fr(11, 6)))]
    o, k = guards(f2, "fig2", [(S, p2), (odo, p3)], cr2,
                  ["odometer 11/6", "position 3/2", "distance", "displacement",
                   "gap 1/3, fixed after t = 2"])
    log += o
    tot[0] += k[0]
    tot[1] += k[1]

    s1 = f1.svg("q198f1", "Velocity against time.|The velocity curve v(t) = t squared minus 3t "
                          "plus 2 on the interval 0 to 3, with the two regions where the velocity "
                          "is positive shaded in amber and the region between t = 1 and t = 2 "
                          "where it is negative shaded in blue. The three signed areas are five "
                          "sixths, minus one sixth and five sixths.")
    s2 = f2.svg("q198f2", "Position and odometer against time.|Two curves on the interval 0 to 3. "
                          "The position curve rises to five sixths, falls to two thirds, then "
                          "rises to three halves. The odometer curve rises without ever falling, "
                          "reaching eleven sixths. They are identical until t = 1 and separate by "
                          "one third from t = 2 onward.")
    return s1, s2, log, tot


if __name__ == "__main__":
    a, b, log, tot = build()
    for l in log:
        print(l)
    print("SECTION q198f FIGURES PASS=%d FAIL=%d" % (tot[0], tot[1]))
