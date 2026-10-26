# Daily SEO log (business / MSP pages)

## 2026-10-07
- Added `scripts/seo_audit.py` (did not exist): checks title, meta description, canonical-in-sitemap, single h1. Reports 0 errors, 20 length warnings.
- New page `/industries/law-firms` (Service + FAQPage + Breadcrumb JSON-LD), linked from `industries.html`, added to sitemap.
- Target keywords: IT support for law firms BC, managed IT law firm Lower Mainland, Law Society of BC cloud computing IT.
- No invented facts; Law Society/PIPA statements are general and defer to counsel.
- Next steps: fix long titles/descriptions (listed by the audit; services.html description is 204 chars); blog post "IT requirements for a new law firm in BC"; `/industries/medical-clinics` and `/industries/dental` pages; link law-firms page from location pages; owner to verify Law Society wording.

## 2026-10-08
- New blog post `/blog/it-requirements-new-law-firm-bc` (~1,900 words, BlogPosting JSON-LD): setup checklist covering email/MFA, practice-management software, document storage, Law Society cloud due diligence, devices, backup, insurance. No prices or statistics; Law Society/PIPA statements kept general with a defer-to-regulator note.
- Added to `blog/index.html` (list + JSON-LD), `sitemap.xml`, and linked from `/industries/law-firms`.
- Target keywords: IT requirements new law firm BC, law firm IT setup checklist BC, Law Society of BC cloud computing.
- Next steps: `/industries/medical-clinics` and `/industries/dental` pages; "Is Clio secure enough for Law Society of BC rules" post; link law-firms page from location pages; shorten long titles flagged by the audit (blog posts mostly); owner to verify Law Society wording.

## 2026-10-09
- New vertical page `/industries/medical-clinics` (Service + FAQPage + Breadcrumb JSON-LD): EMR environments (OSCAR Pro, Accuro, TELUS PS Suite, Med Access named only as software we support around, not partnerships), PIPA/PIPEDA safeguards, backups, ransomware readiness, e-fax, imaging, front-desk reliability. Regulators described generally with a defer-to-college/counsel note; no prices, stats or clients.
- Linked from `industries.html` clinic section, `industries/law-firms`, and all 10 location pages (short cross-link sentence only; no city-swapped content). Added to `sitemap.xml`.
- Target keywords: IT support medical clinics BC, dental office IT support Lower Mainland, EMR IT support BC, clinic managed IT.
- Next steps: `/industries/dental` page only if it can be distinct (dental imaging, practice software); blog "EMR backup best practices for BC clinics"; "Is Clio secure enough for Law Society of BC rules" post; give location pages genuinely local content; shorten long titles flagged by audit (blog posts, services description 204 chars); owner to confirm college names and which EMRs the team actually supports.

## 2026-10-10
- Audit: 0 errors at start (52 length/lastmod warnings, mostly pre-existing).
- New blog post `/blog/emr-backup-best-practices-bc-clinics` (~1,400 words, BlogPosting + Breadcrumb JSON-LD): hosted vs on-prem EMR, RPO/RTO, 3-2-1 plus isolated copy, what to include, encryption, restore testing, monitoring, recovery runbook, checklist. No prices, stats or clients; regulator references general with defer-to-advisors note. CTA: free IT assessment + phone.
- Added to `blog/index.html` (list + JSON-LD) and `sitemap.xml`; linked from `/industries/medical-clinics`; bumped lastmod for blog index and medical-clinics.
- Target keywords: EMR backup best practices BC, clinic backup ransomware BC, EMR disaster recovery.
- Next steps: "Is Clio secure enough for Law Society of BC rules" post; `/industries/dental` only if distinct; genuinely local content for location pages; stale sitemap lastmods (52 audit warnings); owner to confirm which EMRs/backup tools the team supports (TODO comment in post).

## 2026-10-11
- Audit: 0 errors at start (45 mostly lastmod/length warnings).
- New blog post `/blog/clio-law-society-bc-security` (~1,350 words, BlogPosting + Breadcrumb JSON-LD): vendor-vs-firm security layers, due-diligence questions, configuration baseline (MFA, least privilege, offboarding), trust-accounting safeguards, email/devices, checklist and FAQ. No prices, stats or clients; Law Society/PIPA statements general with defer-to-regulator note; TODO owner comments for linking current Law Society guidance, trust-accounting products and data residency.
- Added to `blog/index.html` (list + JSON-LD) and `sitemap.xml`; linked from `/industries/law-firms`; bumped lastmod for blog index and law-firms.
- Target keywords: is Clio secure BC, Law Society of BC cloud computing, law firm practice management security.
- Next steps: `/industries/dental` only if distinct; genuinely local content for location pages; stale sitemap lastmods; owner to review Law Society wording and TODOs.

