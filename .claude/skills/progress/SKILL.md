---
name: progress
description: Show where the student stands and what to do today — tracker summary per subject, flashcards due, weak spots, next plan item — and start the tracker page. Use on /progress, "what should I do today", "how am I doing", "open my tracker".
---

# Progress

## 0. Read

`me/profile.md`, `me/study_plan.md`, `me/weak_spots/*.md` (priority lists only), and the tracker
data: `python3 tools/tracker/record.py summary` and `python3 tools/tracker/record.py due`
(artifact mode: read `progress/*` and `decks/*` with the database tools, per
`tools/tracker/README.md`). No `me/`? Offer `/setup`.

## 1. Answer in one short message

- **Today:** the plan's slot for today (and the test it prepares for, if any) + flashcards due
  (count, capped at 15 per run).
- **Per subject** (small table): points rated g / a / r / not rated, and the change since the last
  week if `d` dates allow it.
- **Top 3 weak spots** across subjects, from the weak-spots priority lists.
- One suggested next action as a command (`/revise Biology "2.5"`).

Keep it encouraging and factual; no lectures about how much is left.

## 2. Tracker page (if asked, or if they want to review cards)

- Local: tell them to run `python3 tools/tracker/serve.py` and open the address shown (start it
  yourself only if the agent runs on their computer and they ask).
- Artifact: give the `tracker_url` from `me/profile.md`.

Nothing to commit.
