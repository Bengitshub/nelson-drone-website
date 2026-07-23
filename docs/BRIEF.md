# Nelson Drone Co. — Owner's Brief (v2.0)

*Written 23 July 2026 by the operator. This replaces all external briefs. Where an
old document and this one disagree, this one wins.*

Nelson Drone Co. is a one-pilot aerial photography and video service based in
Nelson, New Zealand, working across Nelson, Tasman and Marlborough. We sell
useful pictures from the air — not cinema, not surveying, not an agency
retainer. A client should be able to land on the site, understand the offer in
thirty seconds, see a price, and request a date.

---

## 1. The business in one paragraph

A professional pilot with a DJI Avata 360 flies planned, legal, weather-checked
shoots and delivers edited stills, ready-to-use clips or a short edited
highlight within days, as a download link. Quoting is written and fixed before
the flight. Invoicing is done with **Stripe** after delivery — pay online by
card or bank transfer. Booking runs through a **Cal.com** request (never an
instant confirmation), because no drone job is real until airspace, access,
people and weather have been checked.

## 2. What we sell

| Service | What the client gets |
|---|---|
| **Aerial photography** | Edited high-res stills + web-sized copies. Property, land, buildings, coastline, records. |
| **Video clips** | Trimmed, colour-corrected clips, no music/titles — made for the client's own editor or social team. |
| **Short highlight** | A 20–45 s edited cut: one music track, clean pacing, simple title/logo card, one format, one revision. |
| **FPV & 360 capture** | Continuous fly-throughs, close movement, and 360 shots that can be reframed after the flight. |
| **Progress shoots** | The same viewpoints revisited on schedule — date-labelled photos and clips for builds and projects. |

**We do not sell** (and the site must never imply): survey-grade mapping or
measurement, thermal or engineering inspection, weddings as full films,
scripted productions, interviews/audio, motion graphics, film-grade grading,
guaranteed social-media performance.

## 3. Pricing (launch)

| Package | From | Included |
|---|---|---|
| Aerial Photos | NZ$295 | ≤30 min on site, 10–15 edited stills, hi-res + web files, Nelson/Richmond travel |
| Photo + Video | NZ$495 | ≤45 min on site, 10–15 stills, 5–10 trimmed clips, horizontal, colour-corrected |
| Short Highlight | NZ$695 | Planned capture, 20–45 s edit, music, title card, 1 format, 1 revision, 5 stills |
| Progress Visit | NZ$245/visit | Repeat viewpoints, progress clips, date-labelled folders (3+ visits recommended) |

Add-ons quoted per job: extra stills, vertical version, raw handover, extra
location, extra revision, priority delivery, travel beyond Nelson/Richmond.

Rules: always "from" pricing; a written quote fixes the number before the
flight; the quote states the total payable. No on-site payment. Weather
reschedules are never treated as cancellations.

## 4. How a job runs (operations)

1. **Request** — client picks a provisional slot on Cal.com (60-min placeholder,
   requires confirmation, 48 h minimum notice, Pacific/Auckland) and answers the
   booking questions (location, service, use, access, ownership).
2. **Check** — pilot reviews airspace, landowner permission, people, wildlife,
   weather window and scope. Clarify by phone/email if needed.
3. **Quote** — written quote sent; booking confirmed or rescheduled in Cal.com.
4. **Fly** — shoot happens inside the agreed window.
5. **Deliver** — download link with organised, labelled files.
6. **Invoice** — Stripe invoice sent after delivery; card or bank transfer.

## 5. Voice

Plain New Zealand English. Short sentences. Specific over impressive. We say
what's included, what it costs, and what we won't do.

- Say: "we check", "written quote", "download link", "trimmed clips",
  "the call is the pilot's".
- Never say: cinematic, breathtaking, stunning, elevate, cutting-edge,
  storytelling, "Book now" (booking is always a *request*).
- Never invent: clients, reviews, credentials, insurance, permits. Sample work
  is always labelled **Portfolio Project**. Placeholders stay placeholders
  until Ben supplies verified details.

Flag lines (mine — use them, don't re-import old brief copy):

- Hero: **"Your place, from above."**
- Hero support: "Drone photography and video for property, tourism,
  construction and events across Nelson, Tasman and Marlborough."
- Slogan (schema): "Your place, from above."
- Booking disclaimer: "Picking a time sends us a request — nothing is locked in
  until we've checked the site and confirmed the scope with you."
- Payment line: "After delivery we send a Stripe invoice — pay online by card
  or bank transfer. No payment is taken on this website."

## 6. Site map & page jobs

All pages are bespoke HTML in `pages/`, assembled by `build.py` into the
Netlify deploy folder. Existing design system only (tokens/classes in
`static/css/styles.css`); Manrope; bright blue-and-white; drone quadcopter
logo mark stays.

| Page | Job | Key blocks |
|---|---|---|
| `/` | Land → understand → request | Done. Hero, proof, services, work, industries, process, pricing, about, FAQ, CTA |
| `/services` | Decide + price | Four service detail rows, full package cards, add-ons, honest "not offered" list, FAQ hand-off, CTA |
| `/work` | Prove it | Portfolio grid (honest sample labels), how samples become client work, CTA |
| `/about` | Trust the pilot | Operator (placeholder name), gear (Avata 360), how we plan flights, rules we operate under, service area |
| `/book` | Convert | Request explainer (what happens after), Cal.com embed shell + fallback, disclaimer, contact alternatives |
| `/privacy` | Compliance | Plain-English: booking data (Cal.com), payment data (Stripe), aerial footage & neighbours, NZ Privacy Act 2020, retention, contact |
| `/terms` | Protect both sides | Quotes/booking requests, weather policy, access & permissions, pilot's final call, deliverables & revision, usage licence + our portfolio rights, Stripe payment terms, liability |

SEO titles follow "Primary Keyword | Nelson Drone Co."; descriptions are
original, ≤160 chars; every page gets canonical + BreadcrumbList; `/services`
adds Service schema; FAQ blocks get FAQPage schema. Sitemap priorities:
services/book 0.9, work 0.8, about 0.7, legal 0.3.

## 7. Launch gates (unchanged, Ben supplies)

Domain (`nelsondrone.co.nz` preferred, unregistered), legal entity + GST
status, verified credential/insurance wording, real phone/email, Cal.com
account wired to Google Calendar, Stripe account, four test shoots for real
portfolio media, Google Business Profile. **The site launches on footage, not
code.**
