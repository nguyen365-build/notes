"""Assemble the Q10.1 artifact from the series head + stylesheet + this page's body."""
import io, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "Q9.1-perpendicular-tangent.html")
OUT = os.path.join(HERE, "Q10.1-implicit-differentiation.html")

src = io.open(SRC, encoding="utf-8").read().split("\n")
head = "\n".join(src[0:12])          # title + fonts + MathJax config + script
style = "\n".join(src[12:299])       # <style> ... up to but not including </style>
assert style.lstrip().startswith("<style>"), style[:40]
assert "</style>" not in style
assert 'mjx-container:not([display="true"])' in style, "inline-MathJax fix missing"

# ---- this page's title -----------------------------------------------------
head = head.replace("<title>The Perpendicular Tangent</title>",
                    "<title>The y-prime Ledger</title>")
assert "The y-prime Ledger" in head

# ---- what the five accent hues mean on THIS page ---------------------------
old_legend = re.search(r"/\* ===== ops console.*?\*/", style, re.S)
assert old_legend, "legend comment not found"
new_legend = """/* ===== ops console, MATH 265 series ========================================
   Palette and type are the series system, unchanged since Q1.1.  What is
   specific to THIS page is what the five accent hues MEAN.  Q9.1 was a
   four-station pipeline.  Q10.1 is a LEDGER: the equation splits into terms,
   each term splits into pieces, and every piece either carries a y' or it
   does not.  That single binary is the whole subject, so it owns the two
   loudest hues and the page's signature table is built on it.

     CARRIES A y'  (the chain factor you must not drop)   --rul   amber
     NO y'         (the ordinary derivative half)         --chn   slate
     WHERE MARKS DIE                                      --los   terracotta
     THE VARIATION families                               --fam   teal
     NUMERICS: gates, arms, tolerances, controls          --num   mauve
   ========================================================================= */"""
style = style[:old_legend.start()] + new_legend + style[old_legend.end():]

# ---- rules this page adds --------------------------------------------------
EXTRA = """
/* --- the term ledger: the y' binary, encoded as column colour ------------ */
th.ypy,td.ypy{background:var(--rul-soft);border-left:1px solid var(--rul-line)}
th.ypy{color:var(--rul)}
td.ypy{color:var(--ink);font-weight:500}
th.ypn,td.ypn{background:var(--chn-soft)}
th.ypn{color:var(--chn)}
/* --- the step board -------------------------------------------------------
   Each cell here carries a WHOLE equation, which the series 4-across .pipe
   cannot hold: at 1080px the MathJax SVGs overflowed their cells and
   overlapped the neighbour.  lint.mjs passed it clean; only the screenshot
   showed it.  Two across, dividers painted by the grid gap so the count can
   drop to one on a narrow viewport without leaving a stray border, and each
   equation scrolls inside its own cell as a backstop. ------------------- */
.pipe.steps{grid-template-columns:repeat(auto-fit,minmax(430px,1fr));gap:1px;background:var(--line)}
.pipe.steps > div{border-right:0;background:var(--surface)}
.pipe.steps > div.hot{background:var(--los-soft)}
.pipe.steps .sv{display:block;overflow-x:auto;overflow-y:hidden;padding-bottom:2px}
/* --- six values, so three across reads as two even rows rather than 4+2 --- */
.vgrid{grid-template-columns:repeat(auto-fit,minmax(290px,1fr))}
/* --- figure caption ------------------------------------------------------ */
.cap{margin:12px 0 0;font-size:13px;color:var(--ink3);max-width:74ch}
"""
style = style + EXTRA + "\n</style>"

# ---- body, with the computed figure spliced in -----------------------------
body = io.open(os.path.join(HERE, "_q101_body.html"), encoding="utf-8").read()
svg = io.open(os.path.join(HERE, "_q101_fig.svg"), encoding="utf-8").read()
assert "FIGURE_SVG" in body
body = body.replace("FIGURE_SVG", svg)

page = head + "\n" + style + "\n\n" + body + "\n"

# ---- pre-flight checks -----------------------------------------------------
bad = [hex(ord(c)) for c in page if ord(c) < 32 and c not in "\n\r\t"]
assert not bad, "control characters: %s" % bad
assert chr(0x2014) not in page and chr(0x2013) not in page, "raw dash character in page"
for sp in ("&mdash;", "&ndash;", "&#8212;", "&#8211;", "&#x2014;", "&#x2013;"):
    assert sp not in page, "dash entity in page: %s" % sp
for tag in ("<!doctype", "<html", "<head>", "<body>"):
    assert tag not in page.lower(), "publish skeleton tag present: %s" % tag
# the svg must carry the gate's markup contract
assert 'class="figbox"' in page or "figbox" in page
assert page.count("<svg") == 1
assert 'class="gridl"' in page, "grid lines must be classed or the label gate samples them"
assert 'class="tl lab"' in page and 'class="al lab"' in page, "labels must carry .lab"
# theme contract: no colour defined ONLY inside a media/[data-theme] block
assert ':root:not([data-theme="light"])' in page
assert ':root[data-theme="dark"]' in page
assert "background-color:var(--ground)" in page, "body must paint an explicit ground"

io.open(OUT, "w", encoding="utf-8", newline="\n").write(page)
print("wrote", OUT)
print("bytes", len(page.encode("utf-8")))
print("non-ascii chars:", sorted({c for c in page if ord(c) > 126}))
