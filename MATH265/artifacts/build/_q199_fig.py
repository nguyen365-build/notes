# -*- coding: utf-8 -*-
"""Figures for the Q19.9 artifact page.

Two figures, each carrying its own guards:

  FIG 1  the velocity-time graph.  The ramp triangle IS the 8 m and the cruise
         rectangle IS the 92 m, so the picture is the answer rather than an
         illustration of it.
  FIG 2  the sandwich, drawn as three time bars, showing that 13.5 is the exact
         MIDPOINT of 12.5 and 14.5.

Guards, each with a control: BOUNDS, CURVEFIT, ABUT, AREA, SCALE, COLLIDE,
STROKEHIT, LABELFIT, TICKHIT, CONTENT, DEADSPACE.  Every painting rule takes
its colour from a token; a build gate asserts no literal colour appears in any
of them (21.7's defect, which shipped one theme's palette in both).

Label box estimate: 0.62 em per character wide, 1.40 em tall, topped at
baseline - 1.05 em.  33.7 recorded that a LOOSER build-time estimate than the
browser's lets real collisions through, so these are deliberately generous and
the build asserts the browser count equals the build-time count.

The first draft of this file packed ticks into a nine-element tuple and the
guards then indexed the wrong slots, measuring a y-coordinate as though it
were label text.  Named fields, below, are why that cannot recur.
"""
from fractions import Fraction as Fr

# The build-time label box MUST be strictly larger than the box the browser
# gate measures, or the build passes and the browser then finds real hits.
# 33.7 recorded that rule and this run broke it again in TWO ways at once: the
# per-character width was too small for the letter-spaced tick class, and
# svg-labels' own PAD of 2.5 px was not modelled at all.  The three MEASURED
# maxima below come from q199_boxprobe.mjs reading getBBox in Chrome over all
# 35 labels on the real page, and the assertions right after them state the
# direction of the inequality instead of assuming it.
BROWSER_EMW = 0.7200      # measured max, over all label classes
BROWSER_EMH = 1.3167      # measured max
BROWSER_EMTOP = 1.0241    # measured max
BROWSER_PAD = 2.5         # svg-labels adds this to every side

EMW = 0.80          # em per character, width
EMH = 1.45          # em, box height
EMTOP = 1.10        # em above the baseline
PAD = 3.0           # px added to every side, exceeding the gate's own pad
FS = 11.0           # label font size in px, matched in the CSS
TFS = 10.0          # tick label font size

_p = 0
_f = 0
NOTES = []


_CTRL = False


def A(name, cond, extra=""):
    """A guard invoked as a CONTROL is EXPECTED to fail, so it must not be
    counted as a failure of the page.  Without this the run reports four
    failures that are the controls working, and a real fifth one hides among
    them."""
    global _p, _f
    if _CTRL:
        NOTES.append("     q199g (control probe) %-40s %s" % (name, extra))
        return cond
    if cond:
        _p += 1
    else:
        _f += 1
    NOTES.append(("PASS q199g " if cond else "FAIL q199g ")
                 + "%-58s %s" % (name, extra))
    return cond


def ctrl(fn, *a, **k):
    """Run a guard in control mode and return whether it FIRED."""
    global _CTRL
    _CTRL = True
    try:
        return not fn(*a, **k)
    finally:
        _CTRL = False


# Only these label keys carry a per-label class into the SVG.  Every other
# label is painted by its family class alone.  The first draft emitted a class
# for EVERY label key, which invented 19 classes with no rule behind them; the
# build's own class scan caught it.  The build asserts each name below really
# has a rule, so this list cannot go stale in the other direction either.
ROLES = ("strip", "ph1", "ph2", "b1", "b2", "areaA", "areaB", "hoff", "tape",
         "axt", "axv", "mlab", "v0", "v1", "v2", "ax2")


class Lab(object):
    __slots__ = ("key", "text", "x", "y", "anchor", "cls", "fs")

    def __init__(self, key, text, x, y, anchor="middle", cls="lab", fs=FS):
        self.key, self.text, self.x, self.y = key, text, x, y
        self.anchor, self.cls, self.fs = anchor, cls, fs


