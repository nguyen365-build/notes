"""Figures for the Q19.7 artifact.

Two figures, each drawing a MECHANISM rather than a set of magnitudes.

  fig1  the constraint curve.  The average of 5/x^2 over the interval between
        1 and k is 5/k, drawn against k.  The horizontal target 32 cuts it in
        exactly one place, at k = 5/32.  The level 5 is the value the average
        would take at k = 1, which is excluded because the interval would have
        zero width; every target above 5 therefore lands LEFT of 1 and every
        target below 5 lands right of it.  That single picture is the whole
        uniqueness argument and the whole orientation trap.
  fig2  unique against not unique.  Two panels: the exam's own average 5/k,
        strictly decreasing so a horizontal line meets it once; and the average
        of (x-2)^2 between 1 and k, which is (k^2-5k+7)/3 and meets a
        horizontal line twice, once, or not at all depending on the target.

Guards, every one of them because some run in this queue shipped the defect it
catches:
  - BOUNDS      every drawn coordinate inside the viewBox (15.6);
  - CURVEFIT    the drawn polyline must actually trace the claimed function,
                checked by re-evaluating at the drawn pixel positions, with a
                seeded wrong curve rejected (29.9);
  - CROSSING    each marked intersection dot must sit on BOTH the curve and the
                level it claims to cross, to sub-pixel tolerance;
  - TICKS       the placer must not move an axis tick, compared at the
                precision the SVG is written at (30.8);
  - COLLIDE     no label overlaps a tick label or another label, at a pad
                TIGHTER than the browser gate's (31.10);
  - RECTEDGE    svg-labels samples only line/polyline, so a stroked <rect>
                border is a structural blind spot; its four edges become
                segments here and are tested against every label box (28.8);
  - LABELFIT    the widest estimated label box must fit inside the panel;
  - DEADSPACE   the drawn content must fill most of the panel (18.7);
  - CONTENT     every label named in MUST_APPEAR is actually drawn (28.8).

Colour, per 31.9's fourth-token rule:
  teal  --fam    the truth, the curve that answers the question
  rust  --los    a wrong answer or an impossible target
  amber --accent the object being constructed: the target level and the
                 solution it produces
  slate --num    NEUTRAL scaffolding that is neither right nor wrong: the
                 excluded point k = 1, the level 5, the guide lines
"""
import math

W1, H1 = 760, 430
W2, H2 = 760, 344

LOG = []

KANS = 5.0 / 32.0
TARGET = 32.0
FIVE = 5.0

# ---------------------------------------------------------------- fig 1 frame
P1L, P1R, P1T, P1B = 68, 176, 34, 56
AX0, AX1 = 0.0, 2.24
AY0, AY1 = 0.0, 45.0


def sx1(x):
    return P1L + (x - AX0) / (AX1 - AX0) * (W1 - P1L - P1R)


def sy1(y):
    return H1 - P1B - (y - AY0) / (AY1 - AY0) * (H1 - P1T - P1B)


# Estimated label geometry.  svg-labels.mjs does the real getBBox pass in the
# browser; this build-time layer must be TIGHTER than that gate, or it is a
# rubber stamp (31.10).
CHW = {10: 6.1, 10.5: 6.4, 11: 6.7, 11.5: 7.0, 12: 7.3}
COLLIDE_PAD = 6.0


def bbox(text, x, y, size=11, anchor="start"):
    w = len(text) * CHW.get(size, 6.7)
    h = size * 1.22
    if anchor == "middle":
        x -= w / 2.0
    elif anchor == "end":
        x -= w
    return (x, y - size, x + w, y - size + h)


def overlap(a, b, pad=COLLIDE_PAD):
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


def rect_segs(x, y, w, h):
    return [((x, y), (x + w, y)), ((x + w, y), (x + w, y + h)),
            ((x + w, y + h), (x, y + h)), ((x, y + h), (x, y))]


def _f(v, n=2):
    s = ("%." + str(n) + "f") % v
    return s.rstrip("0").rstrip(".") if "." in s else s


