import { chromium } from 'playwright';
const OUT='_audit/qa'; const B='http://localhost:8895';
const browser=await chromium.launch();
const force='.illu{opacity:1!important;transform:none!important}';
const d=await browser.newContext({viewport:{width:1440,height:900}}); const p=await d.newPage();
const errs=[]; p.on('console',m=>{if(m.type()==='error')errs.push(m.text().slice(0,120));}); p.on('pageerror',e=>errs.push('PE:'+e.message.slice(0,120)));
// index
await p.goto(`${B}/index.html`,{waitUntil:'networkidle'}); await p.addStyleTag({content:force}); await p.waitForTimeout(700);
await (await p.$('#book')).screenshot({path:`${OUT}/cta-new.png`});
await (await p.$('#as-a-service')).screenshot({path:`${OUT}/support-cards.png`});
await (await p.$('#references')).screenshot({path:`${OUT}/refs-vm.png`});
// support page
await p.goto(`${B}/support-services.html`,{waitUntil:'networkidle'}); await p.addStyleTag({content:force}); await p.waitForTimeout(700);
const broken=await p.$$eval('img',els=>els.filter(i=>i.complete&&i.naturalWidth===0).map(i=>i.src.split('/').pop()));
await p.screenshot({path:`${OUT}/support-page.png`,fullPage:true});
console.log('errors:',JSON.stringify(errs.filter(e=>!e.includes('cdn.tailwind'))));
console.log('broken:',JSON.stringify(broken));
await browser.close();
