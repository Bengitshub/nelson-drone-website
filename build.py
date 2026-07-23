#!/usr/bin/env python3
"""
Static site builder for the Nelson FPV drone website.

No Node, no dependencies — pure Python 3 stdlib. Matches the pipeline used by
the other sites in ~/Sites: assemble pages from partials, write the result into
a *-netlify-deploy folder that Netlify publishes as-is (no build command).

SEO is a first-class concern here:
  - per-page <title>, meta description, keywords, canonical URL
  - site-wide LocalBusiness JSON-LD (in partials/base.html) + per-page schema
  - generated sitemap.xml and robots.txt
  - geo meta + cache-busted assets

Usage:
    python3 build.py
    cd nelson-drone-netlify-deploy && python3 -m http.server 4321
"""
from __future__ import annotations

import re
import shutil
from datetime import datetime
from pathlib import Path

# ---- Site config -----------------------------------------------------------
# PLACEHOLDER domain — swap for the real one once chosen (.nz / .co.nz).
SITE_URL = "https://www.skyframe.nz"

ROOT = Path(__file__).resolve().parent
PAGES = ROOT / "pages"
PARTIALS = ROOT / "partials"
STATIC = ROOT / "static"
DEPLOY = ROOT / "nelson-drone-netlify-deploy"

META_RE = re.compile(r"^<!--\s*(\w+)\s*:\s*(.*?)\s*-->\s*$")

# Homepage priority in the sitemap; everything else defaults lower.
SITEMAP_PRIORITY = {"index.html": "1.0"}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


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
            i += 1  # allow blank lines between meta and body
        else:
            break
    return meta, "".join(lines[i:])


def canonical_for(slug: str, meta: dict[str, str]) -> str:
    if meta.get("canonical"):
        return meta["canonical"]
    if slug == "index.html":
        return SITE_URL + "/"
    return f"{SITE_URL}/{slug}"


def write_sitemap(pages: list[tuple[str, str]], today: str) -> None:
    rows = []
    for slug, canonical in pages:
        prio = SITEMAP_PRIORITY.get(slug, "0.7")
        rows.append(
            f"  <url>\n    <loc>{canonical}</loc>\n"
            f"    <lastmod>{today}</lastmod>\n"
            f"    <changefreq>monthly</changefreq>\n"
            f"    <priority>{prio}</priority>\n  </url>"
        )
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(rows)
        + "\n</urlset>\n"
    )
    (DEPLOY / "sitemap.xml").write_text(xml, encoding="utf-8")


def write_robots() -> None:
    txt = (
        "User-agent: *\n"
        "Allow: /\n\n"
        f"Sitemap: {SITE_URL}/sitemap.xml\n"
    )
    (DEPLOY / "robots.txt").write_text(txt, encoding="utf-8")


def build() -> None:
    base = read(PARTIALS / "base.html")
    now = datetime.now()
    year = str(now.year)
    today = now.strftime("%Y-%m-%d")
    version = now.strftime("%Y%m%d%H%M%S")  # cache-bust asset URLs each build

    # Fresh deploy folder
    if DEPLOY.exists():
        shutil.rmtree(DEPLOY)
    DEPLOY.mkdir(parents=True)

    # Copy static assets (css/js/assets) -> /static
    shutil.copytree(STATIC, DEPLOY / "static")

    # Copy any root-level files that must sit at site root (favicon, etc.)
    for name in ("favicon.svg", "_redirects"):
        src = ROOT / name
        if src.exists():
            shutil.copy2(src, DEPLOY / name)

    sitemap_pages: list[tuple[str, str]] = []
    for page in sorted(PAGES.glob("*.html")):
        meta, body = parse_page(read(page))
        canonical = canonical_for(page.name, meta)
        html = (
            base.replace("{{title}}", meta.get("title", "Nelson FPV Drone Films"))
            .replace("{{description}}", meta.get("description", ""))
            .replace("{{keywords}}", meta.get("keywords", ""))
            .replace("{{canonical}}", canonical)
            .replace("{{og_image}}", meta.get("og_image", "/static/assets/og.svg"))
            .replace("{{body_class}}", meta.get("body_class", ""))
            .replace("{{site_url}}", SITE_URL)
            .replace("{{content}}", body)
            .replace("{{year}}", year)
            .replace("{{v}}", version)
        )
        (DEPLOY / page.name).write_text(html, encoding="utf-8")
        sitemap_pages.append((page.name, canonical))
        print(f"  built {page.name}")

    write_sitemap(sitemap_pages, today)
    write_robots()
    print(f"Done. {len(sitemap_pages)} page(s) + sitemap.xml + robots.txt -> {DEPLOY.name}/")


if __name__ == "__main__":
    build()
