import { chromium } from 'playwright';
const b = await chromium.launch();
const p = await (await b.newContext({viewport:{width:1440,height:900}})).newPage();
await p.goto('http://localhost:8895/index.html',{waitUntil:'networkidle'});
await p.addStyleTag({content:'.illu{opacity:1!important;transform:none!important}'});
await p.waitForTimeout(500);
await (await p.$('#references')).screenshot({path:'_audit/diag/idx-references.png'});
await (await p.$('#as-a-service')).screenshot({path:'_audit/diag/idx-asaservice.png'});
console.log('done'); await b.close();
