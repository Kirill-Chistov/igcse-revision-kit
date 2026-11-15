# Tracker

One page, two places to keep the data:

| | Local (default) | claude.ai artifact |
| --- | --- | --- |
| Runs | on your computer: `python3 tools/tracker/serve.py` → <http://localhost:8765> | in your Claude account, opens on your phone |
| Data | `me/progress.json`, `me/flashcards.json` | the artifact's database |
| Who can update it | you, and any AI agent working in this folder | you, and Claude |
| Needs | Python 3 (no packages) | a claude.ai account with artifacts |

The page has an **Overview** (progress bar per subject), a **Flashcards** tab (decks by subject,
reviews of at most 15 cards: Again / Got it, spaced 1-3-7-21-60 days) and one tab per subject: every
specification point with rounds R1, R2, … you rate *Don't know / Need more revision / Feel good*, plus
notes. Your AI tutor adds rounds and a few cards after each marked session.

Data formats: `rules/REVISION.md` § What gets saved.

## Local mode

```
python3 tools/tracker/serve.py           # open the printed address
python3 tools/tracker/record.py summary  # the same data from the command line
```

It listens on 127.0.0.1 only. Agents update the files with `record.py` (or by editing the JSON
carefully); the page reloads the data when you switch back to its tab.

## Artifact mode (Claude only)

Set up by `/setup`, or by asking Claude to "move my tracker to a claude.ai artifact":

1. `python3 tools/tracker/build.py --artifact` → `tools/tracker/dist/tracker.html` (your subjects'
   specification points embedded; no personal data in it).
2. Publish that file as a **new** artifact titled "Revision tracker" (Artifact tool / `publish_files`).
3. Declare the database so only you (and editors) can read or write it:
   `{"db": {"rules": [{"path": "", "read": "admin", "write": "admin"}]}}`.
4. Existing local data: `python3 tools/tracker/sync.py export`, then write each document in
   `dist/db_export.json` with `db_write` (path → body).
5. Put `tracker: artifact` and `tracker_url: <url>` in `me/profile.md`.

Database layout (same data as the local files):

| Document | Body |
| --- | --- |
| `progress/<Subject>` | `{ "points": { "<spec point>": { "h": [...], "note": "" } } }` |
| `decks/<Subject>__<NN>` | `{ "subject", "title", "cards": [...] }` |

To record a round: `db_get progress/<Subject>`, append `{r, d}` to the point's `h` (create the point
or the document if missing), `db_write` the whole document back. Cards: get the deck, apply the
flashcard rules (`rules/REVISION.md`), write it back. Read before every write — the student may have
rated something on their phone a minute ago.

Adding a subject later: rebuild the page with `build.py --artifact` and republish to the same
artifact (the database survives republishing).

Back to local: `db_list` both collections into a JSON list of `{path, data}`, then
`python3 tools/tracker/sync.py import <file>`.
