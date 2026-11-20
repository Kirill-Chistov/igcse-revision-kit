# Changelog

## v0.3.0 — 2026-11
Works with any AI, not just Claude. The rules moved from `CLAUDE.md` to `AGENTS.md` (the
cross-tool standard; `CLAUDE.md` and `GEMINI.md` now just import it). The commands moved from
`.claude/skills/` to plain markdown in `commands/`, and `tools/sync_commands.py` puts them in the
`/` menu of Claude Code, Cursor, Gemini CLI and GitHub Copilot; Codex and chat apps run them from
`AGENTS.md`. Chat apps that can't save files hand the session notes back as text to paste into
`me/`. README redesigned: banner, per-tool setup table, revision-loop diagram.

## v0.2.0 — 2026-11
The kit is now presented as what it is: a Claude tutor set up in a folder. `/setup` asks for exam
dates and target grades; every session is logged in `me/sessions.md` and the next one starts from
it; README rewritten around the setup; the paste-in prompt for other chatbots is kept as
`docs/AI_tutor_prompt.txt`.

## v0.1.0 — 2026-11
First public release: 42 topic PDFs across six subjects, five more subjects mapped, the seven
skills, the tracker (local + artifact), and CI.
