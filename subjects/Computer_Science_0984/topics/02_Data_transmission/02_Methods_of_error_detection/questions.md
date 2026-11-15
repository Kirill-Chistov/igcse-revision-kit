# 2.2 Methods of error detection — questions

**0984 · 2.2.1–2.2.4 · Paper 1.** Exam-style practice. The marking guidance is written for this
repository and is **not** an official Cambridge mark scheme. No past papers are stored in
`me/papers/Computer_Science_0984/` yet.

## Questions

1. Explain why data should be checked for errors after transmission. Include the types of error that
   can occur. [3]
2. Add a parity bit (as the left-most bit) to each 7-bit value:
   (a) 1010110, even parity · (b) 1110011, even parity · (c) 0110001, odd parity. [3]
3. Even parity is used. Which of these received bytes contain an error? 10110110 · 01110010 [1]
4. Explain why a parity check may not detect an error. [2]
5. This block was received. **Even** parity is used; column 1 holds the parity bits and the last
   row is the parity byte. One bit is wrong. Identify it and give the corrected byte. [3]

   | | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
   | --- | --- | --- | --- | --- | --- | --- | --- | --- |
   | Byte 1 | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 1 |
   | Byte 2 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 |
   | Byte 3 | 1 | 1 | 0 | 1 | 0 | 1 | 1 | 1 |
   | Byte 4 | 1 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |
   | Parity byte | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |

6. Describe how a checksum is used to detect errors in transmitted data. [4]
7. Describe how an echo check works and give **one** drawback. [4]
8. The ISBN-13 check digit is found like this: add the digits in odd positions; add the digits in
   even positions and multiply by 3; add the two results and divide by 10; if the remainder is 0
   the check digit is 0, otherwise it is 10 − remainder.
   (a) Calculate the check digit for 978186197876. [2]
   (b) A librarian types 9781861978796. Show how the computer detects the error. [2]
9. State **two** types of data-entry error a check digit can detect. [2]
10. Describe how an automatic repeat query (ARQ) is used to make sure data is received without
    error. [5]

## Marking guidance (not official)

1. Data can be corrupted during transmission, e.g. by interference [1]; data can be lost, gained or
   changed [1]; corrupted data would be unusable / give incorrect results, so it must be detected and
   re-sent [1].
2. (a) four 1s → **0**1010110 · (b) five 1s → **1**1110011 · (c) three 1s → **0**0110001.
3. 10110110 (five 1s, odd). 01110010 has four 1s — no error detected.
4. If two (an even number of) bits change, the number of 1s stays even/odd [1], so the parity is
   still correct and the error is not flagged [1]. (Also credit: it cannot show which bit is wrong.)
5. Byte 2 has three 1s (odd) [1]; column 7 has one 1 (odd) [1]; so bit 7 of byte 2 is wrong:
   corrected byte **10011010** [1].
6. Checksum calculated from the block using an agreed algorithm [1] · sent with the block [1] ·
   receiver recalculates the checksum from the received block [1] · compares the two; if different
   an error has occurred and the block is re-sent [1].
7. Data sent to the receiver [1] · receiver sends a copy back to the sender [1] · sender compares it
   with the original; any difference = error, data re-sent [1]. Drawback: it cannot tell whether the
   error happened on the way there or on the way back / the copy returned could be corrupted [1].
8. (a) 9+8+8+1+7+7 = 40; 3 × (7+1+6+9+8+6) = 3 × 37 = 111 [1]; 40 + 111 = 151 → remainder 1 →
   10 − 1 = **9** [1].
   (b) Recalculate from the first 12 digits 978186197879: 9+8+8+1+7+7 = 40; 3 × (7+1+6+9+8+9) =
   120; 160 → remainder 0 → check digit **0** [1]. The check digit entered is 6; they do not match,
   so an error is reported (the last two digits were transposed) [1].
9. Any two: an incorrect digit · two digits transposed · a digit missed out · an extra digit added.
10. Receiver uses error detection (e.g. checksum) on the data [1] · no error → sends a **positive
    acknowledgement** [1] · error → sends a **negative acknowledgement**, requesting re-transmission
    [1] · sender waits a set time (**timeout**) for an acknowledgement [1] · if none arrives in that
    time the data is re-sent automatically [1] (credit: until a positive acknowledgement arrives or a
    set number of attempts).
