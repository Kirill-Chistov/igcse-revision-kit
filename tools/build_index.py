#!/usr/bin/env python3
"""Generate the human-facing indexes from the repository itself.

    python3 tools/build_index.py          # rewrite notes/README.md, PAPERS.md, docs/catalog.json
    python3 tools/build_index.py --check  # exit 1 if any of them is out of date (CI runs this)

Run it after adding or rebuilding a PDF, adding a subject, or changing a subject.yaml.
docs/catalog.json is the machine-readable version (subjects -> topics -> subtopics -> PDFs), meant
for a future website. Standard library only; page counts need `pypdf` and are skipped without it.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools" / "tracker"))
import common as c  # noqa: E402

try:
    from pypdf import PdfReader
except ImportError:  # page counts are optional
    PdfReader = None

GITHUB_PDF_NOTE = "Click a PDF to read it on GitHub; use the download button (↓) at the top right to save it."


def front_matter(md: Path) -> dict:
    m = re.match(r"^---\n(.*?)\n---", md.read_text(encoding="utf-8"), re.S)
    if not m:
        return {}
    fm = {}
    lines = m.group(1).splitlines()
    for i, line in enumerate(lines):
        mm = re.match(r"^(\w+):\s*(.*)$", line)
        if not mm:
            continue
        key, val = mm.groups()
        if val in (">", "|", ">-", "|-"):  # folded block: take the indented lines that follow
            val = " ".join(x.strip() for x in lines[i + 1:] if x.startswith((" ", "\t")))
            nxt = [j for j in range(i + 1, len(lines)) if not lines[j].startswith((" ", "\t"))]
            if nxt:
                val = " ".join(x.strip() for x in lines[i + 1:nxt[0]])
        fm[key] = val.strip().strip("'\"")
    return fm


def nice(folder: str) -> str:
    nn, _, name = folder.partition("_")
    return f"{int(nn)} {name.replace('_', ' ')}" if nn.isdigit() else folder.replace("_", " ")


def pages(pdf: Path):
    if PdfReader is None:
        return None
    try:
        return len(PdfReader(str(pdf)).pages)
    except Exception:  # noqa: BLE001
        return None


def catalog() -> dict:
    subjects = []
    for folder in c.all_subjects():
        meta = c.subject_meta(folder)
        sdir = c.SUBJECTS / folder
        topics = []
        for t in sorted(p for p in (sdir / "topics").iterdir() if p.is_dir() and re.match(r"\d\d_", p.name)):
            subs = []
            sub_dirs = [t] if (t / "topic.md").exists() else sorted(p for p in t.iterdir() if p.is_dir() and re.match(r"\d\d_", p.name))
            for s in sub_dirs:
                md = s / "topic.md"
                fm = front_matter(md) if md.exists() else {}
                spec = re.match(r"Specification points? ([^—]+?)\s*—", fm.get("subtitle", ""))
                subs.append({"folder": s.name, "title": fm.get("title") or nice(s.name),
                             "spec_points": spec.group(1).strip() if spec else None,
                             "written": md.exists()})
            pdf = ROOT / "notes" / folder / f"{t.name}.pdf"
            topics.append({"folder": t.name, "title": nice(t.name),
                           "pdf": f"notes/{folder}/{t.name}.pdf" if pdf.exists() else None,
                           "pages": pages(pdf) if pdf.exists() else None, "subtopics": subs})
        extras = [{"title": p.stem.replace("_", " "), "pdf": str(p.relative_to(ROOT)), "pages": pages(p)}
                  for p in sorted((ROOT / "notes" / folder / "extras").glob("*.pdf"))]
        subjects.append({"id": folder, "name": meta["name"], "board": meta.get("board", ""),
                         "qualification": meta.get("qualification", ""), "code": meta["code"],
                         "spec_url": meta.get("spec_url", ""), "exam_page": meta.get("exam_page", ""),
                         "papers_note": meta.get("papers_note", ""), "topics": topics, "extras": extras})
    return {"version": 1, "subjects": subjects}


def notes_readme(cat: dict) -> str:
    ready = [s for s in cat["subjects"] if any(t["pdf"] for t in s["topics"])]
    later = [s for s in cat["subjects"] if s not in ready]
    out = ["# Revision notes (PDF)", "",
           "One PDF per topic, written from the official specification. " + GITHUB_PDF_NOTE,
           "To get a whole subject at once, download its zip from the [latest release](../../../releases/latest).",
           "", "**Jump to:** " + " · ".join(f"[{s['name']}](#{anchor(s)})" for s in ready), ""]
    for s in ready:
        out += [f"## {s['name']}", "",
                f"{s['board']} {s['qualification']} · **{s['code']}** · "
                f"[specification]({s['spec_url']}) · [past papers](../PAPERS.md#{anchor(s)})", "",
                "| Topic | What's in it | Pages |", "| --- | --- | --- |"]
        for t in s["topics"]:
            subs = [x for x in t["subtopics"] if x["written"]]
            what = " · ".join(x["title"] for x in subs) if len(subs) > 1 else (subs[0]["title"] if subs and subs[0]["title"] != t["title"] else "")
            link = f"[{t['title']}]({t['pdf'][len('notes/'):]})" if t["pdf"] else f"{t['title']} *(not written yet)*"
            out.append(f"| {link} | {what} | {t['pages'] or ''} |")
        for e in s["extras"]:
            out.append(f"| ⭐ [{e['title']}]({e['pdf'][len('notes/'):]}) | one-page poster | {e['pages'] or ''} |")
        out.append("")
    if later:
        out += ["## Coming later", "",
                "These subjects have their specification mapped but no notes yet — "
                "[help write them](../CONTRIBUTING.md):", ""]
        out += [f"- {s['name']} ({s['board']} {s['code']})" for s in later]
        out.append("")
    out.append("<!-- Generated by tools/build_index.py — do not edit by hand. -->")
    return "\n".join(out) + "\n"


def anchor(s: dict) -> str:
    return re.sub(r"[^a-z0-9 -]", "", s["name"].lower()).replace(" ", "-")


def papers_md(cat: dict) -> str:
    out = ["# Past papers", "",
           "Past papers are the best revision there is — but they belong to the exam boards, so this",
           "repository **links** to them instead of copying them. Pearson puts its papers and mark schemes",
           "online for free; Cambridge publishes recent ones and gives schools the full archive.", "",
           "**How to use them with the kit:** download the question paper (QP) *and* the mark scheme (MS),",
           "save both in `me/papers/<Subject>/` (any folder layout, keep \"QP\" / \"MS\" in the names), then",
           "ask your AI tutor `/test <subject> <topic>` — it picks the questions on that topic and marks",
           "you against the real mark scheme.", "",
           "| Subject | Code | Official papers | Notes |", "| --- | --- | --- | --- |"]
    for s in cat["subjects"]:
        board = "Pearson" if "Pearson" in s["board"] else "Cambridge"
        out.append(f"| <a id=\"{anchor(s)}\"></a>{s['name']} | {s['code']} | "
                   f"[{board} — {s['code']}]({s['exam_page']}) | {s['papers_note']} |")
    out += ["", "## Where exactly", "",
            "- **Pearson Edexcel:** open the link above → **Course materials** → filter by **Exam materials**.",
            "  Recent papers appear there after a short embargo; the newest series may be teacher-only for a while.",
            "- **Cambridge:** recent papers are on the syllabus page linked above (**Past papers** tab where it",
            "  exists). The full archive is in the School Support Hub — ask your teacher.",
            "- **Free collections by topic and year:** [Physics & Maths Tutor](https://www.physicsandmathstutor.com/past-papers/)",
            "  and [Save My Exams](https://www.savemyexams.com/) both host papers and mark schemes.",
            "", "Always check the **code** on the front of a paper matches yours — `4PH1` is not `0625`, and",
            "old-specification papers (e.g. `4PH0`, `4CH0`) cover slightly different content.", "",
            "<!-- Generated by tools/build_index.py — do not edit by hand. -->"]
    return "\n".join(out) + "\n"


def main(argv):
    cat = catalog()
    files = {
        ROOT / "notes" / "README.md": notes_readme(cat),
        ROOT / "PAPERS.md": papers_md(cat),
        ROOT / "docs" / "catalog.json": json.dumps(cat, ensure_ascii=False, indent=1) + "\n",
    }
    stale = [p for p, text in files.items() if not p.exists() or p.read_text(encoding="utf-8") != text]
    if "--check" in argv:
        for p in stale:
            print(f"out of date: {p.relative_to(ROOT)} — run python3 tools/build_index.py")
        return 1 if stale else 0
    for p, text in files.items():
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")
    n = sum(1 for s in cat["subjects"] for t in s["topics"] if t["pdf"])
    print(f"wrote notes/README.md, PAPERS.md, docs/catalog.json — {n} topic PDFs, {len(cat['subjects'])} subjects")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
