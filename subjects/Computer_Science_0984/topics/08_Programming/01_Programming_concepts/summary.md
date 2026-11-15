# Programming concepts — Summary

## Specification coverage

| Field | Value |
| --- | --- |
| Specification points | 8.1.1–8.1.8 |
| Paper | Paper 2 — Algorithms, Programming and Logic |

## Essentials

- **Variable** = named store, value can change. **Constant** = named store, value cannot change;
  `CONSTANT Rate ← 0.2` (literal only). Constants: easier to read; change in one place.
- `DECLARE Name : TYPE`; assignment `←`. Types: `INTEGER`, `REAL` (`4.0`), `CHAR` (`'x'`),
  `STRING` (`"hi"`), `BOOLEAN`. Phone numbers → `STRING`.
- `OUTPUT` a prompt, then `INPUT Variable`; `OUTPUT "A", X` joins values with commas.
- Operators: `+ - * / ^ MOD DIV`; `= < <= > >= <>`; `AND OR NOT`. `7 / 2` = 3.5,
  `DIV(7, 2)` = 3, `MOD(7, 2)` = 1.
- **Sequence** = statements run in written order. **Selection** = condition chooses the path
  (`IF … THEN … ELSE … ENDIF`; `CASE OF … OTHERWISE … ENDCASE` for single values of one variable).
- **Iteration**: `FOR … NEXT` fixed count · `WHILE … DO … ENDWHILE` tests first, may run 0 times ·
  `REPEAT … UNTIL` tests last, runs at least once, stops when TRUE.
- **Totalling** `Total ← Total + X`; **counting** `Count ← Count + 1`; set both to 0 before the loop.
- Strings: `LENGTH`, `SUBSTRING(S, Start, Len)`, `UCASE`, `LCASE`; positions usually from 1.
- **Nesting** = selection/iteration inside another; at most 3 levels to write.
- **Procedure** = named task, `CALL Name(Args)`. **Function** = returns one value with `RETURN`,
  used in an expression, no `CALL`. **Parameter** = variable in the header receiving an argument;
  up to 3.
- **Global** = declared in main program, usable anywhere. **Local** = declared in a subroutine,
  usable only there (safer, reusable names).
- **Library routines** = pre-written, pre-tested: `MOD`, `DIV`, `ROUND(X, Places)`, `RANDOM()`
  (0–1). Dice: `ROUND(RANDOM() * 5, 0) + 1`.
- **Maintainable**: meaningful identifiers, comments (`//`), procedures and functions.
