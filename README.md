# Nelson Drone Co. — website

Static marketing site for **Nelson Drone Co.**, a one-pilot aerial photography
and video business serving Nelson, Tasman and Marlborough (NZ).
The business and copy decisions live in [`docs/BRIEF.md`](docs/BRIEF.md) — the
owner's brief. Built the same way as the other sites in `~/Sites`: a small
Python builder assembles pages from partials into a deploy folder that Netlify
serves as-is. **No Node required.**

## The business model (short)

Photo / video-clip / short-highlight / progress packages from NZ$245–695
("from" pricing, written quote before every flight). Booking is a **request**
via a Cal.com embed (requires confirmation) synced to Google Calendar.
Invoicing is done with **Stripe** after delivery — no payment on the site.

## Stack

- Hand-written HTML/CSS/vanilla JS — no framework.
- `build.py` (Python 3 stdlib) assembles `pages/*.html` + `partials/base.html`
  → `nelson-drone-netlify-deploy/`.
- All pages are bespoke files in `pages/` with `<!-- key: value -->` meta
  headers. (The old `content/pages.json` pipeline was removed.)

## Layout

```
docs/BRIEF.md                  # owner's brief — business + copy source of truth
build.py                       # assembles the site
partials/base.html             # shared shell (head, header, footer, LocalBusiness schema)
pages/*.html                   # per-page meta + body (index, services, work, about, book, privacy, terms)
static/css, static/js, static/assets
nelson-drone-netlify-deploy/   # BUILD OUTPUT — committed, published by Netlify
```

## Build & preview

```bash
python3 build.py
cd nelson-drone-netlify-deploy && python3 -m http.server 4321
# open http://localhost:4321
```

## Deploy

Commit and push to `main` (`git@github.com:Bengitshub/nelson-drone-website.git`).
Netlify publishes `nelson-drone-netlify-deploy/` with no build command
(see `netlify.toml`).

## SEO

Per page: title/description/keywords/canonical + JSON-LD (LocalBusiness
site-wide; BreadcrumbList per page; Service + OfferCatalog on /services;
FAQPage where there's an FAQ), generated `sitemap.xml` + `robots.txt`,
geo meta, cache-busted assets.

## Before launch — must be real, not placeholder

- [ ] Register domain (`nelsondrone.co.nz` preferred) → set `SITE_URL` in build.py
- [ ] Legal entity + GST status confirmed; review privacy/terms drafts with a professional
- [ ] Real contact details (footer + JSON-LD in `partials/base.html`, tel/mailto links in pages)
- [ ] Verified credential/insurance wording only — nothing invented
- [ ] Four test shoots → real portfolio media replaces every `Sample`/`Portfolio Project` placeholder
- [ ] Cal.com account + Google Calendar → replace `.embed-fallback` on /book (see CAL_EMBED comment)
- [ ] Stripe account for invoicing
- [ ] Real OG image (1200×630 raster) → update `og_image`
- [ ] Google Business Profile (service-area business, matching NAP)
- [ ] Submit sitemap in Search Console

**The site launches on footage, not code.**
