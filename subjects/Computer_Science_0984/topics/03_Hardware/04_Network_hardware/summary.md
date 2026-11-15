# Network hardware — Summary

## Specification coverage

| Field | Value |
| --- | --- |
| Specification points | 3.4.1–3.4.4 |
| Paper | Paper 1 — Computer Systems |

## Essentials

- **NIC**: hardware a computer needs to access a network (wired or wireless).
- **MAC address**: unique; set on the NIC at manufacture; identifies a specific device.
  48 bits = 12 hex digits in 6 pairs; first 3 pairs **manufacturer code**, last 3 **serial code**.
- **IP address**: allocated by the network; identifies the device on the network/internet.
  - **Static** = permanent (web servers). **Dynamic** = allocated at each connection, can change.
  - **IPv4**: 32-bit, 4 denary groups 0–255, full stops, e.g. `192.168.1.3`.
  - **IPv6**: 128-bit, 8 groups of 4 hex digits, colons; `::` replaces a run of zero groups.
- **Router**: sends data to a specific destination (using the destination IP address), can assign
  IP addresses, connects a LAN to the internet.

## Traps

- MAC set by manufacturer; IP allocated by the network.
- IPv6 is hex with colons, not denary with full stops.
