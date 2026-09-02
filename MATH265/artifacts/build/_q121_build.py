"""Assemble the Q12.1 artifact from the series head + stylesheet + this page's body.

Head and stylesheet are SLICED from the previous page in the series, never
retyped, and the slice indices are LOCATED rather than copied - the style block
grows every time a page adds rules.

Guards run at build time, each one proved live against a known-present control:
  class-collision   every invented name is namespaced and absent upstream
  figure-name       the page's OWN names (which KEEP exempts) are absent upstream
  token             every var() leaned on is actually defined upstream
  orphan-class      every class the body uses has a rule somewhere
  mathjax delimiter no bracket-delimited display block, balanced $$
  dash / control    no dash spelling and no control character reaches disk
"""
import sys
sys.dont_write_bytecode = True   # keep __pycache__ out of this content directory
import io
import os
import re
import sys

BS = chr(92)
HERE = os.path.dirname(os.path.abspath(__file__))
ART = os.path.dirname(HERE)
SRC = os.path.join(ART, "Q11.2-rocket-radar-related-rates.html")
OUT = os.path.join(ART, "Q12.1-square-root-differentials.html")

sys.path.insert(0, HERE)
import _q121_fig                                     # noqa: E402

src = io.open(SRC, encoding="utf-8").read().split("\n")

# ---- locate the slice, do not copy indices ---------------------------------
sopen = next(i for i, l in enumerate(src) if l.lstrip().startswith("<style>"))
sclose = next(i for i, l in enumerate(src) if "</style>" in l)
head = "\n".join(src[0:sopen])
style = "\n".join(src[sopen:sclose])
assert style.lstrip().startswith("<style>"), style[:60]
assert "</style>" not in style, "slice ran past the closing tag"
assert 'mjx-container:not([display="true"])' in style, "inline-MathJax fix missing"
assert ':root:not([data-theme="light"])' in style, "dark-theme guard missing"
assert ':root[data-theme="dark"]' in style, "explicit dark stamp missing"
assert "<title>" in head, "title not inside the head slice"
assert "tex-svg" in head, "MathJax script not inside the head slice"
assert re.search(r"--mono\s*:", style), "the --mono repair should be inherited"

# ---- this page's name ------------------------------------------------------
head = re.sub(r"<title>.*?</title>", "<title>The Nearest Exact Point</title>",
              head, count=1)
assert "<title>The Nearest Exact Point</title>" in head
assert "Eliminate Or Compute" not in head, "inherited the previous page's title"

# ---- what the five accent hues mean on THIS page ---------------------------
old = re.search(r"/\* ===== ops console.*?\*/", style, re.S)
assert old, "legend comment not found"
new = """/* ===== ops console, MATH 265 series ========================================
   Palette and type are the series system, unchanged since Q1.1.  What is
   specific to THIS page is what the five accent hues MEAN.  Q12.1 OPENS the
   linear-approximation category, and its one idea is that CHOOSING THE ANCHOR
   is the whole question: the linearization is the tangent line, so both the
   anchor's quality and the error's sign are geometry rather than arithmetic.
   The two loudest hues therefore carry that pair - the anchor against the
   distance from it - and the signature block is the two-column anchor
   decision in section 03, beside the figure that measures it.

     THE ANCHOR: exact, near, f'(a) clean                          --rul amber
     THE DISTANCE dx and everything it costs                       --chn slate
     WHERE MARKS DIE                                               --los terracotta
     THE VARIATION families                                        --fam teal
     NUMERICS: bounds, errors, gates, controls                     --num mauve
   ========================================================================= */"""
style = style[:old.start()] + new + style[old.end():]

INHERITED = style                       # snapshot BEFORE this page's own EXTRA

