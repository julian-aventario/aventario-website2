import { chromium } from 'playwright';
const b = await chromium.launch();
const p = await (await b.newContext({viewport:{width:1440,height:900}})).newPage();
await p.goto('http://localhost:8895/impact.html',{waitUntil:'networkidle'});
await p.waitForTimeout(600);
const countVisible = async () => p.$$eval('.impact-card', els => els.filter(e=>e.offsetParent!==null).length);
const initial = await countVisible();
// click Savings area
await p.click('button[data-area="savings"]');
await p.waitForTimeout(300);
const afterArea = await countVisible();
// which sub-topics are now visible
const visibleSubs = await p.$$eval('#impact-filter-solution button', els => els.filter(e=>e.style.display!=='none').map(e=>e.dataset.solution));
const solWrapHidden = await p.$eval('#solWrap', e => e.classList.contains('hidden'));
await p.locator('#impact-filterbar').screenshot({path:'_audit/diag/filter-savings.png'});
// click a sub-topic
await p.click('button[data-solution="service-cost"]');
await p.waitForTimeout(300);
const afterSub = await countVisible();
console.log(JSON.stringify({initial, afterArea, solWrapHidden, visibleSubs, afterSub}, null, 0));
await b.close();
