# Cambridge IGCSE (9–1) Computer Science (0984) — Syllabus Representation

## Source

| Field | Value |
| --- | --- |
| Official document | `subjects/Computer_Science_0984/Specification.pdf` |
| Downloaded from | https://www.cambridgeinternational.org/Images/697248-2026-2028-syllabus.pdf |
| Issue / version | Syllabus for examination in **2026, 2027 and 2028** (a 2-page official syllabus update is stored alongside as `official_syllabus_update.pdf`) |
| Retrieved | 2026-08-31 |

## Qualification at a glance

| Paper | Duration | Marks | Weighting | Content | Style |
| --- | --- | --- | --- | --- | --- |
| Paper 1 – Computer Systems | 1 h 45 min | 75 | 50% | Topics **1–6** | Short-answer and structured questions |
| Paper 2 – Algorithms, Programming and Logic | 1 h 45 min | 75 | 50% | Topics **7–10** | Short-answer, structured, plus a scenario-based question |

All questions are compulsory on both papers. **No calculators are permitted in either paper.**
Both are externally assessed. There is no coursework and no separate practical examination.

## Assessment objectives

| AO | Description | Qualification | Paper 1 | Paper 2 |
| --- | --- | --- | --- | --- |
| AO1 | Knowledge and understanding of principles and concepts | 40% | 60% | 20% |
| AO2 | Apply knowledge and understanding to a given context, including analysis and design of computational or programming problems | 40% | 20% | 60% |
| AO3 | Provide solutions by evaluating systems, making reasoned judgements and presenting conclusions | 20% | 20% | 20% |

## Course distinctions that affect what can be assessed

- **The content is split cleanly between the two papers**: topics 1–6 are Paper 1 only, topics
  7–10 are Paper 2 only. This is the single most important planning fact for this subject.
- **Paper 2 answers are written in pseudocode or a high-level language.** Cambridge's own
  pseudocode conventions (published in the syllabus appendix) are what exam answers are marked
  against. Program code written in a real language is accepted, but the pseudocode conventions
  must be understood.
- The final Paper 2 question is a **15-mark unseen scenario question**.
- **Practical programming is compulsory teaching but is not separately examined.** The classroom
  language is a centre choice; confirm which language the class uses before writing code examples
  (see `subjects/Computer_Science_0984/SUBJECT_RULES.md`).
- Cambridge numbers content as topic → sub-topic (e.g. `1.1`) and then as a numbered list of
  *"Candidates should be able to"* statements. This repository refers to those statements as
  `1.1.2` — sub-topic plus the item number **as printed in the syllabus**.


## How to read this file

- This file is a **curriculum representation**, not revision notes. It exists so that AI
  agents can plan and trace study material without re-parsing the official PDF.
- Official identifiers (section numbers, specification point numbers, topic names) are
  preserved so every statement can be traced back to `subjects/Computer_Science_0984/Specification.pdf`.
- Requirement wording is condensed/paraphrased from the official objective statements.
  **The official PDF is always authoritative** where this file is ambiguous.
- `specification_map.csv` maps each specification point to its planned folder in `Computer_Science_0984/`.
- `coverage_checklist.md` tracks which points have study material written.

## Content


### 1 — Data representation  _(Paper 1)_


#### 1.1 Number systems

Planned content folder: `Computer_Science_0984/01_Data_representation/01_Number_systems/`

| Spec point | Candidates should be able to |
| --- | --- |
| 1.1.1 | Understand how and why computers use binary to represent all forms of data |
| 1.1.2 | (a) Understand the denary, binary and hexadecimal number systems (b) Convert between (i) positive denary and positive binary (ii) positive denary and positive hexadecimal (iii) positive hexadecimal and positive binary |
| 1.1.3 | Understand how and why hexadecimal is used as a beneficial method of data representation |
| 1.1.4 | (a) Add two positive 8-bit binary integers (b) Understand the concept of overflow and why it occurs in binary addition |
| 1.1.5 | Perform a logical binary shift on a positive 8-bit binary integer and understand the effect this has on the positive binary integer |
| 1.1.6 | Use the two’s complement number system to represent positive and negative 8-bit binary integers |

#### 1.2 Text, sound and images

Planned content folder: `Computer_Science_0984/01_Data_representation/02_Text_sound_and_images/`

| Spec point | Candidates should be able to |
| --- | --- |
| 1.2.1 | Understand how and why a computer represents text and the use of character sets, including American standard code for information interchange (ASCII) and Unicode |
| 1.2.2 | Understand how and why a computer represents sound, including the effects of the sample rate and sample resolution |
| 1.2.3 | Understand how and why a computer represents an image, including the effects of the resolution and colour depth |

