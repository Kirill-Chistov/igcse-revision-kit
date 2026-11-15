# Number systems — Questions

| Field | Value |
| --- | --- |
| Specification points | 1.1.1–1.1.6 |
| Paper | Paper 1 — no calculator |

No past papers are stored in `me/papers/Computer_Science_0984/` yet. Marking guidance below is
written for this repository and is **not an official mark scheme**.

## 1. Recall

1. State the base of the denary, binary and hexadecimal number systems.
2. What is the largest denary value an 8-bit register can hold?
3. What denary value does the hex digit D represent?

## 2. Conversions

4. Convert 10011101 to denary.
5. Convert 214 to 8-bit binary.
6. Convert the 16-bit binary number 0110 1011 1110 0001 to hexadecimal.
7. Convert hex 9C to (a) denary (b) 8-bit binary.
8. Convert 250 to hexadecimal.

## 3. Binary arithmetic and shifts

9. Add 01101001 and 00110110. Give the 8-bit answer.
10. Add 10110111 and 01011010 in an 8-bit register. State the stored result and explain what has
    happened.
11. Perform a logical left shift of two places on 00101101. State the effect on the denary value.
12. Perform a logical right shift of three places on 11010000. State the denary values before
    and after.
13. 00001011 is shifted right two places. Explain why the result is not exactly the original
    value ÷ 4.

## 4. Two's complement

14. Write +93 and −93 as 8-bit two's complement integers.
15. Convert the two's complement integer 11110110 to denary.
16. State the largest and smallest values that can be stored in 8-bit two's complement.

## 5. Exam-style

17. **[2 marks]** *Explain* why computers use binary to represent data.
18. **[3 marks]** *Explain* why hexadecimal is used by computer scientists, giving **one** area
    where it is used.
19. **[3 marks]** *Explain* what is meant by an overflow error and why it occurs.

## Answers and marking guidance

1. Denary 10, binary 2, hexadecimal 16.
2. 255.
3. 13.
4. 128 + 16 + 8 + 4 + 1 = **157**.
5. 128 + 64 + 16 + 4 + 2 → **11010110**.
6. 0110 = 6, 1011 = B, 1110 = E, 0001 = 1 → **6BE1**.
7. (a) 9 × 16 + 12 = **156** (b) 9 = 1001, C = 1100 → **10011100**.
8. 250 ÷ 16 = 15 r 10 → **FA**.
9. 105 + 54 = 159 → **10011111**.
10. 183 + 90 = 273 > 255. A 9th bit is generated and lost; stored result **00010001** (17).
    This is an **overflow** error.
11. **10110100**; value multiplied by 4 (45 → 180).
12. **00011010**; 208 → 26 (÷ 8).
13. Result 00000010 (2) instead of 2.75: the **1**s shifted off the right (least significant
    bits) are **lost**.
14. +93 = **01011101**; −93: invert → 10100010, add 1 → **10100011**.
15. −128 + 64 + 32 + 16 + 4 + 2 = **−10**.
16. Largest +127 (01111111); smallest −128 (10000000).
17. Any two: computer made of switches/transistors with **two states** (on/off) ✓; represented
    by 1 and 0 ✓; data **processed by logic gates** / **stored in registers** ✓.
18. Shorter representation of binary / one hex digit = 4 bits ✓; easier for humans to read,
    write or remember ✓; fewer errors ✓ (max 2); one use: MAC address / IPv6 / HTML colour
    code / error code ✓.
19. A device has a **predefined limit** on the value it can store (e.g. 8 bits, max 255) ✓;
    a calculation produces a value **greater than this limit** ✓; the extra (9th) bit cannot be
    stored, so the result is incorrect ✓.
