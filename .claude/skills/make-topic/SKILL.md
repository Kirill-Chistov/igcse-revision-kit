---
name: make-topic
description: Create, update, compress, audit or fully rebuild one topic's revision notes (topic.md, summary.md, questions.md, diagrams) from the exact specification, then rebuild its PDF. Use on /make-topic <subject> <topic>, "make notes for Physics topic 3", "these notes are too long", "rebuild Biology section 2".
---

# Make a topic

Builds or improves one topic's notes from the repository's exact specification — never generic
GCSE material. `CLAUDE.md` wins over this skill if they disagree; `rules/WORKFLOW.md` is the step
list this skill follows.

## Arguments

- `subject` — name, alias or code (`Physics`, `bio`, `4CH1`, `CS`…) → `subjects/*/subject.yaml`
- `topic` — top-level topic or subtopic (`Topic 1`, `Waves`, `3.4`, `Tectonic hazards`)
- optional mode: `audit` (report only), `compress`, `rebuild` (delete and rewrite from scratch)

Infer missing arguments from the conversation when unambiguous; otherwise ask one short question.

## 0. Read (every time — the files change)

`CLAUDE.md`, `rules/WORKFLOW.md`, `rules/CONTENT_RULES.md`, `rules/STYLE_GUIDE.md`,
`rules/SOURCE_POLICY.md`, `me/profile.md` (tier, route, set texts, case studies, language for this
subject), then the subject files listed in WORKFLOW step 2.

## 1. Resolve and scope

Resolve the folder(s) under `subjects/<Subject>/topics/`. List every specification point and
sub-bullet in scope from `specification_map.csv` and the official PDF wording. The user's request
selects a target; the specification decides the content — do not ask what to include.

Check dependencies (WORKFLOW step 3). Anything centre-chosen and not in `me/profile.md` or
`me/sources/<Subject>/`: use the subject's placeholder policy and tell the student exactly what
source would fill it. Never fill it from model knowledge or the web.

## 2. Create, edit or rebuild

- **No pack yet** → create from `templates/`.
- **Pack exists** (default) → keep what is accurate and visually strong; edit, correct, complete,
  compress. Do not regenerate just because the skill was invoked.
- **`rebuild`** → only when asked, or when the pack has factual/structural problems harder to repair
  than rewrite. Delete the subtopic's `topic.md`, `summary.md`, `questions.md` and unused assets,
  then write from scratch.
- **`audit`** → write nothing; report coverage gaps, enrichment to cut, missing visuals, render
  problems, with file and section.

## 3. Write

Follow WORKFLOW steps 4–5: plan visuals first, then the pack. Subject-required elements from the
subject's `CONTENT_STYLE.md`. Diagrams as SVG in `assets/` (fonts `Carlito, Calibri, sans-serif`,
`viewBox` on the root); a photo only if openly licensed, recorded in `assets/SOURCES.md`.

## 4. Lean pass (mandatory, separate)

Re-read every file as the student. For every block ask the question in `CLAUDE.md` § Mandatory
final lean pass; cut or compress. Look for: repeated explanations, a second example where one is
enough, background, forward-teaching, overlong pros/cons lists, generic exam advice, the same idea
as prose + table + diagram, any back matter, an oversized summary.

## 5. Build and inspect

`python3 tools/pdf/build_pdf.py <Subject>/NN_<Topic>` (needs Chromium — `tools/pdf/README.md`).
Look at every affected page (render pages to images if you cannot view the PDF directly) and fix
clipping, broken SVGs, unreadable labels, bad page breaks, blank pages. If this environment cannot
render, say so and tell the student the one command to run, or that CI builds it on push.

## 6. Audit, trackers, checks

- Every point and sub-bullet in scope covered at command-word depth; subject `QA_CHECKLIST.md` run.
- Tick `coverage_checklist.md`, set `content_status` in `specification_map.csv` — those rows only.
- `python3 tools/check_repo.py --subject <Subject>` passes.
- No personal data anywhere outside `me/` (`CLAUDE.md` § Privacy).

## 7. Commit and report

Commit only this session's paths (`CLAUDE.md` § Git), e.g. `Physics 4PH1 topic 3: compress Waves`.
Report briefly: subject/spec, folders, PDF path and page count, points covered, files changed, the
commit, unresolved dependencies. If the topic was new for the kit, mention that a pull request would
share it with other students. Then stop — no next topic.
