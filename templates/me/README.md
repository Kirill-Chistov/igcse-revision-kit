# `me/` — your private folder

`/setup` copies these templates into `me/` at the top of the repository. Git ignores `me/`, so
nothing in it is ever committed or pushed — your profile, plan, marks, past papers and school
material stay on your computer.

| Path | What |
| --- | --- |
| `profile.md` | subjects and options, dates, time, how you like to be taught |
| `study_plan.md` | weekly shape and backlog (`/plan`) |
| `progress.json` | tracker ratings (format: `rules/REVISION.md`) |
| `flashcards.json` | flashcard decks |
| `weak_spots/<Subject>.md` | priorities and the re-test bank |
| `work/` | marked long answers |
| `papers/<Subject>/` | past papers and mark schemes you downloaded |
| `sources/<Subject>/` | school material: class notes, case-study documents, textbook pages |

**Backing up:** to keep `me/` safe across computers, make it its own **private** Git repository
(`cd me && git init`) and push it to a private remote. Never remove `me/` from the main
repository's `.gitignore`.
