"""Assemble the Q10.2 artifact from the series head + stylesheet + this page's body."""
import sys
sys.dont_write_bytecode = True   # keep __pycache__ out of this content directory
import io
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ART = os.path.dirname(HERE)
SRC = os.path.join(ART, "Q10.1-implicit-differentiation.html")
OUT = os.path.join(ART, "Q10.2-tangent-to-implicit-curve.html")

src = io.open(SRC, encoding="utf-8").read().split("\n")
head = "\n".join(src[0:12])            # title + fonts + MathJax config + script
style = "\n".join(src[12:321])         # <style> ... up to but NOT including </style>
assert style.lstrip().startswith("<style>"), style[:60]
assert "</style>" not in style, "slice ran past the closing tag"
assert 'mjx-container:not([display="true"])' in style, "inline-MathJax fix missing"
assert ':root:not([data-theme="light"])' in style
assert ':root[data-theme="dark"]' in style

# ---- this page's name ------------------------------------------------------
head = head.replace("<title>The y-prime Ledger</title>",
                    "<title>The Point Must Be On The Curve</title>")
assert "The Point Must Be On The Curve" in head
assert "y-prime Ledger" not in head

# ---- what the five accent hues mean on THIS page ---------------------------
old = re.search(r"/\* ===== ops console.*?\*/", style, re.S)
assert old, "legend comment not found"
new = """/* ===== ops console, MATH 265 series ========================================
   Palette and type are the series system, unchanged since Q1.1.  What is
   specific to THIS page is what the five accent hues MEAN.  Q9.1 was a
   four-station pipeline.  Q10.1 was a ledger of the y' binary.  Q10.2 is a
   JOIN: it invents no technique.  It welds Q10.1's derivative to Q9.1's line
   and adds exactly one obligation - that the point be proved to lie on the
   curve first.  So the two loudest hues carry INHERITED against ADDED, and
   the page's signature block is the three-way exit at the solve step, which
   is the one thing students never draw.

     ADDED here     (what Q10.2 contributes)             --rul   amber
     INHERITED      (from Q10.1 and Q9.1)                --chn   slate
     WHERE MARKS DIE                                     --los   terracotta
     THE VARIATION families                              --fam   teal
     NUMERICS: gates, arms, tolerances, controls         --num   mauve
   ========================================================================= */"""
style = style[:old.start()] + new + style[old.end():]
INHERITED = style          # snapshot BEFORE this page's own EXTRA is appended

