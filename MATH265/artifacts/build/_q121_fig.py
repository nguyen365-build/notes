"""The Q12.1 figure: two panels, one idea each.

Panel A  the tangent at a = 9 lies ABOVE y = sqrt(x) everywhere, so the shaded
         wedge between them IS the error - invisible at 9.2, obvious at 25.
Panel B  the same statement as a measurement: |error| in sqrt(9.2) for each
         candidate anchor, log scale, so "nearest wins" is visible rather than
         asserted.

Every plotted number is computed here, not typed.

Label policy, after svg-labels.mjs reported six real collisions on the first
draft: a horizontal label placed above a SLOPED line is always crossed once it
is long enough, because the line rises through the label's far end.  So the two
line labels live in a LEGEND in the empty region under the curve, and the two
annotations live in the empty region above it, each at 22px row spacing.
"""
import math

W, H = 720, 600

# ---- panel A frame ---------------------------------------------------------
AX0, AX1 = 70.0, 660.0
AY0, AY1 = 86.0, 306.0
XMAX, YMAX = 30.0, 6.0


def px(x):
    return AX0 + x * (AX1 - AX0) / XMAX


def py(y):
    return AY1 - y * (AY1 - AY0) / YMAX


def tangent(x):
    return 3.0 + (x - 9.0) / 6.0


def f(x):
    return math.sqrt(x)


