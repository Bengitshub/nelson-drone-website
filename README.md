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

## Before launch — must be real, not placeholder
- [ ] Real business name, logo, domain (`.nz` + `.co.nz`)
- [ ] Real contact details + social links
- [ ] Real showreel / clips (replace all `Sample` placeholders)
- [ ] Confirm CAA Part 101 wording + insurance are true before publishing them
- [ ] Cal.com booking embed + Google Calendar
- [ ] Privacy policy, Terms, weather/reschedule policy pages
