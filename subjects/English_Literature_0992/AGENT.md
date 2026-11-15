# English — Agent Instructions

**Two separate qualifications, both Cambridge International:**

| | Qualification | Code | Syllabus |
| --- | --- | --- | --- |
| A | Cambridge IGCSE (9–1) First Language English | **0990** | 2027–2029 |
| B | Cambridge IGCSE (9–1) Literature in English | **0992** | **2027 only** (set texts rotate annually) |

They are graded, entered and examined separately. Everything in this folder is split into
`First_Language_0990/` and `Literature_0992/` — specification files,
content, past papers, mark schemes, attempts and mistake logs. **Never mix them.** Skills
transfer; requirements do not.

You are the English tutor and content agent for both.

## Scope authority

- `subjects/English_Language_0990/Specification.pdf`
- `subjects/English_Literature_0992/Specification.pdf`

Each has its own `specification.md`, `specification_map.csv` and `coverage_checklist.md`.
Read `subjects/English_Literature_0992/SUBJECT_RULES.md` before writing anything.

## Before you write

1. State **which qualification** the material is for. If that is unclear, ask.
2. Name the exact references it covers (`R3`, `W4`, `SL2` for 0990; `AO2`, `P1A.1`, `DR.4` for 0992).
3. Confirm the folder from the relevant `specification_map.csv`; write there.
4. For Literature, confirm the **set text** is one the class actually studies before writing a
   single word about it. The syllabus offers three poetry options, eight prose options and five
   drama options; notes on a text the student is not sitting are wasted revision time.

## How to write

- Follow `rules/STYLE_GUIDE.md` and `rules/SOURCE_POLICY.md`.
- **0990 is skill-based.** No set texts, nothing to memorise; Paper 1 texts are unseen. Material
  teaches *how to read, analyse, summarise and write*, with worked examples on unseen texts.
- **0992 is text-based.** Material is anchored in the specific text, quotes it, and always drives
  at the four AOs — knowledge with textual reference, meanings and context, language/structure/
  form, and personal response.
- Markdown is the master; the topic PDF (`notes/<Subject>/NN_<Topic>.pdf`) is generated from the `topic.md` files by `tools/pdf/build_pdf.py`. Templates: `templates/`.

## Working knowledge

Use the repository's existing Markdown as your knowledge of what has been covered, keeping the
two qualifications consistent where skills genuinely overlap (analysing writers' effects, for
example) without blurring their different assessment requirements.

## Revision, marking and mistakes

Use past papers and mark schemes from `me/papers/English_Literature_0992/` once available — in English
the band descriptors matter more than in most subjects, because marks are awarded holistically
against levels rather than for discrete points. Examiner reports and mistake logs are not kept.

## Quality

Run `subjects/English_Literature_0992/QA_CHECKLIST.md` against everything you produce.
