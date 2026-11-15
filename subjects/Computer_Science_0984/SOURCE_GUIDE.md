# Computer Science 0984 — Source Guide

Which source governs what, when writing Computer Science revision material.

## Hierarchy

| # | Source | Authority over |
| --- | --- | --- |
| 1 | `subjects/Computer_Science_0984/Specification.pdf` + `subjects/Computer_Science_0984/official_syllabus_update.pdf` | **What is assessable and to what depth.** Absolute. Nothing overrides it. |
| 2 | The endorsed textbook, **if the student owns it** — their copy goes in `me/sources/Computer_Science_0984/` (never in Git) | **How** to explain specification content: explanations, terminology, teaching sequence, conceptual framing. |
| 3 | Official Cambridge assessment material held locally (`me/papers/Computer_Science_0984/`: papers, mark schemes, specimen papers) | Exam wording, pseudocode conventions in practice, marking expectations.  |
| 4 | Targeted web research | Only to fill an exact gap left by 1–3. |

**Always read the syllabus update with the specification.** It is a live change log — version 5,
December 2025 at the time of writing — and it has already changed operator names, the parameter
limit for procedures and functions, and, critically, the rules on writing solutions in pseudocode
versus program code.

## The textbook

| Field | Value |
| --- | --- |
| Title | *Cambridge IGCSE™ and O Level Computer Science*, Second Edition |
| Authors | David Watson and Helen Williams |
| Publisher | Hodder Education, 2021 · ISBN 9781398318281 |
| Endorsement | Endorsed for full syllabus coverage; written for 0478 / 0984 / 2210 **for examination from 2023** |
| Where it goes | If the student owns it: `me/sources/Computer_Science_0984/` (never commit it) |

Its chapters 1–10 map cleanly onto specification topics 1–10, so finding the relevant pages for a
mapped topic is direct.

### Version drift — check this every time

The textbook was written for the **2023–2025** syllabus. Students now sit the **2026–2028**
syllabus. Where the two differ, the specification wins, silently and always. In particular the
book predates every change listed in `official_syllabus_update.pdf`. Treat the book as an
explanation source, never as a scope or convention source.

## Cambridge pseudocode, flowcharts and logic gates

**Section 4 of the official syllabus is the only authority** for:

- the pseudocode format used in examinations;
- the standard flowchart symbols students must use;
- the standard logic gate symbols students must use.

The syllabus guidance for topics 7–10 states that where a solution involves coding, candidates must
write it in **pseudocode**; program code scores nothing — the sole exception being the 15-mark
scenario question, which accepts pseudocode or Python, Visual Basic or Java.

The classroom high-level language is a centre choice and has **not** been confirmed. Until it is
recorded in `me/profile.md`, write Cambridge pseudocode only. Do not produce parallel
Python / Java / VB versions. The textbook's real-code examples may aid understanding; they do not
change what the revision material writes.

## Targeted web research

Allowed only when:

1. a mapped specification point is not adequately explained in the textbook;
2. a factual or technical detail looks unclear or outdated;
3. an official Cambridge convention needs verification;
4. a required concept genuinely needs a second authoritative explanation.

When browsing: search the specific gap only, prefer Cambridge first, then authoritative technical
or educational documentation, and stop once the gap is closed. No broad research per topic.

If external information materially enters a pack, note it during QA and say where it came from —
do not present it as textbook-derived.

## The rule that governs all of the above

> **No source below the specification may expand the assessable syllabus.**

A textbook or web source may improve an explanation, supply an example, or clarify a mechanism. It
may never add, remove or redefine what is assessed. Where a source disagrees with the
specification, the specification wins and the discrepancy is worth a note.

Do not reproduce long passages from the textbook. Paraphrase into concise revision language.
