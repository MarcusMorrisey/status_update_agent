---
name: weekly-update
description: Draft and produce a Waabanong weekly update document. Generates a markdown draft from GitHub commits and meeting notes, then converts to Word. Use when the user types /weekly-update or asks to write, draft, or generate a weekly update. Trigger on /weekly-update, "weekly update", "write the weekly", "draft the update", or similar.
---

# weekly-update

Produces a Waabanong weekly update document in two phases:

1. **Draft phase** — queries GitHub and meeting notes, writes a `.md` draft to `outputs/weekly-updates/`. User reviews and tweaks the markdown.
2. **Convert phase** — converts the approved `.md` to `.docx` using the unpack → edit XML → repack approach against the prior week's `.docx` as a base. This preserves the exact table styling, Features boxes, grey section headers, logo, and footer that pandoc alone cannot reproduce.

**Never skip the markdown review step.** The draft is the primary content review artifact.

---

## Invocation

```
/weekly-update [week-monday]           → draft phase
/weekly-update [week-monday] --convert → convert phase
```

**`week-monday`** is the Monday of the **reported** work week (Mon–Fri). Examples:
- Reporting on week Jun 15–19 → arg `2026-06-16` would be wrong; the Monday is `2026-06-15`
- Reporting on week Jun 22–26 → arg `2026-06-22`

Shorthands: `last-week` (Monday of the most recently completed work week) and `this-week` (Monday of the current work week). If no arg provided, infer `last-week`.

**Filename convention:** `Waabanong Weekly Update - Week of [week-monday].docx`
**Header in document:** `Week of [Month D, YYYY]` — single date line, no "Delivered" prefix.
This matches the existing generated files in `outputs/peguis-cfs/`.

---

## Step 0 — Compute dates

From `week-monday`:
- Reported week start = week-monday
- Reported week end = week-monday + 4 days (Friday)
- Draft path:  `outputs/weekly-updates/[week-monday]-draft.md`
- Docx path:   `outputs/weekly-updates/Waabanong Weekly Update - Week of [week-monday].docx`

---

## Step 1 (draft phase) — Gather data

### 1a — GitHub commits
Query the dev repo for commits in the reported week:

```bash
gh api "repos/ID-Fusion/PCFS/commits?per_page=50&since=[week-monday]T00:00:00Z&until=[week-monday+5days]T00:00:00Z" \
  --jq '.[] | {sha: .sha[0:7], date: .commit.author.date[0:10], message: .commit.message | split("\n")[0]}'
```

Group commits by date. For merge PRs, use the branch name and individual commits to infer what the PR covered. Do not surface merge commit messages themselves — surface what they contain.

### 1b — Meeting notes (equal weight to GitHub)
Read `project/meeting-notes-current.md` and `project/project-state.md`. For iterations in design or discovery phases (I5 A, I5 B, I6, I7), meeting notes are typically the **primary** source — there may be few or no GitHub commits for these. Capture session content, decisions, and outcomes with specificity matching the Apr 27 and May 27 approved examples.

### 1c — Features content
Read `project/iteration-features.md`. Every iteration section in the draft must include its Features list verbatim from this file. Do not omit or abbreviate Features. If scope has changed this week, flag it for the user and propose an update to iteration-features.md.

### 1d — Map commits to iterations

| Keywords in commit | Iteration |
|--------------------|-----------|
| login, auth, SSO, permission, role, session, logout | I2 - Login & Authorization |
| person, profile, family, member, genogram, search (person), address book, DOB | I3 - Client, Member & Family Data |
| intake, CFSIS, eligibility, supervisor review, closure, prior contact, self-referral | I4 - Intake Management |
| case file, case note, placement, AMR, F2F, SOS, safety, casework, placement | I5 A - Case File Management |
| abuse, investigation | I5 B - Abuse Investigations |
| migration, data clean, FAMCare, Campfire | I6 - Data Cleaning and Migration |
| finance, sage, PO, GL, budget, credit card | I7 - Financial Tracking |
| dashboard, reporting | I8 - Dashboard & Reporting |
| infrastructure, environment, Azure, deploy, version bump | I1 - System Infrastructure |
| General / cross-cutting (logging, UI, document, navigation) | Project Management |

When in doubt, include under the most relevant iteration.

---

## Step 2 (draft phase) — Write the markdown draft

Write to `outputs/weekly-updates/[week-monday]-draft.md` using this exact schema:

```markdown
# Waabanong Weekly Update
**Week of:** [Month D, YYYY]

> ⚠️ Roadmap image: provide updated PNG path before converting. Prior week's image will be used as placeholder if not supplied.

---

## Iteration Summary

| Iteration | Status | Current Phase | Notes |
|-----------|--------|---------------|-------|
| I1 - System Infrastructure & Environments | [status] | [phase] | [1-line note or blank] |
| I2 - Login & Authorization | [status] | [phase] | [1-line note or blank] |
| I3 - Client, Member & Family Data | [status] | [phase] | [1-line note or blank] |
| I4 - Intake Management & Automated Notifications | [status] | [phase] | [1-line note or blank] |
| I5 A - Case File Management & Signs of Safety | [status] | [phase] | [1-line note or blank] |
| I5 B – Abuse Investigations | [status] | [phase] | [1-line note or blank] |
| I6 - Data Cleaning and Migration | [status] | [phase] | [1-line note or blank] |
| I7 - Financial Tracking & Exports for Sage | [status] | [phase] | [1-line note or blank] |
| I8 - My Dashboard & Reporting | [status] | [phase] | [1-line note or blank] |

---

## Project Management & General

**Weekly Progress**

- [bullet]

---

## I1 - System Infrastructure & Environments

**Features**

[copy from iteration-features.md verbatim]

**Weekly Progress**

- [bullet, or "No infrastructure changes this week — Azure environment work continues."]

---

## I2 - Login & Authorization

**Features**

[copy from iteration-features.md verbatim]

**Weekly Progress**

- [bullet, or "No authentication changes this week."]

---

[... same pattern for I3 through I8 ...]
```

