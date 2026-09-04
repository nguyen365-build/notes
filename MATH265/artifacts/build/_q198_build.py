# -*- coding: utf-8 -*-
"""Build the Q19.8 artifact page.

Token+base prefix only, sliced from the Q19.7 page at its first FIGURE CSS
boundary. Figure CSS is emitted BEFORE the body, inside the SAME style block.
Every invented class carries the 198 suffix. The <title> is set explicitly and
asserted DIFFERENT from the inherited one (30.6).
"""
import os
import re
import sys

BS = chr(92)
HERE = os.path.dirname(os.path.abspath(__file__))
ART = os.path.dirname(HERE)
PREV = os.path.join(ART, "Q19.7-the-interval-runs-backwards.html")
OUT = os.path.join(ART, "Q19.8-two-answers-one-integral.html")
TITLE = "Two Answers, One Integral"

_p = 0
_f = 0


def A(name, cond, extra=""):
    global _p, _f
    if cond:
        _p += 1
    else:
        _f += 1
    print(("PASS q198b " if cond else "FAIL q198b ") + "%-58s %s" % (name, extra))


# ---------------- slice the inherited prefix ----------------
prev = open(PREV, encoding="utf-8").read()
MARK = "/* ---- Q19.2 FIGURE CSS"
A("slice anchor present in the previous page exactly once", prev.count(MARK) == 1)
prefix = prev[:prev.index(MARK)]
A("the slice ends INSIDE an open style block",
  prefix.count("<style>") == 1 and "</style>" not in prefix)
A("the slice drags NO body content", "<div class=\"wrap\"" not in prefix and "<body" not in prefix)

inh_title = re.search(r"<title>(.*?)</title>", prefix).group(1)
A("inherited title recovered", bool(inh_title), repr(inh_title))
A("30.6 guard: the inherited title is DIFFERENT from ours, so the guard is not vacuous",
  inh_title != TITLE, "%r vs %r" % (inh_title, TITLE))
prefix = prefix.replace("<title>%s</title>" % inh_title, "<title>%s</title>" % TITLE, 1)
A("title rewritten", "<title>%s</title>" % TITLE in prefix)
A("exactly one <title> in the prefix", prefix.count("<title>") == 1)
A("<meta charset> present", '<meta charset="utf-8">' in prefix)

inh_classes = sorted(set(re.findall(r"(?m)^\s*\.([a-zA-Z][-\w]*)", prefix)))
inh_tokens = sorted(set(re.findall(r"(--[a-z0-9-]+)\s*:", prefix)))
inh_bare = sorted(set(re.findall(r"(?m)^([a-zA-Z][a-zA-Z0-9]*(?:\s*,\s*[a-zA-Z0-9]+)*)\s*\{", prefix)))
print("SECTION q198b inherited: %d classes, %d tokens, %d bare-element rules"
      % (len(inh_classes), len(inh_tokens), len(inh_bare)))
print("SECTION q198b ACKNOWLEDGED bare-element rules: %s" % ", ".join(inh_bare))
A("29.8 re-declaration still required: --sans absent from the slice", "--sans" not in prefix)
A("29.8 re-declaration still required: .tscroll absent from the slice", "tscroll" not in prefix)

