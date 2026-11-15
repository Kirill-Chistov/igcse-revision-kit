# Algorithm design and problem-solving — summary

Cambridge IGCSE (9–1) Computer Science 0984 · Topic 7 · Paper 2 · specification points 7.1–7.9

## Life cycle (7.1)

- **Analysis:** identify the problem and requirements; **abstraction** (keep only needed detail);
  **decomposition** (break into smaller parts).
- **Design:** decomposition into sub-systems; structure diagrams, flowcharts, pseudocode.
- **Coding:** write code; **iterative testing** (test each part, amend, re-test).
- **Testing:** run the whole program with test data.

## Decomposition and design (7.2)

- Systems → sub-systems → further sub-systems (top-down design).
- Component parts: **inputs, processes, outputs, storage**.
- Structure diagram = hierarchy of sub-systems. Flowchart symbols: terminator, input/output,
  process, decision (two labelled exits), subroutine, flow line.

## Purpose of an algorithm (7.3)

State **what it does overall**, then **describe its processes** in order.

## Standard methods (7.4)

- Totalling `Total ← Total + Value`; counting `Count ← Count + 1`; both start at 0.
- Max/min: start at the first value (or lowest/highest possible); compare each value.
- Average: total ÷ number of values, **after** the loop.
- Linear search: check each item in turn until found (flag) or end of list.
- Bubble sort: compare adjacent pairs, swap if out of order; repeat passes until no swaps.

## Validation and verification (7.5)

- **Validation** = data is *reasonable*: range, length, type, presence, format, check digit.
  Written as a REPEAT … UNTIL loop with an error message.
- **Verification** = data *entered accurately*: visual check, double entry check.

## Test data (7.6)

Normal (accept) · abnormal (reject) · extreme (largest/smallest accepted) · boundary (largest/smallest
accepted **and** the rejected value next to it). For 0–100: extreme 0, 100; boundary −1/0, 100/101.

## Trace tables, errors, writing (7.7–7.9)

- Trace table: a column per variable + OUTPUT; record each change, every output and prompt.
- Errors: initial values, loop limits, `<`/`>` reversed, `Total ← Mark`, statement in/out of loop.
  Give line, error, correction.
- Write precisely (`Mark > 50`). Pseudocode everywhere; program code (Python/VB/Java) only in the
  15-mark scenario question.
