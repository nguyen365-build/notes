"""Assemble the Q12.3 artifact from the series head + stylesheet + this page's body.

Head and stylesheet are SLICED from the previous page in the series, never
retyped, and the slice indices are LOCATED rather than copied.

Guards run at build time, each proved live against a known-present control:
  class-collision   every invented name is namespaced and absent upstream
  figure-name       the page's OWN names (which KEEP exempts) are absent upstream
  token             every var() leaned on is actually defined upstream
  element-inherit   every element.class rule redeclares or records an inherited
                    constraining property from a bare element selector upstream
  orphan-class      every class the body uses has a rule somewhere
  display delimiter no bracket-delimited display block, balanced $$
  inline delimiter  every $...$ converted, zero bare dollars survive
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
SRC = os.path.join(ART, "Q12.2-sine-linearization.html")
OUT = os.path.join(ART, "Q12.3-four-decimal-places.html")

sys.path.insert(0, HERE)
import _q123_fig                                     # noqa: E402

src = io.open(SRC, encoding="utf-8").read().split("\n")

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

TITLE = "Write Four, Trust Two"
head = re.sub(r"<title>.*?</title>", "<title>" + TITLE + "</title>",
              head, count=1)
assert "<title>" + TITLE + "</title>" in head
assert "Radians Or Nothing" not in head, "inherited the previous page's title"
assert "The Nearest Exact Point" not in head, "inherited an older title"

old = re.search(r"/\* ===== ops console.*?\*/", style, re.S)
assert old, "legend comment not found"
new = """/* ===== ops console, MATH 265 series ========================================
   Palette and type are the series system, unchanged since Q1.1.  What is
   specific to THIS page is what the five accent hues MEAN.  Q12.3 CLOSES the
   linear-approximation category.  Q12.1's idea was choosing the anchor and
   Q12.2's was choosing the unit; this page's idea is what the answer is WORTH.
   So the two loudest hues carry THE ESTIMATE against THE TRUE VALUE, and the
   signature block is the place ladder in section 03, where the two are rounded
   side by side and the agreement turns out not to be nested.

     THE ESTIMATE, what you write                            --rul amber
     THE TRUE VALUE, what you must NOT write                 --chn slate
     WHERE MARKS DIE                                         --los terracotta
     THE VARIATION families                                  --fam teal
     NUMERICS: bounds, errors, place counts, gates           --num mauve
   ========================================================================= */"""
style = style[:old.start()] + new + style[old.end():]

INHERITED = style                       # snapshot BEFORE this page's own EXTRA

EXTRA = """
/* --- answer bar ---------------------------------------------------------- */
.ansbar{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(300px,100%),1fr));
  gap:1px;background:var(--line);border:1px solid var(--line);border-radius:3px;margin-top:26px}
.ansbar > div{background:var(--surface);padding:13px 16px;display:flex;flex-direction:column;gap:5px}
.ansbar .k{font-family:var(--mono);font-size:10px;letter-spacing:.09em;
  text-transform:uppercase;color:var(--ink3)}
.ansbar .v{font-size:17px;color:var(--rul);font-weight:600}
.ansbar .v.mono{font-family:var(--mono);font-size:14px}
.ansbar .v mjx-container,.ansbar .v mjx-container svg{color:var(--rul);
  fill:currentColor}

/* --- the two-part ledger: this page runs the method twice ----------------- */
.ledger{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(360px,100%),1fr));
  gap:1px;background:var(--line);border:1px solid var(--line);border-radius:3px;margin:24px 0}
.ledger .col{background:var(--surface);padding:18px 20px;overflow-x:auto}
.ledger .col.add{background:var(--rul-soft)}
.ledger .col.inh{background:var(--chn-soft)}
.ledger .colh{font-family:var(--mono);font-size:10.5px;letter-spacing:.09em;
  text-transform:uppercase;color:var(--ink3);margin:0 0 12px}
.ledger .col.add .colh{color:var(--rul)}
.ledger .col.inh .colh{color:var(--chn)}
.ledger .tag{margin:14px 0 0;padding:11px 13px;border-radius:3px;font-size:13.5px;line-height:1.6}
.ledger .tag.ok{background:var(--surface);border-left:3px solid var(--rul)}

