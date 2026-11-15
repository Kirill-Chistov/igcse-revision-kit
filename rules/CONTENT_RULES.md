# Content rules

## Purpose

Detailed content rules for creating, editing, compressing, reviewing or auditing study material in
this repository. `CLAUDE.md` is the canonical rule set (layout, write safety, PDF rules, lean pass)
and wins on any conflict; `rules/WORKFLOW.md` gives the ordered steps. This file explains
**how much** to write and **how** to present it.

Students sit many subjects. The goal is **not** the most comprehensive textbook possible; it is
the **smallest genuinely complete exam-ready resource** for each specification topic.

## 1. Core content rule

> Include everything the official specification requires, plus only the minimum extra explanation
> needed to understand and apply it correctly.

**SPECIFICATION-COMPLETE + CLEAR ENOUGH TO LEARN FROM + AS CONCISE AS REASONABLY POSSIBLE**

Do not add material merely because it is interesting, related, normally taught in textbooks, useful
at the next level, or theoretically connected to an exam question.

Remove enrichment before required explanation, repetition before required detail, extra examples
before required examples. Never remove an assessable requirement to make the resource shorter.

## 2. Three-level information filter

- **Level A — Required.** Everything the specification explicitly requires: facts, definitions,
  processes, structures/functions, equations, calculations, required examples, practical knowledge,
  prescribed case studies, assessed skills, named terminology, Higher/separate-science material.
- **Level B — Bridging.** Only when needed: the small amount of extra information required to
  understand, explain, apply, or avoid a likely misconception about Level A. Keep it brief.
- **Level C — Enrichment.** Omit: side facts, advanced mechanisms, history, future-course detail,
  redundant examples, pre-teaching another topic, broad context.

## 3. Do not pre-teach later topics

If a concept is taught fully later in the specification, give only what is needed now and
cross-reference the later topic. This prevents duplication across topic folders.

## 4. Source authority

1. Current official specification/syllabus — **what** is required.
2. Official exam-board material — mark schemes, examiner reports, sample assessments, guidance.
3. The student's school material (`me/sources/`) — course-specific examples, set texts, case
   studies, teacher requirements.
4. Reliable educational/reference sources — **how** to explain required material.

External research must improve explanation or assessment accuracy; it must not silently expand
scope. The official PDF wins when `specification.md` is condensed or ambiguous. Details in
`SOURCE_POLICY.md`.

## 5. Repository architecture

See `CLAUDE.md` § Repository layout. In short: one PDF per top-level topic in
`notes/<Subject>/NN_<Topic>.pdf`; all sources in `subjects/<Subject>/topics/NN_<Topic>/NN_<Subtopic>/`;
everything personal in `me/`. Do not redesign this architecture during content generation.

## 6. Standard pack and pipeline

```text
official specification → exact mapped scope → topic.md (per subtopic)
                                               ├─ summary.md    (markdown only)
                                               └─ questions.md  (markdown only)
all topic.md of a topic → build_pdf.py → notes/<Subject>/NN_<Topic>.pdf
```

- `topic.md` — complete canonical teaching resource.
- `summary.md` — much shorter 5–10 minute rapid revision (no checklist).
- `questions.md` — focused practice bank with concise answers/marking guidance.
- The topic PDF — polished primary learning resource, rendered from `topic.md` only. No recap,
  self-test, answers or checklist.

`assets/` only when genuinely useful visuals are needed. Important examinable knowledge must not
exist only in the summary or the PDF.

## 7. Visual rule

Plan visuals before writing (see `CLAUDE.md` § Visual rule). Use labelled diagrams, flowcharts,
graphs, maps, timelines, worked visual examples, experimental setups, cause → mechanism →
consequence diagrams. A useful diagram replaces several paragraphs — delete those paragraphs.
Tables are for comparisons only. No decorative images.

