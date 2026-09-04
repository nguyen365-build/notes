"""Build the Q16.2 artifact page.

Inherits the accumulated series head + stylesheet by SLICING the Q16.1 page, then appends this
page's own EXTRA block.  Every guard the carryover records runs at build time, so a dirty page
never reaches disk.

20.7 predicted the slice would carry NINE <style> blocks and advised asserting nine.  That
advice is WRONG and this build documents why: Q16.1 is the first page whose FIGURE carries its
own <style>, and that block sits MID-BODY, so a `rfind("</style>")` slice drags the previous
page's masthead and first three sections along with the stylesheet.  The stylesheet ends where
the BODY begins, so the search is bounded by that and the slice is EIGHT blocks.
The assembled page is 8 inherited + this page's EXTRA + this page's figure = TEN.
The next page slicing THIS one should again bound by the body start and expect NINE.
"""
import sys

sys.dont_write_bytecode = True

import io
import os
import re

import _q162_fig

HERE = os.path.dirname(os.path.abspath(__file__))
ART = os.path.dirname(HERE)
SRC = os.path.join(ART, "Q16.1-a-search-not-a-lookup.html")
OUT = os.path.join(ART, "Q16.2-nothing-checks-the-name.html")
BODY = os.path.join(HERE, "_q162_body.html")

TITLE = "Nothing Checks the Name"

KEEP_SERIES = [
    "wrap", "mast", "main", "eyebrow", "stand", "note", "tscroll", "vtab",
    "figbox", "lab", "gridl",
]

TOKENS_USED = ["--mono", "--ink", "--num", "--line", "--ground", "--surface", "--sunk",
               "--rul", "--los", "--chn", "--fam", "--ok"]

COLOURED_MATH = ["hi162", "los162", "win162", "fam162", "chn162", "num162", "mono162",
                 "pk162"]

GRIDS = {"pgrid162": [3]}

