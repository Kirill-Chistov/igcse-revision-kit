---
# ---------------------------------------------------------------------------
# Front matter drives the cover block, the running footer and PDF metadata.
# Every key is optional; delete what you do not need.
# ---------------------------------------------------------------------------
title: Example topic
eyebrow: Pearson Edexcel International GCSE Biology · 4BI1 · Section 2(b)
subtitle: >
  Specification points 0.1–0.3 — this file is the authoring reference for
  tools/pdf; render it to see every supported block.
footer: Edexcel International GCSE Biology 4BI1 · 0.1–0.3B Example topic
subject: Pearson Edexcel International GCSE Biology 4BI1, specification points 0.1, 0.2, 0.3B
keywords: [4BI1, IGCSE Biology, example, pipeline]
repo_path: tools/pdf
---

# Example topic

## 1. Ordinary markdown

A `## N. Heading` becomes a numbered section: the leading number turns into the
teal badge and the rest into the serif heading. Body text, **bold**, *italic*,
cross-references *(→ 2.15)* and lists all work as normal markdown.

- Bullets are compact by design.
- Nested lists keep the same rhythm.

| Structure | Description | Function |
| --- | --- | --- |
| Nucleus | bounded by a membrane; contains chromosomes | controls the cell's activities |
| Ribosomes | very small organelles in the cytoplasm | site of **protein synthesis** |

Tables get the mint header row automatically; the first column is bolded. Add
`{: .plain }` after a table to switch that off.

![A demonstration diagram](assets/diagram_01_demo.svg)

*Figure 1. An image followed by an italic paragraph becomes a figure with a
caption. Local SVGs are inlined, so they stay sharp and scale to the column.*

## 2. Callout blocks — Paper 2 only

A `— Paper 2 only` suffix on a heading becomes the purple badge.

::: definition
**Differentiation** — the process by which an unspecialised cell develops the
structures needed to become a specialised cell with a particular function.
:::

::: traps
The cell wall is fully permeable — the **membrane** controls entry and exit.
Mitochondria **release** energy; they do not make it.
:::

::: exam
*Discuss/evaluate* questions need at least one point from each side. Use "may"
and "risk" for outcomes that are not certain.
:::

::: why
A specialised cell carries out one function far more efficiently than a cell
doing everything.
:::

::: note | Practical note
Any callout label can be overridden after a pipe: `::: note | Practical note`.
:::

## 3. Side-by-side layouts

Nest blocks by using more colons on the outer fence than on the inner one.

:::: grid
::: card | Embryonic stem cells
From an early embryo; can become **any** type of cell.
:::
::: card | Adult stem cells
In a few adult tissues, e.g. **bone marrow**; only a **limited range** of cells.
:::
::::

:::: grid
::: advantages
- **Replace damaged cells** to treat disease.
- The patient's own adult stem cells are not rejected.
:::
::: disadvantages
- **Ethical objections**: obtaining embryonic stem cells destroys an embryo.
- Risk of **uncontrolled division** and tumour formation.
:::
::::
