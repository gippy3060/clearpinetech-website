#!/usr/bin/env python3
"""SEO audit for the Clearpine static site.

Checks every HTML page for the on-page basics (title, description, canonical,
h1, Open Graph, JSON-LD, image alt text), verifies internal links resolve,
flags duplicate titles/descriptions, and cross-checks sitemap.xml and
robots.txt against the files in the repo.

Standard library only, so it runs anywhere Python 3.9+ is available:

    python3 scripts/seo_audit.py              # human-readable report
    python3 scripts/seo_audit.py --markdown   # report as Markdown (CI summary)

Exits 1 if any ERROR is found; WARNINGs never fail the run.
"""

import argparse
import json
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from collections import defaultdict
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

SITE = "https://clearpinetech.ca"
ROOT = Path(__file__).resolve().parent.parent

TITLE_LEN = (20, 65)
DESC_LEN = (70, 160)
SKIP_DIRS = {".git", ".github", "scripts", "node_modules"}


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.lang = None
        self.title = ""
        self.meta = {}
        self.canonical = None
        self.h1_count = 0
        self.links = []
        self.imgs_missing_alt = []
        self.jsonld = []
        self._in_title = False
        self._in_jsonld = False
        self._buf = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "html":
            self.lang = a.get("lang")
        elif tag == "title":
            self._in_title = True
        elif tag == "meta":
            key = a.get("name") or a.get("property")
            if key:
                self.meta[key.lower()] = (a.get("content") or "").strip()
        elif tag == "link":
            if (a.get("rel") or "").lower() == "canonical":
                self.canonical = a.get("href")
            elif a.get("href"):
                self.links.append(a["href"])
        elif tag == "h1":
            self.h1_count += 1
        elif tag == "a" and a.get("href"):
            self.links.append(a["href"])
        elif tag in ("script", "img") and a.get("src"):
            self.links.append(a["src"])
        if tag == "img" and not a.get("alt") and a.get("alt") != "":
            self.imgs_missing_alt.append(a.get("src", "?"))
        if tag == "script" and (a.get("type") or "").lower() == "application/ld+json":
            self._in_jsonld = True
            self._buf = []

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        elif tag == "script" and self._in_jsonld:
            self._in_jsonld = False
            self.jsonld.append("".join(self._buf))

    def handle_data(self, data):
        if self._in_title:
            self.title += data
        if self._in_jsonld:
            self._buf.append(data)


def url_for(path: Path) -> str:
    """Public URL GitHub Pages serves for a file (extensionless, / for index)."""
    rel = path.relative_to(ROOT).as_posix()
    if rel == "index.html":
        return SITE + "/"
    if rel.endswith("/index.html"):
        return f"{SITE}/{rel[: -len('index.html')]}"
    return f"{SITE}/{rel[: -len('.html')]}"


def resolve_local(href: str):
    """Map an internal URL path to a file in the repo, or None if missing."""
    path = urlparse(href).path
    if not path or path == "/":
        return ROOT / "index.html"
    rel = path.lstrip("/")
    candidates = [ROOT / rel]
    if path.endswith("/"):
        candidates = [ROOT / rel / "index.html"]
    elif not Path(rel).suffix:
        candidates = [ROOT / f"{rel}.html", ROOT / rel / "index.html"]
    for c in candidates:
        if c.is_file():
            return c
    return None


def git_last_modified(path: Path):
    try:
        out = subprocess.run(
            ["git", "log", "-1", "--format=%cs", "--", str(path)],
            cwd=ROOT, capture_output=True, text=True, check=True,
        ).stdout.strip()
        return out or None
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None


class Report:
    def __init__(self):
        self.items = defaultdict(list)  # page -> [(level, msg)]

    def error(self, page, msg):
        self.items[page].append(("ERROR", msg))

    def warn(self, page, msg):
        self.items[page].append(("WARN", msg))

    def count(self, level):
        return sum(1 for v in self.items.values() for lv, _ in v if lv == level)


