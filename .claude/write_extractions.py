"""One-shot helper: write extractions-current.md to the project directory."""
import pathlib

OUT = pathlib.Path(r"C:/ClaudeProjects/status_update_agent/project/extractions-current.md")

CONTENT = """\
# Current Period Extractions — Custom-CMS
**Period:** 2026-W17 (2026-04-10 -> 2026-04-23)
**Status:** Verified — awaiting generate-report

---
## Health Dashboard
- Overall: Red | Schedule: Red | Scope: Yellow | Budget: Yellow
- Client's Feeling: Yellow (improving)
  - Rationale: Clemene proactively engaged and constructive (Apr 13, Apr 21); finance team (Barry/Bev) participating; Ross leading strongly; tone positive but urgency rising around June 30

---
## Progress This Period
- New revised iteration plan/roadmap developed (with senior management, dev team, designers) and presented to full PCFS group at April 13 in-person meeting
- Live product demo delivered to PCFS stakeholders (Apr 13): login/SSO, global search, person profiles with partial-name search, relationship links, membership verification, role-based field masking
- Azure DevOps organization (PeguisCFS) and project (Waabanong) created; managed DevOps agent pool deployed to Azure; CI/CD infrastructure ready for code push
- Finance module deep-dive held (Apr 21) with Barry, Bev, Clemene, Ross, Gabrielle -- full finance workflow documented (one-off payments, ongoing maintenance, petty cash, credit card, POs, approval hierarchy)
- Abuse program scope gap identified and resolved at Apr 13 meeting: confirmed in Phase 1 scope with dedicated tab and role-based access; requirements gathering now underway
- Formal UAT sign-off process agreed; alpha testing group identified (Kelvin, Christine, Darryl)
- Bug fixes and change requests from Apr 13 demo logged in ClickUp and sent to Varun
- Case management wireframes reviewed internally (Marcus + Gabrielle, Apr 17); spec updates identified

---
## Decisions Made
| Decision | Made By | Date | Notes |
|----------|---------|------|-------|
| June 30, 2026 go-live confirmed (revised from March 31) | IDFusion + PCFS leadership | Apr 13 | 4 weeks warranty/support to follow |
| Abuse program in Phase 1 scope with dedicated tab and RBAC | IDFusion + Clemene/Kelvin | Apr 13 | Requirements to be gathered from Kelvin/Clemene |
| All staff can VIEW family budget info; only finance/admin can EDIT | IDFusion + Clemene/Bev | Apr 13 | |
| App access via Peguis Microsoft 365 tenant (SSO); restricted to org security group in Entra | IDFusion + Ross/Ken | Apr 13/17 | Custom domain to comply with agency IT policies |
| Finance/Abuse/Case/Intake IDs all linked via lookup table; any ID can find the correct record | IDFusion | Apr 13 | Raised by Clemene |
| Reserve/non-reserve status to be auto-populated from federal/provincial Manitoba communities database | IDFusion | Apr 13 | For funding determination |
| All financial transactions to flow through Wabanong; daily/scheduled Excel export to Sage 300 | IDFusion + Clemene/Bev/Barry | Apr 21 | Reduces manual re-entry |
| Email notifications limited to critical cases only; most reminders/tasks managed in-app | IDFusion + Clemene | Apr 21 | Avoids email overload |
| Weekly status report cadence: Marcus delivers Mondays; group meets Tuesdays in-person | Marcus/Ross | Apr 10 | Eagle Boardroom booked weekly |
| Scope creep log maintained by Rob; items reviewed as a group before adding to V1 scope | IDFusion/Rob | Apr 13 | |

---
## New Action Items
| ID | Owner | Item | Due Date |
|----|-------|------|----------|
| A-121 | Marcus | Add email notification monitoring/alerting to Feature Change Request list in Requirements doc | Apr 23 -- Complete |
| A-122 | Marcus/Ross | Confirm finance doc storage with finance team (app vs. finance server vs. both) | Apr 13 -- Complete |
| A-123 | Marcus | Define and document formal UAT sign-off procedure with IDFusion | Apr 30 |
| A-124 | Kelvin/Clemene | Send abuse program forms and Excel template (PII removed) to IDFusion for requirements mapping | Apr 28 |
| A-125 | Marcus | Share IDFusion's current abuse-related resources/forms with team; identify requirement gaps | Apr 28 |
| A-126 | Marcus/Ross/Kelvin | Schedule and hold follow-up meeting to review abuse program requirements | Apr 30 |
| A-127 | Christine/Clemene | Provide IDFusion with complete list and definitions of all legal terms used by agency (SSG, agreements with minors, temporary/permanent orders, customary acceptance, etc.) | May 7 |
| A-128 | Marcus/Clemene | Cross-reference agency law/regulations with system terminology to ensure consistency | May 7 |
| A-129 | IDFusion/Kelvin | Set up alpha testing access for Kelvin, Christine, and Darryl; coordinate review of language/forms before broader staff testing | May 7 |
| A-130 | Marcus | Translate project timeline into Outlook calendar invites for key testing/review milestones | Apr 28 |
| A-131 | IDFusion dev | Implement Apr 13 demo feedback items: fix Peguis footer typo; gender to Male/Female/Two-Spirit/Non-binary; add Child profile type option; auto age-18 profile upgrade (with confirmation); ID lookup table (Finance/Abuse/Intake/Case); abuse investigation tab with RBAC; address history with start/end dates + ordinary residence flag + note field; reserve/non-reserve auto-populate; CEFAS copy report; finance processing buttons (Intake/After Hours/Abuse/Prevention) | Apr 30 |
| A-132 | Antonio Faiazza | Add Varun to PeguisCFS Azure subscription and DevOps project (contributor + agent pool access) | Apr 23 -- Complete |
| A-133 | Ken/Antonio/Varun/Ross | Schedule and conduct follow-up session to set up Entra ID tenant and register application for SSO integration | Apr 30 -- Complete |
| A-134 | Antonio/Varun | Restrict test environment access to approved Peguis Entra security group | Apr 30 -- Complete |
| A-135 | IDFusion/Rob/Ross | Define post-go-live support tiers (bronze/silver/gold) and SLAs (e.g., 1-hour response for finance emergencies) | May 28 |
| A-136 | Bev/Christine/Barry/Clemene | Send all finance templates and forms (face sheet, child maintenance Excel, visa rec, check rec, month-end report, chart of accounts) to Marcus/Gabrielle -- headers only, no PII | Apr 28 |
| A-137 | Bev | Send Sage 300 chart of accounts and all GL codes to Marcus/Gabrielle/Christine for integration mapping | Apr 28 |
| A-138 | Marcus | Compile list of finance documents already received from Haley to avoid duplicate submissions | Apr 28 |
| A-139 | Ross | Explore credit card receipt management options with finance team (Barry/Bev/Clemene); assess third-party virtual card providers and Wabanong integration | May 7 |
| A-140 | Ross | Send abuse program master spreadsheet to Marcus/Gabrielle/Clemene/Christine | Apr 28 |
| A-141 | Ross | Book Eagle Boardroom for IDFusion every Tuesday; send Teams invites for Apr 28, Apr 29, and finance Friday | Apr 25 |
| A-142 | Gabrielle | Follow up with Sherry to confirm she has started testing | Apr 23 |
| A-143 | Marcus | Add ClickUp task for address note field (ordinary residence complexity) | Apr 23 |
| A-144 | Marcus | Spec update: remove "new task" button from person record; task creation only available in intake/case records | Apr 28 |
| A-145 | Marcus | Validate case file wireframes/specs are complete; review all features captured | Apr 28 |
| A-146 | Marcus | Create/update spec for case-specific documents tab (aligned with person record documents tab logic) | Apr 28 |
| A-147 | Marcus | Schedule wireframe review meeting with ongoing services team (overview, case notes, placements tabs) | Apr 30 |
| A-148 | Marcus | Send finance/placements flow documentation to Gabrielle in advance of next finance requirements session | Apr 23 |

---
## Action Item Status Updates
| ID | Update |
|----|--------|
| A-108 | Complete -- Barry/Bev present at Apr 21 finance meeting; Clemene engaged at Apr 13 |
| A-111 | Complete -- Apr 13 meeting held |
| A-113 | Complete -- Apr 10 meeting was the internal debrief |
| A-114 | In Progress -- Azure DevOps org + agent pool deployed Apr 17; Entra ID/SSO portion complete (A-133/A-134 done) |
| A-115 | In Progress -- Azure DevOps infrastructure now in place; code push + pipeline setup is next step |
| A-117 | Complete -- Finance meeting held Apr 21; all questions tabled with Barry/Bev/Clemene |
| A-118 | In Progress -- Finance workflows documented Apr 21; wireframes in design |
| A-119 | In Progress -- Spec work continuing (Apr 17 internal); multiple spec updates added this period |

---
## New Issues & Risks
| ID | Description | Severity | Owner | Due Date |
|----|-------------|---------|-------|----------|
| I-035 | Abuse program requirements gap -- scope confirmed in Phase 1 but forms, templates (12 domains, referral routing, 9 factors), and legal definitions not yet documented; dev cannot finalize abuse module until requirements collected (A-124 to A-128) | Medium | Marcus/Kelvin/Clemene | Apr 30 |
| I-036 | Alpha testing not started -- Sherry had not begun testing as of Apr 17; delay risks downstream iteration sign-off timelines | Low | Gabrielle | Apr 30 |

---
## Issue Updates
| ID | Update |
|----|--------|
| I-018 | Significant progress: full finance workflow documented at Apr 21 meeting; Sage 300 export approach agreed; GL codes/templates pending (A-136/A-137) |
| I-029 | June 30 go-live confirmed by all stakeholders at Apr 13; formal contract re-baselining still pending (A-112) |
| I-032 | Azure DevOps CI/CD infrastructure now in place (Apr 17); code deployment is the immediate next step -- partial mitigation |
| I-034 | Clemene fully engaged at Apr 13 and Apr 21; proactively raising issues; risk substantially reduced |

---
## Milestone Updates
| Milestone | Proposed Estimated End | Notes |
|-----------|----------------------|-------|
| M-05 Stage 4 - Post-launch support complete | 2026-07-28 | Go-live now Jun 30 + 4 weeks warranty = ~Jul 28; baseline (Apr 30) already passed |

---
## Return to Green Plans

### Overall -- Red
- Deploy app code to Azure dev environment (A-115) is the single most critical unlock -- once done, iteration velocity can be measured and June 30 assessed realistically
- Close abuse program requirements gap (A-124 to A-128) before Iteration 2 planning to prevent scope delay
- Maintain weekly Monday status reports and Tuesday in-person cadence as agreed Apr 10/13

### Schedule -- Red
- Code deployment + first CI/CD pipeline run must happen before end of W18 (A-115)
- Formally re-baseline the contract timeline post-Apr 13 (A-112) to give all stakeholders a shared, signed-off schedule
- Measure Iteration 1 completion velocity after first UAT cycle to project remaining iterations

### Scope -- Yellow
- 40+ action items logged from Apr 13 demo -- scope creep log in place; prioritize V1 vs. post-launch with Rob/Ross before next iteration planning
- Abuse program requirements to be collected and scoped before Iteration 2 planning (A-124 to A-128)
- Finance dashboard and workflows now fully documented; limit new additions until V1 is deployed

### Budget -- Yellow
- Sage 300 GL codes and finance templates pending (A-136/A-137); needed to finalize integration scope and cost estimate
- Clarify whether expanded abuse module requirements affect contract budget
- Azure dev environment costs (~$200/mo) confirmed; ongoing costs tracking needed as UAT and production environments come online

### Client's Feeling -- Yellow (improving)
- Clemene proactively engaged and flagging real issues constructively -- communication is healthy
- Finance team now fully in the loop; weekly Tuesday in-person cadence established
- Maintain momentum with first meaningful milestone: app deployed to Azure dev

---
## Next Period Plan
- Deploy app code to Azure dev environment and set up CI/CD pipeline (A-115) -- critical path item
- Close abuse program requirements: collect forms from Kelvin/Clemene, hold follow-up requirements session (A-124 to A-126)
- Collect finance templates and Sage 300 GL codes from Bev/Christine/Barry (A-136, A-137)
- Begin alpha testing prep: confirm Sherry is testing, set up access for Kelvin/Christine/Darryl (A-142, A-129)
- Formally re-baseline contract timeline (A-112)
"""

OUT.write_text(CONTENT, encoding="utf-8")
print(f"Written {OUT.stat().st_size} bytes to {OUT}")
