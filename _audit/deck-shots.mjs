// Fresh screenshots of the LIVE production site for the Markus status deck.
// Run: node "C:/Users/robid/Desktop/Aventario Claude/website/_audit/deck-shots.mjs"
import { chromium } from 'playwright';
import fs from 'fs';

const OUT = 'C:/Users/robid/Desktop/Aventario Claude/documents/management-updates/_status-deck-2026-06-20/shots';
fs.mkdirSync(OUT, { recursive: true });
const BASE = 'https://www.aventario.com';
const manifest = [];

async function reveal(page) {
  // Scroll the full page to fire GSAP ScrollTrigger reveals, then return to top.
  await page.evaluate(async () => {
    await new Promise((res) => {
      let y = 0;
      const step = Math.round(window.innerHeight * 0.8);
      const t = setInterval(() => {
        window.scrollBy(0, step);
        y += step;
        if (y >= document.body.scrollHeight + window.innerHeight) { clearInterval(t); res(); }
      }, 100);
    });
  });
  await page.waitForTimeout(900);
  await page.evaluate(() => window.scrollTo(0, 0));
  await page.waitForTimeout(500);
}

async function go(page, url) {
  try { await page.goto(url, { waitUntil: 'networkidle', timeout: 30000 }); }
  catch { try { await page.goto(url, { waitUntil: 'load', timeout: 30000 }); } catch {} }
  await page.waitForTimeout(1200);
}

const browser = await chromium.launch();

// ---- Desktop full pages ----
const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2 });
// suppress the consent banner on normal page shots so it doesn't cover content
await ctx.addInitScript(() => { try { localStorage.setItem('av-consent', 'accepted'); } catch (e) {} });
const page = await ctx.newPage();

const fullPages = [
  ['home-full', '/'],
  ['about', '/about'],
  ['services-overview', '/support-services'],
  ['service-savings', '/services/savings'],
  ['impact', '/impact'],
  ['blog', '/blog'],
  ['blog-article', '/blog/it-vendor-management'],
  ['resources', '/resources'],
  ['contact', '/contact'],
  ['webinar-registration', '/resources/savings-standardization-webinar'],
  ['de-home', '/de/'],
];
for (const [name, path] of fullPages) {
  try {
    await go(page, BASE + path);
    await reveal(page);
    const file = `${OUT}/${name}.png`;
    await page.screenshot({ path: file, fullPage: true });
    manifest.push({ name, path, file, ok: true });
    console.log('OK full', name);
  } catch (e) { manifest.push({ name, path, ok: false, err: String(e) }); console.log('FAIL full', name, String(e)); }
}

// ---- Homepage section-by-section (for comment slides) ----
await go(page, BASE + '/');
await reveal(page);
const sections = [
  ['home-sec-hero', 'section.hero-ridge'],
  ['home-sec-services', '#services'],
  ['home-sec-asaservice', '#as-a-service'],
  ['home-sec-references', '#references'],
  ['home-sec-cta', '#book'],
  ['home-sec-footer', 'footer'],
];
for (const [name, sel] of sections) {
  try {
    const el = page.locator(sel).first();
    await el.scrollIntoViewIfNeeded();
    await page.waitForTimeout(800);
    const file = `${OUT}/${name}.png`;
    await el.screenshot({ path: file });
    manifest.push({ name, sel, file, ok: true });
    console.log('OK section', name);
  } catch (e) { manifest.push({ name, sel, ok: false, err: String(e) }); console.log('FAIL section', name, String(e)); }
}
await ctx.close();

// ---- Consent banner visible (fresh storage) ----
try {
  const ctx2 = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2 });
  const p2 = await ctx2.newPage();
  await go(p2, BASE + '/');
  await p2.waitForTimeout(1500);
  const banner = p2.locator('#av-consent');
  if (await banner.count()) {
    await banner.first().screenshot({ path: `${OUT}/consent-banner.png` });
    manifest.push({ name: 'consent-banner', ok: true });
    console.log('OK consent-banner');
  } else { console.log('no consent banner visible'); }
  await ctx2.close();
} catch (e) { console.log('FAIL consent', String(e)); }

// ---- Mobile homepage (responsive proof) ----
try {
  const ctxM = await browser.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 3, isMobile: true, hasTouch: true });
  await ctxM.addInitScript(() => { try { localStorage.setItem('av-consent', 'accepted'); } catch (e) {} });
  const pm = await ctxM.newPage();
  await go(pm, BASE + '/');
  await reveal(pm);
  await pm.screenshot({ path: `${OUT}/home-mobile.png`, fullPage: true });
  manifest.push({ name: 'home-mobile', ok: true });
  console.log('OK home-mobile');
  await ctxM.close();
} catch (e) { console.log('FAIL mobile', String(e)); }

await browser.close();
fs.writeFileSync(`${OUT}/_manifest.json`, JSON.stringify(manifest, null, 2));
console.log('DONE. shots:', manifest.filter(m => m.ok).length, '/', manifest.length);
