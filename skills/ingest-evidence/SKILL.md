---
name: ingest-evidence
description: Ingest meeting transcripts and evidence emails for project status reporting. Use when the user types /ingest-evidence or asks to ingest, load, or process meeting transcripts or emails for a status update project. This skill reads transcript files from the configured meetings source directory and emails from a configured Access-linked Outlook table, respects reporting period boundaries from project-config.md, and produces a verbatim evidence-notes-current.md file ready for extraction. Trigger on /ingest-evidence, "ingest evidence", "ingest meetings", "load meeting transcripts", "load emails", "process meeting minutes", or similar.
---

# ingest-evidence

Reads meeting transcript files and (optionally) evidence emails, and produces `evidence-notes-current.md` — a labelled, verbatim copy of both for the current reporting period.

**This skill does NOT extract action items, decisions, or issues.** That is `extract-and-verify`'s job. Stay in your lane: read files/records, label them, write them out verbatim, and hand off.

---

## Step 1 — Find the project root

Look for `project-config.md` in this order:
1. The current working directory
2. A `project/` subdirectory of the current working directory (i.e., `./project/project-config.md`)
3. Parent directories (walking upward)

Use the first match as the project root. If not found anywhere, ask the user: "Where is the project root? (I'm looking for project-config.md)"

Read `project-config.md` and extract:
- `Current Period Start` and `Current Period End`
- `Period Length (weeks)`
- `Start Date`
- `Meetings Source:` *(optional — defaults to `./meeting-minutes/` if absent)*
- `Email Evidence DB:` *(optional — path to an `.accdb` file with a linked Outlook table; skip email ingestion entirely if absent)*
- `Email Evidence Table:` *(optional — the linked table name to query, e.g. `project_status`; required if `Email Evidence DB:` is set)*

If `project-state.md` exists, read it and note `Last Completed Period` — you will use this to skip already-processed periods.

---

## Step 2 — Locate and scan meeting files

**Determine the meetings source path:**
- If `Meetings Source:` is present in project-config.md, use that path (resolved relative to the project root).
- Otherwise default to `./meeting-minutes/` under the project root.

**Scan for date folders:**
- Recurse through the source directory at any depth.
- A *date folder* is any folder whose name matches `YYYY-MM-DD` or `YYYY.MM.DD`.
- Non-date folders (e.g. `01_Infrastructure Team/`) are treated as organizational groupings — recurse into them but do not use their names as dates.
- The canonical meeting date is the name of the date folder, normalised to `YYYY-MM-DD`.

**Determine meeting type (Internal / External):**
- If both `internal/` and `external/` subdirectories exist directly under the source root → use them as the type label for all date folders beneath them.
- If only `internal/` exists (no `external/` subfolder) → meetings inside `internal/` are labeled **Internal**; root-level date folders are labeled **External**.
- Otherwise → label all meetings **External**.

**Select the transcript file within each date folder:**
Priority order (case-insensitive filename matching):
1. Any file containing `transcript` → prefer `.docx`, then `.txt`, then `.md`
2. Any file containing `summary` or `notes` → prefer `.docx`
3. Any remaining `.docx` or `.txt` file

Skip entirely: `.csv`, `.mp4`, `.mov`, `.png`, `.jpg`, `.jpeg`, `.xlsx`, `.pdf`

If multiple files match at the same priority level (e.g. two `*transcript*` docx files), read all of them.

Build a list of all meetings with: date, type (Internal/External), file path(s).

---

## Step 3 — Locate and scan evidence emails (if configured)

Skip this step entirely if `Email Evidence DB:` is not set in project-config.md.

**Technical method — use Access COM automation, not ODBC:**

`pyodbc` / raw ODBC connections to `.accdb` files with linked Outlook/Exchange tables are known to crash (native access violation) on this environment. Use `win32com.client` to drive the real Access application instead — the same engine that resolves the live MAPI-linked table:

```python
import win32com.client

app = win32com.client.Dispatch("Access.Application")
# If the target file is already open in a running Access instance, Dispatch()
# reuses that session — CurrentDb() works directly, do NOT call OpenCurrentDatabase
# again (it raises "You already have the database open.").
try:
    db = app.CurrentDb()
    if db.Name.lower() != email_db_path.lower():
        raise Exception("different db open")
except Exception:
    app.OpenCurrentDatabase(email_db_path)
    db = app.CurrentDb()

rs = db.OpenRecordset(
    f"SELECT [Received], [From], [Sender Name], [To], [CC], [Subject], [Contents] "
    f"FROM [{table_name}] "
    f"WHERE [Received] >= #{period_start}# AND [Received] < #{period_end}# "
    f"ORDER BY [Received] ASC"
)
emails = []
while not rs.EOF:
    emails.append({
        "received": rs.Fields("Received").Value,
        "from": rs.Fields("From").Value,
        "sender_name": rs.Fields("Sender Name").Value,
        "to": rs.Fields("To").Value,
        "cc": rs.Fields("CC").Value,
        "subject": rs.Fields("Subject").Value,
        "body": rs.Fields("Contents").Value,
    })
    rs.MoveNext()
rs.Close()
```

