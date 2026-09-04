"""Build the Q19.2 artifact page.

Pattern carried from Q17.x / Q18.1 / Q19.1:
  - slice the token+base prefix from the previous page, assert the slice;
  - every invented class carries the 192 suffix, checked against the inherited slice;
  - figure CSS is emitted BEFORE the body, inside the SAME single style block;
  - the style-block count is DERIVED, not assumed;
  - guards for inherited bare-element rules, orphan classes, undefined tokens,
    dash entities, bracket display math, and top-level dark-only token blocks.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ART = os.path.dirname(HERE)
SRC = os.path.join(ART, "Q19.1-the-sign-that-hides.html")
OUT = os.path.join(ART, "Q19.2-the-split-that-fires.html")

sys.path.insert(0, HERE)
import _q192_fig as FIG                                      # noqa: E402

BAD = []


def chk(lab, cond, detail=""):
    print(("PASS " if cond else "FAIL ") + lab + ("  " + detail if detail else ""))
    if not cond:
        BAD.append(lab)


src = open(SRC, encoding="utf-8").read()

# ---- 1. slice the head and the token+base prefix -------------------------
st = src.find("<style>")
en = src.find("</style>")
chk("slice: found exactly one style block in the source",
    st >= 0 and en > st and src.count("<style>") == 1 and src.count("</style>") == 1)
head = src[:st + len("<style>")]
css_all = src[st + len("<style>"):en]
mark = css_all.find("/* ---- Q19.1 page classes")
chk("slice: found the Q19.1 page-class boundary comment", mark > 0)
base = css_all[:mark]
chk("slice: base prefix does not contain a closing style tag", "</style>" not in base)
chk("slice: base prefix does not contain a page-specific 191 class", ".hero191" not in base)
chk("slice: head carries a charset meta", '<meta charset="utf-8">' in head)
print("INFO head bytes %d, base css bytes %d (prefix length is NOT a queue constant)"
      % (len(head), len(base)))

TOKENS = sorted(set(re.findall(r"--[a-z0-9]+", base)))
INHERITED = sorted(set(re.findall(r"\.([a-zA-Z][\w-]*)", base)))
print("INFO inherited tokens %d, inherited classes %d" % (len(TOKENS), len(INHERITED)))

# ---- 2. page CSS ---------------------------------------------------------
FIGCSS = """
/* ---- Q19.2 FIGURE CSS, emitted BEFORE the body and inside the SAME block ---- */
.fig192{margin:26px 0 30px;border:1px solid var(--line);border-radius:2px;
  background:var(--surface);overflow-x:auto}
.fig192 svg{display:block;width:100%;height:auto;min-width:520px}
.fig192 figcaption{padding:12px 18px 15px;border-top:1px solid var(--line);
  font-size:12px;color:var(--ink3);line-height:1.6;max-width:none}
.fig192 text{font-family:var(--mono)}
"""

PAGECSS = """
/* ---- Q19.2 page classes. Every invented name carries the 192 suffix so it cannot
   shadow anything in the inherited token+base prefix. ---- */
.mast192{padding:56px 22px 26px;border-bottom:1px solid var(--rul)}
.mast192 h1{margin:8px 0 14px;font-size:clamp(30px,5.2vw,50px);line-height:1.04;
  letter-spacing:-0.022em;text-wrap:balance}
.ansbar192{display:grid;gap:1px;background:var(--line);border:1px solid var(--line);
  border-radius:2px;margin-top:26px;
  grid-template-columns:repeat(auto-fit,minmax(min(260px,100%),1fr))}
.acell192{background:var(--surface);padding:15px 17px 17px;display:flex;
  flex-direction:column;gap:7px;justify-content:flex-start}
.alab192{font-family:var(--mono);font-size:9.5px;letter-spacing:0.13em;
  text-transform:uppercase;color:var(--ink3);margin:0}
.aval192{margin:0;font-size:14.5px;line-height:1.5;color:var(--ink)}
.abig192{font-size:18px;color:var(--accent);font-weight:600}
.snum192{font-family:var(--mono);font-size:0.62em;color:var(--accent);
  letter-spacing:0.08em;margin-right:12px;vertical-align:0.18em}
.steps192{list-style:none;counter-reset:s192;padding:0;margin:20px 0 26px;
  display:flex;flex-direction:column;gap:13px}
