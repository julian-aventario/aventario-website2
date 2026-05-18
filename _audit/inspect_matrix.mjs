import { chromium } from 'playwright';

const b = await chromium.launch();
const ctx = await b.newContext({ viewport: { width: 1440, height: 900 } });
const p = await ctx.newPage();
await p.goto('http://localhost:8788/index.html', { waitUntil: 'networkidle' });
await p.evaluate(() => document.getElementById('services').scrollIntoView({ block: 'start' }));
await p.waitForTimeout(300);

// Measure each row of the matrix
const data = await p.evaluate(() => {
  const rail = document.querySelectorAll('#services .flex.flex-col.gap-3.w-32 > div');
  const areas = document.querySelectorAll('#services .grid.grid-cols-5 > div');
  const ms = document.querySelector('#services a[href*="managedsuppliers"]');
  const rect = el => { const r = el.getBoundingClientRect(); return { top: Math.round(r.top), bottom: Math.round(r.bottom), left: Math.round(r.left), right: Math.round(r.right), w: Math.round(r.width), h: Math.round(r.height) }; };
  return {
    leftRail: Array.from(rail).map(el => ({ text: el.textContent.trim().replace(/\s+/g,' ').slice(0,40), ...rect(el) })),
    headerArea: rect(areas[0]),
    headerArea_h3: rect(areas[0].querySelector('h3')),
    solutionRow1_first: rect(areas[5]),  // first cell of solutions row 1
    solutionRow3_first: rect(areas[15]), // first cell of solutions row 3
    crossFnWrapper: rect(areas[20]),     // col-span-5 cross-fn wrapper
    managedSuppliers: rect(ms),
    container: rect(document.querySelector('#services .hidden.md\\:block .flex.gap-3'))
  };
});

console.log(JSON.stringify(data, null, 2));
await p.screenshot({ path: '_audit/screens/_matrix_close.png', clip: { x: 0, y: 50, width: 1440, height: 850 }});
console.log('\nScreenshot → _audit/screens/_matrix_close.png');
await b.close();
