# Biology 4BI1 — Content Style

How Biology packs are written. Read this with `SUBJECT_RULES.md` (what is assessable) and
`rules/CONTENT_RULES.md` (repository-wide rules). This file records the
Biology-specific decisions so future prompts can stay short.

## 1. Core standard

Every Biology pack must be:

> **SPECIFICATION-COMPLETE + CLEAR ENOUGH TO LEARN FROM + AS CONCISE AS REASONABLY POSSIBLE**

The student sits many subjects. Do not build a textbook replacement. Never drop an
assessable requirement to save space; never add material because it is interesting.

## 2. Representation priority

For any required point, choose the cheapest representation that teaches it properly:

1. **A useful annotated diagram**
2. **A compact table**
3. **Concise prose**

Pick one. Do not teach the same information as a figure, *then* an equivalent table, *then*
equivalent prose. If a good diagram already teaches the point, let it do the teaching and write
only what the diagram cannot carry.

## 3. Visuals

Use diagrams where they genuinely improve understanding of:

- structures · processes · mechanisms · cycles
- practical setups · transport pathways
- graphs · cause-and-effect relationships

Diagrams must be scientifically accurate, clearly labelled and educational — never decorative.
Preserve the visual quality already established by the existing Biology PDFs (SVG assets in the
topic's `assets/` folder; roughly 3–8 diagrams for a mid-to-large topic, 1–2 for a small one).

## 4. Definitions and explanation depth

Give an important definition **once**, in full, mark-scheme precise. Afterwards use the term;
do not restate the definition.

Match depth to the specification command word:

| Command word | Depth to give |
| --- | --- |
| state / know / identify / name | The concise fact only |
| describe | The necessary features or stages |
| understand / explain | The necessary causal reasoning |
| compare | The useful similarities/differences, paired |
| calculate | Method + units (one worked example if the method is not obvious) |
| practical | Method, variables, expected results, interpretation, evaluation — at IGCSE depth only |

Do not inflate a simple recall point into a mini-chapter. Do not compress an explain point into
an unexplained bullet.

## 5. Practical investigations

Where possible:

> **diagram = apparatus + numbered method**

Prose then adds only what the diagram cannot efficiently communicate:

- variables (independent, dependent, controlled)
- expected results
- interpretation
- controls and why they are needed
- the evaluation points that actually earn marks

Do not follow a fully illustrated method with a second complete written method.

## 6. Repetition

Avoid:

- **figure → table → prose** triplication of the same content
- repeating a full definition several times
- separate *exam relevance* and *common mistakes* sections that say the same thing

Normally keep **one** concise traps/misconceptions area per topic (a short "Wrong / Right"
table works well). Fold anything genuinely about exam technique into it rather than creating a
standalone "How this topic is examined" section.

## 7. Summary and questions

`summary.md` is the compact rapid-revision file; it must **compress, not reteach**.
`questions.md` holds all practice. Neither is rendered into the PDF, and the PDF carries no recap,
self-test, answers or checklist.

## 8. Density

There is **no fixed page limit** — length scales with specification complexity.

Warning signs of a badly proportioned pack:

- a small topic carrying large fixed back-matter sections
- duplicate tables and figures

Rough diagnostic only (measured on completed Section 02 packs):

- large Biology topics tend to land around **0.7–0.9 PDF pages per specification point**
- above **~1.5 pages per point**, run a duplication check

These are **not quotas**. Do not pad a short topic up to them or cut required content down to
them.

## 9. Calibration from the Section 02 audit

What the completed packs showed:

- **Level of organisation** — too long: a fixed template dominated a one-point topic.
- **Respiration** — about the right density.
- **Nutrition** and **Transport** — long, but their scope justified much of the length.
- The systematic problem was **duplication and oversized back matter**, not weak specification
  discipline.

Future packs must avoid:

1. figure + duplicate table + duplicate prose
2. several traps / exam-commentary sections
3. standalone "How this topic is examined" sections
4. definitions repeated verbatim
5. practical diagrams plus a duplicate complete written method
6. any back matter (recap, self-test, answers, checklist)

Sections of the shared template are **optional**. Delete any heading a topic does not need
rather than filling it.

## 10. Final check before calling a pack done

- Every mapped specification point is covered, at command-word depth.
- Each required point is taught once, in its best representation.
- Diagrams are accurate, labelled and load-bearing.
- One traps/misconceptions area; no duplicate exam-commentary block.
- No back matter in `topic.md` or the PDF; `summary.md` compresses rather than reteaches.
