"""Build the Q15.3 artifact page.

Inherits the accumulated series head + stylesheet by SLICING the Q15.2 page,
then appends this page's own EXTRA block. Every guard the carryover records
runs at build time, so a dirty page never reaches disk:

  SLICE guard          - the slice starts with <title>, ends with </style>,
                         and carries exactly FOUR <style> blocks. Q15.2
                         asserted three and predicted four; expect five next.
  TOKEN guard          - every var(--x) the page leans on is defined
  COLLISION guard      - every class this page invents is absent upstream
  KEEP-INTEGRITY guard - every exemption really is an upstream series name
  ORPHAN-CLASS guard   - every class the body uses has a rule somewhere
  FIGURE-NAME guard    - the generated SVG emits only 153-suffixed classes
                         plus `lab`, the svg-labels hook, and every styled
                         figure class is actually EMITTED (the reverse check)
  ELEMENT-INHERITANCE  - the element/property pairs this page relies on
                         upstream are checked, with a removal probe
  BRACKET-MATH guard   - no \\[ survives, and $$ is balanced
  INLINE-MATH guard    - the head configures \\( \\) for inline math and NOT
                         $, so no bare single $ may survive in the body
  MATH-COLOUR guard    - every coloured cell class that can hold maths has a
                         `color:inherit; fill:currentColor` rule for the
                         MathJax container inside it (carryover 16.7)
  DASH-ENTITY guard    - none of the eight dash spellings is present
  CONTROL-CHAR guard   - no stray control characters
"""
import sys

sys.dont_write_bytecode = True

import io
import os
import re

import _q153_fig

HERE = os.path.dirname(os.path.abspath(__file__))
ART = os.path.dirname(HERE)
SRC = os.path.join(ART, "Q15.2-least-perimeter-open-domain.html")
OUT = os.path.join(ART, "Q15.3-extreme-value-theorem.html")
BODY = os.path.join(HERE, "_q153_body.html")

TITLE = "Existence Is Not Location"

# ---- genuine SERIES names this page reuses. Each is asserted present
# ---- upstream below, so the exemption list cannot silently widen.
KEEP_SERIES = [
    "wrap", "mast", "main", "eyebrow", "stand", "note", "tscroll", "vtab",
    "figbox", "lab", "pgrid", "pcard", "pk", "pv", "pd", "kbd",
    "los", "fam",
]

# element/property pairs this page LEANS ON upstream
ELEMENT_INHERITANCE = [
    (r"\.wrap\s*\{[^}]*max-width", "wrap max-width"),
    (r"\.tscroll\s*\{[^}]*overflow-x", "tscroll overflow-x"),
    (r"\.pgrid\s*\{[^}]*grid", "pgrid grid"),
]

# coloured cell/card classes that CAN contain inline maths, and therefore
# need the MathJax colour-inheritance rule. Asserted below.
COLOURED_MATH = ["hi153", "pos153", "neg153", "bad153", "hid153", "ok153",
                 "non153", "win153", "two153", "dr153c", "fh153"]

