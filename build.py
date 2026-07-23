#!/usr/bin/env python3
"""
Static site builder for the Nelson FPV drone website.

No Node, no dependencies — pure Python 3 stdlib. Matches the pipeline used by
the other sites in ~/Sites: assemble pages from partials, write the result into
a *-netlify-deploy folder that Netlify publishes as-is (no build command).

Two page sources:
  - pages/*.html   : bespoke, hand-authored pages (e.g. the homepage) with
                     leading `<!-- key: value -->` meta comments + body.
  - content/pages.json : data-driven inner pages (services, about, contact,
                     guide) rendered through a shared layout with per-page
                     structured data (Breadcrumb / Service / Article / FAQ).

SEO is a first-class concern: per-page title/description/keywords/canonical,
JSON-LD, generated sitemap.xml + robots.txt, geo meta, cache-busted assets.

Usage:
    python3 build.py
    cd nelson-drone-netlify-deploy && python3 -m http.server 4321
"""
from __future__ import annotations

import html
import json
import re
import shutil
from datetime import datetime
from pathlib import Path

# ---- Site config -----------------------------------------------------------
# PLACEHOLDER values — swap for the real ones before launch.
# Brand: FORTYONE SOUTH — Drone Film Studio (per spec v1.1). Domain unregistered.
SITE_URL = "https://www.fortyonesouth.co.nz"
PHONE_TEL = "+6430000000"
PHONE_DISPLAY = "03 000 0000"
EMAIL = "hello@fortyonesouth.co.nz"
BUSINESS_ID = SITE_URL + "/#business"

ROOT = Path(__file__).resolve().parent
PAGES = ROOT / "pages"
PARTIALS = ROOT / "partials"
STATIC = ROOT / "static"
CONTENT = ROOT / "content"
DEPLOY = ROOT / "nelson-drone-netlify-deploy"

META_RE = re.compile(r"^<!--\s*(\w+)\s*:\s*(.*?)\s*-->\s*$")
SITEMAP_PRIORITY = {"index.html": "1.0", "services.html": "0.9", "contact.html": "0.9"}

SERVICE_SLUGS = {
    "services", "real-estate-drone-video-nelson", "venue-hospitality-drone-video",
    "tourism-adventure-drone-video-nelson", "wedding-event-drone-video-nelson",
    "business-social-content-nelson",
}
EYEBROW = {
    "services": "What we make", "about": "About the studio",
    "contact": "Get in touch", "drone-rules-nelson": "Guide",
}
AREA_SERVED = [
    {"@type": "City", "name": "Nelson"},
    {"@type": "AdministrativeArea", "name": "Tasman"},
    {"@type": "AdministrativeArea", "name": "Marlborough"},
]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def esc(text: str) -> str:
    return html.escape(text or "", quote=True)


def paras(text: str) -> str:
    """Turn a blob with blank-line/newline breaks into <p> elements."""
    blocks = [b.strip() for b in re.split(r"\n\s*\n|\n", text or "") if b.strip()]
    return "".join(f"<p>{esc(b)}</p>" for b in blocks)


def parse_page(raw: str) -> tuple[dict[str, str], str]:
    """Split leading `<!-- key: value -->` meta comments from the body."""
    meta: dict[str, str] = {}
    lines = raw.splitlines(keepends=True)
    i = 0
    for line in lines:
        stripped = line.strip()
        m = META_RE.match(stripped)
        if m:
            meta[m.group(1).lower()] = m.group(2).strip()
            i += 1
        elif stripped == "":
            i += 1
        else:
            break
    return meta, "".join(lines[i:])


def canonical_for(slug_html: str, meta: dict[str, str]) -> str:
    if meta.get("canonical"):
        return meta["canonical"]
    if slug_html == "index.html":
        return SITE_URL + "/"
    return f"{SITE_URL}/{slug_html}"


def json_ld(obj: dict) -> str:
    return ('<script type="application/ld+json">\n'
            + json.dumps(obj, ensure_ascii=False, indent=2)
            + "\n</script>")


# ---- Inner-page rendering --------------------------------------------------

