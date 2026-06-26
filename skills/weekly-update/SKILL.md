---
name: weekly-update
description: Draft and produce a Waabanong weekly update document. Generates a markdown draft from GitHub commits and meeting notes, then converts to Word. Use when the user types /weekly-update or asks to write, draft, or generate a weekly update. Trigger on /weekly-update, "weekly update", "write the weekly", "draft the update", or similar.
---

# weekly-update

Produces a Waabanong weekly update document in two phases:

1. **Draft phase** — queries GitHub and meeting notes, writes a `.md` file to `outputs/weekly-updates/`. User reviews and tweaks in markdown.
2. **Convert phase** — converts the approved `.md` to `.docx` using pandoc with the existing May 25 update as a reference document.

Run draft and convert as separate steps. Never skip the markdown review step.

---

## Invocation

```
/weekly-update [delivery-monday]           → draft phase
/weekly-update [delivery-monday] --convert → convert phase
```

**`delivery-monday`** is the Monday of the week the update is *delivered* (= the Monday immediately following the reported work week). Examples:
- Reported week Jun 15–19 → delivery Monday Jun 22 → arg `2026-06-22`
- Reported week Jun 22–26 → delivery Monday Jun 29 → arg `2026-06-29`

Shorthands: `last-week` (delivery = most recent Monday) and `this-week` (delivery = next Monday). If no arg provided, infer `last-week`.

---

## Step 0 — Compute dates

From `delivery-monday`:
- Reported week start = delivery-monday − 7 days (the preceding Monday)
- Reported week end   = delivery-monday − 3 days (the preceding Friday)
- Output filename base: `Waabanong Weekly Update [delivery-monday]`
- Draft path:  `outputs/weekly-updates/[delivery-monday]-draft.md`
- Docx path:   `outputs/weekly-updates/Waabanong Weekly Update [delivery-monday].docx`

---

## Step 1 (draft phase) — Gather data

### 1a — GitHub commits
Query the dev repo for commits in the reported week:

```bash
gh api "repos/ID-Fusion/PCFS/commits?per_page=50&since=[start]T00:00:00Z&until=[end+1]T00:00:00Z" \
  --jq '.[] | {sha: .sha[0:7], date: .commit.author.date[0:10], message: .commit.message | split("\n")[0]}'
```

Group commits by date. Merge PRs appear as "Merge pull request #N from ..."; use the branch name and individual commits to infer what the PR covered.

### 1b — Meeting notes
Check `project/meeting-notes-current.md` for any meetings that fall within the reported week dates. Also check `project/project-state.md` → recent action items for context on what was done.

### 1c — Map commits to iterations

Use these rules to assign commits to iterations:

| Keywords in commit | Iteration |
|--------------------|-----------|
| login, auth, SSO, permission, role | I2 - Login & Authorization |
| person, profile, family, member, genogram, search (person) | I3 - Client, Member & Family Data |
| intake, CFSIS, eligibility, supervisor review, closure | I4 - Intake Management |
| case file, case note, placement, AMR, F2F, SOS, safety, casework | I5A - Case File Management |
| abuse, investigation | I5B - Abuse Investigations |
| migration, data clean, FAMCare, Campfire | I6 - Data Migration |
| finance, sage, PO, GL, budget, credit card | I7 - Financial Tracking |
| dashboard, reporting | I8 - Dashboard & Reporting |
| infrastructure, environment, Azure, deploy, version bump | I1 - System Infrastructure |
| General / cross-cutting (logging, UI, document, navigation) | Project Management |

When in doubt, include the commit under the most relevant iteration rather than omitting it.

---

## Step 2 (draft phase) — Write the markdown draft

Write to `outputs/weekly-updates/[delivery-monday]-draft.md` using this exact schema:

