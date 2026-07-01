#!/usr/bin/env python3
"""Add honeypot (C4/W9) + UTM attribution merge (W4) to the real lead forms."""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES = ['contact.html', 'de/contact.html', 'webinar.html', 'de/webinar.html',
         'resources/operative-vendor-management.html', 'de/resources/operative-vendor-management.html']
HP = ('<input type="text" name="company_website" tabindex="-1" autocomplete="off" '
      'aria-hidden="true" class="hidden">')
HP_CHECK = ("\n                var _hp=e.target.querySelector('input[name=company_website]');"
            "if(_hp&&_hp.value)return;")
UTM_MERGE = "try{Object.assign(data,(window.avAttr&&window.avAttr())||{});}catch(_){}\n                    "

for rel in FILES:
    p = os.path.join(ROOT, rel)
    if not os.path.exists(p):
        print('MISSING', rel); continue
    with open(p, 'r', encoding='utf-8') as f:
        html = f.read()
    orig = html
    # 1) honeypot input after the real form's opening tag (contactForm/regForm/wpForm)
    for fid in ('contactForm', 'regForm', 'wpForm'):
        tag_start = html.find('<form id="' + fid + '"')
        if tag_start != -1:
            tag_end = html.find('>', tag_start) + 1
            if 'name="company_website"' not in html[tag_end:tag_end + 300]:
                html = html[:tag_end] + HP + html[tag_end:]
            break
    # 2) honeypot check right after e.preventDefault();  (only the inline real-form handler)
    if HP_CHECK.strip() not in html:
        html = html.replace('e.preventDefault();', 'e.preventDefault();' + HP_CHECK, 1)
    # 3) merge UTM/referrer into the payload just before the Supabase POST
    if 'window.avAttr' not in html:
        html = html.replace("var r = await fetch(SB_URL + '/rest/v1/",
                            UTM_MERGE + "var r = await fetch(SB_URL + '/rest/v1/", 1)
    if html != orig:
        with open(p, 'w', encoding='utf-8') as f:
            f.write(html)
        print('updated', rel)
    else:
        print('no-change', rel)
