"""add-outline.py - give the PDF a bookmark tree matching its contents page.

Titles are taken from the HTML table of contents, so headings whose text is
pure TeX get a readable unicode approximation rather than an empty bookmark.

    python add-outline.py print.html out.pdf toc-pages.json
"""
import json
import re
import sys

import fitz
from bs4 import BeautifulSoup

html_path, pdf_path, map_path = sys.argv[1], sys.argv[2], sys.argv[3]

SYMBOLS = [
    (r"\\displaystyle", ""), (r"\\left", ""), (r"\\right", ""),
    (r"\\dfrac\s*\{([^{}]*)\}\s*\{([^{}]*)\}", r"(\1)/(\2)"),
    (r"\\frac\s*\{([^{}]*)\}\s*\{([^{}]*)\}", r"(\1)/(\2)"),
    (r"\\sqrt\s*\{([^{}]*)\}", r"sqrt(\1)"),
    (r"\\lim_\{([^{}]*)\}", r"lim[\1]"),
    (r"\\int_\{([^{}]*)\}\^\{([^{}]*)\}", r"int[\1..\2]"),
    (r"\\to", "->"), (r"\\infty", "inf"), (r"\\cdot", "*"), (r"\\pm", "+/-"),
    (r"\\ne", "!="), (r"\\approx", "~="), (r"\\cdots", "..."), (r"\\ldots", "..."),
    (r"\\alpha", "a"), (r"\\beta", "b"), (r"\\theta", "theta"), (r"\\pi", "pi"),
    (r"\\,", " "), (r"\\;", " "), (r"\\!", ""),
    (r"\\(sin|cos|tan|cot|sec|csc|ln|log|exp|lim|int|sum)\b", r"\1"),
    (r"\\[a-zA-Z]+", ""),          # any remaining control sequence
    (r"[{}$]", ""),
]


def label(a) -> str:
    clone = BeautifulSoup(str(a), "html.parser")
    for s in clone.select("span.toc-pg"):
        s.decompose()
    t = clone.get_text(" ", strip=True)
    for pat, rep in SYMBOLS:
        t = re.sub(pat, rep, t)
    t = re.sub(r"\s+", " ", t).strip()
    return t or "(untitled)"


soup = BeautifulSoup(open(html_path, encoding="utf-8").read(), "html.parser")
nav = soup.find("nav", id="toc")
pages = json.load(open(map_path, encoding="utf-8"))

outline = []
for card in nav.select("section.toc-card"):
    title_a = card.select_one("a.toc-card-title")
    if not title_a:
        continue
    anchor = title_a["href"][1:]
    if anchor in pages:
        outline.append([1, label(title_a), pages[anchor]])
    for li in card.select("ul > li"):
        a = li.find("a", href=True, recursive=False)
        if a is None:
            continue
        depth = 2 + len(li.find_parents("ul")) - 1   # nested lists go one deeper
        anchor = a["href"][1:]
        if anchor in pages:
            outline.append([min(depth, 4), label(a), pages[anchor]])

doc = fitz.open(pdf_path)
# A child may not jump more than one level below its parent.
fixed, prev = [], 0
for lvl, title, pg in outline:
    lvl = min(lvl, prev + 1)
    fixed.append([lvl, title, pg])
    prev = lvl
doc.set_toc(fixed)
doc.saveIncr()

print(f"bookmarks written    {len(fixed)}")
for lvl, title, pg in fixed[:10]:
    print(f"  {'  ' * (lvl - 1)}{title[:64]}  ...  {pg}")
print("  ...")
