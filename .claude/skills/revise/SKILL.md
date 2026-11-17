---
name: revise
description: Run one revision loop on a topic with the student — blurt, check against the notes, read the gaps, flashcards for the misses, questions, then record progress. Use on /revise <subject> <topic>, "help me revise Waves", "teach me 2.3", "quiz me on enzymes".
---

# Revise a topic

The subtopic loop from `rules/REVISION.md`, run as a tutor by `rules/TUTORING.md`. About 60
minutes; shorter if the student says so.

## 0. Read (quietly)

`CLAUDE.md`, `rules/TUTORING.md`, `rules/REVISION.md`, `me/profile.md`, `me/study_plan.md`,
`me/sessions.md` (newest entries for this subject), `me/weak_spots/<Subject>.md` (may not exist
yet). No `me/`? Offer `/setup` first.

## 1. Resolve

Subject → `subjects/<Subject>/`; topic → the subtopic folder(s) and their spec points from
`specification_map.csv`. Read each `topic.md` — it is the content and wording to check against.
If the topic has no notes yet, say so: offer `/make-topic` first, or run the loop from the
specification wording and the official PDF (less reliable — say that too).

If the purpose is unclear (learn new content / practise / mark something), ask once. **Learning
something new** skips the blurt: teach the points one at a time by TUTORING §2, each ending with a
small question, then continue from step 4.

## 2. Blurt (5 min)

Show the subtopic's specification point names as headings only. Ask the student to write
everything they remember under them — typed, or a photo of paper. Then wait.

## 3. Check the blurt

Compare against `topic.md` and the spec points. Reply with a short list: missing, wrong, vague
(name the `topic.md` section heading for each, as printed in the PDF). Praise nothing they didn't
earn. Tell them to read only those sections (10–15 min) and say "ready" when done.

## 4. Questions (15 min)

Sources in order: the re-test bank in the weak-spots log (1–2 earlier misses), past papers in
`me/papers/<Subject>/` on these points, `questions.md`, then questions you write in the board's
style (never labelled as past-paper questions). Solve and check each privately first (TUTORING §1).
One at a time; multi-part one part at a time; misses taught and re-tried; first attempt counts.

## 5. Record (always, without being asked)

Per `rules/REVISION.md` § What gets saved, using `tools/tracker/record.py` (or the artifact
database if `tracker: artifact`):
- a tracker round for every point tested, rated from first attempts;
- ≤ 5 flashcards for the misses worth most marks (check the deck first; respect the ceilings);
- the weak-spots log: dated one-line round entry, priority list, every missed question in the
  re-test bank, now-correct items moved to fixed;
- the session log: one entry at the top of `me/sessions.md` (what was covered, score, misses, what
  comes next).

## 6. Close (one short message)

Score; points by rating (small table if several); the 1–2 sections to re-read; how many cards were
added (first review tomorrow, in the tracker's Flashcards tab); anything untested. Nothing to
commit — `me/` is private.
