# Arrays — Summary

## Specification coverage

| Field | Value |
| --- | --- |
| Specification points | 8.2.1–8.2.3 |
| Paper | Paper 2 — Algorithms, Programming and Logic |

## Essentials

- **Array** = fixed-length structure, elements of one data type, one identifier, accessed by index.
- Why: one name for many values; a **variable as index** lets one loop process every element.
- `DECLARE Names : ARRAY[1:30] OF STRING` · `DECLARE Grid : ARRAY[1:3, 1:4] OF INTEGER`
  (3 rows × 4 columns). First index 0 or 1 — read the bounds.
- Use one element: `Names[I] ← "Ali"`, `Grid[Row, Column]` — always row first.
- 1D: one `FOR` loop, loop variable = index. 2D: nested loops, outer = rows, inner = columns.
- Different data about the same item → separate arrays with the same index.
