"""Two figures for the Q12.3 page.

Both are built from RECTS and horizontal rules only.  `svg-labels.mjs` samples
`line` and `polyline` elements by BOUNDING BOX, and a diagonal's bbox is the
whole rectangle it spans, which is what forced three failed reposition rounds
on Q12.1 and Q12.2.  Using rects for every drawn mass removes that class of
finding entirely; the only `line` elements here are horizontal rules carrying
`class="gridl"`, which the gate exempts.

Every number is COMPUTED here, never typed.
"""
import math as _m
from decimal import Decimal as D, getcontext, ROUND_HALF_UP

getcontext().prec = 60

_BS = chr(92)


def _arct(n):
    getcontext().prec = 100
    x = D(1) / D(n)
    tot = x
    term = x
    k = 1
    xx = x * x
    while True:
        term = -term * xx
        t = term / (2 * k + 1)
        if abs(t) < D(10) ** -95:
            break
        tot += t
        k += 1
    getcontext().prec = 60
    return +tot


PI = +(4 * (4 * _arct(5) - _arct(239)))


def _ds(x):
    getcontext().prec = 100
    x = +D(x)
    tot = x
    term = x
    k = 1
    xx = x * x
    while True:
        term = -term * xx / ((2 * k) * (2 * k + 1))
        if abs(term) < D(10) ** -95:
            break
        tot += term
        k += 1
    getcontext().prec = 60
    return +tot


def _dc(x):
    getcontext().prec = 100
    x = +D(x)
    tot = D(1)
    term = D(1)
    k = 1
    xx = x * x
    while True:
        term = -term * xx / ((2 * k - 1) * (2 * k))
        if abs(term) < D(10) ** -95:
            break
        tot += term
        k += 1
    getcontext().prec = 60
    return +tot


def _rd(d):
    return D(d) * PI / 180


def _qz(d, k):
    return D(d).quantize(D(1).scaleb(-k), rounding=ROUND_HALF_UP)


EST_A = D("0.5") - _ds(PI / 3) * _rd(2)
TRUE_A = _dc(_rd(62))
EST_B = D("4.05")
TRUE_B = D("16.4").sqrt()


def _esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def _txt(x, y, s, cls="lab", anchor="start"):
    return ('<text class="%s" x="%.1f" y="%.1f" text-anchor="%s">%s</text>'
            % (cls, x, y, anchor, _esc(s)))


def _rect(x, y, w, h, cls, rx=2):
    return ('<rect class="%s" x="%.1f" y="%.1f" width="%.1f" height="%.1f" '
            'rx="%.1f"/>' % (cls, x, y, max(w, 0.6), max(h, 0.6), rx))


def _rule(x1, x2, y):
    return ('<line class="gridl" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>'
            % (x1, y, x2, y))


