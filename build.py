#!/usr/bin/env python3
"""
Static site builder for Haven Aerials — havenaerials.nz (placeholder domain).

Pure Python 3 stdlib, no Node. Assembles bespoke pages from a shared shell and
writes the finished site into a folder Netlify publishes as-is (no build
command). Every page is a hand-authored file in pages/*.html: leading
`<!-- key: value -->` meta comments, then the body markup. Structured data
(BreadcrumbList / Service / FAQPage) lives inside each page; the site-wide
LocalBusiness schema lives in partials/base.html.

Usage:
    python3 build.py
    cd haven-aerials-netlify-deploy && python3 -m http.server 4321
"""
from __future__ import annotations

import html
import re
import shutil
from datetime import datetime
from pathlib import Path

# ---- Site config -----------------------------------------------------------
# PLACEHOLDER domain — register havenaerials.nz before launch, then update.
SITE_URL = "https://www.havenaerials.nz"

ROOT = Path(__file__).resolve().parent
PAGES = ROOT / "pages"
PARTIALS = ROOT / "partials"
STATIC = ROOT / "static"
DEPLOY = ROOT / "haven-aerials-netlify-deploy"

META_RE = re.compile(r"^<!--\s*(\w+)\s*:\s*(.*?)\s*-->\s*$")
SITEMAP_PRIORITY = {
    "index.html": "1.0",
    "services.html": "0.9",
    "book.html": "0.9",
    "work.html": "0.8",
    "about.html": "0.7",
    "privacy.html": "0.3",
    "terms.html": "0.3",
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def esc(text: str) -> str:
    return html.escape(text or "", quote=True)


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

    for page in sorted(PAGES.glob("*.html")):
        meta, body = parse_page(read(page))
        slug_html = page.name
        canonical = canonical_for(slug_html, meta)
        htmlout = (
            base.replace("{{title}}", esc(meta.get("title", "Haven Aerials")))
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

    # sitemap + robots
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
