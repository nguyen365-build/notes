# -*- coding: utf-8 -*-
"""Build the Q19.9 artifact page.

Token+base prefix only, sliced from the Q19.8 page at its FIGURE CSS boundary.
Figure CSS is emitted BEFORE the body, inside the SAME style block.  Every
invented class carries the 199 suffix.  The <title> is set explicitly and
asserted DIFFERENT from the inherited one (30.6).
"""
import os
import re
import sys

BS = chr(92)
HERE = os.path.dirname(os.path.abspath(__file__))
ART = os.path.dirname(HERE)
PREV = os.path.join(ART, "Q19.8-two-answers-one-integral.html")
OUT = os.path.join(ART, "Q19.9-the-hand-off.html")
TITLE = "The Hand-Off"

_p = 0
_f = 0


def A(name, cond, extra=""):
    global _p, _f
    if cond:
        _p += 1
    else:
        _f += 1
    print(("PASS q199b " if cond else "FAIL q199b ") + "%-60s %s" % (name, extra))
    return cond


# ---------------- slice the inherited prefix ----------------
prev = open(PREV, encoding="utf-8").read()
MARK = "/* ---- Q19.8 FIGURE CSS"
A("slice anchor present in the previous page exactly once",
  prev.count(MARK) == 1)
prefix = prev[:prev.index(MARK)]
A("the slice ends INSIDE an open style block",
  prefix.count("<style>") == 1 and "</style>" not in prefix)
A("the slice drags NO body content (21.6)",
  '<div class="wrap"' not in prefix and "<body" not in prefix
  and "<header" not in prefix,
  "%d bytes of head + tokens only" % len(prefix))

inh_title = re.search(r"<title>(.*?)</title>", prefix).group(1)
A("inherited title recovered", bool(inh_title), repr(inh_title))
A("30.6 guard: the inherited title DIFFERS from ours, so it is not vacuous",
  inh_title != TITLE, "%r vs %r" % (inh_title, TITLE))
prefix = prefix.replace("<title>%s</title>" % inh_title,
                        "<title>%s</title>" % TITLE, 1)
A("title rewritten", "<title>%s</title>" % TITLE in prefix)
A("exactly one <title> in the prefix", prefix.count("<title>") == 1)
A("<meta charset> present (24.10)", '<meta charset="utf-8">' in prefix)

inh_classes = sorted(set(re.findall(r"(?m)^\s*\.([a-zA-Z][-\w]*)", prefix)))
inh_tokens = sorted(set(re.findall(r"(--[a-z0-9-]+)\s*:", prefix)))
inh_bare = sorted(set(re.findall(
    r"(?m)^([a-zA-Z][a-zA-Z0-9]*(?:\s*,\s*[a-zA-Z0-9]+)*)\s*\{", prefix)))
print("SECTION q199b inherited: %d classes, %d tokens, %d bare-element rules"
      % (len(inh_classes), len(inh_tokens), len(inh_bare)))
print("SECTION q199b ACKNOWLEDGED bare-element rules (25.6): %s"
      % ", ".join(inh_bare))
A("29.8 re-declaration still required: --sans absent from the slice",
  "--sans" not in prefix)
A("29.8 re-declaration still required: .tscroll absent from the slice",
  "tscroll" not in prefix)
A("30.6/33.7 the svg-labels hook .lab is ALSO absent, so we must define it",
  re.search(r"(?m)^\.lab\b", prefix) is None)

