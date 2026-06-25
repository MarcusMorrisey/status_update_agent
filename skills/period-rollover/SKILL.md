---
name: period-rollover
description: Roll over a completed reporting period — carry forward open items, update project state, and advance period dates. Use when the user types /period-rollover or asks to close out a period, roll over to the next period, or archive the current period. Runs after generate-report. Merges extractions-current.md into project-state.md, advances Current Period Start/End in project-config.md, and clears extractions-current.md. Trigger on /period-rollover, "period rollover", "close out period", "roll over", "advance to next period", or similar.
---

# period-rollover

Closes out the current reporting period by merging verified extractions into the project state file, advancing the period dates in config, and clearing the working extraction file.

**Prerequisite:** Both `extractions-current.md` (Status: Verified) and a completed `status-reports/[period-id].qmd` should exist. If the report hasn't been generated yet, warn the user but offer to proceed anyway if they confirm.

**Early rollover check:** After loading `project-config.md`, compare today's date against `Current Period End`. If today is before `Current Period End`, warn the user before doing anything else:

```
⚠️  Period [period-id] doesn't end until [Current Period End] (today is [today]).
Rolling over early means any meetings held between now and [Current Period End]
will need to go into the next period's cycle instead.

Proceed with early rollover? (yes/no)
```

Stop and wait for confirmation. Only continue if the user confirms yes. If they say no, stop with no changes made.

**Do NOT auto-commit to git.** Prompt the user to commit at the end.

---

## Step 1 — Load current state

Read from the project root:
- `extractions-current.md` — verified extractions to merge in
- `project-state.md` — current persistent state
- `project-config.md` — period dates and Period Length

Identify the period being closed: from the `Period:` line in `extractions-current.md`.

---

## Step 2 — Update project-state.md

Apply all changes in this order:

### 2a — Update header
- Set `Last Updated` to today
- Set `Last Completed Period` to the period just closed (e.g., `2026-W11 (2026-03-02 → 2026-03-15)`)
- Increment `Periods Completed` by 1
- Advance `Next Action Item ID` if new items were added this period
- Advance `Next Issue ID` if new issues were added this period

### 2b — Milestones
- Apply any Estimated End updates from `extractions-current.md → ## Milestone Updates`
- Mark any milestones as Complete if noted in the extractions
- Do NOT change any Baseline End — it is immutable
- Do NOT remove completed milestones — keep them in the table with Status = Complete

### 2c — Action items
- Add new action items from `extractions-current.md → ## New Action Items` (with `Periods Open = 1`)
- For existing items: apply status updates from `extractions-current.md → ## Action Item Status Updates`
  - If status → Complete: keep the row, set Status = Complete
  - If still Open: increment `Periods Open` by 1
- Remove rows that have been Complete for more than 1 period (they've already been reported; no need to carry them indefinitely). Keep items that went Complete this period for at least one more period so they appear in the next report.

### 2d — Issues & Risks
- Add new issues from `extractions-current.md → ## New Issues & Risks` (with `Periods Open = 1`)
- Apply status updates from `extractions-current.md → ## Issue Updates`
  - Closed issues: keep for one more period, then remove on next rollover
  - Still-open issues: increment `Periods Open` by 1

### 2e — Active Return to Green Plans
- Add new plans from `extractions-current.md → ## Return to Green Plans`
- If a previously Yellow/Red indicator is now Green (per current extractions health dashboard), remove its plan
- Keep all plans for still-Yellow/Red indicators — they carry forward unchanged unless the user modified them during `extract-and-verify`

### 2f — Period History
Add an entry for the period just closed:

```markdown
### [period-id] ([start] → [end])
- **Health:** [summary — e.g., "Schedule Yellow; all others Green"]
- **Report:** `status-reports/[period-id].qmd`
- **Summary:** [1–3 sentences synthesising the period's key events]
```

Write the 1–3 sentence summary yourself based on the extractions. Keep it factual and brief.

Then trim the Period History to a rolling 4-week window: remove any entries older than 4 weeks from today. (Full history is preserved in git and the `.qmd` files.)

---

## Step 3 — Advance period dates in project-config.md

Compute next period:
- New `Current Period Start` = old `Current Period End` + 1 day
- New `Current Period End` = new `Current Period Start` + `Period Length (weeks)` − 1 day

Update these two fields in `project-config.md`. Leave all other fields unchanged.

---

## Step 4 — Clear extractions-current.md

Replace `extractions-current.md` with a blank template for the next period:

```markdown
# Current Period Extractions — [Project Name]
**Period:** [next-period-id] ([next-start] → [next-end])
**Status:** Empty — awaiting ingest-meetings and extract-and-verify
```

The period-id for the next period: compute from the new start date (ISO week format, e.g., `2026-W13`).

---

## Step 5 — Hand off

```
✓ Period [period-id] closed out.

project-state.md updated:
  [N] action items | [N] issues | [N] milestones | [N] RTG plans

project-config.md advanced:
  Current period: [next-start] to [next-end]

extractions-current.md cleared.

Reminder: commit these changes to git to preserve the period record.

When ready to start the next period, run /ingest-meetings.
```

Do NOT run `ingest-meetings` automatically. Do NOT commit to git automatically.
