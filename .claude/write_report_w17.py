"""One-shot helper: write 2026-W17.qmd to the project status-reports directory."""
import pathlib

OUT_DIR = pathlib.Path(r"C:/ClaudeProjects/status_update_agent/project/status-reports")
OUT_DIR.mkdir(parents=True, exist_ok=True)
OUT = OUT_DIR / "2026-W17.qmd"

CONTENT = r"""---
title: "Project Status Report — Custom-CMS"
subtitle: "Reporting Period: 2026-W17 · 2026-04-10 to 2026-04-23"
date: "2026-04-23"
author: "Marcus Morrisey"
client: "PCFS"
docket: "PD25-1186-CO"
format:
  docx:
    reference-doc: _templates/report-template.docx
    toc: false
    number-sections: false
---

# Project Status Report

| | |
|---|---|
| **Client** | PCFS |
| **Project** | Custom-CMS |
| **Docket #** | PD25-1186-CO |
| **Project Manager** | Marcus Morrisey |
| **Reporting Date** | 2026-04-23 |
| **Start Date** | 2025-11-17 |
| **Planned Finish** | 2026-03-31 |
| **Estimated Finish** | 2026-06-30 |

## Health Dashboard

| Indicator | Status |
|-----------|--------|
| Overall Health | 🔴 Red |
| Schedule | 🔴 Red |
| Scope | 🟡 Yellow |
| Budget | 🟡 Yellow |
| Client's Feeling | 🟡 Yellow (improving) |

## Project Status & Dates

**Project Status:** The Custom-CMS project for PCFS had a high-activity period: a full stakeholder demo was delivered on April 13 with all PCFS leadership present, Azure DevOps CI/CD infrastructure was deployed on April 17, and a comprehensive finance deep-dive was completed on April 21. The go-live date has been formally revised to June 30, 2026, with all stakeholders aligned; however, the project remains Red overall and on schedule as application code deployment — the critical path unlock for iteration velocity — has not yet occurred.

**Variance:** Planned finish 2026-03-31 → Estimated finish 2026-06-30 (+91 days / ~13 weeks delayed)

## Progress This Period

- New revised iteration plan/roadmap developed (with senior management, dev team, designers) and presented to full PCFS group at April 13 in-person meeting
- Live product demo delivered to PCFS stakeholders (Apr 13): login/SSO, global search, person profiles with partial-name search, relationship links, membership verification, role-based field masking
- Azure DevOps organization (PeguisCFS) and project (Waabanong) created; managed DevOps agent pool deployed to Azure; CI/CD infrastructure ready for code push
- Finance module deep-dive held (Apr 21) with Barry, Bev, Clemene, Ross, Gabrielle — full finance workflow documented (one-off payments, ongoing maintenance, petty cash, credit card, POs, approval hierarchy)
- Abuse program scope gap identified and resolved at Apr 13 meeting: confirmed in Phase 1 scope with dedicated tab and role-based access; requirements gathering now underway
- Formal UAT sign-off process agreed; alpha testing group identified (Kelvin, Christine, Darryl)
- Bug fixes and change requests from Apr 13 demo logged in ClickUp and sent to Varun
- Case management wireframes reviewed internally (Marcus + Gabrielle, Apr 17); spec updates identified

## Milestones & Schedule

| Milestone | Baseline End | Estimated End | Status | Variance |
|-----------|-------------|---------------|--------|----------|
| M-01 · Stage 1 - Discovery and Requirements complete | 2025-12-22 | 2026-03-26 | Delayed | +94d |
| M-02 · Stage 2 - Solution Design complete | 2026-01-31 | 2026-03-26 | Delayed | +54d |
| M-03 · Stage 3 - All 9 iterations complete / system ready | 2026-03-31 | 2026-06-30 | Delayed | +91d |
| M-04 · Go-Live | 2026-03-31 | 2026-06-30 | Delayed | +91d |
| M-05 · Stage 4 - Post-launch support complete | 2026-04-30 | 2026-07-28 | Delayed | +89d |

```{mermaid}
gantt
  title Milestone Schedule
  dateFormat YYYY-MM-DD
  section Stage 1 - Discovery & Requirements
    Baseline  :milestone, 2025-12-22, 0d
    Estimated :milestone, crit, 2026-03-26, 0d
  section Stage 2 - Solution Design
    Baseline  :milestone, 2026-01-31, 0d
    Estimated :milestone, crit, 2026-03-26, 0d
  section Stage 3 - All 9 Iterations Complete
    Baseline  :milestone, 2026-03-31, 0d
    Estimated :milestone, crit, 2026-06-30, 0d
  section Go-Live
    Baseline  :milestone, 2026-03-31, 0d
    Estimated :milestone, crit, 2026-06-30, 0d
  section Stage 4 - Post-Launch Support
    Baseline  :milestone, 2026-04-30, 0d
    Estimated :milestone, crit, 2026-07-28, 0d
```

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

## Action Items & Commitments

| # | Owner | Item | Due Date | Status | Carried Over? |
|---|-------|------|----------|--------|---------------|
| A-108 | Clemene | Bring CFO (Bev Stranger), Director of Finance (Barry Mann), and Senior Finance Officer (Carrie) to April 7th in-person meeting | 2026-04-07 | Complete | Yes |
| A-111 | Rob | Prepare and circulate agenda for April 7th meeting | 2026-04-04 | Complete | Yes |
| A-113 | Ross / Marcus | Schedule internal debrief prior to April 7th meeting | 2026-04-04 | Complete | Yes |
| A-117 | Marcus | Finance meeting prep: compile and bring outstanding finance questions to upcoming finance stakeholder meeting | 2026-04-23 | Complete | Yes |
| A-121 | Marcus | Add email notification monitoring/alerting to Feature Change Request list in Requirements doc | 2026-04-23 | Complete | No |
| A-122 | Marcus / Ross | Confirm finance doc storage with finance team (app vs. finance server vs. both) | 2026-04-13 | Complete | No |
| A-132 | Antonio Faiazza | Add Varun to PeguisCFS Azure subscription and DevOps project (contributor + agent pool access) | 2026-04-23 | Complete | No |
| A-133 | Ken / Antonio / Varun / Ross | Schedule and conduct follow-up session to set up Entra ID tenant and register application for SSO integration | 2026-04-30 | Complete | No |
| A-134 | Antonio / Varun | Restrict test environment access to approved Peguis Entra security group | 2026-04-30 | Complete | No |
| A-055 | Hailey / Marcus | Clarify and document requirements for role-based access, high-profile cases, and conflict-of-interest restrictions | 2026-01-29 | Open | Yes |
| A-078 | Marcus | Prepare field-definitions Excel template (tab per screen, field names, dropdown values, rules column) | 2026-01-29 | Open | Yes |
| A-079 | Barry / Bev | Provide exact Sage 300 version/build number for integration documentation | 2026-01-29 | Open | Yes |
| A-082 | Marcus | Establish revised target dates; prepare status update for Jaren and Rob with technical challenges and revised timeline | 2026-02-12 | Open | Yes |
| A-083 | Marcus / Varun | Complete Iteration 1 development; dev walkthrough completed 2026-02-24; development actively underway as of 2026-03-10 | 2026-02-12 | Open | Yes |
| A-104 | Christine | Consult Kinship department and QA to ensure licensing and placement info accurately represented in system design | 2026-03-26 | Open | Yes |
| A-105 | Marcus / Ross | Determine agency email account for external notification sends (Microsoft REST API integration) | 2026-03-26 | Open | Yes |
| A-106 | Marcus | Implement address-based search tab (search address fields on existing records; show associated individuals/cases, prioritized by open status) | 2026-03-26 | Open | Yes |
| A-107 | Marcus | Consult after-hours team to capture any additional requirements for address-based search feature | 2026-03-26 | Open | Yes |
| A-109 | Clemene | Provide Marcus with finance contact email for follow-up and summary sharing from last finance meeting | 2026-04-07 | Open | Yes |
| A-110 | Christine | Send recurring calendar invite for biweekly in-person meetings starting April 7th (all relevant participants) | 2026-04-07 | Open | Yes |
| A-112 | Clemene / Rob | Review contract and create a revised, clean project timeline and implementation schedule | 2026-04-07 | Open | Yes |
| A-114 | Ken Jacobs / Antonio Faiazza | Complete Azure post-setup: verify .onmicrosoft tenant access and permissions; share SQL DB credentials; provide IDFusion office static IP for whitelisting; fine-tune RBAC group assignments | 2026-04-09 | In Progress | Yes |
| A-115 | Ken Jacobs / Marcus | Deploy Wabanong application code to Azure dev environment (PHP backend to App Service + React frontend to Web App) | 2026-04-23 | In Progress | Yes |
| A-116 | Marcus | Document Azure infrastructure recap (high-level) for Clemene; store in SharePoint | 2026-04-09 | Open | Yes |
| A-118 | Marcus / Gabrielle | Design and implement finance dashboard for finance users: track finance sheet requests, in-app notifications + email notifications for pending approvals | 2026-04-23 | In Progress | Yes |
| A-119 | Marcus | Spec cleanup: spec sheet drop-downs only (remove buttons/radio buttons), update pronoun field to free-form, update person record spec (address tab, save button, genogram search clarity) | 2026-04-23 | In Progress | Yes |
| A-120 | Marcus | Clarify with Ross: (a) whether multiple open intakes per person are permitted, (b) assessment worker task assignment (direct assign vs. queue), (c) status terminology final confirmation | 2026-04-23 | Open | Yes |
| A-123 | Marcus | Define and document formal UAT sign-off procedure with IDFusion | 2026-04-30 | Open | No |
| A-124 | Kelvin / Clemene | Send abuse program forms and Excel template (PII removed) to IDFusion for requirements mapping | 2026-04-28 | Open | No |
| A-125 | Marcus | Share IDFusion's current abuse-related resources/forms with team; identify requirement gaps | 2026-04-28 | Open | No |
| A-126 | Marcus / Ross / Kelvin | Schedule and hold follow-up meeting to review abuse program requirements | 2026-04-30 | Open | No |
| A-127 | Christine / Clemene | Provide IDFusion with complete list and definitions of all legal terms used by agency (SSG, agreements with minors, temporary/permanent orders, customary acceptance, etc.) | 2026-05-07 | Open | No |
| A-128 | Marcus / Clemene | Cross-reference agency law/regulations with system terminology to ensure consistency | 2026-05-07 | Open | No |
| A-129 | IDFusion / Kelvin | Set up alpha testing access for Kelvin, Christine, and Darryl; coordinate review of language/forms before broader staff testing | 2026-05-07 | Open | No |
| A-130 | Marcus | Translate project timeline into Outlook calendar invites for key testing/review milestones | 2026-04-28 | Open | No |
| A-131 | IDFusion dev | Implement Apr 13 demo feedback items: fix Peguis footer typo; gender to Male/Female/Two-Spirit/Non-binary; add Child profile type option; auto age-18 profile upgrade (with confirmation); ID lookup table (Finance/Abuse/Intake/Case); abuse investigation tab with RBAC; address history with start/end dates + ordinary residence flag + note field; reserve/non-reserve auto-populate; CEFAS copy report; finance processing buttons (Intake/After Hours/Abuse/Prevention) | 2026-04-30 | Open | No |
| A-135 | IDFusion / Rob / Ross | Define post-go-live support tiers (bronze/silver/gold) and SLAs (e.g., 1-hour response for finance emergencies) | 2026-05-28 | Open | No |
| A-136 | Bev / Christine / Barry / Clemene | Send all finance templates and forms (face sheet, child maintenance Excel, visa rec, check rec, month-end report, chart of accounts) to Marcus/Gabrielle — headers only, no PII | 2026-04-28 | Open | No |
| A-137 | Bev | Send Sage 300 chart of accounts and all GL codes to Marcus/Gabrielle/Christine for integration mapping | 2026-04-28 | Open | No |
| A-138 | Marcus | Compile list of finance documents already received from Haley to avoid duplicate submissions | 2026-04-28 | Open | No |
| A-139 | Ross | Explore credit card receipt management options with finance team (Barry/Bev/Clemene); assess third-party virtual card providers and Wabanong integration | 2026-05-07 | Open | No |
| A-140 | Ross | Send abuse program master spreadsheet to Marcus/Gabrielle/Clemene/Christine | 2026-04-28 | Open | No |
| A-141 | Ross | Book Eagle Boardroom for IDFusion every Tuesday; send Teams invites for Apr 28, Apr 29, and finance Friday | 2026-04-25 | Open | No |
| A-142 | Gabrielle | Follow up with Sherry to confirm she has started testing | 2026-04-23 | Open | No |
| A-143 | Marcus | Add ClickUp task for address note field (ordinary residence complexity) | 2026-04-23 | Open | No |
| A-144 | Marcus | Spec update: remove "new task" button from person record; task creation only available in intake/case records | 2026-04-28 | Open | No |
| A-145 | Marcus | Validate case file wireframes/specs are complete; review all features captured | 2026-04-28 | Open | No |
| A-146 | Marcus | Create/update spec for case-specific documents tab (aligned with person record documents tab logic) | 2026-04-28 | Open | No |
| A-147 | Marcus | Schedule wireframe review meeting with ongoing services team (overview, case notes, placements tabs) | 2026-04-30 | Open | No |
| A-148 | Marcus | Send finance/placements flow documentation to Gabrielle in advance of next finance requirements session | 2026-04-23 | Open | No |

## Issues & Risks

| # | Description | Severity | Owner | Due Date | Status |
|---|-------------|---------|-------|----------|--------|
| I-018 | Finance/Sage integration requirements incomplete — Sage version/build not received, coding structure not formally documented, integration design not yet started. **Update:** Significant progress — full finance workflow documented at Apr 21 meeting; Sage 300 export approach agreed; GL codes/templates pending (A-136/A-137). | Medium | Hailey / Marcus | 2026-01-29 | Open |
| I-029 | Timeline slippage — original delivery targets missed; revised completion estimate is June 2026; M-03 baseline (2026-03-31) now missed with Iteration 1 still in development; re-baselining in progress (A-112). **Update:** June 30 go-live confirmed by all stakeholders at Apr 13; formal contract re-baselining still pending (A-112). | High | Marcus | 2026-02-12 | Open |
| I-032 | Development timeline at risk — Iteration 1 in progress as of 2026-03-10; 9 iterations required by 2026-03-31 baseline; Azure infrastructure now complete; application deployment (A-115) is critical next step. **Update:** Azure DevOps CI/CD infrastructure now in place (Apr 17); code deployment is the immediate next step — partial mitigation. | High | Marcus | 2026-03-12 | Open |
| I-033 | Address-based search confirmed as new development requirement (2026-03-10) — adds scope to an already-constrained timeline; impact on iteration sequencing not yet assessed. | Medium | Marcus | 2026-03-26 | Open |
| I-034 | Client-side continuity risk — Haley absent for 3+ months; Clemene covering but requires full project orientation; risk of decision delays and requirements gaps during transition. **Update:** Clemene fully engaged at Apr 13 and Apr 21; proactively raising issues; risk substantially reduced. | Medium | Marcus / Ross | 2026-04-07 | Open |
| I-035 | Abuse program requirements gap — scope confirmed in Phase 1 but forms, templates (12 domains, referral routing, 9 factors), and legal definitions not yet documented; dev cannot finalize abuse module until requirements collected (A-124 to A-128). | Medium | Marcus / Kelvin / Clemene | 2026-04-30 | Open |
| I-036 | Alpha testing not started — Sherry had not begun testing as of Apr 17; delay risks downstream iteration sign-off timelines. | Low | Gabrielle | 2026-04-30 | Open |

## Return to Green Plans

### Overall — 🔴 Red (first flagged: 2025-W48)

- Deploy app code to Azure dev environment (A-115) is the single most critical unlock — once done, iteration velocity can be measured and June 30 assessed realistically
- Close abuse program requirements gap (A-124 to A-128) before Iteration 2 planning to prevent scope delay
- Maintain weekly Monday status reports and Tuesday in-person cadence as agreed Apr 10/13

### Schedule — 🔴 Red (first flagged: 2025-W48)

- Code deployment + first CI/CD pipeline run must happen before end of W18 (A-115)
- Formally re-baseline the contract timeline post-Apr 13 (A-112) to give all stakeholders a shared, signed-off schedule
- Measure Iteration 1 completion velocity after first UAT cycle to project remaining iterations

### Scope — 🟡 Yellow (first flagged: 2025-W50)

- 40+ action items logged from Apr 13 demo — scope creep log in place; prioritize V1 vs. post-launch with Rob/Ross before next iteration planning
- Abuse program requirements to be collected and scoped before Iteration 2 planning (A-124 to A-128)
- Finance dashboard and workflows now fully documented; limit new additions until V1 is deployed

### Budget — 🟡 Yellow (first flagged: 2025-W50)

- Sage 300 GL codes and finance templates pending (A-136/A-137); needed to finalize integration scope and cost estimate
- Clarify whether expanded abuse module requirements affect contract budget
- Azure dev environment costs (~$200/mo) confirmed; ongoing costs tracking needed as UAT and production environments come online

### Client's Feeling — 🟡 Yellow (improving) (first flagged: 2026-W13)

- Clemene proactively engaged and flagging real issues constructively — communication is healthy
- Finance team now fully in the loop; weekly Tuesday in-person cadence established
- Maintain momentum with first meaningful milestone: app deployed to Azure dev

## Next Period Plan

- Deploy app code to Azure dev environment and set up CI/CD pipeline (A-115) — critical path item
- Close abuse program requirements: collect forms from Kelvin/Clemene, hold follow-up requirements session (A-124 to A-126)
- Collect finance templates and Sage 300 GL codes from Bev/Christine/Barry (A-136, A-137)
- Begin alpha testing prep: confirm Sherry is testing, set up access for Kelvin/Christine/Darryl (A-142, A-129)
- Formally re-baseline contract timeline (A-112)
"""

OUT.write_text(CONTENT, encoding="utf-8")
print(f"Written {OUT.stat().st_size} bytes to {OUT}")
