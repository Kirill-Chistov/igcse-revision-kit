---
name: test
description: Test the student on a topic they have just revised on their own — real past-paper questions where they have them, marked one at a time, misses explained and re-tried, then tracker ratings, a few flashcards and the weak-spots log. Use on /test <subject> <topic>, "test me on topic 2", "mock me on Waves".
---

# Test a topic

The student revised alone; this checks whether it stuck. `rules/TUTORING.md` governs how to set,
mark and explain; `rules/REVISION.md` what to record.

## Arguments

`subject`, `topic` (top-level or subtopic). Optional: `paper` — a timed paper set instead of one at
a time (TUTORING §3). Missing and unclear from the message → one short question; otherwise start.

## 0. Read (quietly, every time)

`AGENTS.md`, `rules/TUTORING.md`, `rules/REVISION.md`, `me/profile.md`, `me/sessions.md` (newest
entries for this subject), `me/weak_spots/<Subject>.md`. No `me/`? Offer `/setup`.

## 1. Scope

Resolve the subtopic folders and specification points (`specification_map.csv`). Read each
`topic.md` (the marking language) and `questions.md`. Note which points are not yet `g` in the
tracker and which are on the weak-spots priority list — favour them.

## 2. Find the questions

Stop when every point in scope is covered once:

1. **Re-test bank:** 1–2 earlier misses from this topic.
2. **The student's past papers** in `me/papers/<Subject>/` — any layout. Find PDFs by name
   (session, paper, "QP"/"MS"/"mark scheme"), extract text (`pdftotext -layout`, or a Python PDF
   library), pick the questions on these points, and mark with the matching mark scheme. Label each
   by session, paper and question number. A question that depends on a figure: reproduce it only if
   you can do so faithfully (table, described diagram, drawn graph); otherwise skip it. No mark
   scheme available → mark against `topic.md` and the command-word rules, and say so once.
3. **`questions.md`** of the subtopic.
4. **Exam-style questions you write**, in the board's command words and mark allocations, only for
   points still uncovered. Never call them past-paper questions.

No papers in `me/papers/<Subject>/`? Say so in one line at the start and mention where to download
them (`/setup` step 4) — then carry on.

**Size:** ~20–25 minutes: 6–10 short questions, or fewer longer ones. Respect the time the student
has (`me/profile.md`). For a large topic, list the points left untested at the end.

**Before setting anything:** write each full solution and the marks privately; compute numbers in
the shell; use official mark-scheme wording where it exists (TUTORING §1).

## 3. Run it

Short opening: subject, topic, number of questions, where they come from, "one at a time".
Each question: source label, full question, marks; one part at a time. Mark straight away (marks +
which marking points). Right → one line, move on. Wrong/partial → point to the exact missing
marking point, explain in 2–4 sentences in `topic.md` wording, end with a small question, let them
re-answer. "Don't know" → hint first, then teach. **First attempt counts.** No running commentary.

## 4. Rate and record (without being asked)

Ratings from first attempts (`rules/REVISION.md` § Ratings); untested points get nothing. Then:
- tracker rounds: `python3 tools/tracker/record.py round <Subject> <point> <g|a|r> --note "Test"`
  for each rated point (artifact mode: the database tools, per `tools/tracker/README.md`);
- ≤ 5 flashcards, misses only, deck checked first, ceilings respected;
- weak-spots log: round entry, priorities, every miss in the re-test bank in full;
- English and 6+ mark answers: the answer and marking to `me/work/`;
- session log: one entry at the top of `me/sessions.md`.

## 5. Close (one message)

Marks / total; points by rating; 1–2 sections of `notes/<Subject>/NN_<Topic>.pdf` to re-read (by
heading); cards added and that the first review is tomorrow; untested points. Nothing to commit.
