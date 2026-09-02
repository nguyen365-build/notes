"""Build the Q15.1 artifact page.

Inherits the accumulated series head + stylesheet by SLICING the Q14.1 page,
then appends this page's own EXTRA block. Every guard the carryover records
runs at build time, so a dirty page never reaches disk:

  SLICE guard          - the slice starts with <title> and ends with </style>
  TOKEN guard          - every var(--x) the page leans on is defined upstream
  COLLISION guard      - every class this page invents is absent upstream
  KEEP-INTEGRITY guard - every exemption really is an upstream series name
  ORPHAN-CLASS guard   - every class the body uses has a rule somewhere
  FIGURE-NAME guard    - the generated SVG emits only renamed classes plus lab
  BRACKET-MATH guard   - no \\[ survives, and $$ is balanced (the head only
                         configures $$ for display math)
  DASH-ENTITY guard    - none of the eight dash spellings is present
  CONTROL-CHAR guard   - no stray control characters
"""
import sys

sys.dont_write_bytecode = True

import io
import os
import re

import _q151_fig

HERE = os.path.dirname(os.path.abspath(__file__))
ART = os.path.dirname(HERE)
SRC = os.path.join(ART, "Q14.1-curve-sketching.html")
OUT = os.path.join(ART, "Q15.1-closed-interval-extremes.html")
BODY = os.path.join(HERE, "_q151_body.html")

TITLE = "Both Ends Count"

# ---- classes this page invents. Every one is renamed with a 151 suffix in
# ---- BOTH the CSS and the body, so nothing can shadow an upstream rule.
# ---- Anything NOT in here must be in KEEP, and KEEP is checked upstream.
KEEP_SERIES = [
    # genuine series names, each asserted present upstream below
    "wrap", "mast", "main", "eyebrow", "stand", "note", "tscroll", "vtab",
    "fscroll", "figbox", "lab", "pgrid", "pcard", "pk", "kbd", "mono",
]

