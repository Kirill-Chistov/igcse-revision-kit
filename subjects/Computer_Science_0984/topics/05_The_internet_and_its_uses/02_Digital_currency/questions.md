# 5.2 Digital currency — practice

Cambridge IGCSE (9–1) Computer Science 0984 · points 5.2.1–5.2.2 · Paper 1

No past papers are stored in `me/papers/Computer_Science_0984/` yet. The marking guidance below
is written for this repository and is **not an official Cambridge mark scheme**.

## Questions

1. State what is meant by a digital currency. **[1]**
2. Describe **two** ways digital currency can be used. **[2]**
3. State what is meant by a blockchain. **[2]**
4. Identify **three** items stored in each block of a blockchain. **[3]**
5. Explain how a blockchain is used to track digital currency transactions. **[5]**
6. A blockchain has five blocks. A criminal changes the amount in block 3. Explain why the change
   would be detected. **[3]**

## Marking guidance

1. A currency that only exists electronically / has no physical form (1).
2. Any two: paying for goods or services; transferring / sending money electronically between
   accounts or digital wallets; online or in-app payment.
3. A digital ledger (1) — a time-stamped series of records that cannot be altered (1).
4. Any three: transaction data (sender, recipient, amount); timestamp; hash of the block; hash of
   the previous block.
5. Any five: decentralised — every computer in the network holds a copy; each transaction is stored
   as a new block; block includes a timestamp; block has its own hash; block stores the previous
   block's hash, linking the chain; new block is sent to every computer and checked; added to every
   copy, so the transaction is permanently recorded and can be traced; records cannot be altered.
6. Changing block 3 changes its hash (1); block 4's previous hash no longer matches (1); the chain
   is broken so the change is detected / blocks 4 and 5 become invalid (1).
