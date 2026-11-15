#!/usr/bin/env python3
"""Download official specifications into subjects/<Subject>/Specification.pdf (ignored by Git).

    python3 tools/fetch_specs.py                 # the subjects in me/profile.md (or all)
    python3 tools/fetch_specs.py Biology_4BI1 Geography_0976
    python3 tools/fetch_specs.py --force ...     # re-download

The URL comes from each subject.yaml (`spec_url`), always the exam board's own site. Boards move
files now and then: if a download fails, open the board's qualification page and save the PDF by hand.
"""
from __future__ import annotations

import sys
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "tracker"))
import common as c  # noqa: E402


def main(argv):
    force = "--force" in argv
    subjects = [a for a in argv if not a.startswith("--")] or c.chosen_subjects()
    bad = 0
    for s in subjects:
        meta = c.subject_meta(s)
        url, out = meta.get("spec_url", ""), c.SUBJECTS / s / "Specification.pdf"
        if out.exists() and not force:
            print(f"have   {s}")
            continue
        if not url.startswith("https://"):
            print(f"skip   {s}: no spec_url in subject.yaml")
            continue
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "igcse-revision-kit"})
            data = urllib.request.urlopen(req, timeout=60).read()
            if not data.startswith(b"%PDF"):
                raise ValueError("the board's site did not return a PDF")
            out.write_bytes(data)
            print(f"saved  {s}: {len(data) // 1024} KB")
        except Exception as e:  # noqa: BLE001
            bad += 1
            print(f"FAILED {s}: {e}\n       download it yourself from {url}\n       and save it as {out.relative_to(c.ROOT)}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
