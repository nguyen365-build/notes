"""Assemble the Q19.4 artifact.

Pattern from Q17.x-Q19.3 (carryover 27.12, 28.14):
  - token + base prefix ONLY, sliced at the previous page's page-classes comment
    and asserted to contain no body markup (21.6);
  - fresh classes, every invented name carrying the 194 suffix, checked against
    the inherited slice for collisions BOTH ways (present-but-unstyled as well);
  - figure CSS emitted BEFORE the body, inside the SAME single style block;
  - style-block count DERIVED, not assumed;
  - zero TOP-LEVEL :root:not([data-theme="light"]) (21.7);
  - <meta charset="utf-8"> present, and 0 non-ASCII bytes;
  - dash entities blocked before the file reaches disk.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ART = os.path.dirname(HERE)
SRC = os.path.join(ART, "Q19.3-rate-in-volume-out.html")
OUT = os.path.join(ART, "Q19.4-build-the-integrand.html")

sys.path.insert(0, HERE)
import _q194_fig as F  # noqa: E402

REPORT = []


def note(k, v):
    REPORT.append((k, v))


# ------------------------------------------------------------------ 1. slice
src = open(SRC, encoding="utf-8").read()
BOUND = "/* ---- Q19.3 page classes"
i_b = src.index(BOUND)
prefix = src[:i_b]
head_end = prefix.index("<style>")
head = prefix[:head_end]
base_css = prefix[head_end + len("<style>"):]

assert "<style>" in prefix and "</style>" not in prefix, "slice crosses a style boundary"
# 21.6: the slice must not drag body markup
for tag in ("<header", "<main", "<section", "<table", "<figure", "<footer", "<h1", "<h2"):
    assert tag not in prefix, "style slice dragged body markup: %s" % tag
assert '<meta charset="utf-8">' in head, "charset meta missing from the inherited head"
note("head bytes", len(head))
note("base CSS bytes", len(base_css))

# the head's MathJax config: parse the delimiters rather than assuming them
m_disp = re.search(r"displayMath:\s*\[(.*?)\]\s*,", head, flags=re.S)
assert m_disp and "'$$','$$'" in m_disp.group(1).replace(" ", ""), "displayMath is not $$"
note("displayMath delimiters", m_disp.group(1).strip())

# ------------------------------------------------------ 2. inherited surface
base_nc = re.sub(r"/\*.*?\*/", "", base_css, flags=re.S)
INHERITED = set(re.findall(r"\.([a-zA-Z][\w-]*)", base_nc))
TOKENS = set(re.findall(r"--[a-zA-Z0-9_-]+\s*:", base_nc))
TOKENS = set(t.split(":")[0].strip() for t in TOKENS)
note("inherited class names", len(INHERITED))
note("inherited tokens defined", len(TOKENS))

# 25.6 guard 4b: inherited BARE ELEMENT rules that reach this body
bare = sorted(set(re.findall(r"(?m)^([a-z][a-z0-9]*)\s*(?:,[^{\n]*)?\{", base_nc)))
ACKNOWLEDGED = {
    "a": "links inherit the accent colour, wanted",
    "body": "the page ground and base type, wanted",
    "code": "the Moebius entry string, wanted",
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
note("fig1 bytes", len(fig1))
note("fig2 bytes", len(fig2))
note("containment", "; ".join(F.CONTAIN_LOG))
assert F.contain_control(), "the containment guard does not reject an outside box"

# --------------------------------------------------------------- 4. page CSS
FIG_CSS = """
/* ---- Q19.4 figure classes.  Emitted BEFORE the body, in this same block. */
.plotbg194{fill:var(--plot)}
.ground194{stroke:var(--ink3);stroke-width:2}
.chain194{stroke:var(--ink2);stroke-width:5;stroke-linecap:round}
.chainhi194{stroke:var(--fam);stroke-width:5;stroke-linecap:round}
.chainlo194{stroke:var(--los);stroke-width:5;stroke-linecap:round}
.knot194{fill:var(--ink3)}
.knothi194{fill:var(--fam)}
.rise194{stroke:var(--accent);stroke-width:1.6}
.tie194{stroke:var(--accent);stroke-width:1;stroke-dasharray:3 3}
.arrowh194{fill:var(--accent)}
.slice194{fill:var(--accent);stroke:var(--accent);stroke-width:1}
.fill194{fill:var(--fam-soft);stroke:none}
.rise2194{fill:none;stroke:var(--fam);stroke-width:2.2;stroke-linejoin:round}
.tick194{fill:var(--plotlab);font:500 10px var(--mono);letter-spacing:.04em}
.lab{fill:var(--plotlab);font:500 11px var(--mono);letter-spacing:.05em}
.movl194{fill:var(--fam)}
.stayl194{fill:var(--los)}
.areal194{fill:var(--ink)}
.gridl{stroke:var(--grid);stroke-width:1}
.axis{stroke:var(--ink3);stroke-width:1.4}
"""

EXTRA = """
/* ---- Q19.4 page classes.  Every invented name carries the 194 suffix.
   The series defines --mono but has never defined a sans token - it spells the
   stack out in 20-odd rules instead.  Defining it here rather than referencing
   an undefined token is the same fix Q11.1 applied to --mono, and the build's
   token guard is what caught it. */