STYLE_EXTRA = r"""
<style>
/* ===== Q15.3 EXTRA =========================================================
   Q15.3 is the only question in the course whose stem NAMES the Extreme
   Value Theorem, so the theorem itself is the object under examination.
   What the five series hues mean on this page:

     THE ANSWER, the two extreme values and the minimum level   --rul amber
     THE MACHINERY, the derivative, the candidate rows,
       the hypothesis checks that pass                          --chn slate
     WHERE MARKS DIE, a dropped hypothesis, an unattained
       extreme, a mutilation that HIDES                          --los terracotta
     THE VARIATION families and the checks that catch things    --fam teal
     NUMERICS: provenance, counts, gates                        --num mauve

   The signature block is panel A in section 04: the curve on [-1,1] with a
   dashed level line at y = 1/2 running the full width of the frame, so the
   two minimum markers are visibly at the SAME height at the two ends. That
   tie is why both endpoint omissions HIDE, which is the run's headline.

   Panel B is three sub-panels of the SAME function with one hypothesis
   dropped in each. A HOLLOW marker means an extreme that is approached and
   never attained; the distinction between hollow and filled is the whole
   figure.
   ======================================================================== */

/* ---- section numbers -------------------------------------------------- */
.sn153{ font-family:var(--mono); font-size:.62em; font-weight:600;
  letter-spacing:.09em; color:var(--num); vertical-align:.32em;
  margin-right:.55em; }
h3.sh153{ font-size:15.5px; letter-spacing:.005em; margin:30px 0 10px;
  color:var(--ink); font-weight:600; }

/* ---- the quoted stem -------------------------------------------------- */
p.quote153{ margin:16px 0 20px; padding:15px 18px; border-radius:2px;
  background:var(--sunk); border-left:3px solid var(--accent-line);
  color:var(--ink); line-height:1.66; }
.qp153{ display:block; margin-top:10px; font-family:var(--mono);
  font-size:.88em; line-height:1.6; color:var(--ink3); }

/* ---- the one-line pull quote: this page's three load-bearing lines ---- */
p.pull153{ margin:22px 0; padding:14px 18px 14px 20px;
  border-left:3px solid var(--rul); background:var(--rul-soft);
  color:var(--ink); font-size:15.5px; line-height:1.6; border-radius:2px; }

/* ---- tables ----------------------------------------------------------- */
table.ans153, table.hyp153, table.ce153, table.loc153, table.cand153,
table.rc153, table.cens153, table.bnd153, table.fam153, table.dr153,
table.ae153, table.pv153t{
  width:100%; border-collapse:collapse; font-size:14px; min-width:700px; }
table.fam153, table.dr153, table.ce153{ min-width:980px; }
table.cens153{ min-width:880px; }
/* rc153's label column squeezed to 127px at the 430px case, wrapping a
   six-word label onto four lines. lint.mjs found it only AFTER a MathJax
   span was removed from one of that table's HEADERS: the span had been
   holding a column open, so the widths redistributed and this one
   collapsed. A wide table's min-width is a lint INPUT, not a style
   choice. 880 was not enough; 1000 plus an explicit floor is. */
table.rc153{ min-width:1000px; }
table.rc153 td:first-child, table.rc153 th:first-child{
  min-width:178px; }
table.bnd153{ min-width:820px; }
table.ae153, table.pv153t, table.loc153{ min-width:560px; }
table.ans153 th, table.hyp153 th, table.ce153 th, table.loc153 th,
table.cand153 th, table.rc153 th, table.cens153 th, table.bnd153 th,
table.fam153 th, table.dr153 th, table.ae153 th, table.pv153t th{
  text-align:left; font-family:var(--mono); font-size:10.5px;
  letter-spacing:.085em; text-transform:uppercase; color:var(--ink3);
  font-weight:600; padding:9px 12px; border-bottom:1px solid var(--line);
  vertical-align:bottom; }
table.ans153 td, table.hyp153 td, table.ce153 td, table.loc153 td,
table.cand153 td, table.rc153 td, table.cens153 td, table.bnd153 td,
table.fam153 td, table.dr153 td, table.ae153 td, table.pv153t td{
  padding:10px 12px; border-bottom:1px solid var(--line-soft);
  vertical-align:top; line-height:1.52; }
td.dl153{ font-weight:600; color:var(--ink); }
td.hi153, tr.hi153 > td{ background:var(--rul-soft); color:var(--ink); }
td.hi153{ font-weight:600; }
td.mono153, span.mono153{ font-family:var(--mono); font-size:12.6px;
  font-variant-numeric:tabular-nums; }
/* a long Windows path carries no break opportunity - a backslash is not
   one - so an inline mono span holding one is an unbreakable token that
   pushes the DOCUMENT sideways at the 430px lint case. */
span.mono153, p.cap153{ overflow-wrap:anywhere; }
td.non153{ font-family:var(--mono); font-size:12.2px; letter-spacing:.06em;
  text-transform:uppercase; color:var(--ink3); font-weight:600; }
td.two153{ font-family:var(--mono); font-size:12.2px; letter-spacing:.07em;
  text-transform:uppercase; color:var(--rul); font-weight:600;
  background:var(--rul-soft); }
td.ok153{ color:var(--fam); }
td.pos153{ color:var(--fam); font-weight:600; }
td.neg153{ color:var(--los); font-weight:600; }
td.bad153{ background:var(--los-soft); color:var(--los); font-weight:600;
  font-family:var(--mono); font-size:11.6px; letter-spacing:.05em;
  text-transform:uppercase; }
td.hid153{ background:var(--num-soft); color:var(--num); font-weight:600;
  font-family:var(--mono); font-size:11.6px; letter-spacing:.05em;
  text-transform:uppercase; }
td.dr153c{ color:var(--los); font-weight:600; font-family:var(--mono);
  font-size:11.8px; letter-spacing:.05em; text-transform:uppercase; }
td.win153{ color:var(--rul); font-weight:600; font-family:var(--mono);
  font-size:11.6px; letter-spacing:.06em; text-transform:uppercase; }
td.fh153{ font-family:var(--mono); font-size:11.4px; font-weight:600;
  letter-spacing:.055em; text-transform:uppercase; color:var(--fam);
  background:var(--fam-soft); }

/* MathJax does NOT inherit its container's colour - upstream sets
   mjx-container{color:var(--mj)} - so every coloured cell holding inline
   maths would render ink-white beside teal or terracotta text in the same
   phrase. No gate sees this; only the screenshot does. Fix all the classes
   at once. Carryover 16.7. */
td.hi153 mjx-container, td.pos153 mjx-container, td.neg153 mjx-container,
td.bad153 mjx-container, td.hid153 mjx-container, td.ok153 mjx-container,
td.non153 mjx-container, td.win153 mjx-container, td.two153 mjx-container,
td.dr153c mjx-container, td.fh153 mjx-container,
td.hi153 mjx-container svg, td.pos153 mjx-container svg,
td.neg153 mjx-container svg, td.bad153 mjx-container svg,
td.hid153 mjx-container svg, td.ok153 mjx-container svg,
td.non153 mjx-container svg, td.win153 mjx-container svg,
td.two153 mjx-container svg, td.dr153c mjx-container svg,
td.fh153 mjx-container svg{ color:inherit; fill:currentColor; }
.pull153 mjx-container, .pull153 mjx-container svg,
.hl153 mjx-container, .hl153 mjx-container svg{
  color:inherit; fill:currentColor; }

/* ---- the model write-up, with the four scoring phrases lifted -------- */
div.wu153{ margin:18px 0 20px; padding:16px 20px; border-radius:2px;
  background:var(--sunk); border-left:3px solid var(--fam);
  display:flex; flex-direction:column; gap:9px; }
div.wu153 > p{ margin:0; line-height:1.66; color:var(--ink); }
span.hl153{ background:var(--fam-soft); color:var(--fam); font-weight:600;
  padding:1px 4px; border-radius:2px; }

/* ---- numbered lists: ONE content child at grid column 2 -------------- */
ol.traps153, ol.def153, ol.cr153{ list-style:none; counter-reset:s153;
  margin:18px 0 4px; padding:0; display:flex; flex-direction:column;
  gap:1px; background:var(--line-soft); border-radius:2px;
  overflow:hidden; }
ol.traps153 > li, ol.def153 > li, ol.cr153 > li{
  counter-increment:s153; display:grid;
  grid-template-columns:38px minmax(0,1fr); align-items:start;
  background:var(--surface); padding:12px 14px; }
ol.traps153 > li::before, ol.def153 > li::before, ol.cr153 > li::before{
  content:counter(s153); grid-column:1; font-family:var(--mono);
  font-size:11px; font-weight:600; letter-spacing:.06em;
  color:var(--accent); padding-top:.3em; }
ol.traps153 > li > span, ol.def153 > li > span, ol.cr153 > li > span{
  grid-column:2; line-height:1.6; color:var(--ink2); }

/* ---- card grids -------------------------------------------------------
   NOT auto-fit. `repeat(auto-fit, minmax(...))` picks whatever track
   count fits and knows nothing about how many cells it must place, so it
   produced a 2-track row for 3 cards at vp 620 and a 3-track row for 4
   cards from vp 860 to 1010 - three ragged grids, all found by
   grid-fill.mjs and by nothing else. For any floor there is some
   viewport where the bad count fits, so the only reliable fix is to
   enumerate track counts that DIVIDE the cell count and skip the rest.

     .two153g   2 cards  ->  1 or 2 tracks
     .three153  3 cards  ->  1 or 3      (2 is never used)
     .cs153     3 cards  ->  1 or 3      (2 is never used)
     .ck153     4 cards  ->  1, 2 or 4   (3 is never used)

   Content width is at most 1080 - 44 = 1036px, so each card gets 358px
   at 2-up, 285px at 3-up (vp 900) and 259px at 4-up (vp 1100).
   ---------------------------------------------------------------------- */
.pgrid.two153g, .pgrid.three153, .pgrid.cs153, .pgrid.ck153{
  grid-template-columns:minmax(0,1fr); }
@media (min-width:760px){
  .pgrid.two153g{ grid-template-columns:repeat(2,minmax(0,1fr)); }
  .pgrid.ck153{ grid-template-columns:repeat(2,minmax(0,1fr)); }
}
@media (min-width:900px){
  .pgrid.three153{ grid-template-columns:repeat(3,minmax(0,1fr)); }
  .pgrid.cs153{ grid-template-columns:repeat(3,minmax(0,1fr)); }
}
@media (min-width:1100px){
  .pgrid.ck153{ grid-template-columns:repeat(4,minmax(0,1fr)); }
}

/* ---- figures ---------------------------------------------------------- */
.figbox svg.fig153{ width:100%; height:auto; display:block; }
p.cap153, figcaption.cap153{ margin:10px 2px 0; font-size:13px;
  line-height:1.58; color:var(--ink3); }

.figbox rect.pbox153{ fill:none; stroke:var(--line); stroke-width:1; }
.figbox line.gridv153, .figbox line.gridh153{ stroke:var(--line-soft);
  stroke-width:1; }
.figbox line.ivl153{ stroke:var(--accent); stroke-width:3.5; }
.figbox line.lev153{ stroke:var(--rul); stroke-width:1.4;
  stroke-dasharray:6 4; }
.figbox polyline.crv153{ fill:none; stroke:var(--chn); stroke-width:2.4; }
.figbox polyline.ghost153{ fill:none; stroke:var(--line);
  stroke-width:1.4; stroke-dasharray:2 3; }
.figbox line.inf153{ stroke:var(--num); stroke-width:1.8; }
.figbox circle.mx153{ fill:var(--rul); stroke:var(--surface); stroke-width:1.6; }
.figbox circle.mn153{ fill:var(--rul); stroke:var(--surface); stroke-width:1.6; }
.figbox circle.opn153{ fill:var(--surface); stroke:var(--los);
  stroke-width:2.2; }

.figbox text.lab{ font-family:var(--mono); fill:var(--ink3);
  font-size:11px; letter-spacing:.05em; }
.figbox text.labmx153{ fill:var(--rul); font-size:11.5px;
  font-weight:600; text-anchor:middle; }
.figbox text.labl153{ fill:var(--rul); font-size:11.5px;
  font-weight:600; }
.figbox text.labr153{ fill:var(--rul); font-size:11.5px; font-weight:600;
  text-anchor:end; }
.figbox text.labtie153{ fill:var(--ink3); font-size:11px;
  text-anchor:middle; }
.figbox text.tx153{ text-anchor:middle; }
.figbox text.ty153{ text-anchor:end; }
.figbox text.lgd153{ fill:var(--ink3); font-size:11px; }
.figbox text.sub153{ fill:var(--ink); font-size:11.5px; font-weight:600;
  letter-spacing:.07em; }
.figbox text.cap153{ fill:var(--ink3); font-size:10.5px; }
.figbox text.arw153{ fill:var(--ink3); font-size:10.5px;
  text-anchor:middle; }
.figbox rect.swcrv153{ fill:var(--chn); }
.figbox rect.swghost153{ fill:var(--line); }
.figbox rect.swlev153{ fill:var(--rul); }
.figbox rect.swinf153{ fill:var(--num); }
</style>
"""


