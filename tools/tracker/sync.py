#!/usr/bin/env python3
"""Convert tracker data between the local files and the artifact database layout.

    sync.py export   # me/*.json -> dist/db_export.json: [{"path": "progress/<Subject>", "data": {...}}, ...]
    sync.py import dist/db_import.json   # same shape -> me/*.json (replaces what is there)

The agent moves the documents with the artifact database tools (db_write / db_list). Use it when
switching tracker mode, or to keep a local backup of an artifact tracker.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import common as c  # noqa: E402


def export():
    docs = [{"path": f"progress/{s}", "data": {"points": pts}} for s, pts in c.load_progress()["points"].items()]
    docs += [{"path": "decks/" + k.replace("/", "__"), "data": d} for k, d in c.load_cards()["decks"].items()]
    out = Path(__file__).with_name("dist") / "db_export.json"
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(docs, ensure_ascii=False, indent=1))
    print(f"wrote {out}: {len(docs)} document(s)")


def import_(path):
    docs = json.loads(Path(path).read_text())
    prog, cards = {"version": 1, "points": {}}, {"version": 1, "decks": {}}
    for d in docs:
        coll, _, doc = d["path"].partition("/")
        if coll == "progress":
            prog["points"][doc] = d["data"].get("points", {})
        elif coll == "decks":
            cards["decks"][doc.replace("__", "/", 1)] = d["data"]
    c.save_json(c.PROGRESS, prog)
    c.save_json(c.FLASHCARDS, cards)
    print(f"imported {len(prog['points'])} subject(s), {len(cards['decks'])} deck(s)")


if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1] == "export":
        export()
    elif len(sys.argv) == 3 and sys.argv[1] == "import":
        import_(sys.argv[2])
    else:
        sys.exit(__doc__)
