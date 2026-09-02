"""Build the Q14.1 artifact.

Every build-time guard the carryover records, in the order it records them:
  - slice head+style from the previous page, LOCATING </style> rather than
    reusing an index, and assert the slice
  - CLASS-COLLISION guard, by mechanical renaming with a 141 suffix
  - KEEP-INTEGRITY guard: KEEP == SERIES | FIGOWN, and every SERIES name really
    is present upstream (closes the hole rather than measuring a ratio)
  - FIGURE-NAME guard: every name the page treats as its own is absent upstream
  - TOKEN guard: every var(--x) the page leans on is defined in the slice
  - ORPHAN-CLASS guard: every class the body uses has a rule somewhere
  - ELEMENT-INHERITANCE guard: a bare-element selector upstream constraining a
    class this page invents must be redeclared or recorded in INHERIT_OK
  - INLINE-MATH gate: author in $...$, convert to the series delimiter, then
    assert zero bare dollars survive outside $$ blocks
  - DISPLAY-MATH gate: no \\[ survives; balanced $$ count
  - DASH-ENTITY gate: none of the six spellings reaches disk
"""
import sys
sys.dont_write_bytecode = True   # housekeeping: no __pycache__ in a content dir

import os
import re

import _q141_fig

HERE = os.path.dirname(os.path.abspath(__file__))
ART = os.path.dirname(HERE)
PREV = os.path.join(ART, "Q13.1-newtons-method.html")
OUT = os.path.join(ART, "Q14.1-curve-sketching.html")

# ---------------------------------------------------------------- 1. slice
src = open(PREV, "r", encoding="utf-8").read()
si = src.index("<style>")
ei = src.index("</style>", si) + len("</style>")
head = src[:si]
style = src[si:ei]
assert style.startswith("<style>"), "style slice does not start with <style>"
assert style.count("</style>") == 1, "style slice has the wrong number of closers"
assert "</style>" not in style[:-len("</style>")], "style slice contains an inner closer"
assert "<title>" in head, "head slice lost the title"
assert "MathJax" in head, "head slice lost MathJax"
print("slice: head %d chars, style %d chars" % (len(head), len(style)))

head = re.sub(r"<title>.*?</title>", "<title>Nothing Is An Answer</title>", head,
              count=1, flags=re.S)
assert "<title>Nothing Is An Answer</title>" in head

# the inline delimiter contract, read out of the head rather than assumed
mj = re.search(r"inlineMath:\s*\[\[(.*?)\]\]", head)
assert mj, "could not read inlineMath out of the head"
INLINE = mj.group(1)
print("head declares inlineMath:", INLINE)
assert "$" not in INLINE, "the head DOES accept bare $; the conversion gate is void"
dm = re.search(r"displayMath:\s*\[\[(.*?)\]\]", head)
assert dm and "$$" in dm.group(1), "the head does not declare $$ for display math"

body = open(os.path.join(HERE, "_q141_body.html"), "r", encoding="utf-8").read()

# ---------------------------------------------------------------- 2. figures
body = body.replace("FIGURE_CURVES", _q141_fig.fig_curves())
body = body.replace("FIGURE_BIF", _q141_fig.fig_bifurcation())
assert "FIGURE_" not in body, "a figure placeholder was left unfilled"