/* --- the five moves ------------------------------------------------------ */
.steps{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(240px,100%),1fr));
  gap:1px;background:var(--line);border:1px solid var(--line);border-radius:3px;margin:22px 0}
.steps .st{background:var(--surface);padding:16px 18px}
.steps .sth{font-family:var(--mono);font-size:10.5px;letter-spacing:.09em;
  text-transform:uppercase;color:var(--rul);margin:0 0 9px}
.steps .st p:last-child{margin:0;font-size:14px;line-height:1.62;max-width:none}

/* --- the verification / discrimination checks ---------------------------- */
.checks{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(280px,100%),1fr));
  gap:1px;background:var(--line);border:1px solid var(--line);border-radius:3px;margin:22px 0}
.checks .ck{background:var(--surface);padding:16px 18px}
.checks .ckh{font-family:var(--mono);font-size:10.5px;letter-spacing:.09em;
  text-transform:uppercase;color:var(--num);margin:0 0 9px}
.checks .ck p:last-child{margin:0;font-size:14px;line-height:1.62;max-width:none}

/* --- variation families -------------------------------------------------- */
.fam{margin:26px 0;padding:2px 0 0;border-top:1px solid var(--line)}
.fam .famh{margin:16px 0 6px;font-size:16.5px;font-weight:600}
.fam .fk{display:inline-block;font-family:var(--mono);font-size:10.5px;
  letter-spacing:.09em;text-transform:uppercase;color:var(--fam);
  background:var(--fam-soft);padding:3px 8px;border-radius:3px;margin-right:10px;
  vertical-align:2px}
.fam .famt{margin:0 0 12px;font-size:14px;color:var(--ink2);line-height:1.66}

/* --- provenance ---------------------------------------------------------- */
.prov{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(300px,100%),1fr));
  gap:1px;background:var(--line);border:1px solid var(--line);border-radius:3px;margin:22px 0}
.prov .pv{background:var(--surface);padding:16px 18px}
.prov .pvh{font-family:var(--mono);font-size:10.5px;letter-spacing:.09em;
  text-transform:uppercase;color:var(--ink3);margin:0 0 9px}
.prov .pv p:last-child{margin:0;font-size:14px;line-height:1.62;max-width:none}

/* --- verification bar ---------------------------------------------------- */
.vbar{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(150px,100%),1fr));
  gap:1px;background:var(--line);border:1px solid var(--line);border-radius:3px;margin:22px 0}
.vbar > div{background:var(--surface);padding:14px 16px;display:flex;
  flex-direction:column;gap:5px}
.vbar .k{font-family:var(--mono);font-size:10px;letter-spacing:.09em;
  text-transform:uppercase;color:var(--ink3)}
.vbar .v{font-family:var(--mono);font-size:19px;color:var(--num);font-weight:600}

/* --- the verbatim stem --------------------------------------------------- */
blockquote.quote123{margin:20px 0;padding:16px 20px;background:var(--surface);
  border:1px solid var(--line);border-left:3px solid var(--chn);border-radius:3px;
  font-size:15px;line-height:1.72;max-width:none}

/* --- ranked trap list and drill list -------------------------------------
   ONE content child at column 2.  A list item holding several inline children
   in a two-column grid pushes everything after the first into the counter
   column and renders one word wide, and no layout gate reports it.
   max-width is redeclared because the inherited bare `ul,ol` rule clamps to
   70ch, which renders these panels 628px wide inside a 1034px column. */
ol.tl,ol.dr{list-style:none;counter-reset:t123;margin:20px 0;padding:0;
  max-width:none;
  display:flex;flex-direction:column;gap:1px;background:var(--line);
  border:1px solid var(--line);border-radius:3px}
ol.tl li,ol.dr li{counter-increment:t123;background:var(--surface);
  display:grid;grid-template-columns:38px minmax(0,1fr);align-items:start;
  padding:13px 16px;line-height:1.66}
ol.tl li::before,ol.dr li::before{content:counter(t123);grid-column:1;
  font-family:var(--mono);font-size:12px;color:var(--los);padding-top:2px}
