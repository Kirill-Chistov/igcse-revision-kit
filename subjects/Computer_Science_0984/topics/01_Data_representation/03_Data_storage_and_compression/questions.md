# Data storage and compression — Questions

| Field | Value |
| --- | --- |
| Specification points | 1.3.1–1.3.4 |
| Paper | Paper 1 — no calculator |

No past papers are stored in `me/papers/Computer_Science_0984/` yet. Marking guidance below is
written for this repository and is **not an official mark scheme**.

## 1. Recall

1. How many bits are in a nibble? In a byte?
2. Put in order, smallest first: GiB, KiB, EiB, TiB, MiB, PiB.
3. How many KiB are in 3 MiB?

## 2. Calculations

4. An image is 2048 × 1024 pixels with a colour depth of 8 bits. Calculate its size in MiB.
5. An image is 512 × 256 pixels with a colour depth of 24 bits. Calculate its size in KiB.
6. A 128-second sound file has a sample rate of 16 000 Hz and a sample resolution of 8 bits.
   Calculate its size in KiB.
7. How many 2 MiB images can be stored in 1 GiB?

## 3. Compression

8. Encode this row of pixels with RLE: WWWWBBWWWWWWWWBB. How many values are needed before and
   after?
9. Decode the RLE data 3R 2G 5B.
10. Explain why RLE is not effective on the text ABABABAB.
11. Give **two** lossy methods of reducing the size of a sound file.

## 4. Exam-style

12. **[3 marks]** *Explain* why files are compressed before they are sent over the internet.
13. **[4 marks]** A student compresses a text document before emailing it. *Identify* the type
    of compression that should be used and *explain* why.
14. **[4 marks]** *Describe* the difference between lossy and lossless compression.

## Answers and marking guidance

1. 4; 8.
2. KiB, MiB, GiB, TiB, PiB, EiB.
3. 3 × 1024 = **3072 KiB**.
4. 2048 × 1024 × 8 bits ÷ 8 = 2048 × 1024 bytes = 2048 KiB = **2 MiB**.
5. 512 × 256 × 24 ÷ 8 = 512 × 256 × 3 bytes; ÷ 1024 = 128 × 3 = **384 KiB**.
6. 16 000 × 8 × 128 ÷ 8 = 16 000 × 128 bytes; ÷ 1024 = 16 000 ÷ 8 = **2000 KiB**.
7. 1024 MiB ÷ 2 = **512**.
8. **4W 2B 8W 2B**; 16 values before, 8 after.
9. **RRRGGBBBBB**.
10. There are no runs: 1A 1B 1A 1B … needs **twice** as many values as the original.
11. Reduce the **sample rate**; reduce the **sample resolution**.
12. Reduces file size ✓; so less **bandwidth** is needed ✓; **shorter transmission time** /
    faster upload or download ✓ (also: less storage space).
13. **Lossless** ✓; the document must be **restored exactly** when decompressed ✓; lossy would
    **permanently remove data** ✓, so characters/words would be lost or changed ✓.
14. Lossy **permanently removes** data ✓; original **cannot** be restored ✓; lossless reduces
    size **without permanent loss** ✓; original **fully restored** ✓ (examples, e.g. RLE for
    lossless / reducing colour depth for lossy, may be credited).