# ---------------------------------------------------------------- 3. this page's CSS
EXTRA = """
<style>
/* ===== Q14.1 EXTRA ==========================================================
   The page's one idea: four of the eight demanded cells are the word "none",
   so ABSENCE is the deliverable. Every rule below exists to make an absence
   read as a stated answer rather than as a gap, and to keep the two parts
   visually parallel so their complementarity is legible.
   Hue roles on this page:
     --accent  the curve, and part (a)'s single critical point
     --los     part (a)'s vertical asymptotes, and the sub-critical amplitude
     --num     the horizontal asymptote, and part (b)'s horizontal tangents
     --rul     the centre line y = x, and part (b)'s inflections
     --chn     the super-critical amplitude
   ========================================================================= */

/* the stem, quoted verbatim */
p.quote { margin:16px 0 18px; max-width:none; padding:15px 18px 16px;
  background:var(--sunk); border-left:3px solid var(--accent-line);
  font-size:15px; line-height:1.68; color:var(--ink2); }
.qp { display:block; margin-top:9px; color:var(--ink); }

/* the answer board: an absence is TYPESET, never blank */
table.ans td.dl { font-family:var(--mono); font-size:11.5px; letter-spacing:0.05em;
  text-transform:uppercase; color:var(--ink3); white-space:nowrap; }
td.none, table.ans td.none {
  font-family:var(--mono); font-weight:600; letter-spacing:0.1em;
  text-transform:uppercase; color:var(--los);
  background:var(--los-soft); text-align:center; }

/* the four order-rationale cells: one content child at column 2 is not needed
   here (this is a plain grid of blocks), but the TRACK COUNT must DIVIDE the
   cell count or grid-fill.mjs reports a ragged last row. Four cells, so the
   only legal track counts are 4, 2 and 1. */
.pipe { display:grid; grid-template-columns:repeat(4,minmax(0,1fr));
  gap:1px; background:var(--line); border:1px solid var(--line);
  margin:20px 0 22px; }
.pipe .cell { background:var(--surface); padding:15px 16px 17px; }
.pipe .cell p { margin:0; max-width:none; font-size:14px; line-height:1.62; }
.pipe .ch { font-family:var(--mono); font-size:10.5px; letter-spacing:0.1em;
  text-transform:uppercase; color:var(--accent); margin-bottom:8px; }
@media (max-width:1010px) { .pipe { grid-template-columns:repeat(2,minmax(0,1fr)); } }
@media (max-width:600px)  { .pipe { grid-template-columns:minmax(0,1fr); } }

/* the per-part walkthrough: a label/value ladder, not cards */
.pv { display:grid; grid-template-columns:170px minmax(0,1fr);
  gap:1px; background:var(--line); border:1px solid var(--line); margin:18px 0 20px; }
.pv > div { background:var(--surface); padding:13px 16px; min-width:0; }
.pv > div.pvh { background:var(--sunk); font-family:var(--mono); font-size:10.5px;
  letter-spacing:0.1em; text-transform:uppercase; color:var(--ink3);
  display:flex; align-items:center; }
.pv > div:not(.pvh) { font-size:14.5px; line-height:1.66; max-width:none; }
.pv mjx-container[display="true"] { overflow-x:auto; overflow-y:hidden; margin:9px 0!important; }
@media (max-width:660px) {
  .pv { grid-template-columns:minmax(0,1fr); }
  .pv > div.pvh { padding-bottom:0; border:0; }
}

/* three cross-checks. THREE cells, so 3 or 1 tracks only. */
.checks { display:grid; grid-template-columns:repeat(3,minmax(0,1fr));
  gap:1px; background:var(--line); border:1px solid var(--line); margin:18px 0 22px; }
.checks .ck { background:var(--surface); padding:15px 16px 17px; }
.checks .ck p { margin:0; max-width:none; font-size:14px; line-height:1.62; }
.checks .ckh { font-family:var(--mono); font-size:10.5px; letter-spacing:0.09em;
  text-transform:uppercase; color:var(--num); margin-bottom:9px; }
@media (max-width:940px) { .checks { grid-template-columns:minmax(0,1fr); } }

/* the family stack: one column, because each family carries a wide table */
.fams { display:flex; flex-direction:column; gap:1px;
  background:var(--line); border:1px solid var(--line); margin:18px 0 20px; }
.fams .fam { background:var(--surface); padding:16px 18px 18px; min-width:0; }
.fams .famh { font-family:var(--mono); font-size:11px; letter-spacing:0.1em;
  text-transform:uppercase; color:var(--accent); margin-bottom:10px; }
.fams .ft { margin:0 0 12px; font-size:14px; line-height:1.6; max-width:none;
  color:var(--ink2); }
.fams .fk { margin:12px 0 0; font-size:14px; line-height:1.64; max-width:none;
  padding:11px 13px; background:var(--sunk); border-left:2px solid var(--accent-line); }
.fams table { font-size:13.5px; }

/* do / do-not. TWO cells, so 2 or 1 tracks. */
.dodont { display:grid; grid-template-columns:repeat(2,minmax(0,1fr));
  gap:1px; background:var(--line); border:1px solid var(--line); margin:18px 0 20px; }
.dodont > div { background:var(--surface); padding:15px 17px 18px; }
.dodont ul { margin:0; padding-left:19px; max-width:none; font-size:14px; line-height:1.66; }
.dodont li { margin-bottom:6px; }
.dodont .ch { font-family:var(--mono); font-size:10.5px; letter-spacing:0.11em;
  text-transform:uppercase; margin-bottom:10px; }
.dodont .do .ch { color:var(--ok); }
.dodont .dont .ch { color:var(--los); }
@media (max-width:780px) { .dodont { grid-template-columns:minmax(0,1fr); } }

/* provenance ladder, same shape as .pv so the page has one label idiom */
.prov { display:grid; grid-template-columns:190px minmax(0,1fr);
  gap:1px; background:var(--line); border:1px solid var(--line); margin:16px 0 22px; }
.prov > div { background:var(--surface); padding:13px 16px; min-width:0;
  font-size:14.5px; line-height:1.64; max-width:none; }
.prov > div.pvh { background:var(--sunk); font-family:var(--mono); font-size:10.5px;
  letter-spacing:0.1em; text-transform:uppercase; color:var(--ink3);
  display:flex; align-items:center; }
@media (max-width:660px) {
  .prov { grid-template-columns:minmax(0,1fr); }
  .prov > div.pvh { padding-bottom:0; }
}

/* the verification bar reads as data, so tabular figures */
table.vbar td.num { font-family:var(--mono); font-variant-numeric:tabular-nums;
  text-align:right; white-space:nowrap; }

/* ordered lists this page invents. The inherited ul,ol sets max-width:70ch,
   which the element-inheritance guard checks; these are wide blocks and must
   redeclare it, and each li holds ONE content child (a span) so the inherited
   two-column .traps grid cannot wrap it one word wide. */
ol.steps, ol.traps, ol.tl { max-width:none; }
ol.steps { margin:16px 0 20px; padding-left:0; list-style:none;
  counter-reset:st141; display:flex; flex-direction:column; gap:1px;
  background:var(--line); border:1px solid var(--line); }
ol.steps li { counter-increment:st141; background:var(--surface);
  padding:12px 16px 13px; display:grid; grid-template-columns:30px minmax(0,1fr);
  align-items:baseline; font-size:14.5px; line-height:1.64; }
ol.steps li::before { content:counter(st141); font-family:var(--mono);
  font-size:11px; color:var(--accent); grid-column:1; }
ol.steps li > span { grid-column:2; }
ol.traps li, ol.tl li { max-width:none; }
ol.traps li > span, ol.tl li > span { grid-column:2; }
ol.tl { margin:14px 0 18px; }

/* ---- figures ------------------------------------------------------------
   ALL SVG paint and type live here, never in a presentation attribute: var()
   does not resolve in one, and a CSS rule beats one outright. In particular
   upstream's `.figbox text.lab{font-size:12px}` and
   `.figbox .gridl{stroke:var(--line);stroke-width:1}` would silently override
   any attribute this page wrote, which is why the reference lines below use
   `gridref` - it still matches the svg-labels /grid|axis/ exemption, and
   inherits none of the gridline paint. */
.figbox { overflow-x:auto; }
.figbox svg { display:block; min-width:820px; }

.figbox text.lab.fhd { font-size:10.5px; letter-spacing:0.1em; fill:var(--ink3); }
.figbox text.lab.ftk { font-size:10.5px; letter-spacing:0.02em; fill:var(--plotlab); }
.figbox text.lab.flg { font-size:11.5px; letter-spacing:0.01em; fill:var(--ink2); }

.figbox .pbox { fill:var(--plot); stroke:var(--line); stroke-width:1; }
.figbox .gridfine { stroke:var(--grid); stroke-width:1; }
.figbox .axisl { stroke:var(--line); stroke-width:1.4; }
/* the drawn curve. The SVG scales to its container, so a plotted stroke would
   thin out with it; pin it to screen pixels instead. */
.figbox .cv { fill:none; stroke:var(--accent); stroke-width:2.6;
  stroke-linecap:round; vector-effect:non-scaling-stroke; }
.figbox .cv.closs { stroke:var(--los); }
.figbox .cv.cacc { stroke:var(--accent); }
.figbox .cv.cchn { stroke:var(--chn); }
/* Reference lines: exempt from the label gate, painted by role, and at FULL
   strength rather than the -line tint. The vertical asymptotes sit exactly on
   top of the x = -1 and x = 1 gridlines, so at tint strength they were
   indistinguishable from the grid - and they are part (a)'s headline answer.
   The screenshot is the only thing that shows this; no gate compares two
   strokes. Same reasoning as the carryover's "two soft tints are not a
   contrast", one tier up. */
.figbox .gridref { fill:none; stroke-width:2; stroke-dasharray:8 5;
  vector-effect:non-scaling-stroke; }
.figbox .gridref.va { stroke:var(--los); stroke-width:2.2; }
.figbox .gridref.ha { stroke:var(--num); }
.figbox .gridref.cl { stroke:var(--rul); }
.figbox .tg { stroke:var(--num-line); stroke-width:2.4; stroke-linecap:round;
  vector-effect:non-scaling-stroke; }
/* marked points */
.figbox .cp { fill:var(--ground); stroke:var(--accent); stroke-width:2.6; }
.figbox .ip { fill:var(--rul); stroke:none; }
.figbox .zr { fill:var(--ground); stroke-width:2.4; }
.figbox .zr.closs { stroke:var(--los); }
.figbox .zr.cacc { stroke:var(--accent); }
.figbox .zr.cchn { stroke:var(--chn); }
/* the tangent stub is full-strength, not the line tint: at 30px it has to read */
.figbox .tg { stroke:var(--num); }

/* MathJax inline must stay INLINE. Series rule, restated because a missing
   copy of it breaks every sentence containing math onto three lines. */
mjx-container:not([display="true"]) { display:inline-block!important; margin:0!important;
  text-align:left; vertical-align:-0.15em; }
/* and typeset math inherits the surrounding colour, which it does not by default */
td.none mjx-container, td.none mjx-container svg { color:var(--los); fill:currentColor; }
.fams .famh mjx-container svg, .pv .pvh mjx-container svg { fill:currentColor; }
</style>
"""

