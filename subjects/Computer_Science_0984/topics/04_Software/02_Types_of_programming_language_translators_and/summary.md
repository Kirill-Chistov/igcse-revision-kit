# Types of programming language, translators and IDEs — Summary

Specification points 4.2.1–4.2.5 · Paper 1

**High-level language** — English-like, hardware independent, must be translated (Python, Java).
**Low-level language** — tied to one processor: machine code or assembly language.

| | High-level | Low-level |
| --- | --- | --- |
| Reading/writing | + easy | – hard |
| Debugging | + easier | – harder |
| Machine independence | + yes | – no |
| Direct hardware manipulation | – no | + yes |

**Assembly language** uses **mnemonics** (LDA, ADD, STO); an **assembler** translates it into machine code.

**Compiler** — whole program at once → executable file; error report for the whole code.
**Interpreter** — translate and execute line by line; stops at the first error; no executable.

- Compiler: + fast executable, runs without compiler, source hidden; – recompile after every change.
- Interpreter: + errors easy to find, test straight away; – slower, interpreter always needed.
- Interpreter while developing; compiler for the final program.

**IDE functions:** code editor · run-time environment · translators · error diagnostics ·
auto-completion · auto-correction · prettyprint.
