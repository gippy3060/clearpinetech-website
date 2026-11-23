# Competitive keyword SEO log (head terms: MSP / business IT support)

Separate from `daily-log.md` (which the vertical-practice routine also writes to) to avoid merge conflicts.

## 2026-11-18
- Audit: 0 errors at start (36 warnings); 0 errors at end (29 warnings).
- New pillar page `/business-it-support`: "Small Business IT Support in the Lower Mainland". Covers what is included, owner-confirmed pricing ($95/user/month, min 5, 1-year, exclusions, free on-site if not fixable remotely, custom billing under 5 users as stated on /services) with plain-arithmetic examples, an 8-question "how to choose the best MSP in the Lower Mainland" checklist (does not claim to be the best), managed IT vs break-fix/contractor/in-house/co-managed, service-area links to all 11 city pages, industry links, FAQ. Service + Offer + FAQPage + BreadcrumbList JSON-LD.
- Linked from the home page managed-IT card and from `/services` intro. Added to sitemap.
- Title/description fixes: `/blog/managed-it-vs-inhouse-smb` title now leads with "In-House IT vs Managed Services" (matches the Search Console query with 13 impressions/0 clicks); `/blog/onsite-it-support-cost-fraser-valley` title shortened; `/services` meta description 204 -> 151 chars.
- Target keywords: small business IT support Lower Mainland, business IT support BC, best MSP Lower Mainland, managed service provider Fraser Valley, how to choose an MSP.
- Next steps: `/managed-it-services` pillar is still todo but would overlap this page; consider instead `/services/microsoft-365`, `/services/cybersecurity` and `/services/co-managed-it` standalone pages (A-priority in keyword map); "Managed IT pricing in BC" blog post; owner to list the business on Clutch/GoodFirms/chamber directories.

## 2026-11-19
- **Unmerged-work warning:** about 40 earlier `claude/kind-cray-*` branches from this routine were never merged to `main`, so each run rebuilt `/business-it-support`. This run carried the 2026-11-18 branch (`kind-cray-ytpwxr`) onto current `main` (clean cherry-pick) instead of rewriting it. The owner needs to merge this branch, or let this routine open PRs like the other routines do.
- Audit: 0 errors at start (34 warnings after carrying the pillar page); 0 errors at end (32 warnings, 86 pages).
- New blog post `/blog/managed-it-services-cost-bc`: "How Much Do Managed IT Services Cost in BC?" Market per-user bands from competitor sites reviewed Oct 2026 (no competitor named), what is included, common extras, worked examples at the owner-confirmed $95/user/month (5/10/15/25 staff), alternatives, why clinics/law firms cost more (links to the vertical cost posts), a quote-comparison checklist, FAQ. BlogPosting + FAQPage + BreadcrumbList JSON-LD. TODO owner comment: OK to publish the market ranges.
- Added to blog index (list + JSON-LD) and sitemap; linked from `/business-it-support` pricing section and `/blog/onsite-it-support-cost-fraser-valley`. Bumped lastmods.
- Target keywords: managed IT services cost BC, how much does an MSP cost, IT support pricing small business Vancouver, managed IT price per user.
- Next steps: once merged, `/services/microsoft-365`, `/services/cybersecurity`, `/services/co-managed-it` standalone pages; strengthen `/locations/chilliwack` and `/locations/surrey` (Search Console queries); Clutch/GoodFirms/chamber listings (owner).

## 2026-11-22
- **Unmerged-work warning (still open):** 45+ `claude/kind-cray-*` branches from this routine sit unmerged; the 11-20 and 11-21 runs rebuilt `/business-it-support` again. This run did **not** rebuild it. It consolidated the best existing work onto current `main` in one branch:
  - `/business-it-support` pillar + `/blog/managed-it-services-cost-bc` (cherry-picked from `kind-cray-addhzh`, 2026-11-19).
  - `/managed-it-services` pillar (cherry-picked from `kind-cray-2iert5`, 2026-11-01), conflicts resolved against current `main`.
- `/managed-it-services` additions: link to the BC pricing guide; new "Choosing an MSP" paragraph linking the `/business-it-support#choosing-an-msp` checklist (new anchor id on that h2). Distinct intent from `/business-it-support`: MSP/managed-service terms vs small-business support terms; the two cross-link.
- Internal links: home managed-IT card now links both pillars; `/services` intro links `/managed-it-services`; Abbotsford, Chilliwack, Langley and Surrey pages (Search Console queries) got a "Comparing IT companies?" line linking both pillars and the MSP checklist.
- Facts used are only those already on `/services` (pricing, custom billing under 5 users, written agreement with defined response times, co-managed IT). Every internal link resolves.
- Audit: 0 errors at end (30 warnings, 88 pages, all lastmod on pages owned by other routines or older pages).
- Target keywords: best MSP Lower Mainland, managed IT services Lower Mainland, managed service provider BC/Fraser Valley, business IT support, small business IT support.
- Next steps: **owner merges this branch first.** Then `/services/microsoft-365`, `/services/cybersecurity`, `/services/co-managed-it`; Clutch/GoodFirms/chamber listings (owner). Future runs: check `git log origin/main` for `/business-it-support` and `/managed-it-services` before building anything.

## 2026-11-23
- **Unmerged-work warning (still open):** this branch carries the 11-22 consolidation (`/business-it-support`, `/managed-it-services`, `/blog/managed-it-services-cost-bc`) plus today's page. None of it is on `main` yet. Did not rebuild either pillar.
- Competitor check (web search, "cybersecurity services small business Abbotsford Fraser Valley Lower Mainland"): results are dominated by Clutch and BBB category listings and by Plurilock's Abbotsford city pages (vulnerability/risk assessment, training). Design2Web IT appears on Clutch. No small-business-focused local MSP cybersecurity page ranked in the results, so a plain-language page has room.
- New service page `/services/cybersecurity`: "Cybersecurity services for small businesses in the Lower Mainland and Fraser Valley". Eight controls (facts taken from the `/services` cybersecurity section and Microsoft 365 section only), a six-step "where to start if you have done nothing yet" list, what is included in the $95/user/month managed plan vs scoped separately, co-managed security, regulated practices (links to clinic/law-firm security and incident-response posts and industry pages, with no-legal-advice note), scam-call guide link, FAQ, service area. Service + FAQPage + BreadcrumbList JSON-LD. TODO owner comment: whether standalone security projects have a published rate.
- Linked from `/services` (cybersecurity section), `/managed-it-services` (Security bullet) and `/business-it-support` (cybersecurity link now points to the new page). Added to sitemap; bumped lastmod for the three linking pages.
- Audit: 0 errors at end (30 warnings, 89 pages). Every internal link on the new page resolves.
- Target keywords: cybersecurity services small business BC, small business cybersecurity Abbotsford/Fraser Valley/Lower Mainland, managed security Fraser Valley, IT security assessment.
- Next steps: **owner merges this branch.** Then `/services/microsoft-365` and `/services/co-managed-it`; switch site-wide footer "Cybersecurity" link to `/services/cybersecurity` once merged; owner to claim Clutch and BBB listings (they dominate local cybersecurity results).
