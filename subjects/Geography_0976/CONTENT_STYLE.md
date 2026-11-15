# Geography 0976 — Content Style

The subject-specific writing standard. Sits under `rules/CONTENT_RULES.md`
and `rules/STYLE_GUIDE.md`; where this file is more specific, follow this file.

**The standard:** SPECIFICATION-COMPLETE + MINIMUM NECESSARY EXPLANATION + EXAM-USABLE + NO FLUFF.

The governing question for every line you write:

> Does the student need to remember this to answer Cambridge 0976 questions on exactly these
> specification points?

If not, cut it. The student has hundreds of topics across all their subjects; length is a cost.

## 1. Scope

- The official specification is the only scope authority. Read the point's **official wording**
  in `subjects/Geography_0976/Specification.pdf` — every named term and every sub-bullet in it is
  assessable and must appear.
- Where the specification lists terms (`hydraulic action, abrasion, attrition, solution`), every
  listed term is required. Where it says "for example, …", the list is illustrative of the *kind*
  of content assessed — cover the idea, not necessarily each item, and never treat it as a
  case-study requirement (see §7).
- Do not pre-teach a later topic. Give only what the current point needs and cross-reference.
- Do not add off-specification material. Bridging that is genuinely needed to understand a
  required point stays, briefly; enrichment is omitted.

## 2. Depth — match the specification's own verb

| Specification wording | What you write |
| --- | --- |
| characteristics / features / types / names | the precise list, in a table or labelled diagram |
| the processes which… / how… operates | the causal chain, each step doing real work |
| the causes of… | the causes, separated into human and natural/physical where the point does |
| the impacts of… | impacts, categorised (see §4) |
| the strategies and techniques used to manage… | what each does, how it works, and what it costs |
| **an evaluation** of… | the above **plus** strengths, weaknesses and a basis for judgement |
| including sustainable | an explicit sustainability line for the strategies (see §5) |
| the model and its strengths and limitations | the model, then the limitations as a short list |

Do not inflate a recall point into an essay. Do not compress an "evaluation" point into a bullet
list with no judgement.

## 3. Processes

Physical and human processes must be understood, not merely named.

- Represent a process **once**, in its strongest form: an annotated diagram or a compact
  cause → mechanism → consequence chain. Not a diagram *and* a table *and* a paragraph.
- Each arrow in a chain must carry a mechanism, not a restatement. "Sea level rises → coastal land
  floods" is a step; "climate change → problems" is not.
- Landform formation: give the sequence of stages a candidate can reproduce, with the process names
  the specification uses at each stage.

## 4. Impacts, causes and management

The syllabus assumes three recurring frames. Use them where they add precision, not as a template
to be filled in everywhere:

- **Impacts:** positive/negative; social, economic, environmental; local → regional → national →
  global. Use whichever categories the point actually asks for; do not print an empty grid.
- **Causes:** human vs natural/physical where the specification separates them.
- **Management:** distinguish **strategies** (plans, policies, agreements) from **techniques**
  (the physical or practical methods). Cambridge uses both words deliberately.

Where the point requires cause → impact → management, keep the relationship visible: the reader
should be able to trace a named impact back to a named cause and forward to the strategy that
addresses it.

## 5. Evaluation and sustainability

- Evaluate only where the specification says "an evaluation". Elsewhere, state and explain.
- An evaluation is: what it achieves, what it costs or fails to do, and on what basis you would
  judge it. Two sharp lines beat a paragraph of hedging. A short strategy-by-strategy table with a
  judgement column is usually the most efficient form.
- "Including sustainable" is a requirement, not a flourish: say whether the strategy addresses the
  cause or only the symptom, whether it lasts, and what it costs socially, economically and
  environmentally.

## 6. Definitions and terminology

- Definitions are mark-scheme precise and one sentence long. Use Cambridge's own terminology and
  spelling (e.g. *corrasion*, *corrosion*, *levée*, *divergent/constructive*).
- Define a term once, in the topic that owns it.
- Give figures with units the syllabus uses: metres/kilometres, °C, millimetres.

