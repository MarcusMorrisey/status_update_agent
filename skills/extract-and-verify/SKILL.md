---
name: extract-and-verify
description: Extract project status items from meeting notes and evidence emails, and verify with the user before writing. Use when the user types /extract-and-verify or asks to extract, analyze, or pull out action items, decisions, issues, or health status from meeting transcripts or emails. Runs after ingest-evidence. Extracts all structured items from evidence-notes-current.md, infers health indicators, assigns stable IDs, presents a single full list for user approval, and writes verified output to extractions-current.md. Trigger on /extract-and-verify, "extract items", "analyze meetings", "pull action items", or similar.
---

# extract-and-verify

Extracts all structured items from `evidence-notes-current.md`, infers health indicators, and presents everything to the user for a single verification pass. Only after the user approves does anything get written to `extractions-current.md`.

**Verification principle:** One full-list pass. The user can approve, reject, merge, or simplify any item. Nothing is written until sign-off.

**This skill does NOT generate the report.** That's `/generate-report`.

---

## Step 1 — Load context

Read from the project root:
- `evidence-notes-current.md` — the source transcripts and emails (required; stop and tell user if missing)
- `project-state.md` — existing action items, issues, milestones (for context and ID continuity)
- `project-config.md` — project type (affects tone inference), period dates, client name

Note the `Next Action Item ID` and `Next Issue ID` from `project-state.md`. If `project-state.md` doesn't exist yet, start IDs at A-001 and I-001.

---

## Step 2 — Extract all items

Read `evidence-notes-current.md` thoroughly. For each meeting and email, extract:

### Progress This Period
Concrete work completed, deliverables produced, or milestones reached. Look for past-tense statements ("we finished", "delivered", "completed", "closed").

### Decisions Made
Any choice or direction that was explicitly agreed upon. Capture who made it and the date. Distinguish from action items: a decision is a concluded choice, an action item is future work.

### Action Items & Commitments
**Be liberal — overdetect.** Any stated intention qualifies: "I'll send", "we need to", "let's make sure", "someone should". Capture: owner (infer from context), item, due date (infer if not stated — use next period end as default). Assign sequential IDs continuing from `Next Action Item ID`.

Also check existing open action items in `project-state.md` and note their current status based on transcript content.

If you add more than 5 Action Items & Commitments, review them all again and try to collapse or summarize them into approximately 5 to 7 items. Anything that was resolved in the meeting itself can be omitted.  

### Issues & Risks
Problems, blockers, concerns, or risks mentioned. Capture: description, severity (High / Medium / Low — infer from language), owner (infer), due date if mentioned. Assign new sequential IDs continuing from `Next Issue ID`.

Also check existing open issues in `project-state.md` and note any updates.

If you add more than 3 Issues & Risks, review them all again and try to collapse or summarize them into approximately 3 items.   

### Milestone Updates
Any mention of milestone dates slipping, completing, or being revised. Map to existing milestones in `project-state.md` by name. Note: you can propose an updated Estimated End, but do not change Baseline End — that's immutable.

### Health Indicators
Infer a RAG status (Green / Yellow / Red) for each:
- **Overall Health** — your gestalt read on the project
- **Schedule** — are milestones on track?
- **Scope** — any scope creep or change requests?
- **Budget** — any cost concerns mentioned?
- **Client's Feeling** — infer from tone and language in external meetings and client emails. If only internal meetings and no client emails this period, note that.

For each Yellow or Red indicator, draft a brief Return to Green Plan (1–3 bullet points) — you'll include this in the verification list.

### Next Period Plan
Propose 3–5 bullets for what should happen next period, based on open items and transcript discussion.

---

## Step 3 — Present the full verification list

Present everything in one structured view. Do NOT write to disk yet.

```
## Extraction Verification — [Project Name], Period [period-id]

Review each item below. For each, I'll proceed as listed unless you
correct, reject, merge, or simplify. Reply when ready.

---
### Health Dashboard
| Indicator | Status | Rationale |
|-----------|--------|-----------|
| Overall | [RAG] | [1 sentence] |
| Schedule | [RAG] | [1 sentence] |
| Scope | [RAG] | [1 sentence] |
| Budget | [RAG] | [1 sentence] |
| Client's Feeling | [RAG] | [1 sentence] |

---
### Progress This Period
[bullet list]

---
### Decisions Made
| Decision | Made By | Date | Notes |
|----------|---------|------|-------|
[rows]

---
### New Action Items
| ID | Owner | Item | Due Date |
|----|-------|------|----------|
[rows]

### Action Item Status Updates (existing items)
| ID | Item | Previous Status | Updated Status | Notes |
|----|------|----------------|----------------|-------|
[rows — only items with updates]

---
### New Issues & Risks
| ID | Description | Severity | Owner | Due Date |
|----|-------------|---------|-------|----------|
[rows]

### Issue Updates (existing issues)
| ID | Description | Update |
|----|-------------|--------|
[rows — only issues that were re-opened, escalated, or had a meaningful status change this period; silently omit issues that "Remain Resolved" with no new activity]

---
### Milestone Updates
| Milestone | Current Estimated End | Proposed Estimated End | Notes |
|-----------|----------------------|----------------------|-------|
[rows — only milestones with changes]

---
### Return to Green Plans (for Yellow/Red indicators)
[one subsection per triggered indicator]

---
### Next Period Plan (proposed)
[bullet list]

---
Reply to approve all, or call out specific items to change.
```

Wait for user response.

---

## Step 4 — Apply feedback and confirm

Incorporate any corrections the user makes. If needed, show a revised excerpt and confirm again.

Once the user approves (explicit "looks good", "approved", "go ahead", or similar), proceed to write.

---

## Step 5 — Write extractions-current.md

Write the verified content to `extractions-current.md` in the project root:

```markdown
# Current Period Extractions — [Project Name]
**Period:** [period-id] ([start] → [end])
**Status:** Verified — awaiting generate-report

---
## Health Dashboard
- Overall: [RAG] | Schedule: [RAG] | Scope: [RAG] | Budget: [RAG]
- Client's Feeling: [RAG]
  - Rationale: [1 sentence]

---
## Progress This Period
[bullet list]

---
## Decisions Made
| Decision | Made By | Date | Notes |
|----------|---------|------|-------|
[rows]

---
## New Action Items
| ID | Owner | Item | Due Date |
|----|-------|------|----------|
[rows]

---
## Action Item Status Updates
| ID | Update |
|----|--------|
[rows — only items with updates]

---
## New Issues & Risks
| ID | Description | Severity | Owner | Due Date |
|----|-------------|---------|-------|----------|
[rows]

---
## Issue Updates
| ID | Update |
|----|--------|
[rows — only re-opened or escalated issues; "Remains Resolved" items are omitted entirely]

---
## Milestone Updates
| Milestone | Proposed Estimated End | Notes |
|-----------|----------------------|-------|
[rows — only if changes]

---
## Return to Green Plans
[subsections per triggered indicator — omit section entirely if all Green]

---
## Next Period Plan
[bullet list]
```

---

## Step 6 — Hand off

```
✓ extractions-current.md written.

[N] action items | [N] issues | [N] decisions | Health: [Overall RAG]

Run /generate-report to produce the status report.
```
