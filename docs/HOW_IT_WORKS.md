# How it works

## The notes

```
official specification ──► specification_map.csv ──► topic.md per subtopic ──► notes/<Subject>/NN_<Topic>.pdf
   (what is assessable)       (every point, by number)    (markdown + SVG diagrams)     (one PDF per topic)
```

The rule is *bare minimum, but still enough to fully understand the specification and get top
marks*:

- every specification point is covered at the depth its command word asks for (*state* ≠ *explain*
  ≠ *evaluate*);
- anything not in the specification is cut, not labelled "extra";
- every process, cycle or structure gets a diagram, and the diagram replaces the prose;
- every run ends with a separate pass that asks, block by block, "would the student lose marks
  without this?".

The full rules an agent follows are in [`AGENTS.md`](../AGENTS.md) and [`rules/`](../rules). The PDFs
are built from the markdown by [`tools/pdf/build_pdf.py`](../tools/pdf/README.md) (headless
Chromium); they are never edited by hand.

## The tutor

Tutoring follows Kestin et al., *AI tutoring outperforms in-class active learning* (Scientific
Reports, 2025): brief replies, one step at a time, an attempt before any answer, and every
question solved and checked by the tutor before it is asked. Details in
[`rules/TUTORING.md`](../rules/TUTORING.md); the revision loop, flashcard limits and data formats are
in [`rules/REVISION.md`](../rules/REVISION.md).

## Repository map

| Path | What |
| --- | --- |
| `notes/` | the PDFs — [index](../notes/README.md) |
| `PAPERS.md` | where to download each subject's past papers |
| `subjects/<Subject>/` | specification map, subject rules, and the markdown sources in `topics/` |
| `rules/` | how notes are written and how tutoring works |
| `AGENTS.md` | the rules every AI follows (`CLAUDE.md`, `GEMINI.md` point to it) |
| `commands/` | the commands: setup, plan, revise, test, progress, make-topic, add-subject |
| `.claude/` `.cursor/` `.gemini/` `.github/prompts/` | generated pointers so the commands appear in each tool's `/` menu (`tools/sync_commands.py`) |
| `tools/` | PDF builder, tracker, checks, spec downloader, index builder |
| `templates/` | templates for notes and for the private `me/` folder |
| `docs/catalog.json` | every subject → topic → subtopic → PDF, machine-readable (for a future website) |
| `me/` | *your* private folder — created by `/setup`, never committed |

## Generated files

`notes/README.md`, `PAPERS.md` and `docs/catalog.json` are generated from the repository by
`python3 tools/build_index.py`. Run it after adding a PDF or changing a `subject.yaml`; CI fails if
they are out of date.
