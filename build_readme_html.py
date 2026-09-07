"""Build README.html: a self-contained, MathJax-rendered HTML render of README.md
for reading in a browser (desktop and mobile).

Math ($...$ and $$...$$) is pulled out before Markdown conversion (so
underscores/asterisks inside LaTeX are never touched by the Markdown parser)
and spliced back in afterwards -- into BOTH the body and the auto-generated
TOC -- HTML-escaped, for MathJax to render.

Placeholder tokens use a Private Use Area Unicode marker (built with chr(),
not a literal character -- literal characters written to disk in this
environment have been observed getting silently mangled) so they cannot
collide with literal text. A plain "MATH0", "MATH1", ... scheme was tried
first and rejected: it corrupts any literal digit-suffixed word in the
document that happens to match a placeholder index.

Same build pattern as build_math265_mobile.py, but for the general README
(not the mobile-landscape 2x-font variant) and using MathJax's SVG output
with global font caching per the user-supplied reference config.
"""
import re
import html
import markdown

SRC = "README.md"
OUT = "README.html"

MARK_OPEN = chr(0xE000)
MARK_CLOSE = chr(0xE001)
PLACEHOLDER_RE = re.compile(re.escape(MARK_OPEN) + r"(\d+)" + re.escape(MARK_CLOSE))

with open(SRC, "r", encoding="utf-8") as f:
    text = f.read()

# --- 1. pull out math spans, block ($$...$$) before inline ($...$) ---------
math_spans = []

def stash(m):
    math_spans.append(m.group(0))
    return MARK_OPEN + str(len(math_spans) - 1) + MARK_CLOSE

text = re.sub(r"\$\$.+?\$\$", stash, text, flags=re.DOTALL)
text = re.sub(r"(?<!\\)\$(?!\$)[^\n$]+?(?<!\\)\$", stash, text)

n_stashed = len(PLACEHOLDER_RE.findall(text))
assert n_stashed == len(math_spans), f"stash count mismatch: {n_stashed} vs {len(math_spans)}"

# --- 2. markdown -> HTML -----------------------------------------------------
md = markdown.Markdown(extensions=["tables", "fenced_code", "sane_lists", "toc"],
                        extension_configs={"toc": {"permalink": False}})
body_html = md.convert(text)
toc_html = md.toc if hasattr(md, "toc") else ""

# --- 3. splice math back in, HTML-escaped, in BOTH body and toc ------------
def restore(m):
    idx = int(m.group(1))
    return html.escape(math_spans[idx], quote=False)

body_html, n_body = PLACEHOLDER_RE.subn(restore, body_html)
toc_html, n_toc = PLACEHOLDER_RE.subn(restore, toc_html)

assert n_body == len(math_spans), (
    "restored " + str(n_body) + " of " + str(len(math_spans)) + " math spans in body"
)
assert MARK_OPEN not in body_html, "leftover placeholder marker in body"
assert MARK_OPEN not in toc_html, "leftover placeholder marker in toc"

