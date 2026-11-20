#!/usr/bin/env python3
"""Consistency, privacy and licence checks — run before committing; CI runs it on every push.

    python3 tools/check_repo.py                    # everything
    python3 tools/check_repo.py --subject Physics_4PH1

Checks
  1. every subject has subject.yaml, specification.md, specification_map.csv, coverage_checklist.md
  2. the map is well formed: unique spec points, content_path folders exist under topics/
  3. coverage_checklist.md lists exactly the map's points
  4. every written subtopic has topic.md with YAML front matter; every image it uses exists
  5. every SVG that embeds a raster image (a photo) is listed in that folder's assets/SOURCES.md
  6. no forbidden files are tracked (me/, Specification.pdf, past papers, mark schemes, textbooks)
  7. no obvious personal data (emails, phone numbers) in shared files
  8. the slash-command pointer files match commands/ (tools/sync_commands.py --check)
Exit code 1 on errors; warnings do not fail.
"""
from __future__ import annotations

import csv
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SUBJ = ROOT / "subjects"
errors, warnings = [], []


def err(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


def check_subject(d: Path):
    for f in ("subject.yaml", "specification.md", "specification_map.csv", "coverage_checklist.md"):
        if not (d / f).exists():
            err(f"{d.name}: missing {f}")
    m = d / "specification_map.csv"
    if not m.exists():
        return
    rows = list(csv.DictReader(open(m, encoding="utf-8")))
    need = {"spec_point", "section", "topic", "requirement", "content_path", "content_status"}
    if rows and not need <= set(rows[0]):
        err(f"{d.name}: specification_map.csv lacks columns {sorted(need - set(rows[0]))}")
        return
    seen = set()
    for r in rows:
        p = r["spec_point"]
        if p in seen:
            err(f"{d.name}: duplicate spec_point {p}")
        seen.add(p)
        cp = r["content_path"]
        if not cp.startswith(d.name + "/"):
            err(f"{d.name}: {p} content_path should start with '{d.name}/': {cp}")
            continue
        if not (d / "topics" / cp[len(d.name) + 1:]).is_dir():
            err(f"{d.name}: {p} content_path folder missing: topics/{cp[len(d.name) + 1:]}")
    cl = d / "coverage_checklist.md"
    if cl.exists():
        listed = set(re.findall(r"^- \[[ x]\] \*\*([^*]+?)\*\*", cl.read_text(encoding="utf-8"), re.M))
        listed = {x.split()[0] for x in listed}
        missing = seen - listed
        if missing:
            warn(f"{d.name}: {len(missing)} map point(s) not in coverage_checklist.md (e.g. {sorted(missing)[:3]})")
    for t in (d / "topics").rglob("topic.md"):
        text = t.read_text(encoding="utf-8")
        rel = t.relative_to(ROOT)
        if not text.startswith("---\n"):
            err(f"{rel}: no YAML front matter")
        for img in re.findall(r"!\[[^\]]*\]\(([^)\s]+)", text):
            if not img.startswith("http") and not (t.parent / img).exists():
                err(f"{rel}: image not found: {img}")
    for svg in (d / "topics").rglob("*.svg"):
        head = svg.read_text(encoding="utf-8", errors="ignore")
        if "data:image/" in head:
            src = svg.parent / "SOURCES.md"
            if not src.exists() or svg.name not in src.read_text(encoding="utf-8"):
                err(f"{svg.relative_to(ROOT)}: embeds a photo but has no entry in {src.relative_to(ROOT)}")
            elif "to verify" in src.read_text(encoding="utf-8").lower():
                warn(f"{src.relative_to(ROOT)}: has image sources still marked 'to verify'")


FORBIDDEN = [
    (re.compile(r"^me/"), "personal folder"),
    (re.compile(r"(^|/)Specification\.pdf$"), "official specification (download locally instead)"),
    (re.compile(r"(?i)(past.?papers?|mark.?scheme|examiner.?report|question.?paper|_QP\.pdf|_MS\.pdf)"), "exam-board paper"),
    (re.compile(r"(?i)textbook.*\.pdf$|\.epub$"), "textbook"),
    (re.compile(r"(?i)\.(mp3|m4a|wav)$"), "audio (usually exam material)"),
]
PERSONAL = [
    (re.compile(r"[A-Za-z0-9._%+-]+@(?!users\.noreply\.github\.com)[A-Za-z0-9.-]+\.[a-z]{2,}"), "email address"),
    (re.compile(r"(?<!\d)(\+?\d{2,3}[ -]?)?\d{3}[ -]\d{3}[ -]\d{3,4}(?!\d)"), "phone number"),
]
TEXT_EXT = {".md", ".csv", ".yaml", ".yml", ".py", ".html", ".css", ".json", ".txt"}


def tracked_files():
    try:
        out = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True, text=True, check=True).stdout
        return [l for l in out.splitlines() if l]
    except Exception:  # noqa: BLE001 — not a git checkout
        skip = ("me/", "tools/tracker/dist/")
        files = [str(p.relative_to(ROOT)) for p in ROOT.rglob("*") if p.is_file() and ".git" not in p.parts]
        return [f for f in files if not f.startswith(skip) and not f.endswith("/Specification.pdf")]


def check_files():
    for f in tracked_files():
        for rx, what in FORBIDDEN:
            if rx.search(f):
                err(f"tracked file looks like a {what}: {f}")
        p = ROOT / f
        if p.suffix in TEXT_EXT and p.exists() and p.stat().st_size < 2_000_000 and not f.startswith("tools/check_repo"):
            text = p.read_text(encoding="utf-8", errors="ignore")
            for rx, what in PERSONAL:
                m = rx.search(text)
                if m:
                    warn(f"{f}: possible {what}: {m.group(0)!r}")


def main(argv):
    only = argv[argv.index("--subject") + 1] if "--subject" in argv else None
    for d in sorted(SUBJ.iterdir()):
        if d.is_dir() and (only is None or d.name == only):
            check_subject(d)
    if only is None:
        check_files()
        sync = subprocess.run([sys.executable, str(ROOT / "tools/sync_commands.py"), "--check"],
                              capture_output=True, text=True)
        if sync.returncode:
            err("command pointers out of date: run python3 tools/sync_commands.py\n" + sync.stdout.strip())
    for w in warnings:
        print("warning:", w)
    for e in errors:
        print("ERROR:  ", e)
    print(f"{len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