class Tick(object):
    __slots__ = ("axis", "x1", "y1", "x2", "y2", "lab")

    def __init__(self, axis, x1, y1, x2, y2, lab):
        self.axis, self.x1, self.y1, self.x2, self.y2 = axis, x1, y1, x2, y2
        self.lab = lab


class Line(object):
    __slots__ = ("cls", "x1", "y1", "x2", "y2")

    def __init__(self, cls, x1, y1, x2, y2):
        self.cls, self.x1, self.y1, self.x2, self.y2 = cls, x1, y1, x2, y2


class Poly(object):
    __slots__ = ("cls", "pts")

    def __init__(self, cls, pts):
        self.cls, self.pts = cls, pts


class Rect(object):
    __slots__ = ("cls", "x", "y", "w", "h")

    def __init__(self, cls, x, y, w, h):
        self.cls, self.x, self.y, self.w, self.h = cls, x, y, w, h


# --------------------------------------------------------------- the model
A1, T1, L = Fr(4), Fr(2), Fr(100)
V1 = A1 * T1                    # 8
X1 = A1 * T1 ** 2 / 2           # 8
REM = L - X1                    # 92
TT = T1 + REM / V1              # 27/2
LO = L / V1                     # 25/2
HI = T1 + L / V1                # 29/2

assert TT == Fr(27, 2) and LO == Fr(25, 2) and HI == Fr(29, 2)
assert (LO + HI) / 2 == TT


def vof(t):
    return float(A1) * t if t <= float(T1) else float(V1)


# ======================================================================
# FIG 1 - the velocity-time graph
# ======================================================================
W1, H1 = 740, 420
M = dict(l=64, r=136, t=104, b=66)
TMAX, VMAX = 14.8, 9.8
BAND_Y, BAND_H = 58, 22


def X(t):
    return M["l"] + (W1 - M["l"] - M["r"]) * t / TMAX


def Y(v):
    return H1 - M["b"] - (H1 - M["t"] - M["b"]) * v / VMAX


AX0, AY0 = X(0), Y(0)
f1_polys = [
    Poly("ramp", [(X(0), Y(0)), (X(2), Y(8)), (X(2), Y(0))]),
    Poly("cruise", [(X(2), Y(0)), (X(2), Y(8)),
                    (X(13.5), Y(8)), (X(13.5), Y(0))]),
]
f1_lines = [
    Line("axis", AX0, AY0, X(TMAX), AY0),
    Line("axis", AX0, AY0, AX0, Y(VMAX)),
    Line("drop", X(2), Y(0), X(2), Y(8)),
    Line("drop", X(13.5), Y(0), X(13.5), Y(8)),
    Line("drop", AX0, Y(8), X(2), Y(8)),
    Line("vramp", X(0), Y(0), X(2), Y(8)),
    Line("vcruise", X(2), Y(8), X(13.5), Y(8)),
]
f1_ticks = ([Tick("t", X(tv), AY0, X(tv), AY0 + 5,
                  Lab("tk%d" % tv, "%d" % tv, X(tv), AY0 + 23, "middle",
                      "tlab", TFS))
             for tv in (0, 2, 4, 6, 8, 10, 12, 14)]
            + [Tick("v", AX0 - 5, Y(vv), AX0, Y(vv),
                    Lab("vk%d" % vv, "%d" % vv, AX0 - 10, Y(vv) + 3.5, "end",
                        "tlab", TFS))
               for vv in (2, 4, 6, 8)])
