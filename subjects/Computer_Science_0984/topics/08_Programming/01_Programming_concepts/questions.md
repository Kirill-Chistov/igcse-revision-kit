# Programming concepts — Questions

## Specification coverage

| Field | Value |
| --- | --- |
| Specification points | 8.1.1–8.1.8 |
| Paper | Paper 2 — Algorithms, Programming and Logic |

No past papers are stored in `me/papers/Computer_Science_0984/` yet. Marking guidance below is
**not official**; it follows the style of Cambridge mark schemes. All code answers in pseudocode.

## 1. Recall

1. Define the terms *variable* and *constant*. **[2]**
2. State the most suitable data type for: (a) the number of people in a room (b) a price of
   4.99 (c) whether a door is locked (d) a postcode (e) a single grade letter. **[5]**
3. State the value returned by: (a) `DIV(17, 5)` (b) `MOD(17, 5)` (c) `ROUND(3.456, 1)`
   (d) `LENGTH("Computer")` (e) `SUBSTRING("Computer", 4, 3)` (f) `UCASE("abc")`. **[6]**

## 2. Understanding

4. Explain the difference between a pre-condition loop and a post-condition loop. **[2]**
5. Explain the difference between a procedure and a function. **[2]**
6. Explain why local variables are usually used instead of global variables. **[2]**
7. A program uses the VAT rate 0.2 in several places. Explain why it should be a constant. **[2]**
8. Describe **three** ways a programmer can make a program maintainable. **[3]**

## 3. Tracing and errors

9. Complete a trace table (`Number`, `Total`, `Count`, output) for this algorithm. **[4]**

```
Total ← 0
Count ← 0
Number ← 5
WHILE Number > 0 DO
    Total ← Total + Number
    Count ← Count + 1
    Number ← Number - 2
ENDWHILE
OUTPUT Total, " ", Count
```

10. This algorithm should total 10 valid marks (0–100). Identify **three** errors and give the
    corrections. **[6]**

```
Count ← 1
REPEAT
    INPUT Mark
    IF Mark > 100
      THEN
        OUTPUT "Invalid"
    ENDIF
    Total = Total + Mark
UNTIL Count = 10
```

## 4. Writing pseudocode

11. Write an algorithm that inputs a whole number and keeps rejecting it, with a message, until it
    is between 1 and 50 inclusive. **[4]**
12. Write a function `Largest` that takes two integers and returns the larger. Show how it is
    called and the result output. **[4]**
13. Write a `CASE` statement for a menu choice `Choice` (a `CHAR`): `'A'` calls procedure
    `AddItem`, `'Q'` outputs `"Goodbye"`, anything else outputs `"Invalid choice"`. **[3]**
14. Write an algorithm that inputs a word and outputs how many times the letter e appears, in
    upper or lower case. **[5]**
15. Write an algorithm that simulates 100 rolls of a six-sided dice and outputs how many sixes
    were rolled. **[4]**

## Answers and marking guidance (not official)

1. Variable: named data store whose value can change during execution (1). Constant: named data
   store whose value cannot change during execution (1).
2. (a) INTEGER (b) REAL (c) BOOLEAN (d) STRING (e) CHAR.
3. (a) 3 (b) 2 (c) 3.5 (d) 8 (e) `"put"` (f) `"ABC"`.
4. Pre-condition tests the condition before the statements, so they may not run at all (1);
   post-condition tests after, so they always run at least once (1).
5. A function returns a value and a procedure does not (1); a function is called as part of an
   expression, a procedure with `CALL` as a complete statement (1).
6. Any two: cannot be changed accidentally by other parts of the program; same name can be reused
   in other subroutines; subroutine is self-contained so easier to test/reuse; memory used only
   while the subroutine runs.
7. The value is fixed/cannot be changed by mistake while running (1); if the rate changes it is
   edited once and every use updates (1).
8. Meaningful identifiers (for variables, constants, arrays, subroutines) (1); comments explaining
   the code (1); procedures/functions for separate tasks (1).
9. Number 5, 3, 1, −1 (1); Total 0, 5, 8, 9 (1); Count 0, 1, 2, 3 (1); output `9 3` (1).
10. Any three, 1 for error + 1 for correction: `Total` not initialised → `Total ← 0` before the
    loop; `=` used for assignment → `Total ← Total + Mark`; `Count` never changes (loop never
    ends) → `Count ← Count + 1` inside the loop; invalid marks are still added / `Mark < 0` not
    checked → add to total only in an `ELSE`, with condition `Mark < 0 OR Mark > 100`.
11. Example — 1 mark each: loop, input inside loop, message for invalid value, correct condition:

```
REPEAT
    OUTPUT "Enter a number from 1 to 50"
    INPUT Number
    IF Number < 1 OR Number > 50
      THEN
        OUTPUT "Invalid, try again"
    ENDIF
UNTIL Number >= 1 AND Number <= 50
```

12. Header with two INTEGER parameters and `RETURNS INTEGER` (1); IF comparing them (1); `RETURN`
    of the larger (1); call inside an expression/output, no `CALL` (1).

```
FUNCTION Largest(Num1 : INTEGER, Num2 : INTEGER) RETURNS INTEGER
    IF Num1 > Num2
      THEN
        RETURN Num1
      ELSE
        RETURN Num2
    ENDIF
ENDFUNCTION

OUTPUT Largest(12, 30)
```

13. `CASE OF Choice` … `ENDCASE` (1); both cases correct (1); `OTHERWISE` output (1).

```
CASE OF Choice
  'A' : CALL AddItem
  'Q' : OUTPUT "Goodbye"
  OTHERWISE OUTPUT "Invalid choice"
ENDCASE
```

14. Count initialised (1); loop 1 to `LENGTH(Word)` (1); `SUBSTRING(Word, Position, 1)` (1);
    case handled with `LCASE`/`UCASE` (1); count incremented and output after loop (1).

```
INPUT Word
Count ← 0
FOR Position ← 1 TO LENGTH(Word)
    IF LCASE(SUBSTRING(Word, Position, 1)) = "e"
      THEN
        Count ← Count + 1
    ENDIF
NEXT Position
OUTPUT Count
```

15. Counter initialised (1); loop 100 times (1); random 1–6 (1); count sixes and output (1).

```
Sixes ← 0
FOR Roll ← 1 TO 100
    Dice ← ROUND(RANDOM() * 5, 0) + 1
    IF Dice = 6
      THEN
        Sixes ← Sixes + 1
    ENDIF
NEXT Roll
OUTPUT "Sixes: ", Sixes
```
