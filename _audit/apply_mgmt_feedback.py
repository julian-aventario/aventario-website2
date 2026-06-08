#!/usr/bin/env python3
# Management feedback pass (PPTX): remove Services + Blog from nav (desktop +
# mobile), drop the footer Services column and Blog link, swap the invented
# footer claim for the standard claim, rebalance the footer. Idempotent,
# prefix-tolerant, live pages only.
import re, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
EXCLUDE_DIRS = {"node_modules", "_staging", ".vercel", "_audit",
                "style-comparison", "illustration-gallery", "_build", "logos"}
EXCLUDE_FILES = {"index-v2.html", "index.v03-draft.html",
                 "index.previous-pre-v03.html"}

OLD_CLAIM = "We help enterprises master complexity in service-cost optimization, sourcing &amp; transformation."
NEW_CLAIM = "Cost &amp; value optimization for IT and supply chain."

def process(path):
    s = path.read_text(encoding="utf-8")
    o = s
    notes = []

    # 1. nav desktop: remove Services + Blog links (with preceding whitespace)
    for label, slug in (("Services", "portfolio"), ("Blog", "blog")):
        s, n = re.subn(
            r'\n\s*<a href="(?:\.\./)*' + slug + r'\.html" class="hover:text-accentdark">' + label + r'</a>',
            '', s)
        if n: notes.append(f"nav-{label.lower()}")

    # 2. nav mobile: remove Services + Blog links
    for label, slug in (("Services", "portfolio"), ("Blog", "blog")):
        s, n = re.subn(
            r'\n\s*<a href="(?:\.\./)*' + slug + r'\.html" class="block py-2 text-base font-bold uppercase tracking-widest hover:text-accentdark">' + label + r'</a>',
            '', s)
        if n: notes.append(f"mnav-{label.lower()}")

    # 3. nav spacing back to space-x-8 (fewer items now)
    s2 = s.replace("hidden lg:flex space-x-6 text-sm uppercase tracking-widest font-bold items-center",
                   "hidden lg:flex space-x-8 text-sm uppercase tracking-widest font-bold items-center")
    if s2 != s: notes.append("nav-space"); s = s2

    # 4. footer: remove Blog link
    s, n = re.subn(r'\n\s*<li><a href="(?:\.\./)*blog\.html" class="hover:text-accent">Blog</a></li>', '', s)
    if n: notes.append("footer-blog")

    # 5. footer: remove the entire Services column block
    s, n = re.subn(
        r'\n\s*<div class="lg:col-span-2">\s*<p[^>]*>Services</p>.*?</ul>\s*</div>',
        '', s, flags=re.S)
    services_removed = bool(n)
    if n: notes.append("footer-services-col")

    # 6. footer: swap invented claim for standard claim
    if OLD_CLAIM in s:
        s = s.replace(OLD_CLAIM, NEW_CLAIM); notes.append("footer-claim")

    # 7. rebalance footer columns only where the Services column was removed
    if services_removed:
        s2 = re.sub(r'(<div class=")lg:col-span-2(">\s*<a href="(?:\.\./)*index\.html" class="inline-flex items-center mb-5">)',
                    r'\1lg:col-span-3\2', s)
        s2 = s2.replace('<div class="lg:col-span-4 space-y-4">', '<div class="lg:col-span-5 space-y-4">')
        if s2 != s: notes.append("footer-rebalance"); s = s2

    if s != o:
        path.write_text(s, encoding="utf-8")
        return notes
    return None

def main():
    changed = 0
    for path in sorted(ROOT.rglob("*.html")):
        rel = path.relative_to(ROOT)
        if any(p in EXCLUDE_DIRS for p in rel.parts): continue
        if path.name in EXCLUDE_FILES: continue
        notes = process(path)
        if notes:
            changed += 1
    print(f"{changed} files updated.")

if __name__ == "__main__":
    main()