### Bullet-writing rules

**For high-activity iterations** (many commits or a major meeting): use a two-level structure — one parent bullet naming the theme, sub-bullets for specifics. Match the depth of the Apr 27 approved example (I4 had 10 sub-bullets under one parent):

```markdown
- Significant intake additions this period:
  - Director approval step added to Intake Closure workflow
  - Existing intake modal added — workers can view and link related open intakes
  - Self-referral option added to intake form
  - CFSIS Intake Number: fixed "PCFS" prefix display and validation
  - Intake Notes field: notes entered at intake auto-create a case note on escalation
```

**For low-activity iterations**: one or two flat bullets is fine. A "no changes" bullet is always better than an empty section.

**For meeting-heavy iterations** (I7 finance, I5 design sessions): use the Apr 27 I7 style — include specific session content, decisions made, and what was confirmed or deferred. Name dates and participants where meaningful.

**Phrase from the client's perspective** where possible: "Workers can now...", "Fixed issue where...", "Design approach confirmed for...".

**Do not surface merge commit messages** — surface the work they contained.

**PR and commit references in the markdown draft** — include them for traceability (e.g. "PR #50", "PR #49"). They are automatically stripped during Word conversion and must not appear in the final `.docx`. Never include them in parent bullet text, only in sub-bullets where they aid review of the draft.

---

## Step 3 (draft phase) — Hand off

```
✓ Draft written to outputs/weekly-updates/[week-monday]-draft.md

Review and edit the markdown, then run:
  /weekly-update [week-monday] --convert

Before converting:
  - Supply updated roadmap PNG path if available (otherwise prior week's image is used)
  - Confirm iteration-features.md is current
```

---

## Step 4 (convert phase) — Convert markdown to Word

### Roadmap image — REQUIRED before conversion

**The roadmap image must be supplied explicitly. There is no silent fallback.**

If the user does not provide a new roadmap PNG:
- Stop here and say: "Conversion requires an updated roadmap PNG. Please supply the path to the new Gantt image. If no new image is available this week, provide the most recent one and I'll replace it."
- Do NOT proceed without a confirmed image path.

### 4a — Run the converter

```bash
python scripts/convert.py [week-monday] --image [path/to/roadmap.png]
```

The script (`scripts/convert.py`) uses **python-docx** to open the most recently-dated `.docx` from `outputs/peguis-cfs/` as the base document, then structurally replaces content at known positions: date lines, summary table cells, Features table rows, and Weekly Progress bullet paragraphs. The base document's grey table headers, logo, and footer are preserved exactly.

Base document selection order (handled automatically by the script):
1. Most recently-dated `.docx` in `outputs/peguis-cfs/` (correct grey-table structure)
2. Most recently-dated `.docx` in `outputs/weekly-updates/` (pandoc output — less ideal)
3. Z: drive fallback: `Z:\...\Waabanong Weekly Update 2026-05-25.docx`

Do NOT fall back to a different project's `.docx` — style drift across projects is a real risk.

Override the base document with `--base [path]` if needed.

---

## Step 5 (convert phase) — Structural QA

After producing the `.docx`, run the structural QA check:

```bash
python scripts/qa_check.py "outputs/weekly-updates/Waabanong Weekly Update - Week of [week-monday].docx" \
  --fixture "outputs/peguis-cfs/Waabanong Weekly Update - Week of 2026-05-18.docx"
```

This checks 12 structural properties including:
- All 10 grey-table section headers present (General + I1–I8)
- Summary table has 10 rows (header + 9 iterations)
- I5 A and I5 B are separate section tables
- `Section`-style Weekly Progress paragraphs present (9 expected)
- `list1`-style bullets present
- No roadmap warning placeholder remaining
- Table count and bullet count match the May 2026 accepted fixture (within tolerance)

The regression test suite can also be run end-to-end:
```bash
python evals/weekly-updates/run_regression.py
```

If any check fails, re-run `scripts/convert.py` with `--dry-run` to inspect parsed content, fix the draft, and re-convert.

---

## Step 6 (convert phase) — Hand off

```
[OK] outputs/weekly-updates/Waabanong Weekly Update - Week of [week-monday].docx written.

QA checks: [pass/fail list — run scripts/qa_check.py]

Copy to:
  Z:\Shared\3_Client Projects\Peguis CFS\Projects\PD25-1186-CO - Custom CMS\4. Controlling\02. Status Reports\

Remaining manual steps:
  1. Open in Word and review formatting — especially table cell heights and bullet indentation
  2. Verify roadmap image is the correct week's Gantt (the script replaces the image bytes but
     cannot confirm the content matches the current period)
  3. Save as PDF for the 01_Sent to Client folder when approved
```

---

## Known limitations

- **Roadmap image**: the script requires `--image` and will exit with an error if omitted. Supplying an image only replaces the bytes — the user must visually confirm the image is the correct week's Gantt before delivering.
- **Iteration-features.md as source of truth**: if scope has changed but iteration-features.md hasn't been updated, the Features boxes will be stale. Update the file whenever scope is formally confirmed.
- **Base document structure**: `scripts/convert.py` finds content by structural position (table index, paragraph style). If the base document gains new tables or the section order changes, update the script's table-matching logic. Run `run_regression.py` after any structural changes to the base document or the script.