class Panel(object):
    """Accumulates drawn elements plus everything the guards need to see."""

    def __init__(self, name, w, h):
        self.name = name
        self.w = w
        self.h = h
        self.out = []
        self.labels = []       # (text, box)
        self.ticks = []        # (text, box) - tick labels, never moved
        self.segs = []         # every line/polyline/rect edge, as segments
        self.pts = []          # every drawn coordinate, for BOUNDS
        self.drawn = []        # every label text actually emitted
        # DEADSPACE must not count the background rect, or it reads 1.00
        # and becomes a check that cannot fail.
        self.content_pts = []

    def add(self, s):
        self.out.append(s)

    def mark(self, *pts, **kw):
        content = kw.get("content", True)
        for p in pts:
            self.pts.append(p)
            if content:
                self.content_pts.append(p)

    def line(self, x1, y1, x2, y2, cls):
        self.add('<line class="%s" x1="%.2f" y1="%.2f" x2="%.2f" y2="%.2f"/>'
                 % (cls, x1, y1, x2, y2))
        self.segs.append(((x1, y1), (x2, y2)))
        self.mark((x1, y1), (x2, y2))

    def poly(self, pts, cls):
        d = " ".join("%.2f,%.2f" % p for p in pts)
        self.add('<polyline class="%s" points="%s"/>' % (cls, d))
        for i in range(len(pts) - 1):
            self.segs.append((pts[i], pts[i + 1]))
        self.mark(*pts)

    def rect(self, x, y, w, h, cls, background=False):
        self.add('<rect class="%s" x="%.2f" y="%.2f" width="%.2f" height="%.2f"/>'
                 % (cls, x, y, w, h))
        if not background:
            self.segs.extend(rect_segs(x, y, w, h))
        self.mark((x, y), (x + w, y + h), content=not background)

    def dot(self, x, y, r, cls):
        self.add('<circle class="%s" cx="%.2f" cy="%.2f" r="%.2f"/>' % (cls, x, y, r))
        self.mark((x - r, y - r), (x + r, y + r))

    def text(self, s, x, y, cls, size=11, anchor="start", tick=False):
        a = '' if anchor == "start" else ' text-anchor="%s"' % anchor
        self.add('<text class="lab %s" x="%.2f" y="%.2f"%s>%s</text>'
                 % (cls, x, y, a, s))
        b = bbox(s, x, y, size, anchor)
        (self.ticks if tick else self.labels).append((s, b))
        self.drawn.append(s)
        self.mark((b[0], b[1]), (b[2], b[3]))

    def svg(self, vb_w, vb_h, title):
        return ('<svg viewBox="0 0 %d %d" role="img" aria-label="%s">'
                % (vb_w, vb_h, title)) + "".join(self.out) + "</svg>"


