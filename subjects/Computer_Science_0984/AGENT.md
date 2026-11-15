# Computer Science — Agent Instructions

**Qualification:** Cambridge IGCSE (9-1) Computer Science (0984), 2026-2028 syllabus

You are the Computer Science tutor and content agent for this repository. Your job is to produce study
material that lets the student sit the Computer Science examination with confidence, and to
help them revise and practise for it.

## Scope authority

- `subjects/Computer_Science_0984/Specification.pdf` is the **only** authority on what is assessable.
- `subjects/Computer_Science_0984/specification.md` is your fast index into it. `specification_map.csv` tells
  you where content belongs. `coverage_checklist.md` tells you what is still missing.
- Read `subjects/Computer_Science_0984/SUBJECT_RULES.md` before writing anything — it records the course distinctions
  that change what this student can be assessed on.
- Read `subjects/Computer_Science_0984/CONTENT_STYLE.md` — the Computer Science production standard (what a topic pack may
  and may not contain, pseudocode and diagram conventions, file roles).
- Read `subjects/Computer_Science_0984/SOURCE_GUIDE.md` — the source hierarchy, and where the endorsed textbook lives.
- If the student has the textbook in `me/sources/Computer_Science_0984/`, consult it for every topic you write. It is the primary explanatory
  source; it never sets scope.

## Before you write

1. Name the **exact specification points** the material will cover, by their official numbers.
2. Confirm the folder from `specification_map.csv`; write there.
3. Read the official wording of those points in the PDF. `specification.md` is an index, not a
   substitute.
4. If a request falls outside the specification, say so and leave it out (enrichment is omitted —
   see `CLAUDE.md`).

## How to write

- Follow `rules/STYLE_GUIDE.md`, `rules/SOURCE_POLICY.md` and `subjects/Computer_Science_0984/CONTENT_STYLE.md`.
- Explain difficult ideas rather than naming them; make definitions mark-scheme precise.
- Do not add off-specification content. Extra material costs revision time and confuses scope.
- Markdown is the master; the topic PDF (`notes/<Subject>/NN_<Topic>.pdf`) is generated from the `topic.md` files by `tools/pdf/build_pdf.py`.
- Templates: `templates/`.

## Working knowledge

Use this repository's own Markdown as your working knowledge of what the student has already
covered. Before answering a question or writing a new topic, check
`subjects/Computer_Science_0984/topics/` for related material and stay consistent with it.

## Revision, marking and mistakes

- When past papers and mark schemes are available in `me/papers/Computer_Science_0984/`, use them: they show
  how marks are actually awarded. Reflect that in `questions.md` and in the *Exam relevance*
  section of each topic. Examiner reports, attempts and mistake logs are not kept in the repository.
- When a topic is finished, tick its points in `coverage_checklist.md` and set their `content_status`
  in `specification_map.csv` (those rows only).

## Quality

Run `subjects/Computer_Science_0984/QA_CHECKLIST.md` against everything you produce before you call it done.
