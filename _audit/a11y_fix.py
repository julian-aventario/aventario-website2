#!/usr/bin/env python3
import re, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent  # website/
SKIP_DIRS = ('.vercel', '_staging', '_audit')
SKIP_NAMES = {'index-v2.html', 'index.previous-pre-v03.html', 'index.v03-draft.html'}

def is_prod(p: pathlib.Path) -> bool:
    parts = p.parts
    if any(s in parts for s in SKIP_DIRS): return False
    if any(part.startswith('_backup') for part in parts): return False
    if p.name in SKIP_NAMES: return False
    return True

files = [p for p in ROOT.rglob('*.html') if is_prod(p)]

stats = {'labels_removed':0, 'accentdark_token':0, 'inline_color':0,
         'logo_aria':0, 'main_added':0, 'heading_fixed':0, 'files_changed':0}

SPAN_RE = re.compile(r'<span\b[^>]*>.*?</span>', re.DOTALL)

def is_card_cta(m: str) -> bool:
    return ('uppercase tracking-widest' in m and 'inline-flex' in m
            and ('text-accentdark' in m or '#8dccc0' in m)
            and ('ph-arrow' in m or 'arrow-right' in m))

LOGO_LINKS = [
    '<a href="../index.html" class="flex items-center">',
    '<a href="index.html" class="flex items-center">',
    '<a href="../index.html" class="inline-flex items-center mb-5">',
    '<a href="index.html" class="inline-flex items-center mb-5">',
    '<a href="index.html" class="inline-flex items-center">',
]

for p in files:
    html = p.read_text(encoding='utf-8')
    orig = html
    is_de = 'de' in p.parts
    label = 'Aventario Startseite' if is_de else 'Aventario Home'

    # 1) remove low-contrast card CTA label spans
    def repl_span(m):
        t = m.group(0)
        if is_card_cta(t):
            stats['labels_removed'] += 1
            return ''
        return t
    html = SPAN_RE.sub(repl_span, html)

    # 2) accentdark token -> accessible deep teal
    html, n = re.subn(r"accentdark:\s*'#5fa99d'", "accentdark: '#2C7A6B'", html, flags=re.I)
    stats['accentdark_token'] += n
    # inline text color usages only (NOT gradients / outlines)
    html, n = re.subn(r'color:\s*#5fa99d', 'color:#2C7A6B', html, flags=re.I)
    stats['inline_color'] += n

    # 3) logo links -> add aria-label (skip if already labelled)
    for link in LOGO_LINKS:
        if link in html:
            labelled = link[:-1] + f' aria-label="{label}">'
            cnt = html.count(link)
            html = html.replace(link, labelled)
            stats['logo_aria'] += cnt

    # 4) main landmark if missing
    if not re.search(r'<main[\s>]', html, re.I):
        if '</nav>' in html and '<footer' in html:
            html = html.replace('</nav>', '</nav>\n    <main>', 1)
            html = html.replace('<footer', '</main>\n    <footer', 1)
            stats['main_added'] += 1

    # 5) heading order: index.html service cards h4 -> h3
    if p.name == 'index.html' and p.parent == ROOT:
        html, n = re.subn(
            r'<h4(\s+class="font-serif text-xl text-text mb-4 group-hover:text-accentdark transition-colors">.*?)</h4>',
            r'<h3\1</h3>', html, flags=re.DOTALL)
        stats['heading_fixed'] += n

    if html != orig:
        p.write_text(html, encoding='utf-8')
        stats['files_changed'] += 1

print(f"production files scanned: {len(files)}")
for k, v in stats.items():
    print(f"  {k}: {v}")
