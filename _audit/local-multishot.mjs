import { chromium } from 'playwright';
const pages=[["support-services","/support-services.html"],["blog","/blog.html"],["impact","/impact.html"],["contact","/contact.html"],["service-savings","/services/savings.html"],["a-blog-article","/blog/it-vendor-management.html"]];
const OUT='C:/Users/robid/Desktop/Aventario Claude/documents/management-updates/_status-deck-2026-06-20/shots/local';
const b=await chromium.launch();
const ctx=await b.newContext({viewport:{width:1440,height:900},deviceScaleFactor:1});
await ctx.addInitScript(()=>{try{localStorage.setItem('av-consent','accepted');}catch(e){}});
const p=await ctx.newPage();
for(const [name,path] of pages){
  await p.goto('http://localhost:8901'+path,{waitUntil:'networkidle',timeout:30000}).catch(()=>{});
  await p.waitForTimeout(700);
  await p.screenshot({path:`${OUT}/${name}.png`});
  console.log('shot',name);
}
await b.close();
