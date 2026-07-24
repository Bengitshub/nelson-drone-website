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
film-grade colour pipelines, and no promises about going viral. Editing is an
add-on, not a core promise (the finished-content pitch overstates a one-person
capability).

**Descriptor:** *Drone photography, video and 360° capture · Nelson* — 360° is
the one meaningful technical point of difference (the Avata 360 genuinely does
8K 360° video + high-res 360° stills), so it belongs in the descriptor.

## 2. Voice — first person, weather-honest, not over-explained

The site speaks as the operator: **I, me, my**. Warm, direct, concrete NZ
English. State the one-operator positioning **once** on the homepage and once on
About — don't repeat "just me / one-man band" everywhere (it starts reassuring
and ends up sounding small). Approved line: *"one experienced operator and one
point of contact from planning through to delivery."* Don't imply the operator
is physically alone on every flight — FPV with goggles needs an observer under
Part 101, and support is brought in where a flight requires it.

- Say: "I'll check the airspace before I quote", "written quote before the
  shoot", "I call the weather early", "download link", "invoice details by email".
- Banned: cinematic, breathtaking, stunning, elevate, cutting-edge,
  storytelling, world-class, "Book now" (a booking is always a request —
  the CTA verb is **"Request a shoot"**).
- Never invent: clients, testimonials, credentials, insurance, permits,
  operator names, or project names/locations on the portfolio. Samples are
  labelled **Sample** until real client work replaces them. Never claim
  "certified / licensed / CAA approved" without a specific Part 102 qualification
  — standard work runs under Part 101. Contact details are placeholders until
  Ben confirms the real ones.

**The Weather Promise** (signature policy, gets its own homepage section):
if the window isn't right, I call it early — usually the day before — and we
move to the next good window at no charge. A weather move is never a
cancellation.

## 3. Services & pricing

Four **core** services (360° promoted to core; editing demoted to add-on):

| # | Service | From | What's in it |
|---|---|---|---|
| 1 | **Aerial photography** | NZ$290 | 12+ edited stills · full-res + web-ready · Nelson/Richmond travel included · delivery within 3 working days |
| 2 | **Aerial photography + video** | NZ$490 | 12+ stills · 6–10 trimmed clips · basic colour correction · horizontal or vertical where practical · usable yourself or by an editor · delivery within 5 working days |
| 3 | **Construction progress** | NZ$240 / visit | Repeat agreed viewpoints · edited photos · short progress clips · dated folders · discounted for ongoing schedules |
| 4 | **FPV + 360° capture** | Quoted / project | 8K 360° video + high-res 360° stills · FPV fly-throughs · interactive 360° viewpoints · specialist, planned per location · observer may be required under Part 101 |

**Add-ons:** *Simple social edit* from $195 (20–45s basic edit — one format, one
track, one revision, no voiceover/interviews/animation/effects); *360° aerial
view* from $150 (a single or small number of interactive aerial viewpoints —
not a full virtual tour); additional location; vertical video versions;
priority delivery; travel outside the local area.

Rules: "from" pricing everywhere; the **written quote fixes the price** and
states the total payable; no payment taken on the website; delivery targets are
three working days for photos, five for video — stated as targets, not guarantees.

## 4. How a job runs

1. **Request a shoot** — client submits location, preferred date and required
   service (Cal.com, requires confirmation, 48 h minimum notice, Pacific/Auckland).
2. **Feasibility check** — I check airspace (Nelson Airport control zone),
   access and whether the site can be flown safely and legally.
3. **Written quote** — sent manually by email; fixed price, scope, deliverables.
4. **Confirm** — once the quote is accepted, the booking is confirmed.
5. **Fly & deliver** — inside the agreed window (pilot's safety/legality call is
   final); organised download link, photos target 3 working days, video 5.
6. **Invoice** — invoice details sent **by email**; payment terms are stated on
   each quote and invoice, kept flexible. The payment tool (Stripe / bank
   transfer / Xero, TBD) is operational detail and is NOT named across the site.

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

Logo mark: a **top-down camera-quadcopter** — four rotor props, an X-frame and a
centre camera lens. Reads unmistakably as a drone, works single-colour (amber).

Media: **royalty-free aerial photos** (Pexels, free for commercial use, no
attribution) in `static/assets/img/`, optimised with Pillow. Used as tasteful
placeholders with a small "Sample" tag; the footer notes media are placeholders
and the /work copy calls them reference images. NO stock is ever passed off as
the operator's own client work — swap all of it for real Avata footage at launch.

## 6. Site map & page jobs

Static site, Python builder (`build.py`), deploy folder
`haven-aerials-netlify-deploy/` published by Netlify as-is. Placeholder
domain: `https://www.havenaerials.nz` (register before launch). Placeholder
contact: `hello@havenaerials.nz`, `03 000 0000` / `tel:+6430000000`.

Nav order (portfolio-led): **Work · Services · About · [Request a shoot]**

| Page | Job | Notes |
|---|---|---|
| `/` | Understand + trust + request | Hero (commercial proposition), trust strip, recent work, four services w/ prices, process, trimmed Weather Promise, who books, one-operator teaser, FAQ, final CTA |
| `/services` | Choose + price | Four service rows (photography, photography+video, construction progress, FPV+360), add-ons (social edit $195, 360° view $150, +others), one-line scope statement, CTA. NO duplicate "at a glance" grid. |
| `/work` | Proof | Reference-image grid with service-type captions only (no fake project names/locations), pre-launch shoots plan, early-subject invitation. Cannot truly launch until 4 real shoots exist. |
| `/about` | Trust the operator | Independent-operator positioning (stated once), one-sentence name story, short equipment blurb, how I plan, Part 101 rules, service area |
| `/book` | Convert | "Request a shoot" explainer, 5-step process, Cal.com embed shell + fallback, what to have ready, request disclaimer |
| `/privacy` | Compliance | Plain-English: Cal.com booking data, payment-provider data (not named), aerial footage & neighbours, Privacy Act 2020, retention, contact |
| `/terms` | Protect both sides | Request model, written quotes, Weather Promise terms, access/permissions, pilot's call, deliverables & revision, usage licence, payment terms (flexible, by email), liability |

SEO: titles "Keyword | Haven Aerials"; original descriptions ≤160 chars;
canonical + BreadcrumbList everywhere; Service+OfferCatalog on /services;
FAQPage where an FAQ exists; LocalBusiness site-wide (base partial);
sitemap priorities: home 1.0, services/book 0.9, work 0.8, about 0.7,
legal 0.3.

## 7. Launch gates (Ben supplies — the site launches on footage, not code)

**Mandatory before public launch:**
- Real operator name + a real photograph of the operator
- Real phone number and email
- Public liability insurance (once obtained) + accurate operating credentials
  (Part 101; only say "certified/licensed/CAA approved" with a real Part 102 qual)
- **Real portfolio** — at least four genuine shoots (residential/lifestyle
  property; accommodation/tourism/venue; construction/development; marine,
  orchard, vineyard or outdoor activity), each 8–12 final photos + several clips
  + one 360° output where appropriate + client permission + short description.
  Remove the "reference images" explanation once these exist.
- At least three genuine testimonials
- Final legal entity + GST status; final payment policy; final media-retention period
- Working Cal.com booking calendar (→ Google Calendar); registered domain
- Google Business Profile; legal review of privacy/terms drafts

There is no shortcut on the portfolio — for a drone business it is the proof.