STYLE_EXTRA = r"""
<style>
/* ===== Q16.2 EXTRA =========================================================
   Q16.2 CLOSES the integration category, and its subject is not a technique -
   it is the SENTENCE you write beside the technique. So the page's job is to
   make one asymmetry unmissable: every mistake in the algebra has a check,
   and the mistake in the NAME has none.

   The five series hues, used here:

     THE ANSWER, the four antiderivatives                        --rul amber
     THE MACHINERY, structural observations                      --chn slate
     WHERE MARKS DIE, the blind families, the absent names       --los terracotta
     THE ALTERNATIVE ROUTE, and the naming family itself         --fam teal
     NUMERICS: provenance, counts, every measured gap            --num mauve

   The signature block is section 03's figure. Panel A is a UNIT chart - 26
   cells, one per seeded wrong answer - rather than a bar chart, because the
   claim is about a count and an exact split, and a unit chart cannot distort
   a ratio the way an axis can. The seven amber cells are the page's whole
   thesis and they are the only place the accent is spent at full strength.

   The figure draws ZERO <line> elements by construction: frames, cells and
   chips are <rect> and the connectors are <polygon> chevrons. That empties
   the label-versus-line collision surface, but it also makes svg-labels'
   lineHits arm VACUOUS here, so only labelPairs and outsideBox are live on
   this page and those are the arms proved with a seeded control.
   ======================================================================== */

/* ---- section numbers and sub-headings --------------------------------- */
.sn162{ font-family:var(--mono); font-size:.62em; font-weight:600;
  letter-spacing:.09em; color:var(--num); vertical-align:.32em;
  margin-right:.55em; }
h3.sh162{ font-size:15.5px; letter-spacing:.005em; margin:30px 0 10px;
  color:var(--ink); font-weight:600; }

/* ---- the quoted stem block -------------------------------------------- */
.stem162{ border-left:2px solid var(--rul); padding:2px 0 2px 18px;
  margin:18px 0 4px; }
.prov162{ font-size:12.5px; color:var(--num); line-height:1.62; margin-top:12px; }

/* ---- the procedure listing --------------------------------------------- */
pre.ladder162{ font-family:var(--mono); font-size:12.5px; line-height:1.62;
  background:var(--sunk); border:1px solid var(--line); border-radius:3px;
  padding:16px 18px; overflow-x:auto; margin:16px 0; }
pre.ladder162 code{ background:none; padding:0; font-size:inherit;
  color:var(--ink); }

/* ---- the rung tag beside a part heading -------------------------------- */
.rung162{ font-family:var(--mono); font-size:10.5px; font-weight:600;
  letter-spacing:.07em; color:var(--rul); border:1px solid var(--rul);
  border-radius:2px; padding:1px 6px; vertical-align:.18em;
  text-transform:uppercase; white-space:nowrap; }

/* ---- semantic colour, applied through the series tokens ---------------- */
.hi162{ color:var(--rul); font-weight:600; }
.los162{ color:var(--los); }
.win162{ color:var(--ok); font-weight:600; }
.fam162{ color:var(--fam); }
.chn162{ color:var(--chn); }
.num162{ color:var(--num); font-family:var(--mono); font-size:.88em; }
.mono162{ font-family:var(--mono); font-size:.9em; }
.pk162{ font-family:var(--mono); font-size:.82em; font-weight:600;
  letter-spacing:.06em; color:var(--num); text-transform:uppercase; }
/* MathJax does not inherit its container's colour (carryover 16.7) */
.hi162 mjx-container, .los162 mjx-container, .win162 mjx-container,
.fam162 mjx-container, .chn162 mjx-container, .num162 mjx-container,
.mono162 mjx-container, .pk162 mjx-container{ color:inherit; }
.hi162 mjx-container svg, .los162 mjx-container svg, .win162 mjx-container svg,
.fam162 mjx-container svg, .chn162 mjx-container svg, .num162 mjx-container svg,
.mono162 mjx-container svg, .pk162 mjx-container svg{ fill:currentColor; }

/* ---- the one-sentence thesis ------------------------------------------- */
.thesis162{ font-size:16px; line-height:1.6; font-weight:600; color:var(--ink);
  border-left:3px solid var(--rul); padding:10px 0 10px 18px; margin:20px 0;
  text-wrap:balance; }

/* ---- callout paragraphs ------------------------------------------------ */
p.warn162{ font-size:13.5px; line-height:1.68; color:var(--ink);
  background:var(--sunk); border:1px solid var(--line);
  border-left:2px solid var(--los); border-radius:3px;
  padding:12px 16px; margin:16px 0; }

/* ---- the three word-sense cards ---------------------------------------- */
/* 17.6's enumerated-breakpoint rule: 3 cells in 3 tracks, then 1. Never
   auto-fit, which cannot satisfy the divide-the-cell-count rule over a
   continuous width range. */
.pgrid162{ display:grid; grid-template-columns:repeat(3,minmax(0,1fr));
  gap:1px; background:var(--line); border:1px solid var(--line);
  border-radius:3px; margin:18px 0; }
@media (max-width:820px){ .pgrid162{ grid-template-columns:minmax(0,1fr); } }
.pcard162{ background:var(--surface); padding:14px 16px 16px; }
.pcard162 p{ font-size:13px; line-height:1.62; margin:8px 0 0; }

/* ---- the trap list ------------------------------------------------------ */
/* ONE content child at column 2 (carryover 4), so nothing wraps into the
   counter column. */
ol.traps162{ list-style:none; counter-reset:t162; padding:0; margin:16px 0; }
ol.traps162 li{ counter-increment:t162; display:grid;
  grid-template-columns:34px minmax(0,1fr); gap:0 6px; margin:0 0 10px; }
ol.traps162 li::before{ content:counter(t162); font-family:var(--mono);
  font-size:11px; font-weight:600; color:var(--num); padding-top:3px; }
ol.traps162 li > span{ grid-column:2; font-size:13.5px; line-height:1.65; }

/* ---- the methods list --------------------------------------------------- */
ul.meth162{ margin:12px 0; padding-left:20px; }
ul.meth162 li{ font-size:13.5px; line-height:1.66; margin:0 0 9px; }

/* ---- figure caption ----------------------------------------------------- */
p.cap162{ font-size:12.5px; line-height:1.62; color:var(--num); margin-top:12px; }
</style>
"""


def fail(msg):
    print("BUILD GUARD FAILED: " + msg)
    sys.exit(1)


GUARDS = []


def guard(name, cond, detail=""):
    GUARDS.append((name, bool(cond)))
    if not cond:
        fail(name + ("  " + detail if detail else ""))


