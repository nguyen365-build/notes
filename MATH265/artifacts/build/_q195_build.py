"""Assemble the Q19.5 artifact.

Pattern from Q17.x-Q19.4 (carryover 27.12, 28.14, 29.12):
  - token + base prefix ONLY, sliced at the previous page's figure-classes
    comment and asserted to contain no body markup (21.6);
  - fresh classes, every invented name carrying the 195 suffix, checked against
    the inherited slice for collisions BOTH ways;
  - figure CSS emitted BEFORE the body, inside the SAME single style block;
  - style-block count DERIVED, not assumed;
  - zero TOP-LEVEL :root:not([data-theme="light"]) (21.7);
  - <meta charset="utf-8"> present, and 0 non-ASCII bytes;
  - dash entities and control characters blocked before the file reaches disk;
  - --sans and .tscroll are re-declared, because they live in Q19.4's EXTRA and
    therefore sit AFTER the slice boundary (29.8 found both).
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ART = os.path.dirname(HERE)
SRC = os.path.join(ART, "Q19.4-build-the-integrand.html")
OUT = os.path.join(ART, "Q19.5-which-factor-varies.html")

sys.path.insert(0, HERE)
import _q195_fig as F  # noqa: E402

REPORT = []


def note(k, v):
    REPORT.append((k, v))


# ------------------------------------------------------------------ 1. slice
src = open(SRC, encoding="utf-8").read()
BOUND = "/* ---- Q19.4 figure classes"
i_b = src.index(BOUND)
prefix = src[:i_b]
head_end = prefix.index("<style>")
head = prefix[:head_end]
base_css = prefix[head_end + len("<style>"):]

assert "<style>" in prefix and "</style>" not in prefix, "slice crosses a style boundary"
for tag in ("<header", "<main", "<section", "<table", "<figure", "<footer",
            "<h1", "<h2"):
    assert tag not in prefix, "style slice dragged body markup: %s" % tag
assert '<meta charset="utf-8">' in head, "charset meta missing from the inherited head"
note("head bytes", len(head))
note("base CSS bytes", len(base_css))

# THE TITLE COMES WITH THE SLICE, AND NO GATE HAS EVER CHECKED IT.  The Q19.4
# page - the slice source - carries "Rate In, Volume Out", which is Q19.3's
# title, so it published under the wrong name.  Rewrite it here and assert both
# directions: the new title is present, and the inherited one is gone.
TITLE = "Which Factor Varies"
m_t = re.search(r"<title>([^<]*)</title>", head)
assert m_t, "the inherited head has no <title> at all"
OLD_TITLE = m_t.group(1)
note("inherited <title> (WRONG, it is Q19.3's)", OLD_TITLE)
assert OLD_TITLE != TITLE, "the inherited title already matches; guard is stale"
head = head.replace("<title>%s</title>" % OLD_TITLE,
                    "<title>%s</title>" % TITLE, 1)
assert "<title>%s</title>" % TITLE in head, "the title rewrite did not apply"
assert OLD_TITLE not in head, "the inherited title survives somewhere in the head"
assert head.count("<title>") == 1, "more than one <title> in the head"
note("<title> rewritten to", TITLE)

m_disp = re.search(r"displayMath:\s*\[(.*?)\]\s*,", head, flags=re.S)
assert m_disp and "'$$','$$'" in m_disp.group(1).replace(" ", ""), \
    "displayMath is not $$"
note("displayMath delimiters", m_disp.group(1).strip())

# ------------------------------------------------------ 2. inherited surface
base_nc = re.sub(r"/\*.*?\*/", "", base_css, flags=re.S)
INHERITED = set(re.findall(r"\.([a-zA-Z][\w-]*)", base_nc))
TOKENS = set(t.split(":")[0].strip()
             for t in re.findall(r"--[a-zA-Z0-9_-]+\s*:", base_nc))
note("inherited class names", len(INHERITED))
note("inherited tokens defined", len(TOKENS))

bare = sorted(set(re.findall(r"(?m)^([a-z][a-z0-9]*)\s*(?:,[^{\n]*)?\{", base_nc)))
ACKNOWLEDGED = {
    "a": "links inherit the accent colour, wanted",
    "body": "the page ground and base type, wanted",
    "code": "the Moebius entry strings, wanted",
    "em": "italic emphasis, wanted",
    "figcaption": "caption type, wanted",
    "figure": "figure spacing, wanted",
    "footer": "footer rule and muted ink, wanted",
    "h1": "masthead type, wanted",
    "h2": "section heads, wanted",
    "h3": "sub-heads, wanted",
    "li": "list spacing, wanted",
    "p": "paragraph measure and spacing, wanted",
    "pre": "the decision tree block, wanted",
    "section": "section spacing, wanted",
    "strong": "bold weight, wanted",
    "table": "table reset, wanted",
    "th": "header cells, wanted",
    "td": "body cells, wanted",
    "ul": "list reset, wanted",
    "ol": "list reset, wanted",
}
unack = [b for b in bare if b not in ACKNOWLEDGED]
assert not unack, "unacknowledged inherited bare-element rules: %s" % unack
note("inherited bare-element rules reaching this body", len(bare))

# ------------------------------------------------------------- 3. the figures
fig1 = F.fig1()
fig2 = F.fig2()
assert F.contain_control(), "the containment guard does not reject an outside shape"
assert F.rectedge_control(), "the rect-edge guard does not report a seeded crossing"
assert F.tick_control(), "the tick guard's in-figure control did not run"
note("fig1 bytes", len(fig1))
note("fig2 bytes", len(fig2))
for line in F.LOG:
    note("  figure guard", line)

# --------------------------------------------------------------- 4. page CSS
FIG_CSS = """
/* ---- Q19.5 figure classes.  Emitted BEFORE the body, in this same block. */
.plotbg195{fill:var(--plot)}
/* the -soft tokens are 10-13 percent alpha, which vanishes on the plot ground.
   An area fill needs its own opacity off the SOLID token, so it works in both
   themes without adding a theme-conditional colour. */