# ---------------- our CSS ----------------
FIGCSS = """
/* ---- Q19.8 FIGURE CSS. Emitted BEFORE the body, inside this same block.
   Semantic roles, one role one token: amber = forward motion and the signed
   answer; blue = the backward piece that creates the gap; teal = the unsigned
   odometer; rust = a wrong answer and nothing else; slate = a FOURTH neutral
   for axes and ticks, which carry no meaning. The inherited -soft tokens are
   10-13 percent alpha and vanish as an area fill, so the two bands below carry
   their own stronger fills. No gridlines are drawn. */
/* 21.7: the first build hard-coded these two fills, so ONE theme's palette was
   being applied in BOTH. They are tokens now, defined in the bare :root for
   light and redefined in all three dark/light stamps, exactly like the inherited
   set. The inherited -soft tokens are 10-13 percent alpha and disappear as an
   area fill, which is why these are their own tokens rather than a reuse. */
:root{--fwdfill:rgba(217,138,31,.22);--bwdfill:rgba(63,100,147,.20)}
@media (prefers-color-scheme:dark){
  :root:not([data-theme="light"]){--fwdfill:rgba(242,165,60,.17);--bwdfill:rgba(126,155,196,.22)}
}
:root[data-theme="dark"]{--fwdfill:rgba(242,165,60,.17);--bwdfill:rgba(126,155,196,.22)}
:root[data-theme="light"]{--fwdfill:rgba(217,138,31,.22);--bwdfill:rgba(63,100,147,.20)}
.lab{font-family:var(--mono)}
.fig198{width:100%;height:auto;display:block;background:transparent}
.fbg198{fill:var(--sunk)}
.fwd198{fill:var(--fwdfill);stroke:none}
.bwd198{fill:var(--bwdfill);stroke:none}
.ax198{stroke:var(--plot);stroke-width:1.2;fill:none}
.curve198{fill:none;stroke:var(--ink);stroke-width:2.1;stroke-linejoin:round}
.odo198{fill:none;stroke:var(--fam);stroke-width:2.4;stroke-linejoin:round}
.pos198{fill:none;stroke:var(--rul);stroke-width:2.4;stroke-linejoin:round}
.tie198{stroke:var(--plot);stroke-width:1.1;stroke-dasharray:3 3;fill:none}
.root198{fill:var(--chn);stroke:var(--sunk);stroke-width:1.6}
.endpos198{fill:var(--rul);stroke:var(--sunk);stroke-width:1.6}
.endodo198{fill:var(--fam);stroke:var(--sunk);stroke-width:1.6}
.tick198{fill:var(--plotlab);font-family:var(--mono);font-size:12.5px}
.axlab198{fill:var(--plotlab);font-family:var(--mono);font-size:12.5px;letter-spacing:.04em}
.areaf198{fill:var(--rul);font-family:var(--mono);font-size:12.5px;font-weight:600}
.areab198{fill:var(--chn);font-family:var(--mono);font-size:12.5px;font-weight:600}
.note198{fill:var(--ink2);font-family:var(--mono);font-size:12.5px}
.lodo198{fill:var(--fam);font-family:var(--mono);font-size:12.5px;font-weight:600}
.lpos198{fill:var(--rul);font-family:var(--mono);font-size:12.5px;font-weight:600}
.lsub198{fill:var(--ink3);font-family:var(--mono);font-size:11px;letter-spacing:.05em}
"""

