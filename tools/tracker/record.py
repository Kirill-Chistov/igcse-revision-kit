#!/usr/bin/env python3
"""Record revision results in me/progress.json and me/flashcards.json — the commands agents use.

    record.py round   <Subject> <point> <g|a|r> [--note TEXT] [--date YYYY-MM-DD]
    record.py card    <Subject> <point> "<question>" "<answer>"      (respects the deck ceilings)
    record.py delcard <Subject> <card-id>
    record.py due                       # cards due today, per subject
    record.py summary [Subject]         # g / a / r / not rated per subject
    record.py show    <Subject> [point] # current ratings and notes
    record.py deck    <Subject> <NN>    # list a deck's cards

Points must exist in subjects/<Subject>/specification_map.csv. Standard library only. Artifact
mode (tracker: artifact in me/profile.md) keeps this data in the artifact database instead — see
tools/tracker/README.md.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import secrets
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import common as c  # noqa: E402

DECK_MAX, SUBJECT_MAX = 15, 40


def spec_rows(subject: str) -> list[dict]:
    f = c.SUBJECTS / subject / "specification_map.csv"
    if not f.exists():
        sys.exit(f"unknown subject folder: {subject} (choose from {', '.join(c.all_subjects())})")
    return list(csv.DictReader(open(f, encoding="utf-8")))


def topic_of(subject: str, point: str) -> tuple[str, str]:
    for r in spec_rows(subject):
        if r["spec_point"] == point:
            top = r["content_path"].split("/")[1] if "/" in r["content_path"] else "00_General"
            nn, _, name = top.partition("_")
            return nn, f"{int(nn) if nn.isdigit() else nn} {name.replace('_', ' ')}"
    sys.exit(f"{point} is not a specification point of {subject}")


def cmd_round(a):
    topic_of(a.subject, a.point)  # validates
    if a.rating not in ("g", "a", "r"):
        sys.exit("rating must be g, a or r")
    d = c.load_progress()
    e = d["points"].setdefault(a.subject, {}).setdefault(a.point, {"h": [], "note": ""})
    e.setdefault("h", []).append({"r": a.rating, "d": a.date or dt.date.today().isoformat()})
    if a.note:
        e["note"] = a.note
    c.save_json(c.PROGRESS, d)
    print(f"{a.subject} {a.point}: R{len(e['h'])} = {a.rating}")


def cmd_card(a):
    nn, title = topic_of(a.subject, a.point)
    d = c.load_cards()
    deck_id = f"{a.subject}/{nn}"
    deck = d["decks"].setdefault(deck_id, {"subject": a.subject, "title": title, "cards": []})
    in_subject = sum(len(x["cards"]) for k, x in d["decks"].items() if k.startswith(a.subject + "/"))
    if any(x.get("ref") == a.point for x in deck["cards"]) and not a.force:
        sys.exit(f"a card for {a.point} already exists in {deck_id} — improve it instead (or --force)")
    if (len(deck["cards"]) >= DECK_MAX or in_subject >= SUBJECT_MAX) and not a.force:
        sys.exit(f"ceiling reached ({len(deck['cards'])}/{DECK_MAX} in deck, {in_subject}/{SUBJECT_MAX} in subject): "
                 "replace a card (delcard one in box 4-5) instead of adding")
    tomorrow = (dt.date.today() + dt.timedelta(days=1)).isoformat()
    card = {"id": secrets.token_hex(3), "q": a.question, "a": a.answer.replace("\\n", "\n"), "ref": a.point,
            "b": 1, "due": tomorrow, "last": None, "c": dt.date.today().isoformat()}
    deck["cards"].append(card)
    c.save_json(c.FLASHCARDS, d)
    print(f"added card {card['id']} to {deck_id} ({len(deck['cards'])} cards)")


def cmd_delcard(a):
    d = c.load_cards()
    for k, deck in list(d["decks"].items()):
        if k.startswith(a.subject + "/"):
            before = len(deck["cards"])
            deck["cards"] = [x for x in deck["cards"] if x["id"] != a.card_id]
            if len(deck["cards"]) != before:
                if not deck["cards"]:
                    del d["decks"][k]
                c.save_json(c.FLASHCARDS, d)
                return print(f"deleted {a.card_id} from {k}")
    sys.exit("card not found")


def cmd_due(a):
    t = dt.date.today().isoformat()
    per = {}
    for k, deck in c.load_cards()["decks"].items():
        n = sum(1 for x in deck["cards"] if (x.get("due") or t) <= t)
        if n:
            per[deck.get("subject", k.split("/")[0])] = per.get(deck.get("subject", k.split("/")[0]), 0) + n
    total = sum(per.values())
    print(f"{total} card(s) due today" + (": " + ", ".join(f"{s} {n}" for s, n in sorted(per.items())) if per else ""))


def now(e):
    return next((x for x in reversed(e.get("h", [])) if x), None)


def cmd_summary(a):
    pts = c.load_progress()["points"]
    subs = [a.subject] if a.subject else c.chosen_subjects()
    print(f"{'subject':28} {'good':>5} {'more':>5} {'dont':>5} {'none':>5}")
    for s in subs:
        cnt = {"g": 0, "a": 0, "r": 0, "none": 0}
        for r in spec_rows(s):
            n = now(pts.get(s, {}).get(r["spec_point"], {}))
            cnt[n["r"] if n else "none"] += 1
        print(f"{s:28} {cnt['g']:5} {cnt['a']:5} {cnt['r']:5} {cnt['none']:5}")


def cmd_show(a):
    pts = c.load_progress()["points"].get(a.subject, {})
    for r in spec_rows(a.subject):
        p = r["spec_point"]
        if a.point and p != a.point:
            continue
        e = pts.get(p)
        if e or a.point:
            hist = " ".join(f"{x['r']}:{x['d']}" if x else "-" for x in (e or {}).get("h", []))
            print(f"{p:10} {hist:40} {(e or {}).get('note', '')}")


def cmd_deck(a):
    deck = c.load_cards()["decks"].get(f"{a.subject}/{a.nn}")
    if not deck:
        sys.exit("no such deck")
    for x in deck["cards"]:
        print(f"{x['id']}  box {x['b']}  due {x['due']}  [{x.get('ref', '')}] {x['q']}  ->  {x['a']!r}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    p = sp.add_parser("round"); p.add_argument("subject"); p.add_argument("point"); p.add_argument("rating")
    p.add_argument("--note"); p.add_argument("--date"); p.set_defaults(f=cmd_round)
    p = sp.add_parser("card"); p.add_argument("subject"); p.add_argument("point"); p.add_argument("question")
    p.add_argument("answer"); p.add_argument("--force", action="store_true"); p.set_defaults(f=cmd_card)
    p = sp.add_parser("delcard"); p.add_argument("subject"); p.add_argument("card_id"); p.set_defaults(f=cmd_delcard)
    p = sp.add_parser("due"); p.set_defaults(f=cmd_due)
    p = sp.add_parser("summary"); p.add_argument("subject", nargs="?"); p.set_defaults(f=cmd_summary)
    p = sp.add_parser("show"); p.add_argument("subject"); p.add_argument("point", nargs="?"); p.set_defaults(f=cmd_show)
    p = sp.add_parser("deck"); p.add_argument("subject"); p.add_argument("nn"); p.set_defaults(f=cmd_deck)
    a = ap.parse_args()
    if a.cmd in ("round", "card", "delcard") and not c.ME.exists():
        sys.exit("no me/ folder — run /setup first")
    a.f(a)


if __name__ == "__main__":
    main()