def render_sections(sections: list) -> str:
    out = []
    for s in sections:
        block = [f"<div class=\"prose-block reveal\"><h2>{esc(s['heading'])}</h2>",
                 f"<p>{esc(s['body'])}</p>"]
        if s.get("bullets"):
            block.append('<ul class="tick-list">'
                         + "".join(f"<li>{esc(b)}</li>" for b in s["bullets"])
                         + "</ul>")
        block.append("</div>")
        out.append("".join(block))
    return "".join(out)


def render_faqs(faqs: list) -> str:
    items = "".join(
        f'<details class="faq-item"><summary>{esc(f["q"])}</summary>'
        f'<div class="faq-a"><p>{esc(f["a"])}</p></div></details>'
        for f in faqs
    )
    return (
        '<section class="section faq"><div class="container">'
        '<div class="section-head reveal"><p class="eyebrow">FAQ</p>'
        '<h2 class="section-title">Questions &amp; answers</h2></div>'
        f'<div class="faq-list reveal">{items}</div></div></section>'
    )


def render_related(links: list) -> str:
    if not links:
        return ""
    lis = "".join(f'<li><a href="{esc(l["href"])}">{esc(l["text"])} <span aria-hidden="true">→</span></a></li>'
                  for l in links)
    return (
        '<section class="section related"><div class="container">'
        '<div class="section-head reveal"><p class="eyebrow">Keep exploring</p>'
        '<h2 class="section-title">Where to next</h2></div>'
        f'<ul class="related-links reveal">{lis}</ul></div></section>'
    )


def render_book_band(cta_text: str, is_contact: bool) -> str:
    calendar = (
        '<div class="book-calendar" aria-label="Booking calendar placeholder">'
        '<span class="ph-tag">Live booking calendar · Cal.com — syncs both ways with Google Calendar</span>'
        '</div>' if is_contact else ""
    )
    return (
        '<section class="section book" id="book"><div class="container book-inner reveal">'
        '<h2 class="book-title">Let’s make your film</h2>'
        f'<p class="book-sub">{esc(cta_text)}</p>'
        '<div class="book-actions">'
        f'<a class="btn btn-primary btn-lg" href="tel:{PHONE_TEL}">'
        '<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M6.6 10.8a15.5 15.5 0 0 0 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1A17 17 0 0 1 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.2.2 2.4.6 3.6.1.4 0 .8-.3 1z"/></svg>'
        f'Call {PHONE_DISPLAY}</a>'
        f'<a class="btn btn-ghost btn-lg" href="mailto:{EMAIL}?subject=Drone%20film%20enquiry">Send an enquiry</a>'
        '</div>'
        f'{calendar}</div></section>'
    )


def render_inner_page(data: dict) -> tuple[dict, str]:
    slug = data["slug"]
    slug_html = f"{slug}.html"
    canonical = canonical_for(slug_html, {})
    is_contact = slug == "contact"
    crumb = data["title"].split(" | ")[0].split(" — ")[0]

    # Hero CTAs
    if is_contact:
        hero_cta = (
            f'<a class="btn btn-primary btn-lg" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a>'
            f'<a class="btn btn-ghost btn-lg" href="mailto:{EMAIL}?subject=Drone%20film%20enquiry">Send an enquiry</a>'
        )
    else:
        hero_cta = (
            '<a class="btn btn-primary btn-lg" href="/contact.html">Get a quote</a>'
            f'<a class="btn btn-ghost btn-lg" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a>'
        )

    body = [
        '<section class="page-hero"><div class="container">',
        '<nav class="crumbs" aria-label="Breadcrumb">'
        f'<a href="/">Home</a> <span aria-hidden="true">/</span> <span>{esc(crumb)}</span></nav>',
        f'<p class="eyebrow">{esc(EYEBROW.get(slug, "Service"))}</p>',
        f'<h1 class="page-title">{esc(data["h1"])}</h1>',
        f'<div class="page-intro">{paras(data["intro"])}</div>',
        f'<div class="page-hero-cta">{hero_cta}</div>',
        '</div></section>',
        '<section class="section"><div class="container page-prose">',
        render_sections(data.get("sections", [])),
        '</div></section>',
        render_related(data.get("internal_links", [])),
        render_faqs(data["faqs"]) if data.get("faqs") else "",
        render_book_band(data.get("cta", "Get in touch for a quote."), is_contact),
    ]

    # ---- Structured data ----
    graph = [{
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE_URL + "/"},
            {"@type": "ListItem", "position": 2, "name": crumb, "item": canonical},
        ],
    }]
    if slug in SERVICE_SLUGS:
        graph.append({
            "@context": "https://schema.org", "@type": "Service",
            "name": crumb, "serviceType": data.get("primary_keyword", ""),
            "provider": {"@id": BUSINESS_ID}, "areaServed": AREA_SERVED, "url": canonical,
        })
    if slug == "drone-rules-nelson":
        graph.append({
            "@context": "https://schema.org", "@type": "Article",
            "headline": data["h1"], "description": data["meta_description"],
            "author": {"@id": BUSINESS_ID}, "publisher": {"@id": BUSINESS_ID},
            "mainEntityOfPage": canonical,
        })
    if data.get("faqs"):
        graph.append({
            "@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [
                {"@type": "Question", "name": f["q"],
                 "acceptedAnswer": {"@type": "Answer", "text": f["a"]}}
                for f in data["faqs"]
            ],
        })
    body.extend(json_ld(g) for g in graph)

    meta = {
        "title": data["title"],
        "description": data["meta_description"],
        "keywords": data.get("keywords", ""),
        "body_class": "inner",
    }
    return meta, "".join(body)