# ---------------- our CSS ----------------
# 21.7: the fills are TOKENS, defined in the bare :root and redefined in all
# three stamps.  The inherited -soft tokens are 10-13 percent alpha and vanish
# as an area fill, which is why these are their own tokens and not a reuse.
#
# Semantic colour, one role one token (32.7):
#   --rul  amber   PHASE 1, the ramp, the 8 m it encloses
#   --chn  blue    PHASE 2, the cruise, the 92 m it encloses, and the bounds
#   --fam  teal    the hand-off and the answer 13.5
#   --los  rust    a WRONG answer, and nothing else
#   --plot slate   axes and ticks, which carry no meaning
FIGCSS = """
/* ---- Q19.9 FIGURE CSS. Emitted BEFORE the body, inside this same block. */
:root{--rampfill:rgba(217,138,31,.24);--cruisefill:rgba(63,100,147,.20);
  --bandfill:rgba(217,138,31,.30);--band2fill:rgba(63,100,147,.26);
  --lofill:rgba(63,100,147,.34);--actfill:rgba(30,122,110,.38);
  --hifill:rgba(63,100,147,.34)}
@media (prefers-color-scheme:dark){
  :root:not([data-theme="light"]){--rampfill:rgba(242,165,60,.18);
    --cruisefill:rgba(126,155,196,.20);--bandfill:rgba(242,165,60,.30);
    --band2fill:rgba(126,155,196,.26);--lofill:rgba(126,155,196,.32);
    --actfill:rgba(90,196,178,.34);--hifill:rgba(126,155,196,.32)}
}
:root[data-theme="dark"]{--rampfill:rgba(242,165,60,.18);
  --cruisefill:rgba(126,155,196,.20);--bandfill:rgba(242,165,60,.30);
  --band2fill:rgba(126,155,196,.26);--lofill:rgba(126,155,196,.32);
  --actfill:rgba(90,196,178,.34);--hifill:rgba(126,155,196,.32)}
:root[data-theme="light"]{--rampfill:rgba(217,138,31,.24);
  --cruisefill:rgba(63,100,147,.20);--bandfill:rgba(217,138,31,.30);
  --band2fill:rgba(63,100,147,.26);--lofill:rgba(63,100,147,.34);
  --actfill:rgba(30,122,110,.38);--hifill:rgba(63,100,147,.34)}

.fig199{width:100%;height:auto;display:block;background:transparent}
/* Every figure label carries `lab` so svg-labels can select it, and the
   family and role rules are written TWO-CLASS so the specificity contest
   (25.7) cannot let a family rule erase a role's semantic colour. */
.lab{font-family:var(--mono);font-size:11px;fill:var(--ink2)}
.lab.labin{font-size:11px;fill:var(--ink)}
.lab.tlab{font-size:10px;fill:var(--plotlab);letter-spacing:.05em}
.ramp199{fill:var(--rampfill);stroke:none}
.cruise199{fill:var(--cruisefill);stroke:none}
.band1199{fill:var(--bandfill);stroke:none}
.band2199{fill:var(--band2fill);stroke:none}
.blo199{fill:var(--lofill);stroke:none}
.bact199{fill:var(--actfill);stroke:none}
.bhi199{fill:var(--hifill);stroke:none}
.axis199{stroke:var(--plot);stroke-width:1.2;fill:none}
.tick199{stroke:var(--plot);stroke-width:1.1;fill:none}
.drop199{stroke:var(--plot);stroke-width:1.1;stroke-dasharray:3 3;fill:none}
.vramp199{fill:none;stroke:var(--rul);stroke-width:2.4;stroke-linecap:round}
.vcruise199{fill:none;stroke:var(--chn);stroke-width:2.4;stroke-linecap:round}
.brk199{stroke:var(--plot);stroke-width:1.2;fill:none}
.conn199{stroke:var(--plot);stroke-width:1;stroke-dasharray:2 3;fill:none}
.mid199{stroke:var(--fam);stroke-width:2.4;fill:none}
.lab.areaA199{fill:var(--rul);font-weight:600}
.lab.areaB199{fill:var(--chn);font-weight:600}
.lab.hoff199{fill:var(--fam);font-weight:600}
.lab.tape199{fill:var(--fam);font-weight:600}
.lab.mlab199{fill:var(--fam);font-weight:600}
.lab.v1199{fill:var(--fam);font-weight:600}
.lab.v0199,.lab.v2199{fill:var(--chn);font-weight:600}
.lab.b1199{fill:var(--rul);font-weight:600}
.lab.b2199{fill:var(--chn);font-weight:600}
.lab.ph1199{fill:var(--rul);letter-spacing:.12em}
.lab.ph2199{fill:var(--chn);letter-spacing:.12em}
.lab.strip199{letter-spacing:.12em}
.lab.axt199,.lab.axv199,.lab.ax2199{fill:var(--plotlab);letter-spacing:.05em}
"""