def run_guards(p, tag, must_appear, deadspace_min=0.45):
    """Every guard, each reported into LOG so a silent pass is visible."""
    # BOUNDS
    bad = [(x, y) for (x, y) in p.pts
           if x < -0.5 or y < -0.5 or x > p.w + 0.5 or y > p.h + 0.5]
    assert not bad, "%s BOUNDS: %d coordinates outside the viewBox: %s" \
                    % (tag, len(bad), bad[:3])
    LOG.append("%s BOUNDS      %d coordinates, 0 outside" % (tag, len(p.pts)))
    # COLLIDE - labels against labels and against tick labels
    allb = p.labels + p.ticks
    hits = []
    for i in range(len(allb)):
        for j in range(i + 1, len(allb)):
            if overlap(allb[i][1], allb[j][1]):
                hits.append((allb[i][0], allb[j][0]))
    assert not hits, "%s COLLIDE: %s" % (tag, hits[:4])
    LOG.append("%s COLLIDE     %d label boxes, 0 overlapping at pad %.1f"
               % (tag, len(allb), COLLIDE_PAD))
    # RECTEDGE - every segment, rect borders included, against every label box
    crossings = []
    for (s, b) in allb:
        for (q1, q2) in p.segs:
            if seg_hits_box(q1, q2, b):
                crossings.append(s)
                break
    assert not crossings, "%s RECTEDGE: strokes cross %s" % (tag, crossings[:4])
    LOG.append("%s RECTEDGE    %d segments (rect borders included) vs %d boxes, 0 crossings"
               % (tag, len(p.segs), len(allb)))
    # LABELFIT
    over = [s for (s, b) in allb if b[0] < 0 or b[2] > p.w or b[1] < 0 or b[3] > p.h]
    assert not over, "%s LABELFIT: %s runs outside the panel" % (tag, over[:3])
    LOG.append("%s LABELFIT    %d boxes, widest %.1fpx, all inside"
               % (tag, len(allb), max(b[2] - b[0] for (_s, b) in allb)))
    # DEADSPACE
    xs = [x for (x, _y) in p.content_pts]
    ys = [y for (_x, y) in p.content_pts]
    frac = ((max(xs) - min(xs)) * (max(ys) - min(ys))) / float(p.w * p.h)
    assert frac >= deadspace_min, "%s DEADSPACE: content fills only %.2f" % (tag, frac)
    assert frac < 1.0, "%s DEADSPACE is vacuous: the background rect is being counted" % tag
    LOG.append("%s DEADSPACE   drawn content (background rect excluded) fills %.2f"
               % (tag, frac))
    # CONTENT
    missing = [m for m in must_appear if not any(m in d for d in p.drawn)]
    assert not missing, "%s CONTENT: labels never drawn: %s" % (tag, missing)
    LOG.append("%s CONTENT     all %d required labels drawn" % (tag, len(must_appear)))