.fill195{fill:var(--fam);fill-opacity:.26;stroke:var(--fam);stroke-width:1.6}
.naivebox195{fill:var(--los);fill-opacity:.13;stroke:var(--los);stroke-width:1.5;
  stroke-dasharray:5 4}
.force195{fill:none;stroke:var(--fam);stroke-width:2.4;stroke-linecap:round}
.avg195{stroke:var(--accent);stroke-width:1.4;stroke-dasharray:2 3}
/* ONE colour mapping across the whole page, checked by looking:
   teal --fam  = the truth, and the routes that generalise
   rust --los  = the wrong answer, and the shortcuts that break
   amber --accent = the factor that VARIES, and the quantity being measured
   A first draft used teal-for-chain and rust-for-spring in figure 1, which
   made teal mean "correct" in one figure and "chain" in the other. */
.slice195{fill:none;stroke:var(--ink3);stroke-width:1.3}
.bar195{fill:var(--accent-soft);stroke:var(--accent);stroke-width:1.2}
.rise195{stroke:var(--accent);stroke-width:1.6}
.arrowh195{fill:var(--accent)}
.tick195{fill:var(--plotlab);font:500 10px var(--mono);letter-spacing:.04em}
.lab{fill:var(--plotlab);font:500 11px var(--mono);letter-spacing:.05em}
.flab195{fill:var(--fam)}
.movl195{fill:var(--fam)}
.stayl195{fill:var(--los)}
.avgl195{fill:var(--accent)}
.varl195{fill:var(--accent)}
.areal195{fill:var(--ink)}
.gridl{stroke:var(--grid);stroke-width:1}
.axis{stroke:var(--ink3);stroke-width:1.4}
"""

EXTRA = """
/* ---- Q19.5 page classes.  Every invented name carries the 195 suffix.
   --sans and .tscroll are defined in Q19.4's EXTRA, which sits AFTER the slice
   boundary, so both have to be re-declared here or the page loses its sans
   stack and its wide tables stop scrolling (29.8). */
:root{--sans:"IBM Plex Sans",system-ui,-apple-system,"Segoe UI",sans-serif}
.lede195{font:500 clamp(15px,1.6vw,17.5px)/1.62 var(--sans);color:var(--ink2);
  max-width:62ch;margin:14px 0 0}
.ansbar195{display:grid;gap:1px;background:var(--line);border:1px solid var(--line);
  grid-template-columns:repeat(auto-fit,minmax(min(232px,100%),1fr))}
.ac195{background:var(--surface2);padding:16px 18px;display:flex;
  flex-direction:column;gap:8px}
.al195{font:600 10px var(--mono);letter-spacing:.13em;color:var(--accent)}
.av195{font:600 18px/1.4 var(--sans);color:var(--ink)}
.small195{font:400 13.5px/1.58 var(--sans);color:var(--ink2)}
.steps195{display:grid;gap:1px;background:var(--line);border:1px solid var(--line);
  margin:18px 0}