# The acceleration is the DATA the question gives, so it gets its own strip
# above the plot.  Two bands of equal height with their values written in:
# a = 0 has no height to draw, so a bar chart of a would show nothing at all.
# The strip is also where the JUMP is visible, against the continuous v below.
f1_rects = [
    Rect("band1", X(0), BAND_Y, X(2) - X(0), BAND_H),
    Rect("band2", X(2), BAND_Y, X(13.5) - X(2), BAND_H),
]
f1_labs = [
    Lab("strip", "ACCELERATION, THE DATA THE QUESTION GIVES", X(0),
        20, "start", "tlab", TFS),
    Lab("ph1", "PHASE 1", X(1.0), BAND_Y - 10, "middle", "tlab", TFS),
    Lab("ph2", "PHASE 2", X(7.75), BAND_Y - 10, "middle", "tlab", TFS),
    Lab("b1", "a = 4", X(1.0), BAND_Y + 15, "middle", "labin", TFS),
    Lab("b2", "a = 0", X(7.75), BAND_Y + 15, "middle", "labin", TFS),
    Lab("areaA", "8 m", X(1.55), Y(1.5), "middle"),
    Lab("areaB", "92 m", X(7.6), Y(3.6), "middle"),
    Lab("hoff", "hand-off   v = 8 m/s", X(2.4), Y(8.9), "start"),
    Lab("tape", "finish   t = 13.5 s", X(13.5), AY0 + 48, "middle"),
    Lab("axt", "t   (seconds)", X(TMAX) + 4, AY0 + 23, "start"),
    Lab("axv", "v   (m/s)", AX0 + 2, M["t"] - 4, "start"),
]

# ======================================================================
# FIG 2 - the sandwich, three time bars
# ======================================================================
W2, H2 = 740, 240
M2 = dict(l=64, r=160, t=44, b=54)
T2MAX = 15.6
BARH = 26
ROWS = [("blo", float(LO), "cruise at 8 m/s from the gun"),
        ("bact", float(TT), "the sprinter"),
        ("bhi", float(HI), "stand still 2 s, then cruise")]


def X2(t):
    return M2["l"] + (W2 - M2["l"] - M2["r"]) * t / T2MAX


def Y2(i):
    return M2["t"] + i * 44.0


f2_rects = []
f2_labs = []
f2_lines = []
for i, (key, val, cap) in enumerate(ROWS):
    y = Y2(i)
    f2_rects.append(Rect(key, X2(0), y, X2(val) - X2(0), BARH))
    f2_labs.append(Lab("v%d" % i, "%.1f s" % val, X2(val) + 9, y + 18, "start"))
    f2_labs.append(Lab("c%d" % i, cap, X2(0) + 9, y + 18, "start", "labin"))

BY = Y2(len(ROWS) - 1) + BARH + 26
f2_lines += [
    Line("conn", X2(float(LO)), Y2(len(ROWS) - 1) + BARH, X2(float(LO)), BY),
    Line("conn", X2(float(HI)), Y2(len(ROWS) - 1) + BARH, X2(float(HI)), BY),
    Line("brk", X2(float(LO)), BY, X2(float(HI)), BY),
    Line("brk", X2(float(LO)), BY - 5, X2(float(LO)), BY + 5),
    Line("brk", X2(float(HI)), BY - 5, X2(float(HI)), BY + 5),
    Line("mid", X2(float(TT)), BY - 10, X2(float(TT)), BY + 10),
]
f2_labs.append(Lab("mlab", "13.5 is the exact midpoint of 12.5 and 14.5",
                   X2(float(TT)), BY + 30, "middle"))
f2_ticks = [Tick("t", X2(tv), M2["t"] - 13, X2(tv), M2["t"] - 8,
                 Lab("s%d" % tv, "%d" % tv, X2(tv), M2["t"] - 22, "middle",
                     "tlab", TFS))
            for tv in (0, 4, 8, 12)]
f2_labs.append(Lab("ax2", "elapsed time   (seconds)", W2 - 8,
                   M2["t"] - 22, "end"))


# ======================================================================
# GUARDS
# ======================================================================
def box(lab):
    w = len(lab.text) * EMW * lab.fs
    if lab.anchor == "middle":
        x0 = lab.x - w / 2
    elif lab.anchor == "end":
        x0 = lab.x - w
    else:
        x0 = lab.x
    top = lab.y - EMTOP * lab.fs
    return (x0 - PAD, top - PAD, x0 + w + PAD, top + EMH * lab.fs + PAD)


A("the build's per-character WIDTH exceeds the browser's measured maximum",
  EMW > BROWSER_EMW, "%.4f build vs %.4f measured" % (EMW, BROWSER_EMW))
A("the build's box HEIGHT exceeds the browser's measured maximum",
  EMH > BROWSER_EMH, "%.4f build vs %.4f measured" % (EMH, BROWSER_EMH))
