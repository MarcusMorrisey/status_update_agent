# Status Update Agent — PCFS Custom-CMS

This workspace hosts the status update agent plugin for the PCFS Custom-CMS project.

## Project Root

All project files live under `./project/`. When any skill references "the project root", that means `./project/` relative to this directory.

Key files:
- `./project/project-config.md` — project identity, schedule, and reporting settings
- `./project/project-state.md` — persistent state: milestones, action items, issues, return-to-green plans
- `./project/meeting-notes-current.md` — working file: verbatim ingested transcripts for the current period
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

## Workflow

Run these skills in order each reporting period:

1. `/ingest-meetings` — reads transcript files, writes `meeting-notes-current.md`
2. `/extract-and-verify` — extracts structured items, presents for user approval, writes `extractions-current.md`
3. `/generate-report` — produces `status-reports/[period-id].qmd`
4. `/period-rollover` — merges state, advances period dates, clears working files

Run `/ingest-project-docs` once at project start or when new project documents arrive — not every period.

## Current State (as of last rollover)

- Last completed period: 2026-W27 (2026-06-19 → 2026-07-02)
- Current period: 2026-W29 (2026-07-03 → 2026-07-16)
- `meeting-notes-current.md` contains W27 notes (now stale — W29 ingest not yet run)
- `extractions-current.md` is empty — next step is `/ingest-meetings` for W29
- No known W29 meetings yet — check Z: drive when starting next period