# ======================================================================
# FIGURE 1 - THE PLACE LADDER.
# Round the estimate and the truth to k = 0 .. 4 places and mark whether
# the two strings agree.  Part (b)'s column is the point of the figure:
# its agreement is NOT nested, so a reader who checks only three places
# concludes the answer is good.
# ======================================================================
def build_ladder():
    W, H = 800, 396
    L = 74           # left gutter for the k label
    CW = 168         # column width for a value pair
    GAP = 26
    C1 = L + 34      # part (a) estimate column
    C2 = C1 + CW     # part (a) true column
    C3 = C2 + CW + GAP   # part (b) estimate column
    C4 = C3 + CW     # part (b) true column
    TOP = 96
    RH = 52

    o = ['<svg viewBox="0 0 %d %d" width="%d" height="%d" '
         'xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="Rounding both estimates to zero through four decimal '
         'places and marking where each agrees with the true value.">'
         % (W, H, W, H)]

    o.append(_txt(L - 44, 30, "ROUNDING", "lab hd"))
    o.append(_txt(C1, 30, "(a)  COS 62 DEGREES", "lab hd"))
    o.append(_txt(C3, 30, "(b)  SQUARE ROOT OF 16.4", "lab hd"))
    o.append(_rule(L - 44, W - 18, 44))

    o.append(_txt(L - 44, 74, "K", "lab tk"))
    o.append(_txt(C1, 74, "ESTIMATE", "lab tk"))
    o.append(_txt(C2, 74, "TRUE", "lab tk"))
    o.append(_txt(C3, 74, "ESTIMATE", "lab tk"))
    o.append(_txt(C4, 74, "TRUE", "lab tk"))
    o.append(_rule(L - 44, W - 18, 84))

    rows = []
    for k in range(5):
        ea, ta = str(_qz(EST_A, k)), str(_qz(TRUE_A, k))
        eb, tb = str(_qz(EST_B, k)), str(_qz(TRUE_B, k))
        rows.append((k, ea, ta, ea == ta, eb, tb, eb == tb))

    for i, (k, ea, ta, oka, eb, tb, okb) in enumerate(rows):
        y = TOP + i * RH
        base = y + 22
        if i:
            o.append(_rule(L - 44, W - 18, y - 8))
        o.append(_txt(L - 44, base, str(k), "lab am"))
        # part (a)
        o.append(_rect(C1 - 10, y, CW - 12, RH - 16,
                       "cell123 " + ("hit123" if oka else "miss123")))
        o.append(_txt(C1, base, ea, "lab" + ("" if oka else " vsn123")))
        o.append(_txt(C2, base, ta, "lab sm"))
        o.append(_txt(C2 + 108, base, "AGREE" if oka else "DIFFER",
                      "lab tk" + ("" if oka else " los123"), "end"))
        # part (b)
        o.append(_rect(C3 - 10, y, CW - 12, RH - 16,
                       "cell123 " + ("hit123" if okb else "miss123")))
        o.append(_txt(C3, base, eb, "lab" + ("" if okb else " vsn123")))
        o.append(_txt(C4, base, tb, "lab sm"))
        o.append(_txt(C4 + 108, base, "AGREE" if okb else "DIFFER",
                      "lab tk" + ("" if okb else " los123"), "end"))

    o.append(_rule(L - 44, W - 18, TOP + 5 * RH - 8))
    o.append(_txt(L - 44, TOP + 5 * RH + 16,
                  "PART (a) FAILS AT THREE AND STAYS FAILED.  PART (b) FAILS "
                  "AT ONE, RECOVERS AT TWO AND THREE, FAILS AGAIN AT FOUR.",
                  "lab tk"))
    o.append("</svg>")
    return "".join(o)


# ======================================================================
# FIGURE 2 - THE BRACKET.
# For each of category 12's five instances, draw the interval between the
# two ENDPOINT values of |f''|/2 dx^2 and mark where the actual error
# falls.  It falls inside every time, which is the whole settlement:
# neither endpoint is "the bound", the larger is an upper bound and the
# smaller is a lower one.
# ======================================================================
def _bracket_rows():
    f2s = lambda x: 1.0 / (4 * x ** 1.5)
    f2c = lambda x: abs(_m.cos(x))
    f2n = lambda x: abs(_m.sin(x))
    h = _m.radians(62) - _m.pi / 3
    out = []

    def row(tag, f2, a, b, est, true):
        dx = b - a
        bA = f2(a) * dx * dx / 2
        bT = f2(b) * dx * dx / 2
        out.append((tag, bA, bT, abs(est - true), bA > bT))

    row("Q12.1  sqrt(9.2) from 9", f2s, 9.0, 9.2,
        3 + 0.2 / 6, float(D("9.2").sqrt()))
    row("Q12.1  sqrt(48.6) from 49", f2s, 49.0, 48.6,
        7 - 0.4 / 14, float(D("48.6").sqrt()))
    row("Q12.2  sin 62 from 60", f2n, _m.pi / 3, _m.radians(62),
        _m.sin(_m.pi / 3) + _m.cos(_m.pi / 3) * h, float(_ds(_rd(62))))
    row("Q12.3a cos 62 from 60", f2c, _m.pi / 3, _m.radians(62),
        float(EST_A), float(TRUE_A))
    row("Q12.3b sqrt(16.4) from 16", f2s, 16.0, 16.4,
        4.05, float(TRUE_B))
    return out