EXTRA = """
/* --- header spacing -------------------------------------------------------
   The series .wrap carries a 110px BOTTOM padding meant for the page end.
   The header shares that class, so without this the page opens with a large
   empty band under the answer bar - the same defect found on Q8.4, and no
   layout gate reports it.  Scope the page-bottom padding to main.wrap. ---- */
header.hdr{padding-top:30px;padding-bottom:30px}

/* --- answer bar under the standfirst ------------------------------------- */
.ansbar{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));
  gap:1px;background:var(--line);border:1px solid var(--line);border-radius:3px;margin-top:26px}
.ansbar > div{background:var(--surface);padding:13px 16px;display:flex;flex-direction:column;gap:5px}
.ansbar .k{font-family:var(--mono);font-size:10px;letter-spacing:.09em;
  text-transform:uppercase;color:var(--ink3)}
.ansbar .v{font-size:17px;color:var(--rul);font-weight:600}
.ansbar .v.mono{font-family:var(--mono);font-size:15px}

/* --- the inherit / add ledger -------------------------------------------- */
.ledger{display:grid;grid-template-columns:repeat(auto-fit,minmax(330px,1fr));
  gap:1px;background:var(--line);border:1px solid var(--line);border-radius:3px;margin:22px 0}
.ledger .col{background:var(--surface);padding:18px 20px}
.ledger .col.add{background:var(--rul-soft)}
.ledger .colh{font-family:var(--mono);font-size:10px;letter-spacing:.09em;
  text-transform:uppercase;margin:0 0 12px;color:var(--chn)}
.ledger .col.add .colh{color:var(--rul)}
.ledger ul{margin:0;padding-left:18px;display:flex;flex-direction:column;gap:10px}
.ledger li{font-size:14.5px;line-height:1.62}

/* --- the 30-second card --------------------------------------------------- */
pre.card30{font-family:var(--mono);font-size:13px;line-height:1.66;background:var(--surface2);
  border:1px solid var(--line);border-left:3px solid var(--rul);border-radius:3px;
  padding:18px 20px;overflow-x:auto;margin:20px 0;color:var(--ink)}

/* --- special-points grid under the figure -------------------------------- */
.pgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));
  gap:1px;background:var(--line);border:1px solid var(--line);border-radius:3px;margin:22px 0}
.pcard{background:var(--surface);padding:15px 17px;display:flex;flex-direction:column;gap:7px}
.pcard .pk{margin:0;font-size:16px;font-weight:600}
.pcard .pv{margin:0;font-family:var(--mono);font-size:10px;letter-spacing:.08em;
  text-transform:uppercase;color:var(--ink3)}
.pcard .pd{margin:0;font-size:13.5px;line-height:1.6;color:var(--ink2)}
.pcard.main{background:var(--rul-soft)} .pcard.main .pk{color:var(--rul)}
.pcard.fam .pk{color:var(--fam)}
.pcard.los .pk{color:var(--los)}
.pcard.sing .pk{color:var(--ink2)}

/* --- route comparison ----------------------------------------------------- */
.routes{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));
  gap:1px;background:var(--line);border:1px solid var(--line);border-radius:3px;margin:22px 0}
.rt{background:var(--surface);padding:18px 20px}
.rt.pick{background:var(--rul-soft)}
.rth{margin:0 0 12px;font-family:var(--mono);font-size:11px;letter-spacing:.08em;
  text-transform:uppercase;color:var(--ink2);display:flex;flex-wrap:wrap;gap:8px;align-items:baseline}
.rt.pick .rth{color:var(--rul)}
.tag{font-size:9.5px;letter-spacing:.08em;padding:2px 7px;border-radius:2px;
  background:var(--surface2);color:var(--ink3);border:1px solid var(--line)}
.tag.on{background:var(--rul);color:var(--ground);border-color:var(--rul);font-weight:600}
.rt p{font-size:14px;line-height:1.6}
.rt .sv,.rt mjx-container[display="true"]{overflow-x:auto;overflow-y:hidden}
.cost{color:var(--ink2);font-size:13.5px;border-top:1px solid var(--line);padding-top:11px;margin-top:14px}

/* --- procedure steps + the three-way exit --------------------------------- */
ol.steps{margin:18px 0;padding-left:22px;display:flex;flex-direction:column;gap:11px}
ol.steps li{font-size:15px;line-height:1.64}
.exits{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));
  gap:1px;background:var(--line);border:1px solid var(--line);border-radius:3px;margin:20px 0}
.ex{background:var(--surface);padding:16px 18px;display:flex;flex-direction:column;gap:8px}
.ex .exh{margin:0;font-family:var(--mono);font-size:10.5px;letter-spacing:.07em;color:var(--ink3)}
.ex .exm{margin:0;font-size:16px;font-weight:600}
.ex p:last-child{margin:0;font-size:13.5px;line-height:1.6;color:var(--ink2)}
.ex.ok{background:var(--rul-soft)} .ex.ok .exm{color:var(--rul)}
.ex.vert .exm{color:var(--los)}
.ex.sing .exm{color:var(--num)}
.then{border-left:3px solid var(--rul);padding:11px 16px;background:var(--surface2);
  border-radius:0 3px 3px 0;font-size:14.5px}

/* --- verification + drill tables ------------------------------------------ */
.vtab{overflow-x:auto;margin:20px 0;border:1px solid var(--line);border-radius:3px}
.vtab table{border-collapse:collapse;width:100%;min-width:700px;font-size:13.5px}
.vtab th{background:var(--surface2);text-align:left;padding:10px 14px;font-family:var(--mono);
  font-size:10px;letter-spacing:.08em;text-transform:uppercase;color:var(--ink3);
  border-bottom:1px solid var(--line);white-space:nowrap}
.vtab td{padding:10px 14px;border-bottom:1px solid var(--line);vertical-align:top;line-height:1.55}
.vtab tr:last-child td{border-bottom:0}
.vtab td.g{font-family:var(--mono);font-size:12px;color:var(--num);white-space:nowrap}
.vtab td.ok{color:var(--fam);font-family:var(--mono);font-size:12px;white-space:nowrap}
.vtab td.mono{font-family:var(--mono);font-variant-numeric:tabular-nums}
.vtab td.yes{color:var(--los);font-weight:600}
.vtab td.no{color:var(--ink3)}
.vtab td.fmc{font-family:var(--mono);font-size:12px;color:var(--fam);font-weight:600}
.tot{font-size:15px;border-left:3px solid var(--fam);padding:11px 16px;
  background:var(--surface2);border-radius:0 3px 3px 0}

/* --- trap list -------------------------------------------------------------
   .traps is a SERIES class: a two-column grid, 34px counter + content.  Do not
   redeclare its layout here - just give the single wrapped content child room
   and the right measure.  Redeclaring display:flex on the ol fought it. ----- */
.traps li > span{display:block;font-size:14.5px;line-height:1.62;max-width:76ch}
.traps li{margin-bottom:13px}

/* --- inline mono, and the emphasis callout ---------------------------------
   The series sheet scopes .mono to td/th only, and defines .note but no .warn,
   so both need declaring or they render as ordinary prose. -------------------*/
span.mono,.e li .mono{font-family:var(--mono);font-size:12.5px;color:var(--rul)}
p.warn{border:1px solid var(--line);border-left:3px solid var(--los);
  background:var(--los-soft);border-radius:0 3px 3px 0;padding:13px 17px;
  font-size:14px;line-height:1.62;max-width:none}

/* --- the eleven families -------------------------------------------------- */
.fams{display:grid;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));
  gap:1px;background:var(--line);border:1px solid var(--line);border-radius:3px;margin:22px 0}
.fm{background:var(--surface);padding:16px 18px;display:flex;flex-direction:column;gap:7px}
.fm .fh{margin:0;font-size:14.5px;font-weight:600;color:var(--fam)}
.fm .ft{margin:0;font-family:var(--mono);font-size:11px;color:var(--ink3);line-height:1.5}
.fm p:last-child{margin:0;font-size:13.5px;line-height:1.6;color:var(--ink2)}

/* --- answer entry --------------------------------------------------------- */
.entry{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));
  gap:1px;background:var(--line);border:1px solid var(--line);border-radius:3px;margin:20px 0}
.e{background:var(--surface);padding:16px 18px}
.e .eh{margin:0 0 11px;font-family:var(--mono);font-size:10px;letter-spacing:.09em;
  text-transform:uppercase}
.e.do .eh{color:var(--fam)} .e.dont .eh{color:var(--los)}
.e.dont{background:var(--los-soft)}
.e ul{margin:0;padding-left:17px;display:flex;flex-direction:column;gap:8px}
.e li{font-size:13.5px;line-height:1.55}

/* --- figure caption ------------------------------------------------------- */
.cap{margin:12px 0 0;font-size:13.5px;color:var(--ink3);max-width:74ch;line-height:1.65}

/* --- footer --------------------------------------------------------------- */
.ftr{border-top:1px solid var(--line);padding-top:24px;margin-top:8px}
.ftr .fk{font-family:var(--mono);font-size:10px;letter-spacing:.09em;text-transform:uppercase;
  color:var(--ink3);margin:16px 0 6px}
.ftr p{font-size:13.5px;line-height:1.65;color:var(--ink2);max-width:82ch}
"""
style = style + EXTRA + "\n</style>"