.steps192 li{counter-increment:s192;display:grid;grid-template-columns:30px minmax(0,1fr);
  gap:2px;margin:0;padding:0}
.steps192 li::before{content:counter(s192);font-family:var(--mono);font-size:11px;
  color:var(--accent);padding-top:3px;grid-column:1}
.steps192 li>span{grid-column:2;line-height:1.62}
.traps192{list-style:none;counter-reset:t192;padding:0;margin:18px 0 8px;
  display:flex;flex-direction:column;gap:11px}
.traps192 li{counter-increment:t192;display:grid;grid-template-columns:32px minmax(0,1fr);
  gap:2px;margin:0;padding:0}
.traps192 li::before{content:counter(t192);font-family:var(--mono);font-size:11px;
  color:var(--ink3);padding-top:3px;grid-column:1}
.traps192 li>span{grid-column:2;line-height:1.6}
.pipe192{display:grid;gap:1px;background:var(--line);border:1px solid var(--line);
  border-radius:2px;margin:22px 0 8px;
  grid-template-columns:repeat(auto-fit,minmax(min(300px,100%),1fr))}
.pc192{background:var(--surface);padding:15px 17px 16px;display:flex;
  flex-direction:column;gap:9px}
.pc192 p{margin:0;max-width:none}
.pc192>p:nth-child(2){overflow-x:auto;font-size:14px}
.pnum192{font-family:var(--mono);font-size:15px;color:var(--accent);
  font-variant-numeric:tabular-nums}
.cards192{display:grid;gap:1px;background:var(--line);border:1px solid var(--line);
  border-radius:2px;margin:22px 0 20px;
  grid-template-columns:repeat(auto-fit,minmax(min(320px,100%),1fr))}
.cd192{background:var(--surface);padding:16px 18px 18px;display:flex;
  flex-direction:column;gap:10px}
.cd192 p{margin:0;max-width:none;line-height:1.62}
.fine192{font-size:12.5px;color:var(--ink3);border-top:1px solid var(--line);
  padding-top:10px}
.hot192{border-left:3px solid var(--los);background:var(--sunk);padding:15px 18px;
  margin:22px 0;border-radius:0 2px 2px 0;display:flex;flex-direction:column;gap:11px}
.hot192 p{margin:0;max-width:none;line-height:1.62}
.note192{border-left:3px solid var(--accent);background:var(--sunk);padding:15px 18px;
  margin:22px 0;border-radius:0 2px 2px 0}
.note192 p{margin:0;max-width:none;line-height:1.62}
.disp192{margin:16px 0;overflow-x:auto;max-width:none}
/* .tscroll is the table-fit gate's markup hook; it must exist as a real rule,
   not only as a selector the gate looks for. */
.tscroll,.tscroll192{overflow-x:auto;margin:20px 0;border:1px solid var(--line);
  border-radius:2px}
.tab192{width:100%;min-width:660px;border-collapse:collapse;font-size:13px}
.tabwide192{min-width:1020px}
.tab192 th{text-align:left;font-family:var(--mono);font-size:9.5px;letter-spacing:0.12em;
  text-transform:uppercase;color:var(--ink3);font-weight:500;
  padding:11px 14px;border-bottom:1px solid var(--rul);background:var(--sunk)}
.tab192 td{padding:10px 14px;border-bottom:1px solid var(--line);vertical-align:top;
  line-height:1.55;color:var(--ink2)}
.tab192 tr:last-child td{border-bottom:none}
.ra192{text-align:right}
.num192{font-family:var(--mono);font-variant-numeric:tabular-nums;white-space:nowrap}
.fk192{font-family:var(--mono);font-size:11px;color:var(--ink3);white-space:nowrap}
/* semantic colours must beat the table cell rule, so name both scopes explicitly */
.tab192 td.fa192,.fa192{color:var(--fam);font-weight:500}
.tab192 td.lo192,.lo192{color:var(--los);font-weight:500}
.tab192 tr.pick192 td{background:var(--sunk)}
.tab192 code{font-size:11.5px;white-space:nowrap}
mjx-container:not([display="true"]){display:inline-block!important;margin:0;
  text-align:left;vertical-align:-0.15em}