## 7. Ordinary examples vs detailed specific examples

Two different things. Do not confuse them.

**A — Ordinary illustrative content.** Specification wording such as "for example, resource
exploitation, climate change, fishing, tourism" (3.2.1) or "for example, trade, international aid,
and debt relief" (8.3.3). This is generic assessable content. Write it from the specification and
ordinary geographical knowledge; a brief, well-chosen illustration is fine. **No class source is
required.**

**B — A detailed specific example.** Specification wording such as "One detailed specific example
to include:", "of a named country", "of a named area", "of a named urban area", "of a named
volcano". Cambridge does not name these — the centre chooses them, and the student must be able to
write place, date, figures and outcomes they actually studied. **These require confirmed class
source material.** All 16 of them are listed in `CASE_STUDY_TRACKER.md`.

### Rules for B

1. Write a detailed specific example **only** from confirmed student/class source material —
   the student's class notes, case-study document or photographed textbook pages in `me/sources/Geography_0976/`.
2. **Never fabricate** dates, statistics, named locations, impacts, responses, outcomes or
   evaluation points for a class example. Not a rounded figure, not a "typical" death toll, not a
   plausible scheme name.
3. Never substitute a famous or plausible case study for the class one, and never quietly "improve"
   the class example with web or model detail. Only do outside research on a class example if the
   student explicitly asks for it.
4. If the source supports some sub-bullets but not others, write what is supported and mark the
   gap under the unsupported sub-bullet only.
5. If the source contains something that looks wrong (an implausible figure, a slipped direction),
   do not silently correct it and do not print it as fact — flag it in the tracker note and ask the
   student.
6. A missing example never blocks the topic. Complete all other specification content, then place:

   ```
   > ⚠ Case study source needed — Specification X.X.X
   > Required detailed specific example not found in the supplied class sources.
   ```

   Nothing goes underneath it. No temporary content, no "meanwhile, consider…".
7. Tell the student, in the session report, exactly which spec point is unresolved and what kind of
   source would close it.

## 8. Visuals

Include a diagram, map, cross-section, flow chart or graph when it teaches faster or more clearly
than words — and then delete the words it replaced. A visual that duplicates adjacent prose is
worse than no visual.

Typically worth drawing in this subject: landform formation sequences, drainage-basin and coastal
process diagrams, plate-boundary cross-sections, global distribution maps, the DTM, population
pyramids, the Butler model, systems diagrams (inputs/processes/outputs), climate graphs.

Decide per topic, from the specification. Nothing here prescribes a visual for a given topic.
Every figure must be geographically accurate, labelled with the specification's own terms, legible
in greyscale, and must render correctly in the topic PDF.

## 9. The files

Per `rules/CONTENT_RULES.md` §6 and `tools/pdf/README.md`.

| File | Role |
| --- | --- |
| `topic.md` | Complete canonical notes: every mapped requirement, taught once, in its strongest representation. Markdown is the master. |
| `summary.md` | Much shorter last-minute revision — the facts, definitions, chains and figures worth carrying into the exam. Not a second teaching pass. |
| `questions.md` | Focused practice across the mapped scope, with concise answers and marking guidance. Use Cambridge command words and printed sub-marks. |
| topic PDF | **The main human revision resource** (`notes/Geography_0976/NN_<Topic>.pdf`). Generated from the `topic.md` files; never hand-edited. Carries the visuals; no recap, self-test, answers or checklist. |

A detailed specific example belongs in `topic.md`, is compressed to its memorable core (place,
date, three or four figures, the management line) in `summary.md`, and is examined in
`questions.md`. A missing-source placeholder must appear in **all** three markdown files, so no file silently
looks complete.

## 10. Do not

- Write textbook background, history of the discipline, or scene-setting introductions.
- Give three examples where one carries the idea.
- Teach the same idea as prose *and* a table *and* a diagram.
- Repeat `topic.md` inside `summary.md`, or put any questions inside the PDF.
- Add motivational padding, "it is important to note", or exam-technique sections that restate the
  content.
- Present anything as examinable that the specification does not require.
- Invent a case study, or any part of one.