# ---------------------------------------------------------------- 4. namespacing
# SERIES: names defined UPSTREAM that this page deliberately reuses.
# The first draft listed ten more (cell, ch, checks, ck, ckh, famh, prov, pvh,
# quote, vbar) and the KEEP-INTEGRITY guard rejected every one: upstream carries
# them only in SUFFIXED form (ck111, prov131, quote131 ...), so as bare names
# they were exemptions no guard covered. They are namespaced instead.
# Nine further names that ARE upstream (pipe, pv, fam, fams, ft, fk, steps, do,
# dont) were also moved out deliberately: each carries an upstream GRID or
# ::before counter, and the carryover records that shadowing a structural rule
# by source order is fragile. Only presentation classes are reused.
SERIES = {
    "wrap", "mast", "main", "eyebrow", "stand", "note", "warn",
    "tscroll", "vtab", "mono", "cap", "figbox", "traps", "tl", "num", "ok",
}
# FIGOWN: the ONLY figure name kept unsuffixed is `lab`, which is svg-labels.mjs's
# own selector hook and must stay bare or the gate measures nothing. Every other
# class the SVG emits is namespaced by the mechanical renamer below, which CLOSES
# the KEEP hole rather than merely measuring it. `gridl` is deliberately NOT used:
# it carries upstream PAINT (stroke:var(--line);stroke-width:1) welded to the gate
# exemption, which repainted every asymptote as a plain gridline in the first draft.
FIGOWN = {"lab"}
KEEP = SERIES | FIGOWN

