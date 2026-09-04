"""Build the Q15.4 artifact page.

Inherits the accumulated series head + stylesheet by SLICING the Q15.3 page,
then appends this page's own EXTRA block. Every guard the carryover records
runs at build time, so a dirty page never reaches disk:

  SLICE guard          - the slice starts with <title>, ends with </style>,
                         and carries exactly FIVE <style> blocks. Q15.3
                         asserted four and predicted five; expect six next.
  TOKEN guard          - every var(--x) the page leans on is defined
  COLLISION guard      - every class this page invents is absent upstream
  KEEP-INTEGRITY guard - every exemption really is an upstream series name
  ORPHAN-CLASS guard   - every class the body uses has a rule somewhere
  FIGURE-NAME guard    - the generated SVG emits only 154-suffixed classes
                         plus `lab`, the svg-labels hook, and every styled
                         figure class is actually EMITTED (the reverse check)
  ELEMENT-INHERITANCE  - the element/property pairs this page relies on
                         upstream are checked, with a removal probe
  BRACKET-MATH guard   - no bracket display math survives, and $$ is balanced
  INLINE-MATH guard    - the head configures inline math with parentheses and
                         NOT with a dollar, so no bare single dollar may
                         survive in the body
  MATH-COLOUR guard    - every coloured cell class that can hold maths has a
                         color:inherit / fill:currentColor rule for the
                         MathJax container inside it (carryover 16.7)
  GRID-COUNT guard     - every grid this page defines uses ENUMERATED
                         breakpoints whose track counts DIVIDE the cell
                         count, never repeat(auto-fit, minmax(...)), which
                         cannot satisfy that rule over a continuous range
                         (carryover 17.6, which supersedes 15.6)
  DASH-ENTITY guard    - none of the eight dash spellings is present
  CONTROL-CHAR guard   - no stray control characters
"""
import sys

sys.dont_write_bytecode = True

import io
import os
import re

import _q154_fig

HERE = os.path.dirname(os.path.abspath(__file__))
ART = os.path.dirname(HERE)
SRC = os.path.join(ART, "Q15.3-extreme-value-theorem.html")
OUT = os.path.join(ART, "Q15.4-cheapest-rectangular-box.html")
BODY = os.path.join(HERE, "_q154_body.html")

TITLE = "Not A Cube"

KEEP_SERIES = [
    "wrap", "mast", "main", "eyebrow", "stand", "note", "tscroll", "vtab",
    "figbox", "lab", "pgrid", "pcard", "pk", "pv", "pd", "kbd",
    "los", "fam",
]

ELEMENT_INHERITANCE = [
    (r"\.wrap\s*\{[^}]*max-width", "wrap max-width"),
    (r"\.tscroll\s*\{[^}]*overflow-x", "tscroll overflow-x"),
    (r"\.pgrid\s*\{[^}]*grid", "pgrid grid"),
]

COLOURED_MATH = ["hi154", "los154", "ok154", "bad154", "non154", "win154",
                 "fk154", "dl154", "mono154"]

# every grid this page defines, with the cell counts it must place. The
# GRID-COUNT guard reads the media queries out of EXTRA and checks that
# every track count offered divides every cell count.
GRIDS = {"two154g": [2], "three154g": [3]}

# legend swatch -> the drawn class it keys. The SWATCH-DASH guard reads the
# curve's own CSS rule and demands a two-piece swatch for a dashed line.
SWATCH_CURVE = {
    "swcrv154": "crv154",
    "swc1154": "c1154",
    "swc2154": "c2154",
    "swlev154": "lev154",
}

