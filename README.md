# Haven Aerials — website

Marketing site for **Haven Aerials**, a one-pilot drone photography and
videography business serving Nelson, Tasman and Marlborough (NZ). Named for
Nelson Haven — the sheltered water behind the Boulder Bank.

The business and copy decisions live in [`docs/BRIEF.md`](docs/BRIEF.md) — the
founding brief and single source of truth. Built with a small Python builder
into a folder Netlify serves as-is. **No Node required.**

## The business model (short)

Four packages — Aerial Photos (from $290), Photos + Clips (from $490), The
Short Cut (from $690) and Progress Flights (from $240/visit). "From" pricing;
a **written quote fixes the price before takeoff**. Booking is a *request*
(the CTA is "Check a date"), handled by a Cal.com embed synced to Google
Calendar. Invoicing is done with **Stripe** after delivery — nothing is
charged on the site. Signature policy: the **Weather Promise** — marginal days
are called early and rescheduled free.

## Stack

- Hand-written HTML/CSS/vanilla JS — no framework.
- `build.py` (Python 3 stdlib) assembles `pages/*.html` + `partials/base.html`
  → `haven-aerials-netlify-deploy/`.
- Every page is a bespoke file in `pages/` with `<!-- key: value -->` meta
  headers. Structured data lives inside each page; site-wide LocalBusiness
  schema is in `partials/base.html`.

## Design system — "golden hour on the Haven"

Warm paper & sand backgrounds, deep-sea teal CTAs, amber sun accents.
Fraunces (display) + Inter (body). Pill buttons, 18px cards, soft warm
shadows. Tokens live at the top of `static/css/styles.css`. Logo is a
viewfinder square holding a horizon + sun disc.

## Layout

```
docs/BRIEF.md                    # founding brief — business + copy source of truth
build.py                         # assembles the site
partials/base.html               # shared shell (head, header, footer, schema)
pages/*.html                     # index, services, work, about, book, privacy, terms
static/css, static/js, static/assets
haven-aerials-netlify-deploy/    # BUILD OUTPUT — committed, published by Netlify
```

## Build & preview

```bash
python3 build.py
cd haven-aerials-netlify-deploy && python3 -m http.server 4321
# open http://localhost:4321
```

## Deploy

Commit and push to `main` (`git@github.com:Bengitshub/nelson-drone-website.git`).
Netlify publishes `haven-aerials-netlify-deploy/` with no build command
(see `netlify.toml`).

## SEO

Per page: title/description/keywords/canonical + JSON-LD (LocalBusiness
site-wide; BreadcrumbList per page; Service + OfferCatalog on /services;
FAQPage on the homepage), generated `sitemap.xml` + `robots.txt`, geo meta,
cache-busted assets. Verified: 7 pages build, all JSON-LD valid, one `<h1>`
per page, no broken links, no horizontal overflow at 375px.

## Before launch — must be real, not placeholder

- [ ] Register `havenaerials.nz` (check availability first) → set `SITE_URL` in build.py
- [ ] Confirm legal entity + GST status; have a professional review privacy/terms drafts
- [ ] Real contact details (footer + JSON-LD in `partials/base.html`, tel/mailto in pages)
- [ ] Verified pilot name, photo, credential & insurance wording (see `<!-- OPERATOR -->` in about.html) — nothing invented
- [ ] Four portfolio shoots → real media replaces every `Sample flight` placeholder
- [ ] Cal.com account + Google Calendar → replace `.embed-fallback` in book.html (see `<!-- CAL_EMBED -->`)
- [ ] Stripe account for invoicing
- [ ] Real OG image (1200×630 raster) → update `og_image`
- [ ] Google Business Profile (service-area business, matching NAP)
- [ ] Submit sitemap in Search Console

**The site launches on footage, not code.**

---

### Project history

This repo previously explored a different brand direction (Nelson Drone Co.,
and earlier FortyOne South / Wide Arc / Skyframe). Those are preserved on
branches (`nelson-drone-co-v2`, `fortyone-south-scenic`) and in git history.
`main` is Haven Aerials — a from-scratch rebuild.
