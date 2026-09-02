"""Figure for the Q11.2 artifact.

Two panels, both drawn to scale from the real numbers.

LEFT: the triangle at the instant, with the rocket's velocity resolved into the
component the radar actually measures.  The two arrows are drawn at their true
relative lengths (the projected arrow is exactly y/z = 4/sqrt(41) = 0.6247 of
the vertical one), so "the radar sees less than the true speed" is something
you can measure off the page rather than a claim.

RIGHT: dy/dt against y for a fixed 2000 mi/h radar rate.  The curve falls
toward the given 2000 and never reaches it, which is the page's sanity check
drawn as a picture, and the exam instant sits on it as a marked point.

Markup contract required by Work\\knowledge\\tools\\artifact-lint\\svg-labels.mjs:
  - the wrapper element carries class "figbox"
  - every <text> to be checked carries class "lab"
  - every grid <line> carries class "gridl" (a bare <line> reports tagName
    "line", which does NOT match the gate's /grid|axis/ exemption)

Label placement is MEASURED against the gate, not eyeballed.  The gate pads its
bounding boxes, so 15px of clearance is not enough; callouts are kept 20px+ off
every drawn segment.
"""
import math

W, H = 760, 352

S41 = math.sqrt(41.0)
ZDOT = 2000.0
ANS = 500.0 * S41

# ---- left panel: the triangle ----------------------------------------------
GY = 286.0                 # ground line
PAD_X = 262.0              # launch pad
MI = 42.0                  # pixels per mile
RAD_X = PAD_X - 5.0 * MI   # radar, 5 mi from the pad
ROC_Y = GY - 4.0 * MI      # rocket, 4 mi up

VLEN = 62.0                # vertical velocity arrow, pixels


def _arrow(x1, y1, x2, y2, cls):
    """A line plus a solid head, as two elements."""
    dx, dy = x2 - x1, y2 - y1
    L = math.hypot(dx, dy)
    ux, uy = dx / L, dy / L
    px, py = -uy, ux
    hb = 9.0
    bx, by = x2 - ux * hb, y2 - uy * hb
    head = "%.2f,%.2f %.2f,%.2f %.2f,%.2f" % (
        x2, y2, bx + px * 4.2, by + py * 4.2, bx - px * 4.2, by - py * 4.2)
    return ('<line class="%s" x1="%.2f" y1="%.2f" x2="%.2f" y2="%.2f" />'
            '<polygon class="%shd" points="%s" />'
            % (cls, x1, y1, bx, by, cls, head))


# ---- right panel scales ----------------------------------------------------
Y0, Y1 = 2.0, 20.0
R0, R1 = 1800.0, 5600.0
PX0, PX1 = 470.0, 738.0
PY0, PY1 = 286.0, 66.0


def sx(y):
    return PX0 + (y - Y0) / (Y1 - Y0) * (PX1 - PX0)


def sy(r):
    return PY0 + (r - R0) / (R1 - R0) * (PY1 - PY0)


def ydot(y):
    return ZDOT * math.sqrt(25.0 + y * y) / y


