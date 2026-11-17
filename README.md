# 📚 IGCSE Revision Kit

**An AI tutor for your IGCSEs and GCSEs that lives in a folder on your laptop.** Download the
folder, open it in Claude, type `/setup` — and you have a tutor that knows your exact
specification, your exam dates and your target grades, tests you on real past-paper questions, and
remembers every session.

<p align="center">
  <a href="#-set-it-up-5-minutes"><b>🚀 Set it up</b></a> &nbsp;·&nbsp;
  <a href="#-commands"><b>⌨️ Commands</b></a> &nbsp;·&nbsp;
  <a href="#-subjects"><b>📘 Subjects</b></a> &nbsp;·&nbsp;
  <a href="#-just-want-the-notes"><b>📄 Just the notes</b></a>
</p>

<p align="center"><img src="docs/img/tracker_subject.png" width="600" alt="The tracker: every specification point with its revision rounds"></p>

## Why not just ask a chatbot?

A chatbot starts from zero every time and teaches "GCSE Biology" in general. This kit gives Claude
everything a real tutor has:

- **Your course, point by point.** Every specification point of each subject is mapped, with notes
  written for exactly that point — so it teaches and marks in the wording your exam board rewards,
  and never drifts off your course.
- **Tutoring rules.** One question at a time, you try before you get the answer, hints before
  solutions, every question solved and checked before it is asked.
- **A memory.** After every session it writes down what you covered, your score, what you got
  wrong and what comes next. The next session starts from there.
- **A plan and a tracker.** A weekly plan that fits the time you really have, flashcards only for
  what you missed, and a progress page for every specification point.

Everything about you stays in one private folder, `me/`, on your own computer.

## 🚀 Set it up (5 minutes)

