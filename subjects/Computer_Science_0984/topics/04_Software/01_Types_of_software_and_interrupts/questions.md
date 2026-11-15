# Types of software and interrupts — Questions

Specification points 4.1.1–4.1.4 · Paper 1. Marks in brackets.

There is no local Cambridge past-paper bank for this subject yet.

> **AI-generated practice written for this repository.** The marking guidance is not an official
> Cambridge mark scheme.

## Questions

1. Describe the difference between system software and application software. (2)
2. Tick whether each is system or application software: anti-virus, spreadsheet, printer driver,
   web browser, defragmentation software, operating system. (6)
3. Give **two** examples of utility software. (2)
4. Describe **three** basic functions of an operating system. (6)
5. Explain how the operating system allows several programs to be open at the same time. (3)
6. A user plugs a new printer into a computer. Describe the role of the operating system in making
   the printer work. (2)
7. Explain why an application cannot run on a computer that has hardware and an operating system
   stored on its SSD, but no firmware. (3)
8. State what is meant by an interrupt. (2)
9. Give **one** example of a hardware interrupt and **one** example of a software interrupt. (2)
10. Describe how the processor handles an interrupt. (5)
11. A program attempts to divide a number by zero. Describe what happens. (3)
12. Explain why interrupts allow a computer to print a long document while the user carries on
    typing. (3)

## Marking guidance

1. System software provides the services the computer requires / runs and manages the hardware (1);
   application software provides the services the user requires / carries out a user's task (1).
2. System: anti-virus, printer driver, defragmentation, OS; application: spreadsheet, browser (1 each).
3. Any two: anti-virus, defragmentation, back-up, file compression (1 each).
4. Any three functions (1) each with a correct description (1), e.g. managing memory — allocates RAM
   to programs / stops programs using the same locations; managing files — create, save, delete,
   organise into folders; managing user accounts — username/password, separate files and settings;
   providing security — log-on, access rights; providing an interface — GUI/CLI.
5. Multitasking (1); CPU and other resources are shared between the processes (1); switched rapidly
   according to priority, so they appear to run at the same time (1).
6. Loads / uses the printer's device driver (1); the driver translates data into a form the printer
   understands / OS manages the print queue (1).
7. At switch-on RAM holds no OS / RAM is volatile (1); the bootloader (firmware) is needed to load the
   OS into RAM (1); applications can only run on a running OS (1).
8. A signal from a hardware device or software to the processor (1) requesting attention / causing it
   to temporarily stop its current task (1).
9. Hardware: key pressed, mouse moved (1). Software: division by zero, two processes accessing the
   same memory location (1).
10. Processor checks for interrupts (at the end of each FDE cycle) (1); checks the interrupt's
    priority against the current task (1); saves the current task's state / register contents,
    including the PC (1); runs the ISR for that interrupt (1); restores the saved register contents
    and resumes the task (1).
11. A software interrupt is generated (1); the processor pauses the program and runs the ISR (1);
    an error message is output / the program may be stopped (1).
12. Printer sends an interrupt only when it needs more data (1); in between, the processor carries on
    with other tasks, e.g. the typing (1); keyboard interrupts are serviced as keys are pressed, so
    both appear to happen at once (1).
