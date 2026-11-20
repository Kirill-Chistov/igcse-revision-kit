# PDF_PIPELINE

Builds the student-facing PDF for **one top-level topic**: `notes/<Subject>/NN_<Topic>.pdf`.
There is one PDF per top-level topic in every subject. Markdown is the master copy; the PDF is
always regenerated, never hand-edited.

```
python3 tools/pdf/build_pdf.py <Subject>/NN_<Topic>
# equally accepted: subjects/<Subject>/topics/NN_<Topic>[/NN_<Subtopic>]  or  notes/<Subject>/NN_<Topic>.pdf
# a subtopic path always rebuilds its whole topic
# --keep-html    also writes the intermediate HTML next to the PDF
```

What it does:

1. finds `subjects/<Subject>/topics/NN_<Topic>/` and every written subtopic in numeric order
   (folders with no `topic.md` yet are skipped and listed);
2. renders them with `render_booklet.py` as ONE continuous document — subtopics follow each
   other without forced page breaks; bookmarks come from the headings;
3. writes `notes/<Subject>/NN_<Topic>.pdf` and prints its page count.

A topic with no subtopics keeps `topic.md` directly in `topics/NN_<Topic>/`.

**What is printed.** Page 1 starts with the qualification line and the topic title; each
subtopic starts with its title and specification points (taken from `subtitle`). Then only the
teaching content of `topic.md`. Never printed: `## Specification coverage`, `## What you must be
able to do`, any recap / self-test / answers / checklist block, and no colophon. `summary.md` and
`questions.md` are never printed.

## Where to run it

Rendering needs Python 3.10+, the packages in `requirements.txt`, headless Chromium (installed by
Playwright) and, for the intended look, the Carlito font (metric-compatible with Calibri):

```
pip install -r tools/pdf/requirements.txt
python3 -m playwright install chromium
# Carlito: Debian/Ubuntu `sudo apt install fonts-crosextra-carlito`; macOS/Windows: Calibri is
# used if installed, otherwise any sans-serif.
```

The GitHub Action in `.github/workflows/build-pdfs.yml` builds every PDF on a clean Ubuntu runner,
so you can also just push and download the result. If your AI agent runs in a sandbox without
Chromium, run the command yourself or let CI do it.

## Files

| File | Role |
| --- | --- |
| `build_pdf.py` | the only command agents run |
| `render_booklet.py` | renders all subtopics of a topic into one PDF (called by `build_pdf.py`) |
| `topic_style.css`, `page_shell.html`, `running_footer.html` | the booklet look |
| `example_topic.md`, `assets/diagram_01_demo.svg` | authoring reference showing every supported block |

## `topic.md` conventions

YAML front matter on line 1:

```
---
title: Movement and position
eyebrow: Pearson Edexcel International GCSE Physics · 4PH1 · Topic 1 Forces and motion
subtitle: >
  Specification points 1.3–1.7 — one line on what this subtopic covers.
footer: 4PH1 · 1(b) Movement and position
subject: Pearson Edexcel International GCSE Physics 4PH1, specification points 1.3–1.7
keywords: [4PH1, IGCSE Physics, ...]
repo_path: Physics_4PH1/01_Forces_and_motion/02_Movement_and_position
---
```

Every key is optional. `title` defaults to the `# H1`. Only the first subtopic's `eyebrow` is
printed (as the qualification line). `subtitle` must start `Specification points <range> —`;
only the range is printed. `footer`, `subject`, `keywords`, `repo_path` are ignored by the renderer
(the footer is `<code> · <Topic title>`).

Structure:

* `## Specification coverage` — one `Point | Section` table so agents can check coverage.
  **Not printed.**
* `## 1. Section title` — numbered teaching section. Add `— Paper 2 only` or `[P2]` to the heading
  for a Paper 2 badge.
* `## Common misunderstandings` / `## Common traps` — red **Traps** callout.
* `## Exam relevance` — amber **Exam language** callout (topic-specific wording only).

Fenced blocks (`:::` — use more colons for the outer block when nesting):

| Block | Renders as |
| --- | --- |
| `::: definition` | teal definition box |
| `::: traps` | red traps box |
| `::: exam` | amber exam-language box |
| `::: why` / `::: note \| Label` | neutral boxes |
| `::: advantages` / `::: disadvantages` | paired green/red panels |
| `::: grid` | two-column layout for the blocks inside it |
| `::: card \| Label` | bordered card |
| `::: banner \| Title \| subtitle` | full-width part banner |
| `::: pagebreak` | page break |

Also: `**Definition — Term:** text` becomes a definition box; `![alt](assets/x.svg)` followed on the
next line by `*Figure 1. caption*` becomes a figure with caption; pipe tables are styled.

## SVG diagrams

SVGs are inlined into the page and rendered by Chromium, so internal `<style>` blocks work. Keep
fonts to `Carlito, Calibri, sans-serif`, give the root `<svg>` a `viewBox`, and check every figure
in the built PDF.

## House rules the pipeline assumes

Set by `AGENTS.md` and `rules/CONTENT_RULES.md`: teach each required point
once, in its strongest representation (annotated diagram > compact table > prose); never diagram
*and* table *and* prose for the same content; no back matter.
