# Computer architecture — Summary

## Specification coverage

| Field | Value |
| --- | --- |
| Specification points | 3.1.1–3.1.5 |
| Paper | Paper 1 — Computer Systems |

## Essentials

- **CPU**: processes instructions and data input into the computer so the result can be output.
- **Microprocessor**: an integrated circuit on a single chip.
- **Von Neumann**: instructions and data stored together in RAM, fetched on the same buses.
- **Core** = CU + ALU + registers. More cores → more instructions processed at once (not in proportion).
- **Cache** = fast memory for frequently used instructions/data. Bigger → fewer slow RAM fetches.
- **Clock** = timing signals. Faster → more FDE cycles per second (risk: overheating).
- **Instruction set** = all commands a CPU can process; they are machine code.
- **Embedded system** = dedicated function inside a larger device (appliances, cars, security,
  lighting, vending machines) vs general purpose computer = many functions (PC, laptop).

## Components

| Component | Holds / does |
| --- | --- |
| CU | decodes; sends control signals |
| ALU | arithmetic and logic |
| PC | address of **next** instruction |
| MAR | address being read from / written to |
| MDR | data/instruction read from or written to memory |
| CIR | current instruction |
| ACC | ALU results |
| Address / data / control bus | addresses (one way) / data and instructions (two way) / signals (two way) |

## FDE cycle

PC → MAR → address bus + read signal → instruction to MDR on data bus → MDR → CIR → PC + 1 →
CU decodes → CU sends control signals → ALU executes, result in ACC → repeat.

## Traps

- PC = address of next instruction, not the instruction.
- Address bus is the only one-way bus.