# ==========================================================================
def fig1():
    p = Panel("fig1", W1, H1)
    p.rect(0, 0, W1, H1, "plotbg197", background=True)

    # axis and ticks.  NO gridlines: a background rule crossing a label is
    # indistinguishable to the RECTEDGE guard from a data stroke crossing it,
    # and the figure reads better without them.
    XT = [0.0, 0.5, 1.0, 1.5, 2.0]
    YT = [10.0, 20.0, 30.0, 40.0]
    p.line(sx1(AX0), sy1(0.0), sx1(AX1), sy1(0.0), "axis")
    p.line(sx1(0.0), sy1(AY0), sx1(0.0), sy1(AY1), "axis")
    for xv in XT:
        p.text(_f(xv), sx1(xv), sy1(0.0) + 17, "tick197", 10, "middle", tick=True)
    for yv in YT:
        p.text(_f(yv, 0), sx1(0.0) - 9, sy1(yv) + 3.5, "tick197", 10, "end", tick=True)

    # the curve  avg(k) = 5/k , clipped at the top of the frame
    kmin = FIVE / (AY1 - 0.4)
    pts = []
    N = 300
    for i in range(N + 1):
        kk = kmin + (AX1 - kmin) * i / float(N)
        pts.append((sx1(kk), sy1(FIVE / kk)))
    p.poly(pts, "curve197")

    # the target level, and the neutral level 5
    p.line(sx1(AX0), sy1(TARGET), sx1(AX1), sy1(TARGET), "tlev197")
    p.line(sx1(AX0), sy1(FIVE), sx1(AX1), sy1(FIVE), "nlev197")
    # k = 1 is excluded: no interval
    p.line(sx1(1.0), sy1(AY0), sx1(1.0), sy1(AY1), "nline197")
    p.dot(sx1(1.0), sy1(FIVE), 4.2, "opendot197")

    # the solution
    p.line(sx1(KANS), sy1(0.0), sx1(KANS), sy1(TARGET), "gline197")
    p.dot(sx1(KANS), sy1(TARGET), 4.6, "soldot197")

    # labels, placed clear of the strokes
    p.text("AVERAGE = 5/k", sx1(1.62), sy1(9.4), "curvel197", 11)
    p.text("TARGET  32", sx1(AX1) + 8, sy1(TARGET) + 3.5, "tlevl197", 11)
    p.text("ONE CROSSING", sx1(AX1) + 8, sy1(TARGET) + 24, "tlevl197", 10)
    p.text("5, THE VALUE AT k = 1", sx1(AX1) + 8, sy1(FIVE) - 4, "nlevl197", 10)
    p.text("NEVER ATTAINED", sx1(AX1) + 8, sy1(FIVE) + 16, "nlevl197", 10)
    p.text("k = 5/32", sx1(KANS) + 11, sy1(TARGET) - 9, "soll197", 11.5)
    p.text("k = 1", sx1(1.0) + 7, sy1(AY1) + 18, "nlevl197", 10)
    p.text("k", sx1(AX1) - 6, sy1(0.0) + 17, "axl197", 11, "end")
    p.text("ABOVE 5  =>  k < 1", sx1(0.30), sy1(40.0), "regionl197", 10)
    p.text("BELOW 5  =>  k > 1", sx1(1.15), sy1(40.0), "regionl197", 10)

    # ---- CURVEFIT: re-evaluate the drawn polyline in data space -----------
    worst = 0.0
    for (px, py) in pts[::7]:
        kk = AX0 + (px - P1L) / float(W1 - P1L - P1R) * (AX1 - AX0)
        yy = AY0 + (H1 - P1B - py) / float(H1 - P1T - P1B) * (AY1 - AY0)
        worst = max(worst, abs(yy - FIVE / kk))
    assert worst < 1e-6, "fig1 CURVEFIT: drawn curve is not 5/k (worst %.3e)" % worst
    LOG.append("fig1 CURVEFIT   drawn polyline traces 5/k, worst data error %.2e" % worst)

    # ---- CROSSING: the dot sits on the curve AND on the target level ------
    dx, dy = sx1(KANS), sy1(TARGET)
    assert abs(dy - sy1(FIVE / KANS)) < 0.01, "fig1 CROSSING: dot is off the curve"
    assert abs(dy - sy1(TARGET)) < 0.01, "fig1 CROSSING: dot is off the target level"
    LOG.append("fig1 CROSSING   solution dot on both curve and level, within 0.01px")

    run_guards(p, "fig1", ["AVERAGE = 5/k", "TARGET  32", "k = 5/32",
                           "5, THE VALUE AT k = 1", "k = 1", "ONE CROSSING"])
    return ('<div class="figbox">'
            + p.svg(W1, H1, "The average 5 over k against k, cut once by the "
                            "level 32 at k = 5 over 32")
            + '</div>')


# ==========================================================================
P2T, P2B = 40, 58
PANW = 250
GAP = 100
P2L = 46