:root{--sans:"IBM Plex Sans",system-ui,-apple-system,"Segoe UI",sans-serif}
.lede194{font:500 clamp(15px,1.6vw,17.5px)/1.62 var(--sans);color:var(--ink2);
  max-width:62ch;margin:14px 0 0}
.ansbar194{display:grid;gap:1px;background:var(--line);border:1px solid var(--line);
  grid-template-columns:repeat(auto-fit,minmax(min(260px,100%),1fr))}
.ac194{background:var(--surface2);padding:16px 18px;display:flex;flex-direction:column;gap:8px}
.al194{font:600 10px var(--mono);letter-spacing:.13em;color:var(--accent)}
.av194{font:600 18px/1.4 var(--sans);color:var(--ink)}
.small194{font:400 13.5px/1.55 var(--sans);color:var(--ink2)}
.steps194{display:grid;gap:1px;background:var(--line);border:1px solid var(--line);margin:18px 0}
.sp194{background:var(--surface);padding:13px 16px;display:grid;
  grid-template-columns:30px minmax(0,1fr);gap:12px;align-items:baseline}
.sp194 > span:nth-child(2){grid-column:2}
.sn194{grid-column:1;font:600 12px var(--mono);color:var(--accent);letter-spacing:.06em}
.box194{border-left:3px solid var(--accent);background:var(--sunk);
  padding:6px 20px;margin:20px 0;overflow-x:auto}
.note194,.warn194{border-left:3px solid var(--fam);background:var(--sunk);
  padding:14px 18px;margin:18px 0;font:400 14.5px/1.62 var(--sans);color:var(--ink2)}
.warn194{border-left-color:var(--los)}
/* .tscroll is the table-fit hook AND the thing that makes a wide table scroll
   inside its own container.  The orphan guard caught it having no rule at all,
   which is the defect Q10.2 shipped. */
.tscroll{overflow-x:auto;margin:16px 0;border:1px solid var(--line)}
.tab194{width:100%;min-width:1020px;border-collapse:collapse;font:400 13.5px/1.5 var(--sans)}
.tab194 th{font:600 10px var(--mono);letter-spacing:.11em;color:var(--ink3);
  text-align:left;padding:9px 12px;border-bottom:1px solid var(--line)}
.tab194 td{padding:9px 12px;border-bottom:1px solid var(--line-soft);vertical-align:top}
.tab194 tbody tr:last-child td{border-bottom:none}
.num194{font-variant-numeric:tabular-nums;font-family:var(--mono);font-size:12.5px;
  white-space:nowrap}
/* semantic colours are their own rules, scoped both ways, never a block class
   borrowed for a cell (28.10) */
.tab194 td.ok194,.ok194{color:var(--fam)}
.tab194 td.no194,.no194{color:var(--los)}
.tab194 td.mov194,.mov194{color:var(--fam)}
.tab194 td.stay194,.stay194{color:var(--los)}
.tab194 tr.hot194 td{background:var(--los-soft)}
.tab194 tr.hid194 td{background:var(--accent-soft)}
.tree194{font:500 12px/1.62 var(--mono);color:var(--ink2);background:var(--sunk);
  border:1px solid var(--line);padding:16px 18px;overflow-x:auto;margin:16px 0}
/* 7: inline MathJax must never resolve to a centred block */
mjx-container:not([display="true"]){display:inline-block!important;margin:0!important;
  text-align:left!important;vertical-align:-0.15em}
