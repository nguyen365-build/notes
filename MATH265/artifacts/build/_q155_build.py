"""Build the Q15.5 artifact page.

Inherits the accumulated series head + stylesheet by SLICING the Q15.4 page,
then appends this page's own EXTRA block. Every guard the carryover records
runs at build time, so a dirty page never reaches disk. Q15.4 predicted the
slice would carry SIX <style> blocks; this build asserts six and expects seven
next time.
"""
import sys

sys.dont_write_bytecode = True

import io
import os
import re

import _q155_fig

HERE = os.path.dirname(os.path.abspath(__file__))
ART = os.path.dirname(HERE)
SRC = os.path.join(ART, "Q15.4-cheapest-rectangular-box.html")
OUT = os.path.join(ART, "Q15.5-cusp-that-hides.html")
BODY = os.path.join(HERE, "_q155_body.html")

TITLE = "The Cusp That Hides"

KEEP_SERIES = [
    "wrap", "mast", "main", "eyebrow", "stand", "note", "tscroll", "vtab",
    "figbox", "lab", "pgrid", "pcard", "pk", "pv", "pd", "kbd",
]

ELEMENT_INHERITANCE = [
    (r"\.wrap\s*\{[^}]*max-width", "wrap max-width"),
    (r"\.tscroll\s*\{[^}]*overflow-x", "tscroll overflow-x"),
    (r"\.pgrid\s*\{[^}]*grid", "pgrid grid"),
]

COLOURED_MATH = ["hi155", "los155", "win155", "fam155", "chn155", "num155",
                 "mono155", "dl155"]

GRIDS = {"two155g": [2], "three155g": [3]}

# swatch -> the drawn mark it keys. The row count is DERIVED from the
# figure's own candidate list rather than typed, because the callout band
# draws one swatch per row and TWO rows key the same mark: the minimum is
# attained twice, which is the whole point of the page.
SWATCH_CURVE = {("sw" + _c): _c for _x, _w, _c in _q155_fig.CANDS}
SWATCH_ROWS = {}
for _x, _w, _c in _q155_fig.CANDS:
    SWATCH_ROWS["sw" + _c] = SWATCH_ROWS.get("sw" + _c, 0) + 1

