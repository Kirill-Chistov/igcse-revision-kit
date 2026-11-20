# Revision — method, flashcards and what gets saved

Read by every command that revises, tests or plans (`/revise`, `/test`, `/plan`, `/progress`).
How to teach and mark is in `rules/TUTORING.md`; this file is what to do and what to record.

## Principles

- **Retrieval beats rereading.** Blurting, flashcards and questions, not highlighting.
- **Spaced, not crammed.** A point is revisited after 1, 3, 7, 21 and 60 days.
- **Small load, every day.** Ten minutes of flashcards daily beats a three-hour weekend. Keep the
  plan inside the time the student said they have (`me/profile.md`); never pile on extra sessions.
- **Rate by result, not by feeling.** After a marked session the tracker is updated from what the
  student actually got right.

## The subtopic loop (~60 min) — `/revise <subject> <topic>`

1. **Blurt** (5 min): show only the specification point names for the subtopic as headings; the
   student writes everything they remember (typed in chat, or a photo of paper).
2. **Check the blurt** against the subtopic's `topic.md` and the spec points: a short list of what
   is missing or wrong, so they read only those parts.
3. **Read the gaps** in the topic PDF (10–15 min).
4. **Cards** for the gaps only, within the flashcard limits below.
5. **Questions** (15 min): past-paper questions from `me/papers/<Subject>/` if present, else the
   subtopic's `questions.md`, else exam-style questions written for the session. Marked per
   `TUTORING.md`.
6. **Record** (always, without being asked): see "What gets saved".

## The self-test — `/test <subject> <topic>`

For a student who revised on their own. ~20–25 min of questions, one at a time, real past-paper
questions first. Misses are explained and re-tried; **the first attempt is what counts** for the
tracker. Then record as below.

## Ratings

| Code | Shown as | From a marked question |
| --- | --- | --- |
| `g` | Feel good | all marks |
| `a` | Need more revision | some marks |
| `r` | Don't know | no marks |

## Flashcard rules

Question → short answer in mark-scheme wording. Card types: definition, "why" (feature → reason),
list with a count ("3 adaptations of…"), numbers/equations/units, case-study facts. Never
"Explain X" cards.

- **Only for what the student got wrong or didn't know.** No cards for points they got right,
  nothing off-specification, nothing they can work out.
- **At most 5 new cards per session**, however many misses. Choose the misses worth most marks or
  most likely to come back; the rest stay in the weak-spots re-test bank. Adding 0 cards is fine.
- **At most one card per specification point.** Related facts go on one card. Answers ≤ 3 lines.
- **Look at the deck first.** Improve an existing card rather than add a near-duplicate.
- **Ceilings: 15 cards per topic deck, 40 per subject.** At a ceiling, a new card replaces one
  (delete a card in box 4–5, or merge two).
- **Never bulk-write a deck** unless the student asks for exactly that — and stay under the ceilings.
- Say in the closing message how many cards were added.
- Quotations from a copyrighted set text come from the student's own notes, not from the agent.

Reviews (in the tracker): a run is at most 15 cards, oldest due first. **Again** → box 0, due
today, re-asked at the end of the run. **Got it** → box +1, due in 1 / 3 / 7 / 21 / 60 days for
boxes 1–5. One run a day is the target; leftovers wait.

## What gets saved

Everything personal lives in `me/` (ignored by Git). Raw chat, blurt pages and photos of book pages
are **not** kept: they add nothing a later session can use, and book pages are copyrighted.

| What | Where | When |
| --- | --- | --- |
| Session log entry | `me/sessions.md` | at the end of **every** session, marked or not |
| Tracker round for the points covered | `me/progress.json` (or the artifact tracker) | after every marked session |
| Missed questions, priorities | `me/weak_spots/<Subject>.md` | after every marked session |
| New flashcards (≤ 5) | `me/flashcards.json` (or the artifact tracker) | after every marked session |
| Long written answers + marking | `me/work/<YYYY-MM-DD>_<Subject>_<task>.md` | English, 6+ mark answers |
| Schedule, test dates | `me/study_plan.md` | when it changes |
| Subjects, options, target grades, preferences | `me/profile.md` | `/setup`, or when the student says something changed |

