---
name: generate-report
description: Generate a Quarto project status report (.qmd) from verified extractions. Use when the user types /generate-report or asks to generate, produce, or create the status report. Runs after extract-and-verify. Reads extractions-current.md, project-state.md, and project-config.md, then produces a fully-formatted Quarto .qmd file in status-reports/. Trigger on /generate-report, "generate report", "create status report", "produce the qmd", "write the report", or similar.
---

# generate-report

Produces a Quarto `.qmd` status report from verified extractions. All 10 report sections are always present — empty sections get an explicit "No [x] this period" placeholder, never silently omitted.

**Prerequisite:** `extractions-current.md` must exist and have `Status: Verified`. If it's missing or not verified, stop and tell the user to run `/extract-and-verify` first.

---

## Step 1 — Load all inputs

Read from the project root:
- `extractions-current.md` — verified extractions (required)
- `project-state.md` — milestones (with Baseline End), open action items, open issues, active Return to Green plans
- `project-config.md` — all identity, schedule, and financial fields

Derive the report filename: `[period-id].qmd` (e.g., `2026-W11.qmd`). The period-id comes from the `Period:` line in `extractions-current.md`.

---

## Step 2 — Merge state and extractions

Before writing, reconcile:

**Action items:** Take all open items from `project-state.md` + new items from `extractions-current.md`. Apply any status updates from extractions. Include items that were marked Complete this period (show status = Complete) plus all still-Open items.

