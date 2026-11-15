# Arrays — Questions

## Specification coverage

| Field | Value |
| --- | --- |
| Specification points | 8.2.1–8.2.3 |
| Paper | Paper 2 — Algorithms, Programming and Logic |

No past papers are stored in `me/papers/Computer_Science_0984/` yet. Marking guidance below is
**not official**; it follows the style of Cambridge mark schemes. All code answers in pseudocode.

## 1. Recall and understanding

1. Define the term *array*. **[2]**
2. Explain why a programmer would store 30 marks in an array rather than in 30 separate
   variables. **[2]**
3. Write declarations for: (a) `Temperatures`, holding 7 real values (b) `Seats`, a table of 10
   rows and 20 columns of Boolean values. **[2]**
4. `Marks` holds 12, 7, 19, 4, 15 at indexes 1–5. State the value of (a) `Marks[3]`
   (b) `Marks[Marks[2] - 4]`. **[2]**

## 2. Tracing and errors

5. State the contents of `Grid` after this code runs. **[3]**

```
FOR Row ← 1 TO 2
    FOR Col ← 1 TO 3
        Grid[Row, Col] ← Row * Col
    NEXT Col
NEXT Row
```

6. `DECLARE Scores : ARRAY[1:10] OF INTEGER` is followed by `FOR Index ← 0 TO 10` and
   `INPUT Scores[Index]`. Identify the error and correct it. **[2]**

## 3. Writing pseudocode

7. Write an algorithm to input 7 temperatures into `Temperatures` and output their average. **[4]**
8. Write an algorithm to set every element of `Seats` (question 3b) to `FALSE`. **[3]**
9. `Names[1:30]` and `Marks[1:30]` store each student's name and mark at the same index. Write an
   algorithm to output the name of every student with a mark of 80 or more. **[4]**

## Answers and marking guidance (not official)

1. A data structure holding several elements of the same data type (1) under one identifier, each
   accessed by an index (1).
2. One identifier for all the marks (1); a loop using a variable as the index can process every
   mark with a few lines of code (1).
3. (a) `DECLARE Temperatures : ARRAY[1:7] OF REAL` (1)
   (b) `DECLARE Seats : ARRAY[1:10, 1:20] OF BOOLEAN` (1). Lower bound 0 acceptable if consistent.
4. (a) 19 (b) `Marks[2]` is 7, 7 − 4 = 3, so `Marks[3]` = 19.
5. Row 1: 1, 2, 3 (1); row 2: 2, 4, 6 (1); correct row/column layout (1).
6. Index 0 is outside the bounds 1–10 (1); `FOR Index ← 1 TO 10` (1).
7. Total initialised (1); loop 1 to 7 inputting into `Temperatures[Index]` (1); totalling (1);
   average = total / 7 output (1).

```
Total ← 0.0
FOR Index ← 1 TO 7
    INPUT Temperatures[Index]
    Total ← Total + Temperatures[Index]
NEXT Index
OUTPUT "Average: ", Total / 7
```

8. Outer loop 1–10 (1); inner loop 1–20 (1); `Seats[Row, Column] ← FALSE` (1).

```
FOR Row ← 1 TO 10
    FOR Column ← 1 TO 20
        Seats[Row, Column] ← FALSE
    NEXT Column
NEXT Row
```

9. Loop 1–30 (1); test `Marks[Index] >= 80` (1); output `Names[Index]` (1); same index for both
   arrays (1).

```
FOR Index ← 1 TO 30
    IF Marks[Index] >= 80
      THEN
        OUTPUT Names[Index]
    ENDIF
NEXT Index
```