.sp195{background:var(--surface);padding:13px 16px;display:grid;
  grid-template-columns:30px minmax(0,1fr);gap:12px;align-items:baseline}
.sp195 > span:nth-child(2){grid-column:2}
.sn195{grid-column:1;font:600 12px var(--mono);color:var(--accent);letter-spacing:.06em}
.box195{border-left:3px solid var(--accent);background:var(--sunk);
  padding:6px 20px;margin:20px 0;overflow-x:auto}
.note195,.warn195{border-left:3px solid var(--fam);background:var(--sunk);
  padding:14px 18px;margin:18px 0;font:400 14.5px/1.62 var(--sans);color:var(--ink2)}
.warn195{border-left-color:var(--los)}
.tscroll{overflow-x:auto;margin:16px 0;border:1px solid var(--line)}
.tab195{width:100%;min-width:940px;border-collapse:collapse;
  font:400 13.5px/1.5 var(--sans)}
.tab195 th{font:600 10px var(--mono);letter-spacing:.11em;color:var(--ink3);
  text-align:left;padding:9px 12px;border-bottom:1px solid var(--line)}
.tab195 td{padding:9px 12px;border-bottom:1px solid var(--line-soft);
  vertical-align:top}
.tab195 tbody tr:last-child td{border-bottom:none}
.num195{font-variant-numeric:tabular-nums;font-family:var(--mono);
  font-size:12.5px;white-space:nowrap}
/* semantic colours are their own rules, scoped both ways, so a table cell keeps
   its meaning without borrowing a block class (28.10) */
.tab195 td.ok195,.ok195{color:var(--fam)}
.tab195 td.no195,.no195{color:var(--los)}
.tab195 td.mov195,.mov195{color:var(--fam)}
.tab195 td.stay195,.stay195{color:var(--los)}
.tab195 td.var195,.var195{color:var(--accent)}
.tab195 tr.hot195 td{background:var(--los-soft)}
.tab195 tr.hid195 td{background:var(--accent-soft)}
.tree195{font:500 12px/1.62 var(--mono);color:var(--ink2);background:var(--sunk);
  border:1px solid var(--line);padding:16px 18px;overflow-x:auto;margin:16px 0}
/* carryover 7: inline MathJax must never resolve to a centred block, and the
   unit has to sit INSIDE the math or it rides above the baseline (29.9) */
mjx-container:not([display="true"]){display:inline-block!important;
  margin:0!important;text-align:left!important;vertical-align:-0.15em}