upstream_classes = set(re.findall(r"\.([a-zA-Z][a-zA-Z0-9_-]*)", style))

# --- KEEP-INTEGRITY guard -------------------------------------------------
assert KEEP == (SERIES | FIGOWN), "KEEP is not exactly SERIES | FIGOWN"
missing_series = sorted(n for n in SERIES if n not in upstream_classes)
assert not missing_series, ("these SERIES names are NOT upstream, so they are "
                            "exemptions no guard covers: " + repr(missing_series))
print("KEEP-INTEGRITY: %d SERIES names all present upstream, %d FIGOWN"
      % (len(SERIES), len(FIGOWN)))

# --- FIGURE-NAME guard ----------------------------------------------------
# Collect every class the generated SVG actually emits, and require that each one
# either IS the gate hook or gets namespaced. The carryover records that figure
# names live in KEEP and are therefore skipped by the collision guard; here the
# set that reaches KEEP is exactly {lab}, so the hole is one name wide and that
# name is checked explicitly.
svg_src = "".join(re.findall(r"<svg[\s\S]*?</svg>", body))
assert svg_src, "no SVG found in the body; the figure-name guard would measure nothing"
svg_classes = set()
for m in re.finditer(r'class="([^"]+)"', svg_src):
    svg_classes.update(m.group(1).split())
assert "lab" in svg_classes, "the gate hook `lab` is absent from the SVG"
assert "gridl" not in svg_classes, "gridl carries upstream paint; use gridref instead"
leaked = sorted(n for n in (svg_classes & KEEP) if n != "lab")
assert not leaked, ("these SVG classes reach KEEP unsuffixed and so skip the "
                    "collision guard: " + repr(leaked))
