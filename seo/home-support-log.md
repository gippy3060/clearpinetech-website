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
- Owner confirmed (follow-up): remote tools "any connect and quick assist" (name of first tool unclear), all payment methods accepted, 2 sessions per issue. Added visible text to the three pages; TODO remains for tool name, whether 2 sessions fall under one $100 fee. Payment resolved: all major cards accepted; never gift card, wire or crypto.

### Next steps
1. `/home-support/seniors` (with "How to spot a tech-support scam")
2. `/home-support/computer-help`, `virus-removal`, `email-help`
3. `phone-tablet-help`, `smart-tv-streaming-help`, `wifi-extender-setup`, `smart-home-camera-help`
4. Brand pages: printer-help/hp, computer-help/mac, wifi-router-help/xfinity, spectrum, tp-link, netgear

## 2026-10-11
- Added `/home-support/seniors/` ("Patient Remote Computer Help for Seniors"): large call buttons (new `.btn-lg` rule in `css/styles.css`), plain-language "what to expect" steps, problem cards, family-can-join/book section, "How to spot a tech-support scam" (with CAFC and ReportFraud.ftc.gov reporting), FAQ, safety promises, price/CAD note, hours, BC phone note, brand disclaimer top and bottom, Service + Offer + FAQPage + Breadcrumb JSON-LD.
- Linked from hub intro and the footer of the three home-support pages; added to `sitemap.xml`.
- Target keywords: online tech support for seniors, computer help for seniors (CA and US), tech help for elderly parents.
- Owner confirmed 2026-10-11: remote tools are Quick Assist (Windows) and LogMeIn (Mac); two sessions for the same issue are covered by the one $100 CAD fee. Added to all four pages, TODOs removed.

### Next steps
1. `/home-support/computer-help`, `virus-removal` (incl. scam clean-up), `email-help`
2. `phone-tablet-help`, `smart-tv-streaming-help`, `wifi-extender-setup`, `smart-home-camera-help`
3. Brand pages: printer-help/hp, computer-help/mac, wifi-router-help/xfinity, spectrum, tp-link, netgear
4. Blog: "How to tell if a tech support call is a scam"

## 2026-10-12
- Added `/home-support/computer-help/` ("Remote Computer Help for Windows and Mac"): large call buttons, services cards (slow computer, new computer setup, software, Microsoft 365, backups, antivirus), a real Windows/Mac slow-computer checklist, honest limits of remote support (failed drives need a lab), FAQ, price/CAD note, hours, BC phone note, brand disclaimer top and bottom, Service + Offer + FAQPage + Breadcrumb JSON-LD.
- Linked from the hub computer card; footer "Computer help" link on all home-support pages now points to the real page; added to `sitemap.xml`.
- `scripts/seo_audit.py`: 0 errors.
- Target keywords: remote computer help, slow computer fix, new computer setup help, Microsoft 365 help (CA and US).

### Next steps
1. `/home-support/virus-removal` (incl. scam clean-up), `email-help`
2. `phone-tablet-help`, `smart-tv-streaming-help`, `wifi-extender-setup`, `smart-home-camera-help`
3. Brand pages: computer-help/mac, printer-help/hp, wifi-router-help/xfinity, spectrum, tp-link, netgear
4. Blog: "How to tell if a tech support call is a scam"

## 2026-10-13
- Added `/home-support/virus-removal/` ("Virus, Pop-up and Scam Clean-up Help"): large call buttons, problem cards (fake virus pop-ups, browser hijacks, remote-access software left by scammers, account security), a "do this first" checklist if a scammer had access (disconnect, call bank, change passwords from another device, report to the Canadian Anti-Fraud Centre / ReportFraud.ftc.gov), honest limits (cannot recover money, cannot guarantee every threat found), FAQ, price/CAD note, hours, BC phone note, brand disclaimer top and bottom, Service + Offer + FAQPage + Breadcrumb JSON-LD.
- Linked from the hub intro, computer-help FAQ and the footer of all home-support pages; added to `sitemap.xml`.
- `scripts/seo_audit.py`: 0 errors.
- Target keywords: virus removal help, fake virus pop-up, remove scammer remote access, tech support scam clean-up (CA and US).

### Next steps
1. `/home-support/email-help`
2. `phone-tablet-help`, `smart-tv-streaming-help`, `wifi-extender-setup`, `smart-home-camera-help`
3. Brand pages: computer-help/mac, printer-help/hp, wifi-router-help/xfinity, spectrum, tp-link, netgear
4. Blog: "How to tell if a tech support call is a scam"

## 2026-10-14
- Added `/home-support/email-help/` ("Remote Email and Account Help"): large call buttons, problem cards (Outlook/Gmail/Yahoo/iCloud setup, email stopped working, locked-out accounts, passwords, two-factor, contacts/full mailbox), a "try this first" checklist, honest limits (we cannot reset or unlock accounts; only the provider can), FAQ incl. phishing-style "account will be closed" emails, price/CAD note, hours, BC phone note, brand disclaimer top and bottom, Service + Offer + FAQPage + Breadcrumb JSON-LD.
- Linked from the hub computer card and computer-help page; "Email help" added to the footer of all home-support pages; added to `sitemap.xml`.
- Target keywords: email help, Outlook setup help, Gmail locked out, Yahoo mail not working, two-factor setup help (CA and US).