```markdown
# Waabanong Weekly Update
**Delivered:** [delivery-monday formatted as "Month D, YYYY"]
**Week of:** [reported-start formatted as "Month D"] to [reported-end formatted as "D, YYYY"]

> ⚠️ Gantt chart image: replace placeholder with updated PNG before converting to Word.

---

## Iteration Summary

| Iteration | Status | Current Phase | Notes |
|-----------|--------|---------------|-------|
| I1 - System Infrastructure & Environments | [status] | [phase] | [1-line note or blank] |
| I2 - Login & Authorization | [status] | [phase] | [1-line note or blank] |
| I3 - Client, Member & Family Data | [status] | [phase] | [1-line note or blank] |
| I4 - Intake Management & Automated Notifications | [status] | [phase] | [1-line note or blank] |
| I5A - Case File Management & Signs of Safety | [status] | [phase] | [1-line note or blank] |
| I5B - Abuse Investigations | [status] | [phase] | [1-line note or blank] |
| I6 - Data Cleaning and Migration | [status] | [phase] | [1-line note or blank] |
| I7 - Financial Tracking & Exports for Sage | [status] | [phase] | [1-line note or blank] |
| I8 - My Dashboard & Reporting | [status] | [phase] | [1-line note or blank] |

---

## Project Management & General

- [bullet]
- [bullet]

---

## I1 - System Infrastructure & Environments

**Weekly Progress**

- [bullet, or "No infrastructure changes this week."]

---

## I2 - Login & Authorization

**Weekly Progress**

- [bullet, or "No authentication changes this week."]

---

## I3 - Client, Member & Family Data

**Weekly Progress**

- [bullet]

---

## I4 - Intake Management & Automated Notifications

**Weekly Progress**

- [bullet]

---

## I5A - Case File Management & Signs of Safety

**Weekly Progress**

- [bullet]

---

## I5B - Abuse Investigations

**Weekly Progress**

- [bullet, or "No new developments this week; solution design in progress."]

---

## I6 - Data Cleaning and Migration

**Weekly Progress**

- [bullet, or "Data migration planning continues; no client-facing changes."]

---

## I7 - Financial Tracking & Exports for Sage

**Weekly Progress**

- [bullet]

---

## I8 - My Dashboard & Reporting

**Weekly Progress**

- Future iteration per schedule; no dashboard or reporting work this week.
```

**Content rules:**
- Weekly Progress bullets should be concrete and specific — reference what actually shipped, not just that work happened.
- Merge PRs are not news; the individual changes they contain are.
- Phrase bullets from the client's perspective where possible ("Users can now..." / "Fixed issue where...").
- If an iteration had zero relevant commits and no meetings, write a single "No [X] changes this week." bullet — never leave a section empty.
- Notes column in the summary table: 1 sentence max, only if something notable; otherwise blank.

---

## Step 3 (draft phase) — Hand off

```
✓ Draft written to outputs/weekly-updates/[delivery-monday]-draft.md

Review and edit the markdown, then run:
  /weekly-update [delivery-monday] --convert

Before converting: replace the Gantt image placeholder with the current PNG.
```

---

## Step 4 (convert phase) — Convert markdown to Word

Verify the draft file exists and the Gantt image warning has been addressed (ask the user if unsure).

Run pandoc with the May 25 update as the reference document:

```bash
pandoc "outputs/weekly-updates/[delivery-monday]-draft.md" \
  --reference-doc="Z:\Shared\3_Client Projects\Peguis CFS\Projects\PD25-1186-CO - Custom CMS\4. Controlling\02. Status Reports\Waabanong Weekly Update 2026-05-25.docx" \
  -o "outputs/weekly-updates/Waabanong Weekly Update [delivery-monday].docx"
```

If the Z: drive reference doc is unavailable, fall back to any existing `.docx` in `outputs/weekly-updates/`.

After conversion, open or validate the file:

```bash
python "C:\Users\Marcus02\AppData\Roaming\Claude\local-agent-mode-sessions\skills-plugin\c35281fb-bb9c-4979-8d7c-c1fec64bd1d1\cde7abc6-c302-4a93-ba64-96aaf4dac4fd\skills\docx\scripts\office\validate.py" \
  "outputs/weekly-updates/Waabanong Weekly Update [delivery-monday].docx"
```

### Known limitations of the pandoc conversion
- The iteration **Features** boxes (the single-cell tables in the Word template) are omitted from the markdown — they're static boilerplate and can be added by copying from the prior week's Word doc if needed.
- The Gantt chart PNG must be embedded manually after conversion.
- Heading styles will follow the reference doc; minor style drift is normal — review in Word before sending.

---

## Step 5 (convert phase) — Hand off

```
✓ outputs/weekly-updates/Waabanong Weekly Update [delivery-monday].docx written.

Copy to:
  Z:\Shared\3_Client Projects\Peguis CFS\Projects\PD25-1186-CO - Custom CMS\4. Controlling\02. Status Reports\

Remaining manual steps:
  1. Embed the updated Gantt chart image
  2. Add Features boxes from prior week's doc (if needed)
  3. Review formatting in Word before sending
```
