# Workflow — making or editing a topic

The ordered process for creating, editing, compressing or auditing a topic (`/make-topic`).
`CLAUDE.md` holds the rules; this file holds the steps.

## The pipeline

```
subjects/<Subject>/Specification.pdf   official specification — authority on WHAT is assessable
   -> specification.md                 AI-readable index of the points
   -> specification_map.csv            spec point -> source folder (content_path)
   -> topic.md                         canonical learning source, one per subtopic
   -> summary.md, questions.md         markdown-only revision and practice
   -> notes/<Subject>/NN_<Topic>.pdf   ONE PDF per top-level topic, built from its topic.md files
   -> me/papers/<Subject>/ practice    feeds back into topic.md / questions.md
```

`content_path` in the map reads `<Subject>/NN_<Topic>/NN_<Subtopic>`; the source folder is
`subjects/<Subject>/topics/NN_<Topic>/NN_<Subtopic>/`.

## 1. Resolve the target

1. Resolve the subject from `subjects/*/subject.yaml` (name, code, aliases).
2. List `subjects/<Subject>/topics/` and check `specification_map.csv`.
   `Topic N` means the whole top-level `NN_<Topic>` folder; a named subtopic means that folder.
3. Ask one short question only if more than one target is still plausible.

## 2. Read before writing

- `rules/CONTENT_RULES.md`, `rules/STYLE_GUIDE.md`, `rules/SOURCE_POLICY.md`
- `me/profile.md` — tier, route, set texts, case studies, programming language for this subject
- `subjects/<Subject>/Specification.pdf` for the exact wording (if missing, run
  `python3 tools/fetch_specs.py <Subject>`; if that fails, use `specification.md` and say so)
- `specification.md`, `specification_map.csv`, `coverage_checklist.md`, `AGENT.md`,
  `SUBJECT_RULES.md`, `QA_CHECKLIST.md`, and `CONTENT_STYLE.md`, `SOURCE_GUIDE.md`, trackers where
  they exist — all in `subjects/<Subject>/`
- the existing files in the target source folder and the current topic PDF
- `me/sources/<Subject>/` if the topic needs school material (case studies, set texts)

A topic that cannot name its specification points by official number is not ready to be written.

## 3. Check dependencies

Case studies, set texts, programming language, tier, practicals, school sources: if `me/profile.md`
or a subject tracker covers it, obey it; if something required is missing, follow the subject's
placeholder policy or ask. Never invent it.

## 4. Plan the visuals

Before writing, list every process, mechanism, sequence, cycle, structure, graph shape and
spatial pattern in the mapped points and choose diagram / graph / photo / table / prose for each
(`CLAUDE.md` § Visual rule). Existing packs: note where a table or bullet list is doing a
diagram's job.

## 5. Write or edit

- Read the subject's `CONTENT_STYLE.md` for elements that subject always needs (Business:
  advantages and disadvantages for every method, choice or policy).
- Absent pack → create `topic.md`, `summary.md`, `questions.md` from `templates/`.
- Existing pack → edit/compress; keep strong content and visuals.
- `topic.md` starts with YAML front matter (`tools/pdf/README.md`); `subtitle` starts
  `Specification points <range> —`.
- Diagrams are SVG in `assets/`, drawn for this repository. A photo is used only if openly
  licensed; record origin, author and licence in `assets/SOURCES.md`.
- No objective lists, introductions or "why it matters" padding. No recap, self-test, answers or
  checklist sections anywhere except the practice in `questions.md`.

## 6. Mandatory lean pass

Re-read every file section by section and cut whatever the student could lose without losing marks
or understanding (full wording in `CLAUDE.md`). `summary.md` must be materially shorter than
`topic.md`.

## 7. Build and inspect

```
python3 tools/pdf/build_pdf.py <Subject>/NN_<Topic>
```

Builds the whole topic PDF from every written subtopic. Needs Chromium (`tools/pdf/README.md`). If
the agent's environment cannot render, say so: the student can run the command, or push and let
the GitHub Action build it. When it does render, look at every affected page and fix genuine
render problems. The PDF is stale the moment a `topic.md` changes — rebuild, never patch.
Then run `python3 tools/build_index.py` so the notes index and catalogue list it.

## 8. QA and trackers

1. Run the subject's `QA_CHECKLIST.md`.
2. Check every mapped point and sub-bullet against the pack.
3. Tick the covered points in `coverage_checklist.md` and set `content_status` for those rows in
   `specification_map.csv` — only those rows.

## 9. Commit

Commit only the paths this session touched, with a one-line message (`CLAUDE.md` § Git).

## 10. Report and stop

Report: subject/spec code, source folder(s), topic PDF path and page count, spec points covered,
files changed, the commit made, any unresolved dependency. If the work is good enough to share,
suggest opening a pull request (see `CONTRIBUTING.md`). Do not start the next topic.