## 2026-10-12
- Audit: 0 errors at start (44 mostly lastmod warnings).
- New vertical page `/industries/dental` (Service + FAQPage + Breadcrumb JSON-LD): practice software (Dentrix, Eaglesoft, Open Dental named only as software supported around, not partnerships), digital imaging, backups, privacy, ransomware, new builds. Uses owner-confirmed pricing ($95/user/month, min 5, 1-year, extras billed separately, free on-site if not fixable remotely) and free assessment (within 300 km of Abbotsford or remote). CTA: Book a free IT assessment + phone.
- Linked from `industries.html` and `/industries/medical-clinics` (whose CTA now reads "Book a free IT assessment"); added to `sitemap.xml`; bumped lastmod for industries and medical-clinics.
- Target keywords: IT support dental office BC, dental IT Lower Mainland, managed IT dentist Abbotsford, orthodontist IT support.
- Next steps: `/industries/physiotherapy` (or allied health) and `/industries/veterinary` only if distinct; genuinely local content for location pages; stale sitemap lastmods; owner to confirm dental software experience (TODO in page) and add pricing/CTA facts to law-firms page.

## 2026-10-13
- Audit: 0 errors at start (47 mostly lastmod warnings); 0 errors at end.
- New vertical page `/industries/allied-health` (Service + FAQPage + Breadcrumb JSON-LD) for physiotherapy, chiropractic, massage, naturopathic and counselling/psychology clinics: booking/charting access, confidential notes on devices, shared-space network segmentation, practitioner-owned devices, virtual care setup, backups, ransomware. Owner-confirmed pricing and free assessment facts used; no product names, clients, stats. Owner confirmed (follow-up): supports all major booking/charting products; custom billing for clinics under 5 users.
- Linked from `industries.html`, `/industries/medical-clinics`, `/industries/dental`; added to `sitemap.xml`; bumped lastmod for industries and medical-clinics.
- Target keywords: IT support physiotherapy clinic BC, chiropractor IT support, counselling office IT security, allied health managed IT Lower Mainland.
- Next steps: `/industries/veterinary` only if distinct; add pricing/CTA facts to law-firms page; genuinely local content for location pages; stale lastmods; owner to resolve TODOs.
- Owner request: added "custom billing for fewer than 5 users" (same $95/user/month structure otherwise) to every page that states pricing: services.html (Offer JSON-LD, pricing card, pricing line), free-it-assessment.html (FAQ + JSON-LD), industries/dental, industries/allied-health.

## 2026-10-14
- Audit: 0 errors at start (50 mostly lastmod warnings).
- `/industries/law-firms`: added owner-confirmed pricing section ($95/user/month, min 5, 1-year, remote business hours, M365/after-hours/on-site billed separately, free on-site if not fixable remotely, custom billing under 5 users) and free assessment details (on site within 300 km of Abbotsford, or remote). Added two FAQ entries (cost, on-site assessment) to visible FAQ and FAQPage JSON-LD. Main CTA is now "Book a free IT assessment" plus "Call (236) 258-3060" in body and bottom CTA.
- Sitemap lastmod bumped for law-firms and dental (dental was stale vs 2026-10-13 edit).
- Target keywords: law firm IT support cost BC, managed IT law firm Abbotsford, IT assessment law office.
- Next steps: `/industries/veterinary` only if distinct; genuinely local content for location pages (check other logs first); stale lastmods on blog/location pages; owner to review Law Society wording and TODOs.

## 2026-10-15
- Audit: 0 errors at start (49 mostly lastmod warnings).
- New vertical page `/industries/veterinary` (Service + FAQPage + Breadcrumb JSON-LD): distinct angle on clinical equipment networks (digital X-ray, ultrasound, lab analyzers), image archive backups, practice software, kennel/surgery environments, mobile/satellite sites. Owner-confirmed pricing (incl. custom billing under 5 users) and free assessment facts used; no clients, stats or product names. Owner confirmed (follow-up): supports all major veterinary software, now stated on the page, TODO removed; College of Veterinarians of BC referenced generally).
- Linked from `industries.html`, medical-clinics, dental, allied-health; added to `sitemap.xml`; bumped lastmod for those pages.
- Target keywords: IT support veterinary clinic BC, animal hospital IT Lower Mainland, vet clinic managed IT Abbotsford.
- Next steps: genuinely local content for location pages (check other logs first); stale lastmods on blog/location pages; owner to resolve TODOs (vet software, Law Society wording).

