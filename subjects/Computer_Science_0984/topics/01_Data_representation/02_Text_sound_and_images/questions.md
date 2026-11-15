# Text, sound and images — Questions

| Field | Value |
| --- | --- |
| Specification points | 1.2.1–1.2.3 |
| Paper | Paper 1 |

No past papers are stored in `me/papers/Computer_Science_0984/` yet. Marking guidance below is
written for this repository and is **not an official mark scheme**.

## 1. Recall

1. What is a character set?
2. Define *sample rate* and *sample resolution*.
3. Define *resolution* and *colour depth* for an image.

## 2. Understanding

4. Give **two** differences between ASCII and Unicode.
5. A sound is recorded with a 4-bit sample resolution. How many different amplitude values can
   be stored?
6. How many colours can be represented with a colour depth of 8 bits?
7. The ASCII code for C is 67. Give the code for G in denary and in 7-bit binary.

## 3. Application

8. A company's website is published in English, Arabic and Japanese. Explain why it uses Unicode
   rather than ASCII.
9. A photographer changes the colour depth of an image from 8 bits to 16 bits. Describe the
   effect on the image and on its file size.
10. A music app lowers the sample rate of a song to save space. Explain the effect on the
    recording.

## 4. Exam-style

11. **[4 marks]** *Describe* how a computer represents a sound as binary.
12. **[3 marks]** *Explain* how a computer represents an image, including the effect of
    increasing its resolution.

## Answers and marking guidance

1. A defined list of characters, each with a **unique binary code**.
2. Sample rate: number of samples taken **per second**. Sample resolution: number of **bits
   per sample**.
3. Resolution: **number of pixels** in the image. Colour depth: **number of bits** used to
   represent each colour.
4. Any two: Unicode uses **more bits per character** ✓; Unicode represents a **greater range of
   characters** ✓, e.g. other languages / emojis ✓; ASCII 7-bit / 128 characters ✓.
5. 2⁴ = **16**.
6. 2⁸ = **256**.
7. G = 71 → **1000111**.
8. ASCII only covers English characters ✓; Unicode has a greater range, including other
   languages' characters such as Arabic and Japanese ✓.
9. More colours can be shown (65 536 instead of 256), so image quality/realism increases ✓;
   file size increases (doubles) ✓.
10. Fewer samples per second ✓, so the recording is less accurate / less like the original
    sound ✓ (file size decreases).
11. Sound wave is **sampled** ✓; **amplitude** measured ✓ at **regular time intervals** ✓;
    each sample stored as a **binary** number ✓; sample rate / resolution defined ✓ (max 4).
12. Image made of **pixels** ✓; each pixel's colour stored as a **binary** code ✓; higher
    resolution = more pixels → more detail / quality ✓ and larger file size ✓ (max 3).
