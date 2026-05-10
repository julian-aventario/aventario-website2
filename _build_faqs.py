"""
Builder for the 10 FAQ articles (Phase 1, weeks 5-8 of the master plan).
800-900 words each, answer-first, FAQPage schema.
"""
from pathlib import Path

OUT = Path(__file__).parent / "blog"
OUT.mkdir(exist_ok=True)

GRADIENTS = [
    "linear-gradient(135deg, #334b60 0%, #50757f 50%, #88c9be 100%)",
    "linear-gradient(135deg, #88c9be 0%, #5fa99d 100%)",
    "linear-gradient(135deg, #f19a51 0%, #d15298 100%)",
    "linear-gradient(135deg, #334b60 0%, #d15298 100%)",
    "linear-gradient(135deg, #5fa99d 0%, #334b60 100%)",
    "linear-gradient(135deg, #334b60 0%, #5f768b 100%)",
    "linear-gradient(135deg, #f19a51 0%, #334b60 100%)",
    "linear-gradient(135deg, #334b60 0%, #88c9be 100%)",
    "linear-gradient(135deg, #d15298 0%, #5fa99d 100%)",
    "linear-gradient(135deg, #5f768b 0%, #88c9be 100%)",
]

TEMPLATE = """<!DOCTYPE html>
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
        .prose-aventario h2 {{ font-size: 1.625rem; margin-top: 2.5rem; margin-bottom: 0.85rem; }}
        .prose-aventario h3 {{ font-size: 1.25rem; margin-top: 1.75rem; margin-bottom: 0.5rem; }}
        .prose-aventario ul {{ margin-bottom: 1.4rem; padding-left: 1.5rem; }}
        .prose-aventario ul li {{ font-size: 1.125rem; line-height: 1.7; margin-bottom: 0.5rem; list-style: disc; color: #334b60; }}
        .prose-aventario ol {{ margin-bottom: 1.4rem; padding-left: 1.5rem; }}
        .prose-aventario ol li {{ font-size: 1.125rem; line-height: 1.7; margin-bottom: 0.6rem; list-style: decimal; color: #334b60; }}
        .prose-aventario a {{ color: #5FA99D; font-weight: 700; text-decoration: underline; text-decoration-thickness: 1px; text-underline-offset: 3px; }}
        .prose-aventario a:hover {{ color: #334b60; }}
        .prose-aventario strong {{ font-weight: 900; color: #334b60; }}
        .answer-box {{ background: #FFFFFF; border-left: 4px solid #88C9BE; padding: 1.5rem 1.75rem; margin: 0 0 2rem 0; border-radius: 4px; }}
        .answer-box p {{ font-size: 1.25rem; font-weight: 700; line-height: 1.5; margin-bottom: 0; color: #334b60; }}
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
      "mainEntityOfPage": "https://aventario.com/blog/{slug}"
    }}
    </script>
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": [{faq_jsonld}]
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

    <section class="px-6 md:px-12 pt-16 md:pt-24 pb-12 border-b border-bordercolor">
        <div class="max-w-3xl mx-auto">
            <a href="../blog.html" class="inline-flex items-center gap-2 text-xs uppercase tracking-widest text-text/60 hover:text-text mb-8"><i class="ph ph-arrow-left"></i> Back to blog</a>
            <span class="inline-block text-xs uppercase tracking-widest font-bold px-3 py-1 rounded-full bg-text text-surface mb-6">FAQ · Definition</span>
            <h1 class="font-serif text-3xl md:text-5xl mb-6">{h1}</h1>
            <p class="text-lg text-text/80 leading-relaxed mb-6">{tagline}</p>
            <div class="flex items-center gap-4 pt-4 border-t border-bordercolor">
                <div class="w-10 h-10 rounded-full bg-text text-surface flex items-center justify-center text-xs font-bold">JR</div>
                <div class="text-sm">
                    <p class="font-bold text-text">Julian Robida</p>
                    <p class="text-text/60">Research Lead · Aventario · {read_time} · 7 May 2026</p>
                </div>
            </div>
        </div>
    </section>

    <section class="px-6 md:px-12 py-10">
        <div class="max-w-3xl mx-auto post-cover aspect-[16/5] rounded-md"></div>
    </section>

    <article class="px-6 md:px-12 pb-16">
        <div class="max-w-3xl mx-auto prose-aventario">
{body}
            <div class="mt-12 p-6 bg-surface border border-bordercolor rounded-md">
                <p class="text-xs uppercase tracking-widest text-text font-bold mb-3">Related</p>
                <ul class="space-y-2">
{related_html}
                </ul>
            </div>
        </div>
    </article>

    <section class="px-6 md:px-12 py-16" style="background-color: #334b60; color: #FFFFFF;">
        <div class="max-w-3xl mx-auto text-center">
            <h2 class="font-serif text-2xl md:text-3xl text-surface mb-3">Want to talk about this?</h2>
            <p class="text-base leading-relaxed mb-6" style="color: rgba(255,255,255,0.75);">We work with CIOs, CPOs, and CFOs across DACH on exactly these problems. One conversation, no pitch deck.</p>
            <a href="../contact.html" class="inline-flex items-center gap-3 text-sm font-bold uppercase tracking-widest px-6 py-3 rounded-full" style="background-color: #f19a51; color: #FFFFFF;">Get in touch <i class="ph ph-arrow-right"></i></a>
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

import json

def faq_jsonld(qa):
    items = []
    for q, a in qa:
        items.append({
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {"@type": "Answer", "text": a},
        })
    return ", ".join(json.dumps(i, ensure_ascii=False) for i in items)


FAQS = [
    dict(
        slug="vendor-management-office",
        title="What Is a Vendor Management Office (VMO)?",
        og_title="What Is a VMO? — Aventario",
        description="A clear, practical definition of a Vendor Management Office (VMO): what it does, what it doesn't do, where it sits in the org, and the four operating models that actually work.",
        schema_headline="What Is a Vendor Management Office (VMO)? Definition and Operating Models",
        h1="What is a vendor management office?",
        tagline="The function that owns the supplier portfolio across the lifecycle. Often confused with procurement; almost never the same thing.",
        read_time="6 min read",
        answer="A Vendor Management Office (VMO) is the centralised function that owns the lifecycle of every external supplier relationship — from sourcing strategy through contract governance, performance management, risk monitoring, and renewal or exit. It is the operational home for vendor management across the organisation.",
        body_md="""<h2>What a VMO actually does.</h2>
