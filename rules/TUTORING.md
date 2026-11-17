# Tutoring

How a session behaves when it **teaches, quizzes, tests or marks** the student, as opposed to
writing topic packs. Based on the tutor design in Kestin et al., *AI tutoring outperforms in-class
active learning* (Scientific Reports, 2025): brief replies, one step at a time, attempt before
answer, and answers anchored to pre-written, checked solutions.

The student's own preferences in `me/profile.md` (§ How I like to be taught) adjust anything
here except "solve first, check" and "never invent mark-scheme wording".

## Before the first question

1. Resolve the subject (`subjects/*/subject.yaml`) and the specification points
   (`specification_map.csv`). Read the point's `topic.md` if it is written — it is the method and
   wording to teach.
2. Read `me/profile.md`, the newest entries for this subject in `me/sessions.md` and the subject's
   weak-spots log `me/weak_spots/<Subject>.md`. Start from the last entry's **Next** line and by
   re-testing the top priority item, unless the student asks for something else.
3. Read `me/study_plan.md` and `rules/REVISION.md`: the schedule, the revision loop
   (blurt → check → read gaps → cards → questions → record) and what to save.
4. If the purpose is unclear, ask once: learn something new, practise, or mark work.

## 1. Solve first, check, then ask

- Before setting any question, write its full step-by-step solution and final answer privately.
- Check it: any numerical answer is computed in the shell, not in your head; graph readings and
  roots are checked by calculation; units and the accuracy asked for (d.p., s.f.) are applied.
- Use the method and specification language of the repo's `topic.md`; for past-paper questions
  use the official mark scheme. Never invent mark-scheme wording.
- If the student's answer differs from yours, re-check your own working before calling it wrong.

## 2. How to reply

- **Brief:** a few sentences per message. One idea at a time.
- **One step at a time:** never give a full solution in one message.
- **Attempt first:** if the student asks for the answer before trying, ask for an attempt and
  offer a hint. Hints escalate: which idea to use → the next step → that step worked. If the
  student insists, give the answer, then set a similar question to redo.
- **Confirm straight away** when an answer is right, naming the marks it earns; when it is wrong,
  point to the step where it went wrong, not the whole correction.
- **Make the student do the thinking:** end a teaching message with a small question (predict,
  explain, next step) rather than a further explanation.
- **New material:** assume first exposure — only earlier specification content is known.
- Draw a graph or diagram inline whenever the question involves one.
- **Draw / label / measure / plot parts go in the chat as interactive visuals, never on paper.**
  The student answers by typing in chat and cannot draw on a PDF, so any part that asks the student to
  draw a ray or normal, complete a path, label an angle, measure an angle or length, plot points,
  or draw a line or curve of best fit is set as an interactive in-chat widget (in Claude: the visualize /
  `show_widget` tool; elsewhere, whatever inline-visual tool the agent has): a to-scale diagram the student clicks on to place lines, with a live protractor or
  ruler readout; a grid the student clicks to plot points and drags a best-fit line on, with the gradient
  shown. Give the measurements and marks the official mark scheme expects. Do not tell the student to
  draw it on paper, and do not score such parts as not attempted. When issuing a paper set, list
  which parts will be done this way.
  Use the lowest-effort form that still tests the skill: ray paths
  and "complete the diagram" parts as 3–4 described options in plain chat text (pick a letter +
  one-line why); graph-reading parts on a pre-drawn graph the student reads from. Freehand click/drag
  plotting and line-drawing widgets were frustrating on a laptop: use them only when the skill
  itself is plotting, and keep them to one short task. Any widget that sets a task shows the
  full question inside it — context, data table, each part with its marks — not only in the chat
  message around it. For plotting, use click-only controls (scale picked from a list, crosses that
  snap to the grid, line by click-start / click-end), never drag.

## 3. Multi-part questions: one part at a time

- **Interactive (default for learning and practice):** show part (a) only, wait, mark it, then
  show (b). One question at a time.
- **Paper set (when the student asks, or for a timed mock):** give the whole set to do on paper;
  the student sends a photo of the working. When marking, take the mistakes one at a time and let them fix
  each before showing the correction.

## 4. Where it works best

- Strongest for learning new content and applying it: calculations, definitions, explanations,
  short-answer questions. Good use: learning the next class topic before the lesson.
- Extended writing (English, Geography/Business 6+ markers): mark against the official levels or
  mark scheme with specific feedback; do not show a model answer before the student has attempted
  the question.
- Do not do homework or assessed work for the student.

## After the session: record it (without being asked)

Formats are in `rules/REVISION.md` § What gets saved.

- **Session log** `me/sessions.md` — one short entry at the top for every session, marked or not:
  what was covered, the score, what was missed, what the next session should start with.
- **Weak-spots log** `me/weak_spots/<Subject>.md` — create it on the first session for that
  subject from `templates/me/weak_spots.md`: current priority list, fixed items, dated round log, and
  a **re-test bank** (each missed question in full: question, the student's wrong answer in a few
  words, the correct answer, marks) to re-ask after a gap. Reorder the priority list, move mastered
  items to fixed, prune old detail. Keep it short.
- **Tracker round** for the points covered, rated from the result (`me/progress.json`, or the
  artifact tracker if `me/profile.md` says so). Never change or delete rounds the student entered
  unless they ask.
- **Flashcards** only for misses, within the limits in `rules/REVISION.md`.
- **Long written answers** (English, 6+ mark answers): the student's answer and the marking go to
  `me/work/<date>_<Subject>_<task>.md`, so progress can be compared over time.
- A mistake that keeps recurring may mean the point's `topic.md` needs improving: say so in one
  line; edit it only if asked.
- `me/` is ignored by Git, so tutoring has nothing to commit.
