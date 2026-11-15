# File handling — Questions

## Specification coverage

| Field | Value |
| --- | --- |
| Specification points | 8.3.1–8.3.2 |
| Paper | Paper 2 — Algorithms, Programming and Logic |

No past papers are stored in `me/papers/Computer_Science_0984/` yet. Marking guidance below is
**not official**; it follows the style of Cambridge mark schemes. All code answers in pseudocode.

## 1. Recall and understanding

1. Explain why a program stores data in a file. **[2]**
2. State what happens to the data already in a file when it is opened `FOR WRITE`. **[1]**
3. State why a file should be closed before it is opened again in a different mode. **[1]**

## 2. Errors

4. Identify **three** errors in this algorithm, which should read a score from `Data.txt`. **[3]**

```
OPENFILE "Data.txt" FOR READ
WRITEFILE "Data.txt", Score
READFILE Score, "Data.txt"
```

## 3. Writing pseudocode

5. Write an algorithm to store the value of `Username` in the file `users.txt`. **[3]**
6. Write an algorithm to read the first line of `story.txt` and output it with its length. **[4]**
7. The array `Scores[1:10]` holds 10 integers. Write an algorithm that saves them to
   `scores.txt`, then reads them back from the file and outputs their total. **[6]**

## Answers and marking guidance (not official)

1. Data in variables/RAM is lost when the program closes (1); a file stores it permanently so it
   can be used again later / by another program / on another computer without re-entering (1).
2. It is lost — a new, empty file is created.
3. A file can be open in only one mode at a time.
4. `WRITEFILE` used on a file opened for reading — should be `READFILE` (or remove) (1);
   `READFILE` arguments in the wrong order — `READFILE "Data.txt", Score` (1); file not closed —
   add `CLOSEFILE "Data.txt"` (1).
5. Open `FOR WRITE` (1); `WRITEFILE "users.txt", Username` (1); `CLOSEFILE` (1).
6. Open `FOR READ` (1); `READFILE` into a STRING variable (1); output line and `LENGTH` (1); close
   (1).

```
DECLARE LineOfText : STRING
OPENFILE "story.txt" FOR READ
READFILE "story.txt", LineOfText
OUTPUT LineOfText, " (", LENGTH(LineOfText), " characters)"
CLOSEFILE "story.txt"
```

7. Open for write (1); loop writing each element (1); close then reopen for read (1); loop reading
   each item (1); totalling (1); output total after closing/after loop (1).

```
OPENFILE "scores.txt" FOR WRITE
FOR Index ← 1 TO 10
    WRITEFILE "scores.txt", Scores[Index]
NEXT Index
CLOSEFILE "scores.txt"

Total ← 0
OPENFILE "scores.txt" FOR READ
FOR Index ← 1 TO 10
    READFILE "scores.txt", Score
    Total ← Total + Score
NEXT Index
CLOSEFILE "scores.txt"
OUTPUT "Total: ", Total
```
