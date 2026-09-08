"""audit-pdf.py - check the PDF itself, not the renderer's own account of it.

Reports page count / size, samples the rendered page pixels for any
non-white background, checks that text is dark, and rasterises requested
pages to PNG so they can actually be looked at.

    python tools/print/audit-pdf.py out.pdf [page,page,...]
"""
import sys, os, collections
import fitz

pdf = sys.argv[1]
pages_to_render = [int(p) for p in sys.argv[2].split(",")] if len(sys.argv) > 2 else []

doc = fitz.open(pdf)
print(f"file        {pdf}")
print(f"size        {os.path.getsize(pdf)/1e6:.2f} MB")
print(f"pages       {doc.page_count}")
r = doc[0].rect
print(f"page box    {r.width:.1f} x {r.height:.1f} pt  ({r.width/72:.2f} x {r.height/72:.2f} in)")

# --- colour audit -------------------------------------------------------
# Sample every Nth page at low DPI and count distinct colours. A correct
# black-on-white print has white, black, and antialiasing greys - nothing else.
step = max(1, doc.page_count // 24)
sampled = list(range(0, doc.page_count, step))
offwhite = collections.Counter()
saturated = collections.Counter()
for i in sampled:
    pix = doc[i].get_pixmap(dpi=40, colorspace=fitz.csRGB)
    data = pix.samples
    for off in range(0, len(data), 3):
        rr, gg, bb = data[off], data[off + 1], data[off + 2]
        mx, mn = max(rr, gg, bb), min(rr, gg, bb)
        if mx - mn > 24:                      # a real hue, not a grey
            saturated[(rr // 32, gg // 32, bb // 32)] += 1
        elif 40 < mn and mx < 235:            # mid grey: a fill, not text/paper
            offwhite[mn // 32] += 1
print(f"\nsampled pages           {len(sampled)} of {doc.page_count}")
print(f"saturated (colour) px   {sum(saturated.values())}  {dict(list(saturated.items())[:5])}")
print(f"mid-grey px             {sum(offwhite.values())} (antialiasing only if small)")

# --- text audit ---------------------------------------------------------
colors = collections.Counter()
fonts = collections.Counter()
sizes = collections.Counter()
empty_pages = []
for i in range(doc.page_count):
    d = doc[i].get_text("dict")
    n = 0
    for blk in d["blocks"]:
        for line in blk.get("lines", []):
            for sp in line["spans"]:
                if not sp["text"].strip():
                    continue
                n += 1
                colors[sp["color"]] += 1
                fonts[sp["font"]] += 1
                sizes[round(sp["size"], 1)] += 1
    if n == 0:
        empty_pages.append(i + 1)
print(f"\ntext colours            {[(hex(c), n) for c, n in colors.most_common(6)]}")
print(f"fonts                   {fonts.most_common(6)}")
print(f"font sizes (pt)         {sorted(sizes.items(), key=lambda kv: -kv[1])[:8]}")
print(f"pages with no text      {len(empty_pages)} {empty_pages[:12]}")

# --- render samples -----------------------------------------------------
outdir = os.path.join(os.path.dirname(pdf) or ".", "_pdf_preview")
os.makedirs(outdir, exist_ok=True)
for p in pages_to_render:
    idx = p - 1
    if 0 <= idx < doc.page_count:
        out = os.path.join(outdir, f"page{p:04d}.png")
        doc[idx].get_pixmap(dpi=120, colorspace=fitz.csRGB).save(out)
        print(f"rendered    {out}")