<p>The job of a VMO is the work that no individual project team has time for and that procurement, on its own, isn't structured to do. Five core responsibilities:</p>
<ul>
<li><strong>Portfolio visibility.</strong> Maintain the single source of truth on who is contracted to do what, at what cost, until when.</li>
<li><strong>Governance cadence.</strong> Run the operational, managerial, and strategic forums (the Three-Tier Governance Model) for the vendors that matter.</li>
<li><strong>Performance management.</strong> Score, benchmark, and challenge supplier performance against contracted SLAs and against the market.</li>
<li><strong>Risk monitoring.</strong> Surface financial, regulatory, security, and operational risk signals before they become incidents.</li>
<li><strong>Renewal pipeline.</strong> Maintain the 12–18 month forward calendar of decisions: renew, renegotiate, or exit.</li>
</ul>
<h2>What a VMO is not.</h2>
<p>It is not procurement. Procurement runs the tender; the VMO runs everything that happens before procurement is engaged (sourcing strategy) and after the contract is signed (governance). The two functions are tightly coupled but they are not the same job.</p>
<p>It is not a service-management function. Service management owns delivery quality of a specific service; the VMO owns the relationship across services and across vendors.</p>
<p>It is not a relationship-only role. A VMO whose responsibilities stop at "managing the relationship" produces nice meetings and no measurable value. The credibility of the function depends on owning numbers — savings realised, SLA compliance verified, risks closed.</p>
<h2>The four VMO operating models.</h2>
<ol>
<li><strong>Centralised.</strong> A dedicated team, reporting to the CIO or CFO, with end-to-end authority over the supplier portfolio. Strongest leverage, highest cost.</li>
<li><strong>Federated.</strong> Central VMO sets standards, methods, and reporting; embedded vendor managers sit inside business or IT functions and execute. Common in larger organisations.</li>
<li><strong>Centre of excellence.</strong> Light-touch central team that owns methodology and tooling; execution stays distributed. Lower cost; relies on adoption discipline.</li>
<li><strong>Outsourced (VM-as-a-Service).</strong> The function is delivered by an external partner under an outcome-based engagement. Common where in-house headcount is constrained or where the value-recovery target requires capability the organisation doesn't have.</li>
</ol>
<p>Most mid-cap organisations land on a federated or outsourced model. The fully centralised model produces the strongest leverage but requires headcount that boards will only fund after the value case has already been proven — which is itself a chicken-and-egg problem.</p>
<h2>Where the VMO sits in the org.</h2>
<p>Reporting line determines behaviour. A VMO under the CIO will optimise for service quality and architectural fit; under the CFO, for cost and contract integrity; under the CPO, for procurement leverage and category strategy. None of these is wrong. The choice should reflect what the organisation actually needs the VMO to fix.</p>
<p>Across our engagements, the most common reporting line in DACH mid-caps is dual: dotted-line into Procurement for category-strategy alignment, solid-line into IT (CIO or COO) for operational accountability.</p>
<h2>How to know whether you need one.</h2>
<p>You need a VMO — or a VM-as-a-Service equivalent — if any three of the following are true: you have more than 50 active IT vendors, more than 20% of contracts auto-renew without active review, no single function can answer "what is our total spend with vendor X" in five minutes, vendor performance is reported by vendors themselves and not independently verified, or the last benchmark on your top vendors was more than 24 months ago.</p>
<h2>FAQ.</h2>
<h3>What does VMO stand for?</h3>
<p>Vendor Management Office.</p>
<h3>Is a VMO the same as procurement?</h3>
<p>No. Procurement typically owns the sourcing event and the contract signature. The VMO owns the strategy that precedes procurement and the governance that follows. The two functions are complementary.</p>
<h3>Who should the VMO report to?</h3>
<p>Most commonly the CIO, COO, or CFO, with a dotted line to the CPO. The choice depends on whether the organisation primarily needs the VMO to fix cost, service, or strategic-leverage problems.</p>""",
        faq=[
            ("What does VMO stand for?", "Vendor Management Office."),
            ("Is a VMO the same as procurement?", "No. Procurement typically owns the sourcing event and the contract signature. The VMO owns the strategy that precedes procurement and the governance that follows. The two functions are complementary, not interchangeable."),
            ("Who should the VMO report to?", "Most commonly the CIO, COO, or CFO, with a dotted line to the CPO. The choice depends on whether the organisation primarily needs the VMO to fix cost, service, or strategic-leverage problems."),
            ("What are the four VMO operating models?", "Centralised, federated, centre of excellence, and outsourced (vendor management-as-a-service). Most mid-cap organisations land on a federated or outsourced model."),
        ],
        related=[("it-vendor-management", "The complete guide to IT vendor management"),
                 ("it-vendor-governance", "The framework that keeps vendors accountable"),
                 ("supplier-relationship-management", "SRM: the CRM you don't have for your vendors")],
    ),

    dict(
        slug="zero-vendor-deviation",
        title="What Is Zero Vendor Deviation in Procurement?",
        og_title="What Is Zero Vendor Deviation? — Aventario",
        description="Zero Vendor Deviation™ is Aventario's RFP methodology. It compresses complex IT tenders to 6–8 weeks and produces line-for-line comparable responses by removing the room vendors normally use to differentiate themselves into ambiguity.",
        schema_headline="What Is Zero Vendor Deviation™ in Procurement?",
        h1="What is Zero Vendor Deviation™?",
        tagline="Aventario's RFP methodology. Built so vendors cannot deviate from the structure of the question — and you get responses that compare line-for-line.",
        read_time="5 min read",
        answer="Zero Vendor Deviation™ is Aventario's proprietary RFP methodology. Every requirement is atomised, weighted, and answerable in a fixed format; every pricing line uses the same units and bands across vendors; every assumption is either pre-stated by the buyer or required to be priced individually. The result is responses that compare line-for-line and a tender that completes in six to eight weeks instead of four to six months.",
        body_md="""<h2>The problem it solves.</h2>
<p>The default failure mode of an IT RFP is not that the wrong vendor wins. It's that, by the time responses come back, no one can confidently say which vendor would have been the right one. Apples-to-oranges proposals. Open-ended assumption blocks. Pricing that depends on volumes the buyer never specified. The buyer ends up choosing on instinct or on slide-deck quality, and the chosen vendor's commercial terms quietly drift in their favour during negotiation.</p>
<p>The root cause is upstream. The RFP gave each vendor too much room to tell their own story instead of answering the same question. Vendors are good at this — it is how they avoid being commoditised. If you don't close that room down deliberately, you give it away.</p>
<h2>The methodology, in mechanics.</h2>
<ul>
<li><strong>Atomised requirements.</strong> 300–600 individually-numbered, individually-weighted line items per RFP, each answerable in a constrained format (compliant / partial / non-compliant + evidence).</li>
<li><strong>Pricing skeleton.</strong> A pre-built pricing matrix the vendor fills in. Same units, same volume bands, same indexation, same currency. No free-form quotes.</li>
<li><strong>Buyer-stated assumptions.</strong> The assumptions the bid should be built on are listed in the document. Vendor-stated assumptions must be priced separately and ranked.</li>
<li><strong>Published evaluation rubric.</strong> Vendors see how their response will be scored before they write it. Surprises are eliminated.</li>
</ul>
<h2>Why it works.</h2>
<p>Vendors respond to incentives. If the only path to winning is answering the actual question in the actual format, vendors do that — even though they would prefer to answer their own question in their own format. The structure does the work.</p>
<p>Evaluation collapses from weeks of debate to hours of compliance scoring. Award decisions become defensible because the methodology, not just the conclusion, is documented. And contract negotiations open from a position where the buyer already knows exactly what they're getting and what they're paying for it — not a position where the negotiation has to fix the ambiguity that the RFP didn't.</p>
<h2>Where it applies.</h2>
<p>Zero Vendor Deviation is built for complex IT and IT-services tenders: outsourcing, platform implementations, large managed-services agreements, multi-vendor consolidation, ERP and SAP rollouts. It is overkill for commodity hardware refreshes (an RFQ does the job) and not the right tool for early-stage market discovery (where an RFI is the right document).</p>
<h2>Track record.</h2>
<p>The methodology has been applied to more than 500 IT tenders across pharma, automotive, financial services, telecoms, and the public sector. Median timeline from kick-off to award: 6–8 weeks. Median number of post-award contract negotiations needed to fix RFP ambiguities: zero, by design.</p>
<h2>FAQ.</h2>
<h3>Is Zero Vendor Deviation a tool or a methodology?</h3>
<p>A methodology, supported by templates and tooling. The methodology is the discipline; the templates make it executable in 6–8 weeks.</p>
<h3>Can we apply Zero Vendor Deviation ourselves?</h3>
<p>Yes — the principles are public. The full methodology, templates, and benchmark data are part of Aventario's Complex RFx engagement, but the principles can be adopted independently.</p>
<h3>How is this different from a normal RFP?</h3>
<p>A normal RFP allows vendors freedom in how they structure responses; Zero Vendor Deviation removes that freedom by design. The trade-off is that more upstream work goes into the document; the payoff is comparable responses and a much shorter evaluation cycle.</p>""",
        faq=[
            ("What is Zero Vendor Deviation?", "Zero Vendor Deviation™ is Aventario's proprietary RFP methodology. It atomises requirements, standardises pricing structures, and publishes the evaluation rubric so that vendors cannot deviate from the structure of the question. The result is line-for-line comparable responses and a 6–8 week tender cycle."),
            ("Is Zero Vendor Deviation a tool or a methodology?", "A methodology, supported by templates and tooling. The methodology is the discipline; the templates make it executable in 6–8 weeks."),
            ("How is Zero Vendor Deviation different from a normal RFP?", "A normal RFP allows vendors freedom in how they structure responses; Zero Vendor Deviation removes that freedom by design. More upstream work goes into the document; the payoff is comparable responses and a much shorter evaluation cycle."),
        ],
        related=[("it-rfp-guide", "The IT RFP guide"),
                 ("it-vendor-management", "The complete guide to IT vendor management"),
                 ("vendor-management-software", "Vendor management software buyer's guide")],
    ),

    dict(
        slug="sla-vs-ola-vs-kpi",
        title="SLA vs OLA vs KPI: The Differences That Matter",
        og_title="SLA vs OLA vs KPI — Aventario",
        description="Service Level Agreement, Operational Level Agreement, Key Performance Indicator — three terms that are routinely confused. Here's the practical definition of each, why they matter, and where the loopholes hide.",
        schema_headline="SLA vs OLA vs KPI: The Differences That Matter for IT Vendor Management",
        h1="SLA vs OLA vs KPI.",
        tagline="Three terms, three jobs. The confusion between them is where most SLA disputes actually live.",
        read_time="5 min read",
        answer="An SLA (Service Level Agreement) is the external, contractual commitment between buyer and vendor. An OLA (Operational Level Agreement) is the internal commitment between teams or sub-suppliers that underpins the SLA. A KPI (Key Performance Indicator) is the specific metric used to measure whether the SLA is being met. Most SLA disputes are not about the threshold — they are about which KPI is used to measure it.",
        body_md="""<h2>SLA — Service Level Agreement.</h2>
