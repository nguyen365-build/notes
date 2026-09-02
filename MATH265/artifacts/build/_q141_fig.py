"""Figures for the Q14.1 artifact.

Every coordinate comes from evaluating f. Nothing is hand-placed.

TWO CONTRACTS, and the first draft broke both of them silently.

 1. `var()` DOES NOT WORK IN AN SVG PRESENTATION ATTRIBUTE. `fill="var(--x)"`
    and `font-family="var(--mono)"` are parsed as the property's grammar, not as
    a declaration, so the substitution never happens. The series therefore paints
    SVG through CSS (`.figbox text.lab { ... }`) and this file emits CLASSES ONLY,
    with no font or paint attributes at all.

 2. A CSS rule BEATS a presentation attribute, so upstream's
    `.figbox text.lab { font-size:12px }` overrode every `font-size="10.5"`
    attribute the first draft wrote, and `.figbox .gridl { stroke:var(--line);
    stroke-width:1 }` repainted every asymptote and the centre line as a plain
    1px gridline. `.gridl` is not merely the svg-labels exemption hook - it
    carries upstream PAINT, welded to the exemption. So the reference lines here
    use `gridref`, which still matches the gate's /grid|axis/ exemption but
    inherits nothing.

Other carryover rules honoured:
  - EVERY non-tick label lives in a LEGEND STRIP below all drawn mass, because
    svg-labels.mjs measures a polyline by its BOUNDING BOX
  - legend rows 22px apart, a row of margin below the last drawn element, and a
    left and top margin so no label falls outside the viewBox
  - no non-ASCII in labels; HTML entities only
  - near-asymptote branches sampled densely and the polyline BROKEN at every
    pole, so no segment steps across one
"""
import sys
sys.dont_write_bytecode = True   # housekeeping: no __pycache__ in a content dir

import math

PI = math.pi

ML = 40      # left margin, so the leftmost tick label stays inside the viewBox
MR = 40      # right margin, so the RIGHTMOST tick label does too - svg-labels
             # reported `3pi` outside the viewBox when this was 0
MT = 40      # top margin, for the panel headers
MB = 14      # bottom margin below the last drawn element


def fa(x):
    return x * x / (x * x - 1)


def fb(x):
    return x + math.sin(x)


def thin(pts, min_px=0.42):
    """Drop a point within min_px of the last KEPT one, always keeping the first
    and last. Sampling is uniform in x, so the density that survives is highest
    exactly where the curve is steepest - which is where a polyline would
    otherwise cut a corner or step across a pole. Sub-pixel, so purely a size
    optimisation."""
    if len(pts) < 3:
        return pts
    out = [pts[0]]
    lx, ly = pts[0]
    for (x, y) in pts[1:-1]:
        if abs(x - lx) + abs(y - ly) >= min_px:
            out.append((x, y))
            lx, ly = x, y
    out.append(pts[-1])
    return out


def poly(pts, cls):
    s = " ".join("%.1f,%.1f" % (x, y) for (x, y) in thin(pts))
    return '<polyline class="%s" points="%s"/>' % (cls, s)


def txt(x, y, cls, s, anchor=None):
    a = ' text-anchor="%s"' % anchor if anchor else ""
    return '<text class="lab %s" x="%.1f" y="%.1f"%s>%s</text>' % (cls, x, y, a, s)


def line(x1, y1, x2, y2, cls):
    return ('<line class="%s" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>'
            % (cls, x1, y1, x2, y2))


