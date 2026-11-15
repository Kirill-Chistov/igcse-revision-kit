---
name: plan
description: Build or update the student's revision plan (me/study_plan.md) from their exam dates, available time, school tests and tracker data. Use on /plan, "make me a revision timetable", "what's my plan for this week", "mocks are in January".
---

# Plan

Writes `me/study_plan.md` — a plan the student can actually keep. Rules in `rules/REVISION.md`
§ Planning.

## 0. Read

`CLAUDE.md`, `rules/REVISION.md`, `me/profile.md`, `me/study_plan.md` (may be the empty template),
the tracker data (`python3 tools/tracker/record.py summary`, or the artifact database), and the
weak-spots logs' priority lists.

## 1. Fill gaps (ask only what is missing)

Exam and mock dates; school test days; which evenings and how long; anything coming up (trips,
holidays). One or two questions at a time. Record answers in `me/profile.md` if they are lasting.

## 2. Build

- **Weekly shape:** a table of days → slot (test prep, one backlog loop, rest). Fit inside the time
  they gave; leave at least one evening free. Daily: one flashcard run (≤ 15 cards, ~10 min).
- **Test prep first:** the two evenings before a school test go to that test's topics.
- **Backlog:** ordered by soonest exam → marks at stake → weakest (most `r`/`a`, weak-spots
  priorities) → quick wins. Each backlog slot names one `/revise` or `/test` (subject + topic).
- **Strong subjects:** a ~20-minute diagnostic instead of point-by-point revision.
- **Holidays:** past papers under timed conditions (`/test <subject> <topic> paper`).
- Topics not yet taught at school are not backlog — ask if unsure.

## 3. Write and show

Write `me/study_plan.md` from `templates/me/study_plan.md`. Show the student the weekly table and the
next 5 backlog items in the chat; ask if it feels doable. Adjust once if they say no.

Nothing to commit.
