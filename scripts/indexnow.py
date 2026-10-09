#!/usr/bin/env python3
"""Submit changed pages to IndexNow (Bing, Yandex, Seznam, Naver; via Bing also
DuckDuckGo, Yahoo and Copilot).

Takes the repo-relative paths of changed files, keeps the HTML pages, maps each
to its public URL and POSTs them in one request. Deleted pages are submitted
too, so search engines drop them sooner.

    python3 scripts/indexnow.py about.html blog/index.html
    git diff --name-only A B | python3 scripts/indexnow.py -     # paths on stdin
    python3 scripts/indexnow.py --dry-run index.html             # print, don't send

The key lives in a file named <key>.txt at the site root; that file is what
proves to IndexNow that the submissions come from the site owner.
"""

import argparse
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

HOST = "clearpinetech.ca"
SITE = f"https://{HOST}"
ENDPOINT = "https://api.indexnow.org/indexnow"
ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {".github", "scripts", "seo"}


def find_key() -> str:
    for f in ROOT.glob("*.txt"):
        text = f.read_text().strip()
        if f.stem == text and len(text) >= 8:
            return text
    sys.exit("No IndexNow key file (<key>.txt containing the key) at the site root.")


def url_for(rel: str):
    """Public URL GitHub Pages serves for an HTML file, or None for non-pages."""
    if not rel.endswith(".html") or SKIP_DIRS.intersection(Path(rel).parts):
        return None
    if rel == "index.html":
        return SITE + "/"
    if rel.endswith("/index.html"):
        return f"{SITE}/{rel[: -len('index.html')]}"
    return f"{SITE}/{rel[: -len('.html')]}"


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("paths", nargs="*", help="changed files, or - to read them from stdin")
    ap.add_argument("--dry-run", action="store_true", help="print the request instead of sending it")
    args = ap.parse_args()

    paths = args.paths
    if paths == ["-"]:
        paths = sys.stdin.read().split()
    urls = sorted({u for u in map(url_for, paths) if u})
    if not urls:
        print("No changed pages to submit.")
        return

    key = find_key()
    body = {"host": HOST, "key": key, "keyLocation": f"{SITE}/{key}.txt", "urlList": urls}
    print(f"Submitting {len(urls)} URL(s):", *urls, sep="\n  ")
    if args.dry_run:
        print(json.dumps(body, indent=2))
        return

    req = urllib.request.Request(
        ENDPOINT,
        data=json.dumps(body).encode(),
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            print(f"IndexNow accepted the submission (HTTP {resp.status}).")
    except urllib.error.HTTPError as e:
        # 403 = key file not reachable yet; 422 = URLs don't match host; 429 = too many requests
        sys.exit(f"IndexNow rejected the submission: HTTP {e.code} {e.reason}")


if __name__ == "__main__":
    main()