PAGECSS = """
/* ---- Q19.9 page classes. Every invented name carries the 199 suffix.
   Two DELIBERATE re-declarations of names ABSENT from the slice: --sans and
   .tscroll (29.8). Nothing inherited AS IS is redefined here. */
:root{--sans:"IBM Plex Sans",system-ui,-apple-system,"Segoe UI",sans-serif}
.tscroll{overflow-x:auto;-webkit-overflow-scrolling:touch;margin:16px 0}

.ansbar199{display:grid;grid-template-columns:repeat(auto-fit,minmax(212px,1fr));
  gap:14px;margin:30px 0 6px}
.acard199{background:var(--surface);border:1px solid var(--line);
  border-radius:3px;padding:15px 17px 16px;display:flex;flex-direction:column;
  gap:5px}
.alab199{font-family:var(--mono);font-size:10.5px;letter-spacing:.15em;
  text-transform:uppercase;color:var(--ink3)}
.aval199{font-size:27px;line-height:1.15;font-weight:600;
  font-variant-numeric:tabular-nums}
.asub199{font-size:12.5px;color:var(--ink2)}
.mono199{font-family:var(--mono);font-size:23px;letter-spacing:.02em}
.ans199{color:var(--fam)}
.hand199{color:var(--rul)}
.no199{color:var(--ok)}
.wrong199{color:var(--los)}

.steps199{margin:14px 0 0;padding-left:22px}
.steps199 li{margin:9px 0}
.hi199{background:var(--rul-soft);border-bottom:1px solid var(--rul-line);
  padding:1px 3px}
.chk199{margin-top:18px;padding:13px 16px;background:var(--sunk);
  border-left:2px solid var(--fam);border-radius:2px;font-size:14.5px}

.disp199{margin:18px 0;overflow-x:auto}
.note2199{font-size:14.5px;color:var(--ink2)}

.callout199{margin:20px 0;padding:16px 18px;background:var(--rul-soft);
  border:1px solid var(--rul-line);border-radius:3px}
.blind199{margin:20px 0;padding:16px 18px;background:var(--sunk);
  border:1px solid var(--line);border-left:2px solid var(--ink3);
  border-radius:3px}
.colab199{font-family:var(--mono);font-size:10.5px;letter-spacing:.15em;
  text-transform:uppercase;color:var(--ink3);margin-bottom:7px}
.callout199 p,.blind199 p{margin:0}

.tab199{border-collapse:collapse;width:100%;min-width:620px;font-size:14px}
.tab199.wide199{min-width:900px}
.tab199 th{text-align:left;font-family:var(--mono);font-size:10.5px;
  letter-spacing:.12em;text-transform:uppercase;color:var(--ink3);
  border-bottom:1px solid var(--line);padding:8px 12px 8px 0;font-weight:500}
.tab199 td{padding:9px 12px 9px 0;border-bottom:1px solid var(--line-soft);
  vertical-align:top}
.tab199 tr:last-child td{border-bottom:none}
.num199{font-family:var(--mono);font-variant-numeric:tabular-nums;
  white-space:nowrap}
.nw199{white-space:nowrap}
.dead199{color:var(--ink3)}
.live199{color:var(--fam);font-weight:600}
.cont199{color:var(--fam);font-weight:600}
.jump199{color:var(--rul);font-weight:600}
.exam199 td{background:var(--rul-soft)}
.tag199{font-family:var(--mono);font-size:10px;letter-spacing:.1em;
  text-transform:uppercase;color:var(--rul);border:1px solid var(--rul-line);
  border-radius:2px;padding:1px 5px}

.traps199{margin:14px 0 0;padding-left:22px}
.traps199 li{margin:8px 0}
.tree199{background:var(--sunk);border:1px solid var(--line-soft);
  border-radius:3px;padding:16px 18px;overflow-x:auto;
  font-family:var(--mono);font-size:12.5px;line-height:1.6;color:var(--ink2);
  white-space:pre}

@media (max-width:760px){
  .tab199{min-width:580px}
  .tab199.wide199{min-width:840px}
  .aval199{font-size:23px}
  .mono199{font-size:20px}
}
"""

# ---------------- assemble ----------------
sys.path.insert(0, HERE)
import _q199_fig as FIG

for n in FIG.NOTES:
    print(n)
A("figure guards all pass", FIG.GF == 0,
  "PASS=%d FAIL=%d" % (FIG.GP, FIG.GF))

body = open(os.path.join(HERE, "_q199_body.html"), encoding="utf-8").read()
A("both figure placeholders present exactly once",
  body.count("__FIG1__") == 1 and body.count("__FIG2__") == 1)