## 2026-10-16
- Audit: 0 errors at start (50 mostly lastmod warnings); 0 errors at end.
- `/locations/abbotsford`: shortened title/description; added owner-confirmed pricing section, free IT assessment section (within 300 km of Abbotsford, or remote), links to all five healthcare/legal industry pages plus the EMR backup and Clio blog posts, FAQ section with FAQPage JSON-LD, and CTAs "Book a free IT assessment" + phone. No invented local facts.
- Sitemap lastmod bumped for abbotsford.
- Target keywords: managed IT Abbotsford, IT support Abbotsford BC, IT support clinics Abbotsford, law firm IT Abbotsford.
- Next steps: same treatment (pricing, assessment, vertical links, FAQ) for chilliwack/mission/langley/surrey, keeping each genuinely distinct (needs owner-supplied local facts, see TODO); stale blog/location lastmods; owner to resolve TODOs.

## 2026-10-17
- Audit: 0 errors at start (51 mostly lastmod warnings).
- `/locations/chilliwack`: shortened title/description; added owner-confirmed pricing section, free IT assessment section (within 300 km of Abbotsford, or remote), links to all five healthcare/legal industry pages plus the EMR backup and Clio posts, FAQ with FAQPage JSON-LD (stated honestly that there is no Chilliwack office), CTAs "Book a free IT assessment" + phone. No invented local facts.
- Sitemap lastmod bumped for chilliwack.
- Target keywords: managed IT Chilliwack, IT support Chilliwack BC, clinic IT Chilliwack, law firm IT Chilliwack.
- Next steps: same treatment for mission/langley/surrey (then others); stale blog/location lastmods; owner-supplied local facts would make these pages more distinct; owner to resolve TODOs.

## 2026-10-18
- Audit: 0 errors at start (51 mostly lastmod warnings); 0 errors at end.
- `/locations/mission`: shortened title/description; added owner-confirmed pricing section, free IT assessment section (within 300 km of Abbotsford, or remote), links to all five healthcare/legal industry pages plus the EMR backup and Clio posts, FAQ with FAQPage JSON-LD (honest that there is no Mission office), CTAs "Book a free IT assessment" + phone. No invented local facts.
- Sitemap lastmod bumped for mission.
- Target keywords: managed IT Mission BC, IT support Mission BC, clinic IT Mission, law firm IT Mission.
- Next steps: same treatment for langley/surrey (then maple-ridge and others); stale blog/location lastmods; owner-supplied local facts would make these pages more distinct; owner to resolve TODOs.

## 2026-10-19
- Audit: 0 errors at start (51 mostly lastmod/length warnings).
- (Mission was already done and merged on 2026-10-18; this run took the next item.)
- `/locations/langley`: shortened title/description; added owner-confirmed pricing section, free IT assessment section (within 300 km of Abbotsford, or remote), links to all five healthcare/legal industry pages plus the EMR backup and Clio posts, FAQ with FAQPage JSON-LD (honest that there is no Langley office), CTAs "Book a free IT assessment" + phone. Existing drive-time and sector copy kept; no new local facts invented.
- Sitemap lastmod bumped for langley.
- Target keywords: managed IT Langley BC, IT support Langley BC, clinic IT Langley, law firm IT Langley.
- Next steps: same treatment for surrey, then maple-ridge and others; stale blog/location lastmods; owner-supplied local facts would make these pages more distinct; owner to resolve TODOs.

## 2026-10-20
- Audit: 0 errors at start (50 mostly lastmod warnings).
- `/locations/surrey`: shortened title/description; added owner-confirmed pricing section, free IT assessment section (within 300 km of Abbotsford, or remote), links to all five healthcare/legal industry pages plus the EMR backup and Clio posts, FAQ with FAQPage JSON-LD (honest that there is no Surrey office), CTAs "Book a free IT assessment" + phone. Kept existing drive-time/sector copy; no new local facts invented.
- Sitemap lastmod bumped for surrey.
- Target keywords: managed IT Surrey BC, IT support Surrey BC, clinic IT Surrey, law firm IT Surrey.
- Next steps: same treatment for maple-ridge, then vancouver/burnaby/new-westminster/north-vancouver; stale blog/location lastmods; owner-supplied local facts would make these pages more distinct; owner to resolve TODOs.

