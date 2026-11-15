# Databases — practice questions (0984, 9.1–9.4)

No Cambridge past papers are stored in `me/papers/Computer_Science_0984/` yet. The marking
guidance below is written for this repository and is **not an official mark scheme**.

Questions 1–10 use this table.

**Table: CLUB**

| MemberID | Surname | Gender | Age | Fee | Junior | JoinDate |
| --- | --- | --- | --- | --- | --- | --- |
| M101 | Okafor | F | 15 | 30.00 | TRUE | 12/09/2024 |
| M102 | Silva | M | 42 | 55.50 | FALSE | 03/01/2023 |
| M103 | Chen | F | 16 | 30.00 | TRUE | 21/06/2025 |
| M104 | Novak | M | 38 | 55.50 | FALSE | 14/02/2022 |
| M105 | Silva | F | 13 | 25.00 | TRUE | 30/08/2025 |
| M106 | Patel | M | 17 | 30.00 | TRUE | 05/05/2024 |

## Questions

1. State the number of fields and the number of records in CLUB. **[2]**
2. Suggest the most suitable data type for `Gender`, `Age`, `Fee` and `Junior`. **[4]**
3. Identify the primary key of CLUB and explain why `Surname` would not be a suitable primary
   key. **[2]**
4. The club adds a field `PhoneNumber`. State its data type and give a reason. **[2]**
5. Suggest a suitable validation check for `Age`, for `MemberID` and for `Surname`. Describe each
   check. **[3]**
6. Give the output of:

   ```
   SELECT Surname, Age
   FROM CLUB
   WHERE Junior = TRUE AND Fee = 30.00
   ORDER BY Age DESC;
   ```
   **[3]**
7. Give the output of:

   ```
   SELECT MemberID
   FROM CLUB
   WHERE Gender = 'M' OR Age < 14;
   ```
   **[2]**
8. Give the output of `SELECT COUNT(*) FROM CLUB WHERE Fee > 28.00;` and of
   `SELECT SUM(Fee) FROM CLUB WHERE Junior = FALSE;` **[2]**
9. Complete the script to show the surname and join date of every female member, in
   alphabetical order of surname. **[4]**

   ```
   SELECT Surname, ..........
   FROM ..........
   WHERE ..........
   ORDER BY ..........;
   ```
10. Write an SQL query to show the `MemberID` and `Age` of every member aged 16 or over who pays
    less than 50.00. **[4]**
11. This query should show the surname and age of every member older than 15 or younger than 13.
    Identify and correct **three** errors. **[3]**

    ```
    SELECT Surname Age
    FROM CLUB
    WHERE Age > 15 OR < 13
    ```
12. A library needs to store, for each book: its ISBN (13 digits, unique to each book), the title,
    the number of pages, the price, whether it is on loan and the date it was added. Define a
    single-table database for this: give the table name, a field name and data type for each
    item, the primary key and one validation check. **[6]**

## Marking guidance (not official)

1. 7 fields (1); 6 records (1).
2. Gender — character; Age — integer; Fee — real; Junior — Boolean (1 each).
3. `MemberID` (1); surnames can repeat — e.g. two members are called Silva — so it does not
   uniquely identify a record (1).
4. Text (1); it may start with 0 / contain spaces or `+` / is not used in calculations (1).
5. Any three, one mark each, check named **and** applied to the field:
   Age — range check, e.g. between 5 and 100 / type check, whole number only;
   MemberID — format check, `M` followed by three digits / length check, exactly 4 characters /
   presence check;
   Surname — presence check, must not be left blank / length check, e.g. at most 30 characters.
6. Records kept: M101, M103, M106 (1); only Surname and Age shown (1); in order
   Patel 17, Chen 16, Okafor 15 (1).
7. M102, M104, M105, M106 — all four (2); three correct with none wrong (1).
8. 5 (1); 111.00 (1).
9. `JoinDate` (1); `CLUB` (1); `Gender = 'F'` (1); `Surname` or `Surname ASC` (1).
   (Output would be Chen, Okafor, Silva.)
10. `SELECT MemberID, Age` (1) `FROM CLUB` (1) `WHERE Age >= 16` (1) `AND Fee < 50.00;` (1).
    (Output: M103 16, M106 17.)
11. Comma missing: `SELECT Surname, Age` (1); field not repeated: `WHERE Age > 15 OR Age < 13`
    (1); missing `;` at the end (1).
12. Table name, e.g. `BOOK` (1). Fields with suitable types — `ISBN` text, `Title` text,
    `Pages` integer, `Price` real, `OnLoan` Boolean, `DateAdded` date/time (up to 3: all six
    correct = 3, four or five = 2, two or three = 1). Primary key `ISBN` (1). One validation
    check named and applied, e.g. length check on ISBN — exactly 13 characters /
    range check on Pages — greater than 0 (1).
