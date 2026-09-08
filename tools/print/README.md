# Printable PDF build

Turns `index.html` (dark ops-console theme, MathJax, 194 tables) into
`MATH265-Calculus-Reference.pdf` - plain black text on white, US Letter,
with a numbered table of contents and PDF bookmarks.

`index.html` is never modified by the build.
Everything print-specific is injected into a generated `print.html`.

## Build

```
node tools/print/make-pdf.mjs
```

Needs Chrome (path overridable with `CHROME=`), Node 22+ for the built-in
`WebSocket`, and Python with `PyMuPDF` and `beautifulsoup4`.

## Why it is two passes

Chrome's `--print-to-pdf` fires on a timer and cannot wait for MathJax, so
the renderer drives Chrome over CDP instead and waits for the page's own
`window.__printReady`, which is set only after MathJax's startup promise
settles and the fit pass has run.

Page numbers in the contents cannot be produced in one pass: nothing knows
which page a section lands on until the document has been paginated, and
`printToPDF` emits no internal link annotations to read back. So:

1. build with fixed-width **placeholders** in the contents, render;
2. locate every section in that PDF (`map-toc-pages.py`);
3. rebuild with the **real numbers**, render.

Because the placeholder and the number occupy the same fixed-width box, the
two passes paginate identically. `make-pdf.mjs` proves this rather than
assuming it: it re-derives the map from the finished PDF and fails the build
if a single number moved.

## Files

| file | role |
| --- | --- |
| `make-pdf.mjs` | orchestrates both passes, verification, bookmarks, audit |
| `build-print.mjs` | `index.html` -> `print.html`; injects CSS/JS + TOC numbers |
| `print-overrides.css` | the black-on-white print stylesheet |
| `print-fit.js` | runs in the page: shrinks overflow, audits colour, reports |
| `render-pdf.mjs` | headless Chrome over CDP -> PDF |
| `map-toc-pages.py` | finds which page each section landed on |
| `add-outline.py` | writes the PDF bookmark tree |
| `audit-pdf.py` | checks the finished PDF and rasterises sample pages |

## Guards

These exist because each one caught a real defect during the first build:

- **Unbalanced inline tags** (`build-print.mjs`). Two missing `</strong>` in
  `index.html` silently set ~100 pages of body text in bold - the parser
  reconstructs the tag around every following block and nothing errors.
  The build now refuses to run on an unbalanced document.
- **Byte-exact injection** (`build-print.mjs`). `String.replace` with a
  string replacement expands `$'` and `$&`; the injected script contains
  both, and got mangled into a syntax error. Function replacers plus an
  `includes()` check.
- **Computed-style colour audit** (`print-fit.js`). Reads back every
  element's computed `background-color` and `color` from the rendered tree,
  so "no backgrounds, black text" is measured rather than hoped for.
- **Overflow locator** (`print-fit.js`). On paper there is no sideways
  scroll, so anything wider than the column is silently clipped. Every box
  past the right edge is named, and math/tables that overflow are scaled to
  fit. The viewport is set to exactly the printable column width, or the
  measurement would describe a layout Chrome never paginates.
- **PDF-level audit** (`audit-pdf.py`). Asserts on the artifact: page count,
  paper size, text colour, font mix, and a pixel sample for stray colour.

## Checking a change

```
python tools/print/audit-pdf.py MATH265-Calculus-Reference.pdf 1,40,80
```

writes `_pdf_preview/pageNNNN.png` so pages can actually be looked at.
