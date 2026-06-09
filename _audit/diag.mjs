import { chromium } from 'playwright';
import { mkdirSync } from 'fs';
const OUT = '_audit/diag';
mkdirSync(OUT, { recursive: true });
const B = 'http://localhost:8895';
const browser = await chromium.launch();

async function shotSection(page, url, selector, name, wait = 900) {
  await page.goto(url, { waitUntil: 'networkidle' });
  await page.waitForTimeout(wait);
  const el = await page.$(selector);
  if (el) { await el.screenshot({ path: `${OUT}/${name}.png` }); console.log('ok', name); }
  else console.log('MISSING selector', selector, 'for', name);
}

// Desktop 1440
const d = await browser.newContext({ viewport: { width: 1440, height: 900 } });
const dp = await d.newPage();
await shotSection(dp, `${B}/index.html`, '#services', 'idx-services');
await shotSection(dp, `${B}/index.html`, '#as-a-service', 'idx-asaservice');
await shotSection(dp, `${B}/index.html`, '#references', 'idx-references');
await shotSection(dp, `${B}/index.html`, '#book', 'idx-book');
await shotSection(dp, `${B}/impact.html`, 'body', 'impact-top', 1200).catch(()=>{});
// impact full page
await dp.goto(`${B}/impact.html`, { waitUntil: 'networkidle' }); await dp.waitForTimeout(1200);
await dp.screenshot({ path: `${OUT}/impact-full.png`, fullPage: true });
// resources full
await dp.goto(`${B}/resources.html`, { waitUntil: 'networkidle' }); await dp.waitForTimeout(1200);
await dp.screenshot({ path: `${OUT}/resources-full.png`, fullPage: true });

// Mobile 390
const m = await browser.newContext({ viewport: { width: 390, height: 844 } });
const mp = await m.newPage();
await shotSection(mp, `${B}/index.html`, '#references', 'm-idx-references');
await shotSection(mp, `${B}/index.html`, '#book', 'm-idx-book');
await mp.goto(`${B}/impact.html`, { waitUntil: 'networkidle' }); await mp.waitForTimeout(1200);
await mp.screenshot({ path: `${OUT}/m-impact-full.png`, fullPage: true });
await mp.goto(`${B}/resources.html`, { waitUntil: 'networkidle' }); await mp.waitForTimeout(1200);
await mp.screenshot({ path: `${OUT}/m-resources-full.png`, fullPage: true });

await browser.close();
console.log('done');
