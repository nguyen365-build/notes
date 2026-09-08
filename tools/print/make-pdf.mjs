/* make-pdf.mjs - the whole printable-PDF pipeline, one command.
 *
 *   node tools/print/make-pdf.mjs
 *
 *   pass 1  build print.html with fixed-width TOC placeholders -> render
 *   map     read the PDF back to learn which page each section landed on
 *   pass 2  rebuild with the real numbers -> render
 *   verify  re-derive the map from the finished PDF; it must be identical,
 *           which is what proves the printed numbers are the true pages
 *   outline add the PDF bookmark tree
 *   audit   assert on the artifact itself, not on this script finishing
 */
import { spawnSync } from 'node:child_process';
import { existsSync, readFileSync, unlinkSync } from 'node:fs';
import { resolve, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
const root = resolve(here, '..', '..');
const OUT = process.argv[2] ?? 'MATH265-Calculus-Reference.pdf';

const run = (cmd, args, label) => {
  process.stdout.write(`\n=== ${label} ===\n`);
  const r = spawnSync(cmd, args, { cwd: root, stdio: 'inherit', shell: false });
  if (r.status !== 0) { console.error(`\nstep failed: ${label}`); process.exit(1); }
};
const node = (args, label, env) => {
  process.stdout.write(`\n=== ${label} ===\n`);
  const r = spawnSync(process.execPath, args, { cwd: root, stdio: 'inherit', env: { ...process.env, ...env } });
  if (r.status !== 0) { console.error(`\nstep failed: ${label}`); process.exit(1); }
};
const py = (args, label) => run('python', args, label);

node(['tools/print/build-print.mjs'], 'pass 1: build (TOC placeholders)');
node(['tools/print/render-pdf.mjs', 'print.html', '_pass1.pdf'], 'pass 1: render');
py(['tools/print/map-toc-pages.py', 'print.html', '_pass1.pdf', 'toc-pages.json'], 'map sections to pages');

node(['tools/print/build-print.mjs'], 'pass 2: build (real page numbers)', { TOC_PAGE_MAP: 'toc-pages.json' });
node(['tools/print/render-pdf.mjs', 'print.html', OUT], 'pass 2: render');

py(['tools/print/map-toc-pages.py', 'print.html', OUT, '_verify.json'], 'verify: re-derive page map');
const a = JSON.parse(readFileSync(resolve(root, 'toc-pages.json'), 'utf8'));
const b = JSON.parse(readFileSync(resolve(root, '_verify.json'), 'utf8'));
const drift = Object.keys({ ...a, ...b }).filter((k) => a[k] !== b[k]);
if (drift.length) {
  console.error(`\nTOC numbers did not converge - ${drift.length} entries moved: ${drift.slice(0, 8)}`);
  process.exit(1);
}
console.log(`converged: all ${Object.keys(a).length} table-of-contents page numbers verified against the finished PDF`);

py(['tools/print/add-outline.py', 'print.html', OUT, 'toc-pages.json'], 'add PDF bookmarks');
py(['tools/print/audit-pdf.py', OUT], 'audit the finished PDF');

for (const tmp of ['_pass1.pdf', '_verify.json']) {
  const p = resolve(root, tmp);
  if (existsSync(p)) unlinkSync(p);
}
console.log(`\ndone: ${resolve(root, OUT)}`);