def build():
    o = []
    a = o.append
    a('<svg viewBox="0 0 %d %d" width="%d" height="%d" '
      'xmlns="http://www.w3.org/2000/svg" role="img" '
      'aria-label="Panel A: the tangent line to the square-root curve at x = 9 '
      'lies above the curve everywhere, and the shaded wedge between them is '
      'the approximation error, which widens with the square of the distance '
      'from 9. Panel B: a bar chart on a logarithmic scale of the error in '
      'estimating the square root of 9.2 from six candidate anchors, in which '
      'the anchor 9 gives by far the smallest error.">' % (W, H, W, H))

    # ---------------- panel A ----------------
    a('<text class="lab hd" x="%.1f" y="26">PANEL A - THE TANGENT AT a = 9 SITS '
      'ABOVE THE CURVE</text>' % AX0)
    a('<text class="lab sm" x="%.1f" y="48">the shaded wedge is the error, at '
      'every x</text>' % AX0)

    for gx in range(0, int(XMAX) + 1, 5):
        a('<line class="gridl" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>'
          % (px(gx), AY0, px(gx), AY1))
    for gy in range(0, int(YMAX) + 1):
        a('<line class="gridl" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>'
          % (AX0, py(gy), AX1, py(gy)))

    # the wedge between the tangent and the curve, x in [0, 27]
    top, bot = [], []
    n = 240
    for i in range(n + 1):
        x = 27.0 * i / n
        top.append("%.2f,%.2f" % (px(x), py(tangent(x))))
        bot.append("%.2f,%.2f" % (px(x), py(f(x))))
    a('<polygon class="gapfill" points="%s"/>' % " ".join(top + bot[::-1]))

    a('<line class="axis" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>'
      % (AX0, AY1, AX1, AY1))
    a('<line class="axis" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>'
      % (AX0, AY0, AX0, AY1))

    pts = []
    for i in range(0, 361):
        x = XMAX * i / 360.0
        pts.append("%.2f,%.2f" % (px(x), py(f(x))))
    a('<polyline class="curve" points="%s"/>' % " ".join(pts))

    a('<line class="tanl" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>'
      % (px(0.0), py(tangent(0.0)), px(27.0), py(tangent(27.0))))

    # the one gap worth marking, at x = 25, where it is 24px tall
    a('<line class="gapline" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>'
      % (px(25.0), py(f(25.0)), px(25.0), py(tangent(25.0))))
    a('<circle class="gdot" cx="%.1f" cy="%.1f" r="3"/>' % (px(25.0), py(f(25.0))))
    a('<circle class="gdot" cx="%.1f" cy="%.1f" r="3"/>'
      % (px(25.0), py(tangent(25.0))))

    a('<circle class="dot" cx="%.1f" cy="%.1f" r="5.5"/>' % (px(9.0), py(3.0)))

    for gx in range(0, int(XMAX) + 1, 5):
        a('<text class="lab tk" x="%.1f" y="%.1f" text-anchor="middle">%d</text>'
          % (px(gx), AY1 + 16, gx))
    for gy in (2, 4, 6):                      # 0 would collide with the x-tick 0
        a('<text class="lab tk" x="%.1f" y="%.1f" text-anchor="end">%d</text>'
          % (AX0 - 8, py(gy) + 4, gy))

    # annotations, in the empty band above the curve on the left
    gap92 = tangent(9.2) - f(9.2)
    gap25 = tangent(25.0) - f(25.0)
    # the leader stops 20px clear of the lower label's baseline; svg-labels
    # pads its boxes, so 14px is the floor and 20 is the working figure.
    a('<line class="leadr" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>'
      % (px(9.2), py(3.08), px(6.5), 162.0))
    a('<text class="lab" x="%.1f" y="%.1f">at x = 9.2 the wedge is %.5f</text>'
      % (px(0.6), 118.0, gap92))
    a('<text class="lab sm" x="%.1f" y="%.1f">too thin to draw; at x = 25 it is '
      '%.3f</text>' % (px(0.6), 140.0, gap25))

    # anchor label, in the empty region under the curve
    a('<text class="lab am" x="%.1f" y="%.1f" text-anchor="middle">anchor '
      '(9, 3)</text>' % (px(9.0), py(3.0) + 54))

    # legend, in the empty region under the curve on the right
    LX = px(15.6)
    LY = py(1.55)
    a('<rect class="tansw" x="%.1f" y="%.1f" width="26" height="4" rx="2"/>'
      % (LX, LY - 9))
    a('<text class="lab am" x="%.1f" y="%.1f">L(x) = 3 + (x - 9)/6, the tangent '
      'at a = 9</text>' % (LX + 36, LY - 2))
    a('<rect class="cursw" x="%.1f" y="%.1f" width="26" height="4" rx="2"/>'
      % (LX, LY + 13))
    a('<text class="lab" x="%.1f" y="%.1f">y = sqrt(x)</text>' % (LX + 36, LY + 20))

    # ---------------- panel B ----------------
    BY = 366.0
    a('<text class="lab hd" x="%.1f" y="%.1f">PANEL B - ERROR IN sqrt(9.2) BY '
      'CHOICE OF ANCHOR</text>' % (AX0, BY))
    a('<text class="lab sm" x="%.1f" y="%.1f">log scale; all six anchors are '
      'exact, only one is near</text>' % (AX0, BY + 22))

    anchors = [4.0, 8.41, 9.0, 9.61, 12.25, 16.0]
    tv = math.sqrt(9.2)
    rows = []
    for av in anchors:
        est = math.sqrt(av) + (9.2 - av) / (2.0 * math.sqrt(av))
        rows.append((av, abs(tv - est)))

    BX0, BX1 = 210.0, 600.0
    LO, HI = -4.0, 0.0
    scale = (BX1 - BX0) / (HI - LO)
    y0 = BY + 48.0
    step = 27.0

    for gl in range(int(LO), int(HI) + 1):
        gxp = BX0 + (gl - LO) * scale
        a('<line class="gridl" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>'
          % (gxp, y0 - 14, gxp, y0 + step * len(rows) - 10))
        a('<text class="lab tk" x="%.1f" y="%.1f" text-anchor="middle">1e%d</text>'
          % (gxp, y0 + step * len(rows) + 8, gl))

    for i, (av, err) in enumerate(rows):
        yy = y0 + i * step
        wpx = max((math.log10(err) - LO) * scale, 1.0)
        best = (av == 9.0)
        a('<rect class="%s" x="%.1f" y="%.1f" width="%.1f" height="14" rx="2"/>'
          % ("barbest" if best else "bar", BX0, yy - 11, wpx))
        nm = ("a = %g" % av) + {9.61: " (3.1 squared)",
                                8.41: " (2.9 squared)",
                                12.25: " (3.5 squared)"}.get(av, "")
        a('<text class="lab %s" x="%.1f" y="%.1f" text-anchor="end">%s</text>'
          % ("am" if best else "sm", BX0 - 12, yy, nm))
        a('<text class="lab %s" x="%.1f" y="%.1f">%.6f</text>'
          % ("am" if best else "tk", BX0 + wpx + 10, yy, err))

    a('</svg>')
    return "".join(o)


if __name__ == "__main__":
    s = build()
    print(len(s), "bytes,", s.count("<text"), "text elements")
    assert not [c for c in s if ord(c) > 127], "non-ASCII in the svg"
