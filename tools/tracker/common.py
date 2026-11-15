"""Shared helpers for the tracker tools (standard library only)."""
from __future__ import annotations

import csv
import json
import os
import re
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ME = ROOT / "me"
SUBJECTS = ROOT / "subjects"
TEMPLATE = Path(__file__).with_name("index.html")
PROGRESS = ME / "progress.json"
FLASHCARDS = ME / "flashcards.json"


def read_yaml_simple(text: str) -> dict:
    """Tiny YAML reader for flat `key: value` and `key: [a, b]` lines (no dependency on PyYAML)."""
    out = {}
    for line in text.splitlines():
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*?)\s*(#.*)?$", line)
        if not m:
            continue
        key, val = m.group(1), m.group(2)
        if val.startswith("[") and val.endswith("]"):
            out[key] = [v.strip().strip("'\"") for v in val[1:-1].split(",") if v.strip()]
        else:
            out[key] = val.strip("'\"")
    return out


def profile() -> dict:
    p = ME / "profile.md"
    if not p.exists():
        return {}
    text = p.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    return read_yaml_simple(m.group(1)) if m else {}


def subject_meta(folder: str) -> dict:
    y = SUBJECTS / folder / "subject.yaml"
    meta = read_yaml_simple(y.read_text(encoding="utf-8")) if y.exists() else {}
    meta.setdefault("name", folder.rsplit("_", 1)[0].replace("_", " "))
    meta.setdefault("code", folder.rsplit("_", 1)[-1])
    meta.setdefault("board", "")
    return meta


def all_subjects() -> list[str]:
    return sorted(p.parent.name for p in SUBJECTS.glob("*/specification_map.csv"))


def chosen_subjects() -> list[str]:
    chosen = [s for s in profile().get("subjects", []) or [] if (SUBJECTS / s).is_dir()]
    return chosen or all_subjects()


def spec_data(subjects: list[str] | None = None) -> dict:
    """The tracker's embedded specification: subjects -> ordered list of points."""
    out = []
    for folder in subjects or chosen_subjects():
        meta = subject_meta(folder)
        rows = list(csv.DictReader(open(SUBJECTS / folder / "specification_map.csv", encoding="utf-8")))
        items = [{"p": r["spec_point"], "sec": r.get("section", ""), "top": r.get("topic", ""),
                  "req": r.get("requirement", ""), "note": (r.get("notes") or "")[:40]} for r in rows]
        name = meta["name"]
        short = {"English (First Language)": "English Lang", "English Literature": "English Lit",
                 "Computer Science": "Comp Sci", "Mathematics A": "Maths"}.get(name, name)
        out.append({"id": folder, "name": name, "short": short, "code": meta["code"],
                    "board": meta["board"], "items": items})
    return {"version": 1, "subjects": out}


def render_page(mode: str, subjects: list[str] | None = None) -> str:
    html = TEMPLATE.read_text(encoding="utf-8")
    data = json.dumps(spec_data(subjects), ensure_ascii=False, separators=(",", ":"))
    data = data.replace("</", "<\\/")  # keep it inside the <script> tag
    return html.replace("__SPEC_DATA__", data).replace("__MODE__", mode)


def load_json(path: Path, empty: dict) -> dict:
    if not path.exists():
        return json.loads(json.dumps(empty))
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def save_json(path: Path, data: dict) -> None:
    """Atomic write, so a reader never sees half a file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=path.parent, prefix=path.name, suffix=".tmp")
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
        f.write("\n")
    os.replace(tmp, path)


def load_progress() -> dict:
    d = load_json(PROGRESS, {"version": 1, "points": {}})
    d.setdefault("points", {})
    return d


def load_cards() -> dict:
    d = load_json(FLASHCARDS, {"version": 1, "decks": {}})
    d.setdefault("decks", {})
    return d