#### 1.3 Data storage and compression

Planned content folder: `Computer_Science_0984/01_Data_representation/03_Data_storage_and_compression/`

| Spec point | Candidates should be able to |
| --- | --- |
| 1.3.1 | Understand how data storage is measured |
| 1.3.2 | Calculate the file size of an image file and a sound file, using information given |
| 1.3.3 | Understand the purpose of and need for data compression |
| 1.3.4 | Understand how files are compressed using lossy and lossless compression methods |

### 2 — Data transmission  _(Paper 1)_


#### 2.1 Types and methods of data transmission

Planned content folder: `Computer_Science_0984/02_Data_transmission/01_Types_and_methods_of_data_transmission/`

| Spec point | Candidates should be able to |
| --- | --- |
| 2.1.1 | (a) Understand that data is broken down into packets to be transmitted (b) Describe the structure of a packet (c) Describe the process of packet switching |
| 2.1.2 | (a) Describe how data is transmitted from one device to another using different methods of data transmission (b) Explain the suitability of each method of data transmission, for a given scenario |
| 2.1.3 | Understand the universal serial bus (USB) interface and explain how it is used to transmit data |

#### 2.2 Methods of error detection

Planned content folder: `Computer_Science_0984/02_Data_transmission/02_Methods_of_error_detection/`

| Spec point | Candidates should be able to |
| --- | --- |
| 2.2.1 | Understand the need to check for errors after data transmission and how these errors can occur |
| 2.2.2 | Describe the processes involved in each of the following error detection methods for detecting errors in data after transmission: parity check (odd and even), checksum and echo check |
| 2.2.3 | Describe how a check digit is used to detect errors in data entry and identify examples of when a check digit is used, including international standard book numbers (ISBN) and bar codes |
| 2.2.4 | Describe how an automatic repeat query (ARQ) can be used to establish that data is received without error |

#### 2.3 Encryption

Planned content folder: `Computer_Science_0984/02_Data_transmission/03_Encryption/`

| Spec point | Candidates should be able to |
| --- | --- |
| 2.3.1 | Understand the need for and purpose of encryption when transmitting data |
| 2.3.2 | Understand how data is encrypted using symmetric and asymmetric encryption |

### 3 — Hardware  _(Paper 1)_


#### 3.1 Computer architecture

Planned content folder: `Computer_Science_0984/03_Hardware/01_Computer_architecture/`

| Spec point | Candidates should be able to |
| --- | --- |
| 3.1.1 | (a) Understand the role of the central processing unit (CPU) in a computer (b) Understand what is meant by a microprocessor |
| 3.1.2 | (a) Understand the purpose of the components in a CPU, in a computer that has a Von Neumann architecture (b) Describe the process of the fetch–decode–execute (FDE) cycle, including the role of each component in the process |
| 3.1.3 | Understand what is meant by a core, cache and clock in a CPU and explain how they can affect the performance of a CPU |
| 3.1.4 | Understand the purpose and use of an instruction set for a CPU |
| 3.1.5 | Describe the purpose and characteristics of an embedded system and identify devices in which they are commonly used |

#### 3.2 Input and output devices

Planned content folder: `Computer_Science_0984/03_Hardware/02_Input_and_output_devices/`

| Spec point | Candidates should be able to |
| --- | --- |
| 3.2.1 | Understand what is meant by an input device and why it is required |
| 3.2.2 | Understand what is meant by an output device and why it is required |
| 3.2.3 | (a) Understand what is meant by a sensor and the purposes of sensors (b) Identify the type of data captured by each sensor and understand when each sensor would be used, including selecting the most suitable sensor for a given context |

#### 3.3 Data storage

Planned content folder: `Computer_Science_0984/03_Hardware/03_Data_storage/`

| Spec point | Candidates should be able to |
| --- | --- |
| 3.3.1 | Understand what is meant by primary storage |
| 3.3.2 | Understand what is meant by secondary storage |
| 3.3.3 | Describe the operation of magnetic, optical and solid-state (flash memory) storage and give examples of each |
| 3.3.4 | Describe what is meant by virtual memory, how it is created and used and why it is necessary |
| 3.3.5 | Understand what is meant by cloud storage |
| 3.3.6 | Explain the advantages and disadvantages of storing data on the cloud in comparison to storing it locally |

#### 3.4 Network hardware

