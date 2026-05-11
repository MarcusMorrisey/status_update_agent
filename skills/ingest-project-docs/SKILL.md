---
name: ingest-project-docs
description: Ingest project documents (SOWs, plans, roadmaps, vendor assessments) for project status reporting. Use when the user types /ingest-project-docs or asks to ingest, load, or process project documents — not meeting transcripts. This skill reads files from the project-docs/ directory, extracts milestones, scope baseline, and budget baseline, and updates project-state.md. Run once at project start, then again when new documents arrive. Trigger on /ingest-project-docs, "ingest project docs", "load project documents", "process SOW", "process roadmap", or similar.
---

# ingest-project-docs

Reads documents from `project-docs/` and extracts baseline project structure: milestones, scope, and budget. Updates `project-state.md` with what it finds. Run once at project start, then again when new documents arrive — not every reporting period.

**This skill does NOT process meeting transcripts.** For meetings, use `/ingest-meetings`.

---

## Step 1 — Find the project root

Look for `project-config.md` in this order:
1. The current working directory
2. A `project/` subdirectory of the current working directory (i.e., `./project/project-config.md`)
3. Parent directories (walking upward)

Use the first match as the project root. Read it for project identity (client name, project name, docket).

If `project-state.md` already exists, read it — note what's already there so you can merge rather than overwrite.

---

## Step 2 — Scan project-docs/

List all files under `project-docs/`. Accepted formats: `.docx`, `.pdf`, `.txt`, `.md`.

If the directory is empty or doesn't exist, say so and stop — nothing to ingest.

Tell the user which files you're about to read.

---

## Step 3 — Read and extract

Read each document. For each, extract:

**Milestones:** Any named deliverable or phase with an associated date. Be inclusive — if it looks like a checkpoint, milestone, or phase end, capture it.
- Name, date (call it Baseline End), status (default: On Track unless doc says otherwise)

**Scope:** The project's stated objectives, deliverables, and explicit out-of-scope items. One or two sentences each is enough — this is for context, not verbatim reproduction.

**Budget baseline:** If a contract value, budget, or cost estimate is stated, note it. Format as CAD unless the document says otherwise.

**Flag conflicts:** If two documents contradict each other (e.g., different milestone dates, different scope), note both versions and flag them — you will present both to the user for resolution during the verification step.

---

## Step 4 — Present for verification

Show the user everything you found before writing anything to disk:

```
## Project Docs Ingestion — Verification

### Milestones found
| ID | Milestone | Baseline End | Status |
|----|-----------|-------------|--------|
| M-01 | [name] | [date] | On Track |
...

### Scope summary
**Objectives:** [extracted text]
**Out of scope:** [extracted text]

### Budget baseline
[amount] CAD (source: [filename])

### Conflicts or ambiguities
[list any contradictions between documents, or "None"]
```

Ask: "Does this look right? Approve, correct, or skip any item."

Wait for the user to respond. Apply any corrections before writing.

---

## Step 5 — Update project-state.md

If `project-state.md` does not exist, create it using this template (filling in what you extracted):

```markdown
# Project State — [Project Name]
**Last Updated:** [today]
**Last Completed Period:** none
**Periods Completed:** 0
**Next Action Item ID:** A-001
**Next Issue ID:** I-001

---
## Milestones
> Baseline End is immutable — agent proposes changes; user must confirm before state is updated.

| ID | Milestone | Baseline End | Estimated End | Status | Variance |
|----|-----------|-------------|---------------|--------|----------|
[rows from extraction]

---
## Action Items

| ID | Owner | Item | Due Date | Status | Periods Open |
|----|-------|------|----------|--------|-------------|

---
## Issues & Risks

| ID | Description | Severity | Owner | Due Date | Status | Periods Open |
|----|-------------|---------|-------|----------|--------|-------------|

---
## Active Return to Green Plans

---
## Period History (rolling 4-week window)
```

If `project-state.md` already exists:
- **Add** new milestones (with new sequential IDs continuing from last M-XX).
- **Do NOT overwrite** existing milestones, action items, issues, or period history.
- **Do NOT change** any Baseline End already recorded — it's immutable.
- If a document updates a milestone date that's already in state, flag it for the user rather than changing it automatically.

Update `project-config.md` if a budget baseline was extracted and the Financial section is not already populated (but don't overwrite existing values).

---

## Step 6 — Hand off

```
✓ project-state.md updated.

Milestones added: [N]
Budget baseline: [amount or "not found"]

Run /ingest-meetings when ready to start the first reporting period.
```
