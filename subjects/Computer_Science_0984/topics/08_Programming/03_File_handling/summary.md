# File handling — Summary

## Specification coverage

| Field | Value |
| --- | --- |
| Specification points | 8.3.1–8.3.2 |
| Paper | Paper 2 — Algorithms, Programming and Logic |

## Essentials

- Variables are lost when the program ends; a **file** stores data **permanently**, so it need not
  be re-entered and can be used later by this program, another program or another computer.
- `OPENFILE "F.txt" FOR READ` / `FOR WRITE` (WRITE creates a new file — old data lost).
- `READFILE "F.txt", Variable` reads the next item/line; `WRITEFILE "F.txt", Variable` writes.
- `CLOSEFILE "F.txt"` when finished. One mode at a time: close, then reopen to read back.
