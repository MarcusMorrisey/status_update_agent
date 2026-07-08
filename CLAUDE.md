# Status Update Agent — PCFS Custom-CMS

This workspace hosts the status update agent plugin for the PCFS Custom-CMS project.

## Project Root

All project files live under `./project/`. When any skill references "the project root", that means `./project/` relative to this directory.

Key files:
- `./project/project-config.md` — project identity, schedule, and reporting settings
- `./project/project-state.md` — persistent state: milestones, action items, issues, return-to-green plans
- `./project/evidence-notes-current.md` — working file: verbatim ingested transcripts and emails for the current period
- `./project/extractions-current.md` — working file: verified extractions awaiting report generation
- `./project/status-reports/` — generated Quarto `.qmd` reports (one per period)
- `./project/_templates/report-template.docx` — Word reference doc for Quarto rendering
- `./project/project-docs/` — source documents (SOWs, plans, architecture)

## Meeting Minutes Structure

Meeting transcripts are sourced from the network drive — **not** the local `./project/01. Meeting Minutes/` folder:

**Source path:** `Z:\Shared\3_Client Projects\Peguis CFS\Projects\PD25-1186-CO - Custom CMS\4. Controlling\01. Meeting Minutes`

The folder uses a mixed structure:
- Root-level `YYYY-MM-DD` date folders → **External** meetings
- `internal\` subfolder with `YYYY.MM.DD` date folders → **Internal** meetings

There is no `external/` subfolder — external meetings sit directly under the source root.

## Email Evidence Source

As of 2026-07-08, `/ingest-evidence` also pulls emails as evidence, configured via `Email Evidence DB:` / `Email Evidence Table:` in `project-config.md`:

- **DB path:** `Z:\Shared\3_Client Projects\Peguis CFS\Projects\PD25-1186-CO - Custom CMS\2. Planning\R\email_repo\PCFS.accdb` (UNC: `\\EgnyteDrive\idfusion\Shared\...`)
- **Linked table:** `project_status` — a live Outlook-linked table pointing at `Inbox\PCFS\CMS\project_status` (marcus.morrisey@idfusion.com mailbox)

**Technical note:** Direct `pyodbc`/ODBC connections to this `.accdb` crash the Python process (native access violation) on this machine — cause unconfirmed, possibly a Python 3.14 / Access driver compatibility issue. Use `win32com.client` COM automation against the real Access application instead (see `skills/ingest-evidence/SKILL.md` Step 3) — this is what actually resolves the live MAPI-linked table content, and it works reliably. A pure-Python file parser (`access_parser`) can open the `.accdb` file directly but **cannot** see linked-table content at all (it only sees physically stored tables), so it's useless for this source.

If new email evidence tables are linked in this database in the future (currently only `project_status` exists), update `Email Evidence Table:` in `project-config.md` accordingly — the skill currently only reads one configured table.

## Workflow

Run these skills in order each reporting period:

1. `/ingest-evidence` — reads transcript files and evidence emails, writes `evidence-notes-current.md`
2. `/extract-and-verify` — extracts structured items, presents for user approval, writes `extractions-current.md`
3. `/generate-report` — produces `status-reports/[period-id].qmd`
4. `/period-rollover` — merges state, advances period dates, clears working files

Run `/ingest-project-docs` once at project start or when new project documents arrive — not every period.

## Current State (as of last rollover)

- Skill renamed 2026-07-08: `ingest-meetings` → `ingest-evidence` (now also ingests emails from the Access DB above; see Email Evidence Source). `meeting-notes-current.md` renamed to `evidence-notes-current.md` everywhere.
- Reporting cadence changed 2026-07-08: **Period Length is now 1 week** (was 2). The in-progress 2026-W29 period was truncated from 07-03→07-16 to 07-03→07-09 as part of this change (nothing had been ingested for it yet, so no data needed splitting). The week of 07-10→07-16 will be its own period (W30) once rolled into.
- Last completed period: 2026-W27 (2026-06-19 → 2026-07-02)
- Current period: 2026-W29 (2026-07-03 → 2026-07-09)
- `evidence-notes-current.md` contains stale W27 meeting notes only (pre-rename content, no emails) — W29 ingest not yet run
- `extractions-current.md` is empty — next step is `/ingest-evidence` for W29
- `Email Evidence DB:` / `Email Evidence Table:` not yet added to `project-config.md` — do this before the next `/ingest-evidence` run if emails should be included in W29
- No known W29 meetings yet — check Z: drive when starting next period
