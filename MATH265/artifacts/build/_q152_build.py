"""Build the Q15.2 artifact page.

Inherits the accumulated series head + stylesheet by SLICING the Q15.1 page,
then appends this page's own EXTRA block. Every guard the carryover records
runs at build time, so a dirty page never reaches disk:

  SLICE guard          - the slice starts with <title>, ends with </style>,
                         and carries exactly THREE <style> blocks. Q15.1
                         asserted two and predicted three; expect four next.
  TOKEN guard          - every var(--x) the page leans on is defined
  COLLISION guard      - every class this page invents is absent upstream
  KEEP-INTEGRITY guard - every exemption really is an upstream series name
  ORPHAN-CLASS guard   - every class the body uses has a rule somewhere
  FIGURE-NAME guard    - the generated SVG emits only 152-suffixed classes
                         plus `lab`, the svg-labels hook
  ELEMENT-INHERITANCE  - the element/property pairs this page relies on
                         upstream are checked, with a removal probe
  BRACKET-MATH guard   - no \\[ survives, and $$ is balanced
  INLINE-MATH guard    - the head configures \\( \\) for inline math and NOT
                         $, so no bare single $ may survive in the body
  DASH-ENTITY guard    - none of the eight dash spellings is present
  CONTROL-CHAR guard   - no stray control characters
"""
import sys

sys.dont_write_bytecode = True

import io
import os
import re

import _q152_fig

HERE = os.path.dirname(os.path.abspath(__file__))
ART = os.path.dirname(HERE)
SRC = os.path.join(ART, "Q15.1-closed-interval-extremes.html")
OUT = os.path.join(ART, "Q15.2-least-perimeter-open-domain.html")
BODY = os.path.join(HERE, "_q152_body.html")

TITLE = "The Argument Is The Answer"

# ---- genuine SERIES names this page reuses. Each is asserted present
# ---- upstream below, so the exemption list cannot silently widen.
KEEP_SERIES = [
    "wrap", "mast", "main", "eyebrow", "stand", "note", "tscroll", "vtab",
    "figbox", "lab", "pgrid", "pcard", "pk", "pv", "pd", "kbd",
    "sing", "los", "fam",
]