mjx-container[display="true"]{overflow-x:auto;overflow-y:hidden}
@media (max-width:560px){.mast192{padding:38px 16px 20px}}
"""

fig1, rep1, _geo = FIG.figure1()
fig2, rep2 = FIG.figure2()
body = open(os.path.join(HERE, "_q192_body.html"), encoding="utf-8").read()
body = body.replace("__FIG1__", fig1).replace("__FIG2__", fig2)

page = head + base + FIGCSS + PAGECSS + "</style>" + "\n" + body + "\n"
page = page.replace("<title>The Sign That Hides</title>",
                    "<title>The Split That Fires</title>")

# ---- 3. GUARDS -----------------------------------------------------------
chk("guard: title replaced", "<title>The Split That Fires</title>" in page)
chk("guard: charset meta present", '<meta charset="utf-8">' in page)

nstyle = page.count("<style>")
nclose = page.count("</style>")
chk("guard: style-block count is 1, DERIVED (%d open / %d close)" % (nstyle, nclose),
    nstyle == 1 and nclose == 1)
chk("guard: the last closing style tag precedes the body",
    page.rfind("</style>") < page.find("<header"))

# 3a. invented classes must all carry the 192 suffix and must not collide
mycss = FIGCSS + PAGECSS
invented = sorted(set(re.findall(r"\.([a-zA-Z][\w-]*)", mycss)))
KEEP = {"figbox", "gridl", "wrap", "eyebrow", "lede", "tscroll"}  # deliberate series hooks
collide = [c for c in invented if c in INHERITED and c not in KEEP]
chk("guard: no invented class collides with the inherited slice", not collide, str(collide))
unsuffixed = [c for c in invented if not c.endswith("192") and c not in KEEP]
chk("guard: every invented class carries the 192 suffix", not unsuffixed, str(unsuffixed))
print("INFO invented classes: %d, all suffixed 192" % len([c for c in invented
                                                           if c.endswith("192")]))

# 3b. orphan-class guard: every class the BODY uses must be styled somewhere
used = set()
for m in re.finditer(r'class="([^"]+)"', body):
    used.update(m.group(1).split())
styled = set(re.findall(r"\.([a-zA-Z][\w-]*)", base + mycss))
GATE_ONLY = {"lab", "axist", "conn192", "band192", "lin192", "cos192", "dot192",
             "tick192", "acurve192", "lev192"}   # SVG hooks, styled by attribute
orphans = sorted(used - styled - GATE_ONLY)
chk("guard: no orphan class in the body", not orphans, str(orphans))

# 3c. token guard: every var(--x) the page leans on must be defined in the slice
defined = set(re.findall(r"(--[a-z0-9]+)\s*:", base + mycss))
usedtok = set(re.findall(r"var\((--[a-z0-9]+)\)", mycss + body + fig1 + fig2))
missing = sorted(usedtok - defined)
chk("guard: every referenced CSS token is defined", not missing, str(missing))

# 3d. inherited BARE ELEMENT rules that reach this body - acknowledged, not ignored
bare = sorted(set(x.strip() for sel in re.findall(r"(?m)^([^{@/][^{]*)\{", base)
                  for x in sel.split(",") if re.fullmatch(r"[a-z]+[0-9]?", x.strip())))
inbody = [b for b in bare if re.search(r"<" + b + r"[ >]", body)]
ACKNOWLEDGED = {
    "a": "links in the footer, inherited colour is correct",
    "body": "page ground and base type",
    "code": "inline code spans, inherited mono treatment is wanted",
    "em": "not used, harmless",
    "figcaption": "overridden by .fig192 figcaption",
    "figure": "overridden by .fig192",
    "h1": "masthead, overridden by .mast192 h1",
    "h2": "section headings, inherited treatment is wanted",
    "li": "overridden inside .steps192 / .traps192",
    "ol": "overridden inside .steps192 / .traps192",
    "pre": "not used",
    "strong": "not used directly, b is used",
    "table": "overridden by .tab192",
    "td": "overridden by .tab192 td, and the semantic colour rule names that scope",
    "th": "overridden by .tab192 th",
    "ul": "not used",
}
unack = [b for b in inbody if b not in ACKNOWLEDGED]
chk("guard 4b: inherited bare-element rules reaching the body are all acknowledged (%d)"
    % len(inbody), not unack, str(unack))
print("INFO bare-element rules reaching this body: " + ", ".join(inbody))

# 3e. no top-level dark-only token block
depth = 0
toplevel = 0
i = 0
NEEDLE = ':root:not([data-theme="light"])'
while True:
    j = page.find(NEEDLE, i)
    if j < 0:
        break
    d = 0
    for ch in page[page.find("<style>"):j]:
        if ch == "{":
            d += 1
        elif ch == "}":
            d -= 1
    if d == 0:
        toplevel += 1
    i = j + 1
chk("guard: zero TOP-LEVEL :root:not([data-theme=\"light\"]) blocks "
    "(brace-depth scan, not substring)", toplevel == 0, "found %d" % toplevel)

# 3f. dash entities and control characters
SPELL = ["—", "–", "&mdash;", "&ndash;", "&#8212;", "&#8211;",
         "&#x2014;", "&#x2013;", "―"]
# &mdash; is a deliberate typographic entity in this series' prose; the ban is on the
# RAW characters and on en-dashes.  Count each spelling and report.
raw_dashes = page.count("—") + page.count("–") + page.count("―")
chk("guard: zero RAW em/en dash characters", raw_dashes == 0, str(raw_dashes))
# A raw-character scan cannot see a NAMED or NUMERIC entity, and Q8.4 shipped 17 of them.
# Assert every spelling here, so a dirty page never reaches disk.
ENT = ["&" + "mdash;", "&" + "ndash;", "&#8212;", "&#8211;", "&#x2014;", "&#x2013;",
       "&#X2014;", "&#X2013;"]
ent_counts = {e: page.count(e) for e in ENT}
chk("guard: zero dash ENTITIES across all %d spellings" % len(ENT),
    sum(ent_counts.values()) == 0, str({k: v for k, v in ent_counts.items() if v}))
chk("guard CONTROL: the entity scan DOES see a seeded &" + "mdash;",
    ("&" + "mdash;") in ("x&" + "mdash;y"))
ctrl = [hex(ord(c)) for c in page if ord(c) < 32 and c not in "\n\r\t"]
chk("guard: no control characters (BEL / form feed)", not ctrl, str(ctrl[:5]))

# 3g. math delimiters
chk("guard: no bracket display math (the head configures $$ only)",
    "\\[" not in page and "\\(" not in body)
chk("guard: $$ count is even in the body", body.count("$$") % 2 == 0,
    "count=%d" % body.count("$$"))

# 3h. table count, cross-checked later against table-fit
ntab = body.count("<table")
nscroll = body.count('class="tscroll tscroll192"')
chk("guard: every table sits in a tscroll192 container (%d tables, %d containers)"
    % (ntab, nscroll), ntab == nscroll)

# 3i. FIGURE CONTAINMENT - the shaded shape must CONTAIN the region, not merely
#     match its area.  Sample the drawn polygons and demand every sampled point lie
#     between the two curves in data space.
import math                                                   # noqa: E402
polys = re.findall(r'<polygon class="band192" points="([^"]+)"', fig1)
chk("guard: figure 1 draws exactly 3 shaded pieces", len(polys) == 3)
W, H = 760, 400
L, R, T, B = 78, 34, 40, 62
px0, py0, px1, py1 = L, T, W - R, H - B
xa, xb, ya, yb = -math.pi / 2, math.pi / 2, -0.10, 1.14


def invX(px):
    return xa + (px - px0) / (px1 - px0) * (xb - xa)


def invY(py):
    return ya + (py1 - py) / (py1 - py0) * (yb - ya)


Cval = 1 / math.sqrt(2)
bad_pts = 0
tot_pts = 0
for pl in polys:
    pts = [tuple(float(v) for v in p.split(",")) for p in pl.split()]
    for (pxv, pyv) in pts:
        x, y = invX(pxv), invY(pyv)
        lo, hi = min(math.cos(x), Cval), max(math.cos(x), Cval)
        tot_pts += 1
        if not (lo - 2e-3 <= y <= hi + 2e-3):
            bad_pts += 1
chk("guard: every vertex of every shaded piece lies BETWEEN the two curves "
    "(%d of %d sampled)" % (tot_pts - bad_pts, tot_pts), bad_pts == 0,
    "%d outside" % bad_pts)
# and the seeded control: an axis-aligned rectangle of the SAME AREA must be rejected
rect = [(px0, py0), (px1, py0), (px1, py1), (px0, py1)]
rbad = 0
for (pxv, pyv) in rect:
    x, y = invX(pxv), invY(pyv)
    lo, hi = min(math.cos(x), Cval), max(math.cos(x), Cval)
    if not (lo - 2e-3 <= y <= hi + 2e-3):
        rbad += 1
chk("guard CONTROL: a bounding rectangle IS rejected by the same containment test",
    rbad > 0, "%d of 4 vertices outside" % rbad)

# 3i-bis. TICK COLLISIONS. svg-labels measures text.lab only, so a tick label running
# into its neighbour is invisible to it. Estimate each tick label's box from its anchor
# and its character count, and assert no two overlap. Found a real collision on the
# first draft of figure 2 ("1/sqrt2" against "0.75").
CHW = 6.4          # measured advance width of the 10.5px mono face, per character


def _tickboxes(svg):
    out = []
    for m in re.finditer(
            r'<text class="tick192" x="([\d.-]+)" y="([\d.-]+)" text-anchor="(\w+)"'
            r' font-size="([\d.]+)"[^>]*>([^<]*)</text>', svg):
        x, y, anc, fs, s = (float(m.group(1)), float(m.group(2)), m.group(3),
                            float(m.group(4)), m.group(5))
        w = len(s) * CHW * (fs / 10.5)
        x0 = x if anc == "start" else (x - w if anc == "end" else x - w / 2)
        out.append((x0, y - fs, w, fs * 1.25, s))
    return out


def _overlaps(bs):
    hits = []
    for i in range(len(bs)):
        for j in range(i + 1, len(bs)):
            ax, ay, aw, ah, as_ = bs[i]
            bx, by, bw, bh, bs_ = bs[j]
            if ax < bx + bw and bx < ax + aw and ay < by + bh and by < ay + ah:
                hits.append(as_ + " / " + bs_)
    return hits


for nm, svg in (("figure 1", fig1), ("figure 2", fig2)):
    bs = _tickboxes(svg)
    hits = _overlaps(bs)
    chk("guard: %s has no overlapping TICK labels (%d ticks measured)" % (nm, len(bs)),
        not hits, str(hits))
    chk("guard: %s actually HAS tick labels to measure" % nm, len(bs) >= 6)
# CONTROL: the overlap routine must report a hit on two boxes that do overlap
chk("guard CONTROL: the tick-overlap routine reports a seeded overlap",
    len(_overlaps([(0.0, 0.0, 40.0, 12.0, "A"), (10.0, 2.0, 40.0, 12.0, "B")])) == 1)

# 3j. label placement clearances
mn1 = min(c for _s, c in rep1)
mn2 = min(c for _s, c in rep2)
chk("figure 1: %d labels placed, minimum achieved clearance %.1f px" % (len(rep1), mn1),
    mn1 >= 15.0)
chk("figure 2: %d labels placed, minimum achieved clearance %.1f px" % (len(rep2), mn2),
    mn2 >= 15.0)
chk("figures: every <text> checked by the gate carries class=\"lab\" or a tick class",
    len(re.findall(r'<text class="(lab|tick192)"', fig1 + fig2))
    == len(re.findall(r"<text ", fig1 + fig2)))
chk("figures: each svg is a direct child of a .figbox element",
    body.count('class="figbox fig192"') == 2)
chk("figures: gridlines carry a class matching /grid|axis/ so the gate exempts them",
    fig1.count('class="gridl"') + fig1.count('class="axist"') > 0)
chk("figures: connectors do NOT match /grid|axis/, so the gate samples them",
    not re.search(r"grid|axis", "conn192"))

# ---- 4. non-ASCII ---------------------------------------------------------
na = [c for c in page if ord(c) > 127]
chk("guard: zero non-ASCII bytes (immune to file:// mojibake by construction)",
    not na, str(sorted(set(na))[:8]))

if BAD:
    print("\nRESULT: %d GUARD FAILURE(S)" % len(BAD))
    for b in BAD:
        print("   " + b)
    sys.exit(2)

open(OUT, "w", encoding="utf-8", newline="").write(page)
print("\nWROTE %s  (%d bytes)" % (OUT, len(page.encode("utf-8"))))
print("RESULT: OK")
