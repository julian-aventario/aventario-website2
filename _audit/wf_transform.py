#!/usr/bin/env python3
"""Site-wide workflow upgrades (idempotent):
  W1/C4 newsletter forms -> real (data-newsletter) + honeypot
  W1/W4/W6 inject shared /assets/site.js on every page
  C1 inject mobile-menu toggle on pages that have the button but no handler
  W8 inject Organization JSON-LD on pages without any JSON-LD
Run from the website/ root. Reports what it changed."""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # website/
EXCLUDE_DIRS = {'_staging', '_audit', '_backup-legal-sweep-2026-06-15', '_design', '_config',
                'style-comparison', 'illustration-gallery', 'node_modules', '.vercel', '.git'}
EXCLUDE_FILES = {'index-v2.html', 'index.previous-pre-v03.html', 'index.v03-draft.html',
                 'google3165196d202229c2.html'}

NEWSLETTER_ONSUBMIT = "onsubmit=\"event.preventDefault(); this.querySelector('button').textContent='Subscribed';\""
HONEYPOT = ('<input type="text" name="company_website" tabindex="-1" autocomplete="off" '
            'aria-hidden="true" class="hidden">')
SITE_JS_TAG = '<script src="/assets/site.js" defer></script>'
MENU_TOGGLE = ("<script>(function(){var b=document.getElementById('mobileMenuBtn'),"
               "m=document.getElementById('mobileMenu');if(b&&m){b.addEventListener('click',"
               "function(){var hidden=m.classList.toggle('hidden');"
               "b.setAttribute('aria-expanded',hidden?'false':'true');});}})();</script>")
ORG_LD = ('<script type="application/ld+json">'
          '{"@context":"https://schema.org","@type":"Organization","name":"Aventario",'
          '"legalName":"Aventario Services GmbH","url":"https://www.aventario.com",'
          '"email":"office@aventario.com","telephone":"+43 134 3354012",'
          '"address":{"@type":"PostalAddress","streetAddress":"Tuchlauben 7a","postalCode":"1010",'
          '"addressLocality":"Vienna","addressCountry":"AT"},'
          '"description":"Cost and value optimization for IT and supply chain."}</script>')

FORM_OPEN_RE = re.compile(r'(<form\s+data-newsletter\b[^>]*>)')

def iter_html():
    for dp, dns, fns in os.walk(ROOT):
        dns[:] = [d for d in dns if d not in EXCLUDE_DIRS]
        for fn in fns:
            if fn.endswith('.html') and fn not in EXCLUDE_FILES:
                yield os.path.join(dp, fn)

stats = {'newsletter': 0, 'honeypot': 0, 'sitejs': 0, 'menu': 0, 'schema': 0, 'files': 0}

for path in iter_html():
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    orig = html

    # W1/C4 newsletter: swap fake onsubmit -> data-newsletter, then add honeypot
    n_nl = html.count(NEWSLETTER_ONSUBMIT)
    if n_nl:
        html = html.replace(NEWSLETTER_ONSUBMIT, 'data-newsletter')
        stats['newsletter'] += n_nl
    def add_hp(m):
        return m.group(1) + HONEYPOT
    # inject honeypot right after each data-newsletter form open that lacks one
    def hp_inject(html):
        out, added = [], 0
        pos = 0
        for m in FORM_OPEN_RE.finditer(html):
            seg = html[m.end():m.end()+400]
            out.append(html[pos:m.end()])
            if 'name="company_website"' not in seg:
                out.append(HONEYPOT)
                added += 1
            pos = m.end()
        out.append(html[pos:])
        return ''.join(out), added
    html, hp_added = hp_inject(html)
    stats['honeypot'] += hp_added

    # W1/W4/W6 shared script before </body>
    if '/assets/site.js' not in html and '</body>' in html:
        html = html.replace('</body>', '    ' + SITE_JS_TAG + '\n  </body>', 1)
        stats['sitejs'] += 1

    # C1 mobile menu toggle where button exists but no handler
    if 'id="mobileMenuBtn"' in html and "getElementById('mobileMenuBtn')" not in html and '</body>' in html:
        html = html.replace('</body>', '    ' + MENU_TOGGLE + '\n  </body>', 1)
        stats['menu'] += 1

    # W8 Organization schema on pages without any JSON-LD
    if 'application/ld+json' not in html and '</head>' in html:
        html = html.replace('</head>', '    ' + ORG_LD + '\n</head>', 1)
        stats['schema'] += 1

    if html != orig:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        stats['files'] += 1

print('Changed files:', stats['files'])
for k in ('newsletter', 'honeypot', 'sitejs', 'menu', 'schema'):
    print(f'  {k}: {stats[k]}')
