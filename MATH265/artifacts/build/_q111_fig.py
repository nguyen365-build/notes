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

Label placement is MEASURED, not eyeballed.  The curve is concave down, so the
band below the tangent and right of t* is empty; every callout lives there,
spaced 20-22px apart so the gate's own bbox padding cannot make two touch.
"""
import math
import os

PI = math.pi
W, H = 760, 312


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
    dt = 21.0
    tan_pts = " ".join("%.2f,%.2f" % (sx(tstar + d), sy(4.0 + slope * d))
                       for d in (-dt, dt))

    parts = []
    parts.append('<svg viewBox="0 0 %d %d" width="100%%" role="img" '
                 'aria-label="Left: the gravel pile in cross-section, with base '
                 'diameter equal to height. Right: the height of the pile against '
                 'time, with the tangent at four metres."> ' % (W, H))

    # ---- LEFT: the pile at one instant -------------------------------------
    apex = (168.0, 70.0)
    bl, br = (68.0, 250.0), (268.0, 250.0)
    parts.append('<text class="lab hd" x="18" y="34">THE PILE AT ONE INSTANT</text>')
    parts.append('<ellipse class="cone" cx="168" cy="250" rx="100" ry="15"/>')
    parts.append('<polygon class="cone" points="%.0f,%.0f %.0f,%.0f %.0f,%.0f"/>'
                 % (apex[0], apex[1], bl[0], bl[1], br[0], br[1]))
    parts.append('<line class="dim" x1="168" y1="70" x2="168" y2="250" '
                 'marker-start="url(#a111)" marker-end="url(#a111)"/>')
    parts.append('<text class="lab" x="178" y="164">h</text>')
    parts.append('<line class="dim" x1="68" y1="282" x2="268" y2="282" '
                 'marker-start="url(#a111)" marker-end="url(#a111)"/>')
    parts.append('<text class="lab" x="142" y="302">d = h</text>')
    parts.append('<line class="dim2" x1="168" y1="250" x2="268" y2="250"/>')
    parts.append('<text class="lab" x="286" y="244">r = h/2</text>')
    parts.append('<text class="lab sm" x="18" y="54">always true, at every size</text>')

    # ---- RIGHT: the pile over time -----------------------------------------
    parts.append('<text class="lab hd" x="424" y="34">THE PILE OVER TIME'
                 ' &#183; h IN m, t IN min</text>')
    for hv in (2.0, 4.0, 6.0):
        parts.append('<line class="gridl" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>'
                     % (PX0, sy(hv), PX1, sy(hv)))
    for tv in (20.0, 40.0, 60.0):
        parts.append('<line class="gridl" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>'
                     % (sx(tv), PY0, sx(tv), PY1))
    parts.append('<line class="axis" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>'
                 % (PX0, PY0, PX1, PY0))
    parts.append('<line class="axis" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>'
                 % (PX0, PY0, PX0, PY1))
    parts.append('<polyline class="curve" points="%s"/>' % curve)
    parts.append('<polyline class="tang" points="%s"/>' % tan_pts)
    parts.append('<circle class="dot" cx="%.2f" cy="%.2f" r="4.2"/>'
                 % (sx(tstar), sy(4.0)))

    # callouts, in the empty band below-right of the marked point
    parts.append('<text class="lab" x="596" y="168">h = 4 m</text>')
    parts.append('<text class="lab sm" x="596" y="190">at t = 33.5 min</text>')
    parts.append('<text class="lab am" x="596" y="212">slope = 1/(8 pi)</text>')
    parts.append('<text class="lab sm" x="596" y="234">it keeps flattening</text>')

    for hv in (2.0, 4.0, 6.0):
        parts.append('<text class="lab tk" x="%.1f" y="%.1f">%d</text>'
                     % (PX0 - 18, sy(hv) + 4, int(hv)))
    for tv in (20.0, 40.0, 60.0):
        parts.append('<text class="lab tk" x="%.1f" y="%.1f">%d</text>'
                     % (sx(tv) - 7, PY0 + 19, int(tv)))

    parts.append('<defs><marker id="a111" markerWidth="7" markerHeight="7" '
                 'refX="3.5" refY="3.5" orient="auto">'
                 '<path d="M0,0 L7,3.5 L0,7 z" class="mk"/></marker></defs>')
    parts.append("</svg>")
    return "\n".join(parts)


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_q111_fig.svg")
    open(out, "w", encoding="utf-8").write(build())
    print("wrote", out)
