"""Q16.2 figure generator.

TWO PANELS, one SVG.

  Panel A  THE PARTITION, drawn as 26 unit cells - one per seeded wrong answer, in the
           order the census reports them.  A unit chart rather than a bar chart, because
           the page's claim is about a COUNT and an exact split, and a unit chart cannot
           distort a ratio the way an axis can (carryover: "log scale hides the ratio").
           Twelve teal cells on the left are what differentiating back catches.  Fourteen
           on the right are what it misses, and SEVEN of those fourteen - the largest
           single blind family, drawn in the accent - are naming errors.  That is the
           whole page in one row of squares.

  Panel B  ONE INTEGRAND, TWO NAME LISTS.  Part (d) reached two ways.  The two routes
           land on the IDENTICAL function, measured, and owe different technique lists.

Carryover contracts honoured here:
  - NO leader lines, and every label sits inside a chip or in a band below its frame
    (19.9 / 20.7).  This figure draws ZERO <line> elements: frames, cells and chips are
    all <rect>, and the connectors are <polygon> chevrons.  That is a real design choice
    (there is nothing for a label to collide WITH), but it also makes svg-labels' lineHits
    arm VACUOUS on this page, so only its labelPairs and outsideBox arms are live here and
    those are the ones proved with a seeded control.
  - Every <text> carries class="lab" so svg-labels measures it.
  - Every drawn shape has an EXPLICIT fill; var() does not resolve in an SVG presentation
    attribute (20.7), so colours are literal and a <style> block inside the SVG themes them.
  - The viewBox leaves room for the outermost label (19.9).
  - Pure ASCII: a non-ASCII byte mojibakes under a local file:// render (4).
"""

W = 980
H = 530

# ---- the census, measured by harness section q162c ----------------------------------------
# (family label, count, bucket)   bucket: "hit" caught, "miss" blind, "name" blind AND the
# subject of this page.
CENSUS = [
    ("DROPPED FACTOR", 4, "hit"),
    ("CHAIN FACTOR", 3, "hit"),
    ("POWER SLIP", 3, "hit"),
    ("ALGEBRA SLIP", 2, "hit"),
    ("PLUS C", 3, "miss"),
    ("DOMAIN", 3, "miss"),
    ("LIMITS", 1, "miss"),
    ("NAMING", 7, "name"),
]
SPLIT_AFTER = 4          # the first four families are the detected half

