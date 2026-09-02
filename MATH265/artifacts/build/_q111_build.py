"""Assemble the Q11.1 artifact from the series head + stylesheet + this page's body.

The head and stylesheet are SLICED from the previous page in the series rather
than retyped.  The slice indices are LOCATED, never copied from a previous run:
the style block grows every time a page adds rules.
"""
import sys
sys.dont_write_bytecode = True   # keep __pycache__ out of this content directory
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ART = os.path.dirname(HERE)
SRC = os.path.join(ART, "Q10.2-tangent-to-implicit-curve.html")
OUT = os.path.join(ART, "Q11.1-gravel-cone-related-rates.html")

sys.path.insert(0, HERE)
import _q111_fig                                     # noqa: E402

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

# ---- this page's name ------------------------------------------------------
head = re.sub(r"<title>.*?</title>", "<title>Always Versus When</title>", head, count=1)
assert "<title>Always Versus When</title>" in head
assert "Point Must Be On The Curve" not in head

# ---- what the five accent hues mean on THIS page ---------------------------
old = re.search(r"/\* ===== ops console.*?\*/", style, re.S)
assert old, "legend comment not found"
new = """/* ===== ops console, MATH 265 series ========================================
   Palette and type are the series system, unchanged since Q1.1.  What is
   specific to THIS page is what the five accent hues MEAN.  Q11.1 OPENS the
   related-rates category, and the category's whole difficulty is a reading
   problem rather than a calculus one: the stem hands you numbers of two
   incompatible kinds and does not label them.  So the two loudest hues carry
   the page's single idea - a quantity that is true ALWAYS against one true
   only WHEN - and the signature block is the two-column substitution licence
   in section 01.

     ALWAYS: substitutable before differentiating       --rul   amber
     WHEN:   a snapshot, substitutable only after       --chn   slate
     WHERE MARKS DIE                                    --los   terracotta
     THE VARIATION families                             --fam   teal
     NUMERICS: gates, arms, tolerances, controls        --num   mauve
   ========================================================================= */"""
style = style[:old.start()] + new + style[old.end():]

# ---- repair an inherited defect --------------------------------------------
# The Q10.2 slice references var(--mono) sixteen times and NOTHING in the whole
# series ever defines --mono, so all sixteen font-family declarations are
# invalid at computed-value time and silently fall back to the inherited sans
# face.  Q10.1 and Q9.1 spell the stack out and never use the token, which is
# why it was never noticed.  Define it once, here, so both the inherited rules
# and this page's resolve.
assert style.count("var(--mono)") >= 16, "expected the inherited --mono uses"
assert not re.search(r"--mono\s*:", style), "--mono is defined after all - re-check"
MONOFIX = '--mono:"IBM Plex Mono",ui-monospace,SFMono-Regular,Menlo,monospace;'
at = style.index(":root{") + len(":root{")
style = style[:at] + MONOFIX + style[at:]
assert re.search(r"--mono\s*:", style), "the --mono repair did not take"
assert "IBM+Plex+Mono" in head or "IBM%20Plex%20Mono" in head or "Plex+Mono" in head, \
    "IBM Plex Mono is not actually being loaded by the head"
print("inherited-defect repair: --mono defined (%d references now resolve)"
      % style.count("var(--mono)"))

INHERITED = style                       # snapshot BEFORE this page's own EXTRA

