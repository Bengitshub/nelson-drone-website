#!/usr/bin/env python3
"""
Static site builder for the Nelson FPV drone website.

No Node, no dependencies — pure Python 3 stdlib. Matches the pipeline used by
the other sites in ~/Sites: assemble pages from partials, write the result into
a *-netlify-deploy folder that Netlify publishes as-is (no build command).

Usage:
    python3 build.py            # build into nelson-drone-netlify-deploy/
    python3 -m http.server ...  # (run separately) preview the deploy folder
"""
from __future__ import annotations

import re
import shutil
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PAGES = ROOT / "pages"
PARTIALS = ROOT / "partials"
STATIC = ROOT / "static"
DEPLOY = ROOT / "nelson-drone-netlify-deploy"

META_RE = re.compile(r"^<!--\s*(\w+)\s*:\s*(.*?)\s*-->\s*$", re.MULTILINE)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_page(raw: str) -> tuple[dict[str, str], str]:
    """Split leading `<!-- key: value -->` meta comments from the body."""
    meta: dict[str, str] = {}
    body_start = 0
    for line in raw.splitlines(keepends=True):
        m = META_RE.match(line.strip() + ("\n" if not line.endswith("\n") else ""))
        if m:
            meta[m.group(1).lower()] = m.group(2).strip()
            body_start += len(line)
        elif line.strip() == "":
            body_start += len(line)  # skip blank lines between meta and body
        else:
            break
    return meta, raw[body_start:]


def build() -> None:
    base = read(PARTIALS / "base.html")
    now = datetime.now()
    year = str(now.year)
    version = now.strftime("%Y%m%d%H%M%S")  # cache-bust asset URLs each build

    # Fresh deploy folder
    if DEPLOY.exists():
        shutil.rmtree(DEPLOY)
    DEPLOY.mkdir(parents=True)

    # Copy static assets (css/js/assets) -> /static
    shutil.copytree(STATIC, DEPLOY / "static")

    # Copy any root-level files that must sit at site root (favicon, etc.)
    for name in ("favicon.svg", "robots.txt", "_redirects"):
        src = ROOT / name
        if src.exists():
            shutil.copy2(src, DEPLOY / name)

    count = 0
    for page in sorted(PAGES.glob("*.html")):
        meta, body = parse_page(read(page))
        html = (
            base.replace("{{title}}", meta.get("title", "Nelson FPV Drone Films"))
            .replace("{{description}}", meta.get("description", ""))
            .replace("{{og_image}}", meta.get("og_image", "/static/assets/og.svg"))
            .replace("{{body_class}}", meta.get("body_class", ""))
            .replace("{{content}}", body)
            .replace("{{year}}", year)
            .replace("{{v}}", version)
        )
        out = DEPLOY / page.name
        out.write_text(html, encoding="utf-8")
        count += 1
        print(f"  built {page.name}")

    print(f"Done. {count} page(s) -> {DEPLOY.relative_to(ROOT)}/")


if __name__ == "__main__":
    build()
