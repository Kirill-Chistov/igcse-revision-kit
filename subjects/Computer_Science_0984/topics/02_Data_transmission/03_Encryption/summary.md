# 2.3 Encryption — summary

**0984 · 2.3.1–2.3.2 · Paper 1**

- **Purpose:** intercepted data is meaningless without the key. Encryption does **not** stop
  interception.
- **Plaintext** → encryption algorithm + key → **ciphertext**; decryption reverses it.
- **Symmetric:** one key encrypts and decrypts. Weakness: the key must be sent and could be
  intercepted.
- **Asymmetric:** matching pair — **public key** (anyone; encrypts) and **private key** (owner only;
  decrypts). Receiver sends public key → sender encrypts with the **receiver's** public key →
  receiver decrypts with own private key. Private key is never sent.