Bucket every action item into exactly one of three groups for Section 7:
- **New This Period** — `Carried Over? = No` (added in this period's extractions).
- **Changed This Period** — carried-over item with a status update this period (present in extractions' `Action Item Status Updates` table — e.g. went Complete, reopened, owner changed).
- **Carried Forward (No Change)** — carried-over item with no update this period.

**Issues:** Same approach — existing open issues from state + new issues from extractions + any updates. Bucket the same way (New This Period / Changed This Period / Carried Forward), using extractions' `Issue Updates` table to determine "changed."

**Aging:** For any item (action item or issue) landing in **Carried Forward**, check its `Periods Open` value from `project-state.md`. If `Periods Open >= 8` (default threshold; use `Aging Threshold (periods):` from `project-config.md` instead if present), mark it as aging — this surfaces long-stalled items instead of letting them sit silently in an ever-growing table.

**Milestones:** Use milestones from `project-state.md` as the source of record (they have both Baseline End and Estimated End). Apply any Estimated End updates from extractions (user already approved these).

**Return to Green Plans:** Active plans from `project-state.md` plus any new plans from extractions (for new Yellow/Red indicators).

---

## Step 3 — Write the .qmd file

Write to `status-reports/[period-id].qmd`. Create the `status-reports/` directory if it doesn't exist.

### Frontmatter

```yaml
---
title: "Project Status Report — [Project Name]"
subtitle: "Reporting Period: [period-id] · [start] to [end]"
date: "[Current Period End]"
author: "[Project Manager]"
client: "[Client]"
docket: "[Docket #]"
format:
  docx:
    reference-doc: ../_templates/report-template.docx
    toc: false
    number-sections: false
---
```

Field sources: `project-config.md` for all values. Period dates from `extractions-current.md`.

### Section 1 — Report Header

```markdown
# Project Status Report

| | |
|---|---|
| **Client** | [Client] |
| **Project** | [Project Name] |
| **Docket #** | [Docket #] |
| **Project Manager** | [Project Manager] |
| **Reporting Date** | [Current Period End] |
| **Start Date** | [Start Date] |
| **Planned Finish** | [Planned Finish Date] |
| **Estimated Finish** | [Estimated Finish Date] |
```

### Section 2 — Health Dashboard

```markdown
## Health Dashboard

| Indicator | Status |
|-----------|--------|
| Overall Health | 🟢 Green / 🟡 Yellow / 🔴 Red |
| Schedule | … |
| Scope | … |
| Budget | … |
| Client's Feeling | … |
```

Use 🟢 🟡 🔴 for the RAG status. Use emoji consistently — don't mix text-only.

### Section 3 — Project Status & Dates

```markdown
## Project Status & Dates

**Project Status:** [1–2 sentence narrative — synthesise from health indicators and progress]

**Variance:** Planned finish [Planned Finish Date] → Estimated finish [Estimated Finish Date] ([+/- N days/weeks] / On Track)
```

If the Financial section exists in `project-config.md`:
```markdown
### Financial Summary

| | |
|---|---|
| **Budget (CAD)** | $[Budget] |
| **Expensed (CAD)** | $[Expensed] |
| **Estimated Remaining (CAD)** | $[Estimated Remaining] |
| **Overage (CAD)** | $[Overage] |
```

If the Financial section is absent from `project-config.md`, omit the Financial Summary subsection entirely.

### Section 4 — Progress This Period

```markdown
## Progress This Period

[bullet list from extractions, or:]
- No progress items recorded this period.
```

### Section 5 — Milestones & Schedule

```markdown
## Milestones & Schedule

| Milestone | Baseline End | Estimated End | Status | Variance |
|-----------|-------------|---------------|--------|----------|
[rows from merged milestones]
```

Compute Variance as: Estimated End − Baseline End. Format as `+Nd` or `−Nd` or `On time`. If Estimated End = Baseline End, write `On time`.

**Mermaid Gantt** (include immediately after table, only if the table has rows):

````markdown
```{mermaid}
gantt
  title Milestone Schedule
  dateFormat YYYY-MM-DD
  [one section per milestone — two markers each]
```
````

Mermaid status mapping:
- Complete → `:milestone, done,`
- On Track → `:milestone,`
- At Risk → `:milestone, crit,`
- Delayed → `:milestone, crit,`

Format each milestone section:
```
  section [Milestone Name]
    Baseline  :milestone, [baseline-date], 0d
    Estimated :milestone, [status-tag], [estimated-date], 0d
```

If no milestones, write:
```markdown
No milestones recorded.
```
(And omit the Gantt entirely.)

### Section 6 — Decisions Made

```markdown
## Decisions Made

| Decision | Made By | Date | Notes |
|----------|---------|------|-------|
[rows, or:]

No decisions recorded this period.
```

### Section 7 — Action Items & Commitments

Use the three buckets computed in Step 2. Render each as its own subsection — this keeps fresh movement visible instead of burying it under an ever-growing backlog table. Full backlog detail still lives in `project-state.md`; this report only carries what's actually needed to read the period.

```markdown
## Action Items & Commitments

### New This Period
| # | Owner | Item | Due Date | Status |
|---|-------|------|----------|--------|
[rows — Carried Over? = No, or:]

None this period.

### Changed This Period
| # | Owner | Item | Due Date | Status | Update |
|---|-------|------|----------|--------|--------|
[rows — carried-over items with a status update this period, or:]

None this period.

### Carried Forward (No Change)
| # | Owner | Item | Due Date | Status | Periods Open |
|---|-------|------|----------|--------|---------------|
[rows — carried-over items with no update this period; prefix # with ⚠️ if aging, or:]

None this period.
```

If there are no action items at all across all three buckets, collapse the whole section to:
```markdown
## Action Items & Commitments

No action items this period.
```

### Section 8 — Issues & Risks

Same three-bucket structure as Section 7.

```markdown
## Issues & Risks

### New This Period
| # | Description | Severity | Owner | Due Date |
|---|-------------|---------|-------|----------|
[rows, or:]

None this period.

### Changed This Period
| # | Description | Severity | Owner | Due Date | Update |
|---|-------------|---------|-------|----------|--------|
[rows, or:]

None this period.

### Carried Forward (No Change)
| # | Description | Severity | Owner | Due Date | Periods Open |
|---|-------------|---------|-------|----------|---------------|
[rows; prefix # with ⚠️ if aging, or:]

None this period.
```

If there are no issues at all across all three buckets, collapse the whole section to:
```markdown
## Issues & Risks

No issues or risks recorded this period.
```

### Section 9 — Return to Green Plans

Only include this section if at least one health indicator is Yellow or Red.

```markdown
## Return to Green Plans
```

One subsection per Yellow or Red indicator:
```markdown
### [Indicator] — [RAG status] (first flagged: [period-id])

[verified plan text — 1–5 bullet points]
```

If all indicators are Green, write:
```markdown
## Return to Green Plans

All indicators Green — no return to green plans active.
```

### Section 10 — Next Period Plan

```markdown
## Next Period Plan

[bullet list, or:]
- No next period plan recorded.
```

---

## Step 4 — Confirm and hand off

Print the file path and prompt:

```
✓ status-reports/[period-id].qmd written.

To render to Word:
  quarto render status-reports/[period-id].qmd

Run /period-rollover to close out this period and prepare for the next.
```

Do NOT run `/period-rollover` automatically.
