# Current Period Extractions — Custom-CMS
**Period:** 2026-W31 (2026-07-17 → 2026-07-23)
**Status:** Verified — awaiting generate-report

---
## Health Dashboard
- Overall: Red | Schedule: Red | Scope: Yellow | Budget: Yellow
- Client's Feeling: Green
  - Rationale: Ross and team cooperative throughout — accommodating on UAT scheduling despite Treaty Days, Gabrielle/Ross exchanges collaborative and solution-oriented, no friction this period.

---
## Progress This Period
- Data migration/cutover plan (2-page brief) drafted and circulated to Varun, Gabrielle, and Rob for review (Jul 17); revised per Rob's feedback and recirculated (Jul 22).
- Case file functionality opened ahead of schedule so Ross's team can test intake scenarios that depend on an existing open case.

---
## Decisions Made
| Decision | Made By | Date | Notes |
|----------|---------|------|-------|
| Access-control testing item dropped from the cutover plan | Marcus / Rob | 2026-07-22 | Rob suggested removing it; Marcus agreed |
| Stress test retained in the cutover plan despite Rob's suggestion to drop it | Marcus | 2026-07-22 | Ross specifically requested it; Marcus flagged this to Rob rather than unilaterally removing it |
| FamCare will remain accessible (not read-only) for a few months post-cutover, for historical lookups | Rob / Marcus | 2026-07-21 | IDFusion has no access to make FamCare read-only regardless; this will be communicated as an internal message to PCFS staff instead |

---
## New Action Items
| ID | Owner | Item | Due Date |
|----|-------|------|----------|
| A-209 | Varun | Review the revised data migration/cutover plan; confirm test-environment access and whether PHP needs to be installed there for migration scripts | 2026-07-27 |
| A-210 | Marcus | Reconcile signed-SOW status with Rob — a signed copy was already sent to Ross on Jul 15 (per reopened W30 evidence); confirm with Rob/Ross that a copy is on file | 2026-07-23 |
| A-211 | Gabrielle / Ross | Hold the case management module UAT walkthrough (targeting Fri Jul 24 or the following Monday) to formally kick off case file UAT; expand the testing pool with additional service delivery staff | 2026-07-27 |
| A-212 | Gabrielle | Review the finance process for ongoing services with Ross's team (session planned Jul 23) | 2026-07-23 |
| A-213 | Marcus / Rob | Assess whether a change request and contingency budget are needed to handle FAMCare's database structure during migration scripting | 2026-07-27 |

---
## Action Item Status Updates
| ID | Update |
|----|--------|
| A-202 | Internally discussed/drafted (Jul 17 recap email) but not yet sent to Ross |
| A-206 | Reconfirmed as a firm Ross request during cutover-plan review (Jul 21–22); not yet scheduled |

---
## New Issues & Risks
None this period.

---
## Issue Updates
| ID | Update |
|----|--------|
| I-042 | Rob flagged (Jul 21) that FAMCare's current database structure is unusually poor quality, likely requiring a CR and contingency-budget spend to build reliable migration scripts — first concrete cost signal on this risk |
| I-035 | Gabrielle confirmed (Jul 22) internal abuse-module testing has just started; UAT not expected to be ready until the week of Aug 3 |

---
## Milestone Updates
None this period.

---
## Return to Green Plans

### Overall / Schedule — Red
- Finalize and circulate the data cutover plan once Varun confirms test-environment readiness (A-209)
- Hold the case file UAT walkthrough to unblock that module's sign-off (A-211)
- Deliver the consolidated go-live readiness update to Ross that's been pending since last period (A-202)

### Scope — Yellow
- No change to plan — continue holding the Phase 1 boundary on events/protection services while the roadmap conversation is scheduled

### Budget — Yellow
- Assess FAMCare CR/contingency-budget need before it becomes a blocker on migration scripting (A-213)

---
## Next Period Plan
- Get Varun's sign-off on the cutover plan and resolve test-environment/PHP access question (A-209)
- Hold the case management UAT walkthrough and finance-process review for ongoing services (A-211, A-212)
- Send Ross the consolidated go-live readiness update (A-202)
- Confirm signed-SOW status with Rob/Ross (A-210)
- Determine CR/contingency budget need for FAMCare migration work (A-213)