EXTRA = """
/* --- answer bar ---------------------------------------------------------- */
.ansbar{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(210px,100%),1fr));
  gap:1px;background:var(--line);border:1px solid var(--line);border-radius:3px;margin-top:26px}
.ansbar > div{background:var(--surface);padding:13px 16px;display:flex;flex-direction:column;gap:5px}
.ansbar .k{font-family:var(--mono);font-size:10px;letter-spacing:.09em;
  text-transform:uppercase;color:var(--ink3)}
.ansbar .v{font-size:17px;color:var(--rul);font-weight:600}
.ansbar .v.mono{font-family:var(--mono);font-size:15px}
/* MathJax SVG does not inherit the cell's colour on its own, so the
   typeset answer rendered ink-black beside three amber siblings.  No
   gate sees this; the screenshot did. */
.ansbar .v mjx-container,.ansbar .v mjx-container svg{color:var(--rul);
  fill:currentColor}

/* --- the anchor decision: this page's signature block --------------------- */
.ledger{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(340px,100%),1fr));
  gap:1px;background:var(--line);border:1px solid var(--line);border-radius:3px;margin:24px 0}
.ledger .col{background:var(--surface);padding:18px 20px}
.ledger .col.add{background:var(--rul-soft)}
.ledger .col.inh{background:var(--chn-soft)}
.ledger .colh{font-family:var(--mono);font-size:10.5px;letter-spacing:.09em;
  text-transform:uppercase;color:var(--ink3);margin:0 0 12px}
.ledger .col.add .colh{color:var(--rul)}
.ledger .col.inh .colh{color:var(--chn)}
.ledger ul{margin:0;padding-left:19px;display:flex;flex-direction:column;gap:9px}
.ledger li{line-height:1.62}
.ledger .tag{margin:14px 0 0;padding:11px 13px;border-radius:3px;font-size:13.5px;line-height:1.6}
.ledger .tag.ok{background:var(--rul-soft);border-left:3px solid var(--rul)}
.ledger .tag.no{background:var(--chn-soft);border-left:3px solid var(--chn)}

/* --- the four setup steps ------------------------------------------------ */
.steps{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(240px,100%),1fr));
  gap:1px;background:var(--line);border:1px solid var(--line);border-radius:3px;margin:22px 0}
.steps .st{background:var(--surface);padding:16px 18px}
.steps .sth{font-family:var(--mono);font-size:10.5px;letter-spacing:.09em;
  text-transform:uppercase;color:var(--rul);margin:0 0 9px}
.steps .st p:last-child{margin:0;font-size:14px;line-height:1.62}

/* --- the four routes.  Cells carry whole equations, so the track floor must
   collapse at narrow widths or the 430px lint case overflows. ------------- */
.chain{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(430px,100%),1fr));
  gap:1px;background:var(--line);border:1px solid var(--line);border-radius:3px;margin:22px 0}
.chain .ch{background:var(--surface);padding:16px 18px}
.chain .chh{font-family:var(--mono);font-size:10.5px;letter-spacing:.09em;
  text-transform:uppercase;color:var(--chn);margin:0 0 10px}

/* --- the eight-second checks --------------------------------------------- */
.checks{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(260px,100%),1fr));
  gap:1px;background:var(--line);border:1px solid var(--line);border-radius:3px;margin:22px 0}
.checks .ck{background:var(--surface);padding:16px 18px}
.checks .ckh{font-family:var(--mono);font-size:10.5px;letter-spacing:.09em;
  text-transform:uppercase;color:var(--num);margin:0 0 9px}
.checks .ck p:last-child{margin:0;font-size:14px;line-height:1.62}

/* --- variation families -------------------------------------------------- */
.fam{margin:26px 0;padding:2px 0 0;border-top:1px solid var(--line)}
.fam .famh{margin:16px 0 6px;font-size:16.5px;font-weight:600}
.fam .fk{display:inline-block;font-family:var(--mono);font-size:10.5px;
  letter-spacing:.09em;text-transform:uppercase;color:var(--fam);
  background:var(--fam-soft);padding:3px 8px;border-radius:3px;margin-right:10px;
  vertical-align:2px}
.fam .famt{margin:0 0 12px;font-size:14px;color:var(--ink2);line-height:1.62}

/* --- provenance ---------------------------------------------------------- */
.prov{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(300px,100%),1fr));
  gap:1px;background:var(--line);border:1px solid var(--line);border-radius:3px;margin:22px 0}
.prov .pv{background:var(--surface);padding:16px 18px}
.prov .pvh{font-family:var(--mono);font-size:10.5px;letter-spacing:.09em;
  text-transform:uppercase;color:var(--ink3);margin:0 0 9px}
.prov .pv p:last-child{margin:0;font-size:14px;line-height:1.62}

/* --- verification bar ---------------------------------------------------- */
.vbar{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(150px,100%),1fr));
  gap:1px;background:var(--line);border:1px solid var(--line);border-radius:3px;margin:22px 0}
.vbar > div{background:var(--surface);padding:14px 16px;display:flex;
  flex-direction:column;gap:5px}
.vbar .k{font-family:var(--mono);font-size:10px;letter-spacing:.09em;
  text-transform:uppercase;color:var(--ink3)}
.vbar .v{font-family:var(--mono);font-size:19px;color:var(--num);font-weight:600}

/* --- ranked trap list and drill list -------------------------------------
   ONE content child at column 2.  A list item holding several inline children
   in a two-column grid pushes everything after the first into the counter
   column and renders one word wide, and no layout gate reports it. */
ol.tl121,ol.dr121{list-style:none;counter-reset:t121;margin:20px 0;padding:0;
  display:flex;flex-direction:column;gap:1px;background:var(--line);
  border:1px solid var(--line);border-radius:3px}
ol.tl121 li,ol.dr121 li{counter-increment:t121;background:var(--surface);
  display:grid;grid-template-columns:38px minmax(0,1fr);align-items:start;
  padding:13px 16px;line-height:1.62}
ol.tl121 li::before,ol.dr121 li::before{content:counter(t121);grid-column:1;
  font-family:var(--mono);font-size:12px;color:var(--los);padding-top:2px}
ol.dr121 li::before{color:var(--fam)}
ol.tl121 li > span,ol.dr121 li > span{grid-column:2}
b.ans121{color:var(--rul);font-family:var(--mono);font-size:13px}

/* --- verdict, warn, caption, decision tree ------------------------------- */
.verdict{margin:14px 0 0;padding:12px 15px;background:var(--rul-soft);
  border-left:3px solid var(--rul);border-radius:3px;line-height:1.6}
p.warn{margin:16px 0;padding:12px 15px;background:var(--los-soft);
  border-left:3px solid var(--los);border-radius:3px;font-size:14px;line-height:1.62}
p.cap121{margin:14px 0 0;font-size:13.5px;color:var(--ink2);line-height:1.65}
pre.tree121{background:var(--surface);border:1px solid var(--line);border-radius:3px;
  padding:20px 22px;overflow-x:auto;font-family:var(--mono);font-size:12.5px;
  line-height:1.62;margin:20px 0;color:var(--ink2)}
p.disp{margin:16px 0;overflow-x:auto}

/* --- table cell tints ---------------------------------------------------- */
td.ok2{color:var(--rul)}
td.no2{color:var(--los)}

/* --- the figure ----------------------------------------------------------
   gapfill/tang/gapline/gdot/leadr/bar/barbest are unique to this page; lab,
   hd, sm, tk, am, vsn, gridl, axis, curve and dot are DELIBERATELY the series
   names, because svg-labels.mjs selects text.lab and exempts /grid|axis/. */
.figbox{background:var(--surface);border:1px solid var(--line);border-radius:3px;
  padding:18px 16px;margin:20px 0;overflow-x:auto}
.figbox svg{display:block;min-width:700px;margin:0 auto}
.figbox .gapfill{fill:var(--chn-soft);stroke:none}
.figbox .tanl{stroke:var(--rul);stroke-width:2.6}
.figbox .gapline{stroke:var(--fam);stroke-width:2.2}
.figbox .gdot{fill:var(--fam);stroke:none}
.figbox .leadr{stroke:var(--ink3);stroke-width:1;stroke-dasharray:3 3}
.figbox .bar{fill:var(--chn)}
.figbox .barbest{fill:var(--rul)}
.figbox .tansw{fill:var(--rul)}
.figbox .cursw{fill:var(--chn)}
.figbox .gridl{stroke:var(--line);stroke-width:1}
.figbox .axis{stroke:var(--ink3);stroke-width:1.2}
.figbox .curve{fill:none;stroke:var(--chn);stroke-width:2.6}
.figbox .dot{fill:var(--rul);stroke:var(--surface);stroke-width:1.8}
.figbox text.lab{font-family:var(--mono);font-size:12px;fill:var(--ink);
  letter-spacing:.02em}
.figbox text.lab.hd{font-size:10.5px;letter-spacing:.1em;fill:var(--ink3)}
.figbox text.lab.sm{font-size:10.5px;fill:var(--ink3);letter-spacing:.03em}
.figbox text.lab.tk{font-size:10px;fill:var(--ink3)}
.figbox text.lab.am{fill:var(--rul);font-size:11.5px}
.figbox text.lab.vsn{fill:var(--fam);font-size:11.5px}
"""