STYLE_EXTRA = r"""
<style>
/* ===== Q15.4 EXTRA =========================================================
   Q15.4 is the second and heavier of the two open-domain questions, and the
   only one in the course whose objective is NOT symmetric in all of its
   variables. So the page's job is to take away a prior rather than to add a
   method: the answer is 2 : 4 : 3, not a cube, and the cube is cheaper.

   What the five series hues mean on this page:

     THE ANSWER, the four reported numbers, the minimum level   --rul amber
     THE MACHINERY, the faces, the rates, the derivative rows   --chn slate
     WHERE MARKS DIE, a misread rate, a mutilation that HIDES,
       the absent maximum                                        --los terracotta
     THE VARIATION families and the checks that catch things    --fam teal
     NUMERICS: provenance, counts, gates                        --num mauve

   The signature block is panel A in section 04. The two component curves
   are drawn together with the total, and a single tie line at one width
   joins the two component markers through the minimum: that is the 1 : 2
   ratio, which is this objective's cheap self-check and is a DIFFERENT
   number from Q15.2's 1 : 1. The frame's left and right edges are dashed
   because the domain has no endpoint, which is the one thing the picture
   can say that a table cannot.

   NO text sits inside either plotting frame. Q15.3's round-2 svg-labels
   finding was that a domain marker is an axis annotation, not a curve
   feature; the conclusion generalises to every callout, so this page's
   labels live in bands below each frame and the collision surface is empty
   by construction.
   ======================================================================== */

/* ---- section numbers and sub-headings --------------------------------- */
.sn154{ font-family:var(--mono); font-size:.62em; font-weight:600;
  letter-spacing:.09em; color:var(--num); vertical-align:.32em;
  margin-right:.55em; }
h3.sh154{ font-size:15.5px; letter-spacing:.005em; margin:30px 0 10px;
  color:var(--ink); font-weight:600; }

/* ---- the quoted stem -------------------------------------------------- */
p.quote154{ margin:16px 0 20px; padding:15px 18px; border-radius:2px;
  background:var(--sunk); border-left:3px solid var(--accent-line);
  color:var(--ink); line-height:1.66; }
.qp154{ display:block; margin-top:10px; font-family:var(--mono);
  font-size:.88em; line-height:1.6; color:var(--ink3); }

/* ---- the pull quote: this page's load-bearing lines -------------------- */
p.pull154{ margin:22px 0; padding:14px 18px 14px 20px;
  border-left:3px solid var(--rul); background:var(--rul-soft);
  color:var(--ink); font-size:15.5px; line-height:1.6; border-radius:2px; }

/* ---- the answer-entry strip ------------------------------------------- */
p.entry154{ margin:18px 0; padding:13px 16px; border-radius:2px;
  background:var(--surface2); border:1px solid var(--line);
  color:var(--ink2); font-size:14px; line-height:1.72; }

/* ---- the exam write-up, set as a transcript ---------------------------- */
p.script154{ margin:18px 0; padding:16px 18px; border-radius:2px;
  background:var(--sunk); border-left:3px solid var(--chn);
  color:var(--ink); font-size:14.5px; line-height:1.9; }

/* ---- a display equation gets its own scroll container ------------------ */
p.dspwrap154{ margin:20px 0; overflow-x:auto; }

/* ---- figure captions --------------------------------------------------- */
p.fcap154{ margin:10px 0 26px; font-size:13.5px; line-height:1.66;
  color:var(--ink3); }

/* ---- tables ------------------------------------------------------------ */
table.ans154, table.cube154t, table.rate154, table.dim154, table.jus154,
table.chk154, table.rat154, table.cens154, table.fam154t, table.cap154t,
table.ver154{
  width:100%; border-collapse:collapse; font-size:14px; min-width:720px; }
table.fam154t, table.ver154, table.jus154{ min-width:1000px; }
table.cens154, table.cap154t{ min-width:880px; }
table.ans154{ min-width:820px; }
/* a wide table's min-width is a lint INPUT, not a style choice: the first
   column of ver154 wraps its six-word label onto four lines at 430px unless
   it carries an explicit floor. */
table.ver154 td:first-child, table.ver154 th:first-child{ min-width:96px; }
table.fam154t td:first-child, table.fam154t th:first-child{ min-width:186px; }
table.ans154 th, table.cube154t th, table.rate154 th, table.dim154 th,
table.jus154 th, table.chk154 th, table.rat154 th, table.cens154 th,
table.fam154t th, table.cap154t th, table.ver154 th{
  text-align:left; font-family:var(--mono); font-size:10.5px;
  letter-spacing:.09em; text-transform:uppercase; color:var(--ink3);
  font-weight:600; padding:9px 12px; border-bottom:1px solid var(--line);
  white-space:nowrap; }
table.ans154 td, table.cube154t td, table.rate154 td, table.dim154 td,
table.jus154 td, table.chk154 td, table.rat154 td, table.cens154 td,
table.fam154t td, table.cap154t td, table.ver154 td{
  padding:9px 12px; border-bottom:1px solid var(--line-soft);
  color:var(--ink2); vertical-align:top; line-height:1.6; }

/* ---- semantic cells ---------------------------------------------------- */
.dl154{ color:var(--ink); }
.mono154{ font-family:var(--mono); font-size:.92em;
  font-variant-numeric:tabular-nums; color:var(--ink2); }
.hi154{ color:var(--rul); font-weight:600; }
.win154{ color:var(--rul); font-weight:600; }
.los154{ color:var(--los); }
.bad154{ color:var(--los); }
.ok154{ color:var(--ok); }
.non154{ color:var(--chn); }
.fk154{ color:var(--fam); font-family:var(--mono); font-size:.9em;
  white-space:nowrap; }

/* MathJax does NOT inherit its container's colour: upstream paints
   mjx-container with var(--mj), so a coloured cell holding inline maths
   renders ink-white beside its own coloured words. Carryover 16.7. */
.hi154 mjx-container, .los154 mjx-container, .ok154 mjx-container,
.bad154 mjx-container, .non154 mjx-container, .win154 mjx-container,
.fk154 mjx-container, .dl154 mjx-container, .mono154 mjx-container{
  color:inherit; }
.hi154 mjx-container svg, .los154 mjx-container svg,
.ok154 mjx-container svg, .bad154 mjx-container svg,
.non154 mjx-container svg, .win154 mjx-container svg,
.fk154 mjx-container svg, .dl154 mjx-container svg,
.mono154 mjx-container svg{ fill:currentColor; }

/* ---- card grids. ENUMERATED breakpoints, never auto-fit ---------------
   repeat(auto-fit, minmax(X,1fr)) picks whatever track count fits and knows
   nothing about how many cells it must place, so for ANY floor there is a
   viewport where a bad count fits and a row is left ragged. The track counts
   below DIVIDE their cell counts by construction. Carryover 17.6. */
.two154g{ grid-template-columns:1fr; }
.three154g{ grid-template-columns:1fr; }
@media (min-width:760px){
  .two154g{ grid-template-columns:repeat(2,minmax(0,1fr)); }
}
@media (min-width:1000px){
  .three154g{ grid-template-columns:repeat(3,minmax(0,1fr)); }
}

/* ---- figures ------------------------------------------------------------
   Every drawn class is set HERE, never as an SVG presentation attribute:
   var() does not resolve in one, and an upstream rule beats one anyway. */
.figbox svg.fig154{ width:100%; height:auto; display:block; }
.figbox rect.pbox154{ fill:none; stroke:var(--line); stroke-width:1; }
.figbox line.gridv154, .figbox line.gridh154{
  stroke:var(--grid); stroke-width:1; }
.figbox line.gridopen154{ stroke:var(--los); stroke-width:2;
  stroke-dasharray:3 4; }
.figbox line.lev154{ stroke:var(--rul); stroke-width:1.4;
  stroke-dasharray:6 4; }
.figbox line.tie154{ stroke:var(--rul); stroke-width:1.4; }
.figbox polyline.crv154{ fill:none; stroke:var(--ink); stroke-width:2.2; }
.figbox polyline.c1154{ fill:none; stroke:var(--fam); stroke-width:1.6;
  stroke-dasharray:5 3; }
.figbox polyline.c2154{ fill:none; stroke:var(--chn); stroke-width:1.6;
  stroke-dasharray:5 3; }
.figbox circle.mn154{ fill:var(--rul); stroke:var(--surface);
  stroke-width:2; }
.figbox circle.cm1154{ fill:var(--fam); stroke:var(--surface);
  stroke-width:1.6; }
.figbox circle.cm2154{ fill:var(--chn); stroke:var(--surface);
  stroke-width:1.6; }
.figbox line.gnd154{ stroke:var(--line); stroke-width:1.4; }
.figbox polyline.ffbx154{ fill:var(--surface2); stroke:var(--ink3);
  stroke-width:1.3; }
.figbox polyline.ttbx154, .figbox polyline.ssbx154{
  fill:var(--sunk); stroke:var(--ink3); stroke-width:1.1; }
.figbox polyline.ffwin154{ fill:var(--rul-soft); stroke:var(--rul);
  stroke-width:1.8; }
.figbox polyline.ttwin154, .figbox polyline.sswin154{
  fill:var(--rul-soft); stroke:var(--rul); stroke-width:1.4; }
.figbox polyline.ffcube154, .figbox polyline.ttcube154,
.figbox polyline.sscube154{ fill:none; stroke:var(--los);
  stroke-width:1.4; stroke-dasharray:4 3; }
.figbox text.lab{ font-family:var(--mono); font-size:11px;
  fill:var(--plotlab); }
.figbox text.tx154{ text-anchor:middle; }
.figbox text.ty154{ text-anchor:end; }
.figbox text.lgd154, .figbox text.note154, .figbox text.bcap154{
  text-anchor:start; }
.figbox text.note154{ fill:var(--ink2); }
.figbox text.bw154, .figbox text.bh154{ text-anchor:middle; }
.figbox text.ccost154{ text-anchor:middle; fill:var(--ink3); }
.figbox text.cwin154{ text-anchor:middle; fill:var(--rul);
  font-weight:600; }
.figbox text.ccube154{ text-anchor:middle; fill:var(--los); }
.figbox text.tag154{ text-anchor:middle; font-size:10px;
  letter-spacing:.09em; fill:var(--ink3); }
.figbox rect.swcrv154{ fill:var(--ink); }
.figbox rect.swc1154{ fill:var(--fam); }
.figbox rect.swc2154{ fill:var(--chn); }
.figbox rect.swlev154{ fill:var(--rul); }
</style>
"""