STYLE_EXTRA = r"""
<style>
/* ===== Q15.2 EXTRA =========================================================
   Q15.2 is the FIRST optimization word problem and the FIRST question in the
   queue whose feasible domain is OPEN. What the five series hues mean here:

     THE ANSWER, the square and the minimum level          --rul amber
     THE MACHINERY, the two component terms, the
       derivative, the candidate the algebra produces      --chn slate
     WHERE MARKS DIE, the missing justification and the
       square that hides three wrong objectives            --los terracotta
     THE VARIATION families                                --fam teal
     NUMERICS: provenance, counts, gates                   --num mauve

   The signature block is panel B in section 03: five rectangles of area 220
   drawn to scale on one baseline, whose perimeters read 118, 71, 59.3296,
   71, 118. The list is symmetric because P(220/w) = P(w), so the square is
   the fixed point of that involution - the page's deepest single fact, and
   the reason the shape is not a check.
   ======================================================================== */

/* ---- section numbers -------------------------------------------------- */
.sn152{ font-family:var(--mono); font-size:.62em; font-weight:600;
  letter-spacing:.09em; color:var(--num); vertical-align:.32em;
  margin-right:.55em; }

/* ---- the quoted stem and the model write-up --------------------------- */
p.quote152{ margin:16px 0 20px; padding:15px 18px; border-radius:2px;
  background:var(--sunk); border-left:3px solid var(--accent-line);
  color:var(--ink); line-height:1.66; }
.qp152{ display:block; margin-top:10px; font-family:var(--mono);
  font-size:.88em; line-height:1.6; color:var(--ink3); }

/* ---- tables ----------------------------------------------------------- */
table.ans152, table.gen152, table.cls152, table.rc152, table.ck152,
table.cens152, table.fam152, table.f2t152, table.dr152{
  width:100%; border-collapse:collapse; font-size:14px; min-width:700px; }
table.fam152, table.dr152, table.cens152{ min-width:940px; }
table.f2t152{ min-width:820px; }
table.ans152 th, table.gen152 th, table.cls152 th, table.rc152 th,
table.ck152 th, table.cens152 th, table.fam152 th, table.f2t152 th,
table.dr152 th{
  text-align:left; font-family:var(--mono); font-size:10.5px;
  letter-spacing:.085em; text-transform:uppercase; color:var(--ink3);
  font-weight:600; padding:9px 12px; border-bottom:1px solid var(--line);
  vertical-align:bottom; }
table.ans152 td, table.gen152 td, table.cls152 td, table.rc152 td,
table.ck152 td, table.cens152 td, table.fam152 td, table.f2t152 td,
table.dr152 td{
  padding:10px 12px; border-bottom:1px solid var(--line-soft);
  vertical-align:top; line-height:1.52; }
td.dl152{ font-weight:600; color:var(--ink); }
td.hi152, tr.hi152 > td{ background:var(--rul-soft); color:var(--ink); }
td.hi152{ font-weight:600; }
td.non152{ font-family:var(--mono); font-size:12.5px; letter-spacing:.06em;
  text-transform:uppercase; color:var(--fam); font-weight:600; }
td.mono152, span.mono152{ font-family:var(--mono); font-size:12.6px;
  font-variant-numeric:tabular-nums; }
/* Long Windows paths carry no break opportunity - a backslash is not one -
   so an inline mono span holding one is an unbreakable 388px token that
   pushes the DOCUMENT sideways at the 430px lint case. Found by lint.mjs
   on the first build; the reported culprits were the wide table inside its
   own scroll container, which is noise, and the real cause was
   `Work\knowledge\topics\math265-answer-verification.py` in section 12. */
span.mono152, p.cap152{ overflow-wrap:anywhere; }
td.bad152{ background:var(--los-soft); color:var(--los); font-weight:600; }
td.hid152{ background:var(--num-soft); color:var(--num); font-weight:600;
  font-family:var(--mono); font-size:11.6px; letter-spacing:.05em; }
td.pos152{ color:var(--fam); font-weight:600; }
td.neg152{ color:var(--los); font-weight:600; }
td.fh152{ font-family:var(--mono); font-size:11.4px; font-weight:600;
  letter-spacing:.055em; text-transform:uppercase; color:var(--fam);
  background:var(--fam-soft); }

/* ---- numbered lists: ONE content child at grid column 2 --------------- */
ol.steps152, ol.traps152, ol.def152{ list-style:none; counter-reset:s152;
  margin:18px 0 4px; padding:0; display:flex; flex-direction:column;
  gap:1px; background:var(--line-soft); border-radius:2px;
  overflow:hidden; }
ol.steps152 > li, ol.traps152 > li, ol.def152 > li{
  counter-increment:s152; display:grid;
  grid-template-columns:38px minmax(0,1fr); align-items:start;
  background:var(--surface); padding:12px 14px; }
ol.steps152 > li::before, ol.traps152 > li::before,
ol.def152 > li::before{
  content:counter(s152); grid-column:1; font-family:var(--mono);
  font-size:11px; font-weight:600; letter-spacing:.06em;
  color:var(--accent); padding-top:.3em; }
ol.steps152 > li > span, ol.traps152 > li > span, ol.def152 > li > span{
  grid-column:2; line-height:1.62; }
ol.traps152 > li::before{ color:var(--los); }
ol.def152 > li::before{ color:var(--num); }

/* ---- callout ---------------------------------------------------------- */
p.warn152{ margin:18px 0; padding:14px 17px; border-radius:2px;
  background:var(--los-soft); border-left:3px solid var(--los-line);
  color:var(--ink); line-height:1.62; }

/* ---- panel grids. Every track count DIVIDES its cell count. ----------- */
.pgrid.inh152, .pgrid.wr152, .pgrid.ent152{ display:grid; gap:1px;
  background:var(--line-soft);
  grid-template-columns:repeat(3,minmax(0,1fr)); margin:20px 0;
  border-radius:2px; overflow:hidden; }
.pgrid.ent152{ grid-template-columns:repeat(2,minmax(0,1fr)); }
.pgrid.rt152{ display:grid; gap:1px; background:var(--line-soft);
  grid-template-columns:repeat(2,minmax(0,1fr)); margin:20px 0;
  border-radius:2px; overflow:hidden; }
.pgrid.ver152{ display:grid; gap:1px; background:var(--line-soft);
  grid-template-columns:repeat(4,minmax(0,1fr)); margin:20px 0;
  border-radius:2px; overflow:hidden; }
.pgrid.ver152 .pk{ font-family:var(--mono); font-size:26px;
  font-variant-numeric:tabular-nums; color:var(--num); }
@media (max-width:1080px){
  .pgrid.ver152{ grid-template-columns:repeat(2,minmax(0,1fr)); }
}
@media (max-width:880px){
  .pgrid.inh152, .pgrid.wr152, .pgrid.rt152, .pgrid.ent152,
  .pgrid.ver152{ grid-template-columns:repeat(1,minmax(0,1fr)); }
}

/* ---- the figures ------------------------------------------------------ */
.figbox.f152{ margin:20px 0 8px; padding:14px 10px 10px;
  background:var(--surface); border:1px solid var(--line);
  border-radius:2px; overflow-x:auto; }
svg.fig152{ display:block; width:100%; min-width:660px; height:auto; }
p.cap152{ margin:0 0 22px; font-size:12.8px; line-height:1.58;
  color:var(--ink3); }

/* SVG paint lives HERE and only here. var() does not resolve in an SVG
   presentation attribute, and an upstream CSS rule beats one anyway. */
.figbox rect.pbox152{ fill:none; stroke:var(--line);
  vector-effect:non-scaling-stroke; }
.figbox line.gridv152, .figbox line.gridh152{ stroke:var(--grid);
  stroke-width:1; vector-effect:non-scaling-stroke; }
.figbox line.gridbase152{ stroke:var(--line); stroke-width:1.4;
  vector-effect:non-scaling-stroke; }
.figbox line.gridlev152{ stroke:var(--rul); stroke-width:1.7;
  stroke-dasharray:7 5; vector-effect:non-scaling-stroke; }
.figbox line.gridrop152{ stroke:var(--chn); stroke-width:1.2;
  stroke-dasharray:3 4; vector-effect:non-scaling-stroke; }
.figbox polyline.curveP152{ fill:none; stroke:var(--ink2);
  stroke-width:2.2; stroke-linejoin:round;
  vector-effect:non-scaling-stroke; }
.figbox polyline.termlin152, .figbox polyline.termhyp152{ fill:none;
  stroke:var(--chn); stroke-width:1.5; stroke-dasharray:6 4;
  stroke-linejoin:round; vector-effect:non-scaling-stroke; }
.figbox circle.minm152{ fill:var(--rul); stroke:var(--surface);
  stroke-width:1.6; vector-effect:non-scaling-stroke; }
.figbox circle.crossm152{ fill:var(--chn); stroke:var(--surface);
  stroke-width:1.4; vector-effect:non-scaling-stroke; }
.figbox rect.rbox152{ fill:var(--chn-soft); stroke:var(--chn);
  stroke-width:1.3; vector-effect:non-scaling-stroke; }
.figbox rect.sqbox152{ fill:var(--rul-soft); stroke:var(--rul);
  stroke-width:2.2; vector-effect:non-scaling-stroke; }
.figbox rect.swpl152{ fill:var(--ink2); stroke:none; }
.figbox rect.swtm152{ fill:var(--chn); stroke:none; }
.figbox rect.swlv152{ fill:var(--rul); stroke:none; }
.figbox text.lab{ font-family:var(--mono); fill:var(--plotlab); }
.figbox text.tick152, .figbox text.ytick152{ font-size:10.5px;
  letter-spacing:.04em; }
.figbox text.tick152{ text-anchor:middle; }
.figbox text.ytick152{ text-anchor:end; }
.figbox text.ph152{ font-size:10.5px; letter-spacing:.09em;
  font-weight:600; fill:var(--ink3); text-anchor:start; }
.figbox text.leg152{ font-size:11px; letter-spacing:.02em;
  fill:var(--ink2); text-anchor:start; }
.figbox text.callo152{ font-size:11px; letter-spacing:.06em;
  font-weight:600; fill:var(--ink2); text-anchor:start; }
.figbox text.levlab152{ font-size:11px; letter-spacing:.05em;
  font-weight:600; fill:var(--rul); text-anchor:end; }
.figbox text.dim152{ font-size:10.5px; letter-spacing:.04em;
  fill:var(--ink3); text-anchor:middle; }
.figbox text.per152{ font-size:11px; letter-spacing:.04em;
  font-weight:600; fill:var(--ink2); text-anchor:middle; }
.figbox text.perwin152{ font-size:11px; letter-spacing:.04em;
  font-weight:600; fill:var(--rul); text-anchor:middle; }

/* Inline MathJax must stay INLINE. Without this the series' own tex-svg
   output can resolve to a centred block and break every sentence that
   contains inline maths onto three lines. */
mjx-container:not([display="true"]){ display:inline-block!important;
  margin:0; text-align:left; vertical-align:-0.15em; }

/* MathJax does NOT inherit its container's colour, because upstream sets
   `mjx-container{color:var(--mj)}`. Every coloured cell and every card
   heading on this page contains inline maths, so without these rules the
   maths renders ink-white beside teal, terracotta, mauve or amber text in
   the SAME phrase. No gate sees it; the screenshot did. */
td.pos152 mjx-container, td.pos152 mjx-container svg,
td.neg152 mjx-container, td.neg152 mjx-container svg,
td.bad152 mjx-container, td.bad152 mjx-container svg,
td.hid152 mjx-container, td.hid152 mjx-container svg,
td.non152 mjx-container, td.non152 mjx-container svg,
td.fh152 mjx-container, td.fh152 mjx-container svg,
.pcard .pk mjx-container, .pcard .pk mjx-container svg,
.pgrid.ver152 .pk mjx-container, .pgrid.ver152 .pk mjx-container svg{
  color:inherit; fill:currentColor; }
</style>
"""