# ---------------------------------------------------------------- figure 1
def fig_curves():
    W = 1180
    PW = (W - ML - MR - 34) / 2.0
    PH = 420
    GAP = 34
    NLEG = 3
    H = MT + PH + 24 + NLEG * 22 + MB
    o = ['<svg viewBox="0 0 %d %d" width="100%%" '
         'preserveAspectRatio="xMidYMid meet" role="img" '
         'aria-label="The two curves of question 14.1, each plotted from '
         'evaluated f">' % (W, H)]

    # ---------------- panel A ------------------------------------------------
    ax0, ay0 = ML, MT
    AX, AY = (-4.0, 4.0), (-6.0, 6.0)
    axp = lambda x: ax0 + (x - AX[0]) / (AX[1] - AX[0]) * PW
    ayp = lambda y: ay0 + PH - (y - AY[0]) / (AY[1] - AY[0]) * PH

    o.append('<rect class="pbox" x="%.1f" y="%.1f" width="%.1f" height="%.1f"/>'
             % (ax0, ay0, PW, PH))
    # NOTE: no gridline at x = -1 or x = 1. The vertical asymptotes are drawn
    # there, and a gridline underneath a dashed line only muddies it.
    for gx in range(-4, 5):
        if abs(gx) == 1:
            continue
        o.append(line(axp(gx), ay0, axp(gx), ay0 + PH, "gridfine"))
    for gy in range(-6, 7, 2):
        o.append(line(ax0, ayp(gy), ax0 + PW, ayp(gy), "gridfine"))
    o.append(line(ax0, ayp(0), ax0 + PW, ayp(0), "axisl"))
    o.append(line(axp(0), ay0, axp(0), ay0 + PH, "axisl"))
    # the horizontal asymptote y = 1
    o.append(line(ax0, ayp(1), ax0 + PW, ayp(1), "gridref ha"))
    # the two vertical asymptotes
    for vx in (-1.0, 1.0):
        o.append(line(axp(vx), ay0, axp(vx), ay0 + PH, "gridref va"))
    # the three branches, each on its OWN open interval
    for (lo, hi) in ((AX[0], -1.0), (-1.0, 1.0), (1.0, AX[1])):
        n = 6000
        eps = (hi - lo) * 1e-7
        runs, run = [], []
        for i in range(n + 1):
            x = lo + eps + (hi - lo - 2 * eps) * i / n
            y = fa(x)
            if AY[0] <= y <= AY[1]:
                run.append((axp(x), ayp(y)))
            else:
                if len(run) > 1:
                    runs.append(run)
                run = []
        if len(run) > 1:
            runs.append(run)
        for run in runs:
            o.append(poly(run, "cv"))
    o.append('<circle class="cp" cx="%.1f" cy="%.1f" r="5.5"/>'
             % (axp(0.0), ayp(fa(0.0))))
    for gx in (-4, -3, -2, 2, 3, 4):
        o.append(txt(axp(gx), ayp(0) + 14, "ftk", str(gx), "middle"))
    # NOTE the extremes are omitted deliberately. A tick at +/-6 sits on the
    # panel's own top and bottom edge, and svg-labels PADS its bounding boxes, so
    # the top one was reported as overlapping the panel header 13px above it.
    # The carryover's 22px clearance figure is the reason; dropping two ticks is
    # cheaper than moving the header, and the grid still reads.
    for gy in (-4, -2, 2, 4):
        o.append(txt(axp(0) - 7, ayp(gy) + 3.4, "ftk", str(gy), "end"))

    # ---------------- panel B ------------------------------------------------
    bx0 = ax0 + PW + GAP
    # widened past 3pi: with the range at exactly +/-3pi the critical points
    # there sat half outside the plot frame. Ticks stay at multiples of pi.
    BX = BY = (-3.35 * PI, 3.35 * PI)
    bxp = lambda x: bx0 + (x - BX[0]) / (BX[1] - BX[0]) * PW
    byp = lambda y: ay0 + PH - (y - BY[0]) / (BY[1] - BY[0]) * PH

    o.append('<rect class="pbox" x="%.1f" y="%.1f" width="%.1f" height="%.1f"/>'
             % (bx0, ay0, PW, PH))
    for k in range(-3, 4):
        o.append(line(bxp(k * PI), ay0, bxp(k * PI), ay0 + PH, "gridfine"))
        o.append(line(bx0, byp(k * PI), bx0 + PW, byp(k * PI), "gridfine"))
    o.append(line(bx0, byp(0), bx0 + PW, byp(0), "axisl"))
    o.append(line(bxp(0), ay0, bxp(0), ay0 + PH, "axisl"))
    # the CENTRE LINE y = x. Deliberately not called an asymptote anywhere.
    o.append(line(bxp(BX[0]), byp(BX[0]), bxp(BX[1]), byp(BX[1]),
                  "gridref cl"))
    n = 6000
    run = [(bxp(BX[0] + (BX[1] - BX[0]) * i / n),
            byp(fb(BX[0] + (BX[1] - BX[0]) * i / n))) for i in range(n + 1)]
    o.append(poly(run, "cv"))
    for k in range(-2, 3, 2):                      # even multiples: plain inflection
        o.append('<circle class="ip" cx="%.1f" cy="%.1f" r="4.6"/>'
                 % (bxp(k * PI), byp(fb(k * PI))))
    for k in (-3, -1, 1, 3):                       # odd: flat AND an inflection
        x = k * PI
        o.append(line(bxp(x - 0.9), byp(fb(x)), bxp(x + 0.9), byp(fb(x)), "tg"))
        o.append('<circle class="cp" cx="%.1f" cy="%.1f" r="6"/>'
                 % (bxp(x), byp(fb(x))))
    for k in (-3, -2, -1, 1, 2, 3):
        s = "pi" if k == 1 else ("-pi" if k == -1 else "%dpi" % k)
        o.append(txt(bxp(k * PI), byp(0) + 14, "ftk", s, "middle"))

    # ---------------- headers, short enough to stay inside ------------------
    o.append(txt(ax0, ay0 - 10, "fhd", "A &#183; PART (a) &#183; EVEN &#183; |y| CLIPPED AT 6"))
    o.append(txt(bx0, ay0 - 10, "fhd", "B &#183; PART (b) &#183; ODD &#183; ONE PERIOD IS pi"))

    # ---------------- legend strip, below every drawn element ---------------
    ly = ay0 + PH + 24 + 12
    # A swatch must be drawn the way the thing it names is drawn: solid for the
    # curve and the tangent, dashed only for the three reference lines.
    LEFT = [("cv", "the curve, from evaluated f"),
            ("gridref va", "vertical asymptote &#183; x = -1, x = 1 &#183; never crossed"),
            ("gridref ha", "horizontal asymptote y = 1 &#183; never crossed either")]
    RIGHT = [("gridref cl", "centre line y = x &#183; NOT an asymptote"),
             ("tg", "horizontal tangent &#183; f' = 0, and no extremum"),
             ("RING", "critical point (ring) &#183; inflection (filled dot)")]
    for col, items in ((ax0, LEFT), (bx0, RIGHT)):
        for i, (cls, s) in enumerate(items):
            yy = ly + i * 22
            if cls == "RING":
                o.append('<circle class="cp" cx="%.1f" cy="%.1f" r="5.5"/>'
                         % (col + 7, yy - 3.5))
                o.append('<circle class="ip" cx="%.1f" cy="%.1f" r="4.6"/>'
                         % (col + 23, yy - 3.5))
            else:
                o.append(line(col, yy - 3.5, col + 28, yy - 3.5, cls))
            o.append(txt(col + 38, yy, "flg", s))
    o.append("</svg>")
    return chr(10).join(o)