EXTRA = """
/* --- two more inherited orphans -------------------------------------------
   .stand and .tscroll are used by the series BODY markup introduced at Q10.2
   but have no rule anywhere in the accumulated sheet, so that page's
   standfirst renders as undifferentiated body text.  .tscroll is a hook the
   table-fit gate selects on; give it the overflow it implies. ------------- */
p.stand{font-size:16.5px;line-height:1.68;color:var(--ink2);max-width:66ch;
  margin:15px 0 0}
.tscroll{overflow-x:auto}

/* --- header spacing: scope the page-bottom padding to main.wrap ---------- */
header.hdr{padding-top:30px;padding-bottom:30px}

/* --- answer bar ---------------------------------------------------------- */
.ansbar{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(210px,100%),1fr));
  gap:1px;background:var(--line);border:1px solid var(--line);border-radius:3px;margin-top:26px}
.ansbar > div{background:var(--surface);padding:13px 16px;display:flex;flex-direction:column;gap:5px}
.ansbar .k{font-family:var(--mono);font-size:10px;letter-spacing:.09em;
  text-transform:uppercase;color:var(--ink3)}
.ansbar .v{font-size:17px;color:var(--rul);font-weight:600}
.ansbar .v.mono{font-family:var(--mono);font-size:15px}

/* --- the always/when licence: this page's signature block ---------------- */
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
.ledger .tag.no{background:var(--los-soft);border-left:3px solid var(--los)}

/* --- the four setup lines ------------------------------------------------ */
.steps{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(240px,100%),1fr));
  gap:1px;background:var(--line);border:1px solid var(--line);border-radius:3px;margin:22px 0}
.steps .st{background:var(--surface);padding:16px 18px}
.steps .sth{font-family:var(--mono);font-size:10.5px;letter-spacing:.09em;
  text-transform:uppercase;color:var(--rul);margin:0 0 9px}
.steps .st p:last-child{margin:0;font-size:14px;line-height:1.62}

/* --- the four-step solve board ------------------------------------------- */
.chain{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(430px,100%),1fr));
  gap:1px;background:var(--line);border:1px solid var(--line);border-radius:3px;margin:22px 0}
.chain .ch{background:var(--surface);padding:16px 18px}
.chain .chh{font-family:var(--mono);font-size:10.5px;letter-spacing:.09em;
  text-transform:uppercase;color:var(--chn);margin:0 0 10px}
.chain .chm{margin:0;overflow-x:auto}

/* --- the eight-second checks --------------------------------------------- */
.checks{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(300px,100%),1fr));
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

/* --- the hiding-point panels --------------------------------------------- */
.hide{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(300px,100%),1fr));
  gap:1px;background:var(--line);border:1px solid var(--line);border-radius:3px;margin:22px 0}
.hide .hd1{background:var(--los-soft);padding:16px 18px}
.hide .hdh{font-family:var(--mono);font-size:10.5px;letter-spacing:.09em;
  text-transform:uppercase;color:var(--los);margin:0 0 9px}
.hide .hd1 p:last-child{margin:0;font-size:14px;line-height:1.62}

/* --- ranked trap list and drill list -------------------------------------
   ONE content child at column 2.  A list item holding several inline children
   in a two-column grid pushes everything after the first into the 34px
   counter column and renders one word wide, and no layout gate reports it. */
ol.tl111,ol.dr111{list-style:none;counter-reset:t111;margin:20px 0;padding:0;
  display:flex;flex-direction:column;gap:1px;background:var(--line);
  border:1px solid var(--line);border-radius:3px}
ol.tl111 li,ol.dr111 li{counter-increment:t111;background:var(--surface);
  display:grid;grid-template-columns:38px minmax(0,1fr);align-items:start;
  padding:13px 16px;line-height:1.62}
ol.tl111 li::before,ol.dr111 li::before{content:counter(t111);grid-column:1;
  font-family:var(--mono);font-size:12px;color:var(--los);padding-top:2px}
ol.dr111 li::before{color:var(--fam)}
ol.tl111 li > span,ol.dr111 li > span{grid-column:2}

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

/* --- verdict, warn, figure caption, decision tree ------------------------ */
.verdict{margin:14px 0 0;padding:12px 15px;background:var(--rul-soft);
  border-left:3px solid var(--rul);border-radius:3px;line-height:1.6}
p.warn{margin:16px 0;padding:12px 15px;background:var(--los-soft);
  border-left:3px solid var(--los);border-radius:3px;font-size:14px;line-height:1.62}
p.cap111{margin:14px 0 0;font-size:13.5px;color:var(--ink2);line-height:1.65}
pre.tree111{background:var(--surface);border:1px solid var(--line);border-radius:3px;
  padding:20px 22px;overflow-x:auto;font-family:var(--mono);font-size:12.5px;
  line-height:1.62;margin:20px 0;color:var(--ink2)}
p.disp{margin:16px 0;overflow-x:auto}

/* --- table cell tints for the entry table -------------------------------- */
td.ok2{color:var(--rul)}
td.no2{color:var(--los)}

/* --- the figure ---------------------------------------------------------- */
.figbox{background:var(--surface);border:1px solid var(--line);border-radius:3px;
  padding:18px 16px;margin:20px 0;overflow-x:auto}
.figbox svg{display:block;min-width:660px}
.figbox .cone{fill:var(--rul-soft);stroke:var(--rul);stroke-width:1.6}
.figbox ellipse.cone{fill:var(--rul-soft);stroke:var(--rul);stroke-width:1.2}
.figbox .dim{stroke:var(--chn);stroke-width:1.3}
.figbox .dim2{stroke:var(--fam);stroke-width:2.4}
.figbox .mk{fill:var(--chn)}
.figbox .gridl{stroke:var(--line);stroke-width:1}
.figbox .axis{stroke:var(--ink3);stroke-width:1.2}
.figbox .curve{fill:none;stroke:var(--chn);stroke-width:2.2}
.figbox .tang{fill:none;stroke:var(--rul);stroke-width:2.2}
.figbox .dot{fill:var(--rul);stroke:var(--surface);stroke-width:1.6}
.figbox text.lab{font-family:var(--mono);font-size:12px;fill:var(--ink);
  letter-spacing:.02em}
.figbox text.lab.hd{font-size:10.5px;letter-spacing:.1em;fill:var(--ink3)}
.figbox text.lab.sm{font-size:10.5px;fill:var(--ink3);letter-spacing:.03em}
.figbox text.lab.tk{font-size:10px;fill:var(--ink3)}
.figbox text.lab.am{fill:var(--rul);font-size:11.5px}
"""