# ---- build-time class-collision guard --------------------------------------
SUFFIX = "121"
KEEP = {                                   # deliberate series overrides
    "wrap", "hdr", "eyebrow", "stand", "num", "note", "mono", "tscroll", "vtab",
    # already page-unique
    "tl121", "dr121", "cap121", "tree121", "ans121",
    # figure internals, all scoped under .figbox
    "figbox", "lab", "hd", "sm", "tk", "am", "vsn", "gridl", "axis", "curve",
    "dot", "gapfill", "tanl", "gapline", "gdot", "leadr", "bar", "barbest",
    "tansw", "cursw",
}
mine = set(re.findall(r"\.([A-Za-z][A-Za-z0-9_-]*)", EXTRA))
rename = {n: n + SUFFIX for n in sorted(mine - KEEP)}


def _rn_css(css):
    for a, b in rename.items():
        css = re.sub(r"\." + re.escape(a) + r"(?![A-Za-z0-9_-])", "." + b, css)
    return css


def _rn_html(html):
    def sub(m):
        names = [rename.get(n, n) for n in m.group(1).split()]
        return 'class="' + " ".join(names) + '"'
    return re.sub(r'class="([^"]*)"', sub, html)


EXTRA = _rn_css(EXTRA)

mine2 = set(re.findall(r"\.([A-Za-z][A-Za-z0-9_-]*)", EXTRA))
collisions = sorted(c for c in mine2
                    if c not in KEEP and re.search(r"\." + re.escape(c) + r"(?![A-Za-z0-9_-])",
                                                   INHERITED))
