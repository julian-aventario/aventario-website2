import { chromium } from 'playwright';
const b=await chromium.launch();
const p=await (await b.newContext({viewport:{width:1440,height:900}})).newPage();
await p.goto('http://localhost:8895/index.html',{waitUntil:'networkidle'});
await p.waitForTimeout(800);
const info=await p.$eval('#book img', img=>{
  const r=img.getBoundingClientRect();
  return {src:img.getAttribute('src'), natW:img.naturalWidth, natH:img.naturalHeight, w:Math.round(r.width), h:Math.round(r.height), opacity:getComputedStyle(img).opacity, cls:img.className};
});
console.log(JSON.stringify(info));
await b.close();
