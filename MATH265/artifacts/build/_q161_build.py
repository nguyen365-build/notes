"""Build the Q16.1 artifact page.

Inherits the accumulated series head + stylesheet by SLICING the Q15.5 page, then appends this
page's own EXTRA block. Every guard the carryover records runs at build time, so a dirty page
never reaches disk.

Q15.5's run predicted the slice would carry SEVEN <style> blocks; this build asserts seven and
expects EIGHT next time.
"""
import sys

sys.dont_write_bytecode = True

import io
import os
import re

import _q161_fig

HERE = os.path.dirname(os.path.abspath(__file__))
ART = os.path.dirname(HERE)
SRC = os.path.join(ART, "Q15.5-cusp-that-hides.html")
OUT = os.path.join(ART, "Q16.1-a-search-not-a-lookup.html")
BODY = os.path.join(HERE, "_q161_body.html")

TITLE = "A Search, Not a Lookup"

# classes that are DELIBERATE series overrides / inherited structure, not this page's inventions
KEEP_SERIES = [
    "wrap", "mast", "main", "eyebrow", "stand", "note", "tscroll", "vtab",
    "figbox", "lab", "gridl",
]

# every var() the page leans on must actually be defined somewhere in slice + EXTRA
TOKENS_USED = ["--mono", "--ink", "--num", "--line", "--ground", "--surface", "--sunk",
               "--rul", "--los", "--chn", "--fam", "--ok"]

# cells that hold MathJax and set their own colour need color:inherit + fill:currentColor
COLOURED_MATH = ["hi161", "los161", "win161", "fam161", "chn161", "num161", "mono161",
                 "pk161"]

# declared grids -> the track counts they must divide cleanly (17.6 enumerated-breakpoint rule)
GRIDS = {"pgrid161": [3]}

