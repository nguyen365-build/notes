"""map-toc-pages.py - work out which PDF page each table-of-contents entry
lands on, and write {anchor-id: page} as JSON.

Chrome's printToPDF emits no internal link annotations, so the destinations
cannot simply be read back - each heading has to be located by its text.

Two wrinkles the naive version gets wrong:

  * 29 of the 324 headings are pure MathJax, which prints as SVG paths and
    carries no extractable text at all. For those the search key is taken
    from the first text-bearing block that FOLLOWS the heading - safe because
    the stylesheet sets `break-after: avoid` on headings, so a heading is
    always on the page of the content beneath it.

  * Heading text repeats across the document ("Steps.", "Answer."). Matching
    is therefore monotonic: an entry is only ever searched from the page the
    previous entry resolved to, which is valid because TOC order is document
    order.

    python map-toc-pages.py print.html out.pdf toc-pages.json
"""
import json
import re
import sys
import unicodedata

import fitz
from bs4 import BeautifulSoup

html_path, pdf_path, out_path = sys.argv[1], sys.argv[2], sys.argv[3]

MIN_KEY = 10        # chars: shorter keys match far too much
MAX_KEY = 60


def plain(node) -> str:
    """Visible text of a node with MathJax and TeX source removed."""
    if node is None:
        return ""
    clone = BeautifulSoup(str(node), "html.parser")
    for m in clone.select("mjx-container, script, style"):
        m.decompose()
    t = clone.get_text(" ", strip=True)
    t = re.sub(r"\$[^$]*\$", " ", t)          # TeX that MathJax will swallow
    t = re.sub(r"\\\(.*?\\\)", " ", t)
    t = t.replace("\\", " ")
    t = unicodedata.normalize("NFKC", t)
    return re.sub(r"\s+", " ", t).strip()


soup = BeautifulSoup(open(html_path, encoding="utf-8").read(), "html.parser")
nav = soup.find("nav", id="toc")
body_ids = {el.get("id"): el for el in soup.select("[id]")}

entries = []            # (anchor id, search key)
for a in nav.select('a[href^="#"]'):
    anchor = a["href"][1:]
    target = body_ids.get(anchor)
    if target is None or target is nav:
        continue

    key = plain(target)
    # No usable text in the heading itself: borrow the block below it.
    node = target
    while len(key) < MIN_KEY:
        node = node.find_next_sibling()
        if node is None:
            break
        nxt = plain(node)
        if len(nxt) >= MIN_KEY:
            key = nxt
            break
    entries.append((anchor, key[:MAX_KEY]))

doc = fitz.open(pdf_path)

# The first content page: everything before it is the TOC, and searching
# there would match the entry's own text in the contents list.
first_content = 0
for p in range(doc.page_count):
    if not doc[p].search_for("Jump to a section") and doc[p].get_text().strip():
        # a page is content once we are past the nav block
        pass
nav_pages = set()
for p in range(doc.page_count):
    txt = doc[p].get_text()
    if "Table of contents" in txt or "STEP 0" in txt or "Step 0" in txt:
        nav_pages.add(p)
first_content = (max(nav_pages) + 1) if nav_pages else 0

mapping, unresolved, key_used = {}, [], {}
cursor = first_content
for anchor, key in entries:
    if len(key) < MIN_KEY:
        unresolved.append((anchor, key, "no usable search key"))
        continue
    found = None
    for p in range(cursor, doc.page_count):
        if doc[p].search_for(key, quads=False):
            found = p
            break
    if found is None:
        # Fall back to a shorter prefix before giving up.
        short = key[:24]
        for p in range(cursor, doc.page_count):
            if len(short) >= MIN_KEY and doc[p].search_for(short):
                found = p
                break
    if found is None:
        unresolved.append((anchor, key, "not found in pdf"))
        continue
    mapping[anchor] = found + 1
    key_used[anchor] = key
    cursor = found

json.dump(mapping, open(out_path, "w", encoding="utf-8"), indent=1)

print(f"toc entries          {len(entries)}")
print(f"resolved             {len(mapping)}")
print(f"unresolved           {len(unresolved)}")
for a, k, why in unresolved[:15]:
    print(f"   {a}  ({why})  key={k!r}")
print(f"first content page   {first_content + 1}")
print(f"page range           {min(mapping.values(), default=0)}..{max(mapping.values(), default=0)}")
print(f"wrote                {out_path}")
