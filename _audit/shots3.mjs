import { chromium } from 'playwright';
const B='http://localhost:8899', OUT='_audit/qa';
const b=await chromium.launch();
const ctx=await b.newContext({viewport:{width:1280,height:900}});
const p=await ctx.newPage();
const force='.illu{opacity:1!important;transform:none!important}';
async function shot(url,sel,name){
  await p.goto(`${B}/${url}`,{waitUntil:'networkidle'});
  await p.addStyleTag({content:force}); await p.waitForTimeout(400);
  const el=sel?await p.$(sel):null;
  if(el) await el.screenshot({path:`${OUT}/${name}.png`});
  else await p.screenshot({path:`${OUT}/${name}.png`,fullPage:true});
}
await shot('index.html','#as-a-service','fb-support');
await shot('index.html','#references','fb-refs');
await shot('index.html','#book','fb-cta');
await shot('contact.html',null,'fb-contact');
await shot('about.html',null,'fb-about');
await ctx.close(); await b.close();
console.log('done');