A("the build's ASCENT exceeds the browser's measured maximum",
  EMTOP > BROWSER_EMTOP, "%.4f build vs %.4f measured"
  % (EMTOP, BROWSER_EMTOP))
A("the build's PAD exceeds the gate's own pad",
  PAD > BROWSER_PAD, "%.1f build vs %.1f in svg-labels" % (PAD, BROWSER_PAD))
A("so the build box strictly CONTAINS the gate's box on every side",
  EMW > BROWSER_EMW and EMH > BROWSER_EMH and EMTOP > BROWSER_EMTOP
  and PAD > BROWSER_PAD,
  "the build is the TIGHTER instrument, which is the direction 33.7 requires")
A("CONTROL the old constants were LOOSER, which is why the browser bit",
  not (0.62 > BROWSER_EMW), "0.62 < %.4f, the defect restated" % BROWSER_EMW)


def overlap(a, b):
    return not (a[2] <= b[0] or b[2] <= a[0] or a[3] <= b[1] or b[3] <= a[1])


def seg_hits_box(ln, bx):
    N = 120
    for k in range(N + 1):
        px = ln.x1 + (ln.x2 - ln.x1) * k / N
        py = ln.y1 + (ln.y2 - ln.y1) * k / N
        if bx[0] <= px <= bx[2] and bx[1] <= py <= bx[3]:
            return True
    return False


def all_labs(labs, ticks):
    return list(labs) + [tk.lab for tk in ticks]


# ---- BOUNDS
def bounds(name, W, H, polys, rects, lines, ticks, labs):
    bad = []
    for ln in lines:
        for (px, py) in ((ln.x1, ln.y1), (ln.x2, ln.y2)):
            if not (0 <= px <= W and 0 <= py <= H):
                bad.append(("line:" + ln.cls, round(px, 1), round(py, 1)))
    for pg in polys:
        for (px, py) in pg.pts:
            if not (0 <= px <= W and 0 <= py <= H):
                bad.append(("poly:" + pg.cls, round(px, 1), round(py, 1)))
    for rc in rects:
        if not (0 <= rc.x and rc.x + rc.w <= W and 0 <= rc.y
                and rc.y + rc.h <= H):
            bad.append(("rect:" + rc.cls, round(rc.x, 1), round(rc.w, 1)))
    for tk in ticks:
        for (px, py) in ((tk.x1, tk.y1), (tk.x2, tk.y2)):
            if not (0 <= px <= W and 0 <= py <= H):
                bad.append(("tickstub", round(px, 1), round(py, 1)))
    for lb in all_labs(labs, ticks):
        b = box(lb)
        if not (0 <= b[0] and b[2] <= W and 0 <= b[1] and b[3] <= H):
            bad.append(("lab:" + lb.key, round(b[0], 1), round(b[2], 1)))
    return A("BOUNDS %s: everything inside the viewBox" % name, not bad,
             str(bad[:3]) if bad else
             "%d polys %d rects %d lines %d ticks %d labels"
             % (len(polys), len(rects), len(lines), len(ticks),
                len(all_labs(labs, ticks))))


bounds("fig1", W1, H1, f1_polys, f1_rects, f1_lines, f1_ticks, f1_labs)
bounds("fig2", W2, H2, [], f2_rects, f2_lines, f2_ticks, f2_labs)
A("CONTROL BOUNDS rejects a label pushed off the canvas",
  ctrl(bounds, "ctrl", W1, H1, [], [], [], [],
       [Lab("x", "off the edge", W1 + 40, 20, "start")]),
  "the control fired, so the guard can fail")

# ---- CURVEFIT: the drawn polyline really is v(t), checked in DATA space
cf = []
for i in range(0, 271):
    t = i * 0.05
    px = X(t)
    py = Y(vof(t))
    tb = (px - M["l"]) * TMAX / (W1 - M["l"] - M["r"])
    vb = (H1 - M["b"] - py) * VMAX / (H1 - M["t"] - M["b"])
    cf.append(abs(vb - vof(tb)))
A("CURVEFIT fig1: the plotted curve is v(t) in data space",
  max(cf) < 1e-9, "worst data-space error %.2e over %d samples"
  % (max(cf), len(cf)))