ol.dr li::before{color:var(--fam)}
ol.tl li > span,ol.dr li > span{grid-column:2}
b.ans{color:var(--rul);font-family:var(--mono);font-size:12.5px}

/* --- verdict, warn, caption ---------------------------------------------- */
.verdict{margin:18px 0;padding:14px 17px;background:var(--rul-soft);
  border-left:3px solid var(--rul);border-radius:3px;line-height:1.66;max-width:none}
p.warn{margin:16px 0;padding:12px 15px;background:var(--los-soft);
  border-left:3px solid var(--los);border-radius:3px;font-size:14px;
  line-height:1.64;max-width:none}
p.cap{margin:14px 0 0;font-size:13.5px;color:var(--ink2);line-height:1.68}

/* --- table cell tints ---------------------------------------------------- */
td.ok2{color:var(--rul)}
td.no2{color:var(--los)}

/* --- the figures ---------------------------------------------------------
   cell123/hit123/miss123/vsn123/los123/track123/fill123/mark123 are unique to
   this page; lab, hd, sm, tk, am and gridl are DELIBERATELY the series names,
   because svg-labels.mjs selects text.lab and exempts /grid|axis/.
   Both figures are built from RECTS, so no diagonal line bounding box can be
   reported as crossing a label. */
.figbox{background:var(--surface);border:1px solid var(--line);border-radius:3px;
  padding:18px 16px;margin:20px 0;overflow-x:auto}
.figbox svg{display:block;min-width:800px;margin:0 auto}
.figbox .gridl{stroke:var(--line);stroke-width:1}
.figbox .cell123{fill:var(--surface);stroke:none}
.figbox .hit123{fill:var(--rul-soft)}
.figbox .miss123{fill:var(--los-soft)}
.figbox .track123{fill:var(--surface);stroke:var(--line);stroke-width:1}
.figbox .fill123{fill:var(--num-soft)}
.figbox .mark123{fill:var(--rul)}
.figbox text.lab{font-family:var(--mono);font-size:12.5px;fill:var(--ink);
  letter-spacing:.02em}
