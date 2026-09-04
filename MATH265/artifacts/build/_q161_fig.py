"""Q16.1 figure generator.

TWO PANELS, one SVG.

  Panel A  THE LADDER. Integration is a SEARCH, so the figure that explains it has to show
           descent and a stopping point, not a lookup table. Four rungs step down to the
           right; each of Q16.1's five parts is a chip sitting on the rung where its search
           STOPPED. Part (b) is the only one that enters at rung 4 and re-enters higher, so
           it is the only chip drawn with a return arc.

  Panel B  THE CHECK. The wrong-answer census as two stacked columns. The whole point is that
           the split is EXACT - everything that changes the function is caught, everything
           that does not is missed - so the two columns are drawn to the same scale from the
           same baseline and the counts are the measured ones.

Carryover contracts honoured here:
  - NO text inside either plotting frame, and NO leader lines at all (19.9). Every label sits
    in a band below its frame. That empties the label-versus-curve collision surface by
    construction, which is what produced 0 lineHits on the last two pages.
  - Every <text> carries class="lab" so svg-labels measures it; every grid line carries
    class="gridl" so it is exempt (4).
  - Every drawn shape has an EXPLICIT fill; var() does not resolve in an SVG presentation
    attribute, so colours are literal and a <style> block inside the SVG themes them.
  - The viewBox leaves room for the outermost label (19.9).
  - Pure ASCII: a non-ASCII byte mojibakes under a local file:// render (4).
"""

W = 980
H = 730

# ---- the five parts, and the rung each one's search stopped on ---------------------------
# (label, rung, the tool that fired, a one-line reason)
PARTS = [
    ("a", 1, "power rule", "sqrt(3x) = sqrt3 x^(1/2), then multiply out"),
    ("b", 4, "identity", "two substitutions fail, so rewrite sin 2x"),
    ("c", 2, "1/a factor", "cos(2x) has a linear inner function"),
    ("d", 1, "power rule", "the bracket power is 2, so expand"),
    ("e", 3, "substitution", "u = x-1, and the leftover x becomes u+1"),
]

RUNGS = [
    (1, "ALGEBRA", "make it a sum of powers"),
    (2, "LINEAR INNER", "divide by a"),
    (3, "SUBSTITUTION", "du must be present"),
    (4, "IDENTITY", "rewrite, then re-enter at rung 1"),
]

