# 2.2 Methods of error detection — summary

**0984 · 2.2.1–2.2.4 · Paper 1**

- **Why:** interference during transmission → **data loss, data gain, data change**.
- **Parity:** agree even/odd; sender sets the parity bit (usually the left-most bit) so the count of
  1s is even/odd; receiver recounts → wrong parity = error. Misses two-bit errors; can't locate the
  bit.
- **Parity block:** bytes each with a parity bit + a **parity byte** of column parity bits. Odd row ×
  odd column = the faulty bit → can be corrected.
- **Checksum:** sender calculates a checksum from the block (agreed algorithm) and sends both;
  receiver recalculates and compares; different → block re-sent.
- **Echo check:** receiver sends the data back; **sender** compares with the original; different →
  re-send. Can't tell which direction the error happened in.
- **Check digit:** final digit calculated from the other digits; recalculated on entry/scan;
  mismatch → re-enter. Catches wrong digit, transposition, missing/extra digit. **ISBN**, **bar codes**.
  Data-entry errors, not transmission.
- **ARQ:** receiver checks each block → **positive acknowledgement** (OK) or **negative
  acknowledgement** (error, re-send). No acknowledgement within the **timeout** → sender re-sends
  automatically.