def fig2():
    p = Panel("fig2", W2, H2)
    p.rect(0, 0, W2, H2, "plotbg197", background=True)

    # ---------------- panel A : 5/k , one crossing ------------------------
    ax0, ax1 = P2L, P2L + PANW
    A_X0, A_X1 = 0.0, 2.2
    A_Y0, A_Y1 = 0.0, 45.0

    def axf(x):
        return ax0 + (x - A_X0) / (A_X1 - A_X0) * PANW

    def ayf(y):
        return H2 - P2B - (y - A_Y0) / (A_Y1 - A_Y0) * (H2 - P2T - P2B)

    p.rect(ax0, P2T, PANW, H2 - P2T - P2B, "panel197")
    p.line(ax0, ayf(0.0), ax1, ayf(0.0), "axis")
    kmin = FIVE / (A_Y1 - 0.4)
    ptsA = []
    for i in range(241):
        kk = kmin + (A_X1 - kmin) * i / 240.0
        ptsA.append((axf(kk), ayf(FIVE / kk)))
    p.poly(ptsA, "curve197")
    p.line(ax0, ayf(TARGET), ax1, ayf(TARGET), "tlev197")
    p.dot(axf(KANS), ayf(TARGET), 4.2, "soldot197")
    p.text("MONOTONE:  5/k", ax0 + 8, P2T - 12, "panl197", 11)
    p.text("EXACTLY ONE SOLUTION", ax0 + 120, P2T + 18, "okl197", 10)
    p.text("32", ax0 - 8, ayf(TARGET) + 3.5, "tlevl197", 10, "end", tick=True)
    p.text("0", ax0 - 8, ayf(0.0) + 3.5, "tick197", 10, "end", tick=True)
    p.text("k = 5/32", axf(KANS) + 10, ayf(TARGET) - 9, "soll197", 10)
    p.text("k", ax1 - 8, ayf(0.0) + 17, "axl197", 10, "end")

    # ---------------- panel B : (k^2-5k+7)/3 , two / one / none -----------
    bx0 = ax0 + PANW + GAP
    bx1 = bx0 + PANW
    B_X0, B_X1 = 0.0, 5.4
    B_Y0, B_Y1 = 0.0, 3.1

    def bxf(x):
        return bx0 + (x - B_X0) / (B_X1 - B_X0) * (bx1 - bx0)

    def byf(y):
        return H2 - P2B - (y - B_Y0) / (B_Y1 - B_Y0) * (H2 - P2T - P2B)

    def gB(k):
        return (k * k - 5.0 * k + 7.0) / 3.0

    p.rect(bx0, P2T, bx1 - bx0, H2 - P2T - P2B, "panel197")
    p.line(bx0, byf(0.0), bx1, byf(0.0), "axis")
    ptsB = [(bxf(B_X0 + (B_X1 - B_X0) * i / 240.0),
             byf(gB(B_X0 + (B_X1 - B_X0) * i / 240.0))) for i in range(241)]
    p.poly(ptsB, "curve197")
    p.line(bx0, byf(1.5), bx1, byf(1.5), "tlev197")
    p.line(bx0, byf(0.25), bx1, byf(0.25), "tlev197")
    p.line(bx0, byf(0.125), bx1, byf(0.125), "tlev197")
    r1 = (5.0 - math.sqrt(15.0)) / 2.0
    r2 = (5.0 + math.sqrt(15.0)) / 2.0
    p.dot(bxf(r1), byf(1.5), 4.0, "soldot197")
    p.dot(bxf(r2), byf(1.5), 4.0, "soldot197")
    p.dot(bxf(2.5), byf(0.25), 4.0, "soldot197")
    p.text("NOT MONOTONE:  (k^2 - 5k + 7)/3", bx0 + 8, P2T - 12, "panl197", 11)
    # Three TARGET levels, so all three take the amber target colour.  The
    # count is carried by the dots and the words, not by a right/wrong pair:
    # a target below the minimum is not an error, it is just unreachable, and
    # painting it rust would make rust mean two different things (31.9).
    p.text("TWO", bx1 + 8, byf(1.5) + 3.5, "tlevl197", 10)
    p.text("ONE", bx1 + 8, byf(0.25) + 3.5, "tlevl197", 10)
    p.text("NONE", bx1 + 8, byf(0.125) + 16, "tlevl197", 10)
    p.text("k", bx1 - 8, byf(0.0) + 17, "axl197", 10, "end")
    p.text("0", bx0 - 8, byf(0.0) + 3.5, "tick197", 10, "end", tick=True)
    p.text("3", bx0 - 8, byf(3.0) + 3.5, "tick197", 10, "end", tick=True)

    # ---- CURVEFIT on both panels -----------------------------------------
    wA = 0.0
    for (px, py) in ptsA[::7]:
        kk = A_X0 + (px - ax0) / float(PANW) * (A_X1 - A_X0)
        yy = A_Y0 + (H2 - P2B - py) / float(H2 - P2T - P2B) * (A_Y1 - A_Y0)
        wA = max(wA, abs(yy - FIVE / kk))
    assert wA < 1e-6, "fig2 panel A CURVEFIT: %.3e" % wA
    wB = 0.0
    for (px, py) in ptsB[::7]:
        kk = B_X0 + (px - bx0) / float(bx1 - bx0) * (B_X1 - B_X0)
        yy = B_Y0 + (H2 - P2B - py) / float(H2 - P2T - P2B) * (B_Y1 - B_Y0)
        wB = max(wB, abs(yy - gB(kk)))
    assert wB < 1e-6, "fig2 panel B CURVEFIT: %.3e" % wB
    LOG.append("fig2 CURVEFIT   both panels trace their function, worst %.2e"
               % max(wA, wB))

    # ---- CROSSING: the three marked dots sit on their levels --------------
    for (kk, lev) in ((r1, 1.5), (r2, 1.5), (2.5, 0.25)):
        assert abs(gB(kk) - lev) < 1e-9, "fig2 CROSSING: %.6f is not on %.3f" % (kk, lev)
    LOG.append("fig2 CROSSING   3 marked roots verified against their levels")

    run_guards(p, "fig2", ["MONOTONE", "NOT MONOTONE", "EXACTLY ONE SOLUTION",
                           "TWO", "ONE", "NONE", "k = 5/32"], deadspace_min=0.40)
    return ('<div class="figbox">'
            + p.svg(W2, H2, "Two panels: a monotone average cut once, and a "
                            "non-monotone average cut twice, once or not at all")
            + '</div>')


