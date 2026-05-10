"""
One-shot builder for the 9 remaining pillar pages (Pillar 1 was hand-written).
Writes self-contained HTML files into ./blog/ matching the design of pillar 1.
"""
from pathlib import Path
from textwrap import dedent

OUT = Path(__file__).parent / "blog"
OUT.mkdir(exist_ok=True)

HEAD = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} — Aventario</title>
    <meta name="description" content="{description}">
    <link rel="canonical" href="https://aventario.com/blog/{slug}">
    <meta property="og:type" content="article">
    <meta property="og:title" content="{og_title}">
    <meta property="og:description" content="{description}">
    <meta property="og:url" content="https://aventario.com/blog/{slug}">
    <meta property="og:site_name" content="Aventario">
    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 55.42 55.2'%3E%3Cdefs%3E%3ClinearGradient id='g' x1='11.43' y1='48.04' x2='37.22' y2='48.04' gradientUnits='userSpaceOnUse'%3E%3Cstop offset='0' stop-color='%23324a60'/%3E%3Cstop offset='.45' stop-color='%236a9a9b'/%3E%3Cstop offset='1' stop-color='%238dccc0'/%3E%3C/linearGradient%3E%3C/defs%3E%3Cpath d='M37.22,40.94l-5.14-8.91c-.11-.19-.38-.19-.49,0l-5.14,8.91h10.78Z' fill='%238dccc0'/%3E%3Cpolygon points='11.43 55.15 37.22 40.94 26.44 40.94 16.64 46.19 15.81 47.62 11.51 55.06 11.43 55.15' fill='url(%23g)'/%3E%3Cpath d='M55.38,40.51l-7.53-13.05L32.08,.14c-.11-.19-.38-.19-.49,0L15.81,27.46.04,54.78c-.06,.1-.05,.21,0,.29,.05,.08,.13,.14,.24,.14H11.26c.1,0,.2-.05,.25-.14l4.3-7.45,.83-1.43,14.95-25.89c.11-.19,.38-.19,.49,0l11.83,20.49c.05,.09,.15,.14,.25,.14h10.98c.22,0,.36-.24,.25-.43Z' fill='%23324a60'/%3E%3C/svg%3E">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Lato:wght@400;700;900&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{ theme: {{ extend: {{ colors: {{ base: '#FAFAF7', surface: '#FFFFFF', text: '#334b60', muted: '#5f768b', accent: '#88C9BE', accentdark: '#5FA99D', orange: '#f19a51', bordercolor: 'rgba(51, 75, 96, 0.12)' }}, fontFamily: {{ serif: ['"Lato"', '-apple-system', 'sans-serif'], sans: ['"Lato"', '-apple-system', 'sans-serif'] }} }} }} }}
    </script>
    <script src="https://unpkg.com/@phosphor-icons/web"></script>
    <style>
        body {{ background-color: #FAFAF7; color: #334b60; font-family: 'Lato', -apple-system, sans-serif; font-weight: 400; -webkit-font-smoothing: antialiased; }}
        h1, h2, h3, h4, h5, .font-serif {{ font-family: 'Lato', -apple-system, sans-serif; font-weight: 900; letter-spacing: -0.015em; line-height: 1.1; }}
        .post-cover {{ background: {gradient}; }}
        .prose-aventario p {{ font-size: 1.125rem; line-height: 1.7; margin-bottom: 1.4rem; color: #334b60; }}
        .prose-aventario h2 {{ font-size: 1.875rem; margin-top: 3rem; margin-bottom: 1rem; }}
        .prose-aventario h3 {{ font-size: 1.375rem; margin-top: 2rem; margin-bottom: 0.75rem; }}
        .prose-aventario ul {{ margin-bottom: 1.4rem; padding-left: 1.5rem; }}
        .prose-aventario ul li {{ font-size: 1.125rem; line-height: 1.7; margin-bottom: 0.5rem; list-style: disc; color: #334b60; }}
        .prose-aventario ol {{ margin-bottom: 1.4rem; padding-left: 1.5rem; }}
        .prose-aventario ol li {{ font-size: 1.125rem; line-height: 1.7; margin-bottom: 0.6rem; list-style: decimal; color: #334b60; }}
        .prose-aventario a {{ color: #5FA99D; font-weight: 700; text-decoration: underline; text-decoration-thickness: 1px; text-underline-offset: 3px; }}
        .prose-aventario a:hover {{ color: #334b60; }}
        .prose-aventario strong {{ font-weight: 900; color: #334b60; }}
        .pull-quote {{ background: #FFFFFF; border-top: 3px solid #88C9BE; border-bottom: 3px solid #88C9BE; padding: 1.75rem 1.5rem; margin: 2.5rem 0; }}
        .pull-quote p {{ font-size: 1.25rem; font-weight: 700; line-height: 1.4; color: #334b60; margin-bottom: 0.5rem; }}
        .pull-quote cite {{ font-size: 0.875rem; font-style: normal; color: #5f768b; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; }}
    </style>
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "Article",
      "headline": "{schema_headline}",
      "description": "{description}",
      "datePublished": "2026-05-07",
      "dateModified": "2026-05-07",
      "author": {{
        "@type": "Person",
        "name": "Julian Robida",
        "jobTitle": "Research Lead",
        "worksFor": {{ "@type": "Organization", "name": "Aventario" }}
      }},
      "publisher": {{
        "@type": "Organization",
        "name": "Aventario",
        "logo": {{ "@type": "ImageObject", "url": "https://aventario.com/logos/aventario-logo-CMYK.png" }}
      }},
      "mainEntityOfPage": "https://aventario.com/blog/{slug}",
      "mentions": [{schema_mentions}]
    }}
    </script>
</head>
<body>

    <nav class="sticky top-0 z-40 bg-base/95 backdrop-blur-sm border-b border-bordercolor px-6 md:px-12 py-4 flex justify-between items-center">
        <a href="../index.html" class="flex items-center"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 199.29 55.2" class="h-6"><g><path d="M37.22,40.94l-5.14-8.91c-.11-.19-.38-.19-.49,0l-5.14,8.91h10.78Z" fill="#8dccc0"/><polygon points="11.43 55.15 37.22 40.94 26.44 40.94 16.64 46.19 15.81 47.62 11.51 55.06 11.43 55.15" fill="#324a60"/><path d="M55.38,40.51l-7.53-13.05L32.08,.14c-.11-.19-.38-.19-.49,0L15.81,27.46.04,54.78c-.06,.1-.05,.21,0,.29,.05,.08,.13,.14,.24,.14H11.26c.1,0,.2-.05,.25-.14l4.3-7.45,.83-1.43,14.95-25.89c.11-.19,.38-.19,.49,0l11.83,20.49c.05,.09,.15,.14,.25,.14h10.98c.22,0,.36-.24,.25-.43Z" fill="#324a60"/></g></svg></a>
        <div class="hidden md:flex space-x-8 text-xs uppercase tracking-widest font-bold items-center">
            <a href="../index.html#services" class="hover:text-accentdark">Services</a>
            <a href="../success-stories.html" class="hover:text-accentdark">Success Stories</a>
            <a href="../blog.html" class="text-accentdark">Blog</a>
            <a href="../about.html" class="hover:text-accentdark">About</a>
            <a href="../contact.html" class="hover:text-accentdark">Contact</a>
        </div>
        <a href="../contact.html" class="hidden md:inline-flex text-xs font-bold uppercase tracking-widest bg-text text-surface px-5 py-2.5 rounded-full">Contact Us</a>
    </nav>

    <section class="bg-surface px-6 md:px-12 pt-16 md:pt-24 pb-12 border-b border-bordercolor">
        <div class="max-w-3xl mx-auto">
            <a href="../blog.html" class="inline-flex items-center gap-2 text-xs uppercase tracking-widest text-text/60 hover:text-text mb-8"><i class="ph ph-arrow-left"></i> Back to blog</a>
            <span class="inline-block text-xs uppercase tracking-widest font-bold px-3 py-1 rounded-full bg-text text-surface mb-6">{topic} · Pillar</span>
            <h1 class="font-serif text-4xl md:text-6xl mb-6">{h1}</h1>
            <p class="text-xl text-text/80 leading-relaxed mb-8">{tagline}</p>
            <div class="flex items-center gap-4 pt-4 border-t border-bordercolor">
                <div class="w-12 h-12 rounded-full bg-text text-surface flex items-center justify-center text-sm font-bold">JR</div>
                <div class="text-sm">
                    <p class="font-bold text-text">Julian Robida</p>
                    <p class="text-text/60">Research Lead · Aventario · {read_time} · 7 May 2026</p>
                </div>
            </div>
        </div>
    </section>

    <section class="bg-base px-6 md:px-12 py-12">
        <div class="max-w-4xl mx-auto post-cover aspect-[16/7] rounded-md"></div>
    </section>

    <article class="bg-base px-6 md:px-12 pb-20">
        <div class="max-w-3xl mx-auto prose-aventario">
{body}
        </div>
    </article>

    <section class="px-6 md:px-12 py-20" style="background-color: #334b60; color: #FFFFFF;">
        <div class="max-w-3xl mx-auto text-center">
            <h2 class="font-serif text-3xl md:text-4xl text-surface mb-4">{cta_title}</h2>
            <p class="text-lg leading-relaxed mb-8" style="color: rgba(255,255,255,0.75);">{cta_body}</p>
            <a href="../contact.html" class="inline-flex items-center gap-3 text-sm font-bold uppercase tracking-widest px-8 py-4 rounded-full" style="background-color: #f19a51; color: #FFFFFF;">Get in touch <i class="ph ph-arrow-right"></i></a>
        </div>
    </section>

    <footer class="bg-text text-surface px-6 md:px-12 py-16">
        <div class="max-w-6xl mx-auto">
            <div class="grid grid-cols-1 md:grid-cols-12 gap-10 mb-12">
                <div class="md:col-span-5">
                    <p class="font-serif text-2xl mb-3">Aventario</p>
                    <p class="text-sm text-surface/60 max-w-sm">Cost &amp; value optimization for IT and supply chain. We own the outcome, not just the hours.</p>
                </div>
                <div class="md:col-span-3">
                    <p class="text-xs uppercase tracking-widest text-surface/40 mb-4 font-bold">Contact</p>
                    <ul class="space-y-2 text-sm text-surface/80">
                        <li><a href="mailto:office@aventario.com" class="hover:text-accent">office@aventario.com</a></li>
                        <li>Tuchlauben 7a, 1010 Vienna</li>
                        <li>+43 134 3354012</li>
                    </ul>
                </div>
                <div class="md:col-span-2">
                    <p class="text-xs uppercase tracking-widest text-surface/40 mb-4 font-bold">Services</p>
                    <ul class="space-y-2 text-sm text-surface/80">
                        <li><a href="../services/savings.html" class="hover:text-accent">Savings</a></li>
                        <li><a href="../services/complex-rfx.html" class="hover:text-accent">Complex RFx</a></li>
                        <li><a href="../services/vendor-management.html" class="hover:text-accent">Vendor Management</a></li>
                    </ul>
                </div>
                <div class="md:col-span-2">
                    <p class="text-xs uppercase tracking-widest text-surface/40 mb-4 font-bold">Company</p>
                    <ul class="space-y-2 text-sm text-surface/80">
                        <li><a href="../about.html" class="hover:text-accent">About</a></li>
                        <li><a href="../success-stories.html" class="hover:text-accent">Success Stories</a></li>
                        <li><a href="../blog.html" class="hover:text-accent">Blog</a></li>
                    </ul>
                </div>
            </div>
            <div class="border-t border-surface/10 pt-6 flex flex-col sm:flex-row justify-between items-start sm:items-center text-xs text-surface/40 gap-2">
                <p>&copy; 2026 Aventario Services GmbH</p>
                <div class="flex gap-6">
                    <a href="../impressum.html" class="hover:text-surface">Imprint</a>
                    <a href="../datenschutz.html" class="hover:text-surface">Privacy</a>
                </div>
            </div>
        </div>
    </footer>
</body>
</html>"""

GRADIENTS = {
    "p2": "linear-gradient(135deg, #88c9be 0%, #5fa99d 100%)",
    "p3": "linear-gradient(135deg, #f19a51 0%, #d15298 100%)",
    "p4": "linear-gradient(135deg, #334b60 0%, #d15298 100%)",
    "p5": "linear-gradient(135deg, #5fa99d 0%, #334b60 100%)",
    "p6": "linear-gradient(135deg, #334b60 0%, #5f768b 100%)",
    "p7": "linear-gradient(135deg, #f19a51 0%, #334b60 100%)",
    "p8": "linear-gradient(135deg, #334b60 0%, #88c9be 100%)",
    "p9": "linear-gradient(135deg, #d15298 0%, #5fa99d 100%)",
    "p10": "linear-gradient(135deg, #5f768b 0%, #88c9be 100%)",
}

def expert_bio(name, role):
    return f"""<hr class="my-12 border-bordercolor">
            <p class="text-sm text-text/60">Julian Robida is Research Lead at Aventario. {name} ({role}) contributed expert input drawn from 25+ years of running IT engagements across pharma, automotive, financial services, and the public sector. Aventario is a boutique consultancy in Vienna; we have negotiated over €3B in IT contract volume and delivered more than 500 engagements across DACH and beyond.</p>"""

def related(items):
    rows = "\n".join(f'                    <li><a href="{slug}">{label}</a></li>' for slug, label in items)
    return f"""
            <div class="mt-12 p-8 bg-surface border border-bordercolor rounded-md">
                <p class="text-xs uppercase tracking-widest text-text font-bold mb-3">Related reading</p>
                <ul class="space-y-2">
{rows}
                </ul>
            </div>"""

def quote(text, attrib):
    return f"""
            <div class="pull-quote">
                <p>"{text}"</p>
                <cite>— {attrib}</cite>
            </div>"""

# ---------- PILLAR DEFINITIONS ----------

PILLARS = []

# ============ PILLAR 2: SAVINGS ============
PILLARS.append(dict(
    slug="it-vendor-spend-optimization",
    title="IT Vendor Spend Optimization (2026 Guide)",
    og_title="How to Recover 10–40% of Your IT Budget",
    description="A field-tested guide to finding and recovering the 10–40% of IT vendor spend that most organisations are quietly overpaying. Built from €3B in benchmarked contract volume.",
    schema_headline="IT Vendor Spend Optimization: How to Recover 10–40% of Your IT Budget",
    schema_mentions='{"@type": "Person", "name": "Margit Györfi", "jobTitle": "CPO", "worksFor": {"@type": "Organization", "name": "Aventario"}}',
    gradient=GRADIENTS["p2"],
    topic="Savings",
    h1="IT vendor spend optimization.",
    tagline="How to recover 10–40% of your IT budget — without renegotiating in bad faith, breaking strategic relationships, or pretending it's just about price.",
    read_time="13 min read",
    cta_title="Find your 10–40%.",
    cta_body="We run an outcome-based savings engagement: you only pay against realised savings. €3B of benchmark data does the heavy lifting.",
    body_sections=[
        ("Quick answer.",
         "<p>Across the IT vendor portfolios we assess, the recoverable overpayment sits between 10% and 40% of annual contracted spend. The variance isn't random — it tracks how long since the last benchmark, how much auto-renewal has happened unread, and how concentrated the portfolio is in two or three categories where market pricing has moved faster than the contract.</p><p>This article is a practical map of where that money sits and how to get it back.</p>"),
        ("Why most IT contracts overpay, structurally.",
         "<p>IT services pricing has three properties that compound against the buyer over time. First, prices reset upward at renewal by default — the contract was negotiated when the market was tighter, the vendor's cost base has improved, but the rate card has not. Second, scope tends to drift one direction: change requests add, they rarely subtract. Third, the buyer's leverage is asymmetric: at renewal the vendor knows exactly what it would cost you to leave, you do not know exactly what the next provider would charge.</p><p>The combined effect is a slow upward drift in unit prices and a slow downward drift in delivered value. We call the resulting gap the <strong>Vendor Governance Vacuum™</strong> — the structural space between contract signature and contract delivery where savings erode quietly while everyone is busy with the next thing.</p>"),
        ("Where the money actually hides.",
         "<p>From the engagement archive, eight categories account for the bulk of recoverable spend. They are listed roughly in order of how reliably each shows up:</p><ul><li><strong>Auto-renewed contracts.</strong> The notice window closed unread; the deal rolled forward at the original price for another two to five years. We routinely find 15–25% of a portfolio in this state at first assessment.</li><li><strong>Unused entitlements.</strong> Licences provisioned but not deployed. Support tiers paid for but not consumed. Pre-paid professional services hours sitting in an escrow that nobody tracks. Often 5–15% of category spend.</li><li><strong>Tier mismatch.</strong> Premium support on commodity workloads. 24/7 SLAs on systems that are read-only outside business hours.</li><li><strong>Volume-band drift.</strong> Original pricing assumed a usage band the organisation has long since outgrown — both ways. Some contracts under-deliver volume discount; others penalise for unused commitment.</li><li><strong>Stranded shelfware.</strong> Software bought as part of a bundle, never deployed, still being maintained.</li><li><strong>Change-request creep.</strong> Original SOW for €X, three CRs later the run-rate is 1.6× the original price, and nobody can fully reconstruct the path from A to B.</li><li><strong>Benchmark-stale rate cards.</strong> Day rates and unit prices that are 18–36 months behind the market.</li><li><strong>Hidden hyperscaler waste.</strong> Idle compute, oversized instances, untagged resources, dev environments running 24/7.</li></ul>"),
        ("AI-augmented contract analysis.",
         "<p>What used to take a senior consultant two weeks per major vendor — reading the contract, benchmarking line items, modelling the renegotiation envelope — now takes a few hours with the right tooling. Aventario's contract-analysis pipeline ingests the executed contract, the SOW, the latest invoice run, and the SLA reports, and outputs a line-by-line gap analysis against the benchmark base.</p><p>The point isn't speed for its own sake. The point is that you can run this across the entire portfolio rather than the top three vendors, which is where most cost-recovery programmes draw the line and where 30–50% of the recoverable spend tends to sit.</p>"),
        ("The renegotiation envelope, defined.",
         "<p>Every renegotiation has an upper bound (what the vendor will accept before they walk) and a lower bound (what you will accept before <em>you</em> walk). The envelope between the two is what the negotiation is for. Most procurement-led renegotiations approach this as a single number; we treat it as a portfolio.</p><ul><li><strong>Price.</strong> Unit rates, volume bands, FX adjustments, indexation clauses.</li><li><strong>Terms.</strong> Notice periods, exit rights, benchmark rights, rate-review cadence.</li><li><strong>Scope.</strong> What is in, what is out, what triggers a CR, what is bundled.</li><li><strong>Service level.</strong> SLA targets, OLA underpinnings, service credits.</li><li><strong>Innovation commitment.</strong> Contractual obligations to bring roadmap value and continuous improvement.</li></ul><p>A good negotiation trades across these dimensions. A bad one fixates on price and gives up the terms that would have made the next negotiation easier.</p>"),
        ("The 30/60/90 quick-wins playbook.",
         "<p>You don't need to wait for a six-month transformation programme. Most portfolios contain immediate, low-risk savings that can land inside one quarter:</p><ol><li><strong>Days 1–30 — Visibility.</strong> Pull every contract with renewal in the next 12 months. Identify the auto-renewal traps and trigger formal notice on the ones with material overpayment risk.</li><li><strong>Days 31–60 — Quick fixes.</strong> Cancel demonstrable shelfware. Right-size hyperscaler resources. Downgrade tier mismatches. Clean up obvious entitlement waste.</li><li><strong>Days 61–90 — First renegotiations.</strong> Open the top two or three vendors with the strongest gap-to-benchmark. Use the runway you bought in days 1–30 as leverage.</li></ol><p>Realistic expectation for a clean 90-day cycle on a typical mid-cap portfolio: 3–8% of annual IT spend recovered, baseline reset for the larger 10–40% over the following 12–18 months.</p>"),
        ("Building the business case for the board.",
         "<p>The mistake most CIOs make in this conversation is leading with the number. Boards have learned to discount stated savings, often by half. The conversation that lands is structural: <em>here is the gap between what we contracted and what we are paying, here is the evidence, here is the recovery path, here is the governance that prevents it from re-opening</em>. The number falls out of that.</p>"),
        ("How Aventario approaches this.",
         "<p>Our Savings-as-a-Service engagement is outcome-based: the fee is a share of realised, signed-off savings. There is no consulting day rate to argue about. We bring the benchmark base (€3B in negotiated IT contract volume), the AI contract-analysis tooling, and the negotiation team. You bring the relationships and the sign-off. The output is a portfolio that is 10–40% cheaper, on terms that don't quietly re-open the gap.</p>"),
        ("FAQ.",
         "<h3>How much can we realistically save on IT vendor spend?</h3><p>The recoverable range is 10–40% of annual contracted IT spend, depending on portfolio age, last benchmark date, and category mix. Mature, well-governed portfolios sit at the lower end; portfolios that have not been benchmarked in 24+ months sit at the upper end.</p><h3>Is this just hard-line price negotiation?</h3><p>No. Across our engagements, less than half of the recovered value comes from rate reductions. The rest comes from terms cleanup, entitlement recovery, tier rationalisation, and scope corrections. Strategic relationships are typically strengthened, not damaged.</p><h3>What is AI contract analysis?</h3><p>It's the use of large-language-model-based tooling to parse executed contracts, SOWs, and invoice data, and to flag clauses, pricing terms, and consumption patterns against a benchmark library. Aventario uses this to triage portfolios at scale rather than line-by-line.</p>"),
    ],
    expert=("Margit Györfi", "CPO"),
    quote_text="When we benchmark a vendor portfolio that hasn't been touched in three years, the question is never whether there's overpayment — it's whether it's 12% or 35%.",
    quote_attrib="Margit Györfi, CPO, Aventario",
    related=[("it-vendor-management", "The complete guide to IT vendor management"),
             ("it-contract-management", "From signature to savings: a practical guide"),
             ("it-rfp-guide", "How to run complex IT tenders that actually work")],
))

# ============ PILLAR 3: RFx ============
PILLARS.append(dict(
    slug="it-rfp-guide",
    title="IT RFP & RFx Guide (2026)",
    og_title="How to Run Complex IT Tenders That Actually Work",
    description="The structural reason most IT tenders fail — and the methodology (Zero Vendor Deviation™) that compresses a 4–6 month process into 6–8 weeks while improving the comparability of the responses.",
    schema_headline="IT RFP & RFI Guide: How to Run Complex IT Tenders That Actually Work",
    schema_mentions='{"@type": "Person", "name": "Markus Kern", "jobTitle": "CEO", "worksFor": {"@type": "Organization", "name": "Aventario"}}',
    gradient=GRADIENTS["p3"],
    topic="RFx",
    h1="The IT RFP guide.",
    tagline="How to run a complex IT tender in 6–8 weeks instead of 4–6 months — and why it's structure, not speed, that gets you there.",
    read_time="15 min read",
    cta_title="Run your next RFP with Zero Vendor Deviation™.",
    cta_body="500+ tenders run, six- to eight-week cadence, comparable responses, defensible award. Outcome-based engagement.",
    body_sections=[
        ("Quick answer.",
         "<p>An IT RFP runs in 6–8 weeks when the structural work is done before vendors see the question. It runs in 4–6 months when it isn't. The difference is not effort, talent, or vendor cooperation — it is whether the question itself was built to be answered comparably.</p>"),
        ("Why most IT tenders fail before they begin.",
         "<p>The default failure mode of an IT RFP is not that the wrong vendor wins. It is that, by the time the responses come back, no one can confidently say which vendor would have been the right one. Apples-to-oranges responses. Open-ended assumption blocks. Pricing that depends on volumes the buyer hasn't specified. Scope variations that make the spreadsheet useless.</p><p>The root cause is almost always upstream: the requirements document gave each vendor too much room to tell their own story instead of answering the same question. Vendors are good at this — it's their primary defence against being commoditised. If you don't close that room down deliberately, you give it away.</p>"),
        ("The taxonomy: RFI vs RFP vs RFQ.",
         "<p>Three documents, three different jobs. They are routinely used interchangeably, which is why they routinely produce sub-optimal results.</p><ul><li><strong>RFI — Request for Information.</strong> Used to map the market. The output is a shortlist and a refined understanding of what's available. No commercial commitment on either side.</li><li><strong>RFP — Request for Proposal.</strong> Used to compare structured proposals against a defined requirement set. The output is a ranked award decision. Pricing is a component, not the primary axis.</li><li><strong>RFQ — Request for Quotation.</strong> Used when the requirement is fully specified and price is the discriminator. Common for commodity hardware, less common for complex services.</li></ul><p>Most IT tenders are RFPs that have been mis-named, run as RFQs, or expected to do the work of an RFI. Naming the document correctly — and writing it accordingly — is the first cheap win.</p>"),
        ("Zero Vendor Deviation™: the methodology.",
         "<p>Aventario's proprietary methodology for complex IT tenders is built around a single principle: <strong>vendors cannot deviate from the structure of the question.</strong> Every requirement is atomic, weighted, and answerable in a fixed format. Every pricing line is broken down to a unit that is consumable in the same way across vendors. Every assumption is either pre-stated by the buyer or required to be explicit and individually priced.</p><p>The mechanics:</p><ul><li><strong>Atomised requirements.</strong> 300–600 individually-numbered, individually-weighted line items per RFP, each answerable in a constrained format (compliant / partial / non-compliant + evidence).</li><li><strong>Pricing skeleton.</strong> A pre-built pricing matrix the vendor fills in. Same units, same volume bands, same indexation, same currency. No free-form quotes.</li><li><strong>Assumption register.</strong> Buyer-stated assumptions are baked into the requirements; vendor-stated assumptions must be priced separately and ranked.</li><li><strong>Evaluation rubric, published.</strong> Vendors see the weighting before they respond. Surprises are eliminated; debates collapse.</li></ul><p>The result is responses that compare line-for-line. Evaluation that takes hours instead of weeks. Award decisions that survive board scrutiny because the methodology, not just the conclusion, is documented.</p>"),
        ("The 6–8 week timeline, broken down.",
         "<ol><li><strong>Week 1 — Requirements engineering.</strong> The hard, upstream work. Strategy, scope, weighting, evaluation rubric.</li><li><strong>Weeks 2–3 — Document build.</strong> Atomised requirements, pricing skeleton, assumption register, vendor question protocol.</li><li><strong>Week 4 — Issue and clarification.</strong> RFP goes to longlist. Single Q&A window, all questions and answers shared with all bidders.</li><li><strong>Weeks 5–6 — Vendor response window.</strong> Two weeks if the document is good; the structure does the work.</li><li><strong>Week 7 — Evaluation and shortlist.</strong> Compliance scoring against the rubric. Quantitative gap to qualitative discussion.</li><li><strong>Week 8 — Final round and award.</strong> Best-and-final, contract negotiation kick-off, award documented.</li></ol><p>This is the median cadence across our last 50 IT outsourcing tenders. Outliers exist — regulated procurements with statutory windows are longer; commodity refreshes are shorter — but the architecture is consistent.</p>"),
        ("Where most tenders quietly burn time.",
         "<ul><li><strong>Requirements drift.</strong> The team keeps refining requirements after the document is issued. Every refinement triggers a vendor clarification cycle. Discipline: freeze the document at issue.</li><li><strong>Q&A flood.</strong> 200+ vendor questions, most of which reveal a defect in the document. Discipline: aggregate, answer once, share with all bidders.</li><li><strong>Scope creep mid-flight.</strong> A new stakeholder asks for something to be added in week 5. Discipline: park it; address in contract negotiation, not the RFP.</li><li><strong>Comparison-by-narrative.</strong> Evaluation panel argues over which vendor's slide deck was more impressive. Discipline: rubric first; narrative second; evidence always.</li></ul>"),
        ("Common-mode failure: the requirement nobody owns.",
         "<p>Every long IT tender contains at least one requirement that no internal stakeholder fully owns. It is in the document because it sounded important; it is unweighted because nobody can defend a weight; it produces vendor responses that nobody can score because there is no acceptance criterion. Hunt for these in week 1. Either someone owns it (and weights it) or it comes out.</p>"),
        ("How Aventario approaches this.",
         "<p>Our Complex RFx-as-a-Service engagement runs the full cycle. Requirements engineering, document build, vendor management, evaluation, contract negotiation. We bring the methodology, the templates, and the negotiation muscle; you keep the relationships and the sign-off. The promise: zero vendor deviation in the responses, six- to eight-week cadence, defensible award.</p>"),
        ("FAQ.",
         "<h3>What is the difference between RFI and RFP?</h3><p>An RFI maps the market — vendors describe their capability without commitment. An RFP asks vendors to bid against a defined requirement set with structured pricing. RFI output is a shortlist; RFP output is an award decision.</p><h3>How long should an IT RFP take?</h3><p>For a complex IT outsourcing or platform tender, 6–8 weeks is achievable when requirements engineering is done properly upstream. Tenders that take 4–6 months are typically suffering from requirements drift, scope ambiguity, or vendor-deviation in the responses.</p><h3>What is Zero Vendor Deviation?</h3><p>It is Aventario's RFP methodology. Atomised requirements, structured pricing skeleton, published evaluation rubric — built so vendors cannot deviate from the structure of the question. The result is line-for-line comparable responses.</p>"),
    ],
    expert=("Markus Kern", "CEO"),
    quote_text="If your evaluation panel is arguing about which slide deck was more compelling, the RFP failed before the responses came in.",
    quote_attrib="Markus Kern, CEO, Aventario",
    related=[("it-vendor-management", "The complete guide to IT vendor management"),
             ("it-contract-management", "From signature to savings"),
             ("it-vendor-consolidation", "From 47 vendors to 5 strategic partners")],
))

# ============ PILLAR 4: CONSOLIDATION ============
PILLARS.append(dict(
    slug="it-vendor-consolidation",
    title="IT Vendor Consolidation: From 47 to 5 (2026)",
    og_title="From 47 IT Vendors to 5 Strategic Partners",
    description="A structural guide to IT vendor consolidation: why sprawl happens, how to rationalise without breaking delivery, and what good looks like when 80% of services run through five strategic partners.",
    schema_headline="IT Vendor Consolidation: How to Go from 47 Vendors to 5 Strategic Partners",
    schema_mentions='{"@type": "Person", "name": "Markus Jaksch", "jobTitle": "COO", "worksFor": {"@type": "Organization", "name": "Aventario"}}',
    gradient=GRADIENTS["p4"],
    topic="Consolidation",
    h1="From 47 vendors to 5 strategic partners.",
    tagline="Vendor sprawl is rarely a procurement problem. It's the residue of many reasonable decisions made without a global view. Putting that view back is the engagement.",
    read_time="12 min read",
    cta_title="Rationalise your vendor portfolio.",
    cta_body="We've taken portfolios from 80+ active suppliers to top-5 dominance without breaking delivery. The methodology is repeatable.",
    body_sections=[
        ("Quick answer.",
         "<p>IT vendor consolidation is the deliberate reduction of an organisation's active supplier portfolio toward a smaller number of strategic partners — typically with the goal of routing 70–85% of in-scope IT services through five primary vendors. Done well, it lowers cost, improves leverage, simplifies governance, and reduces the operational tax of managing a long tail. Done badly, it concentrates risk, breaks delivery, and creates the next migration project before the previous one has stabilised.</p>"),
        ("Why the long tail exists in the first place.",
         "<p>Vendor sprawl is not a procurement failure. It is the residue of many reasonable local decisions, made by competent people, in the absence of a global view. A team needs a niche capability for a project; nobody at the time would have argued for going through a strategic partner instead. Three years later, that vendor is on the books, the project is gone, and nobody remembers why the contract auto-renews.</p><p>Multiply by ten years and three reorganisations and you have the average DACH mid-cap IT vendor portfolio: 80 to 220 active suppliers, 60–70% of spend concentrated in the top ten, and a long tail of 50–150 vendors collectively consuming 15–25% of spend and roughly the same proportion of vendor management bandwidth.</p>"),
        ("What consolidation actually delivers.",
         "<ul><li><strong>Cost.</strong> 10–25% category savings from concentrated volume, fewer overhead-heavy small contracts, and simpler benchmark refreshes.</li><li><strong>Leverage.</strong> Strategic partners take a relationship more seriously when they see a credible path to growth — and when the relationship can be lost.</li><li><strong>Governance.</strong> Five Tier-3 governance forums per year is achievable. Forty-seven is theatre.</li><li><strong>Innovation.</strong> Partners with skin in the game commit roadmap energy. Transactional vendors do not.</li><li><strong>Delivery resilience.</strong> Fewer vendors, deeper integration, clearer accountability when something breaks at 03:00.</li></ul>"),
        ("The risks consolidation introduces.",
         "<p>Concentration is not free. Done thoughtlessly, it creates new exposure:</p><ul><li><strong>Concentration risk.</strong> One vendor holding 30% of in-scope services is a single point of failure unless contractually mitigated.</li><li><strong>Reduced market awareness.</strong> Fewer relationships in the portfolio means weaker signal on what the rest of the market is doing.</li><li><strong>Lock-in.</strong> Strategic partners are harder to replace; the exit clauses matter more than they used to.</li><li><strong>Innovation monoculture.</strong> If all your innovation comes from the same five vendors, your roadmap looks like theirs.</li></ul><p>Each of these is manageable through contract design and Tier-3 governance. None of them is a reason not to consolidate; all of them are reasons to design the consolidation deliberately rather than letting it happen by attrition.</p>"),
        ("Segmenting the portfolio: the Kraljic Matrix, applied to IT.",
         "<p>The standard procurement segmentation tool maps vendors on two axes: supply risk (how hard would they be to replace) and profit impact (how much do they cost / how much do they enable). Four quadrants, four governance approaches:</p><ul><li><strong>Strategic (high risk, high impact).</strong> The five-or-so partners. Multi-year, deeply governed, jointly planned. This is where consolidation lands.</li><li><strong>Leverage (low risk, high impact).</strong> Commodity-ish, lots of substitutes, big spend. Rotate aggressively. Benchmark constantly.</li><li><strong>Bottleneck (high risk, low impact).</strong> Niche, hard to replace, not strategically important. Risk-mitigate via contracts; don't waste relationship energy.</li><li><strong>Routine (low risk, low impact).</strong> The long tail. Consolidate ruthlessly through procurement aggregators or strategic partners.</li></ul><p>The map is the first deliverable of any consolidation engagement. Without it, the conversation about which vendors stay is anecdote-driven.</p>"),
        ("ITSM data: where the truth lives.",
         "<p>Procurement records tell you who has a contract. ITSM data — tickets, incidents, change records, asset records — tells you who actually does the work. The two are surprisingly different. We routinely find vendors who appear in 4% of tickets and 12% of contracted spend, and other vendors with the inverse. Cross-referencing the two is the single most informative step in a consolidation diagnostic.</p>"),
        ("The transition risk nobody plans for.",
         "<p>Most consolidation programmes underestimate transition. Moving services from a long-tail vendor to a strategic partner is not a paperwork exercise — there is documentation that doesn't exist, knowledge in heads that won't be written down, integrations that nobody fully owns. The day the outgoing vendor is told their contract isn't renewing, their motivation to support the transition drops to roughly zero.</p><p>Plan accordingly. Knowledge capture before the notice goes out, not after. Transition windows of 90–180 days, not 30. Reverse-transition rights in the new contract, in case the consolidated solution doesn't take.</p>"),
        ("The 5-vendor strategic architecture.",
         "<p>The target state most consolidation programmes converge toward is a five-vendor strategic architecture covering: (1) the primary infrastructure / hyperscaler partner, (2) the primary application development and run partner, (3) the primary end-user computing partner, (4) the primary network / connectivity partner, (5) a strategic specialist for whatever the organisation's distinctive technology axis happens to be. Sectoral variants exist — pharma adds GxP; financial services adds a regulated-platform vendor — but the architecture is recognisably similar across mid-caps.</p>"),
        ("How Aventario approaches this.",
         "<p>Our Service & Vendor Consolidation engagement starts with the diagnostic — Kraljic mapping, ITSM cross-reference, contract triage, transition risk assessment — and ends with the executed migrations. We bring the methodology, the transition playbook, and the contract design for the new strategic partnerships. The benchmark target is &gt;80% of in-scope services through the top five vendors within 18–24 months, with no service breakage during transition.</p>"),
        ("FAQ.",
         "<h3>What is IT vendor consolidation?</h3><p>The deliberate reduction of an active IT supplier portfolio toward a smaller number of strategic partners, typically with the goal of routing the majority of in-scope services through a top-5 set.</p><h3>How much can vendor consolidation save?</h3><p>10–25% of category spend is the typical observed range, plus indirect savings from reduced governance overhead and better-leveraged renegotiations. The variance depends on portfolio fragmentation at baseline.</p><h3>What is the biggest risk in consolidation?</h3><p>Transition risk — the period between notice-given to the outgoing vendor and full handover to the new partner. Most programmes underestimate the time, the knowledge gap, and the drop in cooperation from the outgoing provider.</p>"),
    ],
    expert=("Markus Jaksch", "COO"),
    quote_text="The day the outgoing vendor is told their contract isn't renewing, their motivation to support the transition drops to roughly zero. Plan as if that's true, because it is.",
    quote_attrib="Markus Jaksch, COO, Aventario",
    related=[("it-vendor-management", "The complete guide to IT vendor management"),
             ("it-vendor-spend-optimization", "How to recover 10–40% of your IT budget"),
             ("it-rfp-guide", "How to run complex IT tenders that actually work")],
))

# ============ PILLAR 5: CONTRACT MANAGEMENT ============
PILLARS.append(dict(
    slug="it-contract-management",
    title="IT Contract Management (2026)",
    og_title="IT Contract Management: From Signature to Savings",
    description="A practical guide to managing IT contracts across the full lifecycle. Renewal traps, audit clauses, AI-assisted analysis, and the mechanics of converting contractual rights into realised savings.",
    schema_headline="IT Contract Management: From Signature to Savings — A Practical Guide",
    schema_mentions='{"@type": "Person", "name": "Margit Györfi", "jobTitle": "CPO", "worksFor": {"@type": "Organization", "name": "Aventario"}}',
    gradient=GRADIENTS["p5"],
    topic="Contracts",
    h1="IT contract management.",
    tagline="Signature is the start of the work, not the end. A practical guide to converting contractual rights into actual savings.",
    read_time="12 min read",
    cta_title="Audit your top contracts.",
    cta_body="AI-assisted contract analysis across your portfolio. We surface the clauses, entitlements, and renegotiation triggers your team doesn't have time to read.",
    body_sections=[
        ("Quick answer.",
         "<p>IT contract management is the discipline of actively governing every IT vendor contract from signature through exit — tracking obligations, surfacing renewal triggers, validating consumption, and converting contractual rights (audit, benchmark, change-request, termination-for-convenience) into realised P&amp;L impact. Most organisations have a contract repository. Very few have contract <em>management</em>.</p>"),
        ("The 7-stage IT contract lifecycle.",
         "<ol><li><strong>Pre-signature drafting.</strong> Defining what the contract needs to do — mostly governed by the RFP and the negotiation that follows.</li><li><strong>Execution.</strong> Signature, redlines closed, vendor onboarded.</li><li><strong>Mobilisation.</strong> The first 90 days. SLA baseline established, governance forums set up, change-request mechanics tested.</li><li><strong>Steady-state operation.</strong> Day-to-day delivery. Most contracts spend most of their life here.</li><li><strong>Mid-life intervention.</strong> Annual benchmark, scope change, indexation review. The cheapest moment to fix a contract that is drifting.</li><li><strong>Renewal trigger window.</strong> 9–12 months before contract end. The decision point that determines whether you stay, leave, or renegotiate.</li><li><strong>Renewal or exit.</strong> The transition into the next contract or out of the relationship.</li></ol><p>Each stage has its own owner and artefact. The stages most often skipped are 5 and 6 — and they are the stages where the recoverable money lives.</p>"),
        ("Renewal traps: the eight clauses to audit before every renewal.",
         "<p>Twelve months before contract end, a senior reviewer should put the executed contract on the table and walk through eight specific clause families. Each is a known trap.</p><ul><li><strong>Auto-renewal mechanics.</strong> Notice period, format, recipient, escalation. Miss any of these and the contract rolls forward at the original terms.</li><li><strong>Indexation.</strong> CPI-linked? Capped? Bidirectional? Most contracts only adjust upward.</li><li><strong>Volume bands.</strong> Tiered pricing that may have stopped reflecting consumption.</li><li><strong>Service credit recovery.</strong> SLA misses that should have generated credits — and didn't, because nobody enforced.</li><li><strong>Benchmark clauses.</strong> Right to benchmark every 18–24 months and force a price adjustment if outside market.</li><li><strong>Termination for convenience.</strong> Available? Notice period? Wind-down obligations?</li><li><strong>Audit rights.</strong> Right to inspect vendor delivery records, consumption, security posture. Almost never exercised.</li><li><strong>Change-request mechanics.</strong> What triggers a CR, who approves, what is the pricing methodology.</li></ul>"),
        ("AI contract analysis: what it is and what it finds.",
         "<p>Modern LLM-based contract analysis tooling can ingest an executed contract, the SOW, the latest invoice run, and the SLA report set, and produce a clause-by-clause gap analysis against a benchmark library. Aventario's pipeline runs this across a portfolio in days rather than the weeks a manual review would take.</p><p>Typical findings on first pass across an unmanaged mid-cap portfolio: 15–25% of contracts within 90 days of an unread auto-renewal, 30–50% of contracts with stale benchmark rights, 20% with service-credit balances that have never been claimed, and a small but reliable number of contracts whose paper terms differ materially from what is actually being invoiced.</p>"),
        ("SLA, OLA, KPI: the definitions that matter.",
         "<ul><li><strong>SLA — Service Level Agreement.</strong> The contractually committed performance threshold between buyer and vendor. Breaching it has financial or service-credit consequences.</li><li><strong>OLA — Operational Level Agreement.</strong> The internal commitments between teams or sub-suppliers that <em>underpin</em> the SLA. If the OLA is weaker than the SLA, the SLA will fail.</li><li><strong>KPI — Key Performance Indicator.</strong> The metric used to measure whether the SLA is being met. The choice of KPI is often where the loophole hides.</li></ul><p>Most SLA disputes are not about the threshold; they are about which KPI is being used to measure it. The contract should be unambiguous on both.</p>"),
        ("How to audit an IT vendor contract: the 5-step procedure.",
         "<ol><li><strong>Reconstruct.</strong> Pull the executed contract, all amendments, all CRs, the current SOW. Confirm the chain is complete.</li><li><strong>Reconcile.</strong> Compare the contracted scope against actual invoiced consumption for the last 12 months. Flag deltas.</li><li><strong>Validate.</strong> Cross-check vendor SLA reports against ticket-level data. Flag green reports that don't survive ticket-level scrutiny.</li><li><strong>Benchmark.</strong> Take material line items to the benchmark base. Quantify gap to market.</li><li><strong>Decide.</strong> Continue, renegotiate mid-flight, prepare for non-renewal, or exit early. Document the decision and the supporting evidence.</li></ol>"),
        ("The exit clause trap.",
         "<p>Most IT contracts have weak exit clauses because the buyer was focused on getting in, not on getting out. Consequences only become visible at the renewal point, when the buyer's leverage in negotiation is fundamentally constrained by how expensive it would be to leave. Strong exit clauses — termination for convenience, knowledge-transfer obligations, data-extraction rights, transition-assistance pricing — are the foundation of every subsequent renegotiation. Build them in at signature; you cannot retrofit them later.</p>"),
        ("How Aventario approaches this.",
         "<p>Our contract analysis pipeline runs across the full portfolio. Renewal calendar, clause inventory, consumption reconciliation, benchmark gap, decision log. The output is a prioritised action queue: which contracts to leave alone, which to renegotiate mid-flight, and which to prepare for non-renewal. We can run this as a one-off diagnostic or as a continuous service inside a Vendor Management-as-a-Service engagement.</p>"),
        ("FAQ.",
         "<h3>What is IT contract management?</h3><p>The active governance of IT vendor contracts across the full lifecycle from signature through exit, including obligation tracking, renewal management, consumption validation, and renegotiation.</p><h3>What is the difference between SLA and OLA?</h3><p>An SLA is the external, contractual commitment between buyer and vendor. An OLA is the internal commitment between teams or sub-suppliers that underpins the SLA. The OLA is invisible to the buyer but determines whether the SLA can be met.</p><h3>How often should IT contracts be audited?</h3><p>Material strategic contracts: annually. Mid-tier contracts: at the 50% mark of their term. All contracts: at least 9–12 months before renewal trigger.</p>"),
    ],
    expert=("Margit Györfi", "CPO"),
    quote_text="The contract is the cheapest moment to win the next negotiation. Most teams treat it as the moment to stop reading.",
    quote_attrib="Margit Györfi, CPO, Aventario",
    related=[("it-vendor-management", "The complete guide to IT vendor management"),
             ("it-vendor-spend-optimization", "How to recover 10–40% of your IT budget"),
             ("it-vendor-governance", "The framework that keeps vendors accountable")],
))

# ============ PILLAR 6: SRM ============
PILLARS.append(dict(
    slug="supplier-relationship-management",
    title="Supplier Relationship Management — SRM (2026)",
    og_title="SRM: The CRM You Don't Have for Your Vendors",
    description="Why every enterprise has a CRM for customers but almost none have a real SRM for suppliers — and what changes when supplier relationships are managed with the same discipline as customer relationships.",
    schema_headline="Supplier Relationship Management (SRM): The CRM You Don't Have for Your Vendors",
    schema_mentions='{"@type": "Person", "name": "Markus Kern", "jobTitle": "CEO", "worksFor": {"@type": "Organization", "name": "Aventario"}}',
    gradient=GRADIENTS["p6"],
    topic="SRM",
    h1="Supplier Relationship Management.",
    tagline="The CRM you don't have for your vendors. Why one side of the relationship is instrumented and the other still runs on spreadsheets.",
    read_time="11 min read",
    cta_title="Build a real SRM capability.",
    cta_body="Process first, platform second. We design the SRM operating model and implement it on managedsuppliers — our own SaaS, or a tool you already own.",
    body_sections=[
        ("Quick answer.",
         "<p>Supplier Relationship Management (SRM) is the structured practice of managing the buyer side of every external supplier relationship — segmentation, performance, governance, risk, knowledge — with the same discipline that customer relationships have been managed with for thirty years through CRM. Most enterprises have invested heavily in CRM. Almost none have a real SRM capability.</p>"),
        ("SRM vs CRM: the asymmetry.",
         "<p>Pick any DACH mid-cap. Ask how customers are managed. You'll get an answer involving Salesforce, Dynamics, or HubSpot — pipelines, segmentation, contact history, scorecards, NPS, churn risk, every interaction logged. Ask how the same organisation manages its supplier base. You'll get a contract repository, a finance ERP module, a SharePoint folder of QBR slides, and several spreadsheets.</p><p>Both sides of the business carry similar economic weight: a typical mid-cap spends roughly as much on suppliers as it earns from any single major customer segment. Both sides involve relationships that decay without active management. Only one of them has the toolchain.</p>"),
        ("The SRM maturity model: 5 levels.",
         "<ol><li><strong>Reactive.</strong> Suppliers managed transactionally, contract by contract. No portfolio view.</li><li><strong>Recorded.</strong> Central repository exists. Contracts findable, but performance not tracked systematically.</li><li><strong>Measured.</strong> Scorecards in place for tier-1 vendors. Periodic governance forums.</li><li><strong>Managed.</strong> Full segmentation, structured QBRs, risk register, knowledge captured centrally.</li><li><strong>Strategic.</strong> Suppliers as innovation partners, joint roadmap planning, executive sponsorship matched to strategic value.</li></ol><p>Most mid-caps live somewhere between Levels 1 and 2 across the long tail, and Levels 2–3 for the top ten vendors. Level 4–5 is where SRM stops being administrative overhead and starts producing actual leverage.</p>"),
        ("Supplier segmentation: the foundation.",
         "<p>SRM that treats every supplier the same is just admin. The first design decision is segmentation. The default approach is the Kraljic matrix (supply risk × profit impact), which produces four governance approaches: strategic, leverage, bottleneck, routine. Each segment has a different cadence, different governance forum, different scorecard, different relationship investment.</p><p>The mistake is over-investing in routine vendors and under-investing in strategic ones. The relationship-management calorie budget is finite. Spend it where the value is.</p>"),
        ("The supplier scorecard: what to measure.",
         "<ul><li><strong>Delivery.</strong> SLA performance, ticket-level reality vs reported performance, on-time delivery, defect rate.</li><li><strong>Commercial.</strong> Spend trend, savings vs benchmark, contract compliance, billing accuracy.</li><li><strong>Risk.</strong> Financial health, security posture, regulatory exposure, key-person dependency.</li><li><strong>Relationship.</strong> Responsiveness, escalation history, governance attendance, knowledge transfer.</li><li><strong>Innovation.</strong> Roadmap contribution, new capability brought to the relationship.</li></ul><p>Five dimensions, weighted by segment. Strategic vendors get all five. Routine vendors get two. The point is to make the scorecard visible to both sides — vendors who know how they're scored manage their behaviour accordingly.</p>"),
        ("The knowledge-loss problem.",
         "<p>The single most under-discussed risk in vendor management is knowledge concentration in individuals. The senior vendor manager who has run the relationship for seven years carries an enormous amount of context that is nowhere written down — who at the vendor will actually return a call, what the unwritten escalation path looks like, which clauses were negotiated hard and which were given away. When that person leaves, the relationship resets to zero. A real SRM capability captures this knowledge in the system, not in heads.</p>"),
        ("From Excel to SRM platform: the transition.",
         "<p>Most organisations start the SRM journey on Excel. Spreadsheets capture the contract log, the renewal calendar, the QBR cadence, the scorecard. They work — until they don't. The transition signal is usually one of three: the spreadsheet is too big to maintain, two people maintain conflicting versions, or the answer to a basic question (\"what is our total spend on this vendor?\") takes more than five minutes.</p><p>The transition is process-first, platform-second. The SRM operating model — segmentation, governance cadence, scorecard, knowledge capture, risk register — is what's being implemented; the platform is where it runs. Doing the platform first reliably produces an expensive system that automates yesterday's bad process.</p>"),
        ("AI-powered supplier management: what's actually changing.",
         "<p>The interesting LLM applications in SRM are not chatbot QBRs. They are: contract clause extraction at portfolio scale; SLA reconciliation against ticket data; risk-signal monitoring across financial and security feeds; meeting-summary capture into the scorecard; benchmark gap-analysis at the line-item level. Aventario's managedsuppliers platform implements these as native capabilities; other tools are catching up.</p>"),
        ("How Aventario approaches this.",
         "<p>We design the SRM operating model first — segmentation, cadence, scorecard, governance, knowledge capture. We then implement it on managedsuppliers (our SaaS) for clients who want a purpose-built tool, or on the platform the client already owns. The deliverable is a working SRM capability, not a deck about one.</p>"),
        ("FAQ.",
         "<h3>What is SRM?</h3><p>Supplier Relationship Management — the structured discipline of managing the buyer side of supplier relationships across segmentation, performance, governance, risk, and knowledge.</p><h3>How is SRM different from CRM?</h3><p>CRM manages customer relationships; SRM manages supplier relationships. The mechanics are mirror images, but most organisations have invested heavily in CRM and minimally in SRM.</p><h3>Do we need an SRM platform?</h3><p>Not at every maturity level. Levels 1–3 can run on Excel + a contract repository. From Level 4 upward, the volume and integration requirements typically justify a purpose-built platform.</p>"),
    ],
    expert=("Markus Kern", "CEO"),
    quote_text="What CRM did for sales over the last thirty years, SRM is going to do for procurement over the next ten. The difference is that procurement can't wait that long.",
    quote_attrib="Markus Kern, CEO, Aventario",
    related=[("vendor-management-software", "How to choose the right vendor management platform"),
             ("it-vendor-management", "The complete guide to IT vendor management"),
             ("it-vendor-governance", "The governance framework that keeps vendors accountable")],
))

# ============ PILLAR 7: OPERATIONAL EXCELLENCE ============
PILLARS.append(dict(
    slug="it-operational-excellence",
    title="IT Operational Excellence (2026)",
    og_title="Find and Eliminate the 20% Your Processes Waste",
    description="A pragmatic guide to IT operational excellence: assessing the landscape, finding process waste, building automation business cases, and rationalising the application portfolio.",
    schema_headline="IT Operational Excellence: How to Find and Eliminate the 20% Your Processes Waste",
    schema_mentions='{"@type": "Person", "name": "Margit Györfi", "jobTitle": "CPO", "worksFor": {"@type": "Organization", "name": "Aventario"}}',
    gradient=GRADIENTS["p7"],
    topic="Operations",
    h1="IT operational excellence.",
    tagline="Most IT organisations carry 15–25% of process work that adds no measurable value. Finding it is the engagement; the elimination follows.",
    read_time="12 min read",
    cta_title="Find your hidden 20%.",
    cta_body="Landscape assessment, process mining, automation readiness, application rationalisation. ≥20% efficiency gain target — measured, not promised.",
    body_sections=[
        ("Quick answer.",
         "<p>IT operational excellence is the disciplined removal of work that doesn't produce value — duplicate processes, oversized application portfolios, low-impact automation, manual reconciliation between systems that should be integrated. Across the engagements we've run, the typical recoverable inefficiency in a mid-cap IT operation sits between 15% and 25% of total run cost.</p>"),
        ("Why most CIOs misdiagnose this.",
         "<p>The default approach to IT efficiency is one of two postures: cost-out (a top-down percentage cut applied uniformly) or transformation (a multi-year programme led by a brand-name systems integrator). Both approaches share a flaw: they begin with the answer and work backward to the problem. Cost-out picks numbers before the analysis. Transformation picks technology before the diagnosis.</p><p>Operational excellence runs the other direction. The diagnosis comes first; the action falls out of it. The diagnosis is unglamorous — process mining, ticket-data analysis, application-portfolio inventory — but it is where the recoverable money is actually visible.</p>"),
        ("The IT landscape assessment: a step-by-step.",
         "<ol><li><strong>Application inventory.</strong> Pull every active application, system, and platform. Owner, business purpose, run cost, user count, integration footprint. Expect to find 15–30% more applications than the CIO expected.</li><li><strong>Process mapping.</strong> The top 20 IT-touching business processes (incident, change, fulfilment, onboarding, offboarding, etc.). End-to-end, not within-team.</li><li><strong>Cost allocation.</strong> Run cost by application, by process, by team. Most organisations cannot answer this within 20% accuracy at first attempt.</li><li><strong>Pain-point inventory.</strong> Where does work get stuck, redone, escalated. Talk to the people doing the work; the executive view is consistently wrong about this.</li><li><strong>Synthesis.</strong> A heat map: high-cost / high-pain / low-value combinations are the action queue.</li></ol>"),
        ("Process mining: what it is, what it finds.",
         "<p>Process mining is the practice of reconstructing actual process behaviour from system event logs, rather than from how someone says the process works. The two are reliably different. A process documented as a five-step incident-management workflow turns out, in the event log, to involve 23 distinct paths, of which the documented one accounts for 38% of cases. The other 62% is the work to investigate.</p><p>The typical finding: 10–20% of process volume runs through paths that, on inspection, add no value — duplicate approvals, unnecessary handovers, manual rekeying between systems, exception handling for cases the process should have handled automatically.</p>"),
        ("Shadow IT: the hidden iceberg.",
         "<p>Every CIO underestimates shadow IT. The official application inventory shows 180 applications; the SaaS-management tool, when deployed, finds another 60–90. Each of those is paid by someone, used by someone, integrated with something — and none of it is governed. The first job is visibility. The second is triage: which shadow systems are filling a real need (and should be brought into the official portfolio) and which are duplication (and should be sunset).</p>"),
        ("Application portfolio rationalisation: the four-quadrant decision.",
         "<ul><li><strong>Keep.</strong> The application is fit-for-purpose, well-used, well-integrated, low-risk. Most of these are the obvious cases.</li><li><strong>Kill.</strong> No longer used at the volume that justifies the run cost. Migrate users to existing alternatives; decommission.</li><li><strong>Migrate.</strong> Used, but on an end-of-life platform or with overlapping functionality elsewhere in the portfolio.</li><li><strong>Modernise.</strong> Strategic, used, but the implementation is dated and the run cost has crept up. Replatform.</li></ul><p>The decision rule we use: any application that scores low on usage and high on run cost is in the kill quadrant by default. The burden of proof is on keeping it, not on removing it.</p>"),
        ("Automation readiness: what to automate, what to leave.",
         "<p>The default automation backlog in most IT organisations is too long and badly prioritised. The screening question is not <em>can this be automated</em>; nearly everything can. The question is <em>does the business case survive contact with the implementation cost</em>. The criteria that matter:</p><ul><li><strong>Volume.</strong> The process runs often enough that automation pays back inside 12–18 months.</li><li><strong>Stability.</strong> The process is not going to change shape inside the next 24 months.</li><li><strong>Standardisation.</strong> The process variants are bounded; the automation doesn't need to handle 47 edge cases.</li><li><strong>Data integrity.</strong> The systems involved expose stable APIs, not screen-scraping.</li></ul><p>An automation candidate that fails any one of these is usually not worth doing — even though it could be done.</p>"),
        ("The digitisation business case the board approves.",
         "<p>Boards have learned to discount IT business cases. The cases that survive scrutiny share three properties: a baseline measured rigorously rather than estimated, a recovery path with proof points at 90, 180, and 365 days, and a governance commitment that the savings will be tracked into the operating budget rather than reinvested invisibly. The third is the one most often missing.</p>"),
        ("How Aventario approaches this.",
         "<p>Our Operational Excellence engagement runs the diagnostic — landscape, process mining, ticket analysis, portfolio rationalisation — and stays through the elimination. The benchmark target is ≥20% efficiency gain, measured against a baseline we establish before any change is made. Outcome-based engagement; the fee is tied to realised, signed-off improvement.</p>"),
        ("FAQ.",
         "<h3>What is IT operational excellence?</h3><p>The disciplined removal of work that doesn't produce value across the IT operation — duplicate processes, oversized application portfolios, manual reconciliation, low-impact automation candidates.</p><h3>How much is realistically recoverable?</h3><p>15–25% of total run cost across the engagements we've measured, with a 6–18 month realisation window depending on portfolio complexity.</p><h3>What is process mining?</h3><p>The reconstruction of actual process behaviour from system event logs, rather than from documented process maps. It typically reveals significant divergence between the two.</p>"),
    ],
    expert=("Margit Györfi", "CPO"),
    quote_text="The documented process and the actual process are reliably different. The work isn't in writing better documents — it's in fixing the actual.",
    quote_attrib="Margit Györfi, CPO, Aventario",
    related=[("it-vendor-management", "The complete guide to IT vendor management"),
             ("digital-transformation-sourcing", "Digital transformation without vendor chaos"),
             ("it-vendor-spend-optimization", "How to recover 10–40% of your IT budget")],
))

# ============ PILLAR 8: GOVERNANCE ============
PILLARS.append(dict(
    slug="it-vendor-governance",
    title="IT Vendor Governance Framework (2026)",
    og_title="Keep Vendors Accountable After the Contract Is Signed",
    description="A practical framework for IT vendor governance — three-tier model, escalation discipline, SLA verification, the 18-month decay curve, and how to keep vendors accountable after the contract is signed.",
    schema_headline="IT Vendor Governance: The Framework That Keeps Vendors Accountable After the Contract Is Signed",
    schema_mentions='{"@type": "Person", "name": "Markus Jaksch", "jobTitle": "COO", "worksFor": {"@type": "Organization", "name": "Aventario"}}',
    gradient=GRADIENTS["p8"],
    topic="Governance",
    h1="IT vendor governance.",
    tagline="The framework that keeps vendors accountable after the contract is signed — and the predictable decay curve that takes over when it isn't there.",
    read_time="11 min read",
    cta_title="Stand up real governance.",
    cta_body="Three-tier model, structured QBRs, SLA verification, escalation discipline. We design it; we run it through the first cycle; we hand over the operating model.",
    body_sections=[
        ("Quick answer.",
         "<p>IT vendor governance is the structured set of forums, scorecards, escalation paths, and contractual rights that hold a vendor to the performance the contract promised. Without it, even an excellent contract under-delivers — predictably, on a curve that we observe across virtually every ungoverned engagement.</p>"),
        ("The 18-month governance decay curve.",
         "<p>In the absence of active governance, vendor performance drifts back toward the lowest-effort baseline within roughly 18 months of go-live. The curve is consistent enough across our engagement archive that we treat it as a planning assumption, not a hypothesis. Month 0–3: vendor is on best behaviour, deal is fresh, account team is attentive. Month 4–9: routine sets in, account team turns over, attention shifts to the next deal. Month 10–18: SLA reports start arriving green by default, escalations get slower, innovation commitments quietly drop. Month 18+: you are now the legacy book; the vendor's strategic energy is somewhere else.</p><p>Governance is what flattens the curve.</p>"),
        ("The Three-Tier Governance Model.",
         "<h3>Tier 1 — Operational.</h3><p>Weekly or fortnightly. Service desk leads on both sides. Tickets, incidents, SLA breaches, change requests. Concrete and small. The verification layer for SLA reports — issues that surface here either get resolved or escalate to Tier 2.</p><h3>Tier 2 — Managerial.</h3><p>Monthly. Service owners, account leads, finance representation. Scorecard, financial reconciliation, risk register, change-request pipeline. The layer where small problems get fixed before they become big ones. Most ungoverned vendor relationships skip this entirely; everything either festers in Tier 1 or jumps to Tier 3.</p><h3>Tier 3 — Strategic.</h3><p>Quarterly. CIO/sponsor on the client side; vendor executive on theirs. Roadmap, innovation, contract evolution, relationship health. The conversation that determines whether the vendor is investing in the relationship or harvesting it.</p>"),
        ("The discipline: nothing skips a tier.",
         "<p>The most common governance failure is not the absence of forums. It is the absence of discipline about which forum handles what. Operational issues end up on the CIO's desk; strategic decisions get made in the weekly stand-up; the QBR becomes a status report. The cure is mechanical: every issue gets logged at its tier; escalations are documented and time-bounded; the QBR agenda is set 10 working days in advance and contains nothing that wasn't on it.</p>"),
        ("SLA compliance monitoring: don't trust the vendor's report.",
         "<p>The single most reliable governance gap we find is unverified SLA reporting. The vendor's monthly report shows green; nobody compares it to the underlying ticket-level data. When the comparison is run, real availability is often a tier below contracted, with the gap absorbed by category definitions, exclusion clauses, and creative time-stop logic.</p><p>The fix is small but cultural: every monthly SLA report is independently reconciled against ticket data before it is accepted. The first cycle of doing this is uncomfortable; subsequent cycles produce dramatically more honest reports.</p>"),
        ("Escalation processes that actually work.",
         "<ol><li><strong>Defined trigger.</strong> What event constitutes an escalation. SLA breach by X%, P1 incident open Y hours, financial dispute over Z.</li><li><strong>Defined path.</strong> Who escalates to whom, in what order, with what evidence. No skipping.</li><li><strong>Time-bound resolution targets.</strong> Each escalation tier has its own SLA.</li><li><strong>Logged and reviewed.</strong> Every escalation generates a record that is reviewed at Tier 2 and rolls up to Tier 3 if it recurs.</li></ol><p>Escalations are not a sign of relationship failure. The absence of escalations in a relationship that is materially under-performing is the failure.</p>"),
        ("The vendor governance scorecard.",
         "<p>Five dimensions, scored monthly for tier-1 strategic vendors:</p><ul><li><strong>Delivery</strong> (SLA verified vs contracted)</li><li><strong>Commercial</strong> (spend on plan, billing accuracy, savings vs benchmark)</li><li><strong>Risk</strong> (security incidents, financial signals, key-person changes)</li><li><strong>Relationship</strong> (responsiveness, escalation history, governance attendance)</li><li><strong>Innovation</strong> (roadmap delivery, joint planning, capability brought)</li></ul><p>Weighted by segment. Visible to both sides. Reviewed at every Tier 3 forum. Vendors who know how they are scored manage their behaviour accordingly.</p>"),
        ("Governance after outsourcing: the playbook most companies ignore.",
         "<p>The single most damaging assumption in IT outsourcing is that, having transferred the work, the buyer has also transferred the governance. They haven't. Outsourcing transfers execution; governance has to be built deliberately on the buyer side, often by a function that didn't exist before the deal was signed. Without it, the value of the outsourcing decays on the same 18-month curve, only with less visibility because the buyer no longer touches the work.</p>"),
        ("How Aventario approaches this.",
         "<p>Our Vendor Management-as-a-Service engagement designs the governance model and runs it through the first one or two cycles, then hands over the operating model to the client team. The deliverable is a working three-tier governance capability, not a deck that describes one. Where the client prefers, we stay in the seat as an outsourced vendor management office.</p>"),
        ("FAQ.",
         "<h3>What is IT vendor governance?</h3><p>The structured set of forums, scorecards, escalation paths, and contractual mechanisms that hold IT vendors accountable to the performance their contracts promise.</p><h3>What is the Three-Tier Governance Model?</h3><p>Aventario's governance framework: Tier 1 (operational, weekly), Tier 2 (managerial, monthly), Tier 3 (strategic, quarterly). The discipline is that nothing skips a tier.</p><h3>Why does vendor performance decay?</h3><p>In the absence of active governance, vendor account-team attention shifts to newer deals, internal knowledge degrades, and SLA reports drift toward optimistic. The pattern is consistent enough that we treat it as a planning assumption.</p>"),
    ],
    expert=("Markus Jaksch", "COO"),
    quote_text="The absence of escalations in a relationship that is materially under-performing is not health. It's the wrong people not talking.",
    quote_attrib="Markus Jaksch, COO, Aventario",
    related=[("it-vendor-management", "The complete guide to IT vendor management"),
             ("it-contract-management", "From signature to savings"),
             ("supplier-relationship-management", "The CRM you don't have for your vendors")],
))

# ============ PILLAR 9: DIGITAL TRANSFORMATION ============
PILLARS.append(dict(
    slug="digital-transformation-sourcing",
    title="Digital Transformation Sourcing (2026)",
    og_title="Digital Transformation Without Vendor Chaos",
    description="Why digital transformation programmes stall when vendor sourcing is treated as a procurement event rather than a continuous capability — and what changes when sourcing is built into the transformation operating model.",
    schema_headline="Digital Transformation Without Vendor Chaos: The IT Leader's Sourcing Guide",
    schema_mentions='{"@type": "Person", "name": "Markus Kern", "jobTitle": "CEO", "worksFor": {"@type": "Organization", "name": "Aventario"}}',
    gradient=GRADIENTS["p9"],
    topic="Transformation",
    h1="Digital transformation without vendor chaos.",
    tagline="The IT leader's sourcing guide. Why most transformations stall in the vendor layer — and what to design instead.",
    read_time="11 min read",
    cta_title="Build sourcing into the transformation.",
    cta_body="A sourcing strategy that doesn't break under the weight of the transformation. We design it; you run it.",
    body_sections=[
        ("Quick answer.",
         "<p>Digital transformations don't typically fail in the strategy deck. They fail in the vendor layer — too many partners, unclear accountability, contracts written for a delivery model that the transformation is supposed to retire. A sourcing strategy that supports transformation looks structurally different from one that supports steady-state run.</p>"),
        ("Why digital transformation stalls in the vendor layer.",
         "<p>The default transformation pattern goes: define vision, hire systems integrator, run programme. Inside year one, the SI's subcontracting model has produced a delivery network of 8–15 vendors. The cloud migration has added the hyperscaler and one or two specialist managed-service providers. The data platform has added two more. The application modernisation has added three. By the end of year two, the IT vendor portfolio has grown 30–60% — exactly the inverse of what the transformation business case promised.</p><p>The problem is not the vendors. It is that sourcing was treated as a series of procurement events alongside the transformation, rather than as a capability built into it.</p>"),
        ("Cloud vendor management: the governance gap.",
         "<p>The hyperscaler relationship breaks most existing vendor management frameworks. Consumption is metered rather than contracted; the spending pattern can swing 30% month-on-month; the catalogue changes weekly; the negotiation lever is enterprise commitment rather than line-item pricing.</p><p>The framework adjustment: a dedicated cloud governance forum at Tier 2, monthly consumption review, quarterly committed-spend renegotiation, continuous tagging discipline. Most organisations bolt this onto the existing vendor management model; the result is that cloud is everywhere and managed nowhere.</p>"),
        ("AI vendors: special governance rules.",
         "<p>AI service providers are now appearing in IT vendor portfolios at speed. They share the cloud-vendor pattern (metered, fast-changing) but add three further dimensions: data exposure (what is being sent to whom), model behaviour (which can change without notice), and regulatory exposure (which is moving). A bolt-on contract template doesn't cover this.</p><p>The minimum AI-vendor governance addition: data-flow inventory, model-version tracking, output-quality scorecards, explicit DPA and data-residency clauses, and a Tier 3 review cadence that addresses regulatory drift.</p>"),
        ("Hyperscaler governance: AWS, Azure, Google Cloud.",
         "<p>Whichever hyperscaler is the primary, three governance commitments matter: (1) the enterprise commitment is reviewed annually against actual consumption; (2) there is a named technical account manager and a relationship that operates above the support ticket layer; (3) there is a documented multi-cloud or exit posture, even if it is never used. The third is uncomfortable to negotiate; the relationship without it cannot be renegotiated meaningfully.</p>"),
        ("IT sourcing strategy that enables transformation.",
         "<p>Three design principles separate a transformation-supporting sourcing strategy from one that obstructs:</p><ol><li><strong>Capability first, supplier second.</strong> Define the target capability map. Decide which capabilities are core (kept in-house), which are leverage (sourced through strategic partners), which are commodity (sourced through aggregators). Suppliers fall out of the map.</li><li><strong>Architectural coherence.</strong> The five-vendor strategic architecture (infrastructure, applications, end-user, network, sectoral specialist) survives the transformation; the long tail does not. Discipline at sourcing time prevents the post-transformation sprawl.</li><li><strong>Continuous, not event-driven.</strong> Sourcing capability sits inside the transformation operating model, not next to it. New vendor decisions go through the same governance the existing portfolio does.</li></ol>"),
        ("The DACH digital transformation benchmark.",
         "<p>Across the DACH mid-cap engagements we've run in the last 24 months, the median transformation programme is between 15 and 24 months from kickoff to first measurable business outcome — when the sourcing strategy was set up properly. Programmes without a coherent sourcing strategy commonly extend by 30–50% and deliver under-target ROI for reasons that are individually small but cumulatively decisive.</p>"),
        ("IT strategy for the Mittelstand: a 2026 framework.",
         "<p>Mid-market organisations face a structural disadvantage in transformation sourcing: they are too small for hyperscaler enterprise treatment but too complex for SMB packages. The framework that works at this scale: lean strategic-vendor footprint (three to five), aggressive use of platform standardisation to reduce the integration burden, and an outsourced vendor management capability that punches above the in-house headcount.</p>"),
        ("How Aventario approaches this.",
         "<p>We work alongside the transformation lead — usually an internal CIO or external programme director — and own the sourcing strategy and execution end-to-end. The deliverable is a coherent vendor architecture for the post-transformation steady state, with the contracts, governance, and transition plan in place rather than retrofitted afterward.</p>"),
        ("FAQ.",
         "<h3>Why do digital transformations fail at the vendor layer?</h3><p>Because sourcing is treated as a series of procurement events alongside the transformation rather than as a continuous capability built into it. The result is vendor sprawl that retrospectively undermines the transformation business case.</p><h3>How should hyperscaler relationships be governed?</h3><p>Differently from traditional vendors: dedicated forum, monthly consumption review, quarterly commitment renegotiation, continuous tagging discipline, and a documented multi-cloud or exit posture.</p><h3>What is special about AI vendor governance?</h3><p>Three dimensions on top of standard cloud governance: data exposure, model-behaviour drift, and fast-moving regulatory exposure.</p>"),
    ],
    expert=("Markus Kern", "CEO"),
    quote_text="Most transformations don't fail in the strategy deck. They fail in the vendor layer, eighteen months in, when the sourcing model the programme bolted on starts producing a sprawl the business case never anticipated.",
    quote_attrib="Markus Kern, CEO, Aventario",
    related=[("it-vendor-consolidation", "From 47 vendors to 5 strategic partners"),
             ("it-vendor-management", "The complete guide to IT vendor management"),
             ("it-rfp-guide", "How to run complex IT tenders that actually work")],
))

# ============ PILLAR 10: SOFTWARE ============
PILLARS.append(dict(
    slug="vendor-management-software",
    title="Vendor Management Software (2026 Guide)",
    og_title="How to Choose the Right Vendor Management Platform",
    description="A practical guide to choosing vendor management software in 2026: VMS vs SRM vs CLM, the buyer's evaluation criteria, the implementation failure modes, and the platforms that actually fit mid-market complexity.",
    schema_headline="Vendor Management Software: How to Choose the Right Platform (2026 Guide)",
    schema_mentions='{"@type": "Organization", "name": "Aventario"}',
    gradient=GRADIENTS["p10"],
    topic="Software",
    h1="Vendor management software.",
    tagline="A buyer's guide for IT and procurement leaders who have learned that the platform doesn't fix the process, but the wrong platform definitely makes it worse.",
    read_time="12 min read",
    cta_title="Choose the platform that fits.",
    cta_body="Process diagnostic, requirements engineering, structured RFP. We run the selection through Zero Vendor Deviation™ — no sales theatre.",
    body_sections=[
        ("Quick answer.",
         "<p>Vendor management software is the category of platform tooling used to manage the supplier portfolio across contract repository, performance scorecards, risk monitoring, governance forums, and renewal pipeline. The category contains at least three sub-types — VMS, SRM, CLM — that are routinely conflated. Choosing well starts with knowing which of the three you actually need, in what order, and at what maturity.</p>"),
        ("VMS vs SRM vs CLM: the disambiguation.",
         "<ul><li><strong>VMS — Vendor Management System.</strong> Originally a contingent-workforce term (managing temp-staffing suppliers), now used more broadly. Strength: workflow, supplier-portal mechanics. Weakness: thin on contract analytics.</li><li><strong>SRM — Supplier Relationship Management.</strong> Strategic supplier-side platform: segmentation, scorecards, governance, knowledge capture. The CRM-equivalent for vendors. Strength: relationship and performance. Weakness: depending on the tool, contract storage may be basic.</li><li><strong>CLM — Contract Lifecycle Management.</strong> Pre- and post-signature contract workflow: drafting, redlining, repository, obligation tracking, renewal alerts. Strength: contract operations. Weakness: limited supplier-relationship dimension.</li></ul><p>Most organisations need at least two of the three; the order is usually CLM and SRM first, VMS later if the contingent-workforce volume justifies it. A single platform that genuinely covers all three at depth is rare.</p>"),
        ("The 2026 market map.",
         "<p>The vendor management platform market in 2026 segments into four practical groupings:</p><ul><li><strong>Source-to-pay suites.</strong> Coupa, SAP Ariba, Ivalua, Jaggaer. Strength: end-to-end procurement coverage. Weakness: SRM and CLM modules are often shallower than the standalone tools, and implementation cost dominates the business case.</li><li><strong>Best-of-breed CLM.</strong> Icertis, Agiloft, Sirion, ContractPodAI. Strength: contract depth, AI-assisted clause analysis. Weakness: only solve the contract dimension.</li><li><strong>Best-of-breed SRM.</strong> A smaller field; Aventario's managedsuppliers sits here, alongside several legacy tools and emerging entrants. Strength: relationship and performance. Weakness: smaller market means thinner integration ecosystems.</li><li><strong>Workplace-suite-adjacent.</strong> ServiceNow procurement modules, Microsoft Dynamics extensions. Strength: integration with the rest of the stack. Weakness: rarely best-of-breed at any specific dimension.</li></ul>"),
        ("The buyer's evaluation criteria.",
         "<p>The criteria that consistently differentiate platforms in real-world use, ranked by how often they decide outcomes:</p><ol><li><strong>Time to first value.</strong> 90 days or 18 months? The longer the implementation, the more likely the project loses sponsorship before it lands.</li><li><strong>Process fit.</strong> Does the platform support the operating model you've designed, or does it impose its own? Configuration depth matters more than feature breadth.</li><li><strong>Integration footprint.</strong> ERP, ITSM, finance, HR. The platform's value is largely a function of what data it can access and feed.</li><li><strong>AI capability, real not marketed.</strong> Clause extraction, risk-signal monitoring, SLA reconciliation — at portfolio scale. Most marketing claims do not survive a structured proof-of-concept.</li><li><strong>Total cost of ownership.</strong> Licence, implementation, ongoing configuration, internal admin headcount. Multiply the licence cost by 2.5–4× for realistic year-one TCO.</li><li><strong>Vendor viability.</strong> The platform vendor's own financial and product trajectory. Five years is a long time in this market.</li></ol>"),
        ("The five implementation failure modes.",
         "<ul><li><strong>Platform-first, process-second.</strong> The most common. The tool gets configured; the operating model stays improvised. Symptoms appear in months 6–12 and the project is rarely recovered.</li><li><strong>Big-bang scope.</strong> All vendors, all contracts, all geographies, day one. Implementations that try this almost never finish.</li><li><strong>Customisation creep.</strong> Configuration becomes customisation; upgrade paths break; the platform becomes legacy on arrival.</li><li><strong>Underweight integration.</strong> Standalone deployment with no live data feeds. The tool becomes a parallel-truth source that nobody trusts.</li><li><strong>Owner ambiguity.</strong> Procurement-led but IT-funded, or vice versa. The platform survives only as long as the original sponsor.</li></ul>"),
        ("How to write the SRM software RFI.",
         "<p>The single best signal of a serious buyer is a structured RFI that vendors cannot deviate from — atomised requirements, weighted, answerable in a fixed format. The same Zero Vendor Deviation™ approach we use for IT outsourcing tenders applies here. The output is genuinely comparable responses; the avoided cost is the months of evaluation theatre that platform selection otherwise becomes.</p>"),
        ("From Excel to platform: the migration roadmap.",
         "<p>Most SRM platform implementations should be staged: tier-1 strategic vendors first (10–20 vendors), then the next tier (30–60 vendors), then the long tail. Each stage is its own micro-implementation with its own go-live, its own user training, its own value-realisation review. Big-bang is the failure pattern; staged-by-segment is the success pattern.</p>"),
        ("AI features that actually work.",
         "<ul><li><strong>Clause extraction</strong> across the contract portfolio at indexing speed.</li><li><strong>SLA reconciliation</strong> against ticket-level data.</li><li><strong>Risk-signal monitoring</strong> across financial, security, and regulatory feeds.</li><li><strong>Meeting-summary capture</strong> from QBR transcripts into the scorecard.</li><li><strong>Benchmark-gap analysis</strong> at the line-item level against external pricing data.</li></ul><p>Marketing claims that go further than this in 2026 are usually demos, not deployments.</p>"),
        ("How Aventario approaches this.",
         "<p>We've run more than a dozen vendor management platform selections in the last three years, and we've built our own (managedsuppliers) to fill the gap we kept seeing in mid-market deployments. Our default approach: process diagnostic first, target-state operating model second, structured RFI third. Platform selection should be a 10-week engagement, not a 10-month one.</p>"),
        ("FAQ.",
         "<h3>What is the difference between VMS, SRM, and CLM?</h3><p>VMS (Vendor Management System) focuses on supplier workflow, originally for contingent workforce. SRM (Supplier Relationship Management) focuses on supplier performance and relationship governance. CLM (Contract Lifecycle Management) focuses on contract operations across the full lifecycle.</p><h3>How long should an SRM implementation take?</h3><p>For a tier-1 strategic-vendor cohort (10–20 vendors), 90 days is achievable. Full-portfolio implementations stage out across 9–18 months in successive cohorts.</p><h3>Should we choose a suite or best-of-breed?</h3><p>Depends on integration priority. Suites win on out-of-the-box integration; best-of-breed wins on capability depth. Most mid-market organisations end up with a hybrid: best-of-breed CLM and SRM, federated through their existing ERP.</p>"),
    ],
    expert=("Markus Kern", "CEO"),
    quote_text="The platform doesn't fix the process. The wrong platform definitely makes it worse — and the implementation cost makes the mistake hard to reverse.",
    quote_attrib="Markus Kern, CEO, Aventario",
    related=[("supplier-relationship-management", "Supplier Relationship Management — the CRM you don't have for your vendors"),
             ("it-contract-management", "From signature to savings"),
             ("it-vendor-management", "The complete guide to IT vendor management")],
))


# ---------- RENDER ----------

def render_body(p):
    parts = []
    # First section is always the quick answer; insert the pull-quote after it
    for i, (h, html) in enumerate(p["body_sections"]):
        parts.append(f'            <h2>{h}</h2>')
        parts.append(f'            {html}')
        if i == 1:  # after second h2
            parts.append(quote(p["quote_text"], p["quote_attrib"]))
    parts.append(expert_bio(*p["expert"]))
    parts.append(related(p["related"]))
    return "\n".join(parts)

for p in PILLARS:
    body = render_body(p)
    html = HEAD.format(
        title=p["title"],
        og_title=p["og_title"],
        description=p["description"],
        slug=p["slug"],
        gradient=p["gradient"],
        schema_headline=p["schema_headline"],
        schema_mentions=p["schema_mentions"],
        topic=p["topic"],
        h1=p["h1"],
        tagline=p["tagline"],
        read_time=p["read_time"],
        body=body,
        cta_title=p["cta_title"],
        cta_body=p["cta_body"],
    )
    out_file = OUT / f'{p["slug"]}.html'
    out_file.write_text(html, encoding="utf-8")
    print(f"wrote {out_file.name}")

print(f"\n{len(PILLARS)} pillar pages generated.")