PAGECSS = """
/* ---- Q19.8 page classes. Every invented name carries the 198 suffix.
   Three DELIBERATE overrides of inherited names are declared below and each is
   asserted actually defined: --sans and .tscroll are absent from the slice
   (29.8), and .wide198 is new rather than an override. */
:root{--sans:"IBM Plex Sans",system-ui,-apple-system,"Segoe UI",sans-serif}
.tscroll{overflow-x:auto;-webkit-overflow-scrolling:touch;margin:16px 0}

.ansbar198{display:grid;grid-template-columns:repeat(auto-fit,minmax(215px,1fr));
  gap:14px;margin:30px 0 6px}
.acard198{background:var(--surface);border:1px solid var(--line);border-radius:3px;
  padding:15px 17px 16px;display:flex;flex-direction:column;gap:5px}
.alab198{font-family:var(--mono);font-size:10.5px;letter-spacing:.15em;text-transform:uppercase;
  color:var(--ink3)}
.aval198{font-size:27px;line-height:1.15;font-weight:600;font-variant-numeric:tabular-nums}
.asub198{font-size:12.5px;color:var(--ink2)}
.mono198{font-family:var(--mono);font-size:19px;letter-spacing:.02em}
.sig198{color:var(--rul)}
.uns198{color:var(--fam)}
.no198{color:var(--los)}
.ok198{color:var(--ok)}

.steps198{margin:14px 0 0;padding-left:22px}
.steps198 li{margin:9px 0}
.hi198{background:var(--rul-soft);border-bottom:1px solid var(--rul-line);padding:1px 3px}
.chk198{margin-top:18px;padding:13px 16px;background:var(--sunk);
  border-left:2px solid var(--fam);border-radius:2px;font-size:14.5px}

.disp198{margin:18px 0;overflow-x:auto}
.note2198{font-size:14.5px;color:var(--ink2)}

.callout198{margin:20px 0;padding:16px 18px;background:var(--rul-soft);
  border:1px solid var(--rul-line);border-radius:3px}
.blind198{margin:20px 0;padding:16px 18px;background:var(--sunk);
  border:1px solid var(--line);border-left:2px solid var(--ink3);border-radius:3px}
.colab198{font-family:var(--mono);font-size:10.5px;letter-spacing:.15em;text-transform:uppercase;
  color:var(--ink3);margin-bottom:7px}
.callout198 p,.blind198 p{margin:0}

.tab198{border-collapse:collapse;width:100%;min-width:640px;font-size:14px}
.tab198.wide198{min-width:880px}
.tab198 th{text-align:left;font-family:var(--mono);font-size:10.5px;letter-spacing:.12em;
  text-transform:uppercase;color:var(--ink3);border-bottom:1px solid var(--line);
  padding:8px 12px 8px 0;font-weight:500}
.tab198 td{padding:9px 12px 9px 0;border-bottom:1px solid var(--line-soft);
  vertical-align:top}
.tab198 tr:last-child td{border-bottom:none}
.num198{font-family:var(--mono);font-variant-numeric:tabular-nums;white-space:nowrap}
.nw198{white-space:nowrap}
.yes198{color:var(--fam);font-weight:600}
.dead198{color:var(--ink3)}
.live198{color:var(--fam);font-weight:600}
.exam198 td{background:var(--rul-soft)}
.tag198{font-family:var(--mono);font-size:10px;letter-spacing:.1em;text-transform:uppercase;
  color:var(--rul);border:1px solid var(--rul-line);border-radius:2px;padding:1px 5px}

.traps198{margin:14px 0 0;padding-left:22px}
.traps198 li{margin:8px 0}
.tree198{background:var(--sunk);border:1px solid var(--line-soft);border-radius:3px;
  padding:16px 18px;overflow-x:auto;font-family:var(--mono);font-size:12.5px;
  line-height:1.6;color:var(--ink2);white-space:pre}

@media (max-width:760px){
  .tab198{min-width:600px}
  .tab198.wide198{min-width:820px}
  .aval198{font-size:23px}
}
"""

# ---------------- assemble ----------------
sys.path.insert(0, HERE)
import _q198_fig as FIG

s1, s2, figlog, figtot = FIG.build()
for l in figlog:
    print(l)
A("figure guards all pass", figtot[1] == 0, "PASS=%d FAIL=%d" % (figtot[0], figtot[1]))

body = open(os.path.join(HERE, "_q198_body.html"), encoding="utf-8").read()
A("both figure placeholders present", body.count("__FIG1__") == 1 and body.count("__FIG2__") == 1)
body = body.replace("__FIG1__", s1).replace("__FIG2__", s2)

# the dash gate covers NAMED ENTITIES too, so fold them before they ship
for ent, rep in (("&mdash;", "-"), ("&ndash;", "-"), ("&#8212;", "-"), ("&#8211;", "-")):
    body = body.replace(ent, rep)
A("no entity dashes survive into the body",
  not any(e in body for e in ("&mdash;", "&ndash;", "&#8212;", "&#8211;")))

html = prefix + FIGCSS + PAGECSS + "\n</style>\n" + body + "\n"

# ---------------- gates ----------------
A("exactly ONE style block, DERIVED", html.count("<style>") == 1 and html.count("</style>") == 1,
  "%d open %d close" % (html.count("<style>"), html.count("</style>")))
