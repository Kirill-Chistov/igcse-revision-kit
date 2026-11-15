# Types of software and interrupts — Summary

Specification points 4.1.1–4.1.4 · Paper 1

**System software** — services the computer requires: OS, utilities (anti-virus, defragmentation,
back-up, compression), device drivers, compilers.
**Application software** — services the user requires: word processor, spreadsheet, browser, game.

**OS functions (9):** managing files · handling interrupts · providing an interface (GUI/CLI) ·
managing peripherals and drivers · managing memory · managing multitasking · providing a platform
for running applications · providing system security · managing user accounts.

**Layers:** applications run on the OS → the OS runs on the firmware → the bootloader (firmware, in
ROM) runs on the hardware. At switch-on the bootloader loads the OS into RAM (RAM is volatile).

**Interrupt** — signal from hardware or software to the processor requesting attention; the current
task is paused.
- Hardware: key pressed, mouse moved. Software: division by zero, two processes accessing the same
  memory location.
- Handling: checked at end of each FDE cycle → priority checked → save register contents (incl. PC)
  → run the ISR → restore registers → resume the task.
- Role: processor responds at once without constantly checking devices → multitasking.