STYLE_EXTRA = r"""
<style>
/* ===== Q16.1 EXTRA =========================================================
   Q16.1 OPENS antiderivatives and is the FIRST integration question in the
   bank. Everything before it was differential calculus. So the page's job is
   not to teach a technique - it is to install the LADDER, and to be honest
   that integration is a SEARCH where differentiation was a lookup.

   What the five series hues mean on this page:

     THE ANSWER, the five antiderivatives, the winning route     --rul amber
     THE MACHINERY, the ladder rungs, structural observations    --chn slate
     WHERE MARKS DIE, every blind spot, every losing route       --los terracotta
     THE FAMILY labels and the route that is merely correct      --fam teal
     NUMERICS: provenance, counts, every locked decimal          --num mauve

   The signature block is section 03's two-panel figure. Panel A has to show
   DESCENT and a STOPPING POINT, because that is what distinguishes a search
   from a lookup; a flat table of four techniques would have drawn the wrong
   idea. Panel B draws both census columns from ONE baseline on ONE scale,
   because the page's sharpest claim is that the split is EXACT and a shared
   scale is the only way a reader can see two totals as commensurable.

   NO text sits inside either frame and there are no leader lines at all
   (carryover 19.9). Every label lives in a band below its frame, which
   empties the label-versus-curve collision surface by construction.
   ======================================================================== */

/* ---- section numbers and sub-headings --------------------------------- */
.sn161{ font-family:var(--mono); font-size:.62em; font-weight:600;
  letter-spacing:.09em; color:var(--num); vertical-align:.32em;
  margin-right:.55em; }
h3.sh161{ font-size:15.5px; letter-spacing:.005em; margin:30px 0 10px;
  color:var(--ink); font-weight:600; }

/* ---- the quoted stem block -------------------------------------------- */
.stem161{ border-left:2px solid var(--rul); padding:2px 0 2px 18px;
  margin:18px 0 4px; }
.prov161{ font-size:12.5px; color:var(--num); line-height:1.62; margin-top:12px; }

/* ---- the ladder listing ------------------------------------------------ */
pre.ladder161{ font-family:var(--mono); font-size:12.5px; line-height:1.62;
  background:var(--sunk); border:1px solid var(--line); border-radius:3px;
  padding:16px 18px; overflow-x:auto; margin:16px 0; }
pre.ladder161 code{ background:none; padding:0; font-size:inherit;
  color:var(--ink); }

/* ---- the rung tag beside a part heading -------------------------------- */
.rung161{ font-family:var(--mono); font-size:10.5px; font-weight:600;
  letter-spacing:.07em; color:var(--rul); border:1px solid var(--rul);
  border-radius:2px; padding:1px 6px; vertical-align:.18em;
  text-transform:uppercase; }

/* ---- semantic colour, applied through the series tokens ---------------- */
.hi161{ color:var(--rul); font-weight:600; }
.los161{ color:var(--los); }
.win161{ color:var(--fam); font-weight:600; }
.fam161{ color:var(--fam); font-family:var(--mono); font-size:.86em;
  letter-spacing:.05em; }
.chn161{ color:var(--chn); }
.num161{ color:var(--num); font-family:var(--mono); font-size:.88em; }
.mono161{ font-family:var(--mono); font-size:.9em; }
.pk161{ font-family:var(--mono); font-size:.82em; font-weight:600;
  letter-spacing:.06em; color:var(--num); text-transform:uppercase; }
/* MathJax does not inherit its container's colour (carryover 16.7) */
.hi161 mjx-container, .los161 mjx-container, .win161 mjx-container,
.fam161 mjx-container, .chn161 mjx-container, .num161 mjx-container,
.mono161 mjx-container, .pk161 mjx-container{ color:inherit; }
.hi161 mjx-container svg, .los161 mjx-container svg, .win161 mjx-container svg,
.fam161 mjx-container svg, .chn161 mjx-container svg, .num161 mjx-container svg,
.mono161 mjx-container svg, .pk161 mjx-container svg{ fill:currentColor; }

/* ---- the one-sentence thesis ------------------------------------------- */
.thesis161{ font-size:16px; line-height:1.6; font-weight:600; color:var(--ink);
  border-left:3px solid var(--rul); padding:10px 0 10px 18px; margin:20px 0;
  text-wrap:balance; }

/* ---- callout paragraphs ------------------------------------------------ */
p.warn161{ font-size:13.5px; line-height:1.68; color:var(--ink);
  background:var(--sunk); border:1px solid var(--line);
  border-left:2px solid var(--los); border-radius:3px;
  padding:12px 16px; margin:16px 0; }

/* ---- the three blind-spot cards ---------------------------------------- */
/* 17.6's enumerated-breakpoint rule: 3 cells in 3 tracks, then 1. Never
   auto-fit, which cannot satisfy the divide-the-cell-count rule over a
   continuous width range. */
.pgrid161{ display:grid; grid-template-columns:repeat(3,minmax(0,1fr));
  gap:1px; background:var(--line); border:1px solid var(--line);
  border-radius:3px; margin:18px 0; }
@media (max-width:820px){ .pgrid161{ grid-template-columns:minmax(0,1fr); } }
.pcard161{ background:var(--surface); padding:14px 16px 16px; }
.pcard161 p{ font-size:13px; line-height:1.62; margin:8px 0 0; }
.pcard161 .pd161{ color:var(--num); }

/* ---- the trap list ------------------------------------------------------ */
/* ONE content child at column 2 (carryover 4), so nothing wraps into the
   counter column. */
ol.traps161{ list-style:none; counter-reset:t161; padding:0; margin:16px 0; }
ol.traps161 li{ counter-increment:t161; display:grid;
  grid-template-columns:34px minmax(0,1fr); gap:0 6px; margin:0 0 10px; }
ol.traps161 li::before{ content:counter(t161); font-family:var(--mono);
  font-size:11px; font-weight:600; color:var(--num); padding-top:3px; }
ol.traps161 li > span{ grid-column:2; font-size:13.5px; line-height:1.65; }

/* ---- the methods list --------------------------------------------------- */
ul.meth161{ margin:12px 0; padding-left:20px; }
ul.meth161 li{ font-size:13.5px; line-height:1.66; margin:0 0 9px; }

/* ---- figure caption ----------------------------------------------------- */
p.cap161{ font-size:12.5px; line-height:1.62; color:var(--num); margin-top:12px; }
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
    # Never copy the previous run's indices: locate the boundaries and ASSERT them.
    lines = src.split("\n")
    head = "\n".join(lines[:12])
    guard("head slice ends before the first <style>", "<style>" not in head)
    guard("head slice carries the MathJax script", "tex-svg.js" in head)
    guard("head slice carries the font stylesheet", "fonts.googleapis.com" in head)

    last_close = src.rfind("</style>")
    guard("source has a </style>", last_close > 0)
    style_start = src.find("<style>")
    style = src[style_start:last_close + len("</style>")]
    guard("style slice starts with <style>", style.startswith("<style>"))
    guard("style slice ends with </style>", style.endswith("</style>"))
    n_blocks = style.count("<style>")
    guard("style slice carries SEVEN <style> blocks as Q15.5 predicted",
          n_blocks == 7, "found %d" % n_blocks)

    # ---------------------------------------------------------------- FIGURE
    fig = _q161_fig.build()
    guard("figure is pure ASCII", all(ord(c) < 128 for c in fig))
    guard("figure has no var() in a presentation attribute",
          not re.search(r'(fill|stroke)="var\(', fig))
    guard("every figure <text> carries class lab",
          fig.count("<text") == fig.count('class="lab'))
    guard("every figure grid line is exempt from svg-labels",
          fig.count("<line class=\"gridl") + fig.count("<line class=\"srung161")
          == fig.count("<line"))
    guard("figure body placeholder present", "__FIG__" in body)
    body = body.replace("__FIG__", fig)

    # ---------------------------------------------------------------- NAMESPACE GUARD
    # Every class this page invents must appear ZERO times in the inherited slice.
    invented = sorted(set(re.findall(r"\b([a-z]+161)\b", body + STYLE_EXTRA)))
    guard("page invents at least a dozen namespaced classes", len(invented) >= 12)
    for c in invented:
        guard("invented class '%s' does not collide with the slice" % c,
              c not in style)
    # And every class the BODY uses must be styled somewhere (orphan-class guard).
    used = set()
    for attr in re.findall(r'class="([^"]+)"', body):
        for c in attr.split():
            used.add(c)
    # The FIGURE carries its own <style> block (an SVG presentation attribute cannot use
    # var(), so the figure themes itself), and those rules are as real as the page's own.
    # Note this stays a genuine check rather than a tautology: the body USES a class as
    # `class="lab fg161"`, which never contains the string ".fg161" that the rule defines.
    styled = style + STYLE_EXTRA + fig
    orphans = [c for c in sorted(used)
               if c not in KEEP_SERIES and ("." + c) not in styled]
    guard("no orphan classes in the body", not orphans, str(orphans))

    # ---------------------------------------------------------------- TOKEN GUARD
    for tok in TOKENS_USED:
        guard("token %s is defined in slice + EXTRA" % tok,
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
        cells = body.count('class="pcard161"') if g == "pgrid161" else 0
        if cells:
            guard("grid .%s cell count %d divides its %s tracks"
                  % (g, cells, tracks), cells % tracks[0] == 0)
    # DEFECT FOUND AND FIXED: the first version scanned STYLE_EXTRA raw and fired on the word
    # "auto-fit" inside the comment that explains why auto-fit is banned. A guard that reads
    # its own prose is measuring the documentation, not the rules. Strip comments first.
    rules_only = re.sub(r"/\*.*?\*/", "", STYLE_EXTRA, flags=re.S)
    guard("no auto-fit grid on this page (17.6 supersedes 15.6)",
          "auto-fit" not in rules_only)

    # ---------------------------------------------------------------- MATH DELIMITER GUARD
    # The series head configures displayMath as $$ only, so a \[ ... \] block ships as
    # visible raw LaTeX and NO gate reports it (carryover 4).
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
    # A long free-standing INLINE MathJax span is an unbreakable box that overflows the
    # 430px case (carryover 18.7). Spans inside a .tscroll table are exempt at any length.
    stripped = re.sub(r'<div class="tscroll vtab">.*?</div>', "", body, flags=re.S)
    inline = re.findall(r"(?<!\$)\$([^$\n]{1,400})\$(?!\$)", stripped)
    longest = max((len(s) for s in inline), default=0)
    guard("longest free-standing inline math span is short", longest <= 64,
          "longest is %d chars" % longest)

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
    # Seven inherited + this page's EXTRA + the FIGURE's own block. The figure has to carry
    # its own <style> because var() does not resolve inside an SVG presentation attribute,
    # so the figure themes itself through classes. The next page slicing THIS one will
    # therefore inherit NINE.
    n_fig_style = fig.count("<style>")
    guard("the figure carries exactly one <style> block", n_fig_style == 1)
    guard("assembled page has NINE <style> blocks (7 inherited + EXTRA + figure)",
          page.count("<style>") == 7 + 1 + n_fig_style,
          "found %d" % page.count("<style>"))

    io.open(OUT, "w", encoding="utf-8").write(page)
    print("wrote %s  bytes=%d" % (OUT, len(page.encode("utf-8"))))
    print("namespaced classes: %d   deliberate series overrides: %d"
          % (len(invented), len(KEEP_SERIES)))
    print("build guards: %d, all passed" % len(GUARDS))
    print("tables: %d   inline-math longest free-standing span: %d chars"
          % (n_tables, longest))


if __name__ == "__main__":
    main()