def die(msg):
    raise SystemExit("BUILD FAILED: " + msg)


def main():
    src = io.open(SRC, encoding="utf-8").read()
    lines = src.splitlines(keepends=True)

    # ---- SLICE guard -----------------------------------------------------
    close = [i for i, l in enumerate(lines) if "</style>" in l]
    if len(close) != 5:
        die("expected FIVE style blocks upstream, found %d" % len(close))
    head_end = close[-1] + 1
    head = "".join(lines[:head_end])
    if not head.startswith("<title>"):
        die("slice does not start with <title>")
    if not head.rstrip().endswith("</style>"):
        die("slice does not end with </style>")
    if head.count("<style>") != 5:
        die("slice should carry exactly five <style> blocks, found %d"
            % head.count("<style>"))
    head = re.sub(r"^<title>[^<]*</title>",
                  "<title>" + TITLE + "</title>", head, count=1)
    if "<title>" + TITLE + "</title>" not in head:
        die("title substitution did not land")

    upstream_css = head[head.find("<style>"):]
    upstream_nocomment = re.sub(r"/\*.*?\*/", "", upstream_css, flags=re.S)

    body = io.open(BODY, encoding="utf-8").read()

    # ---- FIGURE-NAME guard -----------------------------------------------
    figa, figb = _q154_fig.build()
    both = figa + figb
    for bad in ("fill=", "stroke=", "font-size=", "var(--", "style="):
        if bad in both:
            die("presentation attribute leaked into the SVG: " + bad)
    fig_classes = set()
    for m in re.finditer(r'class="([^"]+)"', both):
        fig_classes.update(m.group(1).split())
    bare = sorted(c for c in fig_classes if not c.endswith("154"))
    if bare != ["lab"]:
        die("the SVG must emit exactly one bare class, 'lab'; got %r" % bare)
    if not re.search(r"\.figbox\s+text\.lab\s*\{", STYLE_EXTRA):
        die("no rule for the gate's own hook class 'lab'")
    for c in fig_classes:
        if c.startswith("grid") and not re.search(r"grid|axis", c):
            die(c + " will not get the svg-labels exemption")
    if "gridl" in fig_classes or "axis" in fig_classes:
        die("'gridl'/'axis' carry upstream PAINT; use a grid*154 name")
    for c in sorted(fig_classes):
        if c == "lab":
            continue
        if not re.search(r"\.%s\b" % re.escape(c), STYLE_EXTRA):
            die("figure class .%s has no rule in EXTRA" % c)
    styled_fig = set(re.findall(r"\.figbox\s+(?:rect|line|circle|polyline"
                                r"|text|svg)\.([A-Za-z][A-Za-z0-9_-]*)",
                                STYLE_EXTRA))
    unemitted = sorted(styled_fig - fig_classes)
    if unemitted:
        die("EXTRA styles figure classes the generator never emits: %r"
            % unemitted)

    # ---- SWATCH-DASH guard ------------------------------------------------
    # A legend that draws a SOLID swatch for a DASHED curve contradicts its
    # own figure, and no rendering gate sees it (carryover 14.6 and 16.7,
    # where the same defect was hit twice). A 16x3 rect cannot carry a dash
    # pattern, so a dashed row must be drawn as TWO short rects. The build
    # script is the only place that can see both the SVG and the CSS.
    for swatch, curve in SWATCH_CURVE.items():
        if swatch not in fig_classes:
            die("legend swatch .%s is declared but never emitted" % swatch)
        if curve not in fig_classes:
            die("legend swatch .%s is keyed to .%s, which the generator "
                "never draws" % (swatch, curve))
        rule = re.search(r"\.figbox\s+\w+\.%s\b[^{]*\{([^}]*)\}"
                         % re.escape(curve), STYLE_EXTRA)
        if not rule:
            die("no rule found for the curve .%s behind swatch .%s"
                % (curve, swatch))
        dashed = "stroke-dasharray" in rule.group(1)
        pieces = both.count('class="%s"' % swatch)
        if dashed and pieces != 2:
            die("swatch .%s keys a DASHED curve .%s but is drawn as %d "
                "rect(s); a dashed row needs two" % (swatch, curve, pieces))
        if (not dashed) and pieces != 1:
            die("swatch .%s keys a SOLID curve .%s but is drawn as %d "
                "rect(s); a solid row needs one" % (swatch, curve, pieces))

    body = body.replace("<!--FIGA-->", figa).replace("<!--FIGB-->", figb)
    if "<!--FIG" in body:
        die("a figure placeholder survived")

    page = head + STYLE_EXTRA + "\n" + body

    # ---- COLLISION guard --------------------------------------------------
    own = sorted(set(re.findall(r"\.([A-Za-z][A-Za-z0-9_-]*154[a-z]?)",
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
                      if not re.search(r"154[a-z]?$", c)
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
    if not re.search(r"mjx-container\s*\{[^}]*color", upstream_nocomment,
                     flags=re.S):
        die("upstream does not paint mjx-container, so this guard is "
            "protecting against something that cannot happen")

    # ---- GRID-COUNT guard -------------------------------------------------
    # every grid this page defines must offer only track counts that DIVIDE
    # the cell counts it has to place, and must never use auto-fit.
    for name, counts in GRIDS.items():
        rules = re.findall(r"\.%s\s*\{\s*grid-template-columns:([^;}]+)"
                           % re.escape(name), extra_nocomment)
        if not rules:
            die("grid .%s has no grid-template-columns rule" % name)
        tracks = []
        for r in rules:
            if "auto-fit" in r or "auto-fill" in r:
                die("grid .%s uses auto-fit, which cannot satisfy the "
                    "divide-the-cell-count rule over a continuous width "
                    "range" % name)
            m = re.search(r"repeat\(\s*(\d+)", r)
            tracks.append(int(m.group(1)) if m else r.count("fr"))
        if not tracks:
            die("grid .%s offers no track counts" % name)
        for t in tracks:
            for n in counts:
                if n % t != 0:
                    die("grid .%s offers %d tracks for %d cells, which "
                        "leaves a ragged row" % (name, t, n))
        if 1 not in tracks:
            die("grid .%s has no single-column fallback" % name)

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
        die("inlineMath appears to accept a dollar, which this guard "
            "assumes it does not")
    stripped = body.replace("$$", "")
    if "$" in stripped:
        die("%d bare single dollars in the body would ship as VISIBLE raw "
            "LaTeX, because the head configures parenthesis delimiters for "
            "inline math" % stripped.count("$"))
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
    print("  style blocks     5 upstream + 1 EXTRA")
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
    print("  grids            %d, enumerated breakpoints, 0 auto-fit"
          % len(GRIDS))
    print("  legend swatches  %d, each matched to its curve's dash state"
          % len(SWATCH_CURVE))
    print("  inline math      %d parenthesis pairs, 0 bare dollars"
          % body.count("\\("))
    print("  display math     %d $$ pairs" % (body.count("$$") // 2))
    print("  dash spellings   0 of 8")
    print("  all guards passed")


if __name__ == "__main__":
    main()