assert not collisions, "class names collide with the inherited slice: %r" % collisions
assert re.search(r"\.wrap(?![A-Za-z0-9_-])", INHERITED), "guard control: .wrap must be upstream"
print("class-collision guard: %d names namespaced, %d deliberate overrides, 0 collisions"
      % (len(rename), len(KEEP)))

# THIS page's own names sit in KEEP, so the guard above SKIPS them - which is
# exactly the hole that let an upstream rule apply silently on an earlier page.
# Check them separately.
FIGOWN = {"gapfill", "tanl", "gapline", "gdot", "leadr", "bar", "barbest",
          "tansw", "cursw",
          "tl121", "dr121", "cap121", "tree121", "ans121"}
figclash = sorted(c for c in FIGOWN
                  if re.search(r"\." + re.escape(c) + r"(?![A-Za-z0-9_-])", INHERITED))
assert not figclash, "this page's own names already exist upstream: %r" % figclash
assert re.search(r"\.curve(?![A-Za-z0-9_-])", INHERITED), \
    "figure-name guard control: .curve must be upstream"
print("figure-name guard: %d page-own names, none present upstream" % len(FIGOWN))

TOKENS = ("--rul", "--chn", "--los", "--fam", "--num", "--line", "--surface",
          "--ink", "--ink2", "--ink3", "--mono", "--rul-soft", "--los-soft",
          "--fam-soft", "--chn-soft")
for tok in TOKENS:
    assert tok + ":" in INHERITED, "token %s is not defined in the inherited slice" % tok
used_tokens = set(re.findall(r"var\((--[a-z0-9-]+)\)", EXTRA))
missing = sorted(t for t in used_tokens if (t + ":") not in INHERITED)
assert not missing, "EXTRA leans on undefined tokens: %r" % missing
print("token guard: %d tokens confirmed defined upstream, 0 undefined references"
      % len(used_tokens))

style = style + EXTRA + "\n</style>"

body = io.open(os.path.join(HERE, "_q121_body.html"), encoding="utf-8").read()
body = _rn_html(body)

# ---- INLINE MATH DELIMITER CONTRACT ---------------------------------------
# The series head configures inlineMath as BACKSLASH-PAREN only; a $...$ span
# ships as VISIBLE RAW LATEX and no layout gate reports it.  The carryover
# recorded the DISPLAY contract after Q11.1 hit it; this is the inline twin,
# found the same way - by looking at the screenshot.
#
# The body is authored with $...$ because it is far more readable, so convert
# here, leaving $$...$$ display blocks untouched, and then assert that no bare
# dollar survives.
IOPEN = BS + "("
ICLOSE = BS + ")"


def _to_inline(html):
    out = []
    parts = html.split("$$")
    for i, seg in enumerate(parts):
        if i % 2 == 1:                       # inside a $$ display block
            out.append("$$" + seg + "$$")
            continue
        bits = seg.split("$")
        if len(bits) % 2 == 0:
            raise AssertionError("odd number of inline $ in a text segment: %r"
                                 % seg[:120])
        rebuilt = bits[0]
        for j in range(1, len(bits), 2):
            rebuilt += IOPEN + bits[j] + ICLOSE + bits[j + 1]
        out.append(rebuilt)
    # the split/rejoin above re-adds the $$ markers inside odd segments, so the
    # even segments are concatenated directly
    return "".join(out)