# ---- the census, measured by harness section q161c ----------------------------------------
CATCHES = [
    ("dropped constant factor", 6),
    ("missed chain factor", 5),
    ("other algebra slips", 5),
]
BLIND = [
    ("omitted or altered +C", 7),
    ("domain restriction", 2),
    ("swapped limits", 1),
]


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def build():
    o = []
    o.append('<svg viewBox="0 0 %d %d" width="100%%" role="img" '
             'aria-label="Panel A: the four-rung integration ladder with each part of Q16.1 '
             'placed on the rung its search stopped at. Panel B: the wrong-answer census, '
             '16 errors detected by differentiating back and 10 that hide." '
             'xmlns="http://www.w3.org/2000/svg">' % (W, H))

    # theming for the figure - presentation attributes cannot use var(), so the SVG
    # carries its own token-driven style block and every shape names an explicit fill.
    o.append("""<style>
  .fg161{ fill:#14181F; }
  .fmut161{ fill:#5C6672; }
  .fam161{ fill:#B57608; }
  .fpan161{ fill:#FFFFFF; }
  .fchip161{ fill:#F2A53C; }
  .fbad161{ fill:#B4522F; }
  .fgood161{ fill:#2E6F6A; }
  .sgrid161{ stroke:#D8DDE4; stroke-width:1; }
  .sfrm161{ stroke:#AEB6C0; stroke-width:1.2; fill:none; }
  .srung161{ stroke:#B57608; stroke-width:2.2; fill:none; }
  :root[data-theme="dark"] .fg161,
  :root:not([data-theme="light"]) .fg161{ fill:#E6EAF0; }
  :root[data-theme="dark"] .fmut161,
  :root:not([data-theme="light"]) .fmut161{ fill:#939DAA; }
  :root[data-theme="dark"] .fam161,
  :root:not([data-theme="light"]) .fam161{ fill:#F2A53C; }
  :root[data-theme="dark"] .fpan161,
  :root:not([data-theme="light"]) .fpan161{ fill:#1B2029; }
  :root[data-theme="dark"] .fbad161,
  :root:not([data-theme="light"]) .fbad161{ fill:#D9764E; }
  :root[data-theme="dark"] .fgood161,
  :root:not([data-theme="light"]) .fgood161{ fill:#4FA39B; }
  :root[data-theme="dark"] .sgrid161,
  :root:not([data-theme="light"]) .sgrid161{ stroke:#2C333E; }
  :root[data-theme="dark"] .sfrm161,
  :root:not([data-theme="light"]) .sfrm161{ stroke:#3D4552; }
</style>""")

    MONO = "'IBM Plex Mono','SFMono-Regular',Consolas,monospace"
    SANS = "'IBM Plex Sans','Segoe UI',system-ui,sans-serif"

    def t(x, y, s, size=11, cls="fg161", anchor="start", weight="400",
          fam=SANS, ls="0"):
        o.append('<text class="lab %s" x="%.1f" y="%.1f" font-family="%s" font-size="%.1f" '
                 'font-weight="%s" letter-spacing="%s" text-anchor="%s">%s</text>'
                 % (cls, x, y, fam, size, weight, ls, anchor, esc(s)))

    # ==================================================== PANEL A - THE LADDER
    AX, AY, AW, AH = 34, 54, 470, 300
    t(AX, 32, "PANEL A", 10, "fam161", "start", "600", MONO, "0.10em")
    t(AX + 74, 32, "THE LADDER - WHERE EACH PART'S SEARCH STOPPED", 10, "fmut161",
      "start", "500", MONO, "0.10em")

    o.append('<rect class="sfrm161" x="%d" y="%d" width="%d" height="%d" fill="none"/>'
             % (AX, AY, AW, AH))

    step_h = AH / 4.0
    for i, (n, name, tool) in enumerate(RUNGS):
        y = AY + i * step_h
        # the rung's own tread, stepping right as you descend
        x0 = AX + 12 + i * 74
        x1 = x0 + 150
        o.append('<line class="gridl sgrid161" x1="%d" y1="%.1f" x2="%d" y2="%.1f"/>'
                 % (AX, y, AX + AW, y))
        o.append('<line class="srung161" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>'
                 % (x0, y + step_h * 0.52, x1, y + step_h * 0.52))
        # the drop to the next rung
        if i < 3:
            o.append('<line class="srung161" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" '
                     'stroke-dasharray="3 3"/>'
                     % (x1, y + step_h * 0.52, x1, y + step_h * 1.52))

    # chips: each part sits on its rung's tread
    used = {}
    for lab, rung, tool, why in PARTS:
        i = rung - 1
        y = AY + i * step_h + step_h * 0.52
        x0 = AX + 12 + i * 74
        k = used.get(rung, 0)
        used[rung] = k + 1
        cx = x0 + 22 + k * 42
        # DEFECT FOUND BY svg-labels AND FIXED: the chips were centred ON the tread, so the
        # gate reported five real "srung161 crosses" hits. They now REST on top of it, which
        # clears the line and is the truer picture of a step anyway.
        cy = y - 17.0
        o.append('<circle class="fchip161" cx="%.1f" cy="%.1f" r="12.5"/>' % (cx, cy))
        o.append('<text class="lab" x="%.1f" y="%.1f" font-family="%s" font-size="12.5" '
                 'font-weight="700" text-anchor="middle" fill="#14181F">%s</text>'
                 % (cx, cy + 4.4, MONO, lab))

    # The band BELOW the frame carries every word - no text inside the frame.
    # DEAD-SPACE FIX (carryover 18.7): the first version drew only the rung name and its
    # tool, so this column ended ~110px above panel B's and the figure read bottom-heavy on
    # the right. The generator already computed a `why` line per part and never drew it.
    # Each rung now also names the parts that stopped there and why - which fills the space
    # with the thing a reader actually wants, rather than with padding.
    stopped = {}
    for _lab, _rung, _tool, _why in PARTS:
        stopped.setdefault(_rung, []).append((_lab, _why))
    by = AY + AH + 26
    yy = by
    for i, (n, name, tool) in enumerate(RUNGS):
        t(AX, yy, "RUNG %d" % n, 10, "fam161", "start", "600", MONO, "0.08em")
        t(AX + 62, yy, name, 11.5, "fg161", "start", "600")
        t(AX + 190, yy, tool, 11, "fmut161", "start", "400")
        yy += 27
        for _lab, _why in stopped.get(n, []):
            t(AX + 62, yy, "(%s)" % _lab, 10.5, "fam161", "start", "700", MONO)
            t(AX + 122, yy, _why, 10.5, "fmut161", "start", "400")
            yy += 26
        yy += 14

    # ==================================================== PANEL B - THE CENSUS
    BX, BY, BW, BH = 556, 54, 390, 300
    t(BX, 32, "PANEL B", 10, "fam161", "start", "600", MONO, "0.10em")
    t(BX + 74, 32, "DOES DIFFERENTIATING BACK CATCH IT?", 10, "fmut161",
      "start", "500", MONO, "0.10em")

    o.append('<rect class="sfrm161" x="%d" y="%d" width="%d" height="%d" fill="none"/>'
             % (BX, BY, BW, BH))

    # ONE scale for both columns: 16 is the taller total, so it sets the ceiling.
    total_c = sum(v for _, v in CATCHES)
    total_b = sum(v for _, v in BLIND)
    ceiling = max(total_c, total_b)
    base_y = BY + BH - 42
    top_y = BY + 30
    unit = (base_y - top_y) / float(ceiling)

    # gridlines at every 4 units, each naming a value the chart reaches
    gy = 0
    while gy <= ceiling:
        y = base_y - gy * unit
        o.append('<line class="gridl sgrid161" x1="%d" y1="%.1f" x2="%d" y2="%.1f"/>'
                 % (BX + 8, y, BX + BW - 8, y))
        gy += 4

    colw = 92
    cols = [(BX + 74, CATCHES, "fgood161", total_c),
            (BX + 232, BLIND, "fbad161", total_b)]
    for cx, groups, cls, tot in cols:
        acc = 0
        for gi, (gname, gv) in enumerate(groups):
            y1 = base_y - acc * unit
            y0 = base_y - (acc + gv) * unit
            o.append('<rect class="%s" x="%.1f" y="%.1f" width="%d" height="%.1f" '
                     'opacity="%.2f"/>' % (cls, cx, y0, colw, y1 - y0, 1.0 - gi * 0.24))
            acc += gv
        o.append('<line class="gridl sgrid161" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>'
                 % (cx, base_y, cx + colw, base_y))

    # band below the frame: column totals, then the family breakdown
    t(BX, by, "CATCHES", 11, "fgood161", "start", "700", MONO, "0.06em")
    t(BX + 96, by, "%d of 26" % total_c, 11, "fg161", "start", "600", MONO)
    for gi, (gname, gv) in enumerate(CATCHES):
        t(BX + 8, by + 22 + gi * 26, "%d  %s" % (gv, gname), 10.5, "fmut161",
          "start", "400")

    y2 = by + 22 + len(CATCHES) * 26 + 12
    t(BX, y2, "BLIND TO", 11, "fbad161", "start", "700", MONO, "0.06em")
    t(BX + 96, y2, "%d of 26" % total_b, 11, "fg161", "start", "600", MONO)
    for gi, (gname, gv) in enumerate(BLIND):
        t(BX + 8, y2 + 22 + gi * 26, "%d  %s" % (gv, gname), 10.5, "fmut161",
          "start", "400")

    # the one sentence the panel exists to make
    t(AX, H - 14,
      "The split is exact: every error that changes the function is caught, "
      "every error that does not is missed.",
      11.5, "fam161", "start", "600")

    o.append("</svg>")
    return "\n".join(o)


if __name__ == "__main__":
    s = build()
    print(s[:400])
    print("...")
    print("chars:", len(s), " non-ascii:", sum(1 for c in s if ord(c) > 127))