- **Sciences:** structures, mechanisms, cycles, practical setups, graphs.
- **Mathematics:** worked examples, graphs, geometry diagrams, annotated methods.
- **Geography:** real photographs of visible features, process diagrams, maps, graphs, case-study visuals.
- **Business:** diagrams for chains and models (break-even chart, cash-flow chain, organisation charts, product life cycle, supply/demand), worked calculations; tables only for comparisons.
- **Computer Science:** architecture diagrams, flowcharts, trace tables, pseudocode/code, data representations.
- **Languages:** vocabulary organisation, grammar patterns, model structures.
- **English:** textual analysis, argument structure, assessment requirements, set-text evidence; visuals only when they clarify structure.

## 8. Match depth to the specification command word

- **name/state/give** → precise item/fact.
- **define** → exam-accurate definition.
- **describe** → necessary features/stages/pattern.
- **explain** → causal mechanism/reason.
- **compare** → relevant similarities/differences.
- **calculate** → formula/method, substitution and units.
- **interpret/apply/suggest** → enough conceptual understanding for unfamiliar contexts.
- **evaluate/discuss** → relevant reasoning, evidence, trade-offs and judgement structure.

Do not inflate a recall point into a mini-chapter; do not compress an explanation point into an
unexplained bullet.

## 9. Repetition rule

- `topic.md` teaches fully, once.
- `summary.md` compresses.
- `questions.md` retrieves/applies.
- The PDF presents `topic.md`; it adds nothing and repeats nothing.

Avoid repeated teaching inside `topic.md`, exam-tip sections that repeat the content, near-identical
tables, and full teaching of material assigned to another topic. Keep one traps/misconceptions
area per subtopic at most.

## 10. PDF density

There is no page limit; shorter is better only when educational completeness is equal. The PDF should
feel like a **high-density revision booklet**, not a textbook. Before adding material ask: Is it
mapped? Is the explanation necessary? Could a diagram/table teach it more efficiently? Is it
repeated? Does it belong to a later topic? A small specification topic should produce a small
resource.

## 11. Questions

All practice lives in `questions.md`. Non-official marking guidance must not be presented as an
official mark scheme. Where the student has added past papers in `me/papers/<Subject>/`, use them to shape question style
and marking points.

## 12. Prompts

The normal request is just `/make-topic <subject> <topic>` (or "Create Physics Topic 1"). The
repository supplies everything else; do not ask the user to restate scope, rules or folders.

## 13. Parallel sessions

Parallel sessions reduce wall-clock time **only when their write scopes do not overlap**.

Safe: Session A → Biology topic 02, Session B → Chemistry topic 01, Session C → Business topic 03.

Never run parallel sessions that may change the same topic, `rules/*`, `tools/*`, the
same subject's specification map/checklist. Sessions sharing a subject skip tracker updates; do one
tracker pass afterwards. Each session commits only its own paths when it finishes (`CLAUDE.md` §
Commit when you finish). Before large batches, make a clean baseline commit and a
backup. Parallel sessions do not create extra usage allowance — optimise for completed useful
topics per unit of usage.

## 14. Editing vs regenerating

If existing material is accurate and visually strong but too long: **edit/compress it; do not
regenerate.** Regeneration costs more usage, may introduce errors, lose good diagrams, and cause
style drift. A tightening edit preserves all mapped coverage and useful visuals, removes Level C
and duplication, replaces long prose with compact diagrams/tables where better, stops
pre-teaching, and ends with one specification-coverage check. Regenerate only when the material
has a factual or structural problem harder to repair than rebuild.

## 15. Biology calibration

The first Biology pilots set the visual standard but overshot density: later topics were
pre-taught, practical/calculation material went beyond the point, and back matter was large.
Use 1.2–1.4 *Variety of living organisms* as the reference for **visual clarity** (classification
diagrams, fungal/bacterial/viral visuals, specification-named examples), not for length.

## 16. Definition of a successful pack

- covers every mapped specification point at command-word depth;
- understandable without a textbook for missing core explanation;
- teaches no substantial unrelated/later content;
- presents important information efficiently and visually;
- has a summary meaningfully shorter than the master notes and focused questions;
- produces a topic PDF the student would realistically revise from, proportionate to the
  specification content;
- keeps a whole multi-subject course realistically learnable.

> **What is the least material the student needs in order to fully understand and answer
> questions on exactly these specification requirements?**
