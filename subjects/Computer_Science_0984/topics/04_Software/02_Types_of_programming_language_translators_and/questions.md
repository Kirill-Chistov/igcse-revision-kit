# Types of programming language, translators and IDEs — Questions

Specification points 4.2.1–4.2.5 · Paper 1. Marks in brackets.

There is no local Cambridge past-paper bank for this subject yet.

> **AI-generated practice written for this repository.** The marking guidance is not an official
> Cambridge mark scheme.

## Questions

1. Explain what is meant by a high-level language. (2)
2. Give **two** advantages of writing a program in a high-level language rather than a low-level
   language. (2)
3. A programmer is writing a device driver for a new graphics card. Explain why they might choose a
   low-level language. (2)
4. State what is meant by a mnemonic in assembly language. (1)
5. Explain why an assembler is needed. (2)
6. Describe how a compiler translates a high-level program and how it reports errors. (4)
7. Describe how an interpreter translates a high-level program and how it reports errors. (4)
8. Give **one** advantage and **one** disadvantage of using an interpreter. (2)
9. A company has finished writing a game and will sell it to customers. Explain why it should use a
   compiler to translate the final version. (3)
10. Explain why an interpreter is often used while a program is being developed. (2)
11. State **three** functions of an IDE and explain how each helps a programmer. (6)
12. True or false: (a) machine code must be translated before it can run; (b) an interpreter produces
    an executable file; (c) low-level languages are machine dependent. (3)

## Marking guidance

1. Uses English-like statements / easy for humans to read (1); independent of hardware / must be
   translated into machine code (1).
2. Any two: easier to read and write; easier to debug; machine independent / portable (1 each).
3. Can directly manipulate the hardware / registers / memory addresses (1); code can run faster /
   use less memory (1).
4. A short code that represents a machine code instruction, e.g. LDA (1).
5. The processor can only run machine code (1); the assembler translates assembly language into
   machine code (1).
6. Translates the whole program at once (1) before it is executed (1); produces an executable file (1);
   if errors are found, gives an error report for the whole code / lists all errors (1).
7. Translates and executes one line at a time (1); no executable file (1); stops execution when an
   error is found (1); reports that error / lines after it are not run (1).
8. Advantage: easier to find errors / can test straight away after a change (1). Disadvantage: runs
   more slowly / interpreter needed every time the program runs / source code must be given out (1).
9. Produces an executable file (1) that runs without the compiler (1); runs faster / source code is
   not given to customers (1).
10. Stops at the line with an error, so errors are easy to find (1); changes can be tested
    immediately without recompiling the whole program (1).
11. Any three functions (1) each with how it helps (1), e.g. code editor — write and edit code
    without a separate editor; error diagnostics — highlights and reports errors so they are fixed
    quickly; auto-completion — suggests keywords/identifiers, saving time and avoiding spelling
    errors; prettyprint — colour-coding/indentation makes code easier to read; run-time environment
    — run and test the program in the IDE; translators — translate code without leaving the IDE;
    auto-correction — corrects common mistakes.
12. (a) false (b) false (c) true (1 each).