def build():
    p = []
    a = p.append
    a('<svg viewBox="0 0 %d %d" width="%d" height="%d" '
      'xmlns="http://www.w3.org/2000/svg" role="img" '
      'aria-label="Left: the right triangle at the instant, with the rocket velocity '
      'resolved along the radar line of sight. Right: the rocket speed against height, '
      'falling toward the given 2000 mi per hour and never reaching it.">'
      % (W, H, W, H))

    # ================= LEFT PANEL =================
    a('<text class="lab hd" x="24" y="30">THE TRIANGLE AT THE INSTANT</text>')

    # ground
    a('<line class="axis" x1="24" y1="%.1f" x2="330" y2="%.1f" />' % (GY, GY))

    # the triangle
    a('<polygon class="tri2" points="%.1f,%.1f %.1f,%.1f %.1f,%.1f" />'
      % (RAD_X, GY, PAD_X, GY, PAD_X, ROC_Y))
    # the fixed leg, emphasised
    a('<line class="legf" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" />'
      % (RAD_X, GY, PAD_X, GY))
    # the varying leg
    a('<line class="legv" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" />'
      % (PAD_X, GY, PAD_X, ROC_Y))
    # the hypotenuse
    a('<line class="hypo" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" />'
      % (RAD_X, GY, PAD_X, ROC_Y))

    # right-angle marker at the pad
    a('<polyline class="rang" points="%.1f,%.1f %.1f,%.1f %.1f,%.1f" />'
      % (PAD_X - 13, GY, PAD_X - 13, GY - 13, PAD_X, GY - 13))

    # the radar station and the rocket
    a('<circle class="stn" cx="%.1f" cy="%.1f" r="5" />' % (RAD_X, GY))
    a('<circle class="roc" cx="%.1f" cy="%.1f" r="5" />' % (PAD_X, ROC_Y))

    # velocity arrows, drawn at true relative length
    a(_arrow(PAD_X, ROC_Y, PAD_X, ROC_Y - VLEN, "varr"))
    ux, uy = (PAD_X - RAD_X) / (5.0 * MI * S41 / 5.0), (ROC_Y - GY) / (4.0 * MI * S41 / 4.0)
    # unit vector from radar to rocket
    dx, dy = PAD_X - RAD_X, ROC_Y - GY
    L = math.hypot(dx, dy)
    ux, uy = dx / L, dy / L
    proj = VLEN * (4.0 / S41)
    a(_arrow(PAD_X, ROC_Y, PAD_X + ux * proj, ROC_Y + uy * proj, "sarr"))

    # Labels. Placement is MEASURED against svg-labels.mjs, not eyeballed: the
    # gate pads its bounding boxes, so stacked callouts sit 22px apart (16px was
    # reported as an overlap on the first run) and every callout is kept 20px+
    # off every drawn segment.
    a('<text class="lab" x="%.1f" y="%.1f" text-anchor="middle">x = 5 mi</text>'
      % ((RAD_X + PAD_X) / 2.0, GY + 22))
    a('<text class="lab sm" x="%.1f" y="%.1f">radar</text>' % (RAD_X - 20, GY + 22))
    a('<text class="lab sm am" x="%.1f" y="%.1f" text-anchor="middle">'
      'FIXED - substitute it early</text>' % ((RAD_X + PAD_X) / 2.0, GY + 44))
    a('<text class="lab" x="%.1f" y="%.1f">y = 4 mi</text>' % (PAD_X + 14, GY - 66))
    a('<text class="lab sm" x="%.1f" y="%.1f">one instant only</text>'
      % (PAD_X + 14, GY - 44))
    # the z callout sits ABOVE the hypotenuse: on the first run the line crossed
    # both of these where they were, at the hypotenuse's own midpoint.
    a('<text class="lab am" x="175" y="138" text-anchor="end">z = &#8730;41</text>')
    a('<text class="lab sm" x="175" y="160" text-anchor="end">not 3, not 5</text>')
    a('<text class="lab vtr" x="%.1f" y="%.1f" text-anchor="end">3201.56</text>'
      % (PAD_X - 14, ROC_Y - VLEN + 2))
    a('<text class="lab sm" x="%.1f" y="%.1f" text-anchor="end">true speed</text>'
      % (PAD_X - 14, ROC_Y - VLEN + 24))
    a('<text class="lab vsn" x="%.1f" y="%.1f">2000</text>'
      % (PAD_X + ux * proj + 12, ROC_Y + uy * proj - 8))
    a('<text class="lab sm" x="%.1f" y="%.1f">what the radar sees</text>'
      % (PAD_X + ux * proj + 12, ROC_Y + uy * proj + 14))

    # ================= RIGHT PANEL =================
    a('<text class="lab hd" x="424" y="30">SPEED AGAINST HEIGHT - dy/dt IN mi/h, '
      'y IN mi</text>')

    # grid
    for r in (2000.0, 3000.0, 4000.0, 5000.0):
        a('<line class="gridl" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" />'
          % (PX0, sy(r), PX1, sy(r)))
    for yv in (5.0, 10.0, 15.0, 20.0):
        a('<line class="gridl" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" />'
          % (sx(yv), PY0, sx(yv), PY1))

    # axes
    a('<line class="axis" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" />'
      % (PX0, PY0, PX1, PY0))
    a('<line class="axis" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" />'
      % (PX0, PY0, PX0, PY1))

    # the asymptote at the given rate
    a('<line class="asym" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" />'
      % (PX0, sy(ZDOT), PX1, sy(ZDOT)))

    # the curve
    pts = []
    n = 240
    for i in range(n + 1):
        yv = Y0 + (Y1 - Y0) * i / n
        rv = ydot(yv)
        if rv > R1:
            continue
        pts.append("%.2f,%.2f" % (sx(yv), sy(rv)))
    a('<polyline class="curve" points="%s" />' % " ".join(pts))

    # the exam instant
    a('<line class="drop" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" />'
      % (sx(4.0), sy(ANS), sx(4.0), PY0))
    a('<circle class="dot" cx="%.1f" cy="%.1f" r="5.2" />' % (sx(4.0), sy(ANS)))

    # ticks
    for r, t in ((2000.0, "2000"), (3000.0, "3000"), (4000.0, "4000"), (5000.0, "5000")):
        a('<text class="lab tk" x="%.1f" y="%.1f" text-anchor="end">%s</text>'
          % (PX0 - 8, sy(r) + 4, t))
    for yv, t in ((5.0, "5"), (10.0, "10"), (15.0, "15"), (20.0, "20")):
        a('<text class="lab tk" x="%.1f" y="%.1f" text-anchor="middle">%s</text>'
          % (sx(yv), PY0 + 17, t))

    # callouts, in the empty band above the curve and right of the instant
    a('<text class="lab am" x="%.1f" y="%.1f">4 mi, 3201.56</text>'
      % (sx(4.0) + 16, sy(ANS) - 30))
    a('<text class="lab sm" x="%.1f" y="%.1f">the exam instant</text>'
      % (sx(4.0) + 16, sy(ANS) - 8))
    # The asymptote annotation is DELETED rather than repositioned.  The wedge
    # between the curve and the 2000 line is under 15px tall at every x, so no
    # placement clears the gate; the "2000" tick already names the line, the
    # dashed teal styling already distinguishes it, and the caption carries the
    # meaning.  Deleting a label the figure cannot hold is the right fix.

    a('</svg>')
    return "".join(p)


if __name__ == "__main__":
    print(build()[:400])
