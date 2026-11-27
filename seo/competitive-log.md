# Competitive keyword SEO log (head terms: MSP / business IT support)

Owned by the **Daily SEO, competitive keywords** routine. Vertical (clinic/law) work is logged in `daily-log.md`; home-user work in `home-support-log.md`.

## 2026-11-26
- Audit: 0 errors at start (36 warnings); 0 errors at end (30 warnings, 91 pages).
- Checked open PRs: none touch head-term/MSP pillar pages.
- Competitor re-check (first since 2026-10-09): "best MSP Lower Mainland" SERP is mostly Clutch directory pages and vendor buyer's guides; local published prices still ~$80 (Integrity Tech) to $150+/user/mo. Keyword map updated.
- New pillar page `/business-it-support` (~1,700 words): "Small Business IT Support in the Lower Mainland & Fraser Valley". What's included (from services.html), owner-confirmed pricing and exclusions, market price context (no competitors named), signs you've outgrown ad-hoc IT, **"How to choose the best MSP in the Lower Mainland"** 10-question checklist (`#choosing`), managed vs break-fix vs in-house, area links to all 11 location pages, industry links, 6-question FAQ. Service (with Offer) + FAQPage + BreadcrumbList JSON-LD. TODO owner comment: whether to publish a worked monthly example and whether any onboarding fee applies.
- Linked from: home page managed-IT card, services.html managed-IT block (`#choosing`), the pricing section of all 10 main location pages (one sentence each), and `/blog/managed-it-vs-inhouse-smb`.
- `/blog/managed-it-vs-inhouse-smb` (Search Console: 13 impressions, 0 clicks for "in-house it vs managed services"): title 130 → 60 chars, new meta description, added "What managed IT costs with Clearpine" section ($95/user/mo worked example for 25 users) and a free-assessment CTA button.
- `/blog/independent-contractor-vs-msp`: title 130 → 61 chars.
- Sitemap: added `/business-it-support`; bumped lastmod for every page touched.
- Target keywords: small business IT support Lower Mainland, business IT support BC, IT support for small business Fraser Valley, best MSP Lower Mainland, how to choose an MSP, in-house IT vs managed services.
- Next steps: `/managed-it-services` pillar (managed service provider BC, MSP Fraser Valley, outsourced IT department), distinct from `/business-it-support` by focusing on the MSP model, SLAs and onboarding; strengthen `/locations/chilliwack` (Search Console's top query) with local specifics; `/services/microsoft-365` and `/services/cybersecurity` pages; blog "Managed IT pricing in BC". Owner actions: Clutch profile + reviews, Google Business Profile reviews for "near me" queries.

## 2026-11-27
- Audit: 0 errors at start; 0 errors at end (30 warnings, 94 pages).
- **Found a stuck pipeline:** none of this routine's work has ever reached `main`. Since 2026-10-10 it pushed to ~50 `claude/kind-cray-*` branches without opening PRs, and rebuilt the same `/business-it-support` page on 40+ of them. Finished pages from 2026-11-19 to 2026-11-23 were also stranded.
- No new page written today. Instead, consolidated the stranded work onto one branch on top of current `main` (plus yesterday's `seo/competitive-2026-11-26` pillar + MSP checklist):
  - `/managed-it-services` pillar (from `kind-cray-4g7hpe`, 2026-11-22): managed service provider BC, MSP Fraser Valley. Does not yet use "outsourced IT department" wording; add a section next run.
  - `/blog/managed-it-services-cost-bc` (from `kind-cray-addhzh`, 2026-11-19): BC managed IT pricing guide with worked examples for 5–25 staff; datePublished set to 2026-11-27. TODO owner: confirm publishing the market price ranges.
  - `/services/cybersecurity` (from `kind-cray-z42ptm`, 2026-11-23): small business cybersecurity service page. TODO owner: standalone security project pricing.
  - Wired in: sitemap, blog index (list + JSON-LD), home page managed-IT and cybersecurity cards, services.html (managed-IT intro + cybersecurity block), `/business-it-support` (pricing section, cybersecurity link, sidebar), `/blog/onsite-it-support-cost-fraser-valley` (link to pricing guide).
  - Checked pricing on all three pages matches main ($95/user/mo, min 5 users, 1-year term, custom billing under 5 users).
- Target keywords now covered: best MSP Lower Mainland, small business IT support, business IT support BC, managed IT services Lower Mainland, managed service provider BC, MSP Fraser Valley, managed IT services cost BC, cybersecurity services small business BC.
- Next steps (once this branch merges): strengthen `/locations/chilliwack` (top Search Console query); `/services/microsoft-365`; `/services/co-managed-it`. Owner: Clutch profile and Google Business Profile reviews for "best MSP" / "near me" queries.
