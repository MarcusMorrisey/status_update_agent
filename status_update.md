# Project Status Agent — Design Document
**Last Updated:** 2026-03-09
**Status:** Skill Architecture — In Progress
---
## Overview
Building a rapid prototype of an agent with associated skills to summarize project status. The agent should represent a well-trained systems analyst and project manager. Primary context: meeting transcriptions/summaries and planning documents. Output: well-structured Markdown optimised for rendering to Word or PPTX via Quarto.
---
## Core Workflow
1. Ingest and label meeting transcripts and planning documents
2. Extract progress updates, decisions, commitments, issues, and health indicators
3. Present all extractions to user as a full list for verification (approve / reject / merge / simplify)
4. Track and roll over unresolved items across reporting periods
5. Generate structured Quarto `.qmd` output per reporting period
6. Persist project state between periods
---
## All Decisions Log
| # | Decision | Detail |
|---|----------|--------|
| 1 | Project types | Software dev, IT consulting, digital strategy roadmaps, vendor assessments |
| 2 | Agent persona | Well-trained systems analyst and project manager |
| 3 | Primary input formats | Word docs (Teams auto-transcripts primary); also PDF, plaintext, others |
| 4 | Input labelling | Documents should be well-labelled; separate ingestion/labelling sub-process needed |
| 5 | Commitment detection | Liberal / overdetect; any stated intention qualifies; always verify with user before proceeding |
| 6 | Verification style | Full list presented at once; user can approve, reject, merge, or simplify |
| 7 | Milestone plan | Accept formal plan if provided or detected and verified; otherwise construct incrementally |
| 8 | Reporting period | 1–2 weeks default, configurable per project |
| 9 | Period memory | Agent remembers previous period; incomplete items roll over automatically |
| 10 | Output format | Quarto (.qmd) → Word (.docx) primary; Markdown also suitable for PPTX rendering |
| 11 | Deployment | Claude Code (primary); Claude.ai (secondary); Git-based saving preferred in Claude Code |
| 12 | Users | Solo for now; user is comfortable authoring Markdown and YAML |
| 13 | Financial Summary | Manual field; optional — omit section if unused; always CAD; four fields: Budget, Expensed, Estimated Remaining, Overage |
| 14 | Client's Feeling | Agent infers from transcript language/tone; always verified with user before inclusion |
| 15 | Decisions vs. Action Items | Agent distinguishes these during extraction; not expected to be labelled in source docs |
| 16 | Return to Green Plan | AI-generated per triggered RAG indicator (not one general box); one plan per Yellow/Red item; user verifies; carries forward until resolved |
| 17 | Progress This Period | Bullet list format |
| 18 | Empty sections | Always present; explicit "No [x] this period" placeholder — never silently omitted |
| 19 | Report section variation by project type | No — all 10 sections always present for all project types |
| 20 | Folder structure | See Input Folder Structure below |
| 21 | Project documents | Separate ingestion process from meeting minutes |
| 22 | Contradictions between documents | Agent flags conflict and presents both versions to user for resolution during verification pass |
| 23 | Git workflow | Prompt user to commit at end of period — no auto-commit; fits solo workflow |
| 24 | Per-project config | Markdown file (`project-config.md`); schema locked — see Per-Project Config Schema section |
| 25 | `ingest-evidence` trigger | Manually triggered via `/ingest-evidence` — not auto-run on session start |
| 26 | Project state file format | Markdown — human-readable, editable directly, consistent with git workflow |
| 27 | Verification flow | Single full-list pass — user reviews all extracted items at once; approve / reject / merge / simplify |
| 28 | `ingest-project-docs` trigger | On-demand only — run once at project start, then when new documents arrive; not re-run every period |
| 33 | Quarto reference-doc | User has branded `.docx`; stored at `_templates/report-template.docx`; path relative to project root |
| 34 | Quarto frontmatter fields | title, subtitle, date, author, client, docket — all auto-populated by `generate-report`; toc: false; number-sections: false |
| 35 | Milestones Gantt | Mermaid gantt rendered in `.qmd` below the milestones table; two milestone markers per row (Baseline + Estimated); always shown when milestones exist; no config toggle |
| 29 | Project state file — scope | Split: `project-state.md` = persistent carry-forward only; `extractions-current.md` = current-period working area (temp, cleared by `period-rollover`) |
| 30 | Project state — history window | Rolling 4-week window (metadata + brief summary per period); full history available in git + `.qmd` files |
| 31 | Milestone baselines | Stored in `project-state.md`; Baseline End is immutable to agent — agent may propose changes, user must confirm before state is updated; Estimated End is agent-writable (after verification) |
| 32 | Action item / issue IDs | Stable sequential IDs across periods — `A-001` format for action items, `I-001` for issues; assigned during `extract-and-verify`; state file tracks next available ID |
| 36 | `ingest-evidence` scope | Scans ALL meetings regardless of date; computes period boundaries from `Start Date` + `Period Length` in config; if meetings span multiple periods, processes iteratively from oldest to newest — full workflow per period (ingest → extract+verify → generate → rollover); pauses between periods for user verification; if `project-state.md` exists, resumes from last completed period |
| 37 | Evidence sources beyond meetings | 2026-07-08: `ingest-meetings` renamed to `ingest-evidence`; `meeting-notes-current.md` renamed to `evidence-notes-current.md`. Evidence now includes emails pulled from a linked Outlook table in an Access `.accdb`, configured per-project via `Email Evidence DB:` / `Email Evidence Table:` in `project-config.md` (optional — skipped if absent). Access COM automation (`win32com.client`) is required to read linked-table content reliably; direct ODBC (`pyodbc`) crashes on this environment. |
---
## Input Folder Structure
```
{project-root}/
├── _templates/
│   └── report-template.docx      # branded Word reference document for Quarto
├── project-config.md             # project identity, schedule, reporting settings, financial
├── project-state.md              # persistent state: milestones, action items, issues, Return to Green plans, period history
├── extractions-current.md        # temp: current-period verified extractions; cleared by period-rollover
├── meeting-minutes/
│   ├── internal/
│   │   └── 2026.02.15/
│   │       └── transcript.docx   # (or .pdf, .txt, etc.)
│   └── external/
│       └── 2026.02.15/
│           └── transcript.docx
├── project-docs/                 # separate ingestion process
│   └── (plans, SOWs, roadmaps, vendor assessments, etc.)
└── status-reports/               # agent output
    └── 2026-W07.qmd              # one file per reporting period
```
**Ingestion rules:**
- Agent reads all files under `meeting-minutes/internal/` and `meeting-minutes/external/`
- Subfolder name (`yyyy.mm.dd`) is the canonical meeting date — agent does not rely on file metadata
- `internal` vs `external` distinction is preserved as meeting context (affects tone inference for Client's Feeling)
- `project-docs/` is a separate skill/process — not auto-ingested with meeting minutes
- Agent only processes files within the current reporting period unless doing a rollover check
---
## Template Analysis — IDFusion Source Template
### Extracted Fields
**Report Header:** Reporting Date
**Project Details:** Client, Project Name, Project Docket #, Project Manager / Lead
**Status Dates:** Start Date, Planned Finish Date, Estimated Finish Date
**Health Report** *(each is a Red / Yellow / Green indicator):*
Overall Health, Schedule, Scope, Budget, Client's Feeling
**Project Financial Summary:** Project Budget, Expensed, Estimated Remaining, Overage
**Status Summary:** Project Status (narrative), Milestones table (Milestone | Status | Estimated End)
**Why Yellow or Red Status?** *(conditional narrative)*
**Return to Green Plan** *(conditional narrative — one general box in original)*
**Issues Table:** Description, Status, Potential Action Items
### Gaps Identified vs. Option A
1. No "Progress This Period" section
2. Action Items weak — no owner, no due date, buried under Issues
3. No "Decisions Made" section
4. No "Next Period Plan" section
5. Issues table lacks severity, owner, due date
6. Milestones table lacks baseline date for variance tracking
7. Return to Green is one general box — redesigned to be per-indicator
---
## Proposed Report Structure (v1) — LOCKED
| # | Section | Agent Role | Format |
|---|---------|------------|--------|
| 1 | Report Header | Metadata / manual | Fields |
| 2 | Health Dashboard | Infer → verify | RAG per indicator |
| 3 | Project Status & Dates | Extract; financials manual/optional | Fields + optional table |
| 4 | Progress This Period | Extract → verify | Bullet list |
| 5 | Milestones & Schedule | Track with variance → verify | Table + Mermaid Gantt |
| 6 | Decisions Made | Extract → verify | Table |
| 7 | Action Items & Commitments | Over-detect → verify; roll over | Table |
| 8 | Issues & Risks | Extract → verify | Table |
| 9 | Return to Green Plans | Generate per Yellow/Red indicator → verify; carry forward until resolved | Subsections per indicator |
| 10 | Next Period Plan | Propose → verify | Bullet list |
**Section table schemas:**
- **Section 5 Milestones:** Milestone | Baseline End | Estimated End | Status | Variance; followed by Mermaid Gantt (see below)
- **Section 6 Decisions:** Decision | Made By | Date | Notes
- **Section 7 Action Items:** # | Owner | Item | Due Date | Status | Carried Over?
- **Section 8 Issues:** # | Description | Severity | Owner | Due Date | Status

**Section 5 Gantt spec:**
Rendered as a Mermaid milestone chart immediately after the milestones table. Uses milestone markers (point-in-time, not bars) since only end dates are tracked. Two markers per milestone: Baseline End and Estimated End. Mermaid status mapped from milestone Status field:
- Complete → `:milestone, done,`
- On Track → `:milestone,`
- At Risk → `:milestone, crit,`
- Delayed → `:milestone, crit,`

Example output:
````markdown
```{mermaid}
gantt
  title Milestone Schedule
  dateFormat YYYY-MM-DD
  section Discovery Complete
    Baseline  :milestone, 2026-02-28, 0d
    Estimated :milestone, done, 2026-03-07, 0d
  section Beta Release
    Baseline  :milestone, 2026-04-30, 0d
    Estimated :milestone, crit, 2026-05-14, 0d
```
````
Omit Gantt entirely if the Milestones table has no rows.
---
## Proposed Skill Architecture (v1) — LOCKED
| # | Skill | Trigger | Responsibility |
|---|-------|---------|---------------|
| 1 | `ingest-evidence` | Manual: `/ingest-evidence` | Read all transcript files for current period; parse, label, store structured notes |
| 2 | `ingest-project-docs` | Manual: `/ingest-project-docs`; on-demand only | SOWs, plans, roadmaps, vendor docs; extract milestones, scope, budget baseline |
| 3 | `extract-and-verify` | Runs after ingestion | Extract progress, decisions, commitments, issues; infer health + Client's Feeling; present single full list for user verification |
| 4 | `generate-report` | Manual: `/generate-report` | Takes verified extractions + previous period state; produces Quarto `.qmd` output |
| 5 | `period-rollover` | Manual: `/period-rollover` | Carry forward unresolved items, Return to Green plans, open action items; update project state file |
**Verification principle (applies to all skills):** Single full-list pass — user approves, rejects, merges, or simplifies. Agent never writes to final output without explicit user sign-off.
---
## Per-Project Config Schema — LOCKED

File: `project-config.md` (Markdown, human-readable, directly editable)

### Template

```markdown
# Project Config — [Project Name]

## Project Identity
- **Client:** Acme Corp
- **Project Name:** Digital Platform Modernisation
- **Docket #:** AC-2025-047
- **Project Manager:** Marcus Morrisey
- **Project Type:** software-dev, it-consulting
  # Options (comma-separated, one or more): software-dev | it-consulting | itss | digital-strategy | vendor-assessment

## Schedule
- **Start Date:** 2026-01-15
- **Planned Finish Date:** 2026-06-30
- **Estimated Finish Date:** 2026-06-30

## Reporting
- **Period Length (weeks):** 2
- **Current Period Start:** 2026-03-02
- **Current Period End:** 2026-03-15

## Financial (optional — omit section if not used)
- **Budget (CAD):** 250,000
- **Expensed (CAD):** 45,000
- **Estimated Remaining (CAD):** 205,000
- **Overage (CAD):** 0
```

### Field notes
- **Project Type:** controlled vocabulary — `software-dev | it-consulting | itss | digital-strategy | vendor-assessment`; comma-separated for mixed-type projects; agent validates each value on load
- **Estimated Finish Date:** starts equal to Planned Finish Date; user updates when forecast diverges; drives variance tracking in report
- **Current Period Start/End:** set manually at project start; updated automatically by `period-rollover` each cycle
- **Financial section:** always CAD; omit entire section if not used — agent skips financial fields in report; all four fields required if section is present
- **Participants:** not included (MVP) — agent infers attribution from transcript text

### Read by
| Field | Skill |
|-------|-------|
| Identity fields, Schedule | `generate-report` (Sections 1, 3) |
| Project Type | `extract-and-verify` (tone inference context) |
| Estimated Finish Date | `generate-report` (variance vs. Planned) |
| Current Period Start/End | `ingest-evidence` (file date filter) |
| Period Length | `period-rollover` (computes next period dates) |
| Financial | `generate-report` (Section 3, optional) |

---
## Project State Schema — LOCKED

### `project-state.md` — persistent carry-forward state

```markdown
# Project State — [Project Name]
**Last Updated:** 2026-03-15
**Last Completed Period:** 2026-W11 (2026-03-02 → 2026-03-15)
**Periods Completed:** 3
**Next Action Item ID:** A-004
**Next Issue ID:** I-002

---
## Milestones
> Baseline End is immutable — agent proposes changes; user must confirm before state is updated.

| ID | Milestone | Baseline End | Estimated End | Status | Variance |
|----|-----------|-------------|---------------|--------|----------|
| M-01 | Discovery complete | 2026-02-28 | 2026-03-07 | Complete | +7d |
| M-02 | Beta release | 2026-04-30 | 2026-05-14 | At Risk | +14d |

---
## Action Items

| ID | Owner | Item | Due Date | Status | Periods Open |
|----|-------|------|----------|--------|-------------|
| A-001 | Marcus | Draft SOW amendment | 2026-03-07 | Complete | 1 |
| A-002 | Jane | Deliver test plan | 2026-03-21 | Open | 1 |
| A-003 | Tom | Approve budget revision | 2026-03-15 | Open | 2 |

---
## Issues & Risks

| ID | Description | Severity | Owner | Due Date | Status | Periods Open |
|----|-------------|---------|-------|----------|--------|-------------|
| I-001 | Legacy API incompatibility | High | Marcus | 2026-03-21 | Open | 1 |

---
## Active Return to Green Plans

### Schedule — Yellow (first flagged: 2026-W09)
[Verified plan text — carries forward until indicator returns to Green]

---
## Period History (rolling 4-week window)

### 2026-W09 (2026-02-16 → 2026-03-01)
- **Health:** Schedule Yellow; all others Green
- **Report:** `status-reports/2026-W09.qmd`
- **Summary:** [1–3 sentence brief written by agent at period close]

### 2026-W11 (2026-03-02 → 2026-03-15)
- **Health:** Schedule Yellow; all others Green
- **Report:** `status-reports/2026-W11.qmd`
- **Summary:** [1–3 sentence brief written by agent at period close]
```

### `extractions-current.md` — temp, current period only

Written by `extract-and-verify`. Read by `generate-report`. Cleared by `period-rollover` (after state is updated).

```markdown
# Current Period Extractions — [Project Name]
**Period:** 2026-W13 (2026-03-16 → 2026-03-29)
**Status:** Verified — awaiting generate-report

---
## Health Dashboard
- Overall: Green | Schedule: Yellow | Scope: Green | Budget: Green
- Client's Feeling: Green
  - Rationale: client expressed satisfaction in external meeting 2026-03-20

---
## Progress This Period
- Completed API compatibility assessment
- Beta release timeline revised; client agreement confirmed

---
## Decisions Made
| Decision | Made By | Date | Notes |
|----------|---------|------|-------|
| Extend beta deadline 2 weeks | Marcus, Tom | 2026-03-20 | SOW amendment to follow |

---
## New Action Items
| ID | Owner | Item | Due Date |
|----|-------|------|----------|
| A-004 | Marcus | Draft SOW amendment v2 | 2026-04-05 |

---
## Issue Updates
| ID | Update |
|----|--------|
| I-001 | Workaround identified; fix targeted for beta |

---
## Return to Green Plan Updates
- **Schedule Yellow:** plan updated — beta target revised to 2026-05-14; carrying forward

---
## Next Period Plan
- Finalise SOW amendment
- Begin beta testing
- Review budget with client
```

### Lifecycle
1. `ingest-evidence` → reads transcript files, stores parsed notes internally
2. `extract-and-verify` → extracts all items, assigns IDs, presents for user verification → writes verified output to `extractions-current.md`
3. `generate-report` → reads `extractions-current.md` + `project-state.md` + `project-config.md` → produces `status-reports/[period].qmd`
4. `period-rollover` → merges `extractions-current.md` into `project-state.md` (increments Periods Open, retires Complete items, trims history to 4-week window, advances period dates in `project-config.md`) → clears `extractions-current.md`

---
## Quarto Frontmatter Template — LOCKED

Auto-populated by `generate-report` from `project-config.md` and current period dates.

```yaml
---
title: "Project Status Report — Digital Platform Modernisation"
subtitle: "Reporting Period: 2026-W11 · 2026-03-02 to 2026-03-15"
date: "2026-03-15"
author: "Marcus Morrisey"
client: "Acme Corp"
docket: "AC-2025-047"
format:
  docx:
    reference-doc: _templates/report-template.docx
    toc: false
    number-sections: false
---
```

### Field sources
| Field | Source |
|-------|--------|
| `title` | Constructed: `"Project Status Report — {project-name}"` |
| `subtitle` | Constructed: `"Reporting Period: {period-id} · {start} to {end}"` |
| `date` | `Current Period End` from `project-config.md` |
| `author` | `Project Manager` from `project-config.md` |
| `client` | `Client` from `project-config.md` |
| `docket` | `Docket #` from `project-config.md` |
| `reference-doc` | Fixed: `_templates/report-template.docx` |

### Notes
- `client` and `docket` are custom Quarto metadata — accessible in document body via `{{{< meta client >}}}` if needed in header tables
- `toc: false`, `number-sections: false` — report uses its own explicit section structure

---
## Pending Design Decisions
- Detailed SKILL.md content for each of the 5 skills ← ready to build
