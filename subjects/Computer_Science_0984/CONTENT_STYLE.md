# Computer Science 0984 — Content Style

The subject-specific production standard for every piece of Computer Science revision material in
this repository.

**Read before writing anything:**

1. `rules/CONTENT_RULES.md` — the repository-wide content rule.
2. `rules/STYLE_GUIDE.md` and `rules/SOURCE_POLICY.md`.
3. `subjects/Computer_Science_0984/Specification.pdf` is the scope authority;
   `official_syllabus_update.pdf` **must** be read with it; `specification.md` and
   `specification_map.csv` are the index and the folder map.
4. `subjects/Computer_Science_0984/SUBJECT_RULES.md` — papers, AO weightings, course distinctions.
5. `subjects/Computer_Science_0984/SOURCE_GUIDE.md` — which source governs what, and the textbook's location.
6. `tools/pdf/README.md` — the `topic.md` conventions the builder actually parses.

---

## 1. Core rule

> Create the **smallest** resource that gives the student everything they must remember and
> practise while leaving them fully prepared for Cambridge 0984 questions.

Target:

**SPECIFICATION-COMPLETE + BARE MINIMUM NECESSARY EXPLANATION + EXAM-USABLE + NO FLUFF**

The student has hundreds of topics across all their subjects. Every unnecessary sentence costs revision
time and memory. The goal is *not* "everything useful about this topic".

## 2. Three-level filter

| Level | What it is | Action |
| --- | --- | --- |
| **A — Required** | Explicitly required by the 0984 specification, including every sub-bullet in the *Notes and guidance* column of the mapped point. | Always include. |
| **B — Minimum bridging** | The least explanation or example needed to understand or apply A. | Include only enough to make A usable. |
| **C — Optional / fluff** | Background, extra theory, alternative technologies, historical detail, repeated examples, advanced programming features, generic exam advice. | Normally omit. |

For every substantial sentence or block ask:

> *"If this disappeared, would the student still know and understand enough to answer
> specification-level questions?"*

If yes — remove it.

The *Notes and guidance* column is where 0984 hides the assessable lists. Cover every named item in
it; do not add items it does not name.

## 3. Match depth to the command word

| Requirement wording | What the material must deliver |
| --- | --- |
| identify / state | The concise fact. Nothing more. |
| understand | Enough explanation to demonstrate understanding. |
| describe | Ordered steps or the required features, sufficient for the marks. |
| explain | Cause / reason → effect / consequence. |
| calculate | Method + working + correct answer. |
| write / use / complete | The **applied skill**, actually practised — not a description of it. |

Do not over-teach a low-depth requirement. Do not compress an "explain" point into an unexplained
bullet.

---

## 4. Theory topics (Topics 1–6, Paper 1)

Normally contain only:

- exact definitions;
- the named components / items the specification lists;
- required processes, in order;
- essential differences and comparisons;
- advantages / disadvantages **only where the specification explicitly assesses them**;
- the minimum cause → effect explanation;
- calculations and methods where required;
- a concise diagram where it teaches a process faster than prose.

Do **not** write mini textbook chapters. Worked examples:

- **CPU / FDE cycle** — components plus the exact sequence, clearly. Not a computer-architecture
  essay.
- **Data transmission / networking** — the required process and terminology only. Not networking
  in general.
- **Storage** — only the named technologies and the required comparisons.
- **Cyber security** — the exact named threats, their processes, aims and the named solutions.
  Not a general security encyclopedia.
- **AI / robotics** — only the basic operation and characteristics 0984 asks for.

## 5. Numerical and representation topics

Binary, hexadecimal, two's complement, logical shifts, binary addition and overflow, file-size
calculation, sample rate / resolution / colour depth effects.

Pattern:

> rule or method → **one** concise worked example where necessary → the common required
> distinction or error, only if it genuinely helps.

The student must be able to **do** the operation, not read paragraphs about it. Never give five
equivalent worked examples when one teaches the method. Extra practice belongs in `questions.md`.

No calculators are permitted in either paper — keep arithmetic exam-realistic.

## 6. Process-heavy topics

Where the specification says *describe the process*, preserve the actual ordered steps. Choose the
single most efficient representation:

- a numbered process; **or**
- a compact flow diagram; **or**
- a concise labelled diagram.

