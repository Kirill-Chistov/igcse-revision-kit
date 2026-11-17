---
name: setup
description: First-run setup for a student — a short interview that creates me/ (profile, subjects and options, schedule, preferences, tracker). Also re-runs to change subjects or preferences. Use on /setup, "set me up", "I'm new", or when me/ does not exist.
---

# Setup

Creates the student's personal layer, `me/`, so every other skill knows who it is helping. `me/` is
ignored by Git: nothing here is ever committed or published.

Read `CLAUDE.md` first. Templates are in `templates/me/`.

## 0. Already set up?

If `me/profile.md` exists, this is a **re-run**: show a 5-line summary of the profile and ask what
to change (subjects, options, schedule, preferences, tracker). Change only that, then go to step 6.

## 1. Welcome (one short message)

Say what the kit does in three lines (notes for each topic, a tutor that tests and marks, a tracker
with flashcards), that setup takes about 5 minutes, and that answers stay on their computer in
`me/`. Then start the questions. Ask **one or two questions at a time**, with tappable options
where the agent supports them. Accept "skip" for anything optional.

## 2. The questions

**a. Basics**
- First name or nickname (optional — only used to talk to them).
- Year group and exam session (e.g. "Year 11, exams May–June 2027"). Mock dates if known.
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

**d. Time and energy**
- Which days and roughly how long they can revise (be realistic — after school most students have
  45–90 minutes, not 3 hours).
- Regular tests at school (e.g. "cycle tests on Tuesdays and Fridays").
- Which subjects feel strong, OK, weak — and what kind of thing slips (definitions, details,
  calculations, essays, case studies).

**e. How they like to be taught** (offer the defaults from `rules/TUTORING.md` and let them adjust):
short replies one step at a time / longer explanations; hints before answers; photos of paper
working vs typing; anything that annoys them.

**f. Tracker** — explain the two modes in two lines and ask:
- **Local** (default): a page on their computer (`python3 tools/tracker/serve.py`), works offline,
  any AI agent can update it.
- **claude.ai artifact**: the same page hosted in their Claude account; nicer on a phone; only
  Claude can update it. Needs the claude.ai artifact tools in this session.

## 3. Write `me/`

Create from `templates/me/`:

- `me/profile.md` — YAML front matter (`subjects:` list of subject folder names, `tracker: local |
  artifact`, `tracker_url:`, `exam_session:`, `home_languages:`) and the readable sections filled
  from the answers. Keep it short; no information they didn't give.
- `me/study_plan.md` — leave as the template for now (step 5 offers `/plan`).
- `me/progress.json` → `{"version": 1, "points": {}}`; `me/flashcards.json` →
  `{"version": 1, "decks": {}}`.
- Empty folders `me/weak_spots/`, `me/work/`, `me/papers/<Subject>/`, `me/sources/<Subject>/` for
  each chosen subject.

Check `git check-ignore me/profile.md` reports it ignored. If not, stop and fix `.gitignore` before
writing anything personal.

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

One short message: what was set up (subjects with their options, tracker mode), what's missing
(`unknown — ask teacher` items, subjects the kit doesn't have → `/add-subject`), and the next step:
`/plan` to build a weekly plan, or `/revise <subject> <topic>` to start straight away.

Nothing to commit — `me/` is private.