### Session log — `me/sessions.md`

The tutor's memory between conversations. Every session that taught, quizzed, tested, marked or
planned anything ends with one entry added at the top (create the file from
`templates/me/sessions.md` if it is missing):

```
## 2026-11-17 · Biology_4BI1 · 2 Enzymes (2.10–2.13) · revise
- Did: blurt, then 8 questions (3 from June 2024 P1)
- Score: 14/20 · ratings: 2.10 g, 2.11 a, 2.12 a, 2.13 r
- Missed: effect of pH on the active site; units in the rate calculation
- Next: re-test 2.13, then start 2.14 Diffusion
```

At most 5 short lines; details belong in the weak-spots log, not here. A session with no marked
questions (a plan, an explanation) leaves out the Score line. The start of the next session reads
the newest entries for that subject and begins from their **Next** line unless the student asks
for something else. If the student stops without saying so, write the entry as soon as it is clear
the session is over — or first thing next time, from the conversation, marked "(written late)".

### `me/progress.json`

```json
{
  "version": 1,
  "points": {
    "Biology_4BI1": {
      "2.5B": { "h": [ { "r": "a", "d": "2026-11-15" }, null, { "r": "g", "d": "2026-11-22" } ], "note": "Test 1" }
    }
  }
}
```

- Keys: subject folder name → `spec_point` exactly as in `specification_map.csv`.
- `h[i]` is round R(i+1): `{ "r": "g" | "a" | "r", "d": "YYYY-MM-DD" }` or `null` (gaps allowed;
  trailing nulls trimmed). "Now" = the last non-null entry. To add a round, append.
- Unrated points have no entry.

### `me/flashcards.json`

```json
{
  "version": 1,
  "decks": {
    "Biology_4BI1/02": {
      "subject": "Biology_4BI1",
      "title": "2 Structure and functions in living organisms",
      "cards": [
        { "id": "k3f9", "q": "Name the enzyme that digests starch", "a": "amylase (to maltose)",
          "ref": "2.29", "b": 1, "due": "2026-11-16", "last": null, "c": "2026-11-15" }
      ]
    }
  }
}
```

- One deck per top-level topic, id `<Subject>/<NN>`. `b` = box 0–5; `due`, `last`, `c` (created)
  are `YYYY-MM-DD`; `a` may contain `\n`. New cards: `b: 1`, `due`: tomorrow, `id`: any short
  unique string.

### Editing safely

The tracker page may be open while an agent edits these files. Read the file, change only the
entries you mean to, write it back whole, and keep valid JSON (`python3 -m json.tool` checks it).
`python3 tools/tracker/record.py` does this for you:

```
python3 tools/tracker/record.py round Biology_4BI1 2.29 g --note "Test 1"
python3 tools/tracker/record.py card Biology_4BI1 2.29 "Name the enzyme that digests starch" "amylase (to maltose)"
python3 tools/tracker/record.py due        # cards due today, per subject
```

### Artifact tracker (claude.ai)

If `me/profile.md` has `tracker: artifact`, the same data lives in the artifact's database instead
of the two JSON files: one document per subject `progress/<Subject>` with body `{ "points": {…} }`
(the inner object of `progress.json`), and one per deck `decks/<Subject>__<NN>` with the deck object
as body. The artifact URL is `tracker_url` in `me/profile.md`. Read with the artifact database
tools (`db_get` / `db_list`), change, write back with `db_write`. `tools/tracker/README.md` has
the details and the sync commands.

## Planning — `/plan`

`me/study_plan.md` holds: exam and mock dates, the weekly shape (which evenings, how long), test
days, and a short backlog order. Built from `me/profile.md` (available time, energy, what they
find hard) and the tracker. Rules:

- Fit the time the student actually has. A week of flashcards only is acceptable.
- Order the backlog by: soonest test → most marks at stake → biggest gap between target grade and
  grade now (`me/profile.md`) → weakest (most `r`/`a`) → quick wins.
- Many "not rated yet" points are content not yet taught — ask before treating them as backlog.
- For a subject the student says is strong, a short mixed **diagnostic** (~20 min, marked, ratings
  set from the result) beats rating point by point.
