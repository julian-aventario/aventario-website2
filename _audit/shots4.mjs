import { chromium } from 'playwright';
const B='http://localhost:8899', OUT='_audit/qa';
const b=await chromium.launch();
const ctx=await b.newContext({viewport:{width:1280,height:760}});
const p=await ctx.newPage();
await p.goto(`${B}/contact.html`,{waitUntil:'networkidle'});await p.waitForTimeout(400);
await p.screenshot({path:`${OUT}/fb-contact-top.png`});           // hero + form
await p.evaluate(()=>window.scrollTo(0,780));await p.waitForTimeout(300);
await p.screenshot({path:`${OUT}/fb-contact-sched.png`});         // scheduler
await ctx.close(); await b.close(); console.log('done');
