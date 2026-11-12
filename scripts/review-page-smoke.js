#!/usr/bin/env node
// review-page-smoke.js — run a jail-prototype review page in a real browser, two ways:
//   1. opened directly (file://), at desktop and 360px phone width
//   2. inside a sandboxed srcdoc iframe (allow-scripts, no same-origin), like the Claude app preview
// In each: click every variant switch, answer one question, press Copy my answers.
// Fails (exit 1) on any page error or console error, a switch that doesn't show its variant,
// an empty copied-answers block, or horizontal overflow at phone width.
// Needs Node + Playwright; exits 3 ("skipped") when Playwright isn't installed.
// Repo tooling (infrastructure), not skill content.
// Usage: node scripts/review-page-smoke.js page.html [page2.html ...]
let chromium;
try { ({ chromium } = require('playwright')); } catch (e) { console.log('review-page-smoke: SKIPPED (playwright not installed)'); process.exit(3); }
const fs = require('fs'); const path = require('path');

async function exercise(frame, label, problems) {
  const switches = await frame.$$('[data-show]');
  for (const s of switches) {
    const want = await s.getAttribute('data-show');
    await s.click();
    const shown = await frame.$$eval('[data-variant]', els => els.filter(x => getComputedStyle(x).display !== 'none').map(x => x.dataset.variant));
    if (shown.length !== 1 || shown[0] !== want) problems.push(`${label}: switch ${want} shows ${JSON.stringify(shown)}`);
  }
  const radio = await frame.$('[data-question] input[type=radio]');
  if (radio) await radio.check();
  const copy = await frame.$('[data-copy-feedback]');
  if (copy) {
    await copy.click();
    await frame.waitForTimeout(150);
    const text = await frame.evaluate(() => { const o = document.querySelector('#out, [data-feedback-output]'); return o ? o.textContent.trim() : ''; });
    if (!text) problems.push(`${label}: Copy my answers produced no visible text`);
  }
}

(async () => {
  const files = process.argv.slice(2);
  if (!files.length) { console.error('usage: review-page-smoke.js page.html ...'); process.exit(2); }
  const browser = await chromium.launch(); let failed = false;
  for (const f of files) {
    const problems = []; const html = fs.readFileSync(f, 'utf8');
    const watch = (page, label) => {
      page.on('pageerror', e => problems.push(`${label}: page error: ${e.message.slice(0, 160)}`));
      page.on('console', m => { if (m.type() === 'error') problems.push(`${label}: console error: ${m.text().slice(0, 160)}`); });
    };
    for (const [name, vp] of [['direct-desktop', { width: 1200, height: 900 }], ['direct-phone', { width: 360, height: 780 }]]) {
      const p = await browser.newPage({ viewport: vp }); watch(p, name);
      await p.goto('file://' + path.resolve(f));
      await exercise(p, name, problems);
      if (name.endsWith('phone') && await p.evaluate(() => document.documentElement.scrollWidth > window.innerWidth + 1))
        problems.push(`${name}: horizontal overflow at 360px`);
      await p.close();
    }
    const p = await browser.newPage({ viewport: { width: 900, height: 900 } }); watch(p, 'sandboxed-iframe');
    await p.setContent('<iframe id="f" sandbox="allow-scripts allow-forms allow-popups" style="width:880px;height:880px;border:0"></iframe>');
    await p.$eval('#f', (el, h) => { el.srcdoc = h; }, html);
    await p.waitForTimeout(600);
    const frame = p.frames().find(fr => fr !== p.mainFrame());
    await exercise(frame, 'sandboxed-iframe', problems);
    await p.close();
    if (problems.length) { failed = true; console.error(`review-page-smoke: ${f}: FAIL`); problems.forEach(x => console.error('  ' + x)); }
    else console.log(`review-page-smoke: ${f}: PASS (direct desktop + phone, sandboxed iframe)`);
  }
  await browser.close(); process.exit(failed ? 1 : 0);
})().catch(e => { console.error('review-page-smoke: error: ' + e.message); process.exit(2); });
