# Databases — summary (0984, 9.1–9.4)

- **Table** = all the data; **record** = one row (one item/person/event); **field** = one column
  (one item of data for every record). The field-name row is not a record.
- Field names: meaningful, one word, no spaces.
- **Data types:** text/alphanumeric · character (one character) · Boolean (TRUE/FALSE) ·
  integer (whole number) · real (decimal) · date/time. Phone numbers and ID codes → **text**;
  money → **real**.
- **Primary key:** a field that uniquely identifies each record — its value is never repeated,
  now or later. Usually an ID/code; if none exists, add one.
- **Defining a table:** table name → one field per data item → data type → primary key →
  validation (range, length, type, presence, format, check digit).
- **SQL query:**

```
SELECT <fields or *> FROM <table> WHERE <condition> ORDER BY <field> ASC | DESC;
```

- `AND` = both true; `OR` = at least one true; repeat the field each time
  (`Type = 'R' OR Type = 'H'`).
- `SUM(field)` = one total; `COUNT(*)` = number of records selected.
- Quotes round text, character and dates; not round numbers or TRUE/FALSE.
- **Output:** test each record against WHERE → keep only the SELECT fields, in SELECT order →
  sort by ORDER BY (ASC = A→Z, smallest first; DESC = Z→A, largest first).
