import { chromium } from 'playwright';
import { mkdirSync } from 'fs';
const OUT='_audit/qa'; mkdirSync(OUT,{recursive:true});
const B='http://localhost:8895';
const browser=await chromium.launch();
const force='[data-reveal]{opacity:1!important;transform:none!important}[data-hero]>span,[data-hero-fade]{transform:none!important;opacity:1!important}.illu{opacity:1!important;transform:none!important}';
// v2 desktop
const d=await browser.newContext({viewport:{width:1440,height:900}}); const dp=await d.newPage();
await dp.goto(`${B}/index-v2.html`,{waitUntil:'networkidle'}); await dp.addStyleTag({content:force}); await dp.waitForTimeout(800);
await dp.screenshot({path:`${OUT}/v2-hero.png`});
for(const sel of ['#services','#method','#proof']){ const el=await dp.$(sel); if(el){ await el.scrollIntoViewIfNeeded(); await dp.waitForTimeout(500); await el.screenshot({path:`${OUT}/v2-${sel.replace('#','')}.png`}); } }
// index fixes
await dp.goto(`${B}/index.html`,{waitUntil:'networkidle'}); await dp.addStyleTag({content:force}); await dp.waitForTimeout(600);
await (await dp.$('#book')).screenshot({path:`${OUT}/idx-book.png`});
await (await dp.$('#as-a-service')).screenshot({path:`${OUT}/idx-asaservice.png`});
// contact scheduler
await dp.goto(`${B}/contact.html`,{waitUntil:'networkidle'}); await dp.waitForTimeout(1500);
await (await dp.$('#book')).screenshot({path:`${OUT}/contact-book.png`});
// v2 mobile
const m=await browser.newContext({viewport:{width:390,height:844}}); const mp=await m.newPage();
await mp.goto(`${B}/index-v2.html`,{waitUntil:'networkidle'}); await mp.addStyleTag({content:force}); await mp.waitForTimeout(800);
await mp.screenshot({path:`${OUT}/v2-mobile-hero.png`});
console.log('done'); await browser.close();
