import { chromium } from 'playwright';
import { mkdirSync } from 'fs';

const OUT = '_audit/shots';
mkdirSync(OUT, { recursive: true });

const browser = await chromium.launch();
const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1 });
const page = await ctx.newPage();

async function scrollThrough() {
  await page.evaluate(async () => {
    await new Promise((resolve) => {
      let y = 0;
      const step = 600;
      const timer = setInterval(() => {
        window.scrollBy(0, step);
        y += step;
        if (y >= document.body.scrollHeight) { clearInterval(timer); resolve(); }
      }, 100);
    });
  });
  await page.waitForTimeout(2500);
  await page.evaluate(() => window.scrollTo(0, 0));
  await page.waitForTimeout(800);
}

for (const p of ['index.html', 'contact.html']) {
  const name = p.replace('.html', '');
  await page.goto(`http://localhost:8899/${p}`, { waitUntil: 'networkidle' });
  await scrollThrough();
  await page.screenshot({ path: `${OUT}/${name}-full2.jpg`, fullPage: true, type: 'jpeg', quality: 68 });
  console.log('shot', name);
}

await browser.close();
console.log('done');
