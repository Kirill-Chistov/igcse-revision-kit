#!/usr/bin/env python3
"""Build a standalone tracker page.

    python3 tools/tracker/build.py --artifact        # dist/tracker.html for a claude.ai artifact
    python3 tools/tracker/build.py --artifact --subjects Biology_4BI1 Physics_4PH1

The subjects default to those in me/profile.md (or every subject). The specification points are
embedded in the page; ratings and cards live in the artifact's database, not in the HTML.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import common as c  # noqa: E402


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--artifact", action="store_true", help="build for a claude.ai artifact (database storage)")
    ap.add_argument("--subjects", nargs="*", help="subject folder names (default: me/profile.md)")
    ap.add_argument("--out", default=str(Path(__file__).with_name("dist") / "tracker.html"))
    a = ap.parse_args()
    if not a.artifact:
        ap.error("only --artifact builds a standalone page; for the local tracker run serve.py")
    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(c.render_page("artifact", a.subjects or None), encoding="utf-8")
    print(f"wrote {out} ({out.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