def audit_page(path: Path, report: Report, seen_titles, seen_descs):
    page = path.relative_to(ROOT).as_posix()
    p = PageParser()
    p.feed(path.read_text(encoding="utf-8"))

    robots = p.meta.get("robots", "")
    noindex = "noindex" in robots.lower()

    if not p.lang:
        report.error(page, "<html> is missing a lang attribute")

    title = " ".join(p.title.split())
    if not title:
        report.error(page, "missing <title>")
    else:
        seen_titles[title].append(page)
        if not TITLE_LEN[0] <= len(title) <= TITLE_LEN[1]:
            report.warn(page, f"title is {len(title)} chars (aim for {TITLE_LEN[0]}-{TITLE_LEN[1]})")

    desc = p.meta.get("description", "")
    if not desc:
        report.error(page, "missing meta description")
    else:
        seen_descs[desc].append(page)
        if not DESC_LEN[0] <= len(desc) <= DESC_LEN[1]:
            report.warn(page, f"meta description is {len(desc)} chars (aim for {DESC_LEN[0]}-{DESC_LEN[1]})")

    expected = url_for(path)
    if not p.canonical:
        report.error(page, "missing canonical link")
    elif p.canonical.rstrip("/") != expected.rstrip("/"):
        report.warn(page, f"canonical is {p.canonical}, expected {expected}")

    if p.h1_count != 1:
        report.error(page, f"has {p.h1_count} <h1> elements (should be exactly 1)")

    for key in ("og:title", "og:description", "og:url", "og:image"):
        if not p.meta.get(key):
            report.warn(page, f"missing {key}")
    og_img = p.meta.get("og:image", "")
    if og_img.startswith(SITE) and resolve_local(og_img) is None:
        report.error(page, f"og:image points to a file that doesn't exist: {og_img}")

    if not p.jsonld:
        report.warn(page, "no JSON-LD structured data")
    for i, block in enumerate(p.jsonld, 1):
        try:
            json.loads(block)
        except json.JSONDecodeError as e:
            report.error(page, f"JSON-LD block {i} is invalid JSON: {e}")

    for src in p.imgs_missing_alt:
        report.warn(page, f"<img> without alt text: {src}")

    for href in sorted(set(p.links)):
        parsed = urlparse(href)
        if parsed.scheme in ("mailto", "tel", "javascript", "data") or href.startswith("#"):
            continue
        if parsed.netloc and not href.startswith(SITE):
            continue  # external link
        if not parsed.netloc and not href.startswith("/"):
            target = (path.parent / parsed.path).resolve()
            href = "/" + target.relative_to(ROOT).as_posix() if target.is_relative_to(ROOT) else href
        if resolve_local(href) is None:
            report.error(page, f"broken internal link: {href}")

    return expected, noindex


def audit_sitemap(page_urls, report: Report):
    sm = ROOT / "sitemap.xml"
    if not sm.is_file():
        report.error("sitemap.xml", "sitemap.xml is missing")
        return
    try:
        tree = ET.parse(sm)
    except ET.ParseError as e:
        report.error("sitemap.xml", f"invalid XML: {e}")
        return

    ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    listed = {}
    for url in tree.getroot().findall("s:url", ns):
        loc = (url.findtext("s:loc", default="", namespaces=ns)).strip()
        lastmod = (url.findtext("s:lastmod", default="", namespaces=ns)).strip()
        if loc in listed:
            report.error("sitemap.xml", f"duplicate entry: {loc}")
        listed[loc] = lastmod
        f = resolve_local(loc)
        if f is None:
            report.error("sitemap.xml", f"lists a URL with no matching page: {loc}")
            continue
        changed = git_last_modified(f)
        if lastmod and changed and changed > lastmod:
            report.warn("sitemap.xml", f"lastmod {lastmod} is older than last change ({changed}) for {loc}")

    norm = {u.rstrip("/") for u in listed}
    for url, noindex in sorted(page_urls.items()):
        if noindex:
            if url.rstrip("/") in norm:
                report.error("sitemap.xml", f"lists a noindex page: {url}")
        elif url.rstrip("/") not in norm:
            report.error("sitemap.xml", f"page is missing from the sitemap: {url}")


def audit_robots(report: Report):
    robots = ROOT / "robots.txt"
    if not robots.is_file():
        report.error("robots.txt", "robots.txt is missing")
        return
    text = robots.read_text(encoding="utf-8")
    if f"Sitemap: {SITE}/sitemap.xml" not in text:
        report.warn("robots.txt", "doesn't reference the sitemap URL")
    if re.search(r"^\s*Disallow:\s*/\s*$", text, re.M):
        report.error("robots.txt", "blocks the whole site (Disallow: /)")


def render(report: Report, pages_checked: int, markdown: bool) -> str:
    errors, warns = report.count("ERROR"), report.count("WARN")
    lines = []
    if markdown:
        status = "❌ Failed" if errors else "✅ Passed"
        lines += [f"## SEO audit: {status}", "",
                  f"Checked **{pages_checked}** pages — **{errors}** errors, **{warns}** warnings.", ""]
        for page in sorted(report.items):
            lines.append(f"### `{page}`")
            for level, msg in report.items[page]:
                icon = "🔴" if level == "ERROR" else "🟡"
                lines.append(f"- {icon} {msg}")
            lines.append("")
    else:
        for page in sorted(report.items):
            lines.append(page)
            for level, msg in report.items[page]:
                lines.append(f"  {level:5} {msg}")
        lines.append(f"\nChecked {pages_checked} pages: {errors} errors, {warns} warnings.")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--markdown", action="store_true", help="output Markdown")
    args = ap.parse_args()

    report = Report()
    seen_titles, seen_descs = defaultdict(list), defaultdict(list)
    page_urls = {}

    pages = sorted(
        p for p in ROOT.rglob("*.html")
        if not SKIP_DIRS.intersection(p.relative_to(ROOT).parts)
    )
    for path in pages:
        url, noindex = audit_page(path, report, seen_titles, seen_descs)
        page_urls[url] = noindex

    for title, where in seen_titles.items():
        if len(where) > 1:
            for page in where:
                report.error(page, f"duplicate title shared with {', '.join(w for w in where if w != page)}")
    for desc, where in seen_descs.items():
        if len(where) > 1:
            for page in where:
                report.warn(page, f"duplicate meta description shared with {', '.join(w for w in where if w != page)}")

    audit_sitemap(page_urls, report)
    audit_robots(report)

    print(render(report, len(pages), args.markdown))
    sys.exit(1 if report.count("ERROR") else 0)


if __name__ == "__main__":
    main()