STYLE_EXTRA = r"""
<style>
/* ===== Q15.1 EXTRA =========================================================
   Q15.1 OPENS category 15. What the five series hues mean on THIS page:

     THE ANSWER, the value and the point that win        --rul amber
     THE CANDIDATE LIST, the machinery that finds them   --chn slate
     WHERE MARKS DIE, the dropped endpoint and the
       value/point confusion                            --los terracotta
     THE VARIATION families                              --fam teal
     NUMERICS: provenance, counts, gates                 --num mauve

   The signature block is the two-panel figure in section 02, where the
   maximum LEVEL is drawn all the way across part (a): nothing on the curve
   reaches it until the last point of the interval.
   ======================================================================== */

/* ---- section numbers -------------------------------------------------- */
.sn151{ font-family:var(--mono); font-size:.62em; font-weight:600;
  letter-spacing:.09em; color:var(--num); vertical-align:.32em;
  margin-right:.55em; }

/* ---- the quoted stem -------------------------------------------------- */
p.quote151{ margin:16px 0 20px; padding:15px 18px; border-radius:2px;
  background:var(--sunk); border-left:3px solid var(--accent-line);
  color:var(--ink); line-height:1.62; }
.qp151{ display:block; margin-top:10px; font-family:var(--mono);
  font-size:.92em; color:var(--ink2); }

/* ---- tables ----------------------------------------------------------- */
table.ans151, table.kinds151, table.cand151, table.sgn151, table.cat151,
table.cens151, table.fam151, table.dr151{
  width:100%; border-collapse:collapse; font-size:14px;
  min-width:700px; }
table.fam151, table.dr151{ min-width:920px; }
table.ans151 th, table.kinds151 th, table.cand151 th, table.sgn151 th,
table.cat151 th, table.cens151 th, table.fam151 th, table.dr151 th{
  text-align:left; font-family:var(--mono); font-size:10.5px;
  letter-spacing:.085em; text-transform:uppercase; color:var(--ink3);
  font-weight:600; padding:9px 12px; border-bottom:1px solid var(--line);
  vertical-align:bottom; }
table.ans151 td, table.kinds151 td, table.cand151 td, table.sgn151 td,
table.cat151 td, table.cens151 td, table.fam151 td, table.dr151 td{
  padding:10px 12px; border-bottom:1px solid var(--line-soft);
  vertical-align:top; line-height:1.5; }
td.dl151{ font-weight:600; color:var(--ink); white-space:nowrap; }
td.hi151{ background:var(--rul-soft); color:var(--ink); font-weight:600; }
td.non151{ font-family:var(--mono); font-size:12.5px; letter-spacing:.06em;
  text-transform:uppercase; color:var(--fam); font-weight:600; }
td.mono151, code.mono151, span.mono151{ font-family:var(--mono);
  font-size:12.8px; font-variant-numeric:tabular-nums; }
td.wint151{ background:var(--rul-soft); color:var(--rul); font-weight:600;
  white-space:nowrap; }
td.endw151{ color:var(--rul); font-family:var(--mono); font-size:11.5px;
  letter-spacing:.05em; text-transform:uppercase; white-space:nowrap; }
td.critw151{ color:var(--chn); font-family:var(--mono); font-size:11.5px;
  letter-spacing:.05em; text-transform:uppercase; white-space:nowrap; }
td.pos151{ color:var(--fam); font-weight:600; }
td.neg151{ color:var(--los); font-weight:600; }
td.bad151{ background:var(--los-soft); color:var(--los); font-weight:600; }
td.hid151{ background:var(--num-soft); color:var(--num); font-weight:600;
  font-family:var(--mono); font-size:11.5px; letter-spacing:.05em; }
td.nap151{ color:var(--ink3); text-align:center; }
td.tie151{ color:var(--fam); font-weight:600; }
td.fh151{ font-family:var(--mono); font-size:11.5px; font-weight:600;
  letter-spacing:.06em; text-transform:uppercase; color:var(--fam);
  background:var(--fam-soft); white-space:nowrap; }
span.pt151{ display:block; margin-top:3px; font-family:var(--mono);
  font-size:10px; letter-spacing:.07em; color:var(--ink3);
  text-transform:uppercase; font-weight:500; }

/* ---- step and trap lists: ONE content child at column 2 --------------- */
ol.steps151, ol.traps151, ol.def151{ list-style:none; counter-reset:s151;
  margin:18px 0 4px; padding:0; display:flex; flex-direction:column;
  gap:1px; background:var(--line-soft); border-radius:2px;
  overflow:hidden; }
ol.steps151 > li, ol.traps151 > li, ol.def151 > li{
  counter-increment:s151; display:grid;
  grid-template-columns:38px minmax(0,1fr); align-items:start;
  background:var(--surface); padding:12px 14px; }
ol.steps151 > li::before, ol.traps151 > li::before, ol.def151 > li::before{
  content:counter(s151); grid-column:1; font-family:var(--mono);
  font-size:11px; font-weight:600; letter-spacing:.06em;
  color:var(--accent); padding-top:.28em; }
ol.steps151 > li > span, ol.traps151 > li > span, ol.def151 > li > span{
  grid-column:2; line-height:1.6; }
ol.traps151 > li::before{ color:var(--los); }
ol.def151 > li::before{ color:var(--num); }

/* ---- callouts --------------------------------------------------------- */
p.warn151{ margin:16px 0; padding:13px 16px; border-radius:2px;
  background:var(--los-soft); border-left:3px solid var(--los-line);
  color:var(--ink); line-height:1.6; }

/* ---- panel grids. Track counts DIVIDE the cell counts. ---------------- */
.pgrid.evt151{ display:grid; gap:1px; background:var(--line-soft);
  grid-template-columns:repeat(3,minmax(0,1fr)); margin:18px 0;
  border-radius:2px; overflow:hidden; }
.pgrid.bif151{ display:grid; gap:1px; background:var(--line-soft);
  grid-template-columns:repeat(3,minmax(0,1fr)); margin:18px 0;
  border-radius:2px; overflow:hidden; }
.pgrid.shape151, .pgrid.prov151, .pgrid.ent151{ display:grid; gap:1px;
  background:var(--line-soft);
  grid-template-columns:repeat(3,minmax(0,1fr)); margin:18px 0;
  border-radius:2px; overflow:hidden; }
.pgrid.ver151{ display:grid; gap:1px; background:var(--line-soft);
  grid-template-columns:repeat(4,minmax(0,1fr)); margin:18px 0;
  border-radius:2px; overflow:hidden; }
@media (max-width:1080px){
  .pgrid.ver151{ grid-template-columns:repeat(2,minmax(0,1fr)); }
}
@media (max-width:880px){
  .pgrid.evt151, .pgrid.bif151, .pgrid.shape151, .pgrid.prov151,
  .pgrid.ent151{ grid-template-columns:repeat(1,minmax(0,1fr)); }
  .pgrid.ver151{ grid-template-columns:repeat(1,minmax(0,1fr)); }
}
.pv151{ margin-top:6px; font-size:13.5px; line-height:1.55;
  color:var(--ink2); }
.pcard.ok151 .pk{ color:var(--fam); }
.pcard.no151 .pk{ color:var(--los); }

/* ---- display maths ---------------------------------------------------- */
.disp151{ margin:18px 0; padding:4px 0; overflow-x:auto; text-align:center; }

/* ---- the figure ------------------------------------------------------- */
.figbox.f151{ margin:20px 0 8px; padding:14px 10px 10px;
  background:var(--surface); border:1px solid var(--line);
  border-radius:2px; overflow-x:auto; }
svg.fig151{ display:block; width:100%; min-width:640px; height:auto; }
p.cap151{ margin:0 0 22px; font-size:12.6px; line-height:1.55;
  color:var(--ink3); }

/* SVG paint. Every colour lives HERE, never in a presentation attribute,
   because var() does not resolve in one and a CSS rule beats one anyway. */
.figbox rect.pbox151{ fill:none; stroke:var(--line);
  vector-effect:non-scaling-stroke; }
.figbox line.gridv151, .figbox line.gridh151{ stroke:var(--grid);
  stroke-width:1; vector-effect:non-scaling-stroke; }
.figbox line.gridrule151{ stroke:var(--line); stroke-width:1;
  vector-effect:non-scaling-stroke; }
.figbox polyline.curve151{ fill:none; stroke:var(--ink2); stroke-width:2;
  stroke-linejoin:round; vector-effect:non-scaling-stroke; }
.figbox line.lev151{ stroke:var(--rul); stroke-width:1.6;
  stroke-dasharray:7 5; vector-effect:non-scaling-stroke; }
.figbox line.flat151{ stroke:var(--chn); stroke-width:2.6;
  vector-effect:non-scaling-stroke; }
.figbox rect.endp151{ fill:var(--rul); stroke:var(--surface);
  stroke-width:1.4; vector-effect:non-scaling-stroke; }
.figbox circle.crit151{ fill:var(--chn); stroke:var(--surface);
  stroke-width:1.4; vector-effect:non-scaling-stroke; }
.figbox circle.win151{ fill:none; stroke:var(--accent); stroke-width:2;
  vector-effect:non-scaling-stroke; }
.figbox text.lab{ font-family:var(--mono); fill:var(--plotlab); }
.figbox text.tick151, .figbox text.ytick151{ font-size:10.5px;
  letter-spacing:.04em; }
.figbox text.tick151{ text-anchor:middle; }
.figbox text.ytick151{ text-anchor:end; }
.figbox text.ph151{ font-size:10.5px; letter-spacing:.09em;
  font-weight:600; fill:var(--ink3); text-anchor:start; }
.figbox text.leg151{ font-size:11px; letter-spacing:.02em;
  fill:var(--ink2); text-anchor:start; }
</style>
"""


