# Data storage and compression — Summary

| Field | Value |
| --- | --- |
| Specification points | 1.3.1–1.3.4 |
| Paper | Paper 1 — no calculator |

## Units

bit → nibble (4 bits) → byte (8 bits) → KiB → MiB → GiB → TiB → PiB → EiB,
each step above the byte **× 1024** (never 1000).

## File size (answer in bits)

- Image = **resolution × colour depth**
- Sound = **sample rate × sample resolution × length (s)**
- ÷ 8 → bytes; ÷ 1024 per step up. Give the unit the question asks for.

## Compression

- Purpose: reduce file size → **less storage**, **less bandwidth**, **shorter transmission time**.
- **Lossy:** permanently removes data; original cannot be restored. E.g. reduce resolution,
  colour depth, sample rate or sample resolution.
- **Lossless:** no permanent loss; original fully restored. E.g. **RLE**.
- **RLE:** each run of identical values → count + value (WWWWBBB → 4W 3B). Poor with few repeats.

## Traps

- Formulas give **bits**, not bytes.
- 1 KiB = **1024** bytes.
