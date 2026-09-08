/* ==========================================================================
   print-fit.js - runs inside print.html AFTER MathJax has typeset.

   The page is loaded at exactly the printable column width (see
   render-pdf.mjs), so a box that overflows here is a box that would be
   clipped on paper. Anything still too wide is scaled down just enough to
   fit, and the results are left on window.__printReport so the build can
   assert on them instead of trusting the render.
   ========================================================================== */
(function () {
  'use strict';

  var MIN_MATH_SCALE = 0.60;   // below this, math stops being exam-readable
  var MIN_TABLE_SCALE = 0.62;

  window.__printReady = false;
  window.__printError = null;

  function fitMath(avail, report) {
    var nodes = document.querySelectorAll('mjx-container');
    for (var i = 0; i < nodes.length; i++) {
      var el = nodes[i];
      // Measure the glyph box, not the container: a display container is a
      // full-width block whose SVG child is the thing that overflows.
      var svg = el.querySelector('svg');
      if (!svg) continue;
      var w = svg.getBoundingClientRect().width;
      if (w <= avail + 0.5) continue;

      var scale = avail / w;
      if (scale < MIN_MATH_SCALE) scale = MIN_MATH_SCALE;
      el.style.fontSize = (scale * 100).toFixed(2) + '%';

      // Re-measure: font-size scaling is what MathJax itself uses, so this
      // should now fit unless we hit the floor.
      var after = svg.getBoundingClientRect().width;
      report.mathScaled.push({
        scale: Number(scale.toFixed(3)),
        before: Math.round(w),
        after: Math.round(after),
        tex: (el.getAttribute('aria-label') || el.textContent || '').slice(0, 90)
      });
      if (after > avail + 1) {
        report.mathStillWide.push({
          over: Math.round(after - avail),
          tex: (el.getAttribute('aria-label') || el.textContent || '').slice(0, 120)
        });
      }
    }
  }

  function fitTables(avail, report) {
    var tables = document.querySelectorAll('table');
    for (var i = 0; i < tables.length; i++) {
      var t = tables[i];
      // scrollWidth is the width the table WANTS; clientWidth is what it got.
      var want = t.scrollWidth;
      if (want <= avail + 1) continue;

      var scale = avail / want;
      if (scale < MIN_TABLE_SCALE) scale = MIN_TABLE_SCALE;
      t.style.zoom = scale.toFixed(3);   // zoom, not transform: it reflows

      var after = t.scrollWidth * scale;
      report.tablesScaled.push({
        scale: Number(scale.toFixed(3)),
        before: Math.round(want),
        after: Math.round(after)
      });
      if (after > avail + 2) {
        report.tablesStillWide.push({ over: Math.round(after - avail) });
      }
    }
  }

  /* Independent audit: walk the rendered tree and report any computed
     background that is not fully transparent, and any text colour that is
     not black. This is the check for "no background colors, black text" -
     it reads the COMPUTED style, so it catches anything the overrides
     missed rather than assuming they worked. */
  function auditColors(report) {
    var all = document.querySelectorAll('body, body *');
    for (var i = 0; i < all.length; i++) {
      var el = all[i];
      var tag = el.tagName.toLowerCase();
      if (tag === 'script' || tag === 'style' || tag === 'defs') continue;
      var cs = getComputedStyle(el);

      var bg = cs.backgroundColor;
      if (bg && bg !== 'rgba(0, 0, 0, 0)' && bg !== 'transparent') {
        if (!(tag === 'html' || tag === 'body') || bg !== 'rgb(255, 255, 255)') {
          report.badBackgrounds.push(tag + ' :: ' + bg);
        }
      }
      if (cs.backgroundImage && cs.backgroundImage !== 'none') {
        report.badBackgrounds.push(tag + ' :: image ' + cs.backgroundImage.slice(0, 60));
      }
      if (cs.color && cs.color !== 'rgb(0, 0, 0)') {
        report.badColors.push(tag + ' :: ' + cs.color);
      }
    }
    report.badBackgrounds = report.badBackgrounds.slice(0, 25);
    report.badColors = report.badColors.slice(0, 25);
  }

  function run() {
    var report = {
      availPx: 0,
      mathTotal: document.querySelectorAll('mjx-container').length,
      mathScaled: [],
      mathStillWide: [],
      tablesTotal: document.querySelectorAll('table').length,
      tablesScaled: [],
      tablesStillWide: [],
      badBackgrounds: [],
      badColors: [],
      unrenderedTex: 0,
      bodyOverflowPx: 0,
      overflowing: [],
      overflowCount: 0
    };

    var wrap = document.querySelector('.wrap');
    var avail = wrap ? wrap.clientWidth : document.documentElement.clientWidth;
    report.availPx = Math.round(avail);

    fitMath(avail, report);
    fitTables(avail, report);

    // Any '$...$' left in the text means MathJax did not typeset it.
    var body = document.body.innerText || '';
    var leftovers = body.match(/\$[^$\n]{1,120}\$/g);
    report.unrenderedTex = leftovers ? leftovers.length : 0;
    report.unrenderedSample = leftovers ? leftovers.slice(0, 5) : [];

    report.bodyOverflowPx = Math.max(
      0,
      Math.round(document.documentElement.scrollWidth - document.documentElement.clientWidth)
    );

    // A page-level overflow number says nothing about WHERE the clip is, so
    // name every box whose right edge sits past the printable column.
    var limit = (wrap ? wrap.getBoundingClientRect().right : avail);
    var all = document.querySelectorAll('body *');
    for (var k = 0; k < all.length; k++) {
      var e = all[k];
      var r = e.getBoundingClientRect();
      if (r.width === 0 || r.height === 0) continue;
      if (r.right > limit + 1) {
        report.overflowing.push({
          tag: e.tagName.toLowerCase(),
          cls: (e.className && e.className.baseVal !== undefined ? e.className.baseVal : e.className) || '',
          over: Math.round(r.right - limit),
          text: (e.textContent || '').trim().slice(0, 70)
        });
      }
    }
    report.overflowCount = report.overflowing.length;
    report.overflowing = report.overflowing.slice(0, 12);

    auditColors(report);

    window.__printReport = report;
    window.__printReady = true;
  }

  function start() {
    var mjReady = (window.MathJax && window.MathJax.startup && window.MathJax.startup.promise)
      ? window.MathJax.startup.promise
      : Promise.resolve();

    mjReady
      .then(function () { return document.fonts ? document.fonts.ready : null; })
      // one frame so the post-typeset layout is settled before measuring
      .then(function () { return new Promise(function (r) { requestAnimationFrame(function () { requestAnimationFrame(r); }); }); })
      .then(run)
      .catch(function (e) {
        window.__printError = String((e && e.stack) || e);
        window.__printReady = true;
      });
  }

  if (document.readyState === 'complete') start();
  else window.addEventListener('load', start);
})();
