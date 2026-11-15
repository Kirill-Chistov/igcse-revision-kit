# Number systems — Summary

| Field | Value |
| --- | --- |
| Specification points | 1.1.1–1.1.6 |
| Paper | Paper 1 — no calculator |

## Essentials

- Computers use **binary** because they are built from two-state switches; data is processed by
  **logic gates** and stored in **registers**. All data must be converted to binary.
- **Denary** base 10 · **binary** base 2 · **hexadecimal** base 16 (A–F = 10–15).
- 8-bit columns: 128 64 32 16 8 4 2 1. Max 8-bit = **255**; conversions go up to **16 bits**.
- Hex columns: 4096 256 16 1.
- **Hex is used** because it is a **shorter representation of binary**, so easier for humans to
  read, write and remember, with fewer errors. Uses: **MAC addresses, IPv6 addresses, HTML colour
  codes, error codes**.

## Methods

| Conversion | Method |
| --- | --- |
| binary → denary | add column values under each 1 |
| denary → binary | subtract the largest column value that fits, left to right |
| binary ↔ hex | groups of 4 bits **from the right**; each nibble = one hex digit (8 4 2 1) |
| hex → denary | digit × 16 + digit × 1 |
| denary → hex | ÷ 16: quotient = 16s digit, remainder = 1s digit |

- **Addition:** 1 + 1 = 0 carry 1; 1 + 1 + 1 = 1 carry 1.
- **Overflow:** result too large for the register (> 255 in 8 bits) → 9th bit lost → wrong answer.
- **Logical shift:** left *n* = × 2ⁿ, right *n* = ÷ 2ⁿ; bits off the end are lost, **0s** shift
  in. Losing a 1 makes the result wrong (MSB lost on left shift, LSB on right shift).
- **Two's complement:** MSB worth **−128**; range −128 to +127; MSB 1 = negative.
  Negative: write +n → **invert → add 1**. Reading: add values using −128.

## Traps

- Group nibbles from the **right**.
- Shifts fill with **0**, never with the lost bit.
- Two's complement: invert **and add 1**.