TEMPLATE = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>README &mdash; Calculus &amp; Trig Reference</title>
<style>
  :root{
    --bg:#14181F; --panel:#1B2029; --line:#2A3140; --text:#E7E9EE; --muted:#9AA3B2;
    --accent:#F2A53C;
    --mono:"IBM Plex Mono","SFMono-Regular",Consolas,monospace;
    --serif:Georgia,"Times New Roman",serif;
    --fs-base: 19px;
  }
  *{box-sizing:border-box}
  html{-webkit-text-size-adjust:100%; text-size-adjust:100%}
  body{
    margin:0; background:var(--bg); color:var(--text);
    font-family:var(--serif); font-size:var(--fs-base); line-height:1.6;
    padding:20px calc(20px + env(safe-area-inset-right)) 70px calc(20px + env(safe-area-inset-left));
  }
  .wrap{max-width:80ch; margin:0 auto}
  h1,h2,h3{font-family:var(--mono); font-weight:650; letter-spacing:-.01em; color:var(--text)}
  h1{font-size:1.7em; line-height:1.25; margin:.4em 0 .5em; border-bottom:2px solid var(--accent); padding-bottom:.3em}
  h2{font-size:1.35em; margin:1.5em 0 .55em; padding-top:.4em; border-top:1px solid var(--line); color:var(--accent)}
  h3{font-size:1.12em; margin:1.2em 0 .45em}
  p,li{margin:.6em 0}
  strong{color:#fff}
  em{color:var(--muted)}
  code{
    font-family:var(--mono); background:#0F1319; border:1px solid var(--line); border-radius:5px;
    padding:.05em .35em; font-size:.88em; color:#F2C879; word-break:break-word;
  }
  pre{background:#0F1319; border:1px solid var(--line); border-radius:8px; padding:.8em 1.1em; overflow-x:auto}
  pre code{border:none; padding:0; background:none}
  hr{border:none; border-top:1px solid var(--line); margin:1.6em 0}
  a{color:var(--accent); text-decoration:none}
  a:hover{text-decoration:underline}
  .table-scroll{overflow-x:auto; -webkit-overflow-scrolling:touch; margin:.9em 0; border:1px solid var(--line); border-radius:8px}
  table{border-collapse:collapse; width:100%; font-size:.9em}
  th,td{border-bottom:1px solid var(--line); padding:.55em .8em; text-align:left}
  th{font-family:var(--mono); color:var(--accent); background:var(--panel); text-transform:uppercase; font-size:.82em; letter-spacing:.03em; white-space:nowrap}
  tr:last-child td{border-bottom:none}
  mjx-container{overflow-x:auto; overflow-y:hidden; max-width:100%}

  /* quick-jump nav, collapsible */
  #jump{position:sticky; top:0; z-index:5; background:var(--bg); border-bottom:1px solid var(--line); padding:.6em 0 .7em; margin-bottom:.7em}
  #jump summary{
    font-family:var(--mono); font-size:.72em; letter-spacing:.1em; text-transform:uppercase; color:var(--accent);
    cursor:pointer; list-style:none; padding:.4em .1em;
  }
  #jump summary::-webkit-details-marker{display:none}
  #jump summary::before{content:"\25B8 "}
  #jump[open] summary::before{content:"\25BE "}
  #jump .toc{font-size:.62em; max-height:50vh; overflow-y:auto; padding:.4em .2em .1em; line-height:1.8}
  #jump .toc ul{list-style:none; margin:0; padding-left:1.1em}
  #jump .toc > ul{padding-left:0}
  #jump .toc a{color:var(--text)}
  #jump .toc a:hover{color:var(--accent)}

  @media (max-width:640px){ :root{--fs-base:17px} .wrap{max-width:100%} }
</style>
<script>
  window.MathJax = {
    tex: {
      inlineMath: [['$', '$'], ['\\(', '\\)']],
      displayMath: [['$$', '$$'], ['\\[', '\\]']]
    },
    svg: {
      fontCache: 'global'
    },
    options: { skipHtmlTags: ['script','noscript','style','textarea','pre','code'] }
  };
</script>
<script defer src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.2/es5/tex-svg.js"></script>
</head>
<body>
<div class="wrap">
<details id="jump">
  <summary>Jump to a section</summary>
  <div class="toc">__TOC__</div>
</details>
__BODY__
</div>
</body>
</html>
"""

# wrap every markdown table in a horizontally-scrollable container
body_html = re.sub(r"<table>", '<div class="table-scroll"><table>', body_html)
body_html = re.sub(r"</table>", "</table></div>", body_html)

out = TEMPLATE.replace("__TOC__", toc_html).replace("__BODY__", body_html)

assert MARK_OPEN not in out, "leftover placeholder marker in final output"

with open(OUT, "w", encoding="utf-8") as f:
    f.write(out)

print("Wrote " + OUT + ": " + str(len(out)) + " chars, " + str(len(math_spans)) +
      " math spans (" + str(n_body) + " in body, " + str(n_toc) + " in toc), 0 leftover placeholders.")