A("the last </style> comes BEFORE the body",
  html.rindex("</style>") < html.index('<div class="wrap"'))
A("figure CSS is emitted BEFORE the page body",
  html.index(".fig198") < html.index('<div class="wrap"'))
A("figure CSS is inside the SAME block as the base",
  html.index(".fig198") > html.index("<style>") and html.index(".fig198") < html.rindex("</style>"))

# ONE inline-math delimiter, body-scoped with SVG stripped
bodyonly = html[html.index('<div class="wrap"'):]
nosvg = re.sub(r"<svg.*?</svg>", " ", bodyonly, flags=re.S)
nocode = re.sub(r"<pre.*?</pre>", " ", nosvg, flags=re.S)
n_paren = len(re.findall(r"\\\(", nocode))
n_dollar = len(re.findall(r"(?<![$\\])\$(?!\$)", nocode))
A("ONE inline-math delimiter is used", n_paren > 0 and n_dollar == 0,
  "backslash-paren %d, bare dollar %d" % (n_paren, n_dollar))
A("inline math delimiters balance", n_paren == len(re.findall(r"\\\)", nocode)),
  "open %d close %d" % (n_paren, len(re.findall(r"\\\)", nocode))))
A("display math balances", nocode.count(r"\[") == nocode.count(r"\]"))

# zero top-level :root:not([data-theme="light"]) by a brace-depth scan
css = html[html.index("<style>") + 7:html.rindex("</style>")]
depth = 0
toplevel_guarded = 0
guarded_at_1 = 0
i = 0
while i < len(css):
    if css.startswith(':root:not([data-theme="light"])', i):
        if depth == 0:
            toplevel_guarded += 1
        elif depth == 1:
            guarded_at_1 += 1
    if css[i] == "{":
        depth += 1
    elif css[i] == "}":
        depth -= 1
    i += 1
A("zero TOP-LEVEL :root:not([data-theme=light]) by a brace-depth scan", toplevel_guarded == 0,
  "top-level %d" % toplevel_guarded)
A("the guarded block IS present at depth 1", guarded_at_1 >= 1, "depth-1 %d" % guarded_at_1)
A("brace depth returns to zero", depth == 0, "depth %d" % depth)

# every class USED is defined, and the scan must not read its own CSS comments (30.7)
css_nocomment = re.sub(r"/\*.*?\*/", " ", css, flags=re.S)
defined = set(re.findall(r"\.([a-zA-Z][-\w]*)", css_nocomment))
used = set()
for m in re.finditer(r'class="([^"]+)"', bodyonly):
    used.update(m.group(1).split())
undef = sorted(used - defined)
A("every class USED in the body is DEFINED in the CSS", not undef, str(undef))
A("30.7 the class scan skips CSS comments",
  "q198f1" not in defined and len(css_nocomment) < len(css))
mine = sorted(c for c in used if c.endswith("198"))
overrides = sorted(c for c in used if not c.endswith("198"))
print("SECTION q198b %d namespaced classes used, %d deliberate inherited names: %s"
      % (len(mine), len(overrides), ", ".join(overrides)))
# An inherited name is used in one of two ways, and they need DIFFERENT assertions.
# Conflating them is what made the first version of this gate fail on five names it
# had no business checking.
prefix_defined = set(re.findall(r"\.([a-zA-Z][-\w]*)", re.sub(r"/\*.*?\*/", " ", prefix, flags=re.S)))
mine_defined = set(re.findall(r"\.([a-zA-Z][-\w]*)",
                              re.sub(r"/\*.*?\*/", " ", FIGCSS + PAGECSS, flags=re.S)))
as_is = [o for o in overrides if o in prefix_defined]
redecl = [o for o in overrides if o not in prefix_defined]
print("SECTION q198b inherited AS IS: %s | RE-DECLARED here: %s"
      % (", ".join(as_is), ", ".join(redecl)))
