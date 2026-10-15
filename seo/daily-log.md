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
- New vertical page `/industries/veterinary` (Service + FAQPage + Breadcrumb JSON-LD): distinct angle on clinical equipment networks (digital X-ray, ultrasound, lab analyzers), image archive backups, practice software, kennel/surgery environments, mobile/satellite sites. Owner-confirmed pricing (incl. custom billing under 5 users) and free assessment facts used; no clients, stats or product names (TODO owner comment for veterinary software experience; College of Veterinarians of BC referenced generally).
- Linked from `industries.html`, medical-clinics, dental, allied-health; added to `sitemap.xml`; bumped lastmod for those pages.
- Target keywords: IT support veterinary clinic BC, animal hospital IT Lower Mainland, vet clinic managed IT Abbotsford.
- Next steps: genuinely local content for location pages (check other logs first); stale lastmods on blog/location pages; owner to resolve TODOs (vet software, Law Society wording).
