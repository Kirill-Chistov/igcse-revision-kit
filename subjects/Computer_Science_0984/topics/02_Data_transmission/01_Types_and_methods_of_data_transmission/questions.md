# 2.1 Types and methods of data transmission — questions

**0984 · 2.1.1–2.1.3 · Paper 1.** Exam-style practice. The marking guidance is written for this
repository and is **not** an official Cambridge mark scheme. No past papers are stored in
`me/papers/Computer_Science_0984/` yet.

## Questions

1. Data is broken down into packets before it is transmitted. State the **three** parts of a packet.
   [3]
2. State **three** items of data stored in a packet header. [3]
3. Describe the process of packet switching. [5]
4. Identify the method of data transmission described:
   (a) 8 bits are sent at the same time, in one direction only;
   (b) one bit is sent at a time, in both directions at the same time. [4]
5. A company connects a printer to a computer with a 4 m cable. Explain why serial transmission is
   more suitable than parallel. [2]
6. Explain why parallel transmission is used for data travelling between components inside a
   computer. [2]
7. Two friends talk using a video-calling app. Identify the most suitable direction of transmission
   and justify your choice. [2]
8. Give **one** advantage and **one** disadvantage of half-duplex compared with full-duplex. [2]
9. A digital camera is connected to a computer with a USB cable. Explain how USB is used to
   transmit the photos to the computer. [3]
10. Give **two** benefits and **two** drawbacks of the USB interface. [4]

## Marking guidance (not official)

1. Header · payload · trailer.
2. Any three: destination address · packet number · originator's (sender's) address.
3. One mark each, max 5: data broken down into packets · each packet sent independently / could
   take a different route · router controls/decides the route (using the destination address) ·
   packets may arrive out of order · once the last packet arrives, packets are reordered (using
   packet numbers).
4. (a) parallel [1] simplex [1] · (b) serial [1] full-duplex [1].
5. Bits cannot become skewed / arrive out of synchronisation over the 4 m [1]; fewer wires so
   cheaper / less interference [1].
6. Distance is very short, so skew is not a problem [1]; parallel sends several bits at once, so it
   is faster [1].
7. Full-duplex [1] — both people must send and receive (speak and hear) at the same time [1].
8. Advantage: cheaper / needs only one channel [1]. Disadvantage: slower — devices must take turns /
   wait for the channel [1].
9. Computer automatically detects the camera [1] · identifies it and loads the correct device
   driver [1] · photos sent serially along the data wires [1] (credit: error checking / re-send if an
   error is found).
10. Benefits (any two): automatic detection and driver loading · connector fits only one way ·
    industry standard, widely supported · supplies power · backward compatible.
    Drawbacks (any two): cable limited to about 5 m · slower than e.g. Ethernet · very old devices
    may not be supported.
