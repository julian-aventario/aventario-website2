// Render landing-page-variants.html → PDF for management review.
import { chromium } from 'playwright';
import { fileURLToPath } from 'node:url';
import path from 'node:path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const HTML = 'C:/Users/robid/Desktop/Aventario Claude/Aventario-Website-Draft/Aventario-Website/style-comparison/landing-page-variants.html';
const OUT  = 'C:/Users/robid/Desktop/Aventario Claude/Aventario-Website-Draft/Aventario-Website/style-comparison/Aventario_Homepage_Variants.pdf';

const fileUrl = 'file:///' + HTML.replace(/\\/g, '/');
console.log('Launching Chromium...');
const browser = await chromium.launch();
const ctx = await browser.newContext({ viewport: { width: 1700, height: 1300 } });
const page = await ctx.newPage();
console.log('Loading: ' + fileUrl);
await page.goto(fileUrl, { waitUntil: 'networkidle' });
await page.evaluate(async () => {
  if (document.fonts && document.fonts.ready) await document.fonts.ready;
});
await page.waitForTimeout(800);

// Measure actual content height so the PDF fits the row in one page
const heightPx = await page.evaluate(() => Math.ceil(document.body.scrollHeight) + 24);
console.log('Content height: ' + heightPx + 'px');

console.log('Rendering PDF...');
const pdfBuffer = await page.pdf({
  width:  '1700px',
  height: heightPx + 'px',
  printBackground: true,
  preferCSSPageSize: false,
  margin: { top: 0, right: 0, bottom: 0, left: 0 },
});

await browser.close();

import fs from 'node:fs';
fs.writeFileSync(OUT, pdfBuffer);
console.log('Wrote ' + OUT);
console.log('Size: ' + (pdfBuffer.length / 1024).toFixed(1) + ' KB');