ndollar = body.count("$") - 2 * body.count("$$")
body = _to_inline(body)
assert body.count(IOPEN) == body.count(ICLOSE), "unbalanced inline delimiters"
assert body.count(IOPEN) == ndollar // 2, (
    "expected %d inline spans, produced %d" % (ndollar // 2, body.count(IOPEN)))
print("inline-math gate: %d inline spans converted to the series delimiter"
      % body.count(IOPEN))

svg = _q121_fig.build()                    # the figure keeps the KEEP names
assert "FIGURE_SVG" in body
body = body.replace("FIGURE_SVG", '<div class="figbox">' + svg + "</div>")

used = set()
for m in re.finditer(r'class="([^"]*)"', body):
    used.update(m.group(1).split())
sheet = INHERITED + EXTRA
undefined = sorted(c for c in used
                   if not re.search(r"\." + re.escape(c) + r"(?![A-Za-z0-9_-])", sheet))
assert not undefined, "classes used in the body with no rule anywhere: %r" % undefined
print("orphan-class guard: %d distinct classes used, all defined" % len(used))

page = head + "\n" + style + "\n" + body + "\n"

BAD = ["&" + "mdash;", "&" + "ndash;", "&#8212;", "&#8211;", "&#x2014;", "&#x2013;",
       chr(0x2014), chr(0x2013)]
# the series body DOES use the named mdash entity deliberately as a punctuation
# dash; the house rule bans the CHARACTER, and dash-lint bans every spelling, so
# convert here rather than shipping one.
page = page.replace("&" + "mdash;", " - ").replace("&" + "ndash;", "-")
found = {b: page.count(b) for b in BAD if page.count(b)}
assert not found, "dash spellings present: %r" % found
ctrl = sorted({hex(ord(c)) for c in page if ord(c) < 32 and c not in "\n\r\t"})
assert not ctrl, "control characters present: %r" % ctrl

cfg = re.search(r"displayMath:\s*(\[\[.*?\]\])", head)
assert cfg and "$$" in cfg.group(1), "display delimiters are not $$"
bodyonly = page[page.index("<main"):]
assert BS + "[" not in bodyonly, "bracket-delimited display math will not typeset"
assert bodyonly.count("$$") % 2 == 0 and bodyonly.count("$$") >= 2, "unbalanced $$"
print("mathjax delimiter gate: %d display blocks, all $$-delimited"
      % (bodyonly.count("$$") // 2))
# no BARE dollar may survive outside a $$ block - a $...$ span would ship as
# visible raw LaTeX under this head's inlineMath configuration.
icfg = re.search(r"inlineMath:\s*(\[\[.*?\]\])", head)
assert icfg, "inlineMath is not configured in the head"
assert "$" not in icfg.group(1), (
    "the head DOES accept $...$ inline; this gate assumes it does not: %s"
    % icfg.group(1))
assert bodyonly.count("$") == 2 * (bodyonly.count("$$")), (
    "%d bare dollars survive outside $$ blocks and will render as raw LaTeX"
    % (bodyonly.count("$") - 2 * bodyonly.count("$$")))
assert bodyonly.count(BS + "(") == bodyonly.count(BS + ")") > 100, \
    "inline math did not survive into the page"
print("inline-math gate: %d bare dollars outside display blocks, %d inline spans"
      % (bodyonly.count("$") - 2 * bodyonly.count("$$"), bodyonly.count(BS + "(")))
assert page.count("<style>") == 1 and page.count("</style>") == 1
assert page.count("<main") == 1 and page.count("</main>") == 1
assert "figbox" in page and 'text class="lab' in page
assert "FIGURE_SVG" not in page, "the figure placeholder survived"
nonascii = sorted({c for c in svg if ord(c) > 127})
assert not nonascii, "non-ASCII in the SVG will mojibake under file://: %r" % nonascii
print("svg ascii gate: 0 non-ASCII bytes in the figure")

io.open(OUT, "w", encoding="utf-8", newline="\n").write(page)
print("wrote", OUT, len(page), "bytes")
print("dash gate: 0 across all 8 spellings; control characters: none")