# ---- Build -----------------------------------------------------------------

def build() -> None:
    base = read(PARTIALS / "base.html")
    now = datetime.now()
    year, today, version = str(now.year), now.strftime("%Y-%m-%d"), now.strftime("%Y%m%d%H%M%S")

    if DEPLOY.exists():
        shutil.rmtree(DEPLOY)
    DEPLOY.mkdir(parents=True)
    shutil.copytree(STATIC, DEPLOY / "static")
    for name in ("favicon.svg", "_redirects"):
        if (ROOT / name).exists():
            shutil.copy2(ROOT / name, DEPLOY / name)

    sitemap_pages: list[tuple[str, str]] = []

    def emit(slug_html: str, meta: dict, body: str) -> None:
        canonical = canonical_for(slug_html, meta)
        htmlout = (
            base.replace("{{title}}", esc(meta.get("title", "Nelson FPV Drone Films")))
            .replace("{{description}}", esc(meta.get("description", "")))
            .replace("{{keywords}}", esc(meta.get("keywords", "")))
            .replace("{{canonical}}", canonical)
            .replace("{{og_image}}", meta.get("og_image", "/static/assets/og.svg"))
            .replace("{{body_class}}", meta.get("body_class", ""))
            .replace("{{site_url}}", SITE_URL)
            .replace("{{content}}", body)
            .replace("{{year}}", year)
            .replace("{{v}}", version)
        )
        (DEPLOY / slug_html).write_text(htmlout, encoding="utf-8")
        sitemap_pages.append((slug_html, canonical))
        print(f"  built {slug_html}")

    # 1) Bespoke pages (homepage). These already contain final HTML in the body,
    #    so their meta values are used verbatim (esc() is safe/idempotent here).
    for page in sorted(PAGES.glob("*.html")):
        meta, body = parse_page(read(page))
        emit(page.name, meta, body)

    # 2) Data-driven inner pages
    pages_json = CONTENT / "pages.json"
    if pages_json.exists():
        for data in json.loads(read(pages_json)):
            meta, body = render_inner_page(data)
            emit(f"{data['slug']}.html", meta, body)

    # 3) sitemap + robots
    rows = []
    for slug_html, canonical in sitemap_pages:
        prio = SITEMAP_PRIORITY.get(slug_html, "0.7")
        rows.append(f"  <url>\n    <loc>{canonical}</loc>\n    <lastmod>{today}</lastmod>\n"
                    f"    <changefreq>monthly</changefreq>\n    <priority>{prio}</priority>\n  </url>")
    (DEPLOY / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(rows) + "\n</urlset>\n", encoding="utf-8")
    (DEPLOY / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n", encoding="utf-8")

    print(f"Done. {len(sitemap_pages)} pages + sitemap.xml + robots.txt -> {DEPLOY.name}/")


if __name__ == "__main__":
    build()
