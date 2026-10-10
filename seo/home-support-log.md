# Home support SEO log

Separate from the business/MSP SEO work. Scope: `/home-support/` URLs only.

## 2026-10-07
- Built the hub `/home-support/` ("Remote Tech Support for Home Users Across Canada, $100 flat"): above-the-fold call CTA, brand disclaimer (top and bottom), permission/end-session statement, how-it-works, FAQ, Service + Offer ($100 CAD, areaServed Canada) + FAQPage + Breadcrumb JSON-LD.
- Added "Home tech support" link to the footer of every page, plus a pointer on `services.html`, and the hub URL in `sitemap.xml`.
- Note: `scripts/seo_audit.py` does not exist on `main`, so the audit could not be run; checked links/JSON-LD manually.
- Open owner question (TODO comment in hub): what happens if a problem cannot be fixed remotely; which remote tool is used.
- Target keywords: remote tech support Canada, online computer help, home tech support Canada.

### Next steps
1. `/home-support/printer-help` (then `printer-help/hp`, brother, canon)
2. `/home-support/wifi-router-help` and `wifi-extender-setup`
3. `/home-support/computer-help`, `virus-removal`, `software-help`
4. Blog: "Why does my printer say offline?", "How to fix weak Wi-Fi in a Canadian home"
5. Link each child from the hub cards (cards currently anchor to the hub sections).

## 2026-10-08
- Added `/home-support/printer-help/`: above-the-fold call CTA, brand disclaimer (top and bottom), permission/end-session statement, problem cards, a real "printer offline" Windows/Mac self-help checklist, limits of remote support, FAQ, Service + Offer ($100 CAD, areaServed Canada) + HowTo + FAQPage + Breadcrumb JSON-LD.
- Linked it from the hub printer card and the footer "Printer help" link on hub and new page; added to `sitemap.xml`.
- `scripts/seo_audit.py`: 0 errors (warnings pre-exist on other pages).
- Owner confirmed 2026-10-08: no charge if the problem cannot be fixed. Added to printer page and hub; TODO removed (hub still has a TODO on which remote tool is used).
- Target keywords: printer help Canada, printer offline fix, wifi printer setup, remote printer support.
- Note: the footer "Printer help" link on other site pages still points to `/home-support/#printer`; update site-wide when convenient.

### Next steps
1. `/home-support/wifi-router-help` and `wifi-extender-setup`
2. `/home-support/computer-help`, `virus-removal`, `software-help`
3. Brand pages: `printer-help/hp`, `brother`, `canon`
4. Blog: "Why does my printer say offline? Fixes for HP, Brother & Canon", "How to fix weak Wi-Fi in a Canadian home"

## 2026-10-09
- Added `/home-support/wifi-router-help/`: above-the-fold call CTA, brand/ISP disclaimer (top and bottom), permission/end-session statement, problem cards, routers-we-work-with cards (Netgear, TP-Link, ASUS, D-Link, Linksys, Eero, Google Nest Wifi, Rogers/Bell/Telus/Shaw/Videotron), self-help checklist for weak Wi-Fi, limits of remote support, FAQ, Service + Offer ($100 CAD, areaServed Canada) + HowTo + FAQPage + Breadcrumb JSON-LD.
- Linked from the hub Wi-Fi card and the "Wi-Fi & router help" footer link (hub, printer page, new page); added to `sitemap.xml`.
- `scripts/seo_audit.py`: 0 errors.
- Target keywords: wifi router help Canada, fix weak wifi, router setup help, mesh wifi setup.
- Note: the footer "Wi-Fi & router help" link on other site pages (outside /home-support/) may still point to `/home-support/#wifi`; update site-wide when convenient.

### Next steps
1. `/home-support/wifi-extender-setup`
2. `/home-support/computer-help`, `virus-removal`, `software-help`
3. Brand pages: `printer-help/hp`, `brother`, `canon`; `wifi-router-help/tp-link`
4. Blog: "Why does my printer say offline? Fixes for HP, Brother & Canon", "How to fix weak Wi-Fi in a Canadian home"

## 2026-10-10
- Converted the hub, `/home-support/printer-help/` and `/home-support/wifi-router-help/` from "Canada" to "Canada and the USA": titles, meta/OG descriptions, H1s, copy, FAQ, Service JSON-LD `areaServed` (Canada + United States) and `hoursAvailable` (Mon–Fri 08:00–20:00).
- Added to each page: hours block (Pacific Time with Mountain/Central/Eastern/Atlantic equivalents), CAD-to-USD card-conversion note, BC phone note for US callers, the "never call/text/email first, no pop-ups, no gift card/wire/crypto" statement, and hours in the bottom CTA.
- Added US ISPs (Xfinity, Comcast, Spectrum, AT&T, Verizon Fios, Cox) to the Wi-Fi page card, FAQ and disclaimers; hub disclaimer now names more brands.
- Footer links: only home-support pages carry the "Printer help"/"Wi-Fi & router help" links and they already point to the real pages; other site pages only link the hub, so no site-wide edit was needed.
- `scripts/seo_audit.py`: 0 errors.
- Target keywords: remote tech support USA/Canada, online computer help, printer help, wifi router help (CA and US).
- Owner confirmed (follow-up): remote tools "any connect and quick assist" (name of first tool unclear), all payment methods accepted, 2 sessions per issue. Added visible text to the three pages; TODO remains for tool name, whether 2 sessions fall under one $100 fee, and gift card/wire/crypto policy.

### Next steps
1. `/home-support/seniors` (with "How to spot a tech-support scam")
2. `/home-support/computer-help`, `virus-removal`, `email-help`
3. `phone-tablet-help`, `smart-tv-streaming-help`, `wifi-extender-setup`, `smart-home-camera-help`
4. Brand pages: printer-help/hp, computer-help/mac, wifi-router-help/xfinity, spectrum, tp-link, netgear
