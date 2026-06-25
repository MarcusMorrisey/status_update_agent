# Current Period Extractions — Custom-CMS
**Period:** 2026-W25 (2026-06-05 → 2026-06-18)
**Status:** Verified — awaiting generate-report

---
## Health Dashboard
- Overall: 🔴 Red | Schedule: 🔴 Red | Scope: 🟡 Yellow | Budget: 🟡 Yellow
- Client's Feeling: 🟡 Yellow
  - Rationale: UAT has started and the June 16 session was very positive (engaged testers, constructive feedback, Darryl asking substantive questions), but the July go-live requires completing case file, finance, and abuse UAT in a compressed window and no signed-off project schedule exists.

---
## Progress This Period

> Note: The June 16 meeting date is from the recording header ("16 June 2026"); the source folder is dated 2026-06-17 (upload date).

- **UAT Intake Module Walkthrough completed** (June 16) — Full PCFS stakeholder UAT session demonstrated the end-to-end intake workflow: individual search, intake creation, document upload, referral source, persons involved via search and genogram, issue categories, narrative, SLA timer, task assignment to supervisor, supervisor review and return-to-worker, CFIS entry, intake log, and intake close. New testers onboarded: Keisha, Cassandra, Geraldine, Leanne Lippins.
- **First round of UAT feedback already received** — Prior to the June 16 session, Teagan and other participants had already submitted a first round of edits; Marcus confirmed these are being processed as a priority.
- **Search bug identified and ticketed** — Gabrielle created a Freshdesk/ClickUp ticket live during the session for "open services not showing in person search results" — a UAT finding immediately captured and actioned.

---
## Decisions Made

| Decision | Made By | Date | Notes |
|----------|---------|------|-------|
| Intake task assignment: default to general supervisor pool; optional specific assignment; directors monitor unassigned/overdue queue | Darryl / Gabrielle / Ross | 2026-06-16 | |
| Add optional case synopsis / summary field at end of intake form; carries over to case file | Teagan / Gabrielle / Marcus | 2026-06-16 | Hidden if empty; shown front-and-centre if populated |
| Issue categories expanded to full CFIS list before go-live — development ticket to be submitted | Darryl / Gabrielle / Marcus | 2026-06-16 | May not be available at UAT start but must be complete for go-live |
| PCC and assessment documents: upload to intake record via document upload; brief summary in presenting problem narrative | Darryl / Marcus | 2026-06-16 | Required only for transition from intake to ongoing case |
| Step one for any intake is always search — check if person already exists before creating records | Ross / Darryl / Marcus | 2026-06-16 | Reinforced as standard workflow for all testers |
| Limited profiles can be upgraded to child/adult later; cannot be downgraded | Marcus | 2026-06-16 | |
| Finance tab visible to all workers as read-only summary; intake supervisors can modify family budgets; after-hours needs some financial access | Darryl / Marcus / Ross | 2026-06-16 | Darryl to be included in upcoming finance module design session |
| SLA timer continues when supervisor sends task back to worker; worker receives a new sub-deadline | Ross / Marcus | 2026-06-16 | Confirmed as original design; subject to adjustment if UAT feedback requires it |
| Follow-up intake practice sessions to be scheduled by Ross and Darryl; Marcus and Gabrielle available for support calls | Ross / Darryl / Marcus | 2026-06-16 | |

---
## New Action Items

| ID | Owner | Item | Due Date |
|----|-------|------|----------|
| A-177 | Gabrielle | Implement dual supervisor task assignment in intake task modal: default to general pool with option for specific supervisor assignment | 2026-07-02 |
| A-178 | Gabrielle | Add optional case synopsis/summary field at end of intake form; carry over to case file (visible if populated, hidden if empty) | 2026-07-02 |
| A-179 | Gabrielle | Submit development ticket for issue categories expansion to full CFIS list (all subcategories); confirmed must-have before go-live | 2026-07-02 |
| A-180 | Ross / Darryl | Schedule follow-up intake practice run sessions for PCFS team; use real-world scenarios with anonymized data; coordinate with Marcus/Gabrielle for follow-up review meetings | 2026-07-02 |
| A-181 | Ross / Gabrielle / Marcus | Define and implement intake supervisor finance permissions: read + ability to change family budgets; include after-hours access; review scope with Darryl in upcoming finance module session | 2026-07-02 |
| A-182 | Marcus | Activate UAT accounts for newly added team members following June 16 meeting | 2026-06-18 |
| A-183 | Marcus | Send UAT session summary to all June 16 participants: role assignments chart + feedback submission instructions (devteam@idfusion.com + cc Ross/Kelvin/Christina) | 2026-06-18 |
| A-184 | Gabrielle | Create/confirm bug ticket for "open services" not showing in person search results when initiating a new intake | 2026-06-18 |

