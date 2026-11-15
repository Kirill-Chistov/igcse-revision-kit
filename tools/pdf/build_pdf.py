#!/usr/bin/env python3
"""
Build the revision PDF for one top-level topic.

One PDF per top-level topic:              notes/<Subject>/NN_<Topic>.pdf
Its sources are every written subtopic under   subjects/<Subject>/topics/NN_<Topic>/
(or topic.md directly in that folder when the topic has no subtopics).

    python3 tools/pdf/build_pdf.py Physics_4PH1/01_Forces_and_motion
    python3 tools/pdf/build_pdf.py subjects/Physics_4PH1/topics/01_Forces_and_motion
    python3 tools/pdf/build_pdf.py subjects/Physics_4PH1/topics/01_Forces_and_motion/02_Movement_and_position
    python3 tools/pdf/build_pdf.py notes/Physics_4PH1/01_Forces_and_motion.pdf  [more targets...]
    python3 tools/pdf/build_pdf.py --all            # every topic that has written subtopics

Any of those forms builds the WHOLE topic (a subtopic path is resolved to its topic), so the
topic PDF is always complete and current.

All written subtopics are rendered together by render_booklet.py (headless Chromium) as ONE
continuous document — no forced page break between subtopics; bookmarks come from the headings.

Only topic.md is rendered. summary.md and questions.md are never put into the PDF.
Subtopic folders without a topic.md (unwritten skeletons) are skipped and listed.

Options:
  --keep-html     also write the intermediate HTML next to the PDF
"""

import argparse
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
NN = re.compile(r"^\d{2}_")


def resolve(target: Path):
    """Return (repo_root, subject, topic_name) for any accepted target form.

    Accepted:  <Subject>/NN_<Topic>   notes/<Subject>/NN_<Topic>.pdf
               subjects/<Subject>/topics/NN_<Topic>[/NN_<Subtopic>]
    """
    root = Path(__file__).resolve().parents[2]
    raw = Path(target)
    parts = list(raw.parts)
    if raw.is_absolute():
        try:
            parts = list(raw.resolve().relative_to(root).parts)
        except ValueError:
            sys.exit(f"not inside the repository: {raw}")
    if parts and parts[0] in ("subjects", "notes"):
        kind = parts.pop(0)
        if kind == "subjects":
            if "topics" not in parts or len(parts) <= parts.index("topics") + 1:
                sys.exit(f"give a topic folder under topics/: {target}")
            i = parts.index("topics")
            return root, parts[0], parts[i + 1]
    if len(parts) < 2:
        sys.exit(f"give <Subject>/NN_<Topic>: {target}")
    name = parts[1][:-4] if parts[1].endswith(".pdf") else parts[1]
    return root, parts[0], name


def subtopic_dirs(topic_src: Path):
    """Ordered list of source folders to render, plus unwritten skeletons."""
    if (topic_src / "topic.md").exists():
        return [topic_src], []
    subs = sorted(p for p in topic_src.iterdir() if p.is_dir() and NN.match(p.name))
    written = [p for p in subs if (p / "topic.md").exists()]
    missing = [p.name for p in subs if not (p / "topic.md").exists()]
    return written, missing


def build(target: Path, keep_html: bool = False):
    import render_booklet as r
    repo_root, subject, topic = resolve(target)
    topic_src = repo_root / "subjects" / subject / "topics" / topic
    if not topic_src.is_dir():
        sys.exit(f"no source folder: {topic_src}")
    parts, missing = subtopic_dirs(topic_src)
    if not parts:
        sys.exit(f"nothing written yet in {topic_src}")

    out_pdf = repo_root / "notes" / subject / f"{topic}.pdf"
    out_pdf.parent.mkdir(parents=True, exist_ok=True)
    topic_title = topic.split("_", 1)[1].replace("_", " ")
    code = subject.rsplit("_", 1)[-1]
    footer = f"{code} · {topic_title}"
    pages = r.render_topic(parts, out_pdf, topic_title, footer, keep_html)

    print(f"{pages:3d} pages  {out_pdf.relative_to(repo_root)}   <- {len(parts)} subtopic(s)")
    if missing:
        print(f"      not written yet (skipped): {', '.join(missing)}")
    return out_pdf, pages


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Build <Subject>/NN_<Topic>.pdf from its subtopic sources.")
    ap.add_argument("targets", nargs="*")
    ap.add_argument("--all", action="store_true", help="build every topic that has at least one written subtopic")
    ap.add_argument("--keep-html", action="store_true", help="also write the intermediate HTML next to the PDF")
    args = ap.parse_args()
    targets = [Path(t) for t in args.targets]
    if args.all:
        root = Path(__file__).resolve().parents[2]
        for tp in sorted((root / "subjects").glob("*/topics/[0-9][0-9]_*")):
            if any(tp.rglob("topic.md")):
                targets.append(Path("subjects") / tp.relative_to(root / "subjects"))
    if not targets:
        ap.error("give at least one target, or --all")
    for t in targets:
        build(t, args.keep_html)