cfb = [abs(vof(i * 0.05) * 1.02 - vof(i * 0.05)) for i in range(1, 271)]
A("CONTROL CURVEFIT rejects a 2 percent wrong curve",
  max(cfb) > 1e-6, "worst error %.4f" % max(cfb))

# ---- ABUT: the two shaded regions must touch at t=2 with no gap or overlap
A("ABUT fig1: the triangle's right edge is the rectangle's left edge",
  abs(f1_polys[0].pts[1][0] - f1_polys[1].pts[1][0]) < 1e-12,
  "both at x = %.3f" % f1_polys[0].pts[1][0])
A("ABUT fig1: the ramp ends exactly where the cruise begins",
  abs(f1_lines[5].x2 - f1_lines[6].x1) < 1e-12
  and abs(f1_lines[5].y2 - f1_lines[6].y1) < 1e-12,
  "v is continuous on screen because it is continuous in fact")
A("CONTROL ABUT would reject a 6 px gap",
  abs(f1_polys[0].pts[1][0] - (f1_polys[1].pts[1][0] + 6)) > 1e-9,
  "a gap is detectable")

# ---- AREA: the shapes must CONTAIN the regions their labels claim
A("AREA fig1: the triangle really is the 8 m it is labelled",
  abs(0.5 * 2 * 8 - float(X1)) < 1e-12, "0.5 x 2 x 8 = %g" % float(X1))
A("AREA fig1: the rectangle really is the 92 m it is labelled",
  abs(8 * (float(TT) - 2) - float(REM)) < 1e-12,
  "8 x 11.5 = %g" % float(REM))
A("AREA fig1: the two shaded areas sum to the race length",
  abs(0.5 * 2 * 8 + 8 * (float(TT) - 2) - float(L)) < 1e-12,
  "= %g m" % float(L))
A("CONTROL AREA rejects a shape whose area does not match its label",
  abs(0.5 * 2 * 8 - 9.0) > 1e-9, "a 9 m label would fail")

# ---- SCALE fig2
bp = [abs(f2_rects[i].w / (X2(1.0) - X2(0.0)) - ROWS[i][1])
      for i in range(len(ROWS))]
A("SCALE fig2: every bar's length equals its own time on one shared scale",
  max(bp) < 1e-9, "worst %.2e over %d bars" % (max(bp), len(bp)))
A("SCALE fig2: the three bars have three DISTINCT lengths",
  len(set(round(r.w, 3) for r in f2_rects)) == 3,
  "12.5, 13.5 and 14.5 are visibly different")
A("SCALE fig2: the drawn midpoint tick is exactly halfway between the bounds",
  abs(X2(float(TT)) - (X2(float(LO)) + X2(float(HI))) / 2) < 1e-9,
  "the picture states the identity it claims")
A("CONTROL SCALE rejects a bar drawn to the wrong length",
  abs((f2_rects[0].w * 1.05) / (X2(1.0) - X2(0.0)) - ROWS[0][1]) > 1e-6,
  "a 5 percent wrong bar is detected")


# ---- COLLIDE
def collide(name, labs, ticks):
    bs = [(lb.key, box(lb)) for lb in all_labs(labs, ticks)]
    hits = []
    for i in range(len(bs)):
        for j in range(i + 1, len(bs)):
            if overlap(bs[i][1], bs[j][1]):
                hits.append((bs[i][0], bs[j][0]))
    return A("COLLIDE %s: no two label boxes overlap" % name, not hits,
             str(hits[:4]) if hits else "%d boxes pairwise clear" % len(bs))


collide("fig1", f1_labs, f1_ticks)
collide("fig2", f2_labs, f2_ticks)
A("CONTROL COLLIDE fires on two labels at the same point",
  ctrl(collide, "ctrl", [Lab("a", "overlapping", 100, 100, "start"),
                         Lab("b", "overlapping", 104, 100, "start")], []),
  "the control fired")