for o in as_is:
    A("inherited-as-is %s is defined in the SLICE" % o, o in prefix_defined)
    A("inherited-as-is %s is NOT silently re-defined here" % o, o not in mine_defined)
for o in redecl:
    A("re-declared %s is absent from the slice AND defined here" % o,
      o not in prefix_defined and o in mine_defined)
A("the re-declared set is exactly tscroll and lab, both absent from the slice",
  sorted(redecl) == ["lab", "tscroll"], str(sorted(redecl)))
A("every SVG text carries the svg-labels hook",
  html.count("<text class=\"lab ") == html.count("<text "),
  "%d hooked of %d" % (html.count("<text class=\"lab "), html.count("<text ")))
A("no invented class collides with an inherited name",
  not (set(mine) & set(inh_classes)), str(sorted(set(mine) & set(inh_classes))))

# tables cross-check against the real .tscroll hook
n_tab = bodyonly.count("<table")
n_scroll = bodyonly.count('class="tscroll"')
A("every table sits in its own .tscroll container", n_tab == n_scroll,
  "%d tables, %d tscroll" % (n_tab, n_scroll))

# non-ASCII / control characters / hosts
nonascii = sorted(set(c for c in html if ord(c) > 127))
A("zero non-ASCII bytes", not nonascii, str(nonascii))
A("no control characters", not [c for c in html if ord(c) < 32 and c not in "\n\r\t"])
A("chr(7) BEL absent", chr(7) not in html)
A("chr(12) form feed absent", chr(12) not in html)
DASHES = [0x2014, 0x2013, 0x2012, 0x2015, 0x2E3A, 0x2E3B, 0xFE58, 0xFE63, 0xFF0D, 0x2010, 0x2011]
A("zero dashes across all 11 spellings", not any(chr(c) in html for c in DASHES))
hosts = sorted(set(re.findall(r"https://([a-z0-9.]+)/", html)))
A("external hosts are exactly the CSP allowlist",
  set(hosts) <= set(["cdnjs.cloudflare.com", "fonts.googleapis.com", "fonts.gstatic.com"]),
  str(hosts))
A("title is ours and appears exactly once",
  html.count("<title>%s</title>" % TITLE) == 1 and html.count("<title>%s</title>" % inh_title) == 0)
A("both figures present", html.count("<svg class=\"fig198\"") == 2)
# 21.7: no colour may be hard-coded outside a token declaration, or one theme's
# palette ships in both. Every rule that PAINTS must go through var(--...).
paint = re.findall(r"(?m)^\.[\w.]+\d{3}\{([^}]*)\}", FIGCSS + PAGECSS)
hard = [d for d in paint if re.search(r"(?:#[0-9a-fA-F]{3,8}|rgba?\()", d)]
A("no hard-coded colour in any painting rule; all go through tokens", not hard, str(hard))
for tok in ("--fwdfill", "--bwdfill"):
    A("%s defined in the bare :root (light)" % tok,
      re.search(r":root\{[^}]*" + tok, FIGCSS) is not None)
    A("%s redefined for BOTH dark stamps" % tok,
      (FIGCSS.count(tok) - 1) >= 3, "%d definitions" % FIGCSS.count(tok))
# 22.11: a gate that cannot SEE the figure reports nothing, and nothing reads as a
# pass. svg-labels selects '.figbox > svg', so the hook must be present and the
# svg must be a DIRECT child.
A("svg-labels hook .figbox present on both figures", html.count('class="figbox"') == 2)
A("each svg is a DIRECT child of its .figbox",
  len(re.findall(r'<figure class="figbox">\s*<svg', html)) == 2,
  str(len(re.findall(r'<figure class="figbox">\s*<svg', html))))

if _f:
    print("SECTION q198b BUILD FAILED, nothing written")
    sys.exit(1)
open(OUT, "w", encoding="utf-8", newline="").write(html)
print("SECTION q198b WROTE %s (%d bytes)" % (OUT, len(html.encode("utf-8"))))
print("SECTION q198b BUILD PASS=%d FAIL=%d" % (_p, _f))