# ---- class-collision guard -------------------------------------------------
# Reusing a class name the series stylesheet already defines silently inherits
# its layout.  .traps cost this run a one-word-wide list that every gate passed.
# Names that must be NEW.  ".cap" and ".note" are deliberate overrides of a
# series rule (same element, this sheet comes later, so the cascade resolves
# in our favour); ".traps" is now USED as the series defines it, not redefined.
_mine = ("ansbar", "ledger", "card30", "pgrid", "pcard", "routes", "rt", "rth",
         "exits", "vtab", "tot", "fams", "entry", "ftr")
_deliberate = ("cap", "traps", "note", "mono")
for _c in _deliberate:
    assert len(re.findall(r"\.%s[^a-zA-Z0-9_-]" % _c, style)) > 0,         "expected .%s to be a series class; if it vanished, restyle it here" % _c
_inherited = INHERITED
for _c in _mine:
    _hits = len(re.findall(r"\.%s[^a-zA-Z0-9_-]" % _c, _inherited))
    assert _hits == 0, "class .%s collides with the series stylesheet (%d hits)" % (_c, _hits)

# ---- body, with the computed figure spliced in -----------------------------
body = io.open(os.path.join(HERE, "_q102_body.html"), encoding="utf-8").read()
svg = io.open(os.path.join(HERE, "_q102_fig.svg"), encoding="utf-8").read()
assert "FIGURE_SVG" in body
body = body.replace("FIGURE_SVG", svg)

page = head + "\n" + style + "\n\n" + body + "\n"

# ---- pre-flight gates ------------------------------------------------------
bad = [hex(ord(c)) for c in page if ord(c) < 32 and c not in "\n\r\t"]
assert not bad, "control characters: %s" % bad
assert chr(0x2014) not in page and chr(0x2013) not in page, "raw dash character in page"
for sp in ("&mdash;", "&ndash;", "&#8212;", "&#8211;", "&#x2014;", "&#x2013;"):
    assert sp not in page, "dash entity in page: %s" % sp
for tag in ("<!doctype", "<html", "<head>", "<body>"):
    assert tag not in page.lower(), "publish skeleton tag present: %s" % tag
# svg-labels.mjs markup contract
assert 'class="figbox"' in page
assert page.count("<svg") == 1
assert 'class="gridl"' in page, "grid lines must be classed or the gate samples them"
assert 'class="lab"' in page, "labels must carry .lab"
# theme contract
assert ':root:not([data-theme="light"])' in page
assert ':root[data-theme="dark"]' in page
assert "background-color:var(--ground)" in page, "body must paint an explicit ground"

io.open(OUT, "w", encoding="utf-8", newline="\n").write(page)
print("wrote", OUT)
print("bytes", len(page.encode("utf-8")))
print("non-ascii:", sorted({c for c in page if ord(c) > 126}))