STYLE_EXTRA = r"""
<style>
/* ===== Q15.5 EXTRA =========================================================
   Q15.5 closes category 15 and it is the only question in the course whose
   answer sits at a point where the derivative does not exist. So the page's
   job is to add a KIND of candidate rather than a method, and then to show
   that this particular interval lets you skip it for free.

   What the five series hues mean on this page:

     THE ANSWER, the two reported values, the cusp itself         --rul amber
     THE MACHINERY, the derivative, its domain, the table rows    --chn slate
     WHERE MARKS DIE, every mutilation that HIDES, the centred
       quotient, the silent second-derivative test                 --los terracotta
     THE SPECIES and the classification that separates them       --fam teal
     NUMERICS: provenance, counts, gates                          --num mauve

   The signature block is panel A in section 03. The curve is sampled on a
   CUBE schedule towards each cusp, because the slope diverges like h^(-1/3)
   and a uniform sample rounds the spike off into a smooth valley - which
   would draw the exact opposite of the page's claim. The level line at
   f = 0 runs the full width, because the tie between an ENDPOINT and an
   INTERIOR CUSP is why the omission hides, and a tie is a statement about
   two heights being equal.

   NO text sits inside either plotting frame, and there are no leader lines
   at all. Every predecessor in this series spent gate rounds on leader
   lines, which svg-labels samples like any other line; the callout band
   names its own x-values instead, which is what a reader needs anyway.
   ======================================================================== */

/* ---- section numbers and sub-headings --------------------------------- */
.sn155{ font-family:var(--mono); font-size:.62em; font-weight:600;
  letter-spacing:.09em; color:var(--num); vertical-align:.32em;
  margin-right:.55em; }
h3.sh155{ font-size:15.5px; letter-spacing:.005em; margin:30px 0 10px;
  color:var(--ink); font-weight:600; }

/* ---- the quoted stem, with its provenance footnote -------------------- */
.quote155{ border-left:3px solid var(--rul); padding:12px 0 12px 16px;
  margin:18px 0 14px; font-size:15px; line-height:1.65; color:var(--ink); }
.qp155{ display:block; margin-top:10px; font-size:12.5px; line-height:1.6;
  color:var(--ink3); }

/* ---- semantic text colours -------------------------------------------- */
.hi155{ color:var(--rul); font-weight:600; }
.los155{ color:var(--los); }
.win155{ color:var(--rul); font-weight:600; }
.fam155{ color:var(--fam); }
.chn155{ color:var(--chn); }
.num155{ color:var(--num); }
.dl155{ color:var(--ink); font-weight:600; }
.mono155{ font-family:var(--mono); font-size:.9em;
  font-variant-numeric:tabular-nums; }

/* MathJax does not inherit a container's colour (carryover 16.7), so every
   coloured cell that can hold maths needs both of these. */
.hi155 mjx-container, .los155 mjx-container, .win155 mjx-container,
.fam155 mjx-container, .chn155 mjx-container, .num155 mjx-container,
.mono155 mjx-container, .dl155 mjx-container{ color:inherit; }
.hi155 mjx-container svg, .los155 mjx-container svg,
.win155 mjx-container svg, .fam155 mjx-container svg,
.chn155 mjx-container svg, .num155 mjx-container svg,
.mono155 mjx-container svg, .dl155 mjx-container svg{ fill:currentColor; }

/* ---- the callout paragraphs ------------------------------------------- */
.entry155{ border:1px solid var(--line); border-left:3px solid var(--rul);
  padding:13px 16px; margin:18px 0; font-size:14px; line-height:1.65;
  background:var(--sunk); }
.warn155{ border-left:3px solid var(--los); padding:12px 0 12px 16px;
  margin:18px 0; font-size:14px; line-height:1.68; color:var(--ink); }

/* ---- the tables -------------------------------------------------------- */
table.ans155, table.fnd155, table.spc155, table.qt155, table.cnd155,
table.cen155, table.tie155, table.cat155, table.ver155{
  min-width:700px; }
table.qt155{ min-width:560px; }
table.tie155{ min-width:620px; }

/* ---- the panel cards --------------------------------------------------- */
.pcard.main155{ border-top:2px solid var(--chn); }
.pcard.los155{ border-top:2px solid var(--los); color:inherit; }
.pcard.fam155{ border-top:2px solid var(--fam); color:inherit; }
.pcard.num155{ border-top:2px solid var(--num); color:inherit; }

/* Enumerated breakpoints, never repeat(auto-fit,...): a track count has to
   DIVIDE the cell count at every width, and auto-fit cannot promise that
   over a continuous range (carryover 17.6). */
.two155g{ grid-template-columns:repeat(2,minmax(0,1fr)); }
.three155g{ grid-template-columns:repeat(3,minmax(0,1fr)); }
@media (max-width:1000px){
  .three155g{ grid-template-columns:repeat(1,minmax(0,1fr)); }
}
@media (max-width:720px){
  .two155g{ grid-template-columns:repeat(1,minmax(0,1fr)); }
  .three155g{ grid-template-columns:repeat(1,minmax(0,1fr)); }
}

/* ---- the decision tree -------------------------------------------------- */
pre.tree155{ font-family:var(--mono); font-size:12px; line-height:1.55;
  background:var(--sunk); border:1px solid var(--line); border-radius:2px;
  padding:16px 18px; margin:20px 0; overflow-x:auto; color:var(--ink);
  white-space:pre; }

/* ---- figures ------------------------------------------------------------ */
.figbox svg{ display:block; width:100%; height:auto; }
.figbox text.lab{ font-family:var(--mono); font-size:11.5px; fill:var(--ink3); }
.figbox text.tick155{ text-anchor:middle; }
.figbox text.tky155{ text-anchor:end; }
.figbox text.axl155{ text-anchor:middle; fill:var(--ink3); }
.figbox text.ayl155{ text-anchor:start; fill:var(--ink3); }
.figbox text.cah155{ fill:var(--num); font-size:11px; letter-spacing:.1em; }
.figbox text.cak155{ fill:var(--ink); }
.figbox text.cav155{ fill:var(--ink); }
.figbox text.cad155{ fill:var(--ink3); }
.figbox text.cap155{ fill:var(--ink3); font-size:11.5px; }
.figbox text.qnm155{ fill:var(--ink); font-size:12px; letter-spacing:.08em; }
.figbox text.qex155{ fill:var(--rul); }
.figbox text.qvd155{ fill:var(--fam); }
.figbox rect.frm155{ fill:none; stroke:var(--line); stroke-width:1; }
.figbox line.grid155{ stroke:var(--line); stroke-width:1; opacity:.55; }
.figbox line.lev155{ stroke:var(--rul); stroke-width:1; stroke-dasharray:4 4;
  opacity:.85; }
/* The one-sided slope segments are DASHED. On the corner panel the tangent
   IS the curve, so a solid segment is drawn exactly underneath the curve and
   is invisible; the dash is the only way the reader sees that the panel drew
   two one-sided slopes at all. Found by rendering the page and looking. */
.figbox line.slp155{ stroke:var(--los); stroke-width:2.2;
  stroke-dasharray:5 3; stroke-linecap:round; }
.figbox polyline.crv155{ fill:none; stroke:var(--chn); stroke-width:2;
  stroke-linejoin:round; stroke-linecap:round; }
.figbox polyline.cor155{ fill:none; stroke:var(--fam); stroke-width:2;
  stroke-linejoin:round; }
.figbox polyline.vtn155{ fill:none; stroke:var(--fam); stroke-width:2;
  stroke-linejoin:round; }
.figbox polyline.cus155{ fill:none; stroke:var(--rul); stroke-width:2;
  stroke-linejoin:round; }
.figbox circle.min155{ fill:var(--rul); stroke:var(--ground); stroke-width:1.5; }
.figbox circle.zer155{ fill:var(--fam); stroke:var(--ground); stroke-width:1.5; }
.figbox circle.max155{ fill:var(--rul); stroke:var(--ground); stroke-width:1.5; }
.figbox circle.brk155{ fill:var(--los); stroke:var(--ground); stroke-width:1.5; }
.figbox rect.swmin155{ fill:var(--rul); }
.figbox rect.swzer155{ fill:var(--fam); }
.figbox rect.swmax155{ fill:var(--rul); }
</style>
"""