<p>The contractually committed performance threshold between the buyer and the vendor. SLAs typically cover availability, response time, resolution time, and quality metrics. Breaching the SLA has financial or service-credit consequences spelled out in the contract.</p>
<p>An SLA is only as good as its definitions. "99.9% availability" sounds firm until you ask: availability of what, measured at which point in the architecture, with which exclusions, over what reporting period. Two vendors offering "99.9% availability" can deliver materially different actual uptime depending on those four answers.</p>
<h2>OLA — Operational Level Agreement.</h2>
<p>The internal commitments — between teams within the vendor's organisation, or between the vendor and its sub-suppliers — that underpin the SLA. The OLA is invisible to the buyer in normal circumstances, but it determines whether the SLA can actually be delivered. A vendor that promises a 4-hour response SLA but whose internal incident-management OLA is "best effort" will miss the SLA repeatedly.</p>
<p>For the buyer, the practical implication is that strong SLAs require evidence of strong OLAs underneath. In a structured RFP, this is one of the things the document asks vendors to demonstrate, not just promise.</p>
<h2>KPI — Key Performance Indicator.</h2>
<p>The specific, measurable metric used to evaluate performance. KPIs operationalise the SLA — they say <em>how</em> the SLA threshold will be measured. The choice of KPI is often where the loophole hides.</p>
<p>Worked example: an SLA committing to "P1 incident resolution within 4 hours" sounds clear. But the underlying KPI may be defined as "elapsed time from incident acknowledgement to status-change to resolved." Acknowledgement can be delayed; status-change can be applied to incidents that aren't actually resolved; reopened incidents can be excluded; certain incident categories can fall outside scope. Each is a small definitional choice; cumulatively they can move the apparent KPI by 30–50%.</p>
<h2>Where most SLA disputes actually live.</h2>
<p>Across the engagements we run, the most common SLA dispute is not about the threshold being missed. It is about whether the KPI used to measure it accurately reflects what the buyer thought they were buying. The fix is upstream: define the KPI mechanics in the contract, not in a separate operational document that can be reinterpreted later.</p>
<h2>The contract checklist.</h2>
<ul>
<li><strong>Define the SLA threshold</strong> with specific numerical targets and reporting period.</li>
<li><strong>Define the KPI mechanics</strong> — how the metric is calculated, what is included, what is excluded, when the clock starts and stops.</li>
<li><strong>Require OLA evidence</strong> — for tier-1 services, request the operational-level agreements that underpin the SLA, in summary form, attached to the contract.</li>
<li><strong>Set service-credit consequences</strong> — financial or operational consequences for missed SLAs that are large enough to drive vendor behaviour.</li>
<li><strong>Reserve verification rights</strong> — the right to independently verify SLA reports against ticket-level or telemetry data.</li>
</ul>
<h2>FAQ.</h2>
<h3>What is the difference between SLA and OLA?</h3>
<p>An SLA is the external, contractual commitment between buyer and vendor. An OLA is the internal commitment between teams or sub-suppliers that supports the SLA. The OLA is invisible to the buyer but essential for SLA delivery.</p>
<h3>What is a KPI in the context of SLAs?</h3>
<p>A KPI is the specific metric used to measure whether the SLA threshold is being met. The choice of KPI — what it measures, when the clock starts and stops, what is included or excluded — is often where SLA disputes actually originate.</p>
<h3>Should KPI definitions be in the contract?</h3>
<p>Yes. Defining the SLA threshold without defining the KPI mechanics that measure it leaves room for reinterpretation later. Both should be unambiguous in the executed contract.</p>""",
        faq=[
            ("What is the difference between SLA and OLA?", "An SLA is the external, contractual commitment between buyer and vendor. An OLA is the internal commitment between teams or sub-suppliers that supports the SLA. The OLA is invisible to the buyer but essential for SLA delivery."),
            ("What is a KPI in the context of SLAs?", "A KPI is the specific metric used to measure whether the SLA threshold is being met. The choice of KPI is often where SLA disputes actually originate."),
            ("Should KPI definitions be in the contract?", "Yes. Defining the SLA threshold without defining the KPI mechanics that measure it leaves room for reinterpretation later. Both should be unambiguous in the executed contract."),
        ],
        related=[("it-contract-management", "From signature to savings: a practical guide"),
                 ("it-vendor-governance", "The framework that keeps vendors accountable"),
                 ("it-vendor-management", "The complete guide to IT vendor management")],
    ),

    dict(
        slug="kraljic-matrix",
        title="What Is the Kraljic Matrix and How Is It Used?",
        og_title="The Kraljic Matrix — Aventario",
        description="The Kraljic Matrix segments suppliers along two dimensions — supply risk and profit impact — to produce four governance approaches: strategic, leverage, bottleneck, and routine.",
        schema_headline="What Is the Kraljic Matrix and How Is It Used in IT Procurement?",
        h1="What is the Kraljic Matrix?",
        tagline="The default supplier-segmentation tool, applied to IT. Four quadrants, four governance approaches, one critical mistake to avoid.",
        read_time="6 min read",
        answer="The Kraljic Matrix is a procurement segmentation tool that maps suppliers along two axes: supply risk (how hard would they be to replace) and profit impact (how much do they cost or how much do they enable). The four resulting quadrants — strategic, leverage, bottleneck, and routine — each call for a different governance approach. It is the most common segmentation framework in mature procurement organisations.",
        body_md="""<h2>The four quadrants.</h2>