def main():
    src = io.open(SRC, "r", encoding="utf-8").read()
    body = io.open(BODY, "r", encoding="utf-8").read()

    # ---------------------------------------------------------------- SLICE
    lines = src.split("\n")
    head = "\n".join(lines[:12])
    guard("head slice ends before the first <style>", "<style>" not in head)
    guard("head slice carries the MathJax script", "tex-svg.js" in head)
    guard("head slice carries the font stylesheet", "fonts.googleapis.com" in head)

    # DEFECT FOUND THIS RUN, and 20.7's own advice is what causes it.  Q16.1 is the first
    # page in the series whose FIGURE carries its own <style> block, and that block sits
    # MID-BODY.  So `src.rfind("</style>")` no longer lands at the end of the stylesheet -
    # it lands inside the figure, and the slice silently drags the whole masthead and the
    # first three sections of the previous page along with it.  Measured: the naive slice
    # carried 3 <section>, 3 <h2> and 1 <table> of Q16.1's body, and the assembled page
    # rendered Q16.1's title and its answers table above this page's own.
    #
    # 20.7 says "expect the slice to be NINE next time"; taking nine is exactly the bug.
    # The stylesheet ends where the BODY begins, so bound the search by that.
    body_start = min([i for i in (src.find("<header"), src.find("<main")) if i > 0])
    guard("source's body start was located", body_start > 0)
    last_close = src.rfind("</style>", 0, body_start)
    guard("source has a </style> before its body", last_close > 0)
    style_start = src.find("<style>")
    style = src[style_start:last_close + len("</style>")]
    guard("style slice starts with <style>", style.startswith("<style>"))
    guard("style slice ends with </style>", style.endswith("</style>"))
    # the guard that would have caught this the first time: a stylesheet has no body markup
    for tag in ["<section", "<table", "<h1", "<h2", "<h3", "<header", "<main", "<svg"]:
        guard("style slice carries no %s markup" % tag, tag not in style,
              "slice contains %d occurrence(s)" % style.count(tag))
    n_blocks = style.count("<style>")
    guard("style slice carries EIGHT <style> blocks (7 inherited by Q16.1, plus its EXTRA)",
          n_blocks == 8, "found %d" % n_blocks)

    # ---------------------------------------------------------------- FIGURE
    fig = _q162_fig.build()
    guard("figure is pure ASCII", all(ord(c) < 128 for c in fig))
    guard("figure has no var() in a presentation attribute",
          not re.search(r'(fill|stroke)="var\(', fig))
    guard("every figure <text> carries class lab",
          fig.count("<text") == fig.count('class="lab'))
    # This page draws no <line> at all, so svg-labels' lineHits arm is vacuous here.
    # Record that explicitly rather than letting 0 == 0 read as a pass.
    guard("figure draws ZERO line elements, so lineHits is VACUOUS on this page",
          fig.count("<line") == 0, "found %d" % fig.count("<line"))
    # THEME CONTRACT GUARD, added after the light render showed the figure painting its
    # DARK palette on a white page. Every `:not([data-theme="light"])` rule must sit inside
    # a prefers-color-scheme media query, or it matches the UNSTAMPED light state too.
    figstyle = re.search(r"<style>(.*?)</style>", fig, flags=re.S).group(1)
    # Brace-depth walk: every :not([data-theme="light"]) occurrence must sit at depth >= 1,
    # i.e. inside the @media block, and that block must be the dark one.
    depth, media_depth, bad_notlight = 0, None, 0
    i = 0
    while i < len(figstyle):
        if figstyle.startswith("@media (prefers-color-scheme: dark)", i):
            media_depth = depth
        if figstyle.startswith(':root:not([data-theme="light"])', i):
            if depth < 1 or media_depth is None:
                bad_notlight += 1
        if figstyle[i] == "{":
            depth += 1
        elif figstyle[i] == "}":
            depth -= 1
        i += 1
    guard("every :not([data-theme=light]) rule in the figure is INSIDE the dark @media block",
          bad_notlight == 0, "%d rule(s) sit at top level and would apply in light mode"
          % bad_notlight)
    guard("the figure declares a complete bare-:root light palette",
          figstyle.count("  .f") + figstyle.count("  .s") >= 8)
    guard("the figure repeats the dark palette under [data-theme=dark]",
          figstyle.count(':root[data-theme="dark"]') ==
          figstyle.count(':root:not([data-theme="light"])'))
    guard("figure body placeholder present", "__FIG__" in body)
    body = body.replace("__FIG__", fig)

    # ---------------------------------------------------------------- NAMESPACE GUARD
    invented = sorted(set(re.findall(r"\b([a-z]+162)\b", body + STYLE_EXTRA)))
    guard("page invents at least a dozen namespaced classes", len(invented) >= 12,
          str(invented))
    for c in invented:
        guard("invented class '%s' does not collide with the slice" % c, c not in style)

    used = set()
    for attr in re.findall(r'class="([^"]+)"', body):
        for c in attr.split():
            used.add(c)
    styled = style + STYLE_EXTRA + fig
    orphans = [c for c in sorted(used)
               if c not in KEEP_SERIES and ("." + c) not in styled]
    guard("no orphan classes in the body", not orphans, str(orphans))

    # ---------------------------------------------------------------- TOKEN GUARD
    for tok in TOKENS_USED:
        guard("token %s is defined in slice + EXTRA" % tok,
              re.search(re.escape(tok) + r"\s*:", styled) is not None)
    # every var() this page's EXTRA actually leans on must resolve (20.7: three invented
    # tokens shipped on an earlier page and silently fell back)
    for tok in sorted(set(re.findall(r"var\((--[a-z0-9]+)\)", STYLE_EXTRA))):
        guard("EXTRA's var(%s) is defined somewhere" % tok,
              re.search(re.escape(tok) + r"\s*:", styled) is not None)

    # ---------------------------------------------------------------- COLOURED MATH GUARD
    for c in COLOURED_MATH:
        guard("coloured-math class .%s sets color:inherit on mjx-container" % c,
              re.search(r"\." + c + r"\s+mjx-container", STYLE_EXTRA) is not None)

    # ---------------------------------------------------------------- GRID GUARD
    for g, tracks in GRIDS.items():
        m = re.search(r"\." + g + r"\{[^}]*grid-template-columns:repeat\((\d+)", STYLE_EXTRA)
        guard("grid .%s declares an explicit track count" % g, m is not None)
        guard("grid .%s has a single-column fallback" % g,
              re.search(r"\." + g + r"\{\s*grid-template-columns:minmax", STYLE_EXTRA)
              is not None)
        cells = body.count('class="pcard162"')
        guard("grid .%s cell count %d divides its %d tracks" % (g, cells, tracks[0]),
              cells % tracks[0] == 0)
    # strip CSS comments before any content scan, or the guard reads its own documentation
    rules_only = re.sub(r"/\*.*?\*/", "", STYLE_EXTRA, flags=re.S)
    guard("no auto-fit grid on this page (17.6 supersedes 15.6)",
          "auto-fit" not in rules_only)

    # ---------------------------------------------------------------- MATH DELIMITER GUARD
    guard("head configures $$ as displayMath", "displayMath: [['$$','$$']]" in head)
    guard("body contains no bracket display delimiters",
          (chr(92) + "[") not in body and (chr(92) + "]") not in body)
    guard("body has a balanced $$ count", body.count("$$") % 2 == 0)

    # ---------------------------------------------------------------- TABLE WRAP GUARD
    n_tables = body.count("<table>")
    n_scroll = body.count('class="tscroll vtab"')
    guard("every table is wrapped in a scroller", n_tables == n_scroll,
          "%d tables, %d wrappers" % (n_tables, n_scroll))

    # ---------------------------------------------------------------- LONG-SPAN GUARD
    stripped = re.sub(r'<div class="tscroll vtab">.*?</div>', "", body, flags=re.S)
    inline = re.findall(r"(?<!\$)\$([^$\n]{1,400})\$(?!\$)", stripped)
    longest = max((len(s) for s in inline), default=0)
    guard("longest free-standing inline math span is short", longest <= 64,
          "longest is %d chars: %r" % (longest, max(inline, key=len) if inline else ""))

    # ---------------------------------------------------------------- DASH GUARD
    for spelling in ["&mdash;", "&ndash;", "&#8212;", "&#8211;", "&#x2014;", "&#x2013;",
                     chr(0x2014), chr(0x2013)]:
        guard("no dash spelling %r in the body" % spelling, spelling not in body)
    ctrl = sorted(set(hex(ord(c)) for c in body if ord(c) < 32 and c not in "\n\r\t"))
    guard("body carries no stray control characters", not ctrl, str(ctrl))

    # ---------------------------------------------------------------- TITLE
    head = re.sub(r"<title>.*?</title>", "<title>%s</title>" % TITLE, head, count=1)
    guard("title is set", "<title>%s</title>" % TITLE in head)

    page = head + "\n" + style + "\n" + STYLE_EXTRA + "\n" + body + "\n"
    n_fig_style = fig.count("<style>")
    guard("the figure carries exactly one <style> block", n_fig_style == 1)
    guard("assembled page has TEN <style> blocks (8 inherited + EXTRA + figure)",
          page.count("<style>") == 8 + 1 + n_fig_style,
          "found %d" % page.count("<style>"))
    # the previous page's identity must not appear anywhere on this one
    guard("no trace of the source page's title survived the slice",
          "A Search, Not a Lookup" not in page)
    guard("the page carries exactly one <h1>", page.count("<h1>") == 1,
          "found %d" % page.count("<h1>"))
    guard("the page carries exactly one <main", page.count("<main") == 1)
    guard("table count in the assembled page equals the body's own",
          page.count("<table>") == n_tables, "page %d, body %d"
          % (page.count("<table>"), n_tables))

    io.open(OUT, "w", encoding="utf-8").write(page)
    print("wrote %s  bytes=%d" % (OUT, len(page.encode("utf-8"))))
    print("namespaced classes: %d   deliberate series overrides: %d"
          % (len(invented), len(KEEP_SERIES)))
    print("build guards: %d, all passed" % len(GUARDS))
    print("tables: %d   inline-math longest free-standing span: %d chars"
          % (n_tables, longest))


if __name__ == "__main__":
    main()
