"""Q13.1 figures. Both are built from RECTS and horizontal gridlines only.

svg-labels.mjs measures a <line> by its BOUNDING BOX, so a diagonal's box is the
whole rectangle it spans and every label inside a panel reads as crossed. Rects
avoid that class of finding entirely (settled on Q12.3, zero lineHits first try).

Figure A  the digit ladder: correct decimal digits per Newton step, for three
          starting points, against the TWO thresholds this question has - the
          4.30 that a 0.5e-4 error tolerance buys, and the 4.90 that the root's
          own distance from its rounding tie point actually demands.
Figure B  two number lines: the basin split at f's critical point, and a zoom on
          the rounding boundary that makes x3-from-1 round the wrong way.
"""
import math

# ---- measured inputs, printed by the harness, never typed ------------------
DIGITS = {
    "x0 = 1":   [0.5918659948244492, 1.1112826895657635, 2.2714210591337616,
                 4.565422430923621, 9.15146996418566, 18.323555041189973],
    "x0 = 1.5": [0.6124990301545253, 1.332716999982951, 2.7030598374842816,
                 5.427462339595866, 10.875541164264728, 21.771697441093875],
    "x0 = 2":   [0.12839061102968584, 0.5187208270611198, 1.1651155311609708,
                 2.375817122000451, 4.77379476622446, 9.56821082778892],
}
# the root's distance to its own four-decimal tie point, measured by the
# harness. NEED is DERIVED from it - a first draft typed 4.904816465003707 from
# head arithmetic and was wrong in the fifth figure.
GAP = 1.2451832076631532e-05
NEED = -math.log10(GAP)
SUGGEST = -math.log10(0.5e-4)
ROOT = 1.2559375481679234
ROOTN = -1.7027063709099214
XC = -0.7937005259840998
X3FROM1 = 1.2559647487106231
BOUND = 1.25595


def _esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def _t(x, y, s, cls="lab"):
    return ('<text class="%s" x="%.1f" y="%.1f">%s</text>'
            % (cls, x, y, _esc(s)))


def _r(x, y, w, h, cls):
    if w < 0:
        x, w = x + w, -w
    return ('<rect class="%s" x="%.1f" y="%.1f" width="%.1f" height="%.1f"/>'
            % (cls, x, y, max(w, 0.0), max(h, 0.0)))


def _hl(x1, x2, y):
    return ('<line class="gridl" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>'
            % (x1, y, x2, y))


