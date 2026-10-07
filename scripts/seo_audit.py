#!/usr/bin/env python3
"""Minimal SEO audit: titles, descriptions, canonicals, h1, sitemap coverage."""
import re, sys, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
errors, warns = [], []
sm = (root / "sitemap.xml").read_text()
locs = set(re.findall(r"<loc>([^<]+)</loc>", sm))
for p in sorted(root.rglob("*.html")):
    rel = p.relative_to(root).as_posix()
    if rel.startswith("home-support/"):
        continue
    h = p.read_text()
    t = re.search(r"<title>(.*?)</title>", h, re.S)
    d = re.search(r'<meta name="description" content="([^"]*)"', h)
    c = re.search(r'<link rel="canonical" href="([^"]*)"', h)
    if not t: errors.append(f"{rel}: missing title")
    elif len(t.group(1)) > 65: warns.append(f"{rel}: title {len(t.group(1))} chars")
    if not d: errors.append(f"{rel}: missing meta description")
    elif len(d.group(1)) > 160: warns.append(f"{rel}: description {len(d.group(1))} chars")
    if not c: errors.append(f"{rel}: missing canonical")
    elif c.group(1) not in locs: errors.append(f"{rel}: canonical {c.group(1)} not in sitemap")
    if len(re.findall(r"<h1[ >]", h)) != 1: errors.append(f"{rel}: needs exactly one h1")
for w in warns: print("WARN ", w)
for e in errors: print("ERROR", e)
print(f"{len(errors)} errors, {len(warns)} warnings")
sys.exit(1 if errors else 0)
