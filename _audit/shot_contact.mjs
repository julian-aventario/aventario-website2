import { chromium } from 'playwright';
const b = await chromium.launch();
const p = await b.newPage({ viewport: { width: 1280, height: 800 }, deviceScaleFactor: 1 });
const errs = [];
p.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
await p.goto('http://localhost:8899/contact.html', { waitUntil: 'networkidle' });
await p.screenshot({ path: '_audit/qa/contact-after.png' });
// overflow check
const ov = await p.evaluate(() => document.documentElement.scrollWidth > window.innerWidth + 1);
const hasForm = await p.evaluate(() => !!document.querySelector('form textarea'));
const hasBook = await p.evaluate(() => !!document.querySelector('#book iframe'));
console.log(JSON.stringify({ errs, overflow: ov, contactFormStillPresent: hasForm, schedulerPresent: hasBook }));
await b.close();
