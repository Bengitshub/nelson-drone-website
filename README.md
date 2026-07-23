# Nelson FPV Drone Website (working name: **Skyframe**)

Static marketing site for a Nelson–Tasman FPV drone film business.
Built the same way as the other sites in `~/Sites`: a small Python builder
assembles pages from partials into a deploy folder that Netlify serves as-is.
**No Node required.**

## Stack
- Hand-written HTML/CSS/vanilla JS — no framework.
- `build.py` (Python 3 stdlib) assembles `pages/*` + `partials/base.html` → `nelson-drone-netlify-deploy/`.
- Booking: Cal.com "Requires Confirmation" embed → Google Calendar (to be added).
- Invoicing: manual via Hnry after each shoot.

## Layout
```
build.py                       # assembles the site
partials/base.html             # shared shell (head, header, footer)
pages/*.html                   # per-page meta + <main> content
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
Netlify is connected to the repo with **publish = `nelson-drone-netlify-deploy`**
and **no build command**.

## Pages
- Homepage: `pages/index.html` (bespoke).
- Inner pages: data-driven from `content/pages.json` (services hub, 5 service
  pages, about, contact, drone-rules guide). Edit the JSON and rebuild.
- SEO per page: title/description/keywords/canonical, JSON-LD
  (LocalBusiness site-wide; Breadcrumb/Service/Article/FAQ per page),
  sitemap.xml, robots.txt.

## Before launch — must be real, not placeholder
- [ ] Real business name + logo (working name "Skyframe"); set real domain in `SITE_URL` (build.py) + base.html canonical
- [ ] Real contact details (`PHONE_TEL`/`PHONE_DISPLAY`/`EMAIL` in build.py, footer + JSON-LD in base.html) + social links (`sameAs`)
- [ ] Real showreel / clips (replace all `Sample`/placeholder media blocks)
- [ ] Confirm CAA Part 101 wording + insurance are true before publishing; personalise the About "person behind the drone" placeholder
- [ ] Cal.com booking embed (replace `.book-calendar` slot) + connect Google Calendar; Stripe for manual invoicing
- [ ] Add Privacy policy, Terms, and weather/reschedule policy pages (+ relink in footer)
- [ ] Real OG image (1200×630) at `/static/assets/og.svg` → swap for a raster (`og.jpg`) and update `og_image`
- [ ] Set up Google Business Profile (service-area: Nelson/Tasman) with matching NAP
