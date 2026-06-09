import { chromium } from 'playwright';
import { mkdirSync } from 'fs';
const OUT='_audit/qa'; mkdirSync(OUT,{recursive:true});
const B='http://localhost:8895';
const browser=await chromium.launch();
const pages=['index.html','contact.html','impact.html','resources.html','index-v2.html','about.html','blog.html','portfolio.html'];
const ctx=await browser.newContext({viewport:{width:1440,height:900}});
const page=await ctx.newPage();
const report={};
for(const p of pages){
  const errors=[]; const broken=[];
  page.removeAllListeners('console'); page.removeAllListeners('pageerror');
  page.on('console',m=>{ if(m.type()==='error') errors.push(m.text().slice(0,140)); });
  page.on('pageerror',e=>errors.push('PAGEERR: '+e.message.slice(0,140)));
  await page.goto(`${B}/${p}`,{waitUntil:'networkidle'}).catch(e=>errors.push('NAV:'+e.message));
  await page.waitForTimeout(1500);
  const imgs=await page.$$eval('img',els=>els.filter(i=>i.complete&&i.naturalWidth===0).map(i=>i.getAttribute('src')));
  broken.push(...imgs);
  report[p]={errors:errors.filter(e=>!e.includes('cdn.tailwindcss')&&!e.includes('Download the React')),broken};
}
console.log(JSON.stringify(report,null,1));
await browser.close();
