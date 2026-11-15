# Boolean logic — Summary

Specification points 10.1–10.3 · Paper 2

## Gates (symbols: `topic.md` Figure 1)

| Gate | Output is 1 when | Outputs for AB = 00, 01, 10, 11 |
| --- | --- | --- |
| NOT (one input) | input is 0 | A = 0 → 1, A = 1 → 0 |
| AND | both inputs are 1 | 0 0 0 1 |
| OR | either or both inputs are 1 | 0 1 1 1 |
| NAND | not both inputs are 1 | 1 1 1 0 |
| NOR | both inputs are 0 | 1 0 0 0 |
| XOR (EOR) | inputs are different | 0 1 1 0 |

Bubble = NOT. Every gate except NOT has exactly two inputs. Circuits: max three inputs, one output.
Truth table: 2ⁿ rows, in order 000, 001 … 111.

## Conversions

- **Circuit → truth table:** label intermediate outputs P, Q …; one working column each.
- **Circuit → expression:** from the inputs forward, one bracket per gate:
  X = (A NAND B) XOR (B NOR C).
- **Expression → circuit:** operator outside all brackets = final gate; brackets first; every NOT
  is a NOT gate; never simplify.
- **Expression → truth table:** one working column per bracket.
- **Problem statement → expression:** one bracket per condition, joined by the linking word.
  "and" AND · "or" OR · 0-state of an input NOT · "but not both" XOR · "neither … nor" NOR ·
  "not both" NAND.
- **Truth table → expression:** one AND term per row with X = 1 (1 → input, 0 → NOT input),
  joined by OR. Three-input term = two chained AND gates.

## Traps

- OR and XOR differ only on 1, 1.
- NOT (A AND B) is NAND, not NOT A AND NOT B.
