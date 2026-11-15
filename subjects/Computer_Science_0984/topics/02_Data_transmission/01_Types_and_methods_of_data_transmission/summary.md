# 2.1 Types and methods of data transmission — summary

**0984 · 2.1.1–2.1.3 · Paper 1**

- **Packet:** data is broken into small packets before sending.
  **Header** = destination address, packet number, originator's address · **payload** = the data ·
  **trailer** = end of packet + error check.
- **Packet switching:** packets sent independently → may take different routes → **router** picks
  the route from the destination address → may arrive out of order → reordered by packet number
  once the last arrives.
- **Serial** = 1 bit at a time, 1 wire: no skew, long distance, cheap, slower (USB).
  **Parallel** = several bits at once, several wires: faster, but **skew** over distance, more
  expensive, crosstalk → short distances (inside a computer).
- **Simplex** = one way only (sensor → computer). **Half-duplex** = both ways, one at a time
  (walkie-talkie). **Full-duplex** = both ways at once (phone call, broadband); costlier hardware.
- Scenario answer = method + reason from the scenario (distance, speed, need to reply, when).
- **USB** = serial interface. Plug in → detected → driver loaded → data sent serially; supplies
  power. Benefits: automatic, fits one way, industry standard, powers devices, backward
  compatible. Drawbacks: ~5 m cable limit, slower than Ethernet, very old devices may not work.
