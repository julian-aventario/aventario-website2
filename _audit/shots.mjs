import { chromium } from 'playwright';
import { mkdirSync } from 'fs';

const OUT = '_audit/shots';
mkdirSync(OUT, { recursive: true });

const pages = [
  'index.html', 'about.html', 'blog.html', 'contact.html',
  'impact.html', 'resources.html', 'portfolio.html'
];

const browser = await chromium.launch();
const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1 });
const page = await ctx.newPage();

for (const p of pages) {
  const name = p.replace('.html', '');
  await page.goto(`http://localhost:8899/${p}`, { waitUntil: 'networkidle' });
  await page.waitForTimeout(1200);
  // full page
  await page.screenshot({ path: `${OUT}/${name}-full.jpg`, fullPage: true, type: 'jpeg', quality: 70 });
  // hero / above the fold
  await page.screenshot({ path: `${OUT}/${name}-fold.jpg`, fullPage: false, type: 'jpeg', quality: 75 });
  console.log('shot', name);
}

// mobile pass on homepage + about
const mctx = await browser.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 1 });
const mpage = await mctx.newPage();
for (const p of ['index.html', 'about.html', 'blog.html']) {
  const name = p.replace('.html', '');
  await mpage.goto(`http://localhost:8899/${p}`, { waitUntil: 'networkidle' });
  await mpage.waitForTimeout(1000);
  await mpage.screenshot({ path: `${OUT}/${name}-mobile.jpg`, fullPage: true, type: 'jpeg', quality: 70 });
  console.log('mobile', name);
}

await browser.close();
console.log('done');