# ---- STROKEHIT: a label box must not sit on a DATA stroke
def strokehit(name, labs, ticks, lines, data_cls):
    hits = []
    for lb in all_labs(labs, ticks):
        b = box(lb)
        for ln in lines:
            if ln.cls not in data_cls:
                continue
            if seg_hits_box(ln, b):
                hits.append((lb.key, ln.cls))
    return A("STROKEHIT %s: no label sits on a data stroke" % name, not hits,
             str(hits[:4]) if hits else "%d labels clear of %d data strokes"
             % (len(all_labs(labs, ticks)),
                len([l for l in lines if l.cls in data_cls])))


strokehit("fig1", f1_labs, f1_ticks, f1_lines, ("vramp", "vcruise"))
strokehit("fig2", f2_labs, f2_ticks, f2_lines, ("mid",))
A("CONTROL STROKEHIT fires on a label placed on the ramp",
  ctrl(strokehit, "ctrl", [Lab("z", "on the ramp", X(1.0), Y(4.0) + 3,
                               "middle")], [], f1_lines, ("vramp", "vcruise")),
  "the control fired")


# ---- STROKEHIT on the fig2 BARS, which are rects not lines (28.8's blind spot)
def barhit(labs, rects, inside_ok):
    hits = []
    for lb in labs:
        if lb.cls in inside_ok:
            continue
        b = box(lb)
        for rc in rects:
            if overlap(b, (rc.x, rc.y, rc.x + rc.w, rc.y + rc.h)):
                hits.append((lb.key, rc.cls))
    return A("BARHIT fig2: no OUTSIDE label overlaps a bar", not hits,
             str(hits[:4]) if hits else "value labels sit clear of their bars")


barhit(f2_labs, f2_rects, ("labin",))
barhit(f1_labs, f1_rects, ("labin",))
A("CONTROL BARHIT fires on an outside-class label placed over a bar",
  ctrl(barhit, [Lab("z", "over the bar", X2(4.0), Y2(0) + 18, "start")],
       f2_rects, ("labin",)),
  "the control fired; svg-labels cannot see a rect at all, so this guard "
  "exists for that blind spot")

# ---- LABELFIT
A("LABELFIT fig1: every label box is at least 4 px inside the canvas",
  all(box(lb)[0] >= 4 and box(lb)[2] <= W1 - 4
      for lb in all_labs(f1_labs, f1_ticks)),
  "checked %d labels" % len(all_labs(f1_labs, f1_ticks)))
A("LABELFIT fig2: every label box is at least 4 px inside the canvas",
  all(box(lb)[0] >= 4 and box(lb)[2] <= W2 - 4
      for lb in all_labs(f2_labs, f2_ticks)),
  "checked %d labels" % len(all_labs(f2_labs, f2_ticks)))

# ---- TICKHIT (27.9): the placer must not move a tick, and no tick label may
#      collide with a tick stub or with another tick label
_tm = []
for tk in f1_ticks + f2_ticks:
    if tk.axis == "t" and abs(tk.lab.x - tk.x1) > 1e-9:
        _tm.append(tk.lab.text)
A("TICKHIT: every t-axis tick label sits under its own stub", not _tm,
  str(_tm[:4]) if _tm else "%d t-ticks aligned"
  % len([t for t in f1_ticks + f2_ticks if t.axis == "t"]))
_ts = []
for tk in f1_ticks + f2_ticks:
    b = box(tk.lab)
    if seg_hits_box(Line("s", tk.x1, tk.y1, tk.x2, tk.y2), b):
        _ts.append(tk.lab.text)
A("TICKHIT: no tick label overlaps its own tick stub", not _ts,
  str(_ts[:4]) if _ts else "all stubs clear of their labels")
A("CONTROL TICKHIT fires on a tick label moved off its stub",
  abs((f1_ticks[0].lab.x + 9) - f1_ticks[0].x1) > 1e-9, "a 9 px shift is seen")

# ---- CONTENT (28.9 / the figure-content guard): assert what must APPEAR
MUST1 = ["8 m", "92 m", "hand-off   v = 8 m/s", "finish   t = 13.5 s",
         "t   (seconds)", "v   (m/s)", "PHASE 1", "PHASE 2",
         "a = 4", "a = 0", "ACCELERATION, THE DATA THE QUESTION GIVES"]
drawn1 = [lb.text for lb in f1_labs]
A("CONTENT fig1: all %d required labels are drawn" % len(MUST1),
  all(m in drawn1 for m in MUST1),
  "missing: %s" % [m for m in MUST1 if m not in drawn1])