# ---- build-time class-collision guard --------------------------------------
# The inherited slice is the WHOLE accumulated series stylesheet, so a name this
# page invents can silently pick up an upstream rule - Q10.2 shipped seven list
# items rendered one word wide exactly that way, with every layout gate passing.
# Rather than shadowing upstream rules by source order, NAMESPACE every name
# this page invents, and keep only the handful of deliberate series overrides.
SUFFIX = "111"
KEEP = {                                   # deliberate series overrides
    "wrap", "hdr", "eyebrow", "stand", "num", "note", "mono", "tscroll", "vtab",
    # already page-unique
    "tl111", "dr111", "cap111", "tree111",
    # figure internals, all scoped under .figbox
    "figbox", "lab", "hd", "sm", "tk", "am", "cone", "dim", "dim2", "mk",
    "gridl", "axis", "curve", "tang", "dot",
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

# now the guard, run on the RENAMED sheet: nothing this page invents may match
# a name already present upstream.
mine2 = set(re.findall(r"\.([A-Za-z][A-Za-z0-9_-]*)", EXTRA))
collisions = sorted(c for c in mine2
                    if c not in KEEP and re.search(r"\." + re.escape(c) + r"(?![A-Za-z0-9_-])",
                                                   INHERITED))
assert not collisions, "class names collide with the inherited slice: %r" % collisions
# and prove the guard can bite
assert re.search(r"\.wrap(?![A-Za-z0-9_-])", INHERITED), "guard control: .wrap must be upstream"
print("class-collision guard: %d names namespaced, %d deliberate overrides, 0 collisions"
      % (len(rename), len(KEEP)))

# the tokens EXTRA leans on must actually exist in the inherited slice
for tok in ("--rul", "--chn", "--los", "--fam", "--num", "--line", "--surface",
            "--ink", "--ink2", "--ink3", "--mono", "--rul-soft", "--los-soft",
            "--fam-soft"):
    assert tok + ":" in INHERITED, "token %s is not defined in the inherited slice" % tok
print("token guard: 14 tokens confirmed defined upstream")

style = style + EXTRA + "\n</style>"

body = io.open(os.path.join(HERE, "_q111_body.html"), encoding="utf-8").read()
body = _rn_html(body)
svg = _q111_fig.build()                    # the figure keeps the KEEP names
assert "FIGURE_SVG" in body
body = body.replace("FIGURE_SVG", svg)

# every class the body uses must now be defined somewhere, upstream or here
used = set()
for m in re.finditer(r'class="([^"]*)"', body):
    used.update(m.group(1).split())
sheet = INHERITED + EXTRA
undefined = sorted(c for c in used
                   if not re.search(r"\." + re.escape(c) + r"(?![A-Za-z0-9_-])", sheet))
assert not undefined, "classes used in the body with no rule anywhere: %r" % undefined
print("orphan-class guard: %d distinct classes used, all defined" % len(used))

page = head + "\n" + style + "\n" + body + "\n"

# ---- dash + control-character gate, BEFORE the file reaches disk -----------
BAD = ["&" + "mdash;", "&" + "ndash;", "&#8212;", "&#8211;", "&#x2014;", "&#x2013;",
       chr(0x2014), chr(0x2013)]
found = {b: page.count(b) for b in BAD if page.count(b)}
assert not found, "dash spellings present: %r" % found
ctrl = sorted({hex(ord(c)) for c in page if ord(c) < 32 and c not in "\n\r\t"})
assert not ctrl, "control characters present: %r" % ctrl
# The head configures displayMath as $$ ONLY.  A bracket-delimited block
# ships as visible raw LaTeX and NO layout gate reports it - found on this
# page's first render, in section 05.
cfg = re.search(r"displayMath:\s*(\[\[.*?\]\])", head)
assert cfg and "$$" in cfg.group(1), "display delimiters are not $$"
bodyonly = page[page.index("<main"):]
assert chr(92) + "[" not in bodyonly, "bracket-delimited display math will not typeset"
assert bodyonly.count("$$") % 2 == 0 and bodyonly.count("$$") >= 2, "unbalanced $$"
print("mathjax delimiter gate: %d display blocks, all $$-delimited"
      % (bodyonly.count("$$") // 2))
assert page.count("<style>") == 1 and page.count("</style>") == 1
assert page.count("<main") == 1 and page.count("</main>") == 1
assert "figbox" in page and "text class=\"lab" in page

io.open(OUT, "w", encoding="utf-8", newline="\n").write(page)
print("wrote", OUT, len(page), "bytes")
print("dash gate: 0 across all 8 spellings; control characters: none")