def die(msg):
    raise SystemExit("BUILD FAILED: " + msg)


def main():
    src = io.open(SRC, encoding="utf-8").read()
    lines = src.splitlines(True)

    # ---- SLICE guard -----------------------------------------------------
    close = [i for i, l in enumerate(lines) if "</style>" in l]
    if len(close) != 2:
        die("expected two style blocks upstream, found %d" % len(close))
    head_end = close[-1] + 1
    head = "".join(lines[:head_end])
    if not head.startswith("<title>"):
        die("slice does not start with <title>")
    if not head.rstrip().endswith("</style>"):
        die("slice does not end with </style>")
    if head.count("<style>") != 2:
        die("slice should carry exactly two <style> blocks")
    head = re.sub(r"^<title>[^<]*</title>",
                  "<title>" + TITLE + "</title>", head, count=1)
    if "<title>" + TITLE + "</title>" not in head:
        die("title substitution did not land")

    upstream_css = head[head.find("<style>"):]
    upstream_nocomment = re.sub(r"/\*.*?\*/", "", upstream_css, flags=re.S)

    body = io.open(BODY, encoding="utf-8").read()

    # ---- FIGURE-NAME guard, delegated to the generator's own check -------
    figa, figb = _q151_fig.build()
    for bad in ("fill=", "stroke=", "font-size=", "var(--"):
        if bad in figa + figb:
            die("presentation attribute leaked into the SVG: " + bad)
    fig_classes = set()
    for m in re.finditer(r'class="([^"]+)"', figa + figb):
        fig_classes.update(m.group(1).split())
    bare = sorted(c for c in fig_classes if not c.endswith("151"))
    if bare != ["lab"]:
        die("the SVG must emit exactly one bare class, 'lab'; got %r" % bare)
    # 'lab' is the ONE bare class the SVG may emit, because it is the gate's
    # own hook. The hole is therefore exactly one name wide, and that name is
    # checked explicitly here.
    if not re.search(r"\.figbox\s+text\.lab\s*\{", STYLE_EXTRA):
        die("no rule for the gate's own hook class 'lab'")
    for c in fig_classes:
        if c.startswith("grid") and not re.search(r"grid|axis", c):
            die(c + " will not get the svg-labels exemption")
    if "gridl" in fig_classes or "axis" in fig_classes:
        die("'gridl'/'axis' carry upstream paint; use a grid*151 name")

    body = body.replace("<!--FIGA-->", figa).replace("<!--FIGB-->", figb)
    if "<!--FIG" in body:
        die("a figure placeholder survived")

    page = head + STYLE_EXTRA + "\n" + body

    # ---- COLLISION guard --------------------------------------------------
    own = sorted(set(re.findall(r"\.([A-Za-z][A-Za-z0-9_-]*151)",
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
    all_css = upstream_nocomment + re.sub(r"/\*.*?\*/", "", STYLE_EXTRA,
                                          flags=re.S)
    orphans = []
    for c in sorted(body_classes):
        if not re.search(r"\.%s\b" % re.escape(c), all_css):
            orphans.append(c)
    if orphans:
        die("orphan classes with no CSS rule anywhere: %r" % orphans)

    # every body class must be namespaced OR explicitly kept
    unexempt = sorted(c for c in body_classes
                      if not c.endswith("151") and c not in KEEP_SERIES)
    if unexempt:
        die("body classes neither namespaced nor in KEEP: %r" % unexempt)

    # ---- TOKEN guard ------------------------------------------------------
    used = sorted(set(re.findall(r"var\((--[a-z0-9-]+)\)", page)))
    defined = set(re.findall(r"(--[a-z0-9-]+)\s*:", upstream_nocomment))
    defined |= set(re.findall(r"(--[a-z0-9-]+)\s*:",
                              re.sub(r"/\*.*?\*/", "", STYLE_EXTRA,
                                     flags=re.S)))
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
    print("  KEEP exemptions  %d (all proved present upstream)"
          % len(KEEP_SERIES))
    print("  body classes     %d, 0 orphans, 0 unexempt" % len(body_classes))
    print("  var() tokens     %d used, 0 undefined" % len(used))
    print("  figure classes   %d, 1 bare ('lab')" % len(fig_classes))
    print("  dash spellings   0 of 8")
    print("  all guards passed")


if __name__ == "__main__":
    main()