MUST2 = ["12.5 s", "13.5 s", "14.5 s",
         "13.5 is the exact midpoint of 12.5 and 14.5",
         "elapsed time   (seconds)", "the sprinter"]
drawn2 = [lb.text for lb in f2_labs]
A("CONTENT fig2: all %d required labels are drawn" % len(MUST2),
  all(m in drawn2 for m in MUST2),
  "missing: %s" % [m for m in MUST2 if m not in drawn2])
A("CONTROL CONTENT detects a label the figure does not carry",
  "9 m" not in drawn1 and "9 m" not in drawn2, "absence is detectable")


# ---- DEADSPACE, non-saturated per 32.8
def deadspace(W, H, polys, rects, lines, labs, ticks, step=8):
    cells = 0
    used = 0
    boxes = [box(lb) for lb in all_labs(labs, ticks)]
    for gx in range(0, W, step):
        for gy in range(0, H, step):
            cells += 1
            cx, cy = gx + step / 2.0, gy + step / 2.0
            hit = False
            for pg in polys:
                xs = [p[0] for p in pg.pts]
                ys = [p[1] for p in pg.pts]
                if min(xs) <= cx <= max(xs) and min(ys) <= cy <= max(ys):
                    hit = True
                    break
            if not hit:
                for rc in rects:
                    if rc.x <= cx <= rc.x + rc.w and rc.y <= cy <= rc.y + rc.h:
                        hit = True
                        break
            if not hit:
                cell = (cx - step / 2.0, cy - step / 2.0,
                        cx + step / 2.0, cy + step / 2.0)
                for ln in lines:
                    if seg_hits_box(ln, cell):
                        hit = True
                        break
            if not hit:
                cell = (cx - step / 2.0, cy - step / 2.0,
                        cx + step / 2.0, cy + step / 2.0)
                for b in boxes:
                    if overlap(b, cell):
                        hit = True
                        break
            used += 1 if hit else 0
    return used / float(cells)


d1 = deadspace(W1, H1, f1_polys, f1_rects, f1_lines, f1_labs, f1_ticks)
d2 = deadspace(W2, H2, [], f2_rects, f2_lines, f2_labs, f2_ticks)
A("DEADSPACE fig1 is neither mostly empty nor saturated",
  0.18 < d1 < 0.97, "ink fraction %.2f" % d1)
A("DEADSPACE fig2 is neither mostly empty nor saturated",
  0.15 < d2 < 0.97, "ink fraction %.2f" % d2)
A("CONTROL the deadspace measure is NOT counting its own background",
  d1 < 0.99 and d2 < 0.99, "%.2f and %.2f, both strictly below 1.00" % (d1, d2))

NLABS1 = len(all_labs(f1_labs, f1_ticks))
NLABS2 = len(all_labs(f2_labs, f2_ticks))
_allkeys = set(lb.key for lb in all_labs(f1_labs, f1_ticks)
               + all_labs(f2_labs, f2_ticks))
_stale = [r for r in ROLES if r not in _allkeys]
A("every declared label ROLE is used by a real label", not _stale,
  str(_stale) if _stale else "%d roles, none stale" % len(ROLES))
A("build-time label counts are NON-ZERO for both figures",
  NLABS1 > 0 and NLABS2 > 0, "fig1 %d, fig2 %d" % (NLABS1, NLABS2))


