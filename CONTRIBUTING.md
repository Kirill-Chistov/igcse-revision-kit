# Contributing

Thanks for helping. The kit gets better every time a student fixes a mistake, adds a subject or
writes a topic the next person can revise from.

## Ways to help

| | How |
| --- | --- |
| Report a mistake | Open an issue ("Notes error"): subject, topic PDF, page, specification point, what's wrong and the source that says so (spec, mark scheme). |
| Fix a topic | Edit its `topic.md` (and `summary.md` / `questions.md` if affected), rebuild the PDF, open a pull request. |
| Write a missing topic | `/make-topic <subject> <topic>` with your agent, review the result yourself, open a PR. |
| Add a subject | `/add-subject <board> <code>` → specification map and empty topic folders. A PR with just the map is already useful. |
| Improve the tools | Tracker, PDF pipeline, checks, skills — PRs welcome; keep `tools/` dependency-light. |

## Rules for pull requests

1. **Nothing personal.** Never commit `me/`, your name in notes, marks, or school details. Git
   ignores `me/`; check `git status` anyway.
2. **Nothing copyrighted.** No textbook pages, past-paper questions, mark schemes, examiner reports,
   school documents or specification PDFs. Paraphrase; draw your own diagrams; photos only if
   openly licensed and recorded in `assets/SOURCES.md` (file, what it shows, URL, author, licence).
3. **Specification first.** Every note names the official point numbers it covers. Content not in
   the specification is cut, not labelled "extra". The rules are in `CLAUDE.md` and `rules/`.
4. **One topic per PR**, with the rebuilt PDF. If you can't build PDFs locally, say so — CI builds
   them, and a maintainer will commit the result.
5. **Run the checks**: `python3 tools/check_repo.py` must pass.
6. **Case studies, set texts, programming language** are school choices. Shared notes either use
   the example a class actually studied (say which) or keep the placeholder; never invent one.

AI-written content is welcome — that's how most of the kit was made — but you are responsible for
reading it before you submit. Reviewers will check it against the specification.

## Setting up

```bash
pip install -r tools/pdf/requirements.txt
python3 -m playwright install chromium
python3 tools/pdf/build_pdf.py Physics_4PH1/03_Waves     # build one topic PDF
python3 tools/build_index.py                             # refresh notes/README.md, PAPERS.md, catalog
python3 tools/check_repo.py                              # run the checks
```

## Code of conduct

Be kind and assume good faith: contributors are mostly students. Feedback on content cites the
specification or a mark scheme, not opinion.