# element/property pairs this page RELIES on inheriting from upstream. Each
# is asserted present, and the removal probe proves the assertion can fail.
ELEMENT_INHERITANCE = [
    (r"\bbody\s*\{[^}]*background", "body background"),
    (r"\bh1\s*\{[^}]*font-family", "h1 font-family"),
    (r"\bh2\s*\{[^}]*font-", "h2 font"),
    (r"\.wrap\s*\{[^}]*max-width", "wrap max-width"),
    (r"\.tscroll\s*\{[^}]*overflow-x", "tscroll overflow-x"),
]


def die(msg):
    raise SystemExit("BUILD FAILED: " + msg)


def main():
    src = io.open(SRC, encoding="utf-8").read()
    lines = src.splitlines(True)

    # ---- SLICE guard -----------------------------------------------------
    close = [i for i, l in enumerate(lines) if "</style>" in l]
    if len(close) != 3:
        die("expected THREE style blocks upstream, found %d" % len(close))
    head_end = close[-1] + 1
    head = "".join(lines[:head_end])
    if not head.startswith("<title>"):
        die("slice does not start with <title>")
    if not head.rstrip().endswith("</style>"):
        die("slice does not end with </style>")
    if head.count("<style>") != 3:
        die("slice should carry exactly three <style> blocks, found %d"
            % head.count("<style>"))
    head = re.sub(r"^<title>[^<]*</title>",
                  "<title>" + TITLE + "</title>", head, count=1)
    if "<title>" + TITLE + "</title>" not in head:
        die("title substitution did not land")

    upstream_css = head[head.find("<style>"):]
    upstream_nocomment = re.sub(r"/\*.*?\*/", "", upstream_css, flags=re.S)

    body = io.open(BODY, encoding="utf-8").read()

    # ---- FIGURE-NAME guard ------------------------------------------------
    figa, figb = _q152_fig.build()
    both = figa + figb
    for bad in ("fill=", "stroke=", "font-size=", "var(--", "style="):
        if bad in both:
            die("presentation attribute leaked into the SVG: " + bad)
    fig_classes = set()
    for m in re.finditer(r'class="([^"]+)"', both):
        fig_classes.update(m.group(1).split())
    bare = sorted(c for c in fig_classes if not c.endswith("152"))
    if bare != ["lab"]:
        die("the SVG must emit exactly one bare class, 'lab'; got %r" % bare)
    # `lab` is the ONE bare class the SVG may emit, because it is the
    # svg-labels hook. The hole is one name wide and that name is checked.
    if not re.search(r"\.figbox\s+text\.lab\s*\{", STYLE_EXTRA):
        die("no rule for the gate's own hook class 'lab'")
    for c in fig_classes:
        if c.startswith("grid") and not re.search(r"grid|axis", c):
            die(c + " will not get the svg-labels exemption")
    if "gridl" in fig_classes or "axis" in fig_classes:
        die("'gridl'/'axis' carry upstream PAINT; use a grid*152 name")
    # every figure class must have a rule in EXTRA, since none exists upstream
    for c in sorted(fig_classes):
        if c == "lab":
            continue
        if not re.search(r"\.%s\b" % re.escape(c), STYLE_EXTRA):
            die("figure class .%s has no rule in EXTRA" % c)
    # ...and the REVERSE, which the carryover's version of this guard did
    # not check: every class styled under `.figbox` must actually be
    # emitted. A rule for a shape the generator no longer draws is drift,
    # and it is how a legend keyed to nothing survives a rewrite.
    styled_fig = set(re.findall(r"\.figbox\s+(?:rect|line|circle|polyline"
                                r"|text)\.([A-Za-z][A-Za-z0-9_-]*)",
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
    own = sorted(set(re.findall(r"\.([A-Za-z][A-Za-z0-9_-]*152)",
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
                      if not c.endswith("152") and c not in KEEP_SERIES)
    if unexempt:
        die("body classes neither namespaced nor in KEEP: %r" % unexempt)

    # ---- ELEMENT-INHERITANCE guard, with a removal probe -----------------
    for pat, label in ELEMENT_INHERITANCE:
        if not re.search(pat, upstream_nocomment, flags=re.S):
            die("this page relies on upstream '%s' and it is absent"
                % label)
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
        n = stripped.count("$")
        die("%d bare single dollars in the body would ship as VISIBLE raw "
            "LaTeX, because the head configures \\( \\) for inline math" % n)
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
    print("  namespaced       %d" % len(own))
    print("  KEEP exemptions  %d (each proved present upstream)"
          % len(KEEP_SERIES))
    print("  ratio            %d renamed against %d exempt"
          % (len(own), len(KEEP_SERIES)))
    print("  body classes     %d, 0 orphans, 0 unexempt" % len(body_classes))
    print("  var() tokens     %d used, 0 undefined" % len(used))
    print("  figure classes   %d, 1 bare ('lab'), all styled in EXTRA"
          % len(fig_classes))
    print("  inline math      %d \\( \\) pairs, 0 bare dollars"
          % body.count("\\("))
    print("  display math     %d $$ pairs" % (body.count("$$") // 2))
    print("  dash spellings   0 of 8")
    print("  all guards passed")


if __name__ == "__main__":
    main()
