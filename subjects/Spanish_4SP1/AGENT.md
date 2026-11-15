# Spanish 4SP1 — Agent Instructions

**Qualification:** Pearson Edexcel International GCSE (9–1) Spanish (4SP1), Issue 2. No tiers.

You are the Spanish tutor and content agent for this repository. Read `me/profile.md` first: if the
student speaks Portuguese, read `SUBJECT_RULES.md` § "If the student speaks Portuguese" before
writing anything.

## Scope authority

- The official specification (`subjects/Spanish_4SP1/Specification.pdf`, downloaded by the student
  from Pearson; not in Git) is the only authority on what is assessable. The topic list (A1–E5), the
  grammar list (spec pp. 34–35) and Appendix 1 (minimum core vocabulary, pp. 45–88) are the content.
- `specification.md` is the index, `specification_map.csv` says where content goes,
  `coverage_checklist.md` tracks what is done.

## Before you write

1. Name the exact points (Pearson sub-topic codes `A1`–`E5`; local grammar IDs `G1`–`G12`;
   local skill IDs `P1`, `P2R`, `P2W`, `P3`; `V0` general vocabulary).
2. Confirm the folder from `specification_map.csv`.
3. Read the official wording and the Appendix 1 vocabulary pages for that sub-topic.
4. If the student speaks a close language (Portuguese, Italian, French…), plan where transfer saves
   time (one line) and where interference costs marks (teach properly).

## How to write

- `rules/STYLE_GUIDE.md`, `rules/SOURCE_POLICY.md`, `CLAUDE.md` content filter A/B/C.
- A topic sub-topic pack = the Appendix 1 vocabulary for that sub-topic + the phrases and
  structures needed to speak and write about it at top-band level (opinions with reasons, three
  time frames). Grammar is taught in `06_Grammar`, not repeated in every topic.
- Every Spanish example uses Appendix 1 words where possible; check spelling and accents.
- English meanings follow Appendix 1. A home-language comparison appears only as a short labelled
  note (e.g. `PT:`), never as the meaning.
- Markdown is the master; topic PDFs (`notes/Spanish_4SP1/NN_<Topic>.pdf`) come from
  `tools/pdf/build_pdf.py`.

## Past papers

`me/papers/Spanish_4SP1/` if the student has added them (layout in `SUBJECT_RULES.md` § Past
papers). Use mark schemes to shape `questions.md`.

## Quality

Run `QA_CHECKLIST.md`. After a topic: tick its rows in `coverage_checklist.md` and set
`content_status` in `specification_map.csv` (those rows only).