### Next steps
1. `phone-tablet-help`, `smart-tv-streaming-help`, `wifi-extender-setup`, `smart-home-camera-help`
2. Brand pages: computer-help/mac, printer-help/hp, wifi-router-help/xfinity, spectrum, tp-link, netgear
3. Blog: "How to tell if a tech support call is a scam"

## 2026-10-15
- Added `/home-support/phone-tablet-help/` ("Remote Help with Your Phone or Tablet"): large call buttons, problem cards (new phone setup, moving to a new phone, photos and contacts, email on phone, Wi-Fi/Bluetooth/printing, everyday know-how), a "before you switch phones" checklist, honest limits (phone screen sharing varies; no passcode/activation-lock bypass; no hardware repair), FAQ incl. unexpected-text scam warning, price/CAD note, hours, BC phone note, brand disclaimer top and bottom, Service + Offer + FAQPage + Breadcrumb JSON-LD.
- Linked from the hub and "Phone & tablet help" added to the footer of all home-support pages; added to `sitemap.xml`.
- `scripts/seo_audit.py`: 0 errors.
- Target keywords: iPhone setup help, move to new phone, transfer photos to new phone, Android help, iPad help (CA and US).

### Next steps
1. `smart-tv-streaming-help`, `wifi-extender-setup`, `smart-home-camera-help`
2. Brand pages: computer-help/mac, printer-help/hp, wifi-router-help/xfinity, spectrum, tp-link, netgear
3. Blog: "How to tell if a tech support call is a scam", "How to move everything to a new iPhone"
- Owner confirmed 2026-10-15: phone support is offered by voice and with TeamViewer on phones/tablets. Updated phone-tablet-help (FAQ + JSON-LD, limits, "How we connect"); TODO resolved.

## 2026-10-16
- Added `/home-support/smart-tv-streaming-help/` ("Smart TV and Streaming Help, Over the Phone"): large call buttons, problem cards (TV Wi-Fi, Roku/Fire TV/Apple TV/Chromecast setup, apps and sign-ins, buffering, sound/remotes, casting), a "TV won't connect to Wi-Fi" checklist, honest limits (TVs guided by voice, no repairs, no pirated streams or subscriptions), FAQ, price/CAD note, hours, BC phone note, brand disclaimer top and bottom, Service + Offer + FAQPage + Breadcrumb JSON-LD.
- Linked from the hub intro and added "Smart TV & streaming help" to the footer of all home-support pages; added to `sitemap.xml`.
- `scripts/seo_audit.py`: 0 errors.
- Target keywords: smart TV won't connect to Wi-Fi, Roku setup help, Fire TV help, Chromecast setup, streaming keeps buffering (CA and US).
- Note: the page says TVs are helped by voice only (TeamViewer/Quick Assist/LogMeIn are not confirmed for TVs).

### Next steps
1. `wifi-extender-setup`, `smart-home-camera-help` (then update TV page to link the extender page)
2. Brand pages: computer-help/mac, printer-help/hp, wifi-router-help/xfinity, spectrum, tp-link, netgear
3. Blog: "How to tell if a tech support call is a scam", "Why does my printer say offline?"

## 2026-10-17
- Added `/home-support/wifi-extender-setup/` ("Wi-Fi Extender and Mesh Setup Help"): large call buttons, problem cards (extender vs mesh, placement, reconnecting devices, slow Wi-Fi in one room), a weak-Wi-Fi checklist (test in two places, router position, extender halfway), honest limits (no equipment sold, can't speed up the plan or fix provider issues), FAQ, price/CAD note, hours, BC phone note, brand disclaimer top and bottom, Service + Offer + FAQPage + Breadcrumb JSON-LD.
- Linked from the hub, Wi-Fi router page ("Mesh and extenders" card), smart TV page; "Wi-Fi extender setup" added to the footer of all home-support pages; added to `sitemap.xml`.
- Target keywords: wifi extender setup help, mesh wifi setup, wifi weak upstairs, wifi dead spots (CA and US).

### Next steps
1. `smart-home-camera-help` (Ring, Arlo, Google Nest)
2. Brand pages: computer-help/mac, printer-help/hp, wifi-router-help/xfinity, spectrum, tp-link, netgear
3. Blog: "How to tell if a tech support call is a scam", "Why does my printer say offline?", "Why is my Wi-Fi slow upstairs?"

## 2026-10-19
- Added `/home-support/smart-home-camera-help/` ("Doorbell, Camera and Smart Home Help"): large call buttons, problem cards (camera/doorbell offline, new device setup, reconnecting after a new router, alerts and sharing, Echo/Nest speakers, account security), a "camera offline" checklist, honest limits (no mounting, wiring or hardware repair; no access to other people's accounts; no equipment or subscriptions sold), FAQ incl. fake "your camera was hacked" message warning, price/CAD note, hours, BC phone note, brand disclaimer (Ring, Amazon Echo, Arlo, Google Nest) top and bottom, Service + Offer + FAQPage + Breadcrumb JSON-LD.
- Linked from the hub intro and the Wi-Fi extender page; "Smart home & camera help" added to the footer of all home-support pages; added to `sitemap.xml`.
- Target keywords: Ring doorbell offline help, Arlo camera offline, Nest camera won't connect, security camera setup help, smart speaker setup help (CA and US).

### Next steps
1. Brand pages: computer-help/mac, printer-help/hp, wifi-router-help/xfinity, spectrum, tp-link, netgear
2. Blog: "How to tell if a tech support call is a scam", "Why does my printer say offline?", "Why is my Wi-Fi slow upstairs?"
3. Later: ring/arlo/nest brand pages under smart-home-camera-help.