## 2026-10-21
- Audit: 0 errors at start (49 warnings).
- `/locations/maple-ridge`: shortened title/description; added owner-confirmed pricing section, free IT assessment section (within 300 km of Abbotsford, or remote), links to all five healthcare/legal industry pages plus the EMR backup and Clio posts, FAQ with FAQPage JSON-LD (honest that there is no Maple Ridge office), CTAs "Book a free IT assessment" + phone. Kept existing drive-time/sector copy; no new local facts invented.
- Sitemap lastmod bumped for maple-ridge.
- Target keywords: managed IT Maple Ridge BC, IT support Maple Ridge BC, clinic IT Maple Ridge, law firm IT Maple Ridge.
- Next steps: same treatment for vancouver/burnaby/new-westminster/north-vancouver; stale blog/location lastmods; owner-supplied local facts would make these pages more distinct; owner to resolve TODOs.

## 2026-10-22
- Audit: 0 errors at start (47 mostly lastmod warnings).
- `/locations/vancouver`: shortened title/description; added owner-confirmed pricing section, free IT assessment section (within 300 km of Abbotsford, or remote), links to all five healthcare/legal industry pages plus the EMR backup and Clio posts, FAQ with FAQPage JSON-LD (honest that there is no Vancouver office), CTAs "Book a free IT assessment" + phone. Kept existing travel-time copy; no new local facts invented.
- Sitemap lastmod bumped for vancouver.
- Target keywords: managed IT Vancouver BC, IT support Vancouver BC, clinic IT Vancouver, law firm IT Vancouver.
- Next steps: same treatment for burnaby/new-westminster/north-vancouver; stale blog/location lastmods; owner-supplied local facts would make these pages more distinct; owner to resolve TODOs.

## 2026-10-25
- Audit: 0 errors at start (46 mostly lastmod warnings).
- `/locations/burnaby`: shortened title/description; added owner-confirmed pricing section, free IT assessment section (within 300 km of Abbotsford, or remote), links to all five healthcare/legal industry pages plus the EMR backup and Clio posts, FAQ with FAQPage JSON-LD (honest that there is no Burnaby office), CTAs "Book a free IT assessment" + phone. Kept existing travel-time copy; no new local facts invented.
- Sitemap lastmod bumped for burnaby.
- Target keywords: managed IT Burnaby BC, IT support Burnaby BC, clinic IT Burnaby, law firm IT Burnaby.
- Next steps: same treatment for new-westminster and north-vancouver; stale blog/location lastmods; owner-supplied local facts would make these pages more distinct; owner to resolve TODOs.

## 2026-10-26
- Audit: 0 errors at start (44 mostly lastmod warnings); 0 errors at end.
- `/locations/new-westminster`: shortened title/description; added owner-confirmed pricing section, free IT assessment section (within 300 km of Abbotsford, or remote), links to all five healthcare/legal industry pages plus the EMR backup and Clio posts, FAQ with FAQPage JSON-LD (honest that there is no New Westminster office), CTAs "Book a free IT assessment" + phone. Kept existing intro and travel-time copy; no new local facts invented.
- Sitemap lastmod bumped for new-westminster.
- Target keywords: managed IT New Westminster BC, IT support New Westminster, clinic IT New Westminster, law firm IT New Westminster.
- Next steps: same treatment for north-vancouver; stale blog/location lastmods; owner-supplied local facts would make these pages more distinct; owner to resolve TODOs.

## 2026-10-26 (second run)
- `/locations/north-vancouver`: shortened title/description; added owner-confirmed pricing section, free IT assessment section (within 300 km of Abbotsford, or remote), links to all five healthcare/legal industry pages plus the EMR backup and Clio posts, FAQ with FAQPage JSON-LD (honest that there is no North Vancouver office), CTAs "Book a free IT assessment" + phone. Kept existing travel-time copy; no new local facts invented.
- Sitemap lastmod bumped for north-vancouver. This completes the pricing/assessment/FAQ treatment for all Lower Mainland city pages.
- Target keywords: managed IT North Vancouver BC, IT support North Vancouver, clinic IT North Vancouver, law firm IT North Vancouver.
- Next steps: build `/managed-it-services` and `/business-it-support` pillar pages (A priority, still todo in keyword-map); stale blog lastmods; owner-supplied local facts; owner to resolve TODOs.
