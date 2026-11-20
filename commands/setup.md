---
name: setup
description: First-run setup of the tutor for a student — a short interview (subjects and options, exam and mock dates, target grades, time available, how they like to be taught) that creates the private me/ folder every later session reads and records into. Also re-runs to change anything. Use on /setup, "set me up", "I'm new", or when me/ does not exist.
---

# Setup

Turns the downloaded folder into this student's own tutor. It creates their personal layer, `me/`,
so every later session knows who it is helping, what they are aiming for, and what happened last
time. `me/` is ignored by Git: nothing here is ever committed or published.

Read `AGENTS.md` first. Templates are in `templates/me/`.

## 0. Already set up?

If `me/profile.md` exists, this is a **re-run**: show a 5-line summary of the profile and ask what
to change (subjects, options, dates, target grades, schedule, preferences, tracker). Change only
that, then go to step 6.

## 1. Welcome (one short message)

Say what the kit does in three lines (a tutor that teaches, tests and marks against their exact
specification; it remembers every session and what they got wrong; a tracker with flashcards),
that setup takes about 5 minutes, and that answers stay on their computer in `me/`. Then start the
questions. Ask **one or two questions at a time**, with tappable options where the agent supports
them. Accept "skip" or "don't know" for anything optional.

## 2. The questions

**a. Basics**
- First name or nickname (optional — only used to talk to them).
- Year group.
- Home language(s), if not English (affects language subjects and explanations).

**b. Subjects.** List what the kit has (`subjects/*/subject.yaml`: name, board, code, status) and
ask which they take. Students often don't know the code: match by subject + board, and check the
board if they are unsure ("Is your Biology exam board Pearson Edexcel or Cambridge? It's on your
exam timetable or past papers."). For each subject they take that the kit does **not** have, note
it — offer `/add-subject` at the end.

**c. Options per subject** — only those in each `subject.yaml` `centre_choices` and `tiers`:
tier (Foundation/Higher), route or components, set texts, the programming language used in class,
Geography case studies ("Do you know which examples your class uses? If not, we'll fill these in as
you meet them."). "Don't know yet" is a fine answer: record it as `unknown — ask teacher`.

**d. Exams**
- Exam session (e.g. "May–June 2027") and mock dates, if they have them.
- Exact paper dates if they have a timetable (they can paste or photograph it); otherwise leave
  them blank — `/plan` asks again closer to the time.

**e. Target grades** — for each subject, in one table-style question:
- the grade they are aiming for (use the subject's scale — 9–1 for the qualifications in the kit);
- the grade they are on now, if they know it (last report, mock or predicted grade).
Do not comment on whether a target is realistic. The gap between the two is used to order the
plan, nothing else.

**f. Time and energy**
- Which days and roughly how long they can revise (be realistic — after school most students have
  45–90 minutes, not 3 hours).
- Regular tests at school (e.g. "cycle tests on Tuesdays and Fridays").
- Per subject, what kind of thing slips (definitions, details, calculations, essays, case studies).

**g. How they like to be taught** (offer the defaults from `rules/TUTORING.md` and let them adjust):
short replies one step at a time / longer explanations; hints before answers; photos of paper
working vs typing; anything that annoys them.

**h. Tracker** — the default is **local**: a page on their computer
(`python3 tools/tracker/serve.py`), works offline, any AI can update its files. Ask only if you are
Claude with the claude.ai artifact tools: offer the **claude.ai artifact** instead (the same page
hosted in their Claude account; nicer on a phone; only Claude can update it). Otherwise skip the
question and use local.

## 3. Write `me/`

Can't write files (a chat app — `AGENTS.md` § Any AI)? Produce the same files as text instead: one
code block per file with its path as the heading, and tell the student to create a `me/` folder in
the kit and save them there (empty folders can wait). Skip the Git check and steps 4–5's commands;
just give the links.

Create from `templates/me/`:

- `me/profile.md` — YAML front matter (`subjects:` list of subject folder names, `tracker: local |
  artifact`, `tracker_url:`, `exam_session:`, `mocks:`, `home_languages:`) and the readable
  sections filled from the answers, including the target and current grade per subject. Keep it
  short; no information they didn't give.
- `me/study_plan.md` — from the template, with the Dates table filled from (d). The weekly shape
  and backlog are left for `/plan` (step 6 offers it).
- `me/sessions.md` — from the template, with one first entry: today's date, "Setup", the subjects
  chosen.
- `me/progress.json` → `{"version": 1, "points": {}}`; `me/flashcards.json` →
  `{"version": 1, "decks": {}}`.
- Empty folders `me/weak_spots/`, `me/work/`, `me/papers/<Subject>/`, `me/sources/<Subject>/` for
  each chosen subject.

Check `git check-ignore me/profile.md` reports it ignored (skip the check if the folder was
downloaded as a ZIP and is not a Git repository). If it is a repository and `me/` is not ignored,
stop and fix `.gitignore` before writing anything personal.

## 4. Specifications and papers

- Run `python3 tools/fetch_specs.py <Subject> …` for their subjects (downloads each official
  specification into `subjects/<Subject>/Specification.pdf`, ignored by Git). If the network
  blocks it, give them the URLs from `subject.yaml` to download themselves.
- Point them to `PAPERS.md` for where each subject's past papers are (links per subject). Papers go
  in `me/papers/<Subject>/` in any layout; `/test` finds them by name.
- School material (class case-study documents, textbook pages they photograph) goes in
  `me/sources/<Subject>/`.

## 5. Tracker

- **Local:** run `python3 tools/tracker/serve.py --check` to confirm it starts, then tell them:
  `python3 tools/tracker/serve.py` and open the address it prints.
- **Artifact:** follow `tools/tracker/README.md` § Artifact mode: build with
  `python3 tools/tracker/build.py --artifact`, publish `tools/tracker/dist/tracker.html` as a new
  artifact titled "Revision tracker", declare the `db` capability, import any existing data with
  `python3 tools/tracker/sync.py export` + `db_write`, and save the URL as `tracker_url` in
  `me/profile.md`. If the artifact tools are not available here, fall back to local and say so.

## 6. Finish

One short message: what was set up (subjects with their options and targets, dates, tracker mode),
what's missing (`unknown — ask teacher` items, subjects the kit doesn't have → `/add-subject`), and
that from now on every session is recorded in `me/` so the tutor picks up where they left off.
Then the next step: `/plan` to build a weekly plan, or `/revise <subject> <topic>` to start
straight away.

Nothing to commit — `me/` is private.