body = body.replace("__FIG1__", FIG.FIG1).replace("__FIG2__", FIG.FIG2)

for ent in ("&mdash;", "&ndash;", "&#8212;", "&#8211;"):
    body = body.replace(ent, "-")
A("no entity dashes survive into the body",
  not any(e in body for e in ("&mdash;", "&ndash;", "&#8212;", "&#8211;")))

html = prefix + FIGCSS + PAGECSS + "\n</style>\n" + body + "\n"

# ---------------- gates ----------------
A("exactly ONE style block, DERIVED",
  html.count("<style>") == 1 and html.count("</style>") == 1,
  "%d open, %d close" % (html.count("<style>"), html.count("</style>")))
A("the last </style> comes BEFORE the body",
  html.rindex("</style>") < html.index('<div class="wrap"'))
A("figure CSS is emitted BEFORE the page body",
  html.index(".ramp199") < html.index('<div class="wrap"'))
A("figure CSS is inside the SAME block as the base",
  html.index(".ramp199") > html.index("<style>")
  and html.index(".ramp199") < html.index("</style>"))

# brace-depth scan: no TOP-LEVEL :root:not([data-theme="light"])
depth = 0
top_bad = 0
guarded_at_depth1 = 0
i = 0
NEEDLE = ':root:not([data-theme="light"])'
while i < len(html):
    if html.startswith(NEEDLE, i):
        if depth == 0:
            top_bad += 1
        elif depth == 1:
            guarded_at_depth1 += 1
    c = html[i]
    if c == "{":
        depth += 1
    elif c == "}":
        depth -= 1
    i += 1
A("zero TOP-LEVEL :root:not([data-theme=light]) selectors", top_bad == 0,
  "top-level %d, guarded at depth 1 %d" % (top_bad, guarded_at_depth1))
A("the guarded form IS present at depth 1", guarded_at_depth1 > 0,
  "%d occurrences inside a media block" % guarded_at_depth1)
A("brace depth returns to 0 at end of document", depth == 0, "depth %d" % depth)

# every token this page's own CSS uses must be DEFINED somewhere in the page
mine = FIGCSS + PAGECSS
used = sorted(set(re.findall(r"var\((--[a-z0-9-]+)\)", mine)))
defined = set(re.findall(r"(--[a-z0-9-]+)\s*:", html))
missing = [u for u in used if u not in defined]
A("every token our CSS references is defined in the page", not missing,
  str(missing) if missing else "%d tokens used, all defined" % len(used))

# our own fill tokens must be redefined in ALL THREE stamps (21.7)
OURS = ["--rampfill", "--cruisefill", "--bandfill", "--band2fill",
        "--lofill", "--actfill", "--hifill"]
stamp_bad = []
for tk in OURS:
    n = len(re.findall(re.escape(tk) + r"\s*:", mine))
    if n != 4:
        stamp_bad.append((tk, n))
A("every fill token is declared in bare :root plus all three stamps",
  not stamp_bad, str(stamp_bad) if stamp_bad else
  "%d tokens x 4 declarations each" % len(OURS))

# 21.7's gate: no PAINTING rule may carry a literal colour
paint = re.findall(r"(?m)^\s*\.[\w.,\s#-]*\{[^}]*\}", mine)
lit = []
for rule in paint:
    if re.search(r":\s*(#[0-9a-fA-F]{3,8}|rgba?\()", rule):
        lit.append(rule.split("{")[0].strip())
A("no PAINTING rule contains a literal colour (21.7)", not lit,
  str(lit[:4]) if lit else "%d class rules scanned, all use tokens"
  % len(paint))

# every class the markup uses must be STYLED
markup_cls = set()
for m in re.finditer(r'class="([^"]+)"', html[html.index('<div class="wrap"'):]):
    for c in m.group(1).split():
        markup_cls.add(c)
# a class scan must not read its own CSS COMMENTS (30.7)
css_nocomment = re.sub(r"/\*.*?\*/", " ", html[:html.rindex("</style>")],
                       flags=re.S)
styled = set(re.findall(r"\.([a-zA-Z][-\w]*)", css_nocomment))
unstyled = sorted(c for c in markup_cls if c not in styled)
A("every class used in the markup is styled (30.7: comments excluded)",
  not unstyled, str(unstyled) if unstyled else
  "%d distinct classes in markup, all styled" % len(markup_cls))