<h3>Strategic (high risk, high impact).</h3>
<p>Few in number — typically the top five strategic IT partners. Hard to replace, large spend, high enablement value. Multi-year contracts, deep governance, joint roadmap planning, executive sponsorship matched to relationship value. This quadrant is where consolidation programmes typically land.</p>
<h3>Leverage (low risk, high impact).</h3>
<p>Commodity-like services with many credible substitutes but significant spend. Cloud infrastructure (within a hyperscaler tier), commodity hardware, standardised software licences, contingent-workforce providers. Rotate aggressively. Benchmark constantly. Vendors here should know they are easily replaceable, and that knowledge should drive their pricing.</p>
<h3>Bottleneck (high risk, low impact).</h3>
<p>Niche capabilities, hard to replace, low overall spend. A specialist support contract for a legacy platform; a regional MSP for a single office. The risk is operational disruption if the vendor fails; the spend is too small to justify deep relationship investment. Mitigate via contract design (escrow, knowledge transfer, exit support) rather than relationship energy.</p>
<h3>Routine (low risk, low impact).</h3>
<p>The long tail. Easily substitutable, low spend per vendor, often dozens or hundreds of vendors collectively consuming significant administrative bandwidth. Consolidate ruthlessly through procurement aggregators or via the strategic partners.</p>
<h2>How to apply it.</h2>
<ol>
<li><strong>Assemble the inventory.</strong> Every active vendor, with annual spend and a brief description of what they provide.</li>
<li><strong>Score profit impact.</strong> Annual spend is the starting point; adjust for criticality (a small-spend vendor that runs your payroll has high impact).</li>
<li><strong>Score supply risk.</strong> How many credible alternatives exist, how long would it take to switch, what data or knowledge is locked in with the vendor.</li>
<li><strong>Plot.</strong> Each vendor lands in one quadrant. Group-level patterns emerge quickly.</li>
<li><strong>Differentiate the management model.</strong> Each quadrant gets a different cadence, scorecard, governance forum, and relationship investment.</li>
</ol>
<h2>The mistake to avoid.</h2>
<p>Over-investing in routine vendors and under-investing in strategic ones. The relationship-management calorie budget is finite. Spend it where the value is. The discipline is to actively cut governance overhead on quadrants where it doesn't pay back, and reinvest the freed capacity into the strategic quadrant where it does.</p>
<h2>Adjusting Kraljic for IT.</h2>
<p>The original Kraljic framework was developed for industrial procurement in the 1980s. Three adjustments make it work for modern IT vendor management:</p>
<ul>
<li><strong>Substitutability is dynamic.</strong> A cloud workload that is "high supply risk" today (deeply tied to one hyperscaler's services) may become low-risk through deliberate architectural choices. Movement between quadrants is itself an output of the strategy.</li>
<li><strong>Innovation value is its own axis.</strong> Some vendors are kept not for cost or replaceability reasons but because they bring strategic capability to the relationship. They sit in the strategic quadrant by judgement, not pure scoring.</li>
<li><strong>Concentration risk needs explicit treatment.</strong> Multiple vendors that look strategic individually may aggregate into a concentration-risk problem (too much spend with one company). Worth flagging at the portfolio level.</li>
</ul>
<h2>FAQ.</h2>
<h3>Who developed the Kraljic Matrix?</h3>
<p>Peter Kraljic, in a 1983 Harvard Business Review article. It has remained the dominant supplier-segmentation framework in mature procurement organisations for four decades.</p>
<h3>How does the Kraljic Matrix apply to IT vendors?</h3>
<p>The two-axis logic translates directly. Most IT vendor portfolios reveal a small strategic quadrant (top 3–7 vendors), a moderate leverage quadrant, a small bottleneck quadrant, and a long routine tail.</p>
<h3>Is the Kraljic Matrix the only segmentation framework?</h3>
<p>No, but it is the most widely used. Alternatives focus on innovation potential, ESG profile, or relationship maturity. In practice, the Kraljic axes are sufficient as a starting point and additional dimensions can be layered for specific decisions.</p>""",
        faq=[
            ("What is the Kraljic Matrix?", "A procurement segmentation framework that maps suppliers along two axes — supply risk and profit impact — into four quadrants: strategic, leverage, bottleneck, and routine. Each quadrant calls for a different governance approach."),
            ("Who developed the Kraljic Matrix?", "Peter Kraljic, in a 1983 Harvard Business Review article. It has remained the dominant supplier-segmentation framework in mature procurement organisations for four decades."),
            ("How does the Kraljic Matrix apply to IT vendors?", "The two-axis logic translates directly. Most IT vendor portfolios reveal a small strategic quadrant (top 3–7 vendors), a moderate leverage quadrant, a small bottleneck quadrant, and a long routine tail."),
        ],
        related=[("it-vendor-consolidation", "From 47 vendors to 5 strategic partners"),
                 ("supplier-relationship-management", "SRM: the CRM you don't have for your vendors"),
                 ("it-vendor-management", "The complete guide to IT vendor management")],
    ),

    dict(
        slug="it-vendor-risk",
        title="What Is IT Vendor Risk and How Is It Categorised?",
        og_title="What Is IT Vendor Risk? — Aventario",
        description="A practical taxonomy for IT vendor risk: the seven categories, how each is monitored, and the governance forum where each is reviewed. Built for CIOs, CFOs, and risk leads in DACH mid-caps.",
        schema_headline="What Is IT Vendor Risk and How Is It Categorised?",
        h1="What is IT vendor risk?",
        tagline="Seven categories. Each has a different signal, a different cadence, and a different forum where it should land before it becomes an incident.",
        read_time="6 min read",
        answer="IT vendor risk is the exposure an organisation carries from its dependency on external technology providers. It spans seven categories: financial, operational, security, regulatory, concentration, exit, and reputational. Each is monitored differently and surfaces in a different governance forum. A mature vendor-risk capability tracks all seven continuously rather than addressing each only when an incident occurs.",
        body_md="""<h2>The seven categories.</h2>
<h3>1. Financial risk.</h3>
<p>The vendor's own financial health. A struggling vendor cuts service investment, raises prices, or fails outright. Signals: declining revenue, missed earnings targets (for public vendors), key-person departures, late filings, debt restructuring. Monitor via credit-watch services and quarterly review of public filings for tier-1 vendors.</p>
<h3>2. Operational risk.</h3>
<p>The vendor's ability to deliver against contractual commitments. Signals: SLA misses, escalating incident rates, slowing response times, deteriorating change-success rates. Monitor via the operational governance forum (Tier 1 in the Three-Tier Governance Model) and monthly scorecard.</p>
<h3>3. Security risk.</h3>
<p>The vendor's information security posture and recent incident history. Signals: published security advisories affecting the vendor's stack, breach disclosures, certification lapses (ISO 27001, SOC 2), audit findings. Monitor via dedicated security review and standing agenda item at managerial governance.</p>
<h3>4. Regulatory and compliance risk.</h3>
<p>Exposure under sector-specific regulation: GDPR for any vendor processing personal data, DORA for financial services, GxP for life sciences, BaFin requirements for banking, EU procurement rules for public sector. Signals: regulatory audit findings, jurisdictional changes, evolving data-residency requirements. Monitor via compliance function and quarterly strategic review.</p>
<h3>5. Concentration risk.</h3>
<p>Excessive dependency on a single vendor or group. Most IT vendor portfolios become concentrated by attrition rather than design — a strategic vendor's scope grows incrementally until 30–40% of in-scope IT services run through one provider. Mitigate via contract design (multi-cloud postures, second-source clauses, exit-support obligations) and explicit board-visible reporting.</p>
<h3>6. Exit and lock-in risk.</h3>
<p>The cost and difficulty of leaving the vendor if the relationship deteriorates. Signals: weak termination-for-convenience clauses, proprietary formats with no clean export, deep integration footprints, knowledge concentrated in vendor staff. Mitigate at contract signature, not later.</p>
<h3>7. Reputational and ESG risk.</h3>
<p>Risk from vendor behaviour reflecting on the buyer: labour practices in the vendor's supply chain, sustainability disclosures, governance scandals, association with sanctioned entities. Signals: media coverage, NGO reports, regulatory action against the vendor. Monitor via ESG function and annual review.</p>
<h2>How to operationalise this.</h2>
<p>Each tier-1 strategic vendor gets a standing risk register with all seven categories. The register is reviewed monthly at the managerial governance forum and quarterly at the strategic forum. Material changes in any category trigger an explicit decision: continue, mitigate, escalate, or prepare for exit.</p>
<p>The discipline that distinguishes mature vendor-risk capability from immature is whether the register is reviewed proactively (every month, on a calendar) or reactively (only when an incident occurs).</p>
<h2>FAQ.</h2>
<h3>How many vendor risk categories should we track?</h3>
<p>Seven covers the practical landscape: financial, operational, security, regulatory, concentration, exit, reputational. For tier-1 strategic vendors, all seven; for routine vendors, the first four are usually sufficient.</p>
<h3>How often should vendor risk be reviewed?</h3>
<p>Tier-1 strategic vendors: monthly at managerial governance, quarterly at strategic governance. Tier-2 vendors: quarterly. Routine vendors: at renewal trigger.</p>
<h3>What is the most under-managed vendor risk?</h3>
<p>Concentration risk. Most portfolios become over-concentrated by accretion rather than design, and the exposure is usually not visible at any individual vendor's scorecard — only at the portfolio level.</p>""",
        faq=[
            ("What is IT vendor risk?", "The exposure an organisation carries from its dependency on external technology providers. It spans seven categories: financial, operational, security, regulatory, concentration, exit, and reputational."),
            ("How many vendor risk categories should we track?", "Seven covers the practical landscape: financial, operational, security, regulatory, concentration, exit, reputational. For tier-1 strategic vendors, all seven; for routine vendors, the first four are usually sufficient."),
            ("What is the most under-managed vendor risk?", "Concentration risk. Most portfolios become over-concentrated by accretion rather than design, and the exposure is usually not visible at any individual vendor's scorecard — only at the portfolio level."),
        ],
        related=[("it-vendor-governance", "The framework that keeps vendors accountable"),
                 ("it-vendor-management", "The complete guide to IT vendor management"),
                 ("it-contract-management", "From signature to savings")],
    ),

    dict(
        slug="frame-contract-it",
        title="What Is a Frame Contract in IT Sourcing?",
        og_title="What Is an IT Frame Contract? — Aventario",
        description="A frame contract (Rahmenvertrag) is a master agreement that pre-negotiates terms and conditions for a category of services, allowing fast call-off without re-tendering each engagement. Used well, it gives buyers leverage; used badly, it locks in stale pricing.",
        schema_headline="What Is a Frame Contract in IT Sourcing?",
        h1="What is a frame contract?",
        tagline="A master agreement that pre-negotiates terms so individual engagements can be called off in days, not months. The leverage tool when designed well; the lock-in trap when designed badly.",
        read_time="6 min read",
        answer="A frame contract (Rahmenvertrag in German) is a master agreement that pre-negotiates terms, conditions, and unit pricing for a category of services or goods. Individual engagements are then called off via a short ordering document referencing the frame contract, rather than re-negotiated each time. Frame contracts are common for IT consulting, staff augmentation, hardware procurement, and recurring software licensing.",
        body_md="""<h2>Why frame contracts exist.</h2>
<p>Re-tendering every engagement is expensive and slow. For categories with frequent, similar engagements — IT contractor staffing, hardware refreshes, recurring professional-services packages — running a competitive process every time produces transaction costs that exceed the savings any individual engagement could realise.</p>
<p>The frame contract pre-negotiates the heavy items (rate cards, T&amp;Cs, IP terms, liability caps, change-control mechanics) once, and reduces each subsequent engagement to a short ordering document — sometimes called a Statement of Work (SOW), call-off, or order — that references the frame.</p>
<h2>What's in a good frame contract.</h2>
<ul>
<li><strong>Rate card.</strong> Day rates by role and seniority, indexation rules, volume bands. Re-benchmarked at fixed intervals.</li>
<li><strong>Standard T&amp;Cs.</strong> Liability, IP, confidentiality, data protection, audit rights. Negotiated once, applied uniformly.</li>
<li><strong>Call-off mechanics.</strong> What an order document must contain, who can sign, how scope changes are handled, how invoices reconcile back to orders.</li>
<li><strong>Service-level baseline.</strong> Minimum SLAs that apply across all call-offs; specific SLAs can be raised in individual orders but not lowered.</li>
<li><strong>Volume commitment (or absence of one).</strong> Whether the buyer commits to minimum spend in exchange for the rate card. Most well-designed frames are non-exclusive: the buyer is not obliged to use the vendor.</li>
<li><strong>Term and review cadence.</strong> Typically 24–36 months with annual rate-card reviews and structured renegotiation triggers.</li>
</ul>
<h2>The two failure modes.</h2>
<h3>Stale pricing.</h3>
<p>A frame contract signed three years ago at then-market rates becomes a structural overpayment when market rates fall. Without indexation rules and review triggers built in, the frame is simply locking in a price that the buyer would never accept today.</p>
<p>Mitigation: rate-card review at fixed intervals (annual minimum), benchmark rights, and force-majeure-style triggers for material market shifts.</p>
<h3>Hidden exclusivity.</h3>
<p>Some frames create de facto exclusivity through volume-discount structures or operational lock-in (the vendor's tooling, processes, or staff become embedded). The buyer thinks they have flexibility; in practice, switching means restarting an engagement that has integrated deeply with internal teams.</p>
<p>Mitigation: explicit non-exclusivity clauses, second-source policies for material categories, deliberate use of multiple frame agreements within the same category.</p>
<h2>Frame contracts vs master service agreements.</h2>
<p>The terminology varies by jurisdiction. In Germany and Austria, "Rahmenvertrag" is the established term. In English-language usage, "Master Service Agreement" (MSA) covers the same concept and is used more widely in DACH for international vendors. Functionally, they are equivalent: a master document that pre-negotiates terms; individual engagements ordered against it.</p>
<h2>When to use a frame contract.</h2>
<ul>
<li>Recurring engagements with the same category of vendor (IT contractors, hardware, recurring SaaS).</li>
<li>Predictable annual spend within a band, but unpredictable per-engagement scope.</li>
<li>Categories where the cost of re-tendering each engagement materially exceeds the savings re-tendering would yield.</li>
</ul>
<h2>When not to use one.</h2>
<ul>
<li>Strategic platform decisions (single ERP, single hyperscaler) — these need bespoke contracts, not frame structures.</li>
<li>One-off transformations or programmes — the frame's overhead does not pay back.</li>
<li>Categories where market pricing moves faster than the frame can be renegotiated.</li>
</ul>
<h2>FAQ.</h2>
<h3>What is the German term for frame contract?</h3>
<p>Rahmenvertrag.</p>
<h3>How long should a frame contract run?</h3>
<p>Typically 24–36 months with annual rate-card reviews. Longer terms increase the lock-in risk; shorter terms erode the cost-saving benefit.</p>
<h3>Are frame contracts exclusive?</h3>
<p>Most well-designed frame contracts are non-exclusive — the buyer is not obliged to use the vendor for any specific volume. Exclusivity should be a deliberate, separately-negotiated trade-off, not a default.</p>""",
        faq=[
            ("What is a frame contract?", "A master agreement that pre-negotiates terms, conditions, and unit pricing for a category of services or goods, so individual engagements can be called off via a short ordering document. The German term is Rahmenvertrag; the English equivalent is often called a Master Service Agreement (MSA)."),
            ("How long should a frame contract run?", "Typically 24–36 months with annual rate-card reviews. Longer terms increase the lock-in risk; shorter terms erode the cost-saving benefit."),
            ("Are frame contracts exclusive?", "Most well-designed frame contracts are non-exclusive — the buyer is not obliged to use the vendor for any specific volume. Exclusivity should be a deliberate, separately-negotiated trade-off, not a default."),
        ],
        related=[("it-contract-management", "From signature to savings"),
                 ("it-rfp-guide", "The IT RFP guide"),
                 ("it-vendor-spend-optimization", "How to recover 10–40% of your IT budget")],
    ),

    dict(
        slug="strategic-vs-tactical-supplier",
        title="Strategic vs Tactical Supplier: The Difference That Matters",
        og_title="Strategic vs Tactical Supplier — Aventario",
        description="The difference between a strategic supplier and a tactical (or transactional) supplier, what each governance approach looks like, and the consequences of mismatching the two.",
        schema_headline="What Is the Difference Between a Strategic and Tactical Supplier?",
        h1="Strategic vs tactical supplier.",
        tagline="Two different jobs, two different management models. Mistaking one for the other reliably destroys value on both sides.",
        read_time="5 min read",
        answer="A strategic supplier is one whose capability is critical to the buyer's value chain, hard to replace, and worth investing relationship energy into. A tactical (or transactional) supplier is one delivering commodity-like services where the buyer-supplier relationship is short-term, replaceable, and price-driven. The two require fundamentally different management approaches, and the most common error is treating tactical suppliers strategically — wasting governance energy — or treating strategic suppliers tactically and losing the leverage that long-term commitment buys.",
        body_md="""<h2>What makes a supplier strategic.</h2>
<p>Three properties distinguish strategic suppliers from tactical ones:</p>
<ul>
<li><strong>Replaceability.</strong> A strategic supplier is hard to replace within an acceptable timeframe — either because their capability is differentiated, because the integration footprint is deep, or because the institutional knowledge they carry would be expensive to rebuild.</li>
<li><strong>Value enabled.</strong> A strategic supplier enables outcomes the buyer cannot easily produce internally or through alternatives. The relationship is partly about cost, but predominantly about capability.</li>
<li><strong>Time horizon.</strong> A strategic relationship is multi-year by design. The investment in joint planning, governance forums, and roadmap alignment pays back over a horizon that does not fit a transactional engagement.</li>
</ul>
<p>In a typical IT vendor portfolio, the strategic set is small: three to seven vendors out of an active list that may number 100–200.</p>
<h2>What makes a supplier tactical.</h2>
<p>The mirror image. Easily replaceable; commodity-like service; short time horizon; price the dominant factor. Examples in IT: contingent-workforce providers, commodity hardware suppliers, standardised software resellers, regional managed-service providers for non-critical services.</p>
<p>Tactical does not mean unimportant. It means the management model should optimise for transactional efficiency rather than relationship investment.</p>
<h2>The two governance models.</h2>
<table style="width:100%; border-collapse: collapse; margin: 1.5rem 0;">
<thead><tr><th style="text-align:left; padding: 0.5rem; border-bottom: 2px solid #88C9BE;">Dimension</th><th style="text-align:left; padding: 0.5rem; border-bottom: 2px solid #88C9BE;">Strategic</th><th style="text-align:left; padding: 0.5rem; border-bottom: 2px solid #88C9BE;">Tactical</th></tr></thead>
<tbody>
<tr><td style="padding: 0.5rem;">Forums</td><td style="padding: 0.5rem;">Three-tier governance, all levels active</td><td style="padding: 0.5rem;">Operational only; managerial as needed</td></tr>
<tr><td style="padding: 0.5rem;">Cadence</td><td style="padding: 0.5rem;">Weekly + monthly + quarterly</td><td style="padding: 0.5rem;">Quarterly or as-needed</td></tr>
<tr><td style="padding: 0.5rem;">Scorecard</td><td style="padding: 0.5rem;">Five-dimension (delivery, commercial, risk, relationship, innovation)</td><td style="padding: 0.5rem;">Two-dimension (delivery, commercial)</td></tr>
<tr><td style="padding: 0.5rem;">Contract</td><td style="padding: 0.5rem;">Bespoke, multi-year, deeply negotiated</td><td style="padding: 0.5rem;">Frame contract or standard T&amp;Cs; short term</td></tr>
<tr><td style="padding: 0.5rem;">Negotiation posture</td><td style="padding: 0.5rem;">Joint roadmap, mutual investment</td><td style="padding: 0.5rem;">Transactional, price-driven</td></tr>
<tr><td style="padding: 0.5rem;">Replacement</td><td style="padding: 0.5rem;">Multi-year transition</td><td style="padding: 0.5rem;">Months</td></tr>
</tbody>
</table>
<h2>The two failure modes.</h2>
<h3>Tactical-as-strategic.</h3>
<p>Investing strategic governance energy into vendors that are commodity-replaceable. Symptoms: too many quarterly business reviews, scorecards that nobody reads, relationship-management overhead consuming a disproportionate share of vendor management bandwidth. The fix: explicit segmentation discipline. The Kraljic Matrix is the standard tool.</p>
<h3>Strategic-as-tactical.</h3>
<p>Treating a vendor whose capability you actually depend on as if they were a commodity. Symptoms: short contracts, transactional negotiations, no joint roadmap, surprise when the vendor's roadmap diverges from yours. The fix: explicit recognition that some relationships are worth investing in even when the spend doesn't immediately justify it.</p>
<h2>FAQ.</h2>
<h3>How do you decide whether a supplier is strategic or tactical?</h3>
<p>Three tests: how hard would they be to replace, how much enablement value do they bring beyond their service, and what is the realistic time horizon of the relationship. Strategic suppliers score high on all three.</p>
<h3>Can a supplier move between strategic and tactical?</h3>
<p>Yes. Cloud hyperscaler relationships were transactional in 2015 and are strategic in 2026. Architectural and market changes routinely move suppliers between quadrants; the segmentation should be reviewed annually.</p>
<h3>How many strategic suppliers should an organisation have?</h3>
<p>Three to seven for most mid-cap IT portfolios. Fewer creates concentration risk; more dilutes the relationship investment that makes strategic relationships pay back.</p>""",
        faq=[
            ("What is the difference between a strategic and tactical supplier?", "A strategic supplier is critical to the buyer's value chain, hard to replace, and worth long-term relationship investment. A tactical supplier delivers commodity-like services where the relationship is short-term, replaceable, and price-driven."),
            ("Can a supplier move between strategic and tactical?", "Yes. Architectural and market changes routinely move suppliers between segments; the segmentation should be reviewed annually."),
            ("How many strategic suppliers should an organisation have?", "Three to seven for most mid-cap IT portfolios. Fewer creates concentration risk; more dilutes the relationship investment that makes strategic relationships pay back."),
        ],
        related=[("supplier-relationship-management", "SRM: the CRM you don't have for your vendors"),
                 ("it-vendor-consolidation", "From 47 vendors to 5 strategic partners"),
                 ("it-vendor-governance", "The framework that keeps vendors accountable")],
    ),

    dict(
        slug="vendor-sprawl",
        title="What Is Vendor Sprawl and Why Is It a Problem?",
        og_title="What Is Vendor Sprawl? — Aventario",
        description="Vendor sprawl is the gradual, unintended accumulation of suppliers in an organisation. It compounds quietly, drives 15–25% of vendor management overhead, and is rarely solvable through one-off rationalisation.",
        schema_headline="What Is Vendor Sprawl and Why Is It a Problem?",
        h1="What is vendor sprawl?",
        tagline="The residue of many reasonable local decisions, made over years, in the absence of a global view. Mostly invisible until it isn't.",
        read_time="5 min read",
        answer="Vendor sprawl is the gradual, unintended accumulation of an excessive number of active suppliers in an organisation. It compounds quietly over years as individual teams make reasonable local decisions without a global view of the vendor portfolio. Across DACH mid-cap IT organisations, the typical vendor portfolio carries between 80 and 220 active suppliers, with 15–25% of vendor management overhead consumed by the long tail of low-spend, low-strategic-value vendors.",
        body_md="""<h2>How vendor sprawl happens.</h2>
<p>It is not a procurement failure. It is the residue of many reasonable local decisions, made by competent people, in the absence of a portfolio view. A team needs a niche capability for a project; nobody at the time would have argued for routing the requirement through a strategic partner instead. Three years later, the project is gone but the vendor is still on the books, the contract auto-renewed, and nobody remembers who originally approved it.</p>
<p>Multiply by ten years and three reorganisations. The result is the average mid-cap IT vendor portfolio: somewhere between 80 and 220 active suppliers, with 60–70% of spend in the top ten and a long tail of 50–150 vendors collectively consuming 15–25% of spend and roughly the same proportion of vendor-management bandwidth.</p>
<h2>Why it matters.</h2>
<ul>
<li><strong>Overhead tax.</strong> Each vendor carries an administrative footprint regardless of spend: contract maintenance, finance reconciliation, security review, governance touch-points. The marginal cost of a small vendor is non-trivial.</li>
<li><strong>Negotiation leverage erosion.</strong> Spend that could be concentrated with strategic partners is fragmented across the long tail. Volume discounts the organisation should be earning, it isn't.</li>
<li><strong>Risk surface.</strong> Each vendor is a potential failure mode — security, financial, regulatory. A long tail of small vendors is an aggregate risk surface that nobody is actively managing.</li>
<li><strong>Knowledge fragmentation.</strong> Institutional knowledge gets scattered across many small relationships. When a vendor leaves, the relationship resets to zero.</li>
<li><strong>Governance capacity.</strong> Vendor management bandwidth is finite. Time spent on the long tail is time not spent on the strategic relationships where it would matter.</li>
</ul>
<h2>How to size your sprawl.</h2>
<p>Three numbers tell the story:</p>
<ol>
<li><strong>Total active vendors.</strong> Pull from finance: every supplier with spend &gt;€1k in the last 12 months. Compare to the procurement record. Expect 15–30% more than the procurement record shows.</li>
<li><strong>Long-tail concentration.</strong> Sort by spend descending. What percentage of spend is in vendors below the top 20? In healthy portfolios, less than 15%. In sprawled portfolios, 25–40%.</li>
<li><strong>Vendors-per-FTE.</strong> Total active vendors divided by vendor-management headcount. Anything above 30:1 means the long tail is functionally unmanaged.</li>
</ol>
<h2>How to fix it.</h2>
<p>Vendor consolidation is the structured response. Three principles:</p>
<ul>
<li><strong>Segment first, cut second.</strong> Use the Kraljic Matrix or equivalent. Strategic, leverage, bottleneck, routine. Different quadrants need different treatment.</li>
<li><strong>Route through strategic partners.</strong> Routine-quadrant work should flow through existing strategic relationships wherever the strategic partner can deliver. Most can deliver more than they're currently being asked to.</li>
<li><strong>Sunset, don't just cancel.</strong> A vendor on the books for three years has integrations, knowledge, and ongoing commitments. Plan the exit deliberately; don't just stop renewing.</li>
</ul>
<h2>Why one-off rationalisation rarely works.</h2>
<p>A vendor consolidation programme that cuts the portfolio from 180 to 60 will, without governance change, regrow to 140 within four years. The accretion mechanics that produced sprawl in the first place are still in place. Sustainable consolidation requires the underlying governance to change: a vendor-onboarding process that asks "could this be done by an existing strategic partner" before approving a new vendor, and a renewal-pipeline review that tests every renewal rather than letting it auto-roll.</p>
<h2>FAQ.</h2>
<h3>What is vendor sprawl?</h3>
<p>The gradual, unintended accumulation of an excessive number of active suppliers in an organisation, typically driven by individual local decisions made without a global portfolio view.</p>
<h3>How many IT vendors should an organisation have?</h3>
<p>The right number depends on size and complexity, but the structural target is to route 70–85% of in-scope IT services through five to seven strategic partners. The remaining long tail should be small and bounded.</p>
<h3>Is vendor sprawl a procurement problem?</h3>
<p>No, it's a governance problem. Procurement typically processes the request that creates a new vendor; the absence of a global onboarding gate is what allows sprawl to accumulate.</p>""",
        faq=[
            ("What is vendor sprawl?", "The gradual, unintended accumulation of an excessive number of active suppliers in an organisation, typically driven by individual local decisions made without a global portfolio view."),
            ("How many IT vendors should an organisation have?", "The right number depends on size and complexity, but the structural target is to route 70–85% of in-scope IT services through five to seven strategic partners. The remaining long tail should be small and bounded."),
            ("Is vendor sprawl a procurement problem?", "No, it's a governance problem. Procurement typically processes the request that creates a new vendor; the absence of a global onboarding gate is what allows sprawl to accumulate."),
        ],
        related=[("it-vendor-consolidation", "From 47 vendors to 5 strategic partners"),
                 ("it-vendor-management", "The complete guide to IT vendor management"),
                 ("it-vendor-governance", "The framework that keeps vendors accountable")],
    ),

    dict(
        slug="it-outsourcing-governance",
        title="What Is IT Outsourcing Governance?",
        og_title="What Is IT Outsourcing Governance? — Aventario",
        description="IT outsourcing governance is the buyer-side capability that holds an outsourcing provider accountable to the contract. The single most common reason outsourcing under-delivers: the buyer transferred execution but never built the governance to match.",
        schema_headline="What Is IT Outsourcing Governance?",
        h1="What is IT outsourcing governance?",
        tagline="The buyer-side capability that holds the outsourcing provider accountable. Frequently assumed to come with the deal; almost never does.",
        read_time="6 min read",
        answer="IT outsourcing governance is the buyer-side function that holds an outsourcing provider accountable to the contract — through structured forums, scorecards, escalation paths, and contractual rights such as audit and benchmark. It is the capability most outsourcing programmes fail to build deliberately, which is the single most common reason outsourcing arrangements under-deliver against their original business case.",
        body_md="""<h2>The assumption that breaks most outsourcing.</h2>
<p>The single most damaging assumption in IT outsourcing is that, having transferred the work, the buyer has also transferred the governance. They haven't. Outsourcing transfers execution; the buyer must build governance deliberately on its own side, often using a function that did not exist before the deal was signed.</p>
<p>Without that governance build, outsourcing arrangements decay on a predictable curve. Year one is usually fine — the deal is fresh, the vendor's account team is attentive, transition is the dominant focus. By month 18, the SLA reports start arriving green by default, the vendor's strategic energy has shifted to newer accounts, and the cost-saving business case starts quietly underperforming.</p>
<h2>What outsourcing governance actually consists of.</h2>
<ul>
<li><strong>Operational forum (weekly or fortnightly).</strong> Service-desk leads on both sides. Tickets, incidents, SLA breaches, change requests. The verification layer for SLA reports.</li>
<li><strong>Managerial forum (monthly).</strong> Service owners, account leads, finance representation. Scorecard, financial reconciliation, risk register. The layer where small problems get fixed before they escalate.</li>
<li><strong>Strategic forum (quarterly).</strong> CIO/sponsor on the buyer side; vendor executive on theirs. Roadmap, innovation, contract evolution, relationship health.</li>
<li><strong>Contract management.</strong> Active obligation tracking, renewal-pipeline calendar, benchmark schedule, audit-rights exercise.</li>
<li><strong>Performance verification.</strong> Independent reconciliation of vendor-reported SLAs against ticket-level data. Not done by the vendor; not negotiable.</li>
<li><strong>Risk register.</strong> Seven-category vendor risk view, reviewed monthly at managerial governance.</li>
</ul>
<h2>How much governance capacity do you need?</h2>
<p>For a tier-1 strategic outsourcing relationship — say, an infrastructure outsourcing deal worth €20–50M annually — the governance capability is typically 2–4 FTE on the buyer side, plus part-time engagement from finance, security, legal, and the CIO. This sounds expensive until you compare it to the value left on the table when governance is absent: usually 5–15% of contract value annually.</p>
<p>For mid-sized outsourcing relationships, fractional governance — either a smaller in-house team or an outsourced VM-as-a-Service capability — is the typical answer.</p>
<h2>The first 90 days.</h2>
<p>The most expensive missed window in outsourcing is the first 90 days post-go-live. The transition is over, the vendor's transition team is rolling off, and the steady-state account team is taking over. This is when SLA baselines get set, governance cadences get established, and the de facto operating model gets codified — often through what doesn't get challenged rather than through what does. A buyer that does not invest heavily in governance during this window cedes the operating model to the vendor.</p>
<h2>Common governance failure modes.</h2>
<ul>
<li><strong>Single-tier governance.</strong> Only the quarterly strategic forum exists. Everything either gets stuck operationally or escalates straight to the CIO.</li>
<li><strong>Vendor-led reporting.</strong> SLA reports arrive from the vendor, get accepted without verification, and harden into the agreed truth.</li>
<li><strong>No benchmark refresh.</strong> The original deal pricing was market when signed. Three years later, it isn't. Without a benchmark refresh, nobody knows.</li>
<li><strong>Scope drift unmanaged.</strong> Original SOW for €X. Three change requests later, the run-rate is 1.6× the original, and nobody can fully reconstruct the path.</li>
<li><strong>Governance underweighted at signature.</strong> The negotiation team focused on price; the governance terms (audit, benchmark, exit) were given away. The relationship cannot be fixed without those rights.</li>
</ul>
<h2>FAQ.</h2>
<h3>What is IT outsourcing governance?</h3>
<p>The structured set of forums, scorecards, escalation paths, and contractual rights that hold an IT outsourcing provider accountable to the performance the contract promises.</p>
<h3>Who owns outsourcing governance on the buyer side?</h3>
<p>Most commonly the Vendor Management Office (VMO) or an equivalent function reporting into the CIO or COO. For larger deals, dedicated governance leads sit alongside the operational service owners.</p>
<h3>What happens to outsourcing performance without governance?</h3>
<p>It decays on a predictable curve. Vendor account-team attention shifts to newer accounts; SLA reporting drifts toward optimistic; the original business case underperforms by 15–30% within 18 months.</p>""",
        faq=[
            ("What is IT outsourcing governance?", "The buyer-side function that holds an outsourcing provider accountable to the contract — through structured forums, scorecards, escalation paths, and contractual rights such as audit and benchmark."),
            ("Who owns outsourcing governance on the buyer side?", "Most commonly the Vendor Management Office (VMO) or an equivalent function reporting into the CIO or COO. For larger deals, dedicated governance leads sit alongside operational service owners."),
            ("What happens to outsourcing performance without governance?", "It decays on a predictable curve. Vendor account-team attention shifts to newer accounts; SLA reporting drifts toward optimistic; the original business case underperforms by 15–30% within 18 months."),
        ],
        related=[("it-vendor-governance", "The framework that keeps vendors accountable"),
                 ("it-vendor-management", "The complete guide to IT vendor management"),
                 ("it-contract-management", "From signature to savings")],
    ),

    dict(
        slug="process-mining-it",
        title="What Is Process Mining and How Is It Used in IT?",
        og_title="What Is Process Mining? — Aventario",
        description="Process mining reconstructs how a process actually behaves from system event logs, rather than from how someone says it works. The two are reliably different — and the gap is where 10–20% of process volume tends to be wasted.",
        schema_headline="What Is Process Mining and How Is It Used in IT?",
        h1="What is process mining?",
        tagline="The discipline of reconstructing actual process behaviour from system event logs. Reliably reveals that the documented process and the real process are two different things.",
        read_time="6 min read",
        answer="Process mining is the practice of reconstructing how a business or IT process actually behaves by analysing system event logs — incident records, ERP transactions, ITSM tickets, workflow timestamps — rather than relying on how the process is documented. The technique reliably reveals that the documented process and the actual process diverge, with 10–20% of process volume typically running through paths that add no value.",
        body_md="""<h2>What process mining does.</h2>
<p>Every system that handles a business process generates events: a ticket is created, assigned, escalated, resolved; a purchase order is raised, approved, fulfilled, invoiced; a change request is submitted, reviewed, deployed. Each event has a timestamp, an actor, and a state. Process mining tools ingest these events, link them by case ID, and reconstruct the actual flow each case took through the process.</p>
<p>The output is a process map drawn from data — not from documentation, not from interviews, not from how anyone says the process works. The map shows every variant of the path, the frequency of each, the average duration of each step, and the rework loops.</p>
<h2>What it typically reveals.</h2>
<p>The documented process versus the actual process are reliably different. A process documented as a five-step incident-management workflow may, in the event log, involve 23 distinct paths, of which the documented one accounts for only 38% of cases. The other 62% — the long tail of variants — is where the work to investigate sits.</p>
<p>Common findings:</p>
<ul>
<li><strong>Rework loops.</strong> Cases that go back to a previous step. Often signal a quality or training problem upstream.</li>
<li><strong>Manual workarounds.</strong> Process variants that exist because the standard path doesn't handle a real-world case the documented process pretends doesn't exist.</li>
<li><strong>Approval cycles.</strong> Cases held for approval by people who, on inspection, are not actually adding judgement to the decision.</li>
<li><strong>Duplicate work.</strong> The same activity being performed in two systems by two teams, neither aware of the other.</li>
<li><strong>Bottlenecks.</strong> The step that consistently takes 5x the average. Usually a specific person, a specific system, or a specific approval gate.</li>
</ul>
<h2>Where it's useful.</h2>
<ul>
<li><strong>Operational efficiency.</strong> Identifying the 10–20% of process volume that doesn't add value. The starting point for most efficiency programmes.</li>
<li><strong>Automation candidate selection.</strong> Process mining identifies which processes are stable enough, standardised enough, and high-volume enough to be worth automating.</li>
<li><strong>Compliance auditing.</strong> Detecting cases that bypassed controls, approvals that weren't recorded, segregation-of-duties violations.</li>
<li><strong>Vendor performance verification.</strong> Reconciling vendor-reported SLAs against actual ticket-level event data. The most common gap we find in outsourcing arrangements.</li>
<li><strong>Process harmonisation.</strong> Comparing how the same process runs in different geographies or business units. Often reveals that "the global standard" is theory rather than practice.</li>
</ul>
<h2>Tools and capability.</h2>
<p>The dedicated process-mining platforms — Celonis is the category leader, alongside Signavio (now SAP), UiPath Process Mining, Software AG ARIS, and several others — handle large event-log volumes and produce sophisticated visualisations. For smaller-scale work, modern data tooling (dbt, Python pandas, BI platforms) can produce meaningful process-mining analysis without specialised software.</p>
<p>The interesting capability in 2026 is not the tool but the analyst skill: someone who understands the business process, knows what to look for in the variants, and can translate process-mining findings into actionable changes. The tool produces the map; the analyst produces the insight.</p>
<h2>Common pitfalls.</h2>
<ul>
<li><strong>Bad data.</strong> Process mining is only as good as the event log. Missing timestamps, inconsistent case IDs, unsynchronised system clocks — all produce maps that look authoritative but are wrong.</li>
<li><strong>Tool-led rather than question-led.</strong> "We have Celonis, what should we do with it" is the wrong starting point. "We need to know why P1 incident resolution time has drifted" is the right one.</li>
<li><strong>Mistaking variation for waste.</strong> Some process variation is legitimate. The analyst's job is to distinguish necessary variation from accidental complexity.</li>
</ul>
<h2>FAQ.</h2>
<h3>What is process mining?</h3>
<p>The practice of reconstructing actual process behaviour from system event logs, rather than from documented process maps or interviews.</p>
<h3>What does process mining typically find?</h3>
<p>That the documented process and the actual process are reliably different. Typical findings: 10–20% of process volume runs through paths that add no value (rework loops, unnecessary approvals, manual workarounds, duplicate work).</p>
<h3>What tools are used for process mining?</h3>
<p>Dedicated platforms include Celonis (category leader), Signavio (SAP), UiPath Process Mining, and Software AG ARIS. For smaller-scale analysis, modern data tooling can produce meaningful results without specialised software.</p>""",
        faq=[
            ("What is process mining?", "The practice of reconstructing actual process behaviour from system event logs, rather than from documented process maps or interviews."),
            ("What does process mining typically find?", "That the documented process and the actual process are reliably different. Typical findings: 10–20% of process volume runs through paths that add no value, including rework loops, unnecessary approvals, manual workarounds, and duplicate work."),
            ("What tools are used for process mining?", "Dedicated platforms include Celonis (category leader), Signavio (SAP), UiPath Process Mining, and Software AG ARIS. For smaller-scale analysis, modern data tooling can produce meaningful results without specialised software."),
        ],
        related=[("it-operational-excellence", "Find and eliminate the 20% your processes waste"),
                 ("it-vendor-governance", "The framework that keeps vendors accountable"),
                 ("it-vendor-management", "The complete guide to IT vendor management")],
    ),
]


def render(p, gradient):
    related_html = "\n".join(
        f'                    <li><a href="{slug}">{label}</a></li>'
        for slug, label in p["related"]
    )
    body = f'            <div class="answer-box"><p>{p["answer"]}</p></div>\n{p["body_md"]}'
    html = TEMPLATE.format(
        title=p["title"],
        og_title=p["og_title"],
        description=p["description"],
        slug=p["slug"],
        gradient=gradient,
        schema_headline=p["schema_headline"],
        h1=p["h1"],
        tagline=p["tagline"],
        read_time=p["read_time"],
        body=body,
        related_html=related_html,
        faq_jsonld=faq_jsonld(p["faq"]),
    )
    (OUT / f'{p["slug"]}.html').write_text(html, encoding="utf-8")
    print(f"wrote {p['slug']}.html")


for i, p in enumerate(FAQS):
    render(p, GRADIENTS[i])

print(f"\n{len(FAQS)} FAQ pages generated.")
