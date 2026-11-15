# Computer architecture — Questions

## Specification coverage

| Field | Value |
| --- | --- |
| Specification points | 3.1.1–3.1.5 |
| Paper | Paper 1 — Computer Systems |

No past papers are stored in `me/papers/Computer_Science_0984/` yet. Marking guidance below is
**not official**; it follows the style of Cambridge mark schemes.

## 1. Recall

1. State the role of the CPU. **[1]**
2. What is a microprocessor? **[1]**
3. Name the register that holds the address of the next instruction. **[1]**
4. Name the bus that carries addresses and state its direction. **[2]**
5. What is an instruction set? **[2]**

## 2. Understanding

6. Describe the purpose of the MAR and the MDR. **[2]**
7. Explain why a larger cache can improve the performance of a CPU. **[2]**
8. Explain why doubling the number of cores may not double the performance of a CPU. **[2]**

## 3. Application

9. A washing machine is controlled by an embedded system. Describe **two** characteristics of an
   embedded system, using the washing machine as the example. **[4]**
10. Identify which of these contain an embedded system: laptop, vending machine, car anti-lock
    brakes, desktop PC, security alarm. **[3]**

## 4. Exam-style

11. **[6]** *Describe* the stages of the fetch–decode–execute cycle, including the role of the
    registers and buses.
12. **[3]** A computer's clock speed is increased from 2.4 GHz to 3.6 GHz. *Explain* how this
    affects its performance.

## Answers and marking guidance (not official)

1. Processes instructions and data (input into the computer) so the result can be output.
2. An integrated circuit on a single chip (that can act as the CPU).
3. Program counter (PC).
4. Address bus (1); one way / from CPU to memory (1).
5. The list of all commands the CPU can process (1); the commands are machine code (1).
6. MAR holds the address of the memory location to be read from/written to (1); MDR holds the
   data/instruction read from or to be written to memory (1).
7. Cache stores frequently used instructions/data (1); more can be held in faster memory so fewer
   (slower) fetches from RAM are needed (1).
8. Any two: the task may not be divisible between cores; cores must communicate/coordinate, which
   takes time; some programs are written to use only one core.
9. Any two characteristics, each with washing-machine context (2 + 2): dedicated function — only
   runs wash programs; microprocessor-controlled — reads the dial settings/sensors and controls the
   motor and heater; program in ROM — cannot be changed by the user; real-time response to sensors
   such as water level/temperature; small, low power, cheap.
10. Vending machine (1), anti-lock brakes (1), security alarm (1).
11. One mark each, max 6: address in PC copied to MAR; address sent on address bus; CU sends read
    signal on control bus; instruction sent on data bus to MDR; MDR contents copied to CIR; PC
    incremented; CU decodes instruction in CIR; CU sends control signals to execute; ALU performs
    calculations/logic; result stored in ACC.
12. More clock cycles per second (1); more FDE cycles/instructions per second, so faster
    processing (1); risk of overheating/instability, or other factors (cores, cache) also limit
    the gain (1).