# ---------------------------------------------------------------- figure 2
def fig_bifurcation():
    W = 1180
    GAP = 46
    PW = (W - ML - MR - 2 * GAP) / 3.0
    PH = 200
    NLEG = 3
    H = MT + PH + 24 + NLEG * 22 + MB
    o = ['<svg viewBox="0 0 %d %d" width="100%%" '
         'preserveAspectRatio="xMidYMid meet" role="img" '
         'aria-label="The derivative one plus A cos x at three amplitudes, '
         'showing that the exam sits on the boundary">' % (W, H)]
    YR = (-1.35, 3.15)
    XR = (-2 * PI, 2 * PI)
    PANELS = [(0.5, "closs", "A = 0.5 &#183; NO CRITICAL POINTS"),
              (1.0, "cacc", "A = 1 &#183; THE EXAM &#183; TOUCHES ZERO"),
              (2.0, "cchn", "A = 2 &#183; A MAX AND A MIN")]
    for pidx, (A, ccls, hdr) in enumerate(PANELS):
        x0 = ML + pidx * (PW + GAP)
        y0 = MT
        xp = lambda x, x0=x0: x0 + (x - XR[0]) / (XR[1] - XR[0]) * PW
        yp = lambda y, y0=y0: y0 + PH - (y - YR[0]) / (YR[1] - YR[0]) * PH
        o.append('<rect class="pbox" x="%.1f" y="%.1f" width="%.1f" height="%.1f"/>'
                 % (x0, y0, PW, PH))
        for gy in (-1, 0, 1, 2, 3):
            o.append(line(x0, yp(gy), x0 + PW, yp(gy), "gridfine"))
        for k in range(-2, 3):
            o.append(line(xp(k * PI), y0, xp(k * PI), y0 + PH, "gridfine"))
        o.append(line(x0, yp(0), x0 + PW, yp(0), "axisl"))
        n = 3000
        run = [(xp(XR[0] + (XR[1] - XR[0]) * i / n),
                yp(1 + A * math.cos(XR[0] + (XR[1] - XR[0]) * i / n)))
               for i in range(n + 1)]
        o.append(poly(run, "cv " + ccls))
        if A >= 1:
            th = math.acos(-1.0 / A)
            for base in (th, -th):
                for kk in (-1, 0, 1):
                    x = base + 2 * kk * PI
                    if XR[0] <= x <= XR[1]:
                        o.append('<circle class="zr %s" cx="%.1f" cy="%.1f" r="5"/>'
                                 % (ccls, xp(x), yp(0.0)))
        o.append(txt(x0, y0 - 10, "fhd", hdr))
        for gy in (0, 2):
            o.append(txt(x0 - 6, yp(gy) + 3.4, "ftk", str(gy), "end"))
        o.append(txt(x0 + PW - 6, y0 + PH - 8, "ftk",
                     "min %s" % ("%.1f" % (1 - A)), "end"))
    ly = MT + PH + 24 + 12
    ROWS = ["1 + A cos x = 0 needs cos x = -1/A, solvable exactly when |A| &#8805; 1,",
            "and giving a REPEATED root exactly when |A| = 1.",
            "So part (b) is the boundary case: critical points exist, none is an extremum."]
    for i, s in enumerate(ROWS):
        o.append(txt(ML, ly + i * 22, "flg", s))
    o.append("</svg>")
    return chr(10).join(o)


if __name__ == "__main__":
    a, b = fig_curves(), fig_bifurcation()
    print("curves %d bytes, bifurcation %d bytes" % (len(a), len(b)))
    assert "var(--" not in a and "var(--" not in b, \
        "a var() reached a presentation attribute; it will not resolve"
    assert 'font-size="' not in a and 'font-size="' not in b, \
        "a font-size attribute would be overridden by the upstream CSS rule"
    assert 'fill="' not in a and 'fill="' not in b, "paint must come from CSS"
    assert 'stroke="' not in a and 'stroke="' not in b, "paint must come from CSS"
    print("contract assertions OK")