def die(msg):
    raise SystemExit("BUILD FAILED: " + msg)


def main():
    src = io.open(SRC, encoding="utf-8").read()
    lines = src.splitlines(True)

    # ---- SLICE guard -----------------------------------------------------
    close = [i for i, l in enumerate(lines) if "</style>" in l]
    if len(close) != 4:
        die("expected FOUR style blocks upstream, found %d" % len(close))
    head_end = close[-1] + 1
    head = "".join(lines[:head_end])
    if not head.startswith("<title>"):
        die("slice does not start with <title>")
    if not head.rstrip().endswith("</style>"):
        die("slice does not end with </style>")
    if head.count("<style>") != 4:
        die("slice should carry exactly four <style> blocks, found %d"
            % head.count("<style>"))
    head = re.sub(r"^<title>[^<]*</title>",
                  "<title>" + TITLE + "</title>", head, count=1)
    if "<title>" + TITLE + "</title>" not in head:
        die("title substitution did not land")

    upstream_css = head[head.find("<style>"):]
    upstream_nocomment = re.sub(r"/\*.*?\*/", "", upstream_css, flags=re.S)

    body = io.open(BODY, encoding="utf-8").read()

    # ---- FIGURE-NAME guard -----------------------------------------------
    figa, figb = _q153_fig.build()
    both = figa + figb
    for bad in ("fill=", "stroke=", "font-size=", "var(--", "style="):
        if bad in both:
            die("presentation attribute leaked into the SVG: " + bad)
    fig_classes = set()
    for m in re.finditer(r'class="([^"]+)"', both):
        fig_classes.update(m.group(1).split())
    bare = sorted(c for c in fig_classes if not c.endswith("153"))
    if bare != ["lab"]:
        die("the SVG must emit exactly one bare class, 'lab'; got %r" % bare)
    if not re.search(r"\.figbox\s+text\.lab\s*\{", STYLE_EXTRA):
        die("no rule for the gate's own hook class 'lab'")
    for c in fig_classes:
        if c.startswith("grid") and not re.search(r"grid|axis", c):
            die(c + " will not get the svg-labels exemption")
    if "gridl" in fig_classes or "axis" in fig_classes:
        die("'gridl'/'axis' carry upstream PAINT; use a grid*153 name")
    for c in sorted(fig_classes):
        if c == "lab":
            continue
        if not re.search(r"\.%s\b" % re.escape(c), STYLE_EXTRA):
            die("figure class .%s has no rule in EXTRA" % c)
    # the REVERSE check: every class styled under .figbox must be EMITTED.
    # A rule for a shape the generator no longer draws is drift, and it is
    # how a legend swatch keyed to nothing survives a rewrite.
    styled_fig = set(re.findall(r"\.figbox\s+(?:rect|line|circle|polyline"
                                r"|text|svg)\.([A-Za-z][A-Za-z0-9_-]*)",
                                STYLE_EXTRA))
    unemitted = sorted(styled_fig - fig_classes)
    if unemitted:
        die("EXTRA styles figure classes the generator never emits: %r"
            % unemitted)

    body = body.replace("<!--FIGA-->", figa).replace("<!--FIGB-->", figb)
    if "<!--FIG" in body:
        die("a figure placeholder survived")

    page = head + STYLE_EXTRA + "\n" + body

    # ---- COLLISION guard --------------------------------------------------
    own = sorted(set(re.findall(r"\.([A-Za-z][A-Za-z0-9_-]*153[a-z]?)",
                                STYLE_EXTRA)))
    if not own:
        die("no namespaced classes found in EXTRA")
    for c in own:
        if re.search(r"\.%s\b" % re.escape(c), upstream_nocomment):
            die("collision: .%s already exists upstream" % c)

    # ---- KEEP-INTEGRITY guard --------------------------------------------
    for c in KEEP_SERIES:
        if not re.search(r"\.%s\b" % re.escape(c), upstream_nocomment):
            die("KEEP name .%s is NOT present upstream, so it is an "
                "exemption no guard covers" % c)

    # ---- ORPHAN-CLASS guard ----------------------------------------------
    body_classes = set()
    for m in re.finditer(r'class="([^"]+)"', body):
        body_classes.update(m.group(1).split())
    extra_nocomment = re.sub(r"/\*.*?\*/", "", STYLE_EXTRA, flags=re.S)
    all_css = upstream_nocomment + extra_nocomment
    orphans = [c for c in sorted(body_classes)
               if not re.search(r"\.%s\b" % re.escape(c), all_css)]
    if orphans:
        die("orphan classes with no CSS rule anywhere: %r" % orphans)
    unexempt = sorted(c for c in body_classes
                      if not re.search(r"153[a-z]?$", c)
                      and c not in KEEP_SERIES)
    if unexempt:
        die("body classes neither namespaced nor in KEEP: %r" % unexempt)

    # ---- MATH-COLOUR guard ------------------------------------------------
    for c in COLOURED_MATH:
        if not re.search(r"\.%s\s+mjx-container\b" % re.escape(c),
                         STYLE_EXTRA):
            die("coloured class .%s can hold maths and has no "
                "mjx-container colour rule" % c)
        if not re.search(r"\.%s\s+mjx-container\s+svg\b" % re.escape(c),
                         STYLE_EXTRA):
            die("coloured class .%s has no mjx-container svg fill rule" % c)
    if "fill:currentColor" not in STYLE_EXTRA:
        die("the mjx colour rule does not set fill:currentColor")
    # and the rule must be REACHED: assert upstream really does paint
    # mjx-container, which is what makes it necessary
    if not re.search(r"mjx-container\s*\{[^}]*color", upstream_nocomment,
                     flags=re.S):
        die("upstream does not paint mjx-container, so this guard is "
            "protecting against something that cannot happen")

    # ---- ELEMENT-INHERITANCE guard, with a removal probe -----------------
    for pat, label in ELEMENT_INHERITANCE:
        if not re.search(pat, upstream_nocomment, flags=re.S):
            die("this page relies on upstream '%s' and it is absent" % label)
    probe = re.sub(r"\.tscroll\s*\{[^}]*\}", "", upstream_nocomment,
                   flags=re.S)
    if re.search(r"\.tscroll\s*\{[^}]*overflow-x", probe, flags=re.S):
        die("the element-inheritance removal probe did not fire, so the "
            "guard is not measuring anything")

    # ---- TOKEN guard ------------------------------------------------------
    used = sorted(set(re.findall(r"var\((--[a-z0-9-]+)\)", page)))
    defined = set(re.findall(r"(--[a-z0-9-]+)\s*:", upstream_nocomment))
    defined |= set(re.findall(r"(--[a-z0-9-]+)\s*:", extra_nocomment))
    missing = [t for t in used if t not in defined]
    if missing:
        die("var() tokens used but never defined: %r" % missing)

    # ---- BRACKET-MATH guard ----------------------------------------------
    cfg = re.search(r"displayMath:\s*\[\[([^\]]*)\]\]", page)
    if not cfg:
        die("could not read the MathJax displayMath config")
    if "$$" not in cfg.group(1):
        die("displayMath is not configured for $$")
    if "\\[" in body or "\\]" in body:
        die("bracket display math in the body would ship as raw LaTeX")
    if body.count("$$") % 2 != 0:
        die("unbalanced $$ in the body: %d" % body.count("$$"))

    # ---- INLINE-MATH guard ------------------------------------------------
    icfg = re.search(r"inlineMath:\s*\[\[([^\]]*)\]\]", page)
    if not icfg:
        die("could not read the MathJax inlineMath config")
    if "$" in icfg.group(1).replace("\\\\(", "").replace("\\\\)", ""):
        die("inlineMath appears to accept $, which this guard assumes it "
            "does not")
    stripped = body.replace("$$", "")
    if "$" in stripped:
        die("%d bare single dollars in the body would ship as VISIBLE raw "
            "LaTeX, because the head configures \\( \\) for inline math"
            % stripped.count("$"))
    if body.count("\\(") != body.count("\\)"):
        die("unbalanced inline math delimiters: %d open, %d close"
            % (body.count("\\("), body.count("\\)")))

    # ---- DASH-ENTITY guard, all eight spellings --------------------------
    dashes = ["&" + "mdash;", "&" + "ndash;", "&#8212;", "&#8211;",
              "&#x2014;", "&#x2013;", chr(0x2014), chr(0x2013)]
    hits = [d for d in dashes if d in page]
    if hits:
        die("dash spellings present: %r" % hits)

    # ---- CONTROL-CHAR guard ----------------------------------------------
    ctrl = sorted({hex(ord(ch)) for ch in page
                   if ord(ch) < 32 and ch not in "\n\r\t"})
    if ctrl:
        die("control characters in the page: %r" % ctrl)

    io.open(OUT, "w", encoding="utf-8", newline="\n").write(page)
    print("wrote %s" % OUT)
    print("  bytes            %d" % len(page.encode("utf-8")))
    print("  style blocks     4 upstream + 1 EXTRA")
    print("  namespaced       %d" % len(own))
    print("  KEEP exemptions  %d (each proved present upstream)"
          % len(KEEP_SERIES))
    print("  ratio            %d renamed against %d exempt"
          % (len(own), len(KEEP_SERIES)))
    print("  body classes     %d, 0 orphans, 0 unexempt" % len(body_classes))
    print("  var() tokens     %d used, 0 undefined" % len(used))
    print("  figure classes   %d, 1 bare ('lab'), all styled AND emitted"
          % len(fig_classes))
    print("  math-colour      %d coloured classes guarded"
          % len(COLOURED_MATH))
    print("  inline math      %d \\( \\) pairs, 0 bare dollars"
          % body.count("\\("))
    print("  display math     %d $$ pairs" % (body.count("$$") // 2))
    print("  dash spellings   0 of 8")
    print("  all guards passed")


if __name__ == "__main__":
    main()