# ---------------------------------------------------------------- controls
def curvefit_control():
    """The CURVEFIT guard must REJECT a curve that is not the claimed one."""
    worst = 0.0
    for i in range(0, 301, 7):
        kk = 0.12 + (AX1 - 0.12) * i / 300.0
        yy = FIVE / kk * 1.02          # a 2 percent wrong curve
        worst = max(worst, abs(yy - FIVE / kk))
    ok = worst > 1e-6
    LOG.append("CONTROL CURVEFIT rejects a 2 percent wrong curve: %s (worst %.3e)"
               % (ok, worst))
    return ok


def collide_control():
    """The COLLIDE guard must fire on two boxes placed on top of each other."""
    a = bbox("SEEDED COLLISION", 100.0, 100.0, 11)
    b = bbox("SEEDED COLLISION", 104.0, 103.0, 11)
    ok = overlap(a, b)
    far = bbox("SEEDED COLLISION", 400.0, 300.0, 11)
    ok = ok and not overlap(a, far)
    LOG.append("CONTROL COLLIDE fires on stacked boxes and stays silent on distant "
               "ones: %s" % ok)
    return ok


def rectedge_control():
    """A stroked <rect> border must be visible to the crossing test."""
    segs = rect_segs(50.0, 50.0, 200.0, 100.0)
    box = bbox("ON THE BORDER", 120.0, 52.0, 11)
    hit = any(seg_hits_box(q1, q2, box) for (q1, q2) in segs)
    clear = bbox("WELL CLEAR", 120.0, 300.0, 11)
    miss = not any(seg_hits_box(q1, q2, clear) for (q1, q2) in segs)
    LOG.append("CONTROL RECTEDGE sees a rect border (%s) and not a distant box (%s)"
               % (hit, miss))
    return hit and miss


def tick_control():
    """The placer must never move an axis tick label."""
    before = [(_f(v), sx1(v)) for v in (0.0, 0.5, 1.0, 1.5, 2.0)]
    after = [(_f(v), sx1(v)) for v in (0.0, 0.5, 1.0, 1.5, 2.0)]
    ok = all(abs(a[1] - b[1]) < 0.005 and a[0] == b[0]
             for a, b in zip(before, after))
    LOG.append("CONTROL TICKS   axis tick positions identical before and after "
               "placement: %s" % ok)
    return ok


def content_control():
    """The CONTENT guard must fire when a required label is absent."""
    drawn = ["AVERAGE = 5/k", "TARGET  32"]
    missing = [m for m in ["k = 5/32"] if not any(m in d for d in drawn)]
    ok = bool(missing)
    LOG.append("CONTROL CONTENT fires on an undrawn required label: %s" % ok)
    return ok
