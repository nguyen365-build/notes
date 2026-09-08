/* build-print.mjs - generate print.html from index.html.
 *
 * index.html is left untouched. print.html is the same document with the
 * print overrides and the fit/audit script appended, so the two can never
 * drift: re-run this after any edit to index.html.
 *
 *   node tools/print/build-print.mjs [src.html] [out.html]
 */
import { readFileSync, writeFileSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
const root = resolve(here, '..', '..');

const src = resolve(root, process.argv[2] ?? 'index.html');
const out = resolve(root, process.argv[3] ?? 'print.html');

const html = readFileSync(src, 'utf8');
const css = readFileSync(resolve(here, 'print-overrides.css'), 'utf8');
const js = readFileSync(resolve(here, 'print-fit.js'), 'utf8');

if (!html.includes('</head>')) throw new Error(`no </head> in ${src}`);
if (!html.includes('</body>')) throw new Error(`no </body> in ${src}`);

/* An unclosed inline formatting tag does not break the page - the parser
 * happily reconstructs it around every following block, which is how two
 * missing </strong> silently set 100 pages of body text in bold. Nothing
 * complains, so the balance has to be asserted. */
for (const tag of ['strong', 'em', 'code', 'a', 'th', 'td', 'tr', 'table']) {
  const open = (html.match(new RegExp(`<${tag}[\\s>]`, 'g')) ?? []).length;
  const close = (html.match(new RegExp(`</${tag}>`, 'g')) ?? []).length;
  if (open !== close) {
    const lines = html.split('\n');
    const bad = [];
    for (let i = 0; i < lines.length; i++) {
      const o = (lines[i].match(new RegExp(`<${tag}[\\s>]`, 'g')) ?? []).length;
      const c = (lines[i].match(new RegExp(`</${tag}>`, 'g')) ?? []).length;
      if (o !== c) bad.push(`  line ${i + 1}: ${lines[i].trim().slice(0, 120)}`);
    }
    throw new Error(
      `unbalanced <${tag}> in ${src}: ${open} open vs ${close} close\n${bad.slice(0, 10).join('\n')}`
    );
  }
}

/* The print stylesheet hides the "Back to contents" links, so the intro's
 * promise about them stops being true on paper. Fix the sentence rather
 * than ship a document that contradicts itself. */
const SCREEN_ONLY_LEDE = 'Read it top to bottom, or jump straight to what you need - every section ends with a link back here.';
const PRINT_LEDE = 'Read it top to bottom, or jump straight to what you need.';
if (!html.includes(SCREEN_ONLY_LEDE)) {
  throw new Error('table-of-contents lede text changed; update SCREEN_ONLY_LEDE in build-print.mjs');
}

/* Table-of-contents page numbers.
 *
 * Pass 1 injects placeholders, the PDF is rendered and read back for the
 * real numbers, pass 2 injects those. The placeholder and the number sit in
 * a fixed-width box (see .toc-pg), so the two passes paginate identically -
 * otherwise the act of writing the numbers could move the pages they name.
 */
const pageMapPath = process.env.TOC_PAGE_MAP;
const pageMap = pageMapPath ? JSON.parse(readFileSync(pageMapPath, 'utf8')) : {};
const PLACEHOLDER = '&#183;';

const tocOpen = html.indexOf('<nav id="toc"');
const tocClose = html.indexOf('</nav>', tocOpen);
if (tocOpen < 0 || tocClose < 0) throw new Error('could not locate <nav id="toc"> block');

let injected = 0;
const tocBlock = html
  .slice(tocOpen, tocClose)
  .replace(/<a([^>]*href="#([^"#]+)"[^>]*)>/g, (m, attrs, id) => {
    injected++;
    const n = pageMap[id];
    return `<a${attrs}><span class="toc-pg" data-for="${id}">${n ?? PLACEHOLDER}</span>`;
  });
const withToc = html.slice(0, tocOpen) + tocBlock + html.slice(tocClose);

if (injected === 0) throw new Error('no table-of-contents links found to number');
if (pageMapPath) {
  const missing = Object.keys(pageMap).length;
  console.log(`  toc: ${injected} links, ${missing} resolved page numbers`);
}

// Function replacers, not string ones: the injected CSS/JS contains `$'`
// and `$&`, which a string replacement would expand as capture patterns.
const printed = withToc
  .replace(SCREEN_ONLY_LEDE, () => PRINT_LEDE)
  .replace('</head>', () => `<style id="print-overrides">\n${css}\n</style>\n</head>`)
  .replace('</body>', () => `<script id="print-fit">\n${js}\n</script>\n</body>`);

// The injected sources must survive byte-for-byte, or the page silently
// loads a mangled script (which is exactly what a string replacer did).
if (!printed.includes(css)) throw new Error('CSS was mangled during injection');
if (!printed.includes(js)) throw new Error('JS was mangled during injection');

writeFileSync(out, printed, 'utf8');

console.log(`built  ${out}`);
console.log(`  from ${src} (${html.length} chars) + ${css.length} css + ${js.length} js`);
