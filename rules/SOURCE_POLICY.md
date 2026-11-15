# Source Policy

## Priority order

1. **The current official specification / syllabus.**
   Determines *what is assessable*. Downloaded locally to
   `subjects/<Subject>/Specification.pdf` (not in Git — `tools/fetch_specs.py`). Nothing overrides it.
2. **Official exam-board resources.**
   Mark schemes, examiner reports, sample assessment materials, official guidance, grade
   boundaries, formulae sheets. These determine *how it is assessed and rewarded*.
3. **The student's school material** (`me/sources/<Subject>/`, never in Git).
   Schemes of work, class notes, teacher resources, case-study documents. These
   determine *what the class is doing and when*, and identify the qualification and options.
4. **High-quality educational and reference sources.**
   Reputable textbooks, university and academic sources, established subject organisations,
   well-regarded revision publishers. Used to *research and explain* the curriculum better.
5. **Other sources.**
   Only when genuinely useful, and only after checking them against 1–4.

## Rules

- **Scope is set by the specification.** A source at level 3–5 may improve an explanation, add
  an example, or clarify a mechanism. It must never quietly add, remove or redefine content.
  If a source disagrees with the specification, the specification wins and the discrepancy is
  worth a note.
- **Watch for the wrong qualification.** Much online material is written for a different board,
  a different tier, or a different specification version. Check the code (e.g. 4BI1 vs 4SD0,
  0976 vs 0460) before using anything.
- **Synthesise, don't copy.** Research is read and re-expressed in this repository's own words
  and structure. Do not paste long passages from any source.
- **Prefer current documents.** Specifications and syllabuses are versioned; check the years a
  syllabus covers (`specification.md` says which version the map was built from).
- **Say when you are unsure.** An honest "the specification does not say" is more useful than a
  confident guess.

- **Copyright.** Never commit textbooks, past papers, mark schemes or school documents. They
  live in `me/` (ignored by Git). Notes paraphrase; diagrams are drawn for this repository or use
  openly licensed images recorded in the subtopic's `assets/SOURCES.md`.