Planned content folder: `Computer_Science_0984/03_Hardware/04_Network_hardware/`

| Spec point | Candidates should be able to |
| --- | --- |
| 3.4.1 | Understand that a computer needs a network interface card (NIC) to access a network |
| 3.4.2 | Understand what is meant by, and the purpose of, a media access control (MAC) address, including its structure |
| 3.4.3 | (a) Understand what is meant by, and the purpose of, an internet protocol (IP) address (b) Understand that there are different types of IP address |
| 3.4.4 | Describe the role of a router in a network |

### 4 — Software  _(Paper 1)_


#### 4.1 Types of software and interrupts

Planned content folder: `Computer_Science_0984/04_Software/01_Types_of_software_and_interrupts/`

| Spec point | Candidates should be able to |
| --- | --- |
| 4.1.1 | Describe the difference between system software and application software and provide examples of each |
| 4.1.2 | Describe the role and basic functions of an operating system |
| 4.1.3 | Understand how hardware, firmware and an operating system are required to run applications software |
| 4.1.4 | Describe the role and operation of interrupts |

#### 4.2 Types of programming language, translators and integrated development environments

Planned content folder: `Computer_Science_0984/04_Software/02_Types_of_programming_language_translators_and/`

| Spec point | Candidates should be able to |
| --- | --- |
| 4.2.1 | Explain what is meant by a high-level language and a low-level language, including the advantages and disadvantages of each |
| 4.2.2 | Understand that assembly language is a form of low-level language that uses mnemonics, and that an assembler is needed to translate an assembly language program into machine code |
| 4.2.3 | Describe the operation of a compiler and an interpreter, including how high-level language is translated by each and how errors are reported |
| 4.2.4 | Explain the advantages and disadvantages of a compiler and an interpreter |
| 4.2.5 | Explain the role of an IDE in writing program code and the common functions IDEs provide |

### 5 — The internet and its uses  _(Paper 1)_


#### 5.1 The internet and the world wide web

Planned content folder: `Computer_Science_0984/05_The_internet_and_its_uses/01_The_internet_and_the_world_wide_web/`

| Spec point | Candidates should be able to |
| --- | --- |
| 5.1.1 | Understand the difference between the internet and the world wide web |
| 5.1.2 | Understand what is meant by a uniform resource locator (URL) |
| 5.1.3 | Describe the purpose and operation of hypertext transfer protocol (HTTP) and hypertext transfer protocol secure (HTTPS) |
| 5.1.4 | Explain the purpose and functions of a web browser |
| 5.1.5 | Describe how web pages are located, retrieved and displayed on a device when a user enters a URL |
| 5.1.6 | Explain what is meant by cookies and how they are used, including session cookies and persistent cookies |

#### 5.2 Digital currency

Planned content folder: `Computer_Science_0984/05_The_internet_and_its_uses/02_Digital_currency/`

| Spec point | Candidates should be able to |
| --- | --- |
| 5.2.1 | Understand the concept of a digital currency and how digital currencies are used |
| 5.2.2 | Understand the process of blockchain and how it is used to track digital currency transactions |

#### 5.3 Cyber security

Planned content folder: `Computer_Science_0984/05_The_internet_and_its_uses/03_Cyber_security/`

| Spec point | Candidates should be able to |
| --- | --- |
| 5.3.1 | Describe the processes involved in, and the aim of carrying out, a range of cyber security threats |
| 5.3.2 | Explain how a range of solutions are used to help keep data safe from security threats |

### 6 — Automated and emerging technologies  _(Paper 1)_


#### 6.1 Automated systems

Planned content folder: `Computer_Science_0984/06_Automated_and_emerging_technologies/01_Automated_systems/`

| Spec point | Candidates should be able to |
| --- | --- |
| 6.1.1 | Describe how sensors, microprocessors and actuators can be used in collaboration to create automated systems |
| 6.1.2 | Describe the advantages and disadvantages of an automated system used for a given scenario |

#### 6.2 Robotics

Planned content folder: `Computer_Science_0984/06_Automated_and_emerging_technologies/02_Robotics/`

| Spec point | Candidates should be able to |
| --- | --- |
| 6.2.1 | Understand what is meant by robotics |
| 6.2.2 | Describe the characteristics of a robot |
| 6.2.3 | Understand the roles that robots can perform and describe the advantages and disadvantages of their use |

#### 6.3 Artificial intelligence

Planned content folder: `Computer_Science_0984/06_Automated_and_emerging_technologies/03_Artificial_intelligence/`