Never present the process as a diagram **and** an equivalent table **and** equivalent prose.

---

## 7. Paper 2 material (Topics 7–10)

Topics 7–10 are skill-heavy. Revision material must not become theory-only: the student needs
enough worked structure to actually perform the skill. Include concise, minimum-count examples for:

decomposition · structure diagrams · algorithms · validation and verification · test data ·
trace tables · finding errors in algorithms · pseudocode · variables, constants and data types ·
sequence, selection, iteration · totalling and counting · string handling · nested statements ·
procedures, functions and parameters · local and global variables · library routines · arrays ·
file handling · SQL · Boolean logic.

the topic PDF teaches the method compactly. `questions.md` carries most of the repetition.

## 8. Pseudocode — the decisive rule

The Cambridge pseudocode conventions in **section 4 of the official syllabus** are authoritative.
Use Cambridge-style pseudocode consistently. **Never invent a house syntax.**

From the syllabus guidance at the start of *Algorithms, programming and logic*:

> Where the solution to a problem involves coding, candidates are required to write solutions in
> **pseudocode**. Solutions written in programming code will **not** be awarded marks. The
> exception is the 15-mark scenario question, where pseudocode **or** Python, Visual Basic or Java
> is accepted.

So: pseudocode is the default and, for everything except the scenario question, the only thing that
scores. The classroom high-level language is a centre choice (`me/profile.md`). Unless the student asks
for examples in it:

- write everything in Cambridge pseudocode;
- do **not** generate parallel Python / Java / VB examples;
- do **not** assume a classroom language.

The endorsed textbook uses real code in places. It may inform understanding; it does not change what the
revision material writes.

### Conventions to follow exactly

- Keywords in UPPER CASE (`IF`, `REPEAT`, `PROCEDURE`); identifiers in Pascal case
  (`NumberOfPlayers`), letters and digits only, starting with a capital.
- Assignment is `←`. Comments are `//`.
- Four-space indentation; `THEN` / `ELSE` clauses and `CASE` cases indented by two.
- Data types: `INTEGER`, `REAL`, `CHAR`, `STRING`, `BOOLEAN`. `DECLARE <identifier> : <data type>`.
- Char in single quotes, string in double quotes, real always with a digit each side of the point.
- Arithmetic operators limited to `+ – / * ^ MOD DIV`; relational to `= < <= > >= <>`; logical to
  `AND OR NOT`.
- Library routines limited to `MOD`, `DIV`, `ROUND`, `RANDOM`.
- Procedures and functions take **up to three parameters**.
- Nesting: candidates are never required to write more than **three levels**.
- Array first index may be zero or one — say so once; do not labour it.

## 9. Programming scope

Teach only what topic 8 maps. Do **not** add object-oriented programming, recursion, advanced data
structures, language-specific shortcuts, APIs or frameworks, or advanced exception handling.

Prefer **one clear canonical example** over many variations. Maintainability (8.1.8) is a short
required list — meaningful identifiers, commenting, procedures and functions — not an essay on
software engineering.

## 10. Algorithms and trace tables

Standard methods of solution are limited to: linear search, bubble sort, totalling, counting, and
finding maximum, minimum and average values. Teach those; do not add other sorts or searches.

Trace tables must record variables, outputs and user prompts at each step. Teach the method with
**one** clear trace. Do not fill the topic PDF with near-identical traces — that is `questions.md`'s
job.

Test data is limited to normal, abnormal, extreme and boundary, with the syllabus's own definitions
of extreme and boundary. Reproduce those definitions precisely; they are frequently confused.

## 11. SQL

Single-table only. Limited to `SELECT`, `FROM`, `WHERE`, `ORDER BY ASCENDING`,
`ORDER BY DESCENDING`, `SUM`, `COUNT`, `AND`, `OR`, plus identifying the output an SQL statement
produces from given table contents.

Do **not** expand into joins, relational design theory, normalisation, `INSERT`/`UPDATE`/`DELETE`
or advanced SQL. Use concise examples that demonstrate the required syntax against one small
sample table reused throughout the topic.

## 12. Boolean logic

Use the **exact** standard gate symbols from section 4 of the syllabus. Gates required: `NOT`,
`AND`, `OR`, `NAND`, `NOR`, `XOR (EOR)`. `NOT` is single-input; all others are limited to two
inputs. Circuits are limited to three inputs and one output, and are **drawn as stated, without
simplification**.