ROUTE1 = ["int sec^3 x tan x dx", "REWRITE by the hint", "SUBSTITUTE u = sec x", "sec^3 x / 3"]
ROUTE2 = ["int sec^3 x tan x dx", "REWRITE as sin x/cos^4 x", "SUBSTITUTE u = cos x",
          "1 / (3 cos^3 x)"]


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def build(seed_collision=False):
    o = []
    o.append('<svg viewBox="0 0 %d %d" width="100%%" role="img" '
             'aria-label="Panel A: twenty-six seeded wrong answers as unit cells. Twelve on '
             'the left are detected by differentiating the answer back. Fourteen on the right '
             'are invisible to it, and seven of those fourteen - the largest single blind '
             'family - are naming errors. Panel B: one integrand reached by two routes that '
             'land on the identical function and owe two different technique lists." '
             'xmlns="http://www.w3.org/2000/svg">' % (W, H))

    # ---- theming -----------------------------------------------------------------------
    # DEFECT FOUND BY LOOKING, and it is INHERITED from the Q16.1 figure.  The series wrote
    # its dark overrides as a bare
    #     :root[data-theme="dark"] .x, :root:not([data-theme="light"]) .x { ... }
    # pair with NO media query.  The viewer has THREE theme states, and the default one
    # stamps nothing at all - so `:root:not([data-theme="light"])` matches an UNSTAMPED
    # LIGHT page and the figure paints its dark palette on a white ground.  Rendered and
    # looked at: both panels came out near-black in the light theme and the caption text
    # was near-white on white.  No gate reports this; only the screenshot does.
    #
    # The correct contract: bare :root carries the complete LIGHT palette; the
    # `:not([data-theme="light"])` half lives INSIDE @media (prefers-color-scheme: dark);
    # and `[data-theme="dark"]` repeats it so an explicit toggle wins in both directions.
    PALETTE = [
        ("fg162", "fill", "#14181F", "#E6EAF0"),
        ("fmut162", "fill", "#5C6672", "#939DAA"),
        ("fam162", "fill", "#B57608", "#F2A53C"),
        ("fpan162", "fill", "#FFFFFF", "#1B2029"),
        ("fsunk162", "fill", "#F2F4F7", "#161B23"),
        ("fhit162", "fill", "#2E6F6A", "#4FA39B"),
        ("fmiss162", "fill", "#B4522F", "#D9764E"),
        ("fname162", "fill", "#D9901F", "#F2A53C"),
        ("sfrm162", "stroke", "#AEB6C0", "#3D4552"),
        ("schip162", "stroke", "#C6CCD5", "#333B47"),
    ]
    css = ["<style>"]
    for cls, prop, light, _dark in PALETTE:
        extra = " fill:none;" if cls in ("sfrm162", "schip162") else ""
        sw = " stroke-width:%s;" % ("1.2" if cls == "sfrm162" else "1") if prop == "stroke" else ""
        css.append("  .%s{ %s:%s;%s%s }" % (cls, prop, light, sw, extra))
    css.append("  @media (prefers-color-scheme: dark){")
    for cls, prop, _light, dark in PALETTE:
        css.append('    :root:not([data-theme="light"]) .%s{ %s:%s; }' % (cls, prop, dark))
    css.append("  }")
    for cls, prop, _light, dark in PALETTE:
        css.append('  :root[data-theme="dark"] .%s{ %s:%s; }' % (cls, prop, dark))
    css.append("</style>")
    o.append("\n".join(css))

    MONO = "'IBM Plex Mono','SFMono-Regular',Consolas,monospace"
    SANS = "'IBM Plex Sans','Segoe UI',system-ui,sans-serif"

    def t(x, y, s, size=11, cls="fg162", anchor="start", weight="400", fam=SANS, ls="0"):
        o.append('<text class="lab %s" x="%.1f" y="%.1f" font-family="%s" font-size="%.1f" '
                 'font-weight="%s" letter-spacing="%s" text-anchor="%s">%s</text>'
                 % (cls, x, y, fam, size, weight, ls, anchor, esc(s)))

    def rect(x, y, w, h, cls, rx=0):
        o.append('<rect class="%s" x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%d"/>'
                 % (cls, x, y, w, h, rx))

    # ============================================================ PANEL A
    AX, AY, AW, AH = 34, 54, 912, 86
    t(AX, 32, "PANEL A", 10, "fam162", "start", "600", MONO, "0.10em")
    t(AX + 78, 32, "26 SEEDED WRONG ANSWERS, AND WHAT DIFFERENTIATING BACK SEES",
      10, "fmut162", "start", "500", MONO, "0.10em")
    rect(AX, AY, AW, AH, "fsunk162")
    o.append('<rect class="sfrm162" x="%d" y="%d" width="%d" height="%d" fill="none"/>'
             % (AX, AY, AW, AH))

    # geometry: 26 cells, a small gap between cells, a wider gap between families,
    # and the widest gap at the detected / blind boundary.
    PAD = 18
    inner = AW - 2 * PAD
    n_cells = sum(c for _, c, _ in CENSUS)
    n_famgap = len(CENSUS) - 1
    GAP, FAMGAP, SPLITGAP = 3.0, 9.0, 30.0
    extras = (n_famgap - 1) * FAMGAP + SPLITGAP
    cw = (inner - (n_cells - len(CENSUS)) * GAP - extras) / n_cells
    ch = 44
    cy = AY + 20

    x = AX + PAD
    marks = {}
    for gi, (name, cnt, bucket) in enumerate(CENSUS):
        gx0 = x
        for k in range(cnt):
            cls = {"hit": "fhit162", "miss": "fmiss162", "name": "fname162"}[bucket]
            rect(x, cy, cw, ch, cls, 1)
            x += cw + (GAP if k < cnt - 1 else 0)
        marks[name] = (gx0, x)
        if gi < len(CENSUS) - 1:
            x += SPLITGAP if gi == SPLIT_AFTER - 1 else FAMGAP

    det_x0 = marks[CENSUS[0][0]][0]
    det_x1 = marks[CENSUS[SPLIT_AFTER - 1][0]][1]
    bl_x0 = marks[CENSUS[SPLIT_AFTER][0]][0]
    bl_x1 = marks[CENSUS[-1][0]][1]

    # the two column verdicts, in a band below the frame
    t((det_x0 + det_x1) / 2, AY + AH + 26, "DETECTED  12 of 26", 12, "fg162", "middle",
      "600", MONO, "0.06em")
    t((bl_x0 + bl_x1) / 2, AY + AH + 26, "INVISIBLE  14 of 26", 12, "fg162", "middle",
      "600", MONO, "0.06em")

    # the legend, two rows of four, 26px apart vertically (19.9's measured band step)
    LEG_Y = AY + AH + 62
    for i, (name, cnt, bucket) in enumerate(CENSUS):
        col, row = i % 4, i // 4
        lx = AX + PAD + col * 222
        ly = LEG_Y + row * 26
        cls = {"hit": "fhit162", "miss": "fmiss162", "name": "fname162"}[bucket]
        rect(lx, ly - 9, 10, 10, cls, 1)
        t(lx + 17, ly, "%s  %d" % (name, cnt), 10.5,
          "fam162" if bucket == "name" else "fmut162", "start",
          "600" if bucket == "name" else "500", MONO, "0.06em")

    # NOTE: an explanatory sentence used to sit here, at LEG_Y + 56. svg-labels reported it
    # as outsideBox, and looking at why showed it was also only 20px clear of panel B's
    # header - under 19.9's measured 26px band step. It is prose, not a chart label, so it
    # was DELETED from the figure and folded into the page's <p class="cap162"> instead.
    # Deleting a label is a legitimate fix and is usually the right one.

    # ============================================================ PANEL B
    BX, BY, BW, BH = 34, 300, 912, 148
    t(BX, 278, "PANEL B", 10, "fam162", "start", "600", MONO, "0.10em")
    t(BX + 78, 278, "ONE INTEGRAND, TWO ROUTES, TWO TECHNIQUE LISTS",
      10, "fmut162", "start", "500", MONO, "0.10em")
    rect(BX, BY, BW, BH, "fsunk162")
    o.append('<rect class="sfrm162" x="%d" y="%d" width="%d" height="%d" fill="none"/>'
             % (BX, BY, BW, BH))

    CW, NCH = 196, 4
    CGAP = (BW - 2 * PAD - NCH * CW) / (NCH - 1)
    for ri, route in enumerate([ROUTE1, ROUTE2]):
        cyy = BY + 34 + ri * 62
        for ci, txt in enumerate(route):
            cx = BX + PAD + ci * (CW + CGAP)
            rect(cx, cyy, CW, 34, "fpan162", 2)
            o.append('<rect class="schip162" x="%.1f" y="%.1f" width="%.1f" height="34" '
                     'rx="2" fill="none"/>' % (cx, cyy, CW))
            t(cx + CW / 2, cyy + 22, txt, 10.5,
              "fam162" if "SUBSTITUTE" in txt else "fg162", "middle",
              "600" if "SUBSTITUTE" in txt else "400", MONO, "0.03em")
            if ci < NCH - 1:
                mx = cx + CW + CGAP / 2
                my = cyy + 17
                o.append('<polygon class="fmut162" points="%.1f,%.1f %.1f,%.1f %.1f,%.1f"/>'
                         % (mx - 5, my - 6, mx + 5, my, mx - 5, my + 6))

    t(BX + PAD, BY + BH + 26,
      "Measured identical to 4.441e-16 across seven sample points - the same function, "
      "not merely a constant apart.", 11.5, "fg162", "start", "400", SANS)
    t(BX + PAD, BY + BH + 52,
      "So a finished answer carries no evidence of which route produced it. "
      "Write the name while you take the step.", 11.5, "fam162", "start", "600", SANS)

    if seed_collision:
        # deliberate labelPairs collision, to prove the gate live on THIS page
        t(BX + PAD, BY + BH + 27, "SEEDED COLLISION", 11.5, "fg162", "start", "400", SANS)

    o.append("</svg>")
    return "\n".join(o)


if __name__ == "__main__":
    s = build()
    print("chars", len(s), "ascii", all(ord(c) < 128 for c in s))
    print("<line elements:", s.count("<line"))
    print("<text elements:", s.count("<text"))
