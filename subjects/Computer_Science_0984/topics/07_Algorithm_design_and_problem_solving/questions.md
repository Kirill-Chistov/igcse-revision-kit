# Algorithm design and problem-solving — practice questions

Cambridge IGCSE (9–1) Computer Science 0984 · Topic 7 · Paper 2 · specification points 7.1–7.9

Marking guidance below is written for this repository and is **not** an official Cambridge mark
scheme. No 0984 past papers are stored yet (`me/papers/Computer_Science_0984/` does not exist);
add real questions here once they are. Write every answer in pseudocode, not program code.

## Questions

**1** (7.1) Name the stage of the program development life cycle in which each task is done:
(a) drawing a structure diagram; (b) identifying the requirements; (c) testing a module as soon
as it is written; (d) running the finished program with normal, abnormal and boundary data. [4]

**2** (7.1) Define *abstraction* and *decomposition*. [2]

**3** (7.2) A smart thermostat keeps a room at a temperature chosen by the user. Decompose the
system into its inputs, processes, outputs and storage. [4]

**4** (7.2) Draw a structure diagram for a quiz program that asks 10 questions, marks each answer,
keeps a score and displays the final score. [3]

**5** (7.3, 7.7) Complete a trace table for this algorithm using the test data 4, −2, 6, 0, then
state its purpose. [6]

```
Count ← 0
Total ← 0
REPEAT
    OUTPUT "Enter value"
    INPUT Value
    IF Value > 0
      THEN
        Total ← Total + Value
        Count ← Count + 1
    ENDIF
UNTIL Value = 0
OUTPUT Total / Count
```

**6** (7.4) Show the list after each pass when a bubble sort puts 7, 3, 9, 2 into ascending order.
Explain how the algorithm knows it has finished. [4]

**7** (7.4) Describe how a linear search finds a value in a list. [3]

**8** (7.5) Name a suitable validation check for each input and give a reason:
(a) a percentage; (b) a product code of the form AB1234; (c) a surname that must be entered;
(d) a 13-digit barcode. [4]

**9** (7.5) Write pseudocode that makes the user enter a password of 8 to 12 characters inclusive,
outputting an error message and asking again until it is valid. [4]

**10** (7.5) Explain why data that has passed validation may still need verification, and describe
a double entry check. [3]

**11** (7.6) A program accepts a whole-number age from 11 to 16 inclusive. Give one example each of
normal, abnormal and extreme test data, and a pair of boundary data, with the expected result. [5]

**12** (7.8) This algorithm should count how many of 20 daily temperatures are above 30. Identify
three errors and give corrections. [6]

```
01  Count ← 1
02  FOR Day ← 1 TO 19
03      INPUT Temp
04      IF Temp >= 30
05        THEN
06          Count ← Count + 1
07      ENDIF
08  NEXT Day
09  OUTPUT Count
```

**13** (7.9) Draw a flowchart for the algorithm in question 12 (corrected). [5]

**14** (7.9) The array `Reading[1:7]` holds seven temperatures. Write pseudocode to output the
highest, the lowest and the average reading, and how many readings are below 0. [7]

**15** (7.9) Amend the bubble sort in `topic.md` section 5 so that it sorts into descending order.
[1]

## Marking guidance (not official)

**1** (a) design (b) analysis (c) coding — iterative testing (d) testing.

**2** Abstraction: keeping only the details needed to solve the problem and removing the rest.
Decomposition: breaking a problem into smaller parts that are easier to solve.

**3** Inputs: temperature from a sensor, temperature chosen by the user. Processes: compare the
reading with the chosen temperature; decide whether to switch heating on or off. Outputs: signal
to the heater; current temperature on a display. Storage: the chosen temperature (and any
schedule).

**4** Top box "Quiz"; below it e.g. "Ask question", "Mark answer", "Update score", "Display
score"; at least one box broken down further (e.g. "Mark answer" → "Input answer", "Compare with
correct answer"). 1 mark hierarchy, 1 mark sensible sub-systems, 1 mark a second level.

**5**

| Count | Total | Value | OUTPUT |
| --- | --- | --- | --- |
| 0 | 0 |  |  |
| 1 | 4 | 4 | Enter value |
|  |  | −2 | Enter value |
| 2 | 10 | 6 | Enter value |
|  |  | 0 | Enter value |
|  |  |  | 5 |

Purpose: inputs numbers until 0 is entered and outputs the average (mean) of the positive numbers.

**6** Pass 1: 3, 7, 2, 9. Pass 2: 3, 2, 7, 9. Pass 3: 2, 3, 7, 9. It stops when a pass makes no
swaps (flag still FALSE) or when there is only one item left to compare.

**7** Start at the first item; compare it with the value searched for; if not equal move to the
next item; stop when a match is found (set a flag) or the end of the list is reached; output the
position or "not found".

**8** (a) range check, 0 to 100 (b) format check, two letters then four digits (c) presence check,
must not be blank (d) check digit, detects mistyped or swapped digits (length check also
acceptable for (b) or (d)).

**9**

```
REPEAT
    OUTPUT "Enter a password of 8 to 12 characters"
    INPUT Password
    IF LENGTH(Password) < 8 OR LENGTH(Password) > 12
      THEN
        OUTPUT "Invalid length, please re-enter"
    ENDIF
UNTIL LENGTH(Password) >= 8 AND LENGTH(Password) <= 12
```

Loop until valid (1), input inside loop (1), correct condition with `LENGTH` and both limits (1),
error message (1).

**10** Validation only checks that data is reasonable; a sensible value can still be typed wrongly
(e.g. 56 instead of 65). Double entry: the data is entered twice, the computer compares the two
and asks for re-entry if they differ.

**11** Normal: 13, accepted. Abnormal: 25 (or −3, "twelve"), rejected. Extreme: 11 or 16, accepted.
Boundary: 10 rejected and 11 accepted (or 16 accepted and 17 rejected).

**12** Line 01: `Count ← 0`. Line 02: `FOR Day ← 1 TO 20`. Line 04: `IF Temp > 30`.
1 mark each error identified, 1 mark each correction.

**13** START → process `Count ← 0`, `Day ← 0` → INPUT Temp → decision `Temp > 30?` (Yes →
`Count ← Count + 1`; No bypasses it) → `Day ← Day + 1` → decision `Day < 20?` (Yes → back to INPUT)
→ No → OUTPUT Count → STOP. Correct symbols (1), initialisation (1), both decisions with labelled
exits (2), loop back and output (1).

**14**

```
Highest ← Reading[1]
Lowest ← Reading[1]
Total ← 0
BelowZero ← 0
FOR Day ← 1 TO 7
    IF Reading[Day] > Highest
      THEN
        Highest ← Reading[Day]
    ENDIF
    IF Reading[Day] < Lowest
      THEN
        Lowest ← Reading[Day]
    ENDIF
    Total ← Total + Reading[Day]
    IF Reading[Day] < 0
      THEN
        BelowZero ← BelowZero + 1
    ENDIF
NEXT Day
OUTPUT "Highest: ", Highest
OUTPUT "Lowest: ", Lowest
OUTPUT "Average: ", Total / 7
OUTPUT "Days below 0: ", BelowZero
```

Initialisation (1), loop through all 7 (1), maximum (1), minimum (1), totalling (1), counting
below 0 (1), average calculated after the loop and all outputs with messages (1).

**15** Change `IF Mark[Index] > Mark[Index + 1]` to `IF Mark[Index] < Mark[Index + 1]`.