Teach enough examples to cover the required transformations —

> problem statement ↔ logic expression ↔ logic circuit ↔ truth table

— but do not repeat every possible transformation several times. Truth-table row order follows the
syllabus example (000, 001, 010, 011, 100, 101, 110, 111).

Visual accuracy is essential: a gate drawn wrongly teaches the wrong answer.

---

## 13. Diagrams

Computer Science **should** use diagrams where they genuinely reduce cognitive load — the FDE
cycle, packet structure and packet switching, network relationships, automated-system
sensor → microprocessor → actuator loops, flowcharts, storage comparisons, logic circuits, and
other process or architecture concepts.

But:

- decide the best single representation from the mapped specification, then use only that;
- never diagram **and** tabulate **and** describe the same content;
- no decorative visuals, and never a diagram to make a PDF look richer;
- flowcharts must use the standard flowchart symbols in section 4 of the syllabus.

### Renderer constraints

The topic PDF is built by `tools/pdf/build_pdf.py`, which renders each `topic.md`
in headless Chromium. SVGs are inlined, so ordinary SVG (including an internal `<style>` block)
works. Give the root `<svg>` a `viewBox`, use `Carlito, Calibri, sans-serif` to match the booklet,
and see `tools/pdf/assets/diagram_01_demo.svg` for a working pattern.

Always open the built PDF and check every figure actually rendered before calling a topic done.

---

## 14. Source use

`subjects/Computer_Science_0984/SOURCE_GUIDE.md` holds the hierarchy. In short: the specification decides **what**, the
textbook explains **how**, targeted web research fills a specific gap.

Consult the textbook for every assigned topic before writing — use its explanations, terminology,
teaching sequence and conceptual framing. Then:

- compress aggressively to the mapped 0984 requirement;
- do not preserve the textbook's chapter structure where the repository mapping is more efficient;
- do not import off-spec material simply because it sits beside required material;
- do not reproduce long passages verbatim — paraphrase into concise revision language;
- the textbook can never expand the syllabus.

---

## 15. File roles

| File | Role |
| --- | --- |
| `topic.md` | Canonical, specification-complete teaching of the knowledge **and** the skill — still concise. Master copy. |
| `summary.md` | Ultra-compressed last-minute revision. Dramatically shorter than `topic.md`. |
| `questions.md` | Focused practice: calculations, conversions, tracing, pseudocode, SQL, logic and exam-style application. This is where repetition lives. |
| topic PDF | `notes/Computer_Science_0984/NN_<Topic>.pdf` — the polished main human revision resource, generated from the `topic.md` files. |
| `assets/` | Only diagrams that genuinely earn their place. |

the topic PDF holds what the student must **learn and remember**. `questions.md` holds most of the
**practice**. Do not inflate the topic PDF with a large question bank.

Important examinable knowledge must never exist only in the PDF or only in the summary.

### Topic PDF standard

Normally include:

- topic title and a small specification reference;
- essential definitions;
- required knowledge;
- required procedures and methods;
- one worked example where necessary;
- diagrams or tables only where they are the most efficient representation;
- a tiny remember / common-error box, only where genuinely useful.

Normally do **not** include:

- reproduced specification tables;
- large "by the end of this topic..." panels;
- generic introductions;
- long exam-technique sections;
- checklists, recaps, self-tests or answers (none of these ever go in the PDF);
- decorative visuals;
- multiple equivalent examples.

## 16. Length

No fixed page count. A small specification topic should genuinely produce a small resource; a
skill-heavy or process-heavy topic may fairly need more space. Page count is not the objective.

> **Nothing required missing. Nothing unnecessary present.**

## 17. Final test

Run `subjects/Computer_Science_0984/QA_CHECKLIST.md`, then inspect every major block and ask:

1. Is this required by the mapped specification point, including its *Notes and guidance*?
2. If not, is it genuinely necessary to understand or apply something that is?
3. Is it repeated elsewhere in the pack?
4. Where the requirement says *use / write / complete / calculate*, is the skill actually
   practised rather than only described?
5. Could the student still get full marks without it?

If the answer to #5 is yes and it is not necessary bridging — remove it.