.tab194 td mjx-container,.tab194 th mjx-container{color:inherit}
.tab194 td mjx-container svg{fill:currentColor}
@media (max-width:760px){.tab194{min-width:760px}}
"""

# ------------------------------------------- 5. collision guard, both ways
invented = sorted(set(re.findall(r"\.([a-zA-Z][\w-]*)", FIG_CSS + EXTRA)))
DELIBERATE = {"lab", "gridl", "axis"}          # gate hooks the series shares
collide = [c for c in invented if c in INHERITED and c not in DELIBERATE]
assert not collide, "invented names collide with the inherited slice: %s" % collide
note("invented class names", len(invented))
note("deliberate overrides", len(DELIBERATE))
for d in sorted(DELIBERATE):
    assert d in invented, "declared override %r is not actually defined" % d

# token guard: every var() the page leans on must exist in the slice or here
used_tokens = set(re.findall(r"var\((--[\w-]+)\)", FIG_CSS + EXTRA))
defined_here = set(t.split(":")[0].strip()
                   for t in re.findall(r"--[\w-]+\s*:", FIG_CSS + EXTRA))
missing = sorted(used_tokens - TOKENS - defined_here)
assert not missing, "undefined tokens: %s" % missing
note("tokens referenced", len(used_tokens))

# ------------------------------------------------------------------ 6. body
body = open(os.path.join(HERE, "_q194_body.html"), encoding="utf-8").read()
assert "FIG1" in body and "FIG2" in body
body = body.replace("FIG1", fig1).replace("FIG2", fig2)

# orphan-class guard: every class the BODY uses must have a rule somewhere
body_classes = set()
for m in re.finditer(r'class="([^"]+)"', body):
    for c in m.group(1).split():
        body_classes.add(c)
have = INHERITED | set(invented)
orphans = sorted(c for c in body_classes if c not in have)
assert not orphans, "body classes with no rule anywhere: %s" % orphans
note("distinct classes used by the body", len(body_classes))

# ONE inline-math delimiter in the BODY (the head configures both, the body
# uses only $...$).  Bracket display math ships as visible raw LaTeX.
body_nosvg = re.sub(r"<svg.*?</svg>", " ", body, flags=re.S)
assert "\\[" not in body_nosvg, "bracket display math in the body"
assert "\\(" not in body_nosvg, "bracket inline math in the body"
assert body_nosvg.count("$$") % 2 == 0, "unbalanced $$ in the body"
note("$$ pairs in the body", body_nosvg.count("$$") // 2)

# table count, cross-checked against table-fit later
n_tables = body.count("<table")
n_scroll = body.count('class="tscroll"')
assert n_tables == n_scroll, "%d tables but %d tscroll wrappers" % (n_tables, n_scroll)
note("tables (build's own count)", n_tables)

# ------------------------------------------------------------- 7. assemble
page = head + "<style>" + base_css + FIG_CSS + EXTRA + "</style>\n" + body

# style-block count, DERIVED
n_open = page.count("<style")
n_close = page.count("</style>")
assert n_open == n_close == 1, "style blocks: %d open, %d close" % (n_open, n_close)
assert page.rindex("</style>") < page.index("<header"), "a style block sits inside the body"
note("style blocks (derived)", n_open)

# 21.7: no TOP-LEVEL :root:not([data-theme="light"]) - it must sit inside a
# media query, or it paints the dark palette in light mode.  Brace-depth scan.
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

# dash entities and control characters must never reach disk
SPELL = ["—", "–", "&" + "mdash;", "&" + "ndash;", "&#8212;", "&#8211;",
         "&#x2014;", "&#x2013;", "&#X2014;", "&#X2013;", "―"]
hits = {s: page.count(s) for s in SPELL if page.count(s)}
assert not hits, "dash spellings present: %s" % hits
ctrl = [hex(ord(c)) for c in page if ord(c) < 32 and c not in "\n\r\t"]
assert not ctrl, "control characters: %s" % ctrl[:6]
nonascii = [c for c in page if ord(c) > 126]
assert not nonascii, "non-ASCII bytes: %s" % sorted(set(nonascii))[:8]
note("non-ASCII bytes", len(nonascii))

# external hosts must be a subset of the CSP allowlist.  Match the host of every
# absolute URL, including one with no trailing path (a bare preconnect).
ALLOW = {"cdnjs.cloudflare.com", "fonts.googleapis.com", "fonts.gstatic.com"}
hosts = set(re.findall(r"https://([A-Za-z0-9.-]+)", page))
assert hosts <= ALLOW, "hosts outside the CSP allowlist: %s" % sorted(hosts - ALLOW)
note("external hosts", ",".join(sorted(hosts)))

# svg-labels markup contract
assert page.count('class="figbox"') == 2, "figbox must wrap each svg"
assert page.count('class="lab') >= 10, "labels must carry class lab"
note("figbox wrappers", page.count('class="figbox"'))

open(OUT, "w", encoding="utf-8", newline="\n").write(page)
note("OUTPUT", OUT)
note("bytes", len(page.encode("utf-8")))

for k, v in REPORT:
    print("%-46s %s" % (k, v))
print("BUILD OK")