print("FIGURE-NAME guard: %d SVG classes, 1 is the gate hook, %d will be namespaced"
      % (len(svg_classes), len(svg_classes) - 1))
# prove the guard can fire at all: these ARE upstream, so a page claiming them
# would be caught
assert "tanl" in upstream_classes and "curve" in upstream_classes, \
    "the figure-name guard's own control failed: it cannot detect an upstream name"

# --- mechanical rename ----------------------------------------------------
own = set(re.findall(r"\.([a-zA-Z][a-zA-Z0-9_-]*)", EXTRA))
own |= set(re.findall(r'class="([^"]+)"', body)
           and " ".join(re.findall(r'class="([^"]+)"', body)).split())
rename = sorted(n for n in own if n not in KEEP)
n_renamed = 0
for n in rename:
    EXTRA = re.sub(r"\.%s\b" % re.escape(n), "." + n + "141", EXTRA)
    n_renamed += 1


def _fix_classattr(m):
    names = m.group(1).split()
    return 'class="%s"' % " ".join((x + "141") if x in rename else x for x in names)


body = re.sub(r'class="([^"]+)"', _fix_classattr, body)
EXTRA = re.sub(r"counter-reset:st141", "counter-reset:st141", EXTRA)
print("namespaced %d invented names, %d deliberate overrides" % (n_renamed, len(KEEP)))
assert n_renamed >= len(KEEP) // 3, "suspiciously few renames; KEEP may be too wide"

# --- TOKEN guard ----------------------------------------------------------
used = set(re.findall(r"var\((--[a-z0-9-]+)\)", EXTRA + body))
defined = set(re.findall(r"(--[a-z0-9-]+)\s*:", style)) | \
          set(re.findall(r"(--[a-z0-9-]+)\s*:", EXTRA))
undef = sorted(used - defined)
assert not undef, "these tokens are used and never defined: " + repr(undef)
print("TOKEN guard: %d tokens used, all defined" % len(used))
assert "--mono" in defined, "the token guard's control failed: --mono must be defined"

# --- ORPHAN-CLASS guard ---------------------------------------------------
body_classes = set()
for m in re.finditer(r'class="([^"]+)"', body):
    body_classes.update(m.group(1).split())
styled = set(re.findall(r"\.([a-zA-Z][a-zA-Z0-9_-]*)", style + EXTRA))
orphans = sorted(body_classes - styled)
assert not orphans, "these classes are used in the body and styled nowhere: " + repr(orphans)
print("ORPHAN-CLASS guard: %d body classes, all styled" % len(body_classes))

# --- ELEMENT-INHERITANCE guard -------------------------------------------
# STRIP CSS COMMENTS FIRST. A rule-scanning regex anchored at a line start will
# happily begin a match INSIDE a preceding comment and swallow the real selector
# into its capture, so the rule's declarations are attributed to nothing. That
# silently cost this build one true `max-width` redeclaration and produced a
# false positive that looked exactly like a real defect.
def _decomment(css):
    return re.sub(r"/\*.*?\*/", "", css, flags=re.S)


style_nc = _decomment(style)
CONSTRAINING = ("max-width", "padding-left", "margin", "width")
elem_rules = {}
for m in re.finditer(r"(?m)^\s*((?:[a-z]+\s*,\s*)*[a-z]+)\s*\{([^}]*)\}", style_nc):
    sel, decl = m.group(1), m.group(2)
    for el in [s.strip() for s in sel.split(",")]:
        if not re.fullmatch(r"[a-z]+", el):
            continue
        for prop in CONSTRAINING:
            if re.search(r"(?<![-a-z])" + prop + r"\s*:", decl):
                elem_rules.setdefault(el, set()).add(prop)
assert "ol" in elem_rules and "max-width" in elem_rules["ol"], \
    "the element-inheritance guard's CONTROL failed: upstream ul,ol must set max-width"
print("ELEMENT-INHERITANCE guard: upstream element/property pairs:",
      {k: sorted(v) for k, v in sorted(elem_rules.items())})
# Recorded deliberate inheritances. ol.traps keeps the series' own list metrics
# on purpose - it is the accumulated ranked-list look, and its ::before counter
# grid is what the single-content-child <span> pattern is written against.
INHERIT_OK = {("ol.traps", "margin"), ("ol.traps", "padding-left"),
               ("ol.tl", "padding-left")}

