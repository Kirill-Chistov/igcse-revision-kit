# Data storage — Summary

## Specification coverage

| Field | Value |
| --- | --- |
| Specification points | 3.3.1–3.3.6 |
| Paper | Paper 1 — Computer Systems |

## Essentials

- **Primary** = directly accessed by CPU (RAM, ROM). **Secondary** = not directly accessed;
  permanent storage (HDD, SSD, optical, SD, USB).
- **RAM**: volatile, read/write, holds data and programs in use.
  **ROM**: non-volatile, read only, holds start-up instructions (BIOS).
- Need both: RAM is empty at switch-on, so boot instructions must be in ROM.

## Operation

- **Magnetic (HDD)**: spinning platters → tracks → sectors; read/write head = electromagnet;
  magnetised areas = 1/0. Moving parts: slower, fragile.
- **Optical (CD, DVD, Blu-ray)**: laser burns pits; lands reflect, pits scatter; one spiral track.
- **Solid-state (SSD, SD, USB)**: NAND/NOR transistors; control gate + floating gate; electrons
  trapped in floating gate = stored bit. No moving parts: fast, robust.

## Virtual memory

Part of HDD/SSD used as extra RAM when RAM is full; pages moved between RAM and virtual memory;
prevents crashes / allows more programs; slower than RAM.

## Cloud vs local

- Cloud = remote physical servers accessed over the internet.
- + access anywhere, no hardware to buy, provider backups.
- − needs internet, security/privacy risk, subscription, provider outage.

## Traps

- ROM is primary, not secondary. Virtual memory is on the HDD/SSD, not in RAM.