You need the [Claude desktop app](https://claude.com/download) (or
[Claude Code](https://docs.claude.com/en/docs/claude-code/overview) in a terminal) on a plan that
includes Claude Code, and [Python 3](https://www.python.org/downloads/) for the tracker.

1. **Download the folder.** Green **Code** button at the top of this page → **Download ZIP**, then
   unzip it somewhere it can stay (e.g. Documents). Or `git clone` this repository.
2. **Open it in Claude as a project.** In the Claude desktop app, open the **Code** tab and choose
   the `igcse-revision-kit` folder. (Terminal: `cd igcse-revision-kit`, then `claude`.)
3. **Type `/setup`.** It asks, a question or two at a time:
   - which subjects you take, and your options (tier, set texts, case studies…)
   - when your mocks and exams are
   - your target grade in each subject, and where you are now
   - which days you can revise and for how long
   - how you like to be taught

That's it. From then on just open the folder in Claude and say what you want — "let's revise",
"test me on waves", "what should I do today?" — or use a command.

## ⌨️ Commands

| Command | What it does |
| --- | --- |
| **`/setup`** | Sets up your tutor: subjects, options, exam dates, target grades, time, preferences. Run it again any time something changes. |
| **`/plan`** | Builds a weekly revision plan that fits your time, your school tests and your target grades. |
| **`/revise Biology enzymes`** | A full revision session (~60 min): write what you remember → see your gaps → read only those → questions → saved. Also teaches a topic you haven't learned yet. |
| **`/test Physics topic 3`** | You revised on your own; this checks it stuck. Past-paper questions, marked one by one against the mark scheme. |
| **`/progress`** | What to do today, how each subject is going against your target, flashcards due. |
| **`/make-topic Chemistry "topic 3"`** | Writes (or fixes, or shortens) the revision notes for a topic and builds its PDF. |
| **`/add-subject AQA 8461`** | Adds a subject or exam board the kit doesn't have yet, from its official specification. |

You never have to remember these — plain words work too.

## 🧠 What it remembers

`/setup` creates a private `me/` folder. Every session reads it first and updates it at the end,
without being asked:

| File | Holds |
| --- | --- |
| `me/profile.md` | your subjects, options, target grades, how you like to be taught |
| `me/study_plan.md` | exam dates, your weekly plan, what to revise next |
| `me/sessions.md` | a log of every session: what you covered, your score, what comes next |
| `me/weak_spots/` | the questions you got wrong, kept to re-test you later |
| `me/progress.json`, `me/flashcards.json` | your rating for every specification point, and your flashcards |
| `me/papers/` | past papers you download ([where to get them](PAPERS.md)) — the tutor finds questions in them |

**See your progress:** run `python3 tools/tracker/serve.py` and open <http://localhost:8765>, or
ask Claude to keep the tracker as a private page you can open on your phone
([details](tools/tracker/README.md)).

`me/` is never uploaded anywhere. To keep it when you update the kit, copy your `me/` folder into
the new download.

## 📘 Subjects

| Subject | Exam board · code | Notes | Past papers |
| --- | --- | --- | --- |
| Biology | Pearson Edexcel International GCSE · **4BI1** | [5 topics](notes/README.md#biology) | [where to get them](PAPERS.md#biology) |
| Chemistry | Pearson Edexcel International GCSE · **4CH1** | [4 topics](notes/README.md#chemistry) | [where to get them](PAPERS.md#chemistry) |
| Physics | Pearson Edexcel International GCSE · **4PH1** | [8 topics](notes/README.md#physics) | [where to get them](PAPERS.md#physics) |
| Business | Pearson Edexcel International GCSE · **4BS1** | [5 topics](notes/README.md#business) | [where to get them](PAPERS.md#business) |
| Computer Science | Cambridge IGCSE (9–1) · **0984** | [10 topics](notes/README.md#computer-science) | [where to get them](PAPERS.md#computer-science) |
| Geography | Cambridge IGCSE (9–1) · **0976** | [10 topics + a poster](notes/README.md#geography) | [where to get them](PAPERS.md#geography) |
| Mathematics A | Pearson Edexcel International GCSE · **4MA1** | coming later | [where to get them](PAPERS.md#mathematics-a) |
| English Language | Cambridge IGCSE (9–1) · **0990** | coming later | [where to get them](PAPERS.md#english-first-language) |
| English Literature | Cambridge IGCSE (9–1) · **0992** | coming later | [where to get them](PAPERS.md#english-literature) |
| Portuguese | Pearson Edexcel GCSE · **1PG0** | coming later | [where to get them](PAPERS.md#portuguese) |
| Spanish | Pearson Edexcel International GCSE · **4SP1** | coming later | [where to get them](PAPERS.md#spanish) |

"Coming later" subjects already have their specification mapped, so the tutor can test and track
them; `/make-topic` writes the notes. **Check the code** — the same subject has different exams on
different boards (`4PH1` is not `0625`); it is on your exam timetable and on the front of any past
paper. Different board or subject? Use `/add-subject`.

## 📄 Just want the notes?

The notes work without any AI: one PDF per topic, every point you can be examined on, a diagram
wherever something has a shape, and nothing extra.

- **One topic:** open [the notes list](notes/README.md) and click a topic.
- **A whole subject:** download its zip from the [latest release](../../releases/latest).

<p align="center"><img src="docs/img/notes_sample.png" width="380" alt="A page of the Physics Waves notes"></p>

## No Claude?

- **Another coding agent** (Codex, Cursor, Gemini CLI): open the folder in it — it reads the same
  instructions through [`AGENTS.md`](AGENTS.md).
- **Any AI chatbot** (ChatGPT, Gemini…): attach one topic PDF, then paste in
  [`docs/AI_tutor_prompt.txt`](docs/AI_tutor_prompt.txt) (edit the "MY COURSES" lines first). You
  get the same tutoring style, but it has no memory: at the end it gives you a session note to
  paste into your next chat. The full kit does all of that for you.

## Good to know

- **The specification is the boss.** Notes are written by a student and AI agents and checked
  against the specification, but mistakes happen — if something disagrees with your
  specification or a mark scheme, trust those, and please [report it](../../issues/new/choose).
- **Geography case studies** are chosen by each school. The notes use one class's examples; if yours
  are different, tell `/setup` and learn yours ([why](subjects/Geography_0976/CASE_STUDY_TRACKER.md)).
- **Age:** Claude's own apps require users to be 18 or over. If you're younger, set it up and use
  it with a parent or teacher, or use the notes and the chatbot prompt with a tool whose terms
  allow your age.
- **Privacy:** nothing about you is ever written outside `me/`, and `me/` is never uploaded.

## 🤝 Help improve it

Fix a mistake, write a missing topic, or add your own exam board's subject — see
[CONTRIBUTING.md](CONTRIBUTING.md). How the notes and the tutor are built is in
[docs/HOW_IT_WORKS.md](docs/HOW_IT_WORKS.md).

## Licence

Made by **Kirill Chistov** and contributors. Notes, diagrams and rules:
[CC BY-NC-SA 4.0](LICENSE-CONTENT) — free to use, share and adapt, not to sell. Code:
[MIT](LICENSE). Not affiliated with Pearson, Cambridge or any exam board.
