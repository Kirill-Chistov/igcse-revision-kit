# 2.3 Encryption — questions

**0984 · 2.3.1–2.3.2 · Paper 1.** Exam-style practice. The marking guidance is written for this
repository and is **not** an official Cambridge mark scheme. No past papers are stored in
`me/papers/Computer_Science_0984/` yet.

## Questions

1. Explain why data should be encrypted before it is transmitted over the internet. [2]
2. State what is meant by **plaintext** and **ciphertext**. [2]
3. Describe how symmetric encryption is used to send data, and give its main drawback. [3]
4. Tom wants to send Jane a confidential document using asymmetric encryption. Describe how the
   document is encrypted and decrypted. [4]
5. Explain why asymmetric encryption is more secure than symmetric encryption. [2]
6. Jane now wants to send an encrypted reply to Tom. State what must happen first. [2]
7. A student says: "Encrypting my data means nobody can intercept it." Explain why the student is
   wrong. [2]

## Marking guidance (not official)

1. Data could be intercepted (by a hacker) during transmission [1]; encryption makes it
   meaningless/unreadable to anyone without the key [1].
2. Plaintext: the original, readable data before encryption [1]. Ciphertext: the unreadable data
   produced by encryption [1].
3. The same key is used to encrypt and decrypt [1]; the receiver must be given a copy of the key [1].
   Drawback: the key could be intercepted while it is being sent, and then used to decrypt the data
   [1].
4. Jane generates a matching public/private key pair [1] · Jane sends her public key to Tom [1] · Tom
   encrypts the document with Jane's public key and sends the ciphertext [1] · Jane decrypts it with
   her private key [1].
5. The private key is never transmitted, so it cannot be intercepted [1]; the public key can only
   encrypt, so intercepting it does not let anyone decrypt the data [1].
6. Tom must generate his own key pair [1] and send his public key to Jane (who encrypts with it) [1].
7. Encryption does not stop data being intercepted [1]; it only makes intercepted data meaningless
   without the key [1].
