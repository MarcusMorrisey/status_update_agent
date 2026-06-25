"""
Period rollover for 2026-W19 → 2026-W21.
Updates project-state.md, project-config.md, and extractions-current.md.
"""
import pathlib

ROOT = pathlib.Path(r'C:/ClaudeProjects/status_update_agent/project')

# ── project-state.md ──────────────────────────────────────────────────────────
STATE = ROOT / 'project-state.md'
STATE.write_text("""\
# Project State - Custom-CMS
**Last Updated:** 2026-05-26
**Last Completed Period:** 2026-W19 (2026-04-24 → 2026-05-07)
**Periods Completed:** 11
**Next Action Item ID:** A-161
**Next Issue ID:** I-040

---
## Milestones
> Baseline End is immutable - agent proposes changes; user must confirm before state is updated.

| ID | Milestone | Baseline End | Estimated End | Status | Variance |
|----|-----------|-------------|---------------|--------|----------|
| M-01 | Stage 1 - Discovery and Requirements complete | 2025-12-22 | 2026-03-26 | Delayed | +94d |
| M-02 | Stage 2 - Solution Design complete | 2026-01-31 | 2026-03-26 | Delayed | +54d |
| M-03 | Stage 3 - All 9 iterations complete / system ready | 2026-03-31 | 2026-06-30 | Delayed | +91d |
| M-04 | Go-Live | 2026-03-31 | 2026-06-30 | Delayed | +91d |
| M-05 | Stage 4 - Post-launch support complete | 2026-04-30 | 2026-07-28 | Delayed | +89d |

---
## Action Items

| ID | Owner | Item | Due Date | Status | Periods Open |
|----|-------|------|----------|--------|-------------|
| A-055 | Hailey / Marcus | Clarify and document requirements for role-based access, high-profile cases, and conflict-of-interest restrictions; access model decisions made Apr 28 (three-tier confidentiality, include-based CoI model) | 2026-01-29 | In Progress | 9 |
| A-078 | Marcus | Prepare field-definitions Excel template (tab per screen, field names, dropdown values, rules column) | 2026-01-29 | Open | 9 |
| A-079 | Barry / Bev | Provide exact Sage 300 version/build number for integration documentation | 2026-01-29 | Open | 9 |
| A-082 | Marcus | Establish revised target dates; prepare status update for Jaren and Rob with technical challenges and revised timeline | 2026-02-12 | Open | 8 |
| A-083 | Marcus / Varun | Complete Iteration 1 development; dev walkthrough completed 2026-02-24; development actively underway; demo environment unstable as of Apr 28 | 2026-02-12 | In Progress | 8 |
| A-104 | Christine | Consult Kinship department and QA to ensure licensing and placement info accurately represented in system design | 2026-03-26 | Open | 5 |
| A-105 | Marcus / Ross | Determine agency email account for external notification sends (Microsoft REST API integration) | 2026-03-26 | Open | 5 |
| A-106 | Marcus | Implement address-based search tab (search address fields on existing records; show associated individuals/cases, prioritized by open status) | 2026-03-26 | Open | 5 |
| A-107 | Marcus | Consult after-hours team to capture any additional requirements for address-based search feature | 2026-03-26 | Open | 5 |
| A-109 | Clemene | Provide Marcus with finance contact email for follow-up and summary sharing from last finance meeting | 2026-04-07 | Open | 4 |
| A-110 | Christine | Send recurring calendar invite for biweekly in-person meetings starting April 7th (all relevant participants) | 2026-04-07 | Open | 4 |
| A-112 | Clemene / Rob | Review contract and create a revised, clean project timeline and implementation schedule | 2026-04-07 | Open | 4 |
| A-114 | Ken Jacobs / Antonio Faiazza | Complete Azure post-setup: verify .onmicrosoft tenant access and permissions; share SQL DB credentials via secure private link; provide IDFusion office static IP for whitelisting; fine-tune RBAC group assignments | 2026-04-09 | In Progress | 3 |
| A-115 | Ken Jacobs / Marcus | Deploy Wabanong application code to Azure dev environment (PHP backend to App Service + React frontend to Web App) | 2026-04-23 | In Progress | 3 |
| A-116 | Marcus | Document Azure infrastructure recap (high-level) for Clemene; store in SharePoint | 2026-04-09 | Open | 3 |
| A-118 | Marcus / Gabrielle | Design and implement finance dashboard for finance users: track finance sheet requests, in-app notifications + email notifications for pending approvals; requirements documented Apr 24 & Apr 28 | 2026-04-23 | In Progress | 3 |
| A-119 | Marcus | Spec cleanup: spec sheet drop-downs only (remove buttons/radio buttons), update pronoun field to free-form, update person record spec (address tab, save button, genogram search clarity) | 2026-04-23 | In Progress | 3 |
| A-120 | Marcus | Clarify with Ross: (a) whether multiple open intakes per person are permitted, (b) assessment worker task assignment (direct assign vs. queue), (c) status terminology final confirmation | 2026-04-23 | Open | 3 |
| A-123 | Marcus | Define and document formal UAT sign-off procedure with IDFusion | 2026-04-30 | Open | 2 |
| A-124 | Kelvin / Clemene | Send abuse program forms and Excel template (PII removed) to IDFusion for requirements mapping; forms reviewed Apr 28; blank/redacted forms for copy-assist screen still needed (see A-154) | 2026-04-28 | In Progress | 2 |
| A-125 | Marcus | Share IDFusion's current abuse-related resources/forms with team; identify requirement gaps; intake form missing Manitoba CFS Act categories identified (see A-155) | 2026-04-28 | In Progress | 2 |
| A-126 | Marcus / Ross / Kelvin | Schedule and hold follow-up meeting to review abuse program requirements | 2026-04-30 | Complete | 1 |
| A-127 | Christine / Clemene | Provide IDFusion with complete list and definitions of all legal terms used by agency (SSG, agreements with minors, temporary/permanent orders, customary acceptance, etc.) | 2026-05-07 | Open | 2 |
| A-128 | Marcus / Clemene | Cross-reference agency law/regulations with system terminology to ensure consistency; Manitoba CFS Act vs Peguis legislation discussed Apr 28; statutory provisions referenced in wireframes | 2026-05-07 | In Progress | 2 |
| A-129 | IDFusion / Kelvin | Set up alpha testing access for Kelvin, Christine, and Darryl; coordinate review of language/forms before broader staff testing | 2026-05-07 | Open | 2 |
| A-130 | Marcus | Translate project timeline into Outlook calendar invites for key testing/review milestones | 2026-04-28 | Open | 2 |
| A-131 | IDFusion dev | Implement Apr 13 demo feedback items: fix Peguis footer typo; gender to Male/Female/Two-Spirit/Non-binary; add Child profile type option; auto age-18 profile upgrade (with confirmation); ID lookup table (Finance/Abuse/Intake/Case); abuse investigation tab with RBAC; address history with start/end dates + ordinary residence flag + note field; reserve/non-reserve auto-populate; CEFAS copy report; finance processing buttons (Intake/After Hours/Abuse/Prevention) | 2026-04-30 | Open | 2 |
| A-135 | IDFusion / Rob / Ross | Define post-go-live support tiers (bronze/silver/gold) and SLAs (e.g., 1-hour response for finance emergencies) | 2026-05-28 | Open | 2 |
| A-136 | Bev / Christine / Barry / Clemene | Send all finance templates and forms (face sheet, child maintenance Excel, visa rec, check rec, month-end report, chart of accounts) to Marcus/Gabrielle -- headers only, no PII; templates walked through Apr 24; RBC CSV headers still needed (see A-158) | 2026-04-28 | In Progress | 2 |
| A-137 | Bev | Send Sage 300 chart of accounts and all GL codes to Marcus/Gabrielle/Christine for integration mapping | 2026-04-28 | Open | 2 |
| A-138 | Marcus | Compile list of finance documents already received from Haley to avoid duplicate submissions | 2026-04-28 | Open | 2 |
| A-139 | Ross | Explore credit card receipt management options with finance team; full credit card reconciliation workflow designed Apr 24 & Apr 28: RBC export → Wabanon ingestion → card holder matching → receipt upload tasks → finance review → Sage export | 2026-05-07 | Complete | 1 |
| A-140 | Ross | Send abuse program master spreadsheet to Marcus/Gabrielle/Clemene/Christine | 2026-04-28 | Open | 2 |
| A-141 | Ross | Book Eagle Boardroom for IDFusion every Tuesday; send Teams invites for standing finance and ongoing services slots; Eagle Boardroom booked through September; Outlook/Teams invites to Bev/Barry for Tuesday finance slot still pending | 2026-04-25 | In Progress | 2 |
| A-142 | Gabrielle | Follow up with Sherry to confirm she has started testing | 2026-04-23 | Open | 2 |
| A-143 | Marcus | Add ClickUp task for address note field (ordinary residence complexity) | 2026-04-23 | Open | 2 |
| A-144 | Marcus | Spec update: remove "new task" button from person record; task creation only available in intake/case records | 2026-04-28 | Open | 2 |
| A-145 | Marcus | Validate case file wireframes/specs are complete; CRD team walkthrough completed Apr 29; revisions required | 2026-04-28 | In Progress | 2 |
| A-146 | Marcus | Create/update spec for case-specific documents tab (aligned with person record documents tab logic) | 2026-04-28 | Open | 2 |
| A-147 | Marcus | Schedule wireframe review meeting with ongoing services team (overview, case notes, placements tabs) | 2026-04-30 | Complete | 1 |
| A-148 | Marcus | Send finance/placements flow documentation to Gabrielle in advance of next finance requirements session | 2026-04-23 | Open | 2 |
| A-149 | Marcus / Gabrielle | Produce detailed wireframes for finance dashboard (PO queue, credit card queue, aging/timer displays) and share with Bev/Barry for review | 2026-05-21 | Open | 1 |
| A-150 | Marcus / Gabrielle | Update finance PO workflow wireframes based on Apr 24 & Apr 28 feedback (correct step sequence: worker request → supervisor approval → finance review → PO generation → receipt attachment → Sage export) | 2026-05-21 | Open | 1 |
| A-151 | Marcus / Gabrielle | Update abuse module wireframes: correct conclusion terminology; add "notice to provide information" step; update form routing to 3 options; add "Other" free-text to evidence reference categories; remove committee access screen; update timer logic for business hours and holidays | 2026-05-21 | Open | 1 |
| A-152 | Ross / IDFusion | Implement global holiday calendar in Wabanon system settings to support business-hour timer calculations for finance and abuse workflows | 2026-05-21 | Open | 1 |
| A-153 | Kelvin (PCFS) | Send finalized abuse investigation conclusion terminology (Valid Incident / Abuse Did Not Occur / Inconclusive + any others) to Ross/Marcus for implementation | 2026-05-21 | Open | 1 |
| A-154 | Kelvin (PCFS) | Provide blank/redacted provincial abuse investigation form fields to IDFusion for copy-assist screen field mapping | 2026-05-21 | Open | 1 |
| A-155 | Marcus | Follow up with intake team re: adding missing Manitoba CFS Act abuse issue categories to Wabanon intake form | 2026-05-21 | Open | 1 |
| A-156 | Marcus | Clarify with ongoing services/intake team how "parenting time" is determined for case anchoring when both parents are Peguis members | 2026-05-21 | Open | 1 |
| A-157 | Marcus / Gabrielle | Update ongoing services wireframes: add in-home/out-of-home toggle per person on case; rename "New Admission Checklist" to "Mandatory Child Services Checklist"; add director reference to case assignment view; confirm face sheet auto-trigger on placement save; add open case/file indicator column to persons-in-case table | 2026-05-21 | Open | 1 |
| A-158 | Bev / Barry (PCFS) | Send RBC bank export file column headers (CSV format) to IDFusion for building the Wabanon credit card import template | 2026-05-21 | Open | 1 |
| A-159 | Marcus | Schedule follow-up ongoing services wireframe review meeting with CRD team after wireframe revisions completed | 2026-05-21 | Open | 1 |
| A-160 | Ross (IDFusion) | Document "Finance Assigner" role in Wabanon role architecture: define queue visibility and task assignment capabilities | 2026-05-21 | Open | 1 |

---
## Issues and Risks

| ID | Description | Severity | Owner | Due Date | Status | Periods Open |
|----|-------------|---------|-------|----------|--------|-------------|
| I-018 | Finance/Sage integration requirements incomplete -- Sage 300 PO module specifics not yet clarified; PO workflow and credit card reconciliation requirements substantially documented at Apr 24 & Apr 28 meetings; GL codes and account numbers referenced throughout; formal receipt and integration design not yet started | Medium | Hailey / Marcus | 2026-01-29 | Open | 10 |
| I-029 | Timeline slippage -- original delivery targets missed; June 30 go-live confirmed as hard constraint by all parties and cited repeatedly as driver of design tradeoffs; formal contract re-baselining still pending (A-112) | High | Marcus | 2026-02-12 | Open | 8 |
| I-032 | Development timeline at risk -- Azure DevOps CI/CD infrastructure in place; application code deployment to Azure dev environment (A-115) is the critical immediate next step; demo environment crash Apr 28 confirms active development but unstable environment | High | Marcus | 2026-03-12 | Open | 6 |
| I-033 | Address-based search confirmed as new development requirement (2026-03-10) -- adds scope to an already-constrained timeline; impact on iteration sequencing not yet assessed | Medium | Marcus | 2026-03-26 | Open | 5 |
| I-034 | Client-side continuity risk -- Haley absent for 3+ months; Clemene covering; abuse program clerk Alice approaching retirement (noted by Kelvin Apr 28); auto-generated file number design partially mitigates; risk still active | Medium | Marcus / Ross | 2026-04-07 | Open | 4 |
| I-035 | Abuse program requirements substantially resolved -- two full sessions Apr 28 covered all major workflow elements; key decisions made; wireframe revisions in progress; remaining items are specific form field details and edge cases | Medium | Marcus / Kelvin / Clemene | 2026-04-30 | Open | 2 |
| I-036 | Alpha testing not started -- Sherry had not begun testing as of Apr 17; no update this period; delay risks downstream iteration sign-off timelines | Low | Gabrielle | 2026-04-30 | Open | 2 |
| I-037 | Demo environment crash at Apr 28 finance meeting -- Wabanon screens could not be shown; whiteboard walkthrough used instead; indicates dev environment instability risk for upcoming UAT cycles | Medium | Ross / IDFusion | 2026-05-21 | Open | 1 |
| I-038 | Wabanon intake form incomplete -- Kelvin identified current intake form missing mandatory Manitoba CFS Act abuse issue categories required for provincial reporting; must be resolved before abuse module can be finalized | Medium | Marcus | 2026-05-21 | Open | 1 |
| I-039 | Holiday calendar missing -- Wabanon timer logic does not yet account for observed holidays (including First Nations-specific and Friday holidays); required for accurate SLA tracking in finance and abuse workflows | Medium | Ross / IDFusion | 2026-05-21 | Open | 1 |

---
## Active Return to Green Plans

### Overall - Red (first flagged: 2025-W48)
- Complete Azure code deployment (A-115) and validate dev environment stability to unblock UAT and eliminate demo reliability risk
- Finalize abuse module and ongoing services wireframe revisions (A-151, A-157) to close the requirements phase for these modules
- Maintain Tuesday in-person cadence and weekly status reports; prioritize A-115 as the single most critical unlock

### Schedule - Red (first flagged: 2025-W48)
- Azure deployment (A-115) remains the critical-path unlock -- confirm before end of W21
- Complete Iteration 1 first UAT cycle to measure actual velocity against June 30 target
- Formally re-baseline contract timeline (A-112) -- all stakeholders have implicitly accepted June 30 but no signed-off schedule exists

### Scope - Yellow (first flagged: 2025-W50)
- Wireframe revisions for finance, abuse, and ongoing services must capture all Apr feedback before developer implementation begins
- New items from Apr sessions (holiday calendar, intake form categories, finance assigner role) are confirmed in-scope for V1; hold the line on further additions
- Continue deferring non-critical items (task automation, advanced reporting) to post-launch roadmap as agreed

### Budget - Yellow (first flagged: 2025-W50)
- Sage 300 PO module integration specifics still unclear -- clarify before implementation scoping to avoid cost surprises
- RBC export format and credit card reconciliation workflow finalized; confirm no Azure/infrastructure surprises as UAT environment comes online
- Assess whether intake form category additions (A-155) and holiday calendar (A-152) create out-of-scope development costs

### Client's Feeling - Yellow (first flagged: 2026-W13)
- CRD and abuse teams engaged and positive -- maintain momentum by delivering revised wireframes promptly after Apr sessions
- Finance team's demo crash managed via whiteboard; follow up with updated wireframes and a screen walkthrough before next Tuesday meeting
- Communicate June 30 realistic assessment clearly once Iteration 1 velocity is measurable

---
## Period History (rolling 4-week window)
_2025-W48, 2025-W50, 2025-W52/2026-W02, 2026-W05, 2026-W07, 2026-W09, 2026-W11, 2026-W13, 2026-W15, and 2026-W17 trimmed: all period ends are outside the 4-week window from today (2026-05-26). Full records in their respective status-reports/ .qmd files._

### 2026-W19 (2026-04-24 → 2026-05-07)
- **Health:** Overall/Schedule Red; Scope/Budget/Client's Feeling Yellow
- **Report:** `status-reports/2026-W19.qmd`
- **Summary:** Highly productive requirements sessions across Finance (Apr 24 & 28), Abuse Investigations (Apr 28), and Ongoing Services (Apr 29) with key architecture decisions locked for all three modules. Live demo crashed at the Apr 28 finance meeting, revealing dev environment instability; three new issues logged. Twelve new action items added from session feedback; credit card reconciliation workflow designed and abuse requirements gap substantially resolved.
""", encoding='utf-8')
print(f'project-state.md written: {STATE.stat().st_size:,} bytes')

# ── project-config.md ─────────────────────────────────────────────────────────
CONFIG = ROOT / 'project-config.md'
config_text = CONFIG.read_text(encoding='utf-8')
config_text = config_text.replace(
    '- **Current Period Start:** 2026-04-24',
    '- **Current Period Start:** 2026-05-08'
).replace(
    '- **Current Period End:** 2026-05-07',
    '- **Current Period End:** 2026-05-21'
)
CONFIG.write_text(config_text, encoding='utf-8')
print(f'project-config.md updated: {CONFIG.stat().st_size:,} bytes')

# ── extractions-current.md ────────────────────────────────────────────────────
EXT = ROOT / 'extractions-current.md'
EXT.write_text("""\
# Current Period Extractions — Custom-CMS
**Period:** 2026-W21 (2026-05-08 → 2026-05-21)
**Status:** Empty — awaiting ingest-meetings and extract-and-verify
""", encoding='utf-8')
print(f'extractions-current.md cleared: {EXT.stat().st_size:,} bytes')
