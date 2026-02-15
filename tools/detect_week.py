#!/usr/bin/env python3
"""Detect which week to grade.

Priority:
1) If the push changed exactly one `submissions/wXX/...` folder => grade that week.
2) Otherwise => grade `ACTIVE_WEEK.txt` (instructor-controlled).
"""

from __future__ import annotations

import os
import re
import subprocess
from pathlib import Path

WEEK_RE = re.compile(r"^submissions/(w\d{2})/")

def get_changed_files() -> list[str]:
    try:
        out = subprocess.check_output(["git", "diff", "--name-only", "HEAD^", "HEAD"], text=True)
        return [l.strip() for l in out.splitlines() if l.strip()]
    except Exception:
        out = subprocess.check_output(["git", "ls-files"], text=True)
        return [l.strip() for l in out.splitlines() if l.strip()]

def read_active_week() -> str:
    p = Path("ACTIVE_WEEK.txt")
    if not p.exists():
        raise SystemExit("Missing ACTIVE_WEEK.txt")
    w = p.read_text(encoding="utf-8").strip()
    if not re.fullmatch(r"w\d{2}", w):
        raise SystemExit(f"ACTIVE_WEEK.txt must contain like 'w01', got: {w!r}")
    return w

def main() -> None:
    changed = get_changed_files()
    touched = sorted({m.group(1) for f in changed if (m := WEEK_RE.match(f))})

    if len(touched) == 1:
        week = touched[0]
    elif len(touched) > 1:
        raise SystemExit(
            f"Your push changed multiple weeks: {touched}. "
            "Please submit changes for only ONE week at a time."
        )
    else:
        week = read_active_week()

    out = os.environ["GITHUB_OUTPUT"]
    with open(out, "a", encoding="utf-8") as f:
        f.write(f"week={week}\n")
        f.write("max_score=100\n")

if __name__ == "__main__":
    main()
