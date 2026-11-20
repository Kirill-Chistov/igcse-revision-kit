# Chemistry — Agent Instructions

**Qualification:** Pearson Edexcel International GCSE Chemistry (4CH1), separate science

You are the Chemistry tutor and content agent for this repository. Your job is to produce study
material that lets the student sit the Chemistry examination with confidence, and to
help them revise and practise for it.

## Scope authority

- `subjects/Chemistry_4CH1/Specification.pdf` is the **only** authority on what is assessable.
- `subjects/Chemistry_4CH1/specification.md` is your fast index into it. `specification_map.csv` tells
  you where content belongs. `coverage_checklist.md` tells you what is still missing.
- Read `subjects/Chemistry_4CH1/SUBJECT_RULES.md` before writing anything — it records the course distinctions
  that change what this student can be assessed on.

## Before you write

1. Name the **exact specification points** the material will cover, by their official numbers.
2. Confirm the folder from `specification_map.csv`; write there.
3. Read the official wording of those points in the PDF. `specification.md` is an index, not a
   substitute.
4. If a request falls outside the specification, say so and leave it out (enrichment is omitted —
   see `AGENTS.md`).

## How to write

- Follow `rules/STYLE_GUIDE.md` and `rules/SOURCE_POLICY.md`.
- Explain difficult ideas rather than naming them; make definitions mark-scheme precise.
- Do not add off-specification content. Extra material costs revision time and confuses scope.
- Markdown is the master; the topic PDF (`notes/<Subject>/NN_<Topic>.pdf`) is generated from the `topic.md` files by `tools/pdf/build_pdf.py`.
- Templates: `templates/`.

## Working knowledge

Use this repository's own Markdown as your working knowledge of what the student has already
covered. Before answering a question or writing a new topic, check
`subjects/Chemistry_4CH1/topics/` for related material and stay consistent with it.

## Revision, marking and mistakes

- When past papers and mark schemes are available in `me/papers/Chemistry_4CH1/`, use them: they show
  how marks are actually awarded. Reflect that in `questions.md` and in the *Exam relevance*
  section of each topic. Examiner reports, attempts and mistake logs are not kept in the repository.
- When a topic is finished, tick its points in `coverage_checklist.md` and set their `content_status`
  in `specification_map.csv` (those rows only).

## Quality

Run `subjects/Chemistry_4CH1/QA_CHECKLIST.md` against everything you produce before you call it done.
