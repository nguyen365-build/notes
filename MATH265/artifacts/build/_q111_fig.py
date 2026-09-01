"""Figure for the Q11.1 artifact.

Two panels.  Left: the pile's cross-section, drawn to scale, so that the
"diameter equals height" constraint is visible rather than asserted.  Right:
the real growth curve h(t) = (6t/pi)^(1/3) with the tangent at the instant the
exam asks about, so the answer 1/(8 pi) is a slope you can see flattening.

Markup contract required by Work\\knowledge\\tools\\artifact-lint\\svg-labels.mjs:
  - the wrapper element carries class "figbox"
  - every <text> to be checked carries class "lab"
  - every grid <line> carries class "gridl" (a bare <line> reports tagName
    "line", which does NOT match the gate's /grid|axis/ exemption)
"""
import math
import os

PI = math.pi
W, H = 760, 306


def h_of_t(t):
    return (6.0 * t / PI) ** (1.0 / 3.0)


# ---- right panel scales ----------------------------------------------------
T0, T1 = 0.0, 70.0
H0, H1 = 0.0, 6.0
PX0, PX1 = 424.0, 742.0
PY0, PY1 = 268.0, 62.0          # h = 0 at the bottom


def sx(t):
    return PX0 + (t - T0) / (T1 - T0) * (PX1 - PX0)


def sy(h):
    return PY0 + (h - H0) / (H1 - H0) * (PY1 - PY0)


def build():
    tstar = PI * 4.0 ** 3 / 12.0 / 0.5
    slope = 1.0 / (8.0 * PI)

    curve = " ".join(
        "%.2f,%.2f" % (sx(T0 + i * (T1 - T0) / 160.0), sy(h_of_t(T0 + i * (T1 - T0) / 160.0)))
        for i in range(161))

    # tangent at t*, drawn as a chord in plot units then mapped
    dt = 21.0
    tan_pts = " ".join("%.2f,%.2f" % (sx(tstar + d), sy(4.0 + slope * d))
                       for d in (-dt, dt))

    grid = []
    for hv in (2.0, 4.0, 6.0):
        grid.append('<line class="gridl" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>'
                    % (PX0, sy(hv), PX1, sy(hv)))
    for tv in (20.0, 40.0, 60.0):
        grid.append('<line class="gridl" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>'
                    % (sx(tv), PY0, sx(tv), PY1))

    # ---- left panel: the cone, drawn with base width == height -------------
    apex = (168.0, 66.0)
    bl, br = (68.0, 246.0), (268.0, 246.0)          # 200 wide, 180 tall on screen
    mid = (168.0, 246.0)

    parts = []
    parts.append('<svg viewBox="0 0 %d %d" width="100%%" role="img" '
                 'aria-label="Left: the gravel pile in cross-section, with base '
                 'diameter equal to height. Right: the height of the pile against '
                 'time, with the tangent at four metres.">' % (W, H))

    # ---- LEFT --------------------------------------------------------------
    parts.append('<text class="lab hd" x="18" y="34">THE PILE AT ONE INSTANT</text>')
    parts.append('<ellipse class="cone" cx="168" cy="246" rx="100" ry="15"/>')
    parts.append('<polygon class="cone" points="%.0f,%.0f %.0f,%.0f %.0f,%.0f"/>'
                 % (apex[0], apex[1], bl[0], bl[1], br[0], br[1]))
    # height marker
    parts.append('<line class="dim" x1="%.0f" y1="%.0f" x2="%.0f" y2="%.0f" '
                 'marker-start="url(#a111)" marker-end="url(#a111)"/>'
                 % (mid[0], apex[1], mid[0], mid[1]))
    parts.append('<text class="lab" x="176" y="160">h</text>')
    # diameter marker, below the base
    parts.append('<line class="dim" x1="%.0f" y1="278" x2="%.0f" y2="278" '
                 'marker-start="url(#a111)" marker-end="url(#a111)"/>' % (bl[0], br[0]))
    parts.append('<text class="lab" x="140" y="296">d = h</text>')
    # radius marker, on the base
    parts.append('<line class="dim2" x1="%.0f" y1="246" x2="%.0f" y2="246"/>'
                 % (mid[0], br[0]))
    parts.append('<text class="lab" x="286" y="240">r = h/2</text>')
    parts.append('<text class="lab sm" x="18" y="270">always true, so it may be '
                 'substituted BEFORE differentiating</text>')

    # ---- RIGHT -------------------------------------------------------------
    parts.append('<text class="lab hd" x="400" y="34">THE PILE OVER TIME</text>')
    parts.extend(grid)
    parts.append('<line class="axis" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>'
                 % (PX0, PY0, PX1, PY0))
    parts.append('<line class="axis" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>'
                 % (PX0, PY0, PX0, PY1))
    parts.append('<polyline class="curve" points="%s"/>' % curve)
    parts.append('<polyline class="tang" points="%s"/>' % tan_pts)
    parts.append('<circle class="dot" cx="%.2f" cy="%.2f" r="4.2"/>'
                 % (sx(tstar), sy(4.0)))
    parts.append('<text class="lab" x="%.0f" y="%.0f">h = 4 m</text>'
                 % (sx(tstar) - 62, sy(4.0) - 14))
    parts.append('<text class="lab sm" x="%.0f" y="%.0f">at t = 33.5 min</text>'
                 % (sx(tstar) - 62, sy(4.0) + 1))
    parts.append('<text class="lab am" x="%.0f" y="%.0f">slope = 1/(8 pi)</text>'
                 % (sx(tstar) + 14, sy(4.0) - 30))
    parts.append('<text class="lab sm" x="%.0f" y="%.0f">the curve flattens, so the '
                 'pile rises ever more slowly</text>' % (PX0 + 4, PY1 - 18))
    parts.append('<text class="lab sm" x="%.1f" y="%.1f">t (min)</text>'
                 % (PX1 - 46, PY0 + 22))
    parts.append('<text class="lab sm" x="%.1f" y="%.1f">h (m)</text>'
                 % (PX0 - 6, PY1 - 4))
    for hv in (2.0, 4.0, 6.0):
        parts.append('<text class="lab tk" x="%.1f" y="%.1f">%d</text>'
                     % (PX0 - 16, sy(hv) + 4, int(hv)))
    for tv in (20.0, 40.0, 60.0):
        parts.append('<text class="lab tk" x="%.1f" y="%.1f">%d</text>'
                     % (sx(tv) - 7, PY0 + 18, int(tv)))

    parts.append('<defs><marker id="a111" markerWidth="7" markerHeight="7" '
                 'refX="3.5" refY="3.5" orient="auto">'
                 '<path d="M0,0 L7,3.5 L0,7 z" class="mk"/></marker></defs>')
    parts.append("</svg>")
    return "\n".join(parts)


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_q111_fig.svg")
    open(out, "w", encoding="utf-8").write(build())
    print("wrote", out)