def die(msg):
    raise SystemExit("BUILD FAILED: " + msg)


def main():
    src = io.open(SRC, encoding="utf-8").read()
    lines = src.splitlines(keepends=True)

    # ---- SLICE guard -----------------------------------------------------
    close = [i for i, l in enumerate(lines) if "</style>" in l]
    if len(close) != 6:
        die("expected SIX style blocks upstream, found %d" % len(close))
    head_end = close[-1] + 1
    head = "".join(lines[:head_end])
    if not head.startswith("<title>"):
        die("slice does not start with <title>")
    if not head.rstrip().endswith("</style>"):
        die("slice does not end with </style>")
    if head.count("<style>") != 6:
        die("slice should carry exactly six <style> blocks, found %d"
            % head.count("<style>"))
    head = re.sub(r"^<title>[^<]*</title>",
                  "<title>" + TITLE + "</title>", head, count=1)
    if "<title>" + TITLE + "</title>" not in head:
        die("title substitution did not land")

    upstream_css = head[head.find("<style>"):]
    upstream_nocomment = re.sub(r"/\*.*?\*/", "", upstream_css, flags=re.S)

    body = io.open(BODY, encoding="utf-8").read()

    # ---- FIGURE-NAME guard -----------------------------------------------
    figa, figb = _q155_fig.build()
    both = figa + figb
    for bad in ("fill=", "stroke=", "font-size=", "var(--", "style="):
        if bad in both:
            die("presentation attribute leaked into the SVG: " + bad)
    fig_classes = set()
    for m in re.finditer(r'class="([^"]+)"', both):
        fig_classes.update(m.group(1).split())
    bare = sorted(c for c in fig_classes if not c.endswith("155"))
    if bare != ["lab"]:
        die("the SVG must emit exactly one bare class, 'lab'; got %r" % bare)
    if not re.search(r"\.figbox\s+text\.lab\s*\{", STYLE_EXTRA):
        die("no rule for the gate's own hook class 'lab'")
    for c in fig_classes:
        if c.startswith("grid") and not re.search(r"grid|axis", c):
            die(c + " will not get the svg-labels exemption")
    if "gridl" in fig_classes or "axis" in fig_classes:
        die("'gridl'/'axis' carry upstream PAINT; use a grid*155 name")
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
    for swatch, curve in SWATCH_CURVE.items():
        if swatch not in fig_classes:
            die("legend swatch .%s is declared but never emitted" % swatch)
        if curve not in fig_classes:
            die("legend swatch .%s is keyed to .%s, which the generator "
                "never draws" % (swatch, curve))
        rule = re.search(r"\.figbox\s+\w+\.%s\b[^{]*\{([^}]*)\}"
                         % re.escape(curve), STYLE_EXTRA)
        if not rule:
            die("no rule found for the mark .%s behind swatch .%s"
                % (curve, swatch))
        dashed = "stroke-dasharray" in rule.group(1)
        pieces = both.count('class="%s"' % swatch)
        rows = SWATCH_ROWS[swatch]
        want = rows * (2 if dashed else 1)
        if pieces != want:
            die("swatch .%s keys a %s mark .%s over %d row(s), so it "
                "needs %d rect(s) and is drawn as %d"
                % (swatch, "DASHED" if dashed else "SOLID", curve, rows,
                   want, pieces))

    body = body.replace("<!--FIGA-->", figa).replace("<!--FIGB-->", figb)
    if "<!--FIG" in body:
        die("a figure placeholder survived")

    page = head + STYLE_EXTRA + "\n" + body

    # ---- COLLISION guard --------------------------------------------------
    own = sorted(set(re.findall(r"\.([A-Za-z][A-Za-z0-9_-]*155[a-z]?)",
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
                      if not re.search(r"155[a-z]?$", c)
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
    print("  style blocks     6 upstream + 1 EXTRA")
    print("  namespaced       %d" % len(own))
    print("  KEEP exemptions  %d (each proved present upstream)"
          % len(KEEP_SERIES))
    print("  ratio            %d renamed against %d exempt"
          % (len(own), len(KEEP_SERIES)))
    print("  body classes     %d, 0 orphans, 0 unexempt" % len(body_classes))
    print("  var() tokens     %d used, 0 undefined" % len(used))
    print("  figure classes   %d, 1 bare ('lab'), all styled AND emitted"
          % len(fig_classes))
    print("  math-colour      %d coloured classes guarded" % len(COLOURED_MATH))
    print("  grids            %d, enumerated breakpoints, 0 auto-fit"
          % len(GRIDS))
    print("  legend swatches  %d marks over %d rows, each matched to its "
          "dash state" % (len(SWATCH_CURVE), sum(SWATCH_ROWS.values())))
    print("  inline math      %d parenthesis pairs, 0 bare dollars"
          % body.count("\\("))
    print("  display math     %d $$ pairs" % (body.count("$$") // 2))
    print("  dash spellings   0 of 8")
    print("  all guards passed")


if __name__ == "__main__":
    main()