Only close/quit the Access application (`app.CloseCurrentDatabase()` / `app.Quit()`) if this skill was the one that opened it (i.e., it wasn't already open when the skill started). Leave a pre-existing user session alone.

**If the linked table isn't visible yet:** Access resolves linked Outlook/Exchange tables through the classic MAPI folder cache. If the query fails or the table can't be found, tell the user:

```
⚠️  Could not read [Email Evidence Table] from [Email Evidence DB].
This is usually a stale MAPI folder cache — try fully closing and
reopening Outlook, then retry.
```

Do not silently skip emails on failure — surface the error and stop, since a missing email source is a data gap, not a "no emails this period" result.

Build a list of all emails with: date (`Received`), subject, from/to/cc, and body — already filtered to the current period's date range (the query does this).

---

## Step 4 — Compute period boundaries and determine what to process

Compute all reporting periods from `Start Date` using `Period Length (weeks)`:
- Period 1: Start Date → Start Date + Period Length
- Period 2: Start Date + Period Length → Start Date + (2 × Period Length)
- …and so on until today

Match each meeting to its period by date, and (if configured) each email to its period by `Received` date. Period boundaries are inclusive-start, exclusive-end (an item on the period end date belongs to the next period).

**Resume logic:** If `project-state.md` exists and has a `Last Completed Period`, skip all periods up to and including that period.

**Multi-period detection:** If evidence (meetings and/or emails combined) spans more than one unprocessed period:
1. Report the situation clearly before doing anything:
   ```
   Found [N] meeting(s) and [N] email(s) across [N] periods:
   • Period [id] ([start] → [end]): [N] meeting(s), [N] email(s)
   • Period [id] ([start] → [end]): [N] meeting(s), [N] email(s)
   ...
   Processing oldest unprocessed period first: [period-id]
   ```
2. Process **only the oldest unprocessed period** in this run.
3. After completing this run, tell the user to run `/extract-and-verify` and then `/generate-report` and `/period-rollover` for this period before running `/ingest-evidence` again for the next.

**Future period check:** After determining the oldest unprocessed period to process, check whether its `Current Period Start` is after today. If the target period hasn't started yet, stop without scanning or writing any files:

```
⚠️  The current period ([period-id]) starts [Current Period Start], which is in the future (today is [today]).
No evidence can exist yet for this period.

If you rolled over early, wait until [Current Period Start] before running /ingest-evidence.
```

If no meetings and no emails fall in any unprocessed period, say so clearly and stop.

---

## Step 5 — Read and write evidence-notes-current.md

For each meeting and email in the target period, ordered chronologically (oldest to newest, interleaved):

**Meetings** — read the transcript file verbatim and write:

```markdown
## [Internal|External] Meeting — [YYYY-MM-DD]
**File:** [relative path to transcript file]

[full verbatim transcript content]

---
```

**Emails** — write the body verbatim with header metadata:

```markdown
## Email — [YYYY-MM-DD] — [Subject]
**From:** [Sender Name] <[From]>
**To:** [To]
**CC:** [CC, or omit if blank]

[full verbatim email body]

---
```

Write `evidence-notes-current.md` to the project root (overwriting if it exists). Include a file header:

```markdown
# Evidence Notes — [Project Name]
**Period:** [period-id] ([start] → [end])
**Generated:** [today's date]
**Meetings:** [N internal], [N external]
**Emails:** [N] (or omit this line if no Email Evidence DB configured)

---
```

Do NOT summarise, restructure, or extract anything from the transcripts or emails. Reproduce the text exactly as found in the source.

---

## Step 6 — Hand off

Print a brief summary and prompt:

```
✓ evidence-notes-current.md written.

Period: [period-id] ([start] → [end])
Meetings: [N internal], [N external]
Emails: [N]

Run /extract-and-verify to proceed.
```

If multiple unprocessed periods remain, remind the user:
```
Note: [N] additional period(s) found after this one. Complete the full
workflow for this period (/extract-and-verify → /generate-report →
/period-rollover) before running /ingest-evidence again.
```

Do NOT run `/extract-and-verify` automatically. The user must trigger it.
