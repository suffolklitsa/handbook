#!/usr/bin/env python3
"""Check every handbook page: front matter (title, owner, last_reviewed) and relative links. Runs in CI.

Pages not reviewed in 365 days are listed as a warning, not a failure.
"""
from __future__ import annotations

import datetime as dt
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGES = ROOT / "pages"


def front_matter(text: str) -> dict[str, str]:
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}
    out = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            out[k.strip()] = v.strip().strip('"')
    return out


def check(path: Path, today: dt.date) -> tuple[list[str], list[str]]:
    text = path.read_text(encoding="utf-8")
    name = path.relative_to(ROOT)
    errors, warnings = [], []
    fm = front_matter(text)
    for key in ("title", "owner", "last_reviewed"):
        if not fm.get(key):
            errors.append(f"{name}: front matter needs {key}")
    try:
        if (today - dt.date.fromisoformat(fm.get("last_reviewed", ""))).days > 365:
            warnings.append(f"{name}: not reviewed in over a year")
    except ValueError:
        errors.append(f"{name}: last_reviewed must be YYYY-MM-DD")
    if not re.search(r"^# \S", text, re.M):
        errors.append(f"{name}: needs a '# ' heading")
    for target in re.findall(r"\]\((?!https?://|mailto:|#)([^)]+)\)", text):
        if not (path.parent / target.split("#")[0]).exists():
            errors.append(f"{name}: broken link {target}")
    return errors, warnings


def main() -> int:
    today = dt.date.today()
    errors, warnings = [], []
    pages = sorted(PAGES.rglob("*.md"))
    for p in pages:
        e, w = check(p, today)
        errors += e
        warnings += w
    for line in warnings:
        print(f"warning: {line}")
    for line in errors:
        print(line)
    print(f"{len(pages)} pages: {'ok' if not errors else f'{len(errors)} problems'}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