# Collect declarations per SELECTOR across every rule, not per rule block: a
# page legitimately splits `max-width` into a shared rule and the rest into its
# own. The first draft checked blocks in isolation and reported six false
# positives for exactly that reason.
own_decls = {}
EXTRA_NC = _decomment(EXTRA)
for m in re.finditer(r"(?m)^\s*([^{}@/][^{}]*?)\s*\{([^}]*)\}", EXTRA_NC):
    sel, decl = m.group(1), m.group(2)
    for one in [s.strip() for s in sel.split(",")]:
        if re.fullmatch(r"[a-z]+\.[a-zA-Z0-9_-]+", one):
            own_decls.setdefault(one, "")
            own_decls[one] += ";" + decl
problems = []
for one, decl in own_decls.items():
    el = one.split(".")[0]
    for prop in elem_rules.get(el, ()):
        if re.search(r"(?<![-a-z])" + prop + r"\s*:", decl):
            continue
        if (one, prop) in INHERIT_OK:
            continue
        problems.append((one, prop))
assert not problems, ("these page-own rules silently inherit an upstream element "
                      "constraint: " + repr(sorted(set(problems))))
print("ELEMENT-INHERITANCE guard: %d element/class subjects checked, "
      "0 silent inheritances, %d recorded as deliberate"
      % (len(own_decls), len(INHERIT_OK)))
# prove the guard can still fire: remove max-width from one subject and re-test
_probe = re.sub(r"ol\.steps141, ol\.traps, ol\.tl \{ max-width:none; \}", "", EXTRA_NC)
_pd = ""
for m in re.finditer(r"(?m)^\s*([^{}@/][^{}]*?)\s*\{([^}]*)\}", _probe):
    for one in [s.strip() for s in m.group(1).split(",")]:
        if one == "ol.steps141":
            _pd += ";" + m.group(2)
assert "max-width" not in _pd, ("the removal probe did not bite; its regex no longer "
                                "matches the rule it is meant to delete")

# --- INLINE-MATH gate -----------------------------------------------------
# Author in $...$; convert to the delimiter the head actually declares.
parts = body.split("$$")
assert len(parts) % 2 == 1, ("unbalanced $$ display blocks: %d segments" % len(parts))
n_disp = (len(parts) - 1) // 2
n_inline = 0
for i in range(0, len(parts), 2):          # even segments are OUTSIDE $$ blocks
    seg = parts[i]

    def _one(m):
        global n_inline
        n_inline += 1
        return "\\(" + m.group(1) + "\\)"
    parts[i] = re.sub(r"\$([^$]+?)\$", _one, seg)
body = "$$".join(parts)
print("INLINE-MATH gate: converted %d inline spans, %d display blocks" % (n_inline, n_disp))
assert n_inline > 200, "suspiciously few inline spans converted: %d" % n_inline
outside = "".join(body.split("$$")[i] for i in range(0, len(body.split("$$")), 2))
assert "$" not in outside, ("bare $ survives outside a $$ block, so it would ship as "
                            "visible raw LaTeX: " + repr(outside[max(0, outside.index("$") - 60):
                                                                 outside.index("$") + 60]
                                                          if "$" in outside else ""))
# --- DISPLAY-MATH gate ----------------------------------------------------
assert "\\[" not in body, "a bracket display block survives; the head never processes it"
assert "\\]" not in body, "a bracket display closer survives"

# --- DASH-ENTITY gate -----------------------------------------------------
page = head + style + EXTRA + body
SPELLINGS = ["&" + "mdash;", "&" + "ndash;", "&" + "#8212;", "&" + "#8211;",
             "&" + "#x2014;", "&" + "#x2013;", chr(0x2014), chr(0x2013)]
# NO CARVE-OUTS. The first draft exempted the en-dash entity as a "deliberate
# spaced dash"; the house rule forbids en dashes as well as em dashes, and
# dash-lint reported the page DIRTY on 27 of them. An exemption invented by the
# thing being checked is not a decision, it is a hole.
for sp in SPELLINGS:
    assert sp not in page, "dash spelling reached the page: " + repr(sp)
print("DASH-ENTITY gate: all %d spellings absent" % len(SPELLINGS))
ctrl = [hex(ord(c)) for c in page if ord(c) < 32 and c not in "\n\r\t"]
assert not ctrl, "control characters in the page: " + repr(ctrl[:8])

open(OUT, "w", encoding="utf-8", newline="\n").write(page)
print("WROTE %s  %d bytes" % (OUT, len(page)))
