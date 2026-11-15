# Network hardware — Questions

## Specification coverage

| Field | Value |
| --- | --- |
| Specification points | 3.4.1–3.4.4 |
| Paper | Paper 1 — Computer Systems |

No past papers are stored in `me/papers/Computer_Science_0984/` yet. Marking guidance below is
**not official**; it follows the style of Cambridge mark schemes.

## 1. Recall

1. What hardware does a computer need to access a network? **[1]**
2. State the purpose of a MAC address. **[1]**
3. How many bits are in an IPv4 address and in an IPv6 address? **[2]**

## 2. Understanding

4. Describe the structure of a MAC address. **[3]**
5. Explain **two** differences between a MAC address and an IP address. **[4]**
6. Explain the difference between a static and a dynamic IP address. **[2]**

## 3. Application

7. Identify each as an IPv4 address, an IPv6 address, a MAC address or invalid. **[5]**
   (a) `172.16.254.1` (b) `A4-5E-60-E8-1B-2C` (c) `2001:db8::ff00:42:8329`
   (d) `192.168.300.4` (e) `fe80:0000:0000:0000:0202:b3ff:fe1e:8329`
8. A company hosts its own website. Explain why its web server should have a static IP address. **[2]**

## 4. Exam-style

9. **[3]** *Describe* the role of a router in a home network.
10. **[3]** *Explain* why IPv6 was introduced and how its format differs from IPv4.

## Answers and marking guidance (not official)

1. Network interface card (NIC).
2. To uniquely identify a (specific) device on a network.
3. IPv4 32 bits (1); IPv6 128 bits (1).
4. 48 bits / 12 hex digits in 6 pairs (1); usually written in hexadecimal (1); first half is the
   manufacturer code, second half is the serial code of the device (1).
5. Any two, explained: MAC is set by the manufacturer / IP is allocated by the network; MAC does
   not change / IP can change (dynamic) or when the device joins another network; MAC is 48-bit hex
   / IP is 32-bit (IPv4) or 128-bit (IPv6).
6. Static: permanently assigned, never changes (1); dynamic: allocated each time the device
   connects, so can change (1).
7. (a) IPv4 (b) MAC (c) IPv6 (d) invalid — 300 is greater than 255 (e) IPv6.
8. The address never changes (1), so users'/DNS requests can always find the server at the same
   address (1).
9. Assigns (dynamic) IP addresses to devices on the network (1); receives packets and sends each to
   its specific destination using the destination IP address (1); connects the home network to the
   internet (1).
10. IPv4 (32-bit) allows only about 4.3 billion addresses, not enough for all devices (1); IPv6 is
    128-bit, giving vastly more addresses (1); IPv6 is written as 8 groups of 4 hex digits
    separated by colons, IPv4 as 4 denary groups separated by full stops (1).
