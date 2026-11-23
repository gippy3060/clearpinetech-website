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

## 2026-10-21
- Added first brand page `/home-support/printer-help/hp/` ("Independent Help with Your HP Printer, $100 CAD Flat"): large call buttons, HP-specific problem cards and offline checklist (wireless light states, wireless test report, HP Smart app, HP's free Print and Scan Doctor on Windows), HP account / HP+ and cartridge-rule notes, honest limits, FAQ, price/CAD note, hours, BC phone note, HP-only disclaimer top and bottom, Service + Offer + FAQPage + Breadcrumb JSON-LD.
- Linked from a new "HP printers" card on `/home-support/printer-help/`; added to `sitemap.xml`.
- Target keywords: HP printer offline, HP Smart app help, HP printer Wi-Fi setup, HP printer scanning help (CA and US).

### Next steps
1. Brand pages: computer-help/mac, wifi-router-help/xfinity, spectrum, tp-link, netgear, printer-help/brother, canon, epson, computer-help/dell
2. Blog: "How to tell if a tech support call is a scam", "Why does my printer say offline?", "Why is my Wi-Fi slow upstairs?"
3. Later: ring/arlo/nest brand pages under smart-home-camera-help.

## 2026-10-22
- Added brand page `/home-support/computer-help/mac/` ("Independent Help with Your Mac, $100 CAD Flat"): large call buttons, Mac problem cards (slow Mac, storage full, macOS updates, new Mac setup with Migration Assistant, Time Machine backups), a slow-Mac checklist (restart, Storage, Login Items, Activity Monitor, updates, warning about "cleaner" pop-ups), Apple ID / older-Mac notes, honest limits (no hardware repair, cannot reset Apple ID or Mac passwords), FAQ, price/CAD note, hours, BC phone note, Apple-only disclaimer top and bottom, Service + Offer + FAQPage + Breadcrumb JSON-LD.
- Linked from `/home-support/computer-help/`; added to `sitemap.xml`.
- Target keywords: Mac running slow, Mac storage full, new Mac setup help, Migration Assistant help, macOS update stuck (CA and US).

### Next steps
1. Brand pages: wifi-router-help/xfinity, spectrum, tp-link, netgear, printer-help/brother, canon, epson, computer-help/dell
2. Blog: "How to tell if a tech support call is a scam", "Why does my printer say offline?", "Why is my Wi-Fi slow upstairs?"
3. Later: ring/arlo/nest brand pages under smart-home-camera-help.

## 2026-10-25
- Added brand page `/home-support/wifi-router-help/xfinity/` ("Independent Help with Your Xfinity Wi-Fi, $100 CAD Flat"): large call buttons, Xfinity problem cards (slow/dropping Wi-Fi, weak rooms, new password, Xfinity app, own router, screen-time pauses), a "slow or not working" checklist that separates home-signal problems from provider outages, Xfinity-specific notes (rented gateway vs own equipment, password change affects all devices, we never ask for the Xfinity account password), honest limits (no line/outage fixes, no account or billing changes), a "caller claiming to be your provider" warning, FAQ, price/CAD note, hours, BC phone note, Xfinity/Comcast-only disclaimer top and bottom, Service + Offer + FAQPage + Breadcrumb JSON-LD.
- Gateway light colours deliberately not described (vary by model; page points to Xfinity's own guide).
- Linked from the Xfinity/Spectrum card on `/home-support/wifi-router-help/`; added to `sitemap.xml`.
- Target keywords: Xfinity Wi-Fi slow, Xfinity Wi-Fi keeps dropping, change Xfinity Wi-Fi password, Xfinity own router help (US).

### Next steps
1. Brand pages: wifi-router-help/spectrum, tp-link, netgear, printer-help/brother, canon, epson, computer-help/dell
2. Blog: "How to tell if a tech support call is a scam", "Why does my printer say offline?", "Why is my Wi-Fi slow upstairs?"
3. Later: ring/arlo/nest brand pages under smart-home-camera-help.

## 2026-10-26
- Added brand page `/home-support/wifi-router-help/spectrum/` ("Independent Help with Your Spectrum Wi-Fi, $100 CAD Flat"): large call buttons, Spectrum problem cards (slow/dropping Wi-Fi, weak rooms, new password, My Spectrum app, own router, screen time), a "slow or not working" checklist (restart modem then router, cable test, outage check), Spectrum-specific notes (Spectrum-supplied equipment vs own, password change affects every device, we never ask for the Spectrum account password), honest limits, provider-impersonation warning, FAQ, price/CAD note, hours, BC phone note, Spectrum/Charter-only disclaimer top and bottom, Service + Offer + FAQPage + Breadcrumb JSON-LD.
- Unconfirmed claims (remote tool, payment methods, follow-up session) deliberately left out and marked with TODO comments. Note: the Xfinity page and possibly earlier pages still contain a "Remote tools" paragraph (Quick Assist/LogMeIn) and a payment/"up to two sessions" sentence that the owner has not confirmed; recommend a clean-up pass.
- Linked from the Xfinity/Spectrum card on `/home-support/wifi-router-help/`; added to `sitemap.xml`.
- Target keywords: Spectrum Wi-Fi slow, Spectrum Wi-Fi keeps dropping, change Spectrum Wi-Fi password, Spectrum own router help (US).

### Next steps
1. Clean-up pass: remove unconfirmed remote-tool/payment/two-session claims from earlier pages (or get owner confirmation).
2. Brand pages: wifi-router-help/tp-link, netgear, printer-help/brother, canon, epson, computer-help/dell
3. Blog: "How to tell if a tech support call is a scam", "Why does my printer say offline?", "Why is my Wi-Fi slow upstairs?"

## 2026-10-27
- Added brand page `/home-support/wifi-router-help/tp-link/` ("Independent Help with Your TP-Link Router or Deco, $100 CAD Flat"): large call buttons, problem cards (new Archer router, Deco mesh setup, weak rooms, replacing an old router, firmware, parental controls), a "slow or not working" checklist (cable to modem, restart order, Deco/Tether app, unit placement, cable test, factory-reset caution), TP-Link-specific notes (Archer vs Deco, TP-Link ID, double Wi-Fi behind provider equipment), honest limits, FAQ, price/CAD note, hours, BC phone note, TP-Link-only disclaimer top and bottom, Service + Offer + FAQPage + Breadcrumb JSON-LD. LED colours deliberately not described.
- Linked from the TP-Link card on `/home-support/wifi-router-help/`; added to `sitemap.xml`.
- `scripts/seo_audit.py`: 0 errors.
- Target keywords: TP-Link router setup help, TP-Link Deco setup, TP-Link Wi-Fi not working, Deco mesh weak signal (CA and US).
- Remote-tool and payment/follow-up-session TODO comments kept on this page, matching Spectrum (earlier log entries record owner confirmation; the clean-up pass below should reconcile).

### Next steps
1. Clean-up pass: reconcile remote-tool/payment/two-session wording across pages with owner-confirmed facts.
2. Brand pages: wifi-router-help/netgear, printer-help/brother, canon, epson, computer-help/dell
3. Blog: "How to tell if a tech support call is a scam", "Why does my printer say offline?", "Why is my Wi-Fi slow upstairs?"

## 2026-10-30
- Added brand page `/home-support/wifi-router-help/netgear/` ("Independent Help with Your Netgear Router or Orbi, $100 CAD Flat"): large call buttons, Netgear problem cards (new Nighthawk router, Orbi mesh and satellites, weak rooms, replacing an old router, firmware, parental controls with a note that some filtering features are paid subscriptions), a "slow or not working" checklist (cable to modem, restart order, routerlogin.net / Orbi app status, satellite placement halfway, cable test, factory-reset caution), Netgear-specific notes (Nighthawk vs Orbi, Netgear account vs router admin password, double Wi-Fi behind provider equipment), honest limits, FAQ, price/CAD note, hours, BC phone note, Netgear-only disclaimer top and bottom, Service + Offer + FAQPage + Breadcrumb JSON-LD. LED colours deliberately not described.
- Linked from the Netgear card on `/home-support/wifi-router-help/`; added to `sitemap.xml`.
- Target keywords: Netgear router setup help, Netgear Orbi setup, Orbi satellite not connecting, Netgear Wi-Fi not working (CA and US).
- Remote-tool / payment / follow-up-session TODO comments kept on this page, as on TP-Link; clean-up pass still pending.

### Next steps
1. Clean-up pass: reconcile remote-tool/payment/two-session wording across pages with owner-confirmed facts.
2. Brand pages: printer-help/brother, canon, epson, computer-help/dell
3. Blog: "How to tell if a tech support call is a scam", "Why does my printer say offline?", "Why is my Wi-Fi slow upstairs?"

## 2026-11-01
- Added brand page `/home-support/printer-help/brother/` ("Independent Help with Your Brother Printer, $100 CAD Flat"): large call buttons, problem cards (Wi-Fi, offline, scanning, toner/drum messages, phone printing, new router), an "offline: what to check" checklist (screen signal, restart order, WLAN report, same network, Setup Wizard after a Wi-Fi password change, duplicate printer entries, software only from Brother's site), Brother-specific notes (toner vs drum, printer's own label password, all-in-one machines), honest limits, FAQ, price/CAD note, hours, BC phone note, Brother-only disclaimer top and bottom, never-call-first statement, Service + Offer + FAQPage + Breadcrumb JSON-LD.
- Deliberately omitted the unconfirmed remote-tool name, payment methods and "two sessions" wording; TODO comments added on the page.
- Linked from the printer hub and the HP page; added to `sitemap.xml`.
- Target keywords: Brother printer offline, Brother printer won't scan, Brother replace toner message, Brother printer Wi-Fi setup (CA and US).

### Next steps
1. Clean-up pass: remove unconfirmed "Remote tools" (Quick Assist/LogMeIn) and payment/"two sessions" wording from earlier pages (list below).
2. Brand pages: printer-help/canon, epson, computer-help/dell
3. Blog: "How to tell if a tech support call is a scam", "Why does my printer say offline?", "Why is my Wi-Fi slow upstairs?"

## 2026-11-02
- Added brand page `/home-support/printer-help/canon/` ("Independent Help with Your Canon Printer, $100 CAD Flat"): large call buttons, problem cards (Wi-Fi, offline, scanning, ink and print quality, phone printing, new router), an "offline: what to check" checklist (screen/light, restart order, network details, same network, redo Wi-Fi setup or Canon PRINT app, duplicate printer entries, software only from Canon's site), Canon-specific notes (PIXMA/MAXIFY inkjet vs G-series ink tanks vs imageCLASS laser, support codes and which need a repair shop, third-party ink), honest limits, FAQ, price/CAD note, hours, BC phone note, Canon-only disclaimer top and bottom, never-call-first statement, Service + Offer + FAQPage + Breadcrumb JSON-LD. Specific support codes and light colours deliberately not listed (vary by model).
- Linked from the printer hub and the Brother page; added to `sitemap.xml`.
- Unconfirmed remote-tool / payment / follow-up TODO comments kept on the page.
- Target keywords: Canon printer offline, Canon PIXMA won't connect to Wi-Fi, Canon printer won't scan, Canon printer support code (CA and US).

### Next steps
1. Clean-up pass: remove unconfirmed "Remote tools" (Quick Assist/LogMeIn) and payment/"two sessions" wording from earlier pages.
2. Brand pages: printer-help/epson, computer-help/dell
3. Blog: "How to tell if a tech support call is a scam", "Why does my printer say offline?", "Why is my Wi-Fi slow upstairs?"

## 2026-11-03
- Added brand page `/home-support/printer-help/epson/` ("Independent Help with Your Epson Printer, $100 CAD Flat"): large call buttons, problem cards (Wi-Fi, offline, scanning, ink and maintenance box messages, phone printing, new router), an "offline: what to check" checklist, Epson-specific notes (EcoTank refillable tanks vs Expression/WorkForce cartridges, maintenance box, refilling and third-party ink, Epson Smart Panel app), honest limits, FAQ, price/CAD note, hours, BC phone note, Epson-only disclaimer top and bottom, never-call-first statement, Service + Offer + FAQPage + Breadcrumb JSON-LD. Specific error codes and light colours deliberately not listed (vary by model).
- Linked from the printer hub and the Canon page; added to `sitemap.xml`.
- Remote-tool / payment / follow-up TODO comments kept on the page.
- Target keywords: Epson printer offline, Epson EcoTank setup, Epson printer won't scan, Epson maintenance box full (CA and US).
- Not done: clean-up pass. Earlier log entries (2026-10-08 to 10-15) record owner confirmation of Quick Assist/LogMeIn/TeamViewer, card payments and two sessions per fee; the standing brief lists these as unconfirmed. Left as is; owner should confirm (see PR).

### Next steps
1. Owner to confirm remote tools / payment / two-session wording; then reconcile all pages.
2. Brand page: computer-help/dell
3. Blog: "How to tell if a tech support call is a scam", "Why does my printer say offline?", "Why is my Wi-Fi slow upstairs?"

## 2026-11-04
- Added brand page `/home-support/computer-help/dell/` ("Independent Help with Your Dell Computer, $100 CAD Flat"): large call buttons, problem cards (slow Dell, charging and battery, updates and drivers, new setup, backups, pop-ups), a "won't charge: what to check" checklist, Dell-specific notes (Service Tag, drivers from Dell's own site only, preinstalled Dell apps, BIOS caution, older Dells and Windows 11), honest limits, FAQ, price/CAD note, hours, BC phone note, Dell-only disclaimer top and bottom, never-call-first statement, Service + Offer + FAQPage + Breadcrumb JSON-LD.
- Unconfirmed remote tool / payment / follow-up wording omitted; one TODO comment on the page.
- Linked from the computer-help hub and the Mac page; added to `sitemap.xml`.
- Target keywords: Dell laptop slow, Dell laptop not charging, Dell Service Tag, Dell new computer setup (CA and US).

### Next steps
1. Owner to confirm remote tools / payment / two-session wording; then reconcile all pages (Mac page still names LogMeIn and two sessions).
2. Brand pages: Lenovo, HP computers, wifi-router-help/brother-free options (D-Link, Linksys, Eero), ISP pages (Rogers, Bell)
3. Blog: "How to tell if a tech support call is a scam", "Why does my printer say offline?", "Why is my Wi-Fi slow upstairs?"

## 2026-11-05
- Added the first home-user blog post `/blog/is-this-tech-support-call-a-scam` ("How to Tell if a Tech Support Call Is a Scam"): plain-language "if it is happening now" steps, seven warning signs, what to do if they already let someone in or paid, how to judge whether a helper is honest (with a note that the reader needn't choose Clearpine), short Q&A, CAFC and ReportFraud.ftc.gov reporting, price/CAD note, hours, BC phone note, never-call-first statement, Microsoft/Apple non-affiliation disclaimer top and bottom, Breadcrumb + BlogPosting JSON-LD, call buttons top and bottom.
- Linked from the seniors scam section, the virus-removal page and the blog index; added to `sitemap.xml`.
- Target keywords: is this tech support call a scam, how to tell if a tech support call is real, fake virus pop-up what to do, tech support scam what to do if I paid (CA and US).
- Owner TODO comment (remote tool, payment methods, follow-up sessions) kept on the post.

### Next steps
1. Owner to confirm remote tools / payment / two-session wording; then reconcile all pages (Mac page still names LogMeIn and two sessions).
2. Blog: "Why does my printer say offline?", "Why is my Wi-Fi slow upstairs?", "How to move everything to a new iPhone"
3. Brand pages: Lenovo, HP computers, D-Link, Linksys, Eero, ISP pages (Rogers, Bell)

## 2026-11-06
- Added blog post `/blog/why-does-my-printer-say-offline` ("Why Does My Printer Say Offline? Simple Fixes"): plain-language steps (restart everything, same Wi-Fi / guest network, Windows "Use Printer Offline" setting, Mac remove and re-add, Windows re-add), reasons it keeps going offline, when to ask for help, price/CAD note, hours, BC phone note, never-call-first statement, Microsoft/Apple non-affiliation disclaimer top and bottom, Breadcrumb + BlogPosting JSON-LD, call buttons top and bottom.
- Linked from the printer hub and the blog index; added to `sitemap.xml`.
- Target keywords: why does my printer say offline, printer offline Windows 11, printer offline Mac, printer keeps going offline (CA and US).
- Owner TODO comment (remote tool, payment methods) kept on the post.

### Next steps
1. Owner to confirm remote tools / payment / two-session wording; then reconcile all pages (Mac page still names LogMeIn and two sessions).
2. Blog: "Why is my Wi-Fi slow upstairs?", "How to move everything to a new iPhone"
3. Brand pages: Lenovo, HP computers, D-Link, Linksys, Eero, ISP pages (Rogers, Bell)

## 2026-11-09
- Added blog post `/blog/why-is-my-wifi-slow-upstairs` ("Why Is My Wi-Fi Slow Upstairs? Simple Fixes"): why signal fades between floors, five ordered fixes (restart, test next to router, move router, try 2.4 vs 5 band, extender vs mesh), other causes, honest limits (can't move a router or run a cable), price/CAD note, hours, BC phone note, never-call-first statement, Breadcrumb + BlogPosting JSON-LD, call buttons top and bottom. No brands named, so no brand disclaimer needed.
- Linked from the Wi-Fi & router hub and the blog index; added to `sitemap.xml`.
- Target keywords: why is my Wi-Fi slow upstairs, weak Wi-Fi in bedroom, Wi-Fi extender or mesh (CA and US).
- Owner TODO comment (remote tool, payment methods) kept on the post.

### Next steps
1. Owner to confirm remote tools / payment / two-session wording; then reconcile all pages (Mac page still names LogMeIn and two sessions).
2. Blog: "How to move everything to a new iPhone"
3. Brand pages: Lenovo, HP computers, D-Link, Linksys, Eero, ISP pages (Rogers, Bell)

## 2026-11-10
- Added blog post `/blog/how-to-move-everything-to-a-new-iphone` ("How to Move Everything to a New iPhone"): before-you-start checklist, three ways to move (Quick Start phone-to-phone, iCloud backup, Android via Move to iOS), after-the-move checks, common snags, honest limits (no passcode/Apple ID bypass), price/CAD note, hours, BC phone note, never-call-first statement, Apple/Google disclaimer top and bottom, Breadcrumb + BlogPosting JSON-LD.
- Linked from the phone & tablet page checklist and the blog index; added to `sitemap.xml`.
- Target keywords: how to move everything to a new iPhone, transfer old iPhone to new iPhone, Android to iPhone transfer (CA and US).
- Owner TODO comment (remote tool, payment methods) kept on the post.

### Next steps
1. Owner to confirm remote tools / payment / two-session wording; then reconcile all pages (Mac page still names LogMeIn and two sessions).
2. Brand pages: Lenovo, HP computers, D-Link, Linksys, Eero, ISP pages (Rogers, Bell)
3. Later: ring/arlo/nest brand pages; Samsung Galaxy / iPhone brand pages under phone-tablet-help.

## 2026-11-11
- Added brand page `/home-support/computer-help/lenovo/` ("Independent Help with Your Lenovo Computer, $100 CAD Flat"): large call buttons with hours, problem cards (battery stops partway, camera shows black, function keys, slow Lenovo, new setup, pop-ups), a "battery stops at 60 percent or won't charge" checklist (Conservation Mode / charge threshold in Lenovo Vantage, socket, USB-C charging port, charger wattage), Lenovo-specific notes (Vantage, camera privacy cover, Fn + Esc function lock, S/N and MT sticker, drivers from Lenovo only, IdeaPad pinhole recovery button caution), honest limits, FAQ, price/CAD note, hours, BC phone note, family-member note, Lenovo/Dell/Microsoft disclaimer top and bottom, never-call-first statement, Service + Offer + FAQPage + Breadcrumb JSON-LD.
- Linked from the computer-help hub and the Dell page (Dell disclaimers updated to name Lenovo too); added to `sitemap.xml` (hub and Dell lastmod bumped).
- Owner TODO comment (remote tool, payment methods, multi-session) kept on the page.
- Target keywords: Lenovo laptop battery stuck at 60 percent, Lenovo camera not working black screen, Lenovo Fn keys, Lenovo laptop slow, ThinkPad / IdeaPad help (CA and US).

### Next steps
1. Owner to confirm remote tools / payment / two-session wording; then reconcile all pages (Mac page still names LogMeIn and two sessions).
2. Brand pages: HP computers, D-Link, Linksys, Eero, ISP pages (Rogers, Bell)
3. Later: Ring/Arlo/Nest brand pages; Samsung Galaxy / iPhone brand pages under phone-tablet-help.

## 2026-11-12
- Added brand page `/home-support/computer-help/hp/` ("Independent Help with Your HP Computer, $100 CAD Flat"): large call buttons with hours, problem cards (touchpad stopped working, slow HP, updates and drivers, new setup, hardware test, pop-ups), an "HP laptop touchpad not working" checklist (top-left corner double-tap light, touchpad key, Windows Touchpad setting, driver from HP only, swollen-battery warning), HP-specific notes (HP Support Assistant, S/N and P/N sticker, HP PC Hardware Diagnostics via Esc menu, caution on recovery options, trial software), honest limits, FAQ, price/CAD note, hours, BC phone note, family-member note, HP/Dell/Lenovo/Microsoft disclaimer top and bottom, never-call-first statement, Service + Offer + FAQPage + Breadcrumb JSON-LD. Points HP printer visitors to the HP printer page.
- Linked from the computer-help hub, Dell, Lenovo and HP printer pages (Dell and Lenovo disclaimers updated to name HP); added to `sitemap.xml` (lastmod bumped on the linking pages).
- Owner TODO comment (remote tool, payment methods, multi-session) kept on the page.
- Target keywords: HP laptop touchpad not working, HP laptop slow, HP Support Assistant, HP serial number, HP hardware diagnostics, HP Pavilion / EliteBook help (CA and US).

### Next steps
1. Owner to confirm remote tools / payment / two-session wording; then reconcile all pages (Mac page still names LogMeIn and two sessions).
2. Brand pages: D-Link, Linksys, Eero, ISP pages (Rogers, Bell); computers: ASUS, Acer, Microsoft Surface
3. Later: Ring/Arlo/Nest brand pages; Samsung Galaxy / iPhone brand pages under phone-tablet-help.

## 2026-11-13
- Added ISP page `/home-support/wifi-router-help/rogers/` ("Independent Help with Your Rogers Wi-Fi, $100 CAD Flat"), the first Canadian ISP page. It has large call buttons with hours and cards for six problems: slow or dropping Wi-Fi, weak rooms, finding or changing the password, reconnecting devices, moving from Shaw, and using your own router in bridge mode. A "slow or not working" checklist covers restarting the gateway, checking for an outage, testing next to the gateway, placement and the password sticker. Rogers notes cover the gateway being modem plus router, Rogers pods, former Shaw customers in the four western provinces getting Rogers equipment, and the fact that we never ask for the Rogers account password. Also on the page: honest limits, a 7-question FAQ, a warning about callers posing as Rogers (with a link to the CAFC and the scam blog post), price with the CAD note, hours, the BC phone note for US family, the family-member note, the Rogers/Shaw disclaimer at top and bottom, the never-call-first statement at top and bottom, and Service + Offer + FAQPage + Breadcrumb JSON-LD.
- Deliberately left out: exact app names, gateway model names and light colours (these vary and change). The page says "the Rogers app" in general terms.
- Linked from the Canadian ISP card on the Wi-Fi & router hub. Added to `sitemap.xml` and bumped the hub's lastmod.
- Owner TODO comment (remote tool, payment methods, follow-up sessions) is on the page.
- Target keywords (CA): Rogers Wi-Fi slow, Rogers Wi-Fi password, Rogers gateway restart, Rogers pods weak signal, Rogers bridge mode own router, Shaw to Rogers Wi-Fi. Cities: Toronto, Ottawa, Calgary, Edmonton, Vancouver.

### Next steps
1. Owner to confirm remote tools / payment / two-session wording, then reconcile all pages. The Xfinity and Mac pages still name Quick Assist/LogMeIn, and Xfinity still says "all major credit and debit cards" and "up to two sessions".
2. Canadian ISP pages: Bell, Telus, Videotron. Routers: D-Link, Linksys, Eero. Computers: ASUS, Acer, Microsoft Surface.
3. Later: Ring/Arlo/Nest brand pages; Samsung Galaxy / iPhone brand pages under phone-tablet-help.

## 2026-11-14
- Added ISP page `/home-support/wifi-router-help/bell/` ("Independent Help with Your Bell Wi-Fi, $100 CAD Flat"), the second Canadian ISP page. It has large call buttons with hours and cards for six problems: slow or dropping Wi-Fi, weak rooms, finding or changing the password, reconnecting devices, wireless Fibe TV boxes losing their link, and your own router behind the Bell hub. A "slow or not working" checklist covers restarting the Home Hub, checking for an outage, cables (with a warning not to bend the fibre cable), testing next to the hub, and placement. Bell notes cover the Home Hub / Giga Hub being modem plus router, the separate fibre box in some homes, Wi-Fi pods and TV boxes depending on the hub (why your own router usually goes behind it, since a plain bridge mode isn't always offered), and the fact that we never ask for the Bell account password. Also on the page: honest limits (including no Fibe TV service fixes), a 7-question FAQ, a warning about callers posing as Bell (CAFC link and scam blog post), price with the CAD note, hours, the BC phone note, the family-member note, the Bell disclaimer and never-call-first statement at top and bottom, and Service + Offer + FAQPage + Breadcrumb JSON-LD.
- Deliberately left out: exact app names, hub model numbers, light colours and Advanced DMZ steps (these vary by hub and change).
- Linked from the Canadian ISP card on the Wi-Fi & router hub and from the Rogers page. Added to `sitemap.xml`; bumped hub and Rogers lastmod.
- Owner TODO comment (remote tool, payment methods, follow-up sessions) is on the page.
- Target keywords (CA): Bell Wi-Fi slow, Bell Home Hub password, Bell Giga Hub restart, Bell Wi-Fi pods weak signal, Bell Fibe TV box lost connection, own router with Bell. Cities: Toronto, Ottawa, Montreal, Halifax, Winnipeg.

### Next steps
1. Owner to confirm remote tools / payment / two-session wording, then reconcile all pages. The Xfinity and Mac pages still name Quick Assist/LogMeIn, and Xfinity still says "all major credit and debit cards" and "up to two sessions".
2. Canadian ISP pages: Telus, Videotron. Routers: D-Link, Linksys, Eero. Computers: ASUS, Acer, Microsoft Surface.
3. Housekeeping: several home-support sitemap lastmod values are older than the last page change (audit warnings); bump them in a small pass.
4. Later: Ring/Arlo/Nest brand pages; Samsung Galaxy / iPhone brand pages under phone-tablet-help.

## 2026-11-15
- Added ISP page `/home-support/wifi-router-help/telus/` ("Independent Help with Your Telus Wi-Fi, $100 CAD Flat"). Same layout as the Rogers page: large call buttons with hours, six problem cards (slow or dropping Wi-Fi, weak rooms, password, reconnecting devices, moving to PureFibre, your own router), a "slow or not working" checklist (restart the Wi-Fi Hub, leave the fibre cable alone, outage check, test next to the hub, placement, password sticker), Telus notes (Wi-Fi Hub, separate fibre box in some PureFibre homes, Boost Wi-Fi, Telus TV may depend on the hub, we never ask for the Telus account password), honest limits, a 7-question FAQ, a warning about callers posing as Telus (CAFC link and scam blog post), price with the CAD note, hours, BC phone note, family-member note, Telus disclaimer top and bottom, never-call-first statement, and Service + Offer + FAQPage + Breadcrumb JSON-LD.
- Deliberately left out: hub model names, app names and light colours (they vary and change).
- Linked from the Canadian ISP card on the Wi-Fi & router hub; added to `sitemap.xml` and bumped the hub's lastmod.
- Note: the Bell page (branch `seo/home-2026-11-14`) was still unmerged, so it was not repeated. Both branches edit the same hub line and sitemap area; when merging, keep both the Bell and Telus links/URLs.
- Owner TODO comment (remote tool, payment methods, follow-up sessions) is on the page.
- Target keywords (CA): Telus Wi-Fi slow, Telus Wi-Fi Hub password, restart Telus Wi-Fi Hub, Telus Boost Wi-Fi weak signal, Telus PureFibre Wi-Fi help, Telus own router. Cities: Vancouver, Victoria, Calgary, Edmonton.

### Next steps
1. Merge the pending Bell (11-14) and Microsoft 365 (11-12) branches, then link Rogers, Bell and Telus pages to each other.
2. Owner to confirm remote tools / payment / two-session wording, then reconcile all pages (Xfinity and Mac pages still name Quick Assist/LogMeIn; Xfinity still says "all major credit and debit cards" and "up to two sessions").
3. Next ISP/router pages: Videotron, then AT&T, Verizon Fios, Cox; routers: D-Link, Linksys, Eero. Computers: ASUS, Acer, Microsoft Surface.

## 2026-11-17
- Added ISP page `/home-support/wifi-router-help/att/` ("Independent Help with Your AT&T Wi-Fi, $100 CAD Flat"), the third US ISP page after Xfinity and Spectrum. Large call buttons with hours (Central/Eastern equivalents listed first for Texas, Georgia and Florida readers), the never-call-first statement and the AT&T disclaimer at top and bottom. Six problem cards (slow or dropping Wi-Fi, weak rooms, lost/new password, devices that won't connect, AT&T Wi-Fi extenders, your own router behind the gateway). An 8-step "slow or not working" checklist: safe power restart, don't press the reset hole (it can erase a custom Wi-Fi name/password), leave the fiber cable alone, outage check, test next to the gateway, placement, keep the gateway sticker (Wi-Fi password and settings code) private. AT&T notes: gateway = modem + router, Fiber vs older service, own router goes behind the gateway via IP Passthrough with gateway Wi-Fi turned off, AT&T Internet Air uses different equipment, we never ask for the AT&T account password. Honest limits, 7-question FAQ (including "someone called saying they're AT&T"), FTC ReportFraud.ftc.gov link and scam blog link, price with CAD note, hours, BC phone note, family-member/seniors link, Service + Offer + FAQPage + Breadcrumb JSON-LD.
- Deliberately left out: gateway model numbers, light colours, app screen names and the gateway settings address (vary by model and change).
- Linked from the US ISP card on the Wi-Fi & router hub; the page links to the Xfinity and Spectrum pages. Added to `sitemap.xml`; bumped the hub's lastmod.
- Owner TODOs on the page: remote tool, payment methods, follow-up sessions.
- Target keywords (US): AT&T Wi-Fi slow, AT&T Wi-Fi password, restart AT&T gateway, AT&T Fiber Wi-Fi weak upstairs, AT&T Wi-Fi extender setup, own router with AT&T IP Passthrough. Cities: Dallas, Houston, Atlanta, Miami, Chicago, Los Angeles.
- Note: Videotron (branch `seo/home-2026-11-16`) is still unmerged; this branch touches the same hub card area and sitemap neighbourhood. When merging, keep both the Videotron and AT&T links/URLs.

### Next steps
1. Merge pending Videotron (11-16) and Microsoft 365 (11-12) branches; then cross-link the Canadian ISP pages (and add AT&T to the Xfinity/Spectrum pages' related links, updating their disclaimers to name AT&T).
2. Owner to confirm remote tools / payment / two-session wording and French support, then reconcile all pages (Xfinity and Mac pages still name Quick Assist/LogMeIn; Xfinity still says "all major credit and debit cards" and "up to two sessions").
3. US ISP pages: Verizon Fios, Cox. Routers: D-Link, Linksys, Eero. Computers: ASUS, Acer, Microsoft Surface.
4. Housekeeping: bump stale home-support sitemap lastmod values (audit warnings).

## 2026-11-18
- Added ISP page `/home-support/wifi-router-help/verizon-fios/` ("Independent Help with Your Verizon Fios Wi-Fi, $100 CAD Flat"), the fourth US ISP page. Large call buttons with hours (Eastern equivalent listed first for New York / Northeast readers), the never-call-first statement and the Verizon disclaimer at top and bottom. Six problem cards (slow or dropping Wi-Fi, weak rooms, lost/new password, devices that won't connect, Fios extenders, your own router on Fios). An 8-step checklist: safe power restart, don't press the reset hole, leave the fiber box (ONT) alone and check the cable to the router, outage check, test next to the router, placement, keep the router sticker (Wi-Fi password and separate settings password) private. Fios notes: two boxes (ONT + Fios router), a beeping battery backup unit is about home-phone backup and not Wi-Fi or a hacker, your own router can often replace the Fios router but Fios TV boxes may need it (then add your system behind it), 5G Home Internet is different, we never ask for the Verizon account password. Honest limits (no Fios TV fixes), 7-question FAQ (including "what is the box in my garage" and "someone called saying they're Verizon"), FTC link, scam blog link, price with CAD note, hours, BC phone note, family-member/seniors link, Service + Offer + FAQPage + Breadcrumb JSON-LD.
- Deliberately left out: router model names, light colours, settings address and MoCA/coax configuration steps (vary by model and change).
- Linked from the US ISP card on the Wi-Fi & router hub and from the AT&T page. AT&T and Fios disclaimers now name all four US providers they link to. Added to `sitemap.xml`; bumped hub and AT&T lastmod.
- Owner TODOs on the page: remote tool, payment methods, follow-up sessions.
- Target keywords (US): Verizon Fios Wi-Fi slow, Fios router password, restart Fios router, Fios ONT box, Fios battery backup beeping, own router with Fios, Fios extender setup. Cities: New York, Philadelphia, Boston area, Washington DC area, Northern Virginia.
- Note: Videotron (`seo/home-2026-11-16`) and Microsoft 365 (`seo/home-2026-11-12-microsoft-365`) branches are still unmerged.

### Next steps
1. Merge pending Videotron and Microsoft 365 branches; then cross-link Canadian ISP pages, and add AT&T/Fios to the Xfinity and Spectrum pages' related links (updating their disclaimers).
2. Owner to confirm remote tools / payment / two-session wording and French support, then reconcile all pages (Xfinity and Mac pages still name Quick Assist/LogMeIn; Xfinity still says "all major credit and debit cards" and "up to two sessions").
3. US ISP page: Cox. Routers: D-Link, Linksys, Eero. Computers: ASUS, Acer, Microsoft Surface.
4. Housekeeping: bump stale home-support sitemap lastmod values (audit warnings).

## 2026-11-19
- Added ISP page `/home-support/wifi-router-help/cox/` ("Independent Help with Your Cox Wi-Fi, $100 CAD Flat"), the fifth US ISP page, which finishes the US ISP list. It has large call buttons with hours and a note for Arizona readers: most of Arizona stays on Mountain Standard Time, so in winter our hours there are 9 am – 9 pm and in summer they match Pacific Time. The never-call-first statement and the Cox disclaimer appear at top and bottom. Six problem cards: slow or dropping Wi-Fi, weak rooms, lost or new password, devices that won't connect, Panoramic Wifi pods, and your own router behind the gateway. An 8-step checklist covers a safe power restart, not pressing the reset hole, checking the coax cable is finger-tight, an outage check, testing next to the gateway, placement, and keeping the sticker private. Cox notes cover the gateway being modem plus router, the gateway usually sitting where the cable comes in (why pods or mesh are often easier than moving it), using your own router behind the gateway (some Cox app and pod features may switch off; your own modem must be Cox-supported), Cox TV being separate, and the fact that we never ask for the Cox account password. Also on the page: honest limits, a 7-question FAQ, the FTC link, the scam blog link, price with the CAD note, hours, the BC phone note, the family-member/seniors link, and Service + Offer + FAQPage + Breadcrumb JSON-LD.
- Deliberately left out: gateway model names, light colours, settings address, the approved-modem list and exact bridge-mode steps, because these vary and change.
- Linked from the US ISP card on the Wi-Fi & router hub and from the AT&T and Verizon Fios pages. Their disclaimers now name Cox. Added to `sitemap.xml`; bumped the lastmod for the hub, AT&T and Fios.
- Owner TODOs on the page: remote tool, payment methods, follow-up sessions.
- Target keywords (US): Cox Wi-Fi slow, Cox Wi-Fi password, restart Cox gateway, Cox Panoramic Wifi pods setup, Cox Wi-Fi weak upstairs, own router with Cox. Cities and areas: Phoenix, Tucson, Las Vegas, San Diego, Orange County, Oklahoma City, Hampton Roads VA, Rhode Island, New Orleans, Omaha.
- Note: the Videotron (`seo/home-2026-11-16`) and Microsoft 365 (`seo/home-2026-11-12-microsoft-365`) branches are still unmerged.

### Next steps
1. Merge the pending Videotron and Microsoft 365 branches. Then cross-link the Canadian ISP pages, and add AT&T, Fios and Cox to the related links on the Xfinity and Spectrum pages (updating their disclaimers).
2. The owner needs to confirm the remote tools, payment methods, two-session wording and French support; then reconcile all pages. The Xfinity and Mac pages still name Quick Assist/LogMeIn, and Xfinity still says "all major credit and debit cards" and "up to two sessions".
3. Routers: D-Link, Linksys, Eero. Computers: ASUS, Acer, Microsoft Surface. Later: Ring/Arlo/Nest and Samsung Galaxy/iPhone brand pages.
4. Housekeeping: bump stale home-support sitemap lastmod values (audit warnings).

## 2026-11-21
- Added router brand page `/home-support/wifi-router-help/linksys/` ("Independent Help with Your Linksys Router or Velop, $100 CAD Flat"). Same layout as the TP-Link page. It has large call buttons with hours, and the never-call-first statement and the Linksys disclaimer (which also names TP-Link, Netgear, Xfinity, Spectrum, Rogers and Bell, since the page links to them) at top and bottom. Six problem cards: Velop setup, a node with a red or yellow light, weak rooms, Linksys app sign-in, a new Wi-Fi name or password, and older routers. An 8-step checklist covers one device or all, finding the main node, the internet-port cable, restarting in order, lights (steady blue = fine, red = lost connection, yellow = too far, "on most models"), placement, a cable test and reset caution. The "specific to Linksys" notes cover Velop vs single routers, the app account vs Wi-Fi vs router password, using Linksys behind an ISP box (with links to the Xfinity, Spectrum, Rogers and Bell pages), and older models that no longer get updates (we tell you honestly; replacing is your choice). Also on the page: honest limits, a 7-question FAQ (including "someone called saying my Linksys was hacked"), CAFC and FTC links, the scam blog link, price with the CAD note, hours, the BC phone note, the family-member/seniors note, links to TP-Link and Netgear, and Service + Offer + FAQPage + Breadcrumb JSON-LD.
- Deliberately left out: model numbers, the settings-page address, light meanings beyond blue/red/yellow, and Linksys subscription features or pricing (these vary and change).
- Linked from the Linksys card on the Wi-Fi & router hub. Added to `sitemap.xml`; bumped the hub's lastmod.
- Merge note: the eero branch (`seo/home-2026-11-20`) is still unmerged. It edits the hub card on the line next to the Linksys card, and the same hub lastmod line, so expect a small conflict: keep both card links and the newer lastmod (2026-11-21).
- Owner TODOs on the page: remote tool, payment methods, follow-up sessions.
- Target keywords (CA + US): Linksys Velop setup help, Linksys Velop red light, Velop yellow light, Linksys app can't log in, Linksys Wi-Fi slow, Linksys router password, old Linksys router update, Linksys behind Xfinity/Rogers modem.

### Next steps
1. Merge the pending eero (11-20), Videotron (#90) and Microsoft 365 (#81) branches. The owner may want to close the older superseded home-support PRs.
2. Owner to confirm remote tools, payment methods, two-session wording and French support, then reconcile all pages.
3. Routers: D-Link, Google Nest Wifi, ASUS. Computers: ASUS, Acer, Microsoft Surface. Add AT&T/Fios/Cox to the Xfinity and Spectrum related links; cross-link TP-Link/Netgear pages to Linksys and eero.
4. Housekeeping: bump stale home-support sitemap lastmod values (audit warnings).

## 2026-11-23
- Added computer brand page `/home-support/computer-help/surface/` ("Independent Help with Your Microsoft Surface, $100 CAD Flat"). It uses the same layout as the Lenovo page: large call buttons with hours, plus the Microsoft disclaimer (which also names Dell, HP and Lenovo, since the page links to them) and the never-call-first statement at top and bottom. Six problem cards: Surface Pro keyboard stopped working, won't charge, battery stops at 80%, pen or touchscreen, slow Surface, and new Surface setup. A 7-step "keyboard not working" checklist covers reseating the magnetic keyboard, cleaning the contacts, restarting, the on-screen keyboard for sign-in, Windows Update (where Surface fixes come from), the forced restart (hold power about 20 seconds "on most models") and knowing when it's a hardware job. The Surface-specific notes cover the magnetic charger and its light, the Surface app and the serial number under the kickstand, updates coming through Windows Update (no "driver updater" programs), some newer Surfaces using Arm chips (older programs and printer drivers may not work, so we check before you move), and "Microsoft will not call you" (scam link). Also on the page: honest limits, an 8-question FAQ (including "someone called saying they are from Microsoft"), CAFC and FTC links, the scam blog link, price with the CAD note, hours, the BC phone note, the family-member/seniors note, and Service + Offer + FAQPage + Breadcrumb JSON-LD.
- Deliberately left out: model numbers, exact Surface app menu names and UEFI steps, the connector light's colours and meanings, and warranty or repair prices (these vary and change).
- Linked from the computer-help hub and from the Lenovo and HP pages (both disclaimers already name Microsoft). Added to `sitemap.xml`; bumped lastmod for the computer-help hub, Lenovo and HP.
- Branched from `main` and touches no router pages, so it shouldn't conflict with the pending eero (#98) and Google Nest Wifi (11-22) branches. Only `sitemap.xml` (a different area) and this log are shared.
- Owner TODOs on the page: remote tool, payment methods, follow-up sessions.
- Target keywords (CA + US): Surface Pro keyboard not working, Surface won't charge, Surface battery stops at 80, Surface Pen not working, Surface black screen won't turn on, Surface serial number, new Surface setup help, Microsoft calling about virus scam.

### Next steps
1. Merge the pending eero (#98), Google Nest Wifi (11-22), Videotron (#90) and Microsoft 365 (#81) branches.
2. Owner to confirm remote tools, payment methods, two-session wording and French support, then reconcile all pages.
3. Computers: ASUS, Acer (then add a Surface link on the Dell page's related links). Routers: D-Link, ASUS. Printers: Lexmark, Xerox.
4. Housekeeping: bump stale home-support sitemap lastmod values (audit warnings).