.figbox text.lab.hd{font-size:10.5px;letter-spacing:.1em;fill:var(--ink3)}
.figbox text.lab.sm{font-size:11.5px;fill:var(--ink2);letter-spacing:.03em}
.figbox text.lab.tk{font-size:10px;fill:var(--ink3);letter-spacing:.06em}
.figbox text.lab.am{fill:var(--rul);font-size:11.5px}
.figbox text.lab.vsn123{fill:var(--los)}
.figbox text.lab.los123{fill:var(--los)}
"""

SUFFIX = "123"
# KEEP is a HOLE in the collision guard, so it holds ONLY the genuine series
# names (which must not be renamed because upstream rules target them) and
# this page's own names, which are already suffixed and are checked separately
# by the figure-name guard below.  Everything else - every helper class this
# page invents, including short ones like .k and .col - is namespaced.
KEEP = {
    "wrap", "hdr", "eyebrow", "stand", "num", "note", "mono", "tscroll", "vtab",
    "figbox", "lab", "hd", "sm", "tk", "am", "gridl",
    "quote123", "cell123", "hit123", "miss123", "vsn123", "los123",
    "track123", "fill123", "mark123",
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
                    if c not in KEEP
                    and re.search(r"\." + re.escape(c) + r"(?![A-Za-z0-9_-])",
                                  INHERITED))
assert not collisions, "class names collide with the inherited slice: %r" % collisions
assert re.search(r"\.wrap(?![A-Za-z0-9_-])", INHERITED), \
    "guard control: .wrap must be upstream"
print("class-collision guard: %d names namespaced, %d deliberate overrides, "
      "0 collisions" % (len(rename), len(KEEP)))

# THIS page's own names sit in KEEP, so the guard above SKIPS them - the hole
# that let an upstream rule apply silently on Q11.2 (.vt) and Q12.1 (.tang).
FIGOWN = {"quote123", "cell123", "hit123", "miss123", "vsn123", "los123",
          "track123", "fill123", "mark123"}
figclash = sorted(c for c in FIGOWN
                  if re.search(r"\." + re.escape(c) + r"(?![A-Za-z0-9_-])",
                               INHERITED))
assert not figclash, "this page's own names already exist upstream: %r" % figclash
# prove the guard would fire: names that ARE upstream and that this page must
# therefore not claim bare.
_proved = []
for known in ("tanl", "vt", "vsn", "curve", "dot", "bar122"):
    if re.search(r"\." + re.escape(known) + r"(?![A-Za-z0-9_-])", INHERITED):
        _proved.append(known)
assert _proved, "figure-name guard unproven - nothing known is upstream"
print("figure-name guard control: %r ARE upstream, so the guard would fire if "
      "this page claimed any of them bare" % _proved)
print("figure-name guard: %d page-own names, none present upstream" % len(FIGOWN))

TOKENS = ("--rul", "--chn", "--los", "--fam", "--num", "--line", "--surface",
          "--ink", "--ink2", "--ink3", "--mono", "--rul-soft", "--los-soft",
          "--fam-soft", "--chn-soft")
for tok in TOKENS:
    assert tok + ":" in INHERITED, \
        "token %s is not defined in the inherited slice" % tok
used_tokens = set(re.findall(r"var\((--[a-z0-9-]+)\)", EXTRA))
missing = sorted(t for t in used_tokens if (t + ":") not in INHERITED)
assert not missing, "EXTRA leans on undefined tokens: %r" % missing
print("token guard: %d tokens confirmed defined upstream, 0 undefined references"
      % len(used_tokens))

# ---- build-time ELEMENT-INHERITANCE guard ----------------------------------
# The two class guards above compare NAMES.  Neither can see a bare ELEMENT
# selector upstream that constrains a class this page invents.  Upstream
# `ul,ol{...max-width:70ch}` clamped Q12.2's two ranked lists to 628px inside
# 1034px panels while every layout gate stayed clean.
CONSTRAINING = ("max-width",)
INHERIT_OK = {
    # prose captions deliberately keep the series' 70ch reading measure
    "p.cap123",
}
ELEMENT_RULES = {}
for m in re.finditer(r"(?m)^\s*([a-z][a-z0-9]*(?:\s*,\s*[a-z][a-z0-9]*)*)\s*\{([^{}]*)\}",
                     INHERITED):
    for el in [e.strip() for e in m.group(1).split(",")]:
        for prop in CONSTRAINING:
            if prop + ":" in m.group(2):
                ELEMENT_RULES.setdefault(el, set()).add(prop)
assert "ol" in ELEMENT_RULES and "max-width" in ELEMENT_RULES["ol"], (
    "guard control: upstream `ul,ol` must set max-width, else this guard "
    "measures nothing")
assert "p" in ELEMENT_RULES, "guard control: upstream `p` must set max-width"

unguarded = []
checked = 0
for m in re.finditer(r"(?m)^\s*([a-z]+\.[A-Za-z][A-Za-z0-9_-]*"
                     r"(?:\s*,\s*[a-z]+\.[A-Za-z][A-Za-z0-9_-]*)*)\s*\{([^{}]*)\}",
                     EXTRA):
    body = m.group(2)
    for sel in [s.strip() for s in m.group(1).split(",")]:
        el = sel.split(".")[0]
        for prop in ELEMENT_RULES.get(el, ()):
            checked += 1
            if prop + ":" not in body and sel not in INHERIT_OK:
                unguarded.append("%s does not redeclare %s" % (sel, prop))
assert not unguarded, "element-inheritance guard: %r" % unguarded
assert checked > 0, "element-inheritance guard checked nothing"
_probe = EXTRA.replace("max-width:none;" + chr(10), "", 1)
assert _probe != EXTRA, "guard control: the probe removed nothing"
_probe_bad = any(
    "max-width:" not in mm.group(2)
    for mm in re.finditer(r"(?m)^\s*(ol\.tl123[^{}]*?)\{([^{}]*)\}", _probe))
assert _probe_bad, ("guard control: removing max-width:none from the ranked "
                    "list rule must make the guard fire, and it did not")
print("element-inheritance guard: %d element/property pairs checked, "
      "%d deliberate inheritances recorded, 0 unguarded"
      % (checked, len(INHERIT_OK)))

style = style + EXTRA + "\n</style>"

body = io.open(os.path.join(HERE, "_q123_body.html"), encoding="utf-8").read()
body = _rn_html(body)

# ---- INLINE MATH DELIMITER CONTRACT ---------------------------------------
IOPEN = BS + "("
ICLOSE = BS + ")"


def _to_inline(html):
    out = []
    parts = html.split("$$")
    for i, seg in enumerate(parts):
        if i % 2 == 1:
            out.append("$$" + seg + "$$")
            continue
        bits = seg.split("$")
        if len(bits) % 2 == 0:
            raise AssertionError("odd number of inline $ in a text segment: %r"
                                 % seg[:160])
        rebuilt = bits[0]
        for j in range(1, len(bits), 2):
            rebuilt += IOPEN + bits[j] + ICLOSE + bits[j + 1]
        out.append(rebuilt)
    return "".join(out)


ndollar = body.count("$") - 2 * body.count("$$")
body = _to_inline(body)
assert body.count(IOPEN) == body.count(ICLOSE), "unbalanced inline delimiters"
assert body.count(IOPEN) == ndollar // 2, (
    "expected %d inline spans, produced %d" % (ndollar // 2, body.count(IOPEN)))
print("inline-math conversion: %d inline spans converted to the series "
      "delimiter" % body.count(IOPEN))

assert "LADDER_SVG" in body and "BRACKET_SVG" in body
body = body.replace("LADDER_SVG",
                    '<div class="figbox">' + _q123_fig.build_ladder() + "</div>")
body = body.replace("BRACKET_SVG",
                    '<div class="figbox">' + _q123_fig.build_bracket() + "</div>")

used = set()
for m in re.finditer(r'class="([^"]*)"', body):
    used.update(m.group(1).split())
sheet = INHERITED + EXTRA
undefined = sorted(c for c in used
                   if not re.search(r"\." + re.escape(c) + r"(?![A-Za-z0-9_-])",
                                    sheet))
assert not undefined, "classes used in the body with no rule anywhere: %r" % undefined
print("orphan-class guard: %d distinct classes used, all defined" % len(used))

page = head + "\n" + style + "\n" + body + "\n"

BAD = ["&" + "mdash;", "&" + "ndash;", "&#8212;", "&#8211;", "&#x2014;",
       "&#x2013;", chr(0x2014), chr(0x2013)]
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
print("display-math gate: %d display blocks, all $$-delimited"
      % (bodyonly.count("$$") // 2))

icfg = re.search(r"inlineMath:\s*(\[\[.*?\]\])", head)
assert icfg, "inlineMath is not configured in the head"
assert "$" not in icfg.group(1), (
    "the head DOES accept $...$ inline; this gate assumes it does not: %s"
    % icfg.group(1))
nbare = bodyonly.count("$") - 2 * bodyonly.count("$$")
assert nbare == 0, (
    "%d bare dollars survive outside $$ blocks and will render as raw LaTeX"
    % nbare)
assert bodyonly.count(IOPEN) == bodyonly.count(ICLOSE) > 100, \
    "inline math did not survive into the page"
print("inline-math gate: %d bare dollars outside display blocks, %d inline spans"
      % (nbare, bodyonly.count(IOPEN)))

assert page.count("<style>") == 1 and page.count("</style>") == 1
assert page.count("<main") == 1 and page.count("</main>") == 1
assert page.count('class="figbox"') == 2, "expected two figures"
assert 'text class="lab' in page
assert "LADDER_SVG" not in page and "BRACKET_SVG" not in page, \
    "a figure placeholder survived"
svgs = _q123_fig.build_ladder() + _q123_fig.build_bracket()
nonascii = sorted({c for c in svgs if ord(c) > 127})
assert not nonascii, "non-ASCII in the SVG will mojibake under file://: %r" % nonascii
print("svg ascii gate: 0 non-ASCII bytes across both figures")

io.open(OUT, "w", encoding="utf-8", newline="\n").write(page)
print("wrote", OUT, len(page), "bytes")
print("dash gate: 0 across all 8 spellings; control characters: none")