def build_bracket():
    rows = _bracket_rows()
    W, H = 800, 424
    L = 232
    R = W - 128
    SPAN = R - L
    TOP = 104
    RH = 56

    o = ['<svg viewBox="0 0 %d %d" width="%d" height="%d" '
         'xmlns="http://www.w3.org/2000/svg" role="img" '
         'aria-label="For each of the five linear-approximation instances, '
         'the actual error falls strictly between the two endpoint values of '
         'the second-derivative bound.">' % (W, H, W, H)]

    o.append(_txt(18, 30, "THE ERROR IS BRACKETED BY THE TWO ENDPOINTS",
                  "lab hd"))
    o.append(_txt(18, 52,
                  "EACH TRACK IS RESCALED TO ITS OWN INTERVAL, SO ONLY THE "
                  "POSITION INSIDE IT IS COMPARABLE", "lab tk"))
    o.append(_rule(18, W - 18, 66))
    o.append(_txt(L, 86, "SMALLER ENDPOINT", "lab tk"))
    o.append(_txt(R, 86, "LARGER ENDPOINT", "lab tk", "end"))

    for i, (tag, bA, bT, err, anchor_is_max) in enumerate(rows):
        y = TOP + i * RH
        lo, hi = min(bA, bT), max(bA, bT)
        frac = (err - lo) / (hi - lo)
        x = L + SPAN * frac
        o.append(_txt(18, y + 15, tag, "lab sm"))
        # the interval, drawn as a rect so no line bbox can be reported
        o.append(_rect(L, y + 6, SPAN, 12, "track123", 6))
        o.append(_rect(L, y + 6, x - L, 12, "fill123", 6))
        # the actual error
        o.append(_rect(x - 2.2, y - 2, 4.4, 24, "mark123", 1))
        o.append(_txt(L, y + 40, "%.4e" % lo, "lab tk"))
        o.append(_txt(R, y + 40, "%.4e" % hi, "lab tk", "end"))
        lab = "ERROR %.4e" % err
        # keep the moving label clear of both fixed end labels
        if frac < 0.42:
            o.append(_txt(R - 2, y + 15, lab, "lab am", "end"))
        else:
            o.append(_txt(L + 2, y + 15, lab, "lab am"))
        o.append(_txt(W - 18, y + 15,
                      "MAX AT ANCHOR" if anchor_is_max else "MAX AT TARGET",
                      "lab tk" + ("" if anchor_is_max else " los123"), "end"))
        if i < len(rows) - 1:
            o.append(_rule(18, W - 18, y + 50))

    o.append(_rule(18, W - 18, TOP + len(rows) * RH - 6))
    o.append(_txt(18, TOP + len(rows) * RH + 14,
                  "FIVE FOR FIVE.  NOTHING WAS EVER VIOLATED - A LOWER BOUND "
                  "WAS READ AS AN UPPER ONE.", "lab tk"))
    o.append("</svg>")
    return "".join(o)


if __name__ == "__main__":
    a, b = build_ladder(), build_bracket()
    print("ladder", len(a), "bytes;  bracket", len(b), "bytes")
    bad = sorted({c for c in a + b if ord(c) > 127})
    print("non-ascii:", bad if bad else "none")
    nin = 0
    for t, bA, bT, e, am in _bracket_rows():
        lo, hi = min(bA, bT), max(bA, bT)
        inside = lo < e < hi
        nin += 1 if inside else 0
        print("  %-28s lo=%.5e  err=%.5e  hi=%.5e  inside=%s  anchor_max=%s"
              % (t, lo, e, hi, inside, am))
    assert nin == 5, "the bracket must hold on all five, got %d" % nin
    print("bracket holds on all five")