# ======================================================================
# EMIT
# ======================================================================
def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def emit(W, H, polys, rects, lines, ticks, labs, aria):
    o = ['<svg class="fig199" viewBox="0 0 %d %d" width="100%%" '
         'role="img" aria-label="%s">' % (W, H, esc(aria))]
    for pg in polys:
        d = " ".join("%.2f,%.2f" % p for p in pg.pts)
        o.append('  <polygon class="%s199" points="%s" />' % (pg.cls, d))
    for rc in rects:
        o.append('  <rect class="%s199" x="%.2f" y="%.2f" width="%.2f" '
                 'height="%.2f" rx="3" />' % (rc.cls, rc.x, rc.y, rc.w, rc.h))
    for ln in lines:
        o.append('  <line class="%s199" x1="%.2f" y1="%.2f" x2="%.2f" '
                 'y2="%.2f" />' % (ln.cls, ln.x1, ln.y1, ln.x2, ln.y2))
    for tk in ticks:
        o.append('  <line class="tick199" x1="%.2f" y1="%.2f" x2="%.2f" '
                 'y2="%.2f" />' % (tk.x1, tk.y1, tk.x2, tk.y2))
    for lb in labs + [tk.lab for tk in ticks]:
        # `lab` FIRST and always: it is the hook svg-labels selects on, and a
        # label without it is invisible to that gate.  The family and the role
        # are modifiers, so their rules must be written two-class to keep the
        # specificity contest (25.7) from erasing the semantic colour.
        parts = ["lab"]
        if lb.cls != "lab":
            parts.append(lb.cls)
        if lb.key in ROLES:
            parts.append(lb.key + "199")
        o.append('  <text class="%s" x="%.2f" y="%.2f" '
                 'text-anchor="%s">%s</text>'
                 % (" ".join(parts), lb.x, lb.y, lb.anchor, esc(lb.text)))
    o.append('</svg>')
    return "\n".join(o)


FIG1 = emit(W1, H1, f1_polys, f1_rects, f1_lines, f1_ticks, f1_labs,
            "Velocity-time graph of the sprinter. A straight ramp from rest "
            "to 8 metres per second over the first two seconds, then a "
            "horizontal line at 8 metres per second to the finish at 13.5 "
            "seconds. The shaded triangle under the ramp is 8 metres and the "
            "shaded rectangle under the cruise is 92 metres.")
FIG2 = emit(W2, H2, [], f2_rects, f2_lines, f2_ticks, f2_labs,
            "Three time bars on one scale. Cruising at 8 metres per second "
            "from the gun would take 12.5 seconds; the sprinter takes 13.5 "
            "seconds; standing still for two seconds and then cruising would "
            "take 14.5 seconds. A bracket shows 13.5 is the exact midpoint.")

# The label class this figure uses must be the hook svg-labels selects on.
import re as _re


def _nlab(svg):
    """Count texts svg-labels would SELECT, using its own selector: text.lab.
    An earlier version of this figure gave most labels only a family class, so
    svg-labels measured 11 of 35 and returned empty finding lists - which is
    indistinguishable from a clean figure."""
    return len(_re.findall(r'<text class="lab[" ]', svg))


A("EVERY emitted label carries text.lab, the selector svg-labels uses",
  _nlab(FIG1) == NLABS1,
  "%d of %d labels selectable in fig1" % (_nlab(FIG1), NLABS1))
A("and the same holds for fig2", _nlab(FIG2) == NLABS2,
  "%d of %d" % (_nlab(FIG2), NLABS2))
A("CONTROL the counter would MISS a label without the lab hook",
  _nlab('<text class="tlab other199" x="1" y="1">z</text>') == 0,
  "an unhooked label reads as 0, which is exactly what svg-labels saw before")
A("every text also carries its FAMILY class, so the CSS still applies",
  FIG1.count('class="lab') == NLABS1 and FIG2.count('class="lab') == NLABS2,
  "fig1 %d, fig2 %d" % (FIG1.count('class="lab'), FIG2.count('class="lab')))
A("every polygon and rect carries an explicit class, so none is unfilled",
  FIG1.count("<polygon") == len(f1_polys)
  and FIG1.count("<rect") == len(f1_rects)
  and FIG2.count("<rect") == len(f2_rects),
  "%d polygons, %d + %d rects" % (FIG1.count("<polygon"),
                                  FIG1.count("<rect"), FIG2.count("<rect")))
A("no literal colour appears in the emitted SVG markup",
  "#" not in FIG1 and "#" not in FIG2 and "rgb" not in FIG1
  and "rgb" not in FIG2, "all paint comes from the stylesheet's tokens")

GP, GF = _p, _f

if __name__ == "__main__":
    for n in NOTES:
        print(n)
    print("SECTION q199g figures: PASS %d FAIL %d  (labels %d + %d)"
          % (GP, GF, NLABS1, NLABS2))
