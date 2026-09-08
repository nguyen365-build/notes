/* render-pdf.mjs - drive headless Chrome over CDP to turn print.html into a PDF.
 *
 * Why not `chrome --headless --print-to-pdf`: that fires on a timer and
 * cannot wait for MathJax, so formulas come out half-typeset. Here the page
 * signals window.__printReady only after MathJax's startup promise settles
 * and the fit/audit pass has run, and the report it leaves behind is printed
 * so the run can be judged on evidence rather than on the file existing.
 *
 *   node tools/print/render-pdf.mjs print.html out.pdf
 */
import { spawn } from 'node:child_process';
import { mkdtempSync, writeFileSync, existsSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join, resolve, dirname } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
const root = resolve(here, '..', '..');

const srcPath = resolve(root, process.argv[2] ?? 'print.html');
const outPath = resolve(root, process.argv[3] ?? 'MATH265-Calculus-Reference.pdf');

if (!existsSync(srcPath)) throw new Error(`missing ${srcPath}`);

/* ---- page geometry -------------------------------------------------------
 * The viewport width MUST equal the printable column width, or the fit pass
 * measures a layout that is not the one Chrome paginates.
 */
const PAPER_W = 8.5;            // in, US Letter
const PAPER_H = 11;
const MARGIN_X = 0.55;
const MARGIN_TOP = 0.5;
const MARGIN_BOTTOM = 0.62;     // room for the page-number footer
const CONTENT_PX = Math.floor((PAPER_W - 2 * MARGIN_X) * 96);

const CHROME = process.env.CHROME
  ?? 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const PORT = Number(process.env.CDP_PORT ?? 9333);
const READY_TIMEOUT_MS = 300_000;

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

const profile = mkdtempSync(join(tmpdir(), 'print-pdf-chrome-'));
const chrome = spawn(CHROME, [
  '--headless=new',
  `--remote-debugging-port=${PORT}`,
  `--user-data-dir=${profile}`,
  '--no-first-run',
  '--no-default-browser-check',
  '--disable-extensions',
  '--disable-gpu',
  '--hide-scrollbars',
  '--force-device-scale-factor=1',
  '--allow-file-access-from-files',
  '--run-all-compositor-stages-before-draw',
  'about:blank',
], { stdio: ['ignore', 'pipe', 'pipe'] });

let chromeStderr = '';
chrome.stderr.on('data', (d) => { chromeStderr += d.toString(); });

async function waitForCdp() {
  for (let i = 0; i < 100; i++) {
    try {
      const r = await fetch(`http://127.0.0.1:${PORT}/json/version`);
      if (r.ok) return await r.json();
    } catch { /* not up yet */ }
    await sleep(200);
  }
  throw new Error(`Chrome CDP never came up on ${PORT}\n${chromeStderr}`);
}

/* Minimal CDP client over the built-in WebSocket. */
function connect(wsUrl) {
  const ws = new WebSocket(wsUrl);
  const pending = new Map();
  let id = 0;
  const ready = new Promise((res, rej) => {
    ws.addEventListener('open', () => res());
    ws.addEventListener('error', (e) => rej(new Error('ws error: ' + e.message)));
  });
  ws.addEventListener('message', (ev) => {
    const msg = JSON.parse(ev.data);
    if (msg.id && pending.has(msg.id)) {
      const { res, rej } = pending.get(msg.id);
      pending.delete(msg.id);
      if (msg.error) rej(new Error(`${msg.error.message} (${JSON.stringify(msg.error.data ?? '')})`));
      else res(msg.result);
    }
  });
  const send = (method, params = {}) => {
    const mid = ++id;
    return new Promise((res, rej) => {
      pending.set(mid, { res, rej });
      ws.send(JSON.stringify({ id: mid, method, params }));
    });
  };
  return { ready, send, close: () => ws.close() };
}

async function main() {
  await waitForCdp();

  // /json/new gives a page target with its own debugger socket.
  const created = await fetch(`http://127.0.0.1:${PORT}/json/new?about:blank`, { method: 'PUT' });
  if (!created.ok) throw new Error(`/json/new failed: ${created.status}`);
  const target = await created.json();

  const cdp = connect(target.webSocketDebuggerUrl);
  await cdp.ready;

  await cdp.send('Page.enable');
  await cdp.send('Runtime.enable');
  await cdp.send('Emulation.setDeviceMetricsOverride', {
    width: CONTENT_PX,
    height: 1200,
    deviceScaleFactor: 1,
    mobile: false,
  });

  const url = pathToFileURL(srcPath).href;
  process.stdout.write(`navigating to ${url}\n  viewport ${CONTENT_PX}px = printable column\n`);
  await cdp.send('Page.navigate', { url });

  // Poll for the page's own ready flag rather than guessing a duration.
  const deadline = Date.now() + READY_TIMEOUT_MS;
  let report = null;
  while (Date.now() < deadline) {
    const r = await cdp.send('Runtime.evaluate', {
      expression: 'window.__printReady === true ? JSON.stringify({report: window.__printReport, error: window.__printError}) : ""',
      returnByValue: true,
    });
    const v = r.result?.value;
    if (v) { const p = JSON.parse(v); if (p.error) throw new Error('page error: ' + p.error); report = p.report; break; }
    await sleep(500);
  }
  if (!report) throw new Error(`page never reached __printReady within ${READY_TIMEOUT_MS}ms`);

  const printed = await cdp.send('Page.printToPDF', {
    paperWidth: PAPER_W,
    paperHeight: PAPER_H,
    marginTop: MARGIN_TOP,
    marginBottom: MARGIN_BOTTOM,
    marginLeft: MARGIN_X,
    marginRight: MARGIN_X,
    printBackground: false,
    preferCSSPageSize: false,
    displayHeaderFooter: true,
    headerTemplate: '<div></div>',
    footerTemplate:
      '<div style="width:100%;font-family:Georgia,serif;font-size:8pt;color:#000;'
      + 'padding:0 .55in;display:flex;justify-content:space-between;">'
      + '<span>Calculus &amp; Trig Reference</span>'
      + '<span class="pageNumber"></span></div>',
    transferMode: 'ReturnAsStream',
  });

  // Stream the PDF out - a 200-page doc as one base64 blob risks the ws frame cap.
  const chunks = [];
  for (;;) {
    const { data, base64Encoded, eof } = await cdp.send('IO.read', { handle: printed.stream, size: 1 << 20 });
    if (data) chunks.push(Buffer.from(data, base64Encoded ? 'base64' : 'utf8'));
    if (eof) break;
  }
  await cdp.send('IO.close', { handle: printed.stream });
  writeFileSync(outPath, Buffer.concat(chunks));

  cdp.close();
  console.log('\n' + JSON.stringify({ pdf: outPath, bytes: Buffer.concat(chunks).length, report }, null, 2));
}

main()
  .catch((e) => { console.error('FAILED:', e.message); process.exitCode = 1; })
  .finally(async () => {
    try { await fetch(`http://127.0.0.1:${PORT}/json/close/`); } catch {}
    chrome.kill();
    await sleep(500);
    try { rmSync(profile, { recursive: true, force: true }); } catch {}
  });