# ===========================================================================
# FIGURE A - the digit ladder
#
# Annotation policy, settled across Q11.2 / Q12.1 / Q12.2 / Q12.3: every label
# that is not an axis tick lives in a LEGEND STRIP below all drawn mass, at 22px
# row spacing.  Callouts placed beside the thing they describe collide with the
# panel subtitle and with each other, and three repositioning attempts never
# converge.  The axis title "DIGITS" was DELETED rather than moved: the panel
# header already says what the bars are, and svg-labels reported it overlapping
# the "10" tick.
# ===========================================================================
def build_ladder():
    W, H = 880, 496
    L, Rt = 74, W - 24
    TOP, BOT = 82, 322
    ymax = 22.5

    def ypx(v):
        return BOT - (v / ymax) * (BOT - TOP)

    o = ['<svg viewBox="0 0 %d %d" width="%d" height="%d" '
         'xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="Correct decimal digits per Newton step for three starting '
         'points, against the two four-decimal thresholds">' % (W, H, W, H)]

    o.append(_t(L, 30, "CORRECT DECIMAL DIGITS AFTER n NEWTON STEPS", "lab hd"))
    o.append(_t(L, 52, "three legal starting points, same equation, same root",
                "lab sm"))

    for v in (0, 5, 10, 15, 20):
        y = ypx(v)
        o.append(_hl(L, Rt, y))
        o.append(_t(L - 14, y + 4, "%d" % v, "lab tk"))

    yb1, yb2 = ypx(NEED), ypx(SUGGEST)
    o.append(_r(L, yb1, Rt - L, yb2 - yb1, "band131"))

    keys = list(DIGITS.keys())
    nsteps = 6
    gw = (Rt - L) / nsteps
    bw = gw / (len(keys) + 1.35)
    cls = ["s1_131", "s2_131", "s3_131"]
    for n in range(nsteps):
        gx = L + n * gw
        for k, key in enumerate(keys):
            v = min(DIGITS[key][n], ymax)
            x = gx + gw * 0.10 + k * bw
            y = ypx(v)
            o.append(_r(x, y, bw * 0.86, BOT - y, cls[k]))
        o.append(_t(gx + gw / 2 - 14, BOT + 20, "n = %d" % n, "lab tk"))

    o.append(_hl(L, Rt, BOT))
    o.append(_r(L, ypx(SUGGEST) - 1, Rt - L, 2, "sug131"))
    o.append(_r(L, ypx(NEED) - 1, Rt - L, 2, "need131"))

    # ---- legend strip, below every drawn mass -----------------------------
    ly = BOT + 62
    o.append(_hl(L, Rt, ly - 24))
    for k, key in enumerate(keys):
        x = L + k * 190
        o.append(_r(x, ly - 10, 13, 13, cls[k]))
        o.append(_t(x + 21, ly + 1, key, "lab sm"))

    ly2 = ly + 30
    o.append(_r(L, ly2 - 8, 13, 3, "sug131"))
    o.append(_t(L + 21, ly2 + 1,
                "%.2f  the digits an error below 0.5e-4 buys" % SUGGEST, "lab sm"))
    o.append(_r(L, ly2 + 22 - 8, 13, 3, "need131"))
    o.append(_t(L + 21, ly2 + 23,
                "%.2f  the digits THIS root actually needs, because it sits "
                "1.2e-5 from its tie point" % NEED, "lab am"))
    o.append(_r(L, ly2 + 44 - 9, 13, 13, "band131"))
    o.append(_t(L + 21, ly2 + 45,
                "the trap band: more than four correct digits, and still the "
                "wrong fourth decimal", "lab los131"))
    o.append("</svg>")
    return "".join(o)