| Spec point | Candidates should be able to |
| --- | --- |
| 6.3.1 | Understand what is meant by artificial intelligence (AI) |
| 6.3.2 | Describe the main characteristics of AI as the collection of data and the rules for using that data, the ability to reason, and it can include the ability to learn and adapt |
| 6.3.3 | Explain the basic operation and components of AI systems to simulate intelligent behaviour Algorithms, programming and logic See section 4 for the: • standard flowchart symbols that must be used by stude • logic gate symbols that must be used by students when • format in which pseudocode will ... |

### 7 — Algorithm design and problem-solving  _(Paper 2)_


#### Algorithm design and problem-solving (no sub-topics)

Planned content folder: `Computer_Science_0984/07_Algorithm_design_and_problem_solving/`

| Spec point | Candidates should be able to |
| --- | --- |
| 7.1 | Understand the program development life cycle, limited to: analysis, design, coding and testing |
| 7.2 | (a) Understand that every computer system is made up of sub-systems, which are made up of further sub-systems (b) Understand how a problem can be decomposed into its component parts (c) Use different methods to design and construct a solution to a problem |
| 7.3 | Explain the purpose of a given algorithm |
| 7.4 | Understand standard methods of solution |
| 7.5 | (a) Understand the need for validation checks to be made on input data and the different types of validation check (b) Understand the need for verification checks to be made on input data and the different types of verification check |
| 7.6 | Suggest and apply suitable test data |
| 7.7 | Complete a trace table to document a dry-run of an algorithm |
| 7.8 | Identify errors in given algorithms and suggest ways of correcting these errors |
| 7.9 | Write and amend algorithms for given problems or scenarios, using: pseudocode, program code and flowcharts |

### 8 — Programming  _(Paper 2)_


#### 8.1 Programming concepts

Planned content folder: `Computer_Science_0984/08_Programming/01_Programming_concepts/`

| Spec point | Candidates should be able to |
| --- | --- |
| 8.1.1 | Declare and use variables and constants |
| 8.1.2 | Understand and use basic data types |
| 8.1.3 | Understand and use input and output |
| 8.1.4 | (a) Understand and use the concept of sequence (b) Understand and use the concept of selection (c) Understand and use the concept of iteration (d) Understand and use the concepts of totalling and counting (e) Understand and use the concept of string handling |
| 8.1.5 | Understand and use nested statements |
| 8.1.6 | (a) Understand what is meant by procedures, functions and parameters (b) Define and use procedures and functions, with or without parameters (c) Understand and use local and global variables |
| 8.1.7 | Understand and use library routines |
| 8.1.8 | Understand how to create a maintainable program |

#### 8.2 Arrays

Planned content folder: `Computer_Science_0984/08_Programming/02_Arrays/`

| Spec point | Candidates should be able to |
| --- | --- |
| 8.2.1 | Declare and use one-dimensional (1D) and two-dimensional (2D) arrays |
| 8.2.2 | Understand the use of arrays |
| 8.2.3 | Write values into, and read values from, an array using iteration |

#### 8.3 File handling

Planned content folder: `Computer_Science_0984/08_Programming/03_File_handling/`

| Spec point | Candidates should be able to |
| --- | --- |
| 8.3.1 | Understand the purpose of storing data in a file to be used by a program |
| 8.3.2 | Open, close and use a file for reading and writing |

### 9 — Databases  _(Paper 2)_


#### Databases (no sub-topics)

Planned content folder: `Computer_Science_0984/09_Databases/`

| Spec point | Candidates should be able to |
| --- | --- |
| 9.1 | Define a single-table database from given data storage requirements |
| 9.2 | Suggest suitable basic data types |
| 9.3 | Understand the purpose of a primary key and identify a suitable primary key for a given database table |
| 9.4 | Read, understand and complete structured query language (SQL) scripts to query data stored in a single database table |

### 10 — Boolean logic  _(Paper 2)_


#### Boolean logic (no sub-topics)

Planned content folder: `Computer_Science_0984/10_Boolean_logic/`

| Spec point | Candidates should be able to |
| --- | --- |
| 10.1 | Identify and use the standard symbols for logic gates |
| 10.2 | Define and understand the functions of logic gates |
| 10.3 | (a) Use logic gates to create given logic circuits from a: (i) problem statement (ii) logic expression (iii) truth table (b) Complete a truth table from a: (i) problem statement (ii) logic expression (iii) logic circuit (c) Write a logic expression from a: (i) problem statement (ii) logic circuit ... |
