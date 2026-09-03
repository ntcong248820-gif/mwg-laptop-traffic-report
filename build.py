#!/usr/bin/env python3
"""Wrap src/report.html into a standalone index.html for GitHub Pages.

`src/report.html` is the single source: it is also the file published as a Claude
Artifact, which supplies its own <head>. GitHub Pages serves raw files, so this
script adds the document skeleton the Artifact host would otherwise inject, plus
the noindex directives this site needs.

Convention the split relies on: everything up to and including the LAST `</style>`
is head content; everything after it is body content. Keep authoring that way.

    python3 build.py
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).parent
SRC = ROOT / "src" / "report.html"
OUT = ROOT / "index.html"
MARK = "</style>"

HEAD_EXTRA = """<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow, noarchive, nosnippet, noimageindex">
<meta name="googlebot" content="noindex, nofollow">
<meta name="referrer" content="no-referrer">
<style>
  :root { color-scheme: light dark; }
  html { -webkit-text-size-adjust: 100%; }
  body { margin: 0; }
  img { max-width: 100%; height: auto; }
  [hidden] { display: none !important; }
</style>"""


def main() -> None:
    if not SRC.exists():
        sys.exit(f"Không thấy {SRC}")
    raw = SRC.read_text("utf-8")
    cut = raw.rfind(MARK)
    if cut == -1:
        sys.exit(
            f"Không thấy {MARK} trong {SRC}.\n"
            "Script tách head/body tại </style> cuối cùng — fragment phải có ít nhất một."
        )
    head = raw[: cut + len(MARK)].strip()
    body = raw[cut + len(MARK):].strip()
    if not body:
        sys.exit("Phần body rỗng — kiểm tra lại fragment.")

    OUT.write_text(
        "<!doctype html>\n"
        '<html lang="vi">\n<head>\n'
        f"{HEAD_EXTRA}\n{head}\n"
        "</head>\n<body>\n"
        f"{body}\n"
        "</body>\n</html>\n",
        encoding="utf-8",
    )
    kb = OUT.stat().st_size / 1024
    print(f"-> {OUT} ({kb:.1f} KB)")
    print(f"   head {len(head.splitlines())} dòng · body {len(body.splitlines())} dòng")


if __name__ == "__main__":
    main()
