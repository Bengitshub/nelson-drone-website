# Haven Aerials — Founding Brief (v1.0)

*Written 23 July 2026 by the founder. Everything here is an original decision.
No text, structure or design in this business may be copied from any earlier
brief or earlier site direction — those are retired and preserved in git
history only.*

---

## 1. The business

**Haven Aerials** — drone photography and videography, based in Nelson,
New Zealand, flying across Nelson, Tasman and Marlborough.

Named for **Nelson Haven**, the sheltered water behind the Boulder Bank. The
name carries the promise: calm, protected, no surprises. One pilot handles
every job start to finish. The aircraft is a DJI Avata 360 — small, agile,
happy in tight spaces, and it captures 360 footage that can be reframed into
different shots after the flight.

**What clients buy:** useful aerial pictures of their property, project,
business or event — delivered fast, priced in writing before takeoff.

**What this is not:** a film studio, a survey company, an agency. No mapping,
no thermal inspections, no certified measurements, no full wedding films, no
scripted productions, no interview/audio work, no motion graphics, no
film-grade colour pipelines, and no promises about going viral.

## 2. Voice — first person, weather-honest

The site speaks as the pilot: **I, me, my**. One person flies your job, so
one person talks to you. Warm, direct, concrete New Zealand English.

- Say: "I'll check the airspace before I quote", "written quote before
  takeoff", "I call the weather early", "download link", "Stripe invoice".
- Banned: cinematic, breathtaking, stunning, elevate, cutting-edge,
  storytelling, world-class, "Book now" (a booking is always a request —
  the CTA verb is **"Check a date"**).
- Never invent: clients, testimonials, credentials, insurance, permits,
  operator names. Samples are labelled **Sample flight** until real client
  work replaces them. Contact details are placeholders until Ben confirms
  the real ones.

**The Weather Promise** (signature policy, gets its own homepage section):
if the window isn't right, I call it early — usually the day before — and we
move to the next good window at no charge. A weather move is never a
cancellation.

## 3. Services & pricing

| # | Package | From | What's in it |
|---|---|---|---|
| 1 | **Aerial Photos** | NZ$290 | Up to 30 min on site · 12+ edited stills · full-res + web-sized · Nelson/Richmond travel included |
| 2 | **Photos + Clips** | NZ$490 | Up to 45 min on site · 12+ stills · 6–10 trimmed, colour-balanced clips (no music/titles — made for your editor or social team) |
| 3 | **The Short Cut** | NZ$690 | A 20–45 second edited piece: licensed track, clean pacing, your logo/title card, one format (horizontal or vertical), one revision, plus 5 stills |
| 4 | **Progress Flights** | NZ$240 / visit | Same viewpoints every visit · dated folders · short clips · three-visit minimum recommended · end-of-project comparison quoted separately |

Add-ons (quoted per job): vertical version of The Short Cut, extra revision,
raw/selected footage handover, second location, priority 48-hour delivery,
extra travel beyond Nelson/Richmond, FPV fly-through planning.

Rules: "from" pricing everywhere; the **written quote fixes the price** and
states the total payable; no payment taken on the website; delivery targets
are three working days for photos, five for video — targets I set, stated as
targets.

## 4. How a job runs

1. **Check a date** — client picks a provisional slot (Cal.com, requires
   confirmation, 48 h minimum notice, Pacific/Auckland) and answers the job
   questions: location, what to capture, where it'll be used, date
   flexibility, site ownership/permission, access notes.
2. **Desk scout** — I check airspace (Nelson Airport control zone matters),
   landowner permission, people, wildlife, privacy and the weather outlook.
3. **Written quote** — fixed price, scope, deliverables. Once accepted, the
   booking is confirmed in Cal.com.
4. **Fly** — inside the agreed window; the pilot's safety/legality call is
   final.
5. **Deliver** — organised download link; photos target 3 working days,
   video 5.
6. **Invoice** — **Stripe** invoice after delivery; pay online by card or
   bank transfer; 7-day terms (placeholder).

I fly under New Zealand's standard drone rules (CAA Part 101): line of
sight, altitude limits, consent for people and property below, controlled
airspace clearances near Nelson Airport. Phrase these as obligations I meet,
never as certifications I hold.

## 5. Design system — "golden hour on the Haven"

Warm, coastal, editorial-but-practical. Feels like early evening light over
still water; nothing corporate-blue about it.

Tokens (`static/css/styles.css`):

- **Paper** `#FBF9F5` — page background
- **Sand** `#F3EDE2` — alternating section bands
- **White** `#FFFFFF` — cards
- **Ink** `#20242B` — text, footer
- **Mist** `#6E6A61` — secondary text (warm grey)
- **Sea** `#0F766E` — primary CTAs, links (deep coastal teal)
- **Deep Sea** `#0C5D57` — hover
- **Sun** `#D97706` — eyebrows, accents, logo sun (amber)
- **Line** `#E6DFD2` — borders (warm)

Type: **Fraunces** (display — headings, 500–650, tight leading) +
**Inter** (body/UI). Buttons are **pills** (999px radius). Cards 18px radius,
soft warm shadows. Container 1160px. Motion: gentle reveal only, respects
reduced-motion.

Logo mark: a rounded viewfinder square containing a horizon line with a sun
disc sitting on it — camera + coastline in one, works single-colour.

Placeholder media blocks use golden-hour gradients (amber → sea-glass →
paper) with an ⟡ "Sample flight" tag. No stock photos, ever.

## 6. Site map & page jobs

Static site, Python builder (`build.py`), deploy folder
`haven-aerials-netlify-deploy/` published by Netlify as-is. Placeholder
domain: `https://www.havenaerials.nz` (register before launch). Placeholder
contact: `hello@havenaerials.nz`, `03 000 0000` / `tel:+6430000000`.

Nav order (portfolio-led): **Work · Services · About · [Check a date]**

| Page | Job | Notes |
|---|---|---|
| `/` | Understand + trust + request | Hero, trust strip, recent work, services w/ prices, process, Weather Promise, who books, about teaser, FAQ, final CTA |
| `/services` | Choose + price | Package detail cards, what's in each, add-ons, delivery targets, the honest "what I don't do" list |
| `/work` | Proof | Sample-flight grid (honest labels), the four pre-launch portfolio shoots plan, early-subject invitation |
| `/about` | Trust the pilot | The pilot (name/photo = placeholder comment for Ben), the aircraft, how I plan, rules I fly under, service area |
| `/book` | Convert | "Check a date" explainer, Cal.com embed shell + fallback, what to have ready, request disclaimer |
| `/privacy` | Compliance | Plain-English: Cal.com booking data, Stripe payments, aerial footage & neighbours, Privacy Act 2020, retention, contact |
| `/terms` | Protect both sides | Request model, written quotes, Weather Promise terms, access/permissions, pilot's call, deliverables & revision, usage licence, Stripe terms, liability |

SEO: titles "Keyword | Haven Aerials"; original descriptions ≤160 chars;
canonical + BreadcrumbList everywhere; Service+OfferCatalog on /services;
FAQPage where an FAQ exists; LocalBusiness site-wide (base partial);
sitemap priorities: home 1.0, services/book 0.9, work 0.8, about 0.7,
legal 0.3.

## 7. Launch gates (Ben supplies — the site launches on footage, not code)

Register domain; confirm legal entity + GST status; verified pilot
name/credentials/insurance wording; real phone/email; Cal.com + Google
Calendar; Stripe account; four portfolio shoots (a home or lifestyle block,
an accommodation or venue, a build site, something moving on the water);
Google Business Profile; legal review of privacy/terms drafts.