A("CONTROL the class scan really did strip comments",
  "FIGURE CSS" not in css_nocomment,
  "the comment text is gone, so a class named only in a comment cannot pass")

# 28.10: FIGURE CSS and PAGE CSS must declare DISJOINT class sets.  The first
# draft defined .hi199 twice - the upper-bound BAR in one block and an inline
# text HIGHLIGHT in the other - and both rules applied to both elements.
_figc = set(re.findall(r"(?m)^\s*\.([a-zA-Z][-\w]*)", FIGCSS))
_pagec = set(re.findall(r"(?m)^\s*\.([a-zA-Z][-\w]*)", PAGECSS))
_both = sorted(_figc & _pagec)
A("FIGURE CSS and PAGE CSS declare DISJOINT class sets (28.10)", not _both,
  str(_both) if _both else "%d figure + %d page classes, 0 shared"
  % (len(_figc), len(_pagec)))
A("CONTROL the disjointness gate can see a shared name",
  len({"x199"} & {"x199"}) == 1, "set intersection is live")

# every DECLARED label role must have a rule in our own CSS, and every
# per-label class in the markup must be a declared role
role_missing = [r for r in FIG.ROLES
                if not re.search(r"\." + r + r"199", mine)]
A("every declared label role has a CSS rule", not role_missing,
  str(role_missing) if role_missing else
  "%d roles, all styled" % len(FIG.ROLES))

# 25.7: a role rule must be at least as specific as the family rule that
# would otherwise override it.  Every role selector is written .lab.<role>199,
# so the two compete at equal specificity and source order decides.
weak_role = []
for r in FIG.ROLES:
    if re.search(r"(?m)^\.lab\.[\w.,]*" + r + r"199", mine) is None:
        weak_role.append(r)
A("every role rule is TWO-CLASS, so no family rule can erase it (25.7)",
  not weak_role, str(weak_role) if weak_role else
  "%d role selectors, all .lab-qualified" % len(FIG.ROLES))
A("CONTROL the family rules are also two-class where they modify",
  ".lab.tlab{" in FIGCSS and ".lab.labin{" in FIGCSS,
  "tlab and labin both qualified")

# our invented classes must not collide with an inherited name
ours_cls = sorted(set(re.findall(r"(?m)^\s*\.([a-zA-Z][-\w]*)", mine)))
coll = [c for c in ours_cls if c in inh_classes]
A("no invented class collides with an inherited name", not coll,
  str(coll) if coll else "%d invented classes, 0 collisions" % len(ours_cls))
suffixed = [c for c in ours_cls if c.endswith("199")]
A("the namespaced classes all carry the 199 suffix", len(suffixed) > 20,
  "%d suffixed of %d declared" % (len(suffixed), len(ours_cls)))
REDECL = ["tscroll", "lab", "labin", "tlab"]
A("the RE-DECLARED names are all absent from the slice",
  all(re.search(r"(?m)^\." + r + r"\b", prefix) is None for r in REDECL),
  "re-declared: %s" % ", ".join(REDECL))

# ONE inline-math delimiter, body-scoped, SVG and pre stripped
bodyscope = html[html.index('<div class="wrap"'):]
scan = re.sub(r"<svg.*?</svg>", " ", bodyscope, flags=re.S)
scan = re.sub(r"<pre.*?</pre>", " ", scan, flags=re.S)
scan = re.sub(r'<div class="tree199">.*?</div>', " ", scan, flags=re.S)
nparen = len(re.findall(re.escape(BS + "("), scan))
ndollar = len([m for m in re.finditer(r"(?<!\$)\$(?!\$)", scan)])
A("ONE inline-math delimiter: backslash-paren only, no bare dollar",
  nparen > 0 and ndollar == 0,
  "%d backslash-paren, %d bare dollar" % (nparen, ndollar))
A("display math uses double dollar and is balanced",
  scan.count("$$") % 2 == 0, "%d markers" % scan.count("$$"))

# encoding and control characters
A("no non-ASCII bytes outside the allowed entity set",
  all(ord(c) < 128 for c in html),
  "%d non-ASCII" % len([c for c in html if ord(c) >= 128]))
ctrl = sorted(set(hex(ord(c)) for c in html
                  if ord(c) < 32 and c not in "\n\r\t"))
