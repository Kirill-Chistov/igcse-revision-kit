---
name: add-subject
description: Add a qualification the kit does not have yet (any board, any code) — download the official specification, build specification.md, specification_map.csv, coverage_checklist.md, subject rules and empty topic folders. Use on /add-subject, "add AQA Chemistry 8462", "my subject isn't here".
---

# Add a subject

Turns an official specification into the scaffolding every other skill relies on. No notes are
written here — that is `/make-topic`, one topic at a time.

Read `CLAUDE.md`, `rules/DECISIONS.md` and `rules/SOURCE_POLICY.md`. Use an existing subject as the
model for every file (Physics_4PH1 for a science, Geography_0976 for a case-study subject,
Spanish_4SP1 for a language, Business_4BS1 for a points-based spec).

## 1. Identify the exact qualification

From the user's words get: board (AQA, Pearson Edexcel, OCR, WJEC/Eduqas, Cambridge, CCEA…),
qualification type (GCSE vs International GCSE vs IGCSE — different specifications!), subject, code
and the syllabus years. If the code is missing, search the board's own site and confirm with the
user ("AQA GCSE Chemistry 8462 — is that the one on your timetable?"). Never guess between
look-alikes (e.g. 4CH1 vs 4SC1, 0620 vs 0971, combined vs separate science).

Folder name: `<Subject_name>_<CODE>` (e.g. `Chemistry_8462`, `History_0977`). If it already exists,
stop and say so.

## 2. Get the specification

Download the current specification PDF **from the board's own domain** to
`subjects/<Folder>/Specification.pdf` (ignored by Git). If the network blocks it, ask the user to
download it and put it there. Read it fully — text extraction plus page images for tables.

## 3. Write the subject files

In `subjects/<Folder>/`, modelled on the closest existing subject:

| File | Content |
| --- | --- |
| `subject.yaml` | name, board, qualification, code, aliases, spec_url, tiers, centre_choices, status |
| `specification.md` | header table (official document path, downloaded-from URL, issue/version), qualification at a glance (papers, timings, weightings), AOs, course distinctions, then every content point by official number, grouped exactly as the spec groups them, with the planned content folder per group |
| `specification_map.csv` | `spec_point,section,topic,requirement,content_path,content_status,notes` — one row per assessable point, official numbering, requirement text close to the official wording, `content_status` = `spec_mapped;content_not_written`, notes for tier/paper-only points |
| `coverage_checklist.md` | the same points as `- [ ]` lines in official order |
| `AGENT.md` | scope authority, before-you-write steps, how to write, past papers in `me/papers/<Folder>/`, QA |
| `SUBJECT_RULES.md` | papers and tiers, what changes by tier/route, centre choices and where they are recorded (`me/profile.md`), look-alike qualifications to avoid |
| `QA_CHECKLIST.md` | copy the closest subject's, adapted |

Then create the skeleton: `topics/NN_<Topic>/NN_<Subtopic>/.gitkeep` for every `content_path`,
numbered in specification order. Names: ASCII, words joined by `_`, ≤ 60 characters.

Point ids must be unique within the subject and stable — the tracker keys ratings by them.

## 4. Check

- `python3 tools/check_repo.py --subject <Folder>` passes (map ↔ folders ↔ checklist agree).
- Every assessable point in the PDF is in the map (count them against the spec's own list).
- Nothing copied at length from the PDF beyond point wording.

## 5. Register and finish

- Add the subject to the student's `me/profile.md` `subjects:` list (and ask its centre choices if
  any).
- Commit the new `subjects/<Folder>/` (not the PDF — it is ignored): `Add <Board> <Subject> <CODE>:
  specification map and topic skeleton`.
- Tell the user it's ready for `/make-topic <Subject> "Topic 1"`, and that a pull request would let
  other students use it (`CONTRIBUTING.md`).
