# AGENTS.md

This repository's agent instructions are in **[`CLAUDE.md`](CLAUDE.md)** — read it first; it is the
canonical rule set for any AI agent (Claude Code, Codex, Cursor, Gemini CLI, …).

The workflows (`/setup`, `/make-topic`, `/revise`, `/test`, `/plan`, `/progress`,
`/add-subject`) are plain markdown in `.claude/skills/<name>/SKILL.md`. If your agent does not
support slash commands, read the matching `SKILL.md` and follow it when the user asks for that
workflow in plain words.
