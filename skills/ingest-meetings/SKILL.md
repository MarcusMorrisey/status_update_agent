---
name: ingest-meetings
description: Ingest meeting transcripts for project status reporting. Use when the user types /ingest-meetings or asks to ingest, load, or process meeting transcripts for a status update project. This skill reads transcript files from the configured meetings source directory, respects reporting period boundaries from project-config.md, and produces a verbatim meeting-notes-current.md file ready for extraction. Trigger on /ingest-meetings, "ingest meetings", "load meeting transcripts", "process meeting minutes", or similar.
---

# ingest-meetings

Reads meeting transcript files and produces `meeting-notes-current.md` — a labelled, verbatim copy of the transcripts for the current reporting period.

**This skill does NOT extract action items, decisions, or issues.** That is `extract-and-verify`'s job. Stay in your lane: read files, label them, write them out verbatim, and hand off.

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

## Step 3 — Compute period boundaries and determine what to process

Compute all reporting periods from `Start Date` using `Period Length (weeks)`:
- Period 1: Start Date → Start Date + Period Length
- Period 2: Start Date + Period Length → Start Date + (2 × Period Length)
- …and so on until today

Match each meeting to its period by date. Period boundaries are inclusive-start, exclusive-end (a meeting on the period end date belongs to the next period).

**Resume logic:** If `project-state.md` exists and has a `Last Completed Period`, skip all periods up to and including that period.

**Multi-period detection:** If meetings span more than one unprocessed period:
1. Report the situation clearly before doing anything:
   ```
   Found [N] meetings across [N] periods:
   • Period [id] ([start] → [end]): [N] meeting(s)
   • Period [id] ([start] → [end]): [N] meeting(s)
   ...
   Processing oldest unprocessed period first: [period-id]
   ```
2. Process **only the oldest unprocessed period** in this run.
3. After completing this run, tell the user to run `/extract-and-verify` and then `/generate-report` and `/period-rollover` for this period before running `/ingest-meetings` again for the next.

If no meetings fall in any unprocessed period, say so clearly and stop.

---

## Step 4 — Read and write meeting-notes-current.md

For each meeting in the target period (oldest to newest):

1. Read the transcript file verbatim.
2. Write it to `meeting-notes-current.md` with this header format:

```markdown
## [Internal|External] Meeting — [YYYY-MM-DD]
**File:** [relative path to transcript file]

[full verbatim transcript content]

---
```

Write `meeting-notes-current.md` to the project root (overwriting if it exists). Include a file header:

```markdown
# Meeting Notes — [Project Name]
**Period:** [period-id] ([start] → [end])
**Generated:** [today's date]
**Meetings:** [N internal], [N external]

---
```

Do NOT summarise, restructure, or extract anything from the transcripts. Reproduce the text exactly as found in the source file.

---

## Step 5 — Hand off

Print a brief summary and prompt:

```
✓ meeting-notes-current.md written.

Period: [period-id] ([start] → [end])
Meetings: [N internal], [N external]

Run /extract-and-verify to proceed.
```

If multiple unprocessed periods remain, remind the user:
```
Note: [N] additional period(s) found after this one. Complete the full
workflow for this period (/extract-and-verify → /generate-report →
/period-rollover) before running /ingest-meetings again.
```

Do NOT run `/extract-and-verify` automatically. The user must trigger it.
