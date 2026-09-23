# Clearpine Technologies — Website

Static site for **clearpinetech.ca**. No build step, no dependencies, no CMS.
Upload the files and it works.

---

## Files

```
index.html            Home
services.html         All eight services, each with an anchor (#cloud, #managed-it, ...)
capabilities.html     Capabilities statement for procurement / vendor onboarding
about.html            Company story, values, location
contact.html          Contact form (mailto-based) + procurement info
blog/index.html       Insights hub with planned topics
css/styles.css        All styling — one file, cached across pages
js/main.js            Mobile nav, footer year, contact form handler
sitemap.xml           Submit to Google Search Console
robots.txt            Points crawlers to the sitemap
favicon.svg           Browser tab icon
```

---

## Before you publish — 4 things to fix

1. **Create the email address `info@clearpinetech.ca`.**
   It appears throughout the site and the contact form sends to it.
   GoDaddy offers email with the domain, or use Google Workspace / Microsoft 365.

2. **Add a phone number** if you want one public. Currently email-only by design —
   fine for a new company, but a phone number raises conversion. Search for
   `info@clearpinetech.ca` and add a `tel:` link beside it.

3. **Create the OG image** at `img/og-clearpine.png` (1200×630px).
   This is what appears when the site is shared on LinkedIn or in messages.
   Until it exists, shares will show no image — not fatal, but worth doing.

4. **Decide on the street address.**
   The site currently says "Abbotsford, British Columbia" without the street.
   Adding the full address helps local SEO significantly but publishes your home
   address. If you get a commercial or virtual address later, add it to the
   `PostalAddress` schema in `index.html` and to the footer.

---

## Deploying

### Option A — GoDaddy hosting

1. Log into GoDaddy → your hosting plan → **File Manager** (or use FTP).
2. Upload everything into the `public_html` folder, keeping the folder structure.
3. Ensure `index.html` sits at the root of `public_html`.
4. Confirm SSL is enabled so the site serves over `https://`.

### Option B — Cloudflare Pages or Netlify (recommended — free and faster)

1. Create a free account.
2. Drag the whole folder into the deploy area.
3. Add `clearpinetech.ca` as a custom domain and follow the DNS instructions.
4. Point your GoDaddy DNS at their nameservers or add the CNAME they provide.

Either works. Cloudflare and Netlify give you a global CDN and automatic HTTPS,
which measurably helps Core Web Vitals — and therefore rankings.

### Domain strategy

You own both `.ca` and `.com`. Recommended setup:

- **`clearpinetech.ca` as the primary** — signals Canadian, which helps with
  both local search and government buyer perception.
- **`clearpinetech.com` 301-redirects to the `.ca`.** Never serve the same content
  on both domains; that splits your ranking signals.

---

## SEO — what is already done

- Unique `<title>` and meta description on every page, written for click-through
- Canonical URLs on every page
- Open Graph and Twitter Card tags
- **JSON-LD structured data:** Organization, ProfessionalService, WebSite, WebPage,
  BreadcrumbList, Service (all eight), Blog, AboutPage, ContactPage
- Semantic HTML with one `h1` per page and a correct heading hierarchy
- `sitemap.xml` and `robots.txt`
- **Fast by construction:** system fonts (no font downloads), one CSS file,
  ~1KB of deferred JavaScript, no frameworks, no render-blocking resources
- Accessible: skip links, ARIA labels, keyboard-navigable menu, visible focus states
- Mobile-first responsive layout
- `en-CA` language and BC geo meta tags for regional relevance

---

## SEO — what you need to do

Ranking is earned after launch, not at launch. In priority order:

### Week 1

1. **Google Search Console** — verify the domain, submit `sitemap.xml`
2. **Bing Webmaster Tools** — same (takes five minutes, non-trivial traffic in Canada)
3. **Google Business Profile** — this is the single highest-impact action for local
   search. Requires an address and verification. "IT services Abbotsford" is winnable
   with a complete profile.

### Month 1

4. **Get listed** in Canadian business directories — Yellow Pages, local chamber of
   commerce, BBB, industry associations. Citations with consistent name, address and
   phone build local authority.
5. **LinkedIn company page** linking to the site.
6. **Publish two articles** from the planned list in `blog/`. Real content is what
   makes a site rank for anything beyond your company name.

### Ongoing

7. **One article per month minimum.** Target questions your clients actually ask.
   Long, specific, genuinely useful posts outrank short keyword-stuffed ones.
8. **Build location pages** if you want to rank in specific cities — a page each for
   Abbotsford, Surrey, Langley, Vancouver, with genuinely different content.
   Duplicated location pages with the city name swapped get penalised.
9. **Earn links.** Client case studies, guest articles, association memberships,
   local sponsorships. This is slow and it is the thing that actually moves rankings.

---

## Adding a blog post

Copy `blog/index.html` as a template, then:

1. Save as `blog/your-post-slug.html`
2. Update `<title>`, meta description, and canonical URL
3. Replace the JSON-LD `Blog` block with a `BlogPosting` block including
   `headline`, `datePublished`, `author` and `image`
4. Add the post to the list in `blog/index.html`
5. Add the URL to `sitemap.xml`

Or ask me and I will write it.

---

## Honest notes

- **The contact form uses `mailto:`.** It opens the visitor's email client rather
  than submitting to a server. It works everywhere with zero setup, but some people
  abandon at that step. When you have traffic, switch to Formspree, Netlify Forms or
  Web3Forms — all free at low volume, all a five-minute change.

- **There are no client logos, testimonials or case studies**, because inventing them
  would be dishonest and easy to catch. Add them as you earn them; a single real
  case study outperforms a wall of stock badges.

- **Ranking takes months.** A new domain with no history competes against firms with
  years of accumulated authority. The site is built correctly — that removes technical
  obstacles, but content and links are what close the gap.
