import { chromium } from 'playwright';
const OUT='_audit/qa'; const B='http://localhost:8895';
const browser=await chromium.launch();
const force='[data-reveal]{opacity:1!important;transform:none!important}[data-hero]>span,[data-hero-fade]{transform:none!important;opacity:1!important}';
const d=await browser.newContext({viewport:{width:1440,height:900}}); const p=await d.newPage();
const errs=[]; p.on('console',m=>{if(m.type()==='error')errs.push(m.text().slice(0,120));}); p.on('pageerror',e=>errs.push('PE:'+e.message.slice(0,120)));
await p.goto(`${B}/index-v2.html`,{waitUntil:'networkidle'}); await p.addStyleTag({content:force}); await p.waitForTimeout(900);
const broken=await p.$$eval('img',els=>els.filter(i=>i.complete&&i.naturalWidth===0).map(i=>i.src.split('/').pop()));
await p.screenshot({path:`${OUT}/v2b-fulltop.png`});
for(const sel of ['#trust','#services','#method']){ const el=await p.$(sel); if(el){await el.scrollIntoViewIfNeeded(); await p.waitForTimeout(400); await el.screenshot({path:`${OUT}/v2b-${sel.replace('#','')}.png`});}}
// problem section (no id) — find the climber img section
const probSec = await p.evaluateHandle(()=>document.querySelector('#problemArt').closest('section'));
await probSec.asElement().scrollIntoViewIfNeeded(); await p.waitForTimeout(400); await probSec.asElement().screenshot({path:`${OUT}/v2b-problem.png`});
console.log('errors:',JSON.stringify(errs.filter(e=>!e.includes('cdn.tailwind'))));
console.log('broken:',JSON.stringify(broken));
await browser.close();