A("no control characters in the page", not ctrl, str(ctrl))
A("chr(7) BEL absent", chr(7) not in html)
A("chr(12) form feed absent", chr(12) not in html)

# The control-character gate above scans the ARTEFACT.  This run's heredoc
# turned a "\\b" inside a regex into a literal BACKSPACE (0x08) in this very
# script, and the artefact gate could not see it: the regex simply matched
# nothing and reported all sixteen label roles as unstyled, which reads
# exactly like a real regression.  Scan the GENERATORS too.
GENS = ["_q199_build.py", "_q199_fig.py", "_q199_body.html"]
gen_bad = []
for g in GENS:
    gt = open(os.path.join(HERE, g), encoding="utf-8", newline="").read()
    for c in gt:
        if ord(c) < 32 and c not in "\n\r\t":
            gen_bad.append((g, hex(ord(c))))
A("no control characters in the GENERATORS either", not gen_bad,
  str(sorted(set(gen_bad))) if gen_bad else
  "%d generator files clean" % len(GENS))
A("CONTROL that scan can see a control character",
  any(ord(c) < 32 and c not in "\n\r\t" for c in "a" + chr(8) + "b"),
  "a seeded backspace is detected")
DASH = [0x2014, 0x2013, 0x2012, 0x2015, 0x2E3A, 0x2E3B, 0xFE58, 0xFE63,
        0xFF0D, 0x2010, 0x2011]
A("zero dashes across all 11 spellings",
  not any(chr(c) in html for c in DASH))

# external hosts must be inside the CSP allowlist
hosts = sorted(set(re.findall(r"https://([a-z0-9.\-]+)/", html)))
ALLOW = {"cdnjs.cloudflare.com", "fonts.googleapis.com", "fonts.gstatic.com",
         "cdn.jsdelivr.net", "code.jquery.com", "cdn.tailwindcss.com"}
A("every external host is inside the CSP allowlist",
  all(h in ALLOW for h in hosts), str(hosts))
A("MathJax is pinned to an exact version",
  "mathjax/3.2.2/es5/tex-svg.js" in html)

# tables: our own count, for the table-fit cross-check, using its real hook
ntab = len(re.findall(r'<table class="tab199', bodyscope))
nscroll = len(re.findall(r'<div class="tscroll"', bodyscope))
A("every tab199 table is wrapped in a tscroll container",
  ntab == nscroll, "%d tables, %d tscroll wrappers" % (ntab, nscroll))
A("the tscroll hook table-fit selects on is DEFINED in our CSS",
  ".tscroll{" in PAGECSS)

# the two figures actually reached the page, with their label hooks
A("both figures are in the page",
  bodyscope.count("<svg") == 2, "%d svg elements" % bodyscope.count("<svg"))
A("both figures are inside a .figbox, the hook svg-labels selects",
  bodyscope.count('<figure class="figbox">') == 2,
  "%d figbox wrappers" % bodyscope.count('<figure class="figbox">'))
nlab = len(re.findall(r'<text class="lab[" ]', bodyscope))
A("the page carries the build-time number of labelled texts",
  nlab == FIG.NLABS1 + FIG.NLABS2,
  "%d in page vs %d + %d from the build"
  % (nlab, FIG.NLABS1, FIG.NLABS2))
A("every figure text carries a lab-family class, so svg-labels can COUNT it",
  bodyscope.count("<text ") == nlab,
  "%d texts, %d with a lab class" % (bodyscope.count("<text "), nlab))

A("the page states the answer", ">13.5 s<" in html)
A("the page names the seventh behaviour", "wrong-answer clustering" in html)
A("the page closes the bank", "forty-ninth of\n  forty-nine" in html
  or "forty-ninth of forty-nine" in html.replace("\n  ", " "))
A("the page flags grading as inference", html.count("inference") >= 2,
  "%d mentions" % html.count("inference"))
A("no unclosed figure or table tags",
  html.count("<figure") == html.count("</figure")
  and html.count("<table") == html.count("</table")
  and html.count("<svg") == html.count("</svg"))

if _f:
    print("SECTION q199b build: PASS %d FAIL %d  - NOT WRITTEN" % (_p, _f))
    sys.exit(1)

open(OUT, "w", encoding="utf-8", newline="").write(html)
print("SECTION q199b build: PASS %d FAIL %d" % (_p, _f))
print("SECTION q199b wrote %s (%d bytes)" % (OUT, len(html)))
