import { chromium } from 'playwright';
const B = 'http://localhost:8899';
const browser = await chromium.launch();
const ctx = await browser.newContext({ viewport: { width: 1024, height: 768 } });
const p = await ctx.newPage();
await p.goto(`${B}/about.html`, { waitUntil: 'networkidle' });
await p.waitForTimeout(300);
const info = await p.evaluate(() => {
  const vw = window.innerWidth;
  const hits = [];
  document.querySelectorAll('button, a').forEach(el => {
    const r = el.getBoundingClientRect();
    if (r.right > vw + 1 && r.width > 30) {
      const cs = getComputedStyle(el);
      const par = el.closest('[id]');
      hits.push({
        tag: el.tagName, id: el.id || '(none)', cls: (el.className||'').toString(),
        text: (el.textContent||'').trim().slice(0,40),
        pos: cs.position, right: Math.round(r.right), left: Math.round(r.left), top: Math.round(r.top),
        parentId: par ? par.id : '(no id ancestor)',
        parentHTML: el.parentElement ? el.parentElement.outerHTML.slice(0,160) : ''
      });
    }
  });
  return { vw, hits };
});
console.log(JSON.stringify(info, null, 1));
await ctx.close(); await browser.close();