# ===========================================================================
# FIGURE B - two number lines, same annotation policy
# ===========================================================================
def build_lines():
    W, H = 880, 560
    L, Rt = 74, W - 24
    bh = 34
    o = ['<svg viewBox="0 0 %d %d" width="%d" height="%d" '
         'xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="Two number lines: the basin split at the critical point, '
         'and a zoom on the four-decimal rounding boundary">' % (W, H, W, H)]

    # ---------------- panel 1: the basins --------------------------------
    o.append(_t(L, 30, "PANEL 1   WHICH ROOT DOES x0 REACH", "lab hd"))
    o.append(_t(L, 52, "the whole real line splits in two, at f's own critical "
                       "point", "lab sm"))
    lo1, hi1 = -3.0, 3.0
    y1 = 78

    def px1(v):
        return L + (v - lo1) / (hi1 - lo1) * (Rt - L)

    xcp = px1(XC)
    o.append(_r(L, y1, xcp - L, bh, "neg131"))
    o.append(_r(xcp, y1, Rt - xcp, bh, "pos131"))
    o.append(_r(px1(1.0), y1, px1(2.0) - px1(1.0), bh, "stem131"))
    # full-strength rails along the top edge. The -soft tints alone are too
    # close in value to separate at reading size, and no gate compares two
    # fills - the same defect species as Q12.3's invisible gauge fill.
    o.append(_r(L, y1, xcp - L, 5, "negr131"))
    o.append(_r(xcp, y1, Rt - xcp, 5, "posr131"))
    o.append(_r(px1(1.0), y1, px1(2.0) - px1(1.0), 5, "stemr131"))
    o.append(_hl(L, Rt, y1 + bh))

    for v in (-3, -2, -1, 0, 1, 2, 3):
        o.append(_r(px1(v) - 0.5, y1 + bh, 1, 6, "tick131"))
        o.append(_t(px1(v) - 4, y1 + bh + 20, "%d" % v, "lab tk"))

    o.append(_r(px1(ROOTN) - 2.5, y1 - 7, 5, bh + 7, "mark131"))
    o.append(_r(px1(ROOT) - 2.5, y1 - 7, 5, bh + 7, "mark131"))
    o.append(_r(xcp - 2.5, y1 - 7, 5, bh + 7, "crit131"))

    ly = y1 + bh + 52
    o.append(_r(L, ly - 9, 13, 13, "neg131"))
    o.append(_r(L, ly - 9, 13, 4, "negr131"))
    o.append(_t(L + 21, ly + 1,
                "every x0 LEFT of x_c reaches the other root, -1.7027",
                "lab sm"))
    o.append(_r(L, ly + 22 - 9, 13, 13, "pos131"))
    o.append(_r(L, ly + 22 - 9, 13, 4, "posr131"))
    o.append(_t(L + 21, ly + 23,
                "every x0 RIGHT of x_c reaches the root asked for, 1.2559",
                "lab sm"))
    o.append(_r(L, ly + 44 - 9, 13, 13, "stem131"))
    o.append(_r(L, ly + 44 - 9, 13, 4, "stemr131"))
    o.append(_t(L + 21, ly + 45,
                "the stem's own interval [1, 2], safely inside the right basin",
                "lab am"))
    o.append(_r(L, ly + 66 - 9, 5, 13, "crit131"))
    o.append(_t(L + 21, ly + 67,
                "x_c = -0.7937, where f' vanishes: the ONLY basin boundary over "
                "[-20, 20]", "lab los131"))

    # ---------------- panel 2: the rounding boundary ---------------------
    o.append(_hl(L, Rt, 300))
    o.append(_t(L, 330, "PANEL 2   THE FOUR-DECIMAL ROUNDING BOUNDARY", "lab hd"))
    o.append(_t(L, 352, "a 1.0e-4 wide window on the root", "lab sm"))
    lo2, hi2 = 1.25590, 1.25600
    y2 = 378

    def px2(v):
        return L + (v - lo2) / (hi2 - lo2) * (Rt - L)

    bx = px2(BOUND)
    o.append(_r(L, y2, bx - L, bh, "keep131"))
    o.append(_r(bx, y2, Rt - bx, bh, "miss131"))
    o.append(_r(L, y2, bx - L, 5, "posr131"))
    o.append(_r(bx, y2, Rt - bx, 5, "negr131"))
    o.append(_hl(L, Rt, y2 + bh))
    # the region labels sit at the OUTER edges. Placed just inside the tie
    # point they run into the marker rects, and svg-labels cannot see that -
    # it tests labels against `line` elements, and every mark here is a rect.
    o.append(_t(L + 14, y2 + 22, "rounds to 1.2559", "lab sm"))
    o.append(_t(Rt - 130, y2 + 22, "rounds to 1.2560", "lab los131"))

    o.append(_r(bx - 1, y2 - 7, 2, bh + 7, "crit131"))
    o.append(_r(px2(ROOT) - 2.5, y2 - 7, 5, bh + 7, "mark131"))
    o.append(_r(px2(X3FROM1) - 2.5, y2 - 7, 5, bh + 7, "vsn131"))

    for v in (1.25590, 1.25592, 1.25594, 1.25596, 1.25598, 1.25600):
        o.append(_r(px2(v) - 0.5, y2 + bh, 1, 6, "tick131"))

    ly2 = y2 + bh + 40
    o.append(_r(L, ly2 - 9, 5, 13, "mark131"))
    o.append(_t(L + 21, ly2 + 1,
                "the true root, 1.25593755  -  rounds to 1.2559", "lab am"))
    o.append(_r(L, ly2 + 22 - 9, 5, 13, "vsn131"))
    o.append(_t(L + 21, ly2 + 23,
                "x3 from x0 = 1, 1.25596475  -  error 2.7e-5, inside the 5e-5 "
                "tolerance", "lab los131"))
    o.append(_r(L, ly2 + 44 - 9, 2, 13, "crit131"))
    o.append(_t(L + 21, ly2 + 45,
                "the tie point 1.25595, only 1.2e-5 above the root: x3 is on "
                "the wrong side of it", "lab sm"))
    o.append("</svg>")
    return "".join(o)


if __name__ == "__main__":
    a, b = build_ladder(), build_lines()
    print("ladder", len(a), "bytes;  lines", len(b), "bytes")
    print("non-ascii:", sorted({c for c in a + b if ord(c) > 127}))
    print("NEED %.4f  SUGGEST %.4f" % (NEED, SUGGEST))
