import { chromium } from 'playwright';
const B = 'http://localhost:8899';
const browser = await chromium.launch();
const ctx = await browser.newContext({ viewport: { width: 1024, height: 768 } });
const p = await ctx.newPage();

async function probe(url) {
  await p.goto(`${B}/${url}`, { waitUntil: 'networkidle' });
  await p.waitForTimeout(300);
  const info = await p.evaluate(() => {
    const vw = window.innerWidth;
    const out = [];
    document.querySelectorAll('*').forEach(el => {
      const r = el.getBoundingClientRect();
      if (r.right > vw + 1 && r.width > 30) {
        out.push({ tag: el.tagName, cls: (el.className || '').toString().slice(0, 55), right: Math.round(r.right), w: Math.round(r.width) });
      }
    });
    // dedupe by widest offenders, innermost only
    return { vw, doc: document.documentElement.scrollWidth, offenders: out.sort((a,b)=>b.right-a.right).slice(0, 10) };
  });
  console.log(`\n== ${url} (vw=${info.vw}, doc=${info.doc}, xover=${info.doc-info.vw}) ==`);
  info.offenders.forEach(o => console.log(`  ${o.right}px R | w${o.w} | ${o.tag} .${o.cls}`));
}

await probe('about.html');                  // current (with my nav change)
await probe('index.previous-pre-v03.html');  // baseline (excluded from my script, old 4-link nav)
await ctx.close();
await browser.close();