---
## Action Item Status Updates

| ID | Update |
|----|--------|
| A-055 | Complete |
| A-078 | Complete |
| A-079 | Complete — current most recent version confirmed online |
| A-082 | Complete |
| A-083 | Complete |
| A-105 | Complete |
| A-106 | Resolved — moved to roadmap |
| A-107 | Resolved — moved to roadmap |
| A-109 | Complete |
| A-110 | Complete |
| A-112 | Complete |
| A-114 | Complete |
| A-115 | Complete |
| A-116 | Complete |
| A-119 | Complete |
| A-123 | Cancelled |
| A-124 | Complete |
| A-125 | Complete |
| A-129 | In Progress — intake module UAT walkthrough completed June 16; formal sign-off procedure still pending |
| A-138 | Complete |
| A-140 | Complete |
| A-141 | Complete |
| A-142 | Complete |
| A-143 | Complete |
| A-144 | Complete |
| A-145 | Complete |
| A-146 | Complete |
| A-148 | Complete |
| A-149 | Complete |
| A-161 | Open — Darryl re-confirmed need for expanded categories at June 16 session; development ticket being submitted (A-179); Darryl's source data still needed |

---
## New Issues & Risks

| ID | Description | Severity | Owner | Due Date |
|----|-------------|---------|-------|----------|
| I-041 | UAT bug: "open services" not showing in person search results — when initiating a new intake, existing open case files should be surfaced; currently not displaying as expected; Gabrielle created ticket during session | Low | Gabrielle | 2026-06-18 |

---
## Issue Updates

| ID | Update |
|----|--------|
| I-036 | Intake module UAT walkthrough completed June 16; UAT now actively running across modules — substantially resolved; process functional |
| I-038 | Issue categories expansion confirmed as mandatory pre-go-live requirement at June 16 UAT session; development ticket being submitted (A-179) |

---
## Milestone Updates

_(No milestone date changes this period — M-04 Go-Live remains 2026-07-31 as set in W21.)_

---
## Return to Green Plans

### Overall — 🔴 Red (first flagged: 2025-W48)
- Complete intake UAT cycle (A-180); route and triage all feedback via Freshdesk → ClickUp pipeline
- Implement high-priority UAT feedback items (A-177, A-178, A-179, A-184) promptly to demonstrate responsiveness before next practice session
- Progress case file and finance modules toward UAT readiness; schedule first finance UAT session

### Schedule — 🔴 Red (first flagged: 2025-W48)
- July 31 go-live requires completing remaining module UAT (case file, finance, abuse) within a compressed W27–W33 window — identify the critical path explicitly
- Formally re-baseline contract timeline with Clemene/Rob (A-112 still open)
- Send updated status report to PCFS confirming July target and remaining milestone sequence (A-171 still open)

### Scope — 🟡 Yellow (first flagged: 2025-W50)
- Case synopsis field and supervisor pool option confirmed in-scope (A-177, A-178); implement promptly to avoid UAT feedback accumulating as scope debt
- Issue categories expansion (A-179, A-161) confirmed must-have before go-live — track as a go-live blocker
- Finance access additions from Darryl (A-181) add scope to finance module; review cost implication with Rob before design begins

### Budget — 🟡 Yellow (first flagged: 2025-W50)
- Abuse module contract amendment still unresolved — include in updated status report to PCFS (A-171)
- Finance access additions from Darryl (A-181) may expand finance module scope; confirm cost implication before implementation begins
- No new cost exposures this period; monitor Azure environment costs

### Client's Feeling — 🟡 Yellow (first flagged: 2026-W13)
- June 16 UAT session had very positive tone; schedule follow-up practice sessions quickly (A-180) to maintain momentum
- Deliver case synopsis field and supervisor pool option in next update to demonstrate responsiveness to UAT feedback
- Keep Ross and Darryl closely involved in remaining module planning; send session summary promptly (A-183)

---
## Next Period Plan

- Complete immediate post-UAT tasks: activate new tester accounts, send session summary and role chart (A-182, A-183)
- Implement intake module UAT feedback: supervisor pool option, case synopsis field, issue categories ticket, search bug fix (A-177–A-179, A-184)
- Ross and Darryl schedule follow-up intake practice sessions; begin triaging UAT feedback through Freshdesk pipeline (A-180)
- Hold finance module design session; include Darryl on intake supervisor budget access requirements (A-181)
- Run /ingest-meetings for W27 to ingest the June 19 internal finance meeting transcript
