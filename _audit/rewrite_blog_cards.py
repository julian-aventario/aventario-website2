"""One-shot transform: rewrite legacy article-card blocks in blog.html into the new unified-gradient format.

- Old card had a separate `cover` div for the gradient, then text below.
- New card uses the gradient on the <a> itself with text overlaid bottom.
- Cluster badges like "Cluster 1.7" get replaced with topic-meaningful labels.
"""
import re
from pathlib import Path

BLOG = Path(r"C:/Users/robid/Desktop/Aventario Claude/website/blog.html")

# Cluster slug -> new badge label
CLUSTER_LABELS = {
    "what-is-it-vendor-management": "Cluster · Definition",
    "vendor-management-lifecycle": "Cluster · Lifecycle",
    "how-to-build-vmo": "Cluster · VMO build",
    "three-tier-governance-model": "Cluster · Governance model",
    "vendor-management-kpis": "Cluster · KPIs",
    "vendor-management-vs-supplier-management": "Cluster · Terminology",
    "hidden-cost-of-poor-vendor-management": "Cluster · Hidden cost",
    "vendor-management-maturity-assessment": "Cluster · Maturity",
    "how-to-choose-it-vendors": "Cluster · Vendor selection",
    "vendor-management-mid-market-dach": "Cluster · Mid-market",
    "vendor-governance-vacuum": "Cluster · Manifesto",
    "it-vendor-risk-framework": "Cluster · Risk framework",
    "vendor-performance-reviews": "Cluster · Performance reviews",
    "why-youre-overpaying-it-vendors": "Cluster · Overpayment",
    "it-contract-auto-renewal-trap": "Cluster · Auto-renewal",
}

text = BLOG.read_text(encoding="utf-8")

# Match the legacy form (already-converted cards are skipped because their pattern differs)
pattern = re.compile(
    r'<a href="blog/(?P<slug>[^"]+)" class="article-card group" data-format="(?P<fmt>[^"]+)" data-topic="(?P<topic>[^"]*)">\s*'
    r'<div class="cover (?P<pc>pc-\d+) aspect-\[4/3\] rounded-md mb-5 flex items-end p-5">'
    r'<span class="inline-block text-xs uppercase tracking-widest font-bold px-2\.5 py-1 rounded-full bg-surface/15 text-surface backdrop-blur-sm border border-surface/20">(?P<badge>[^<]+)</span></div>\s*'
    r'<p class="text-xs uppercase tracking-widest text-text/60 mb-2 font-bold">(?P<mins>[^<]+)</p>\s*'
    r'<h3 class="font-serif text-xl text-text mb-2 group-hover:text-accentdark transition-colors leading-tight">(?P<title>[^<]+)</h3>\s*'
    r'<p class="text-sm text-text/75 leading-relaxed">(?P<desc>[^<]+)</p>\s*'
    r'</a>',
    re.DOTALL,
)

def repl(m):
    slug = m.group("slug")
    fmt = m.group("fmt")
    topic = m.group("topic")
    pc = m.group("pc")
    badge = m.group("badge").strip()
    mins = m.group("mins").replace(" read", "").strip()
    title = m.group("title").strip()
    desc = m.group("desc").strip()

    if fmt == "cluster" and slug in CLUSTER_LABELS:
        badge = CLUSTER_LABELS[slug]

    return (
        f'<a href="blog/{slug}" class="article-card {pc}" data-format="{fmt}" data-topic="{topic}">\n'
        f'                    <div class="flex items-center justify-between gap-3">\n'
        f'                        <span class="card-badge">{badge}</span>\n'
        f'                        <span class="card-meta">{mins}</span>\n'
        f'                    </div>\n'
        f'                    <div>\n'
        f'                        <h3 class="card-title">{title}</h3>\n'
        f'                        <p class="card-desc">{desc}</p>\n'
        f'                    </div>\n'
        f'                </a>'
    )

new_text, count = pattern.subn(repl, text)
print(f"Replaced {count} cards")
BLOG.write_text(new_text, encoding="utf-8")