.tab195 td mjx-container,.tab195 th mjx-container{color:inherit}
.tab195 td mjx-container svg{fill:currentColor}
@media (max-width:760px){.tab195{min-width:760px}}
"""

# ------------------------------------------- 5. collision guard, both ways
# 20.7: a guard that scans a stylesheet must STRIP CSS COMMENTS first, or it
# reads its own documentation.  A bait found exactly that here - the EXTRA
# comment names ".tscroll", so deleting the .tscroll RULE left the name still
# "defined" as far as the guard could tell, and the orphan check went quiet.
PAGE_CSS = FIG_CSS + EXTRA
PAGE_CSS_NC = re.sub(r"/\*.*?\*/", "", PAGE_CSS, flags=re.S)
invented = sorted(set(re.findall(r"\.([a-zA-Z][\w-]*)", PAGE_CSS_NC)))
DELIBERATE = {"lab", "gridl", "axis", "tscroll"}
collide = [c for c in invented if c in INHERITED and c not in DELIBERATE]
assert not collide, "invented names collide with the inherited slice: %s" % collide
for d in sorted(DELIBERATE):
    assert d in invented, "declared override %r is not actually defined" % d
note("invented class names", len(invented))
note("deliberate overrides", "%d %s" % (len(DELIBERATE), sorted(DELIBERATE)))

used_tokens = set(re.findall(r"var\((--[\w-]+)\)", PAGE_CSS_NC))
defined_here = set(t.split(":")[0].strip()
                   for t in re.findall(r"--[\w-]+\s*:", PAGE_CSS_NC))
missing = sorted(used_tokens - TOKENS - defined_here)
assert not missing, "undefined tokens: %s" % missing
note("tokens referenced", len(used_tokens))
# the token guard must be shown to bite (29.8's --sans finding)
assert "--sans" not in TOKENS, \
    "--sans is now in the slice; the re-declaration comment is stale"
note("token guard live", "--sans absent from the slice, re-declared here")

# ------------------------------------------------------------------ 6. body
body = open(os.path.join(HERE, "_q195_body.html"), encoding="utf-8").read()
assert "FIG1" in body and "FIG2" in body
body = body.replace("FIG1", fig1).replace("FIG2", fig2)

body_classes = set()
for m in re.finditer(r'class="([^"]+)"', body):
    for c in m.group(1).split():
        body_classes.add(c)
have = INHERITED | set(invented)
orphans = sorted(c for c in body_classes if c not in have)
assert not orphans, "body classes with no rule anywhere: %s" % orphans
note("distinct classes used by the body", len(body_classes))

body_nosvg = re.sub(r"<svg.*?</svg>", " ", body, flags=re.S)
assert (chr(92) + "[") not in body_nosvg, "bracket display math in the body"
assert (chr(92) + "(") not in body_nosvg, "bracket inline math in the body"
assert body_nosvg.count("$$") % 2 == 0, "unbalanced $$ in the body"
note("$$ pairs in the body", body_nosvg.count("$$") // 2)

n_tables = body.count("<table")
n_scroll = body.count('class="tscroll"')
assert n_tables == n_scroll, "%d tables but %d tscroll wrappers" % (n_tables, n_scroll)
note("tables (build's own count)", n_tables)

# ------------------------------------------------------------- 7. assemble
page = head + "<style>" + base_css + FIG_CSS + EXTRA + "</style>\n" + body

n_open = page.count("<style")
n_close = page.count("</style>")
assert n_open == n_close == 1, "style blocks: %d open, %d close" % (n_open, n_close)
assert page.rindex("</style>") < page.index("<header"), \
    "a style block sits inside the body"
note("style blocks (derived)", n_open)

css_all = page[page.index("<style>") + 7:page.index("</style>")]
css_scan = re.sub(r"/\*.*?\*/", "", css_all, flags=re.S)
depth = 0
top_level_hits = 0
guarded_hits = 0
NEEDLE = ':root:not([data-theme="light"])'
i = 0
while i < len(css_scan):
    if css_scan.startswith(NEEDLE, i):
        if depth == 0:
            top_level_hits += 1
        else:
            guarded_hits += 1
    ch = css_scan[i]
    if ch == "{":
        depth += 1
    elif ch == "}":
        depth -= 1
    i += 1
assert top_level_hits == 0, "%d top-level :root:not([data-theme]) rules" % top_level_hits
assert guarded_hits >= 1, "the guarded dark block is missing entirely"
note("top-level :root:not(light)", top_level_hits)
note("guarded (inside @media) :root:not(light)", guarded_hits)

SPELL = [chr(0x2014), chr(0x2013), "&" + "mdash;", "&" + "ndash;", "&#8212;",
         "&#8211;", "&#x2014;", "&#x2013;", "&#X2014;", "&#X2013;", chr(0x2015)]
hits = {s: page.count(s) for s in SPELL if page.count(s)}
assert not hits, "dash spellings present: %s" % hits
ctrl = [hex(ord(c)) for c in page if ord(c) < 32 and c not in "\n\r\t"]
assert not ctrl, "control characters: %s" % ctrl[:6]
nonascii = [c for c in page if ord(c) > 126]
assert not nonascii, "non-ASCII bytes: %s" % sorted(set(nonascii))[:8]
note("non-ASCII bytes", len(nonascii))

ALLOW = {"cdnjs.cloudflare.com", "fonts.googleapis.com", "fonts.gstatic.com"}
hosts = set(re.findall(r"https://([A-Za-z0-9.-]+)", page))
assert hosts <= ALLOW, "hosts outside the CSP allowlist: %s" % sorted(hosts - ALLOW)
note("external hosts", ",".join(sorted(hosts)))

assert page.count('class="figbox"') == 2, "figbox must wrap each svg"
assert page.count('class="lab') >= 10, "labels must carry class lab"
note("figbox wrappers", page.count('class="figbox"'))
note("text.lab elements", page.count('class="lab'))

open(OUT, "w", encoding="utf-8", newline="\n").write(page)
note("OUTPUT", OUT)
note("bytes", len(page.encode("utf-8")))

for k, v in REPORT:
    print("%-46s %s" % (k, v))
print("BUILD OK")
