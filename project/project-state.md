# Project State - Custom-CMS
**Last Updated:** 2026-06-25
**Last Completed Period:** 2026-W21 (2026-05-08 → 2026-05-21)
**Periods Completed:** 12
**Next Action Item ID:** A-177
**Next Issue ID:** I-041

---
## Milestones
> Baseline End is immutable - agent proposes changes; user must confirm before state is updated.

| ID | Milestone | Baseline End | Estimated End | Status | Variance |
|----|-----------|-------------|---------------|--------|----------|
| M-01 | Stage 1 - Discovery and Requirements complete | 2025-12-22 | 2026-03-26 | Delayed | +94d |
| M-02 | Stage 2 - Solution Design complete | 2026-01-31 | 2026-03-26 | Delayed | +54d |
| M-03 | Stage 3 - All 9 iterations complete / system ready | 2026-03-31 | 2026-06-30 | Delayed | +91d |
| M-04 | Go-Live | 2026-03-31 | 2026-07-31 | Delayed | +122d |
| M-05 | Stage 4 - Post-launch support complete | 2026-04-30 | 2026-08-28 | Delayed | +120d |

---
## Action Items

| ID | Owner | Item | Due Date | Status | Periods Open |
|----|-------|------|----------|--------|-------------|
| A-055 | Hailey / Marcus | Clarify and document requirements for role-based access, high-profile cases, and conflict-of-interest restrictions; access model decisions made Apr 28 (three-tier confidentiality, include-based CoI model); May 6 locked restrict case (2 reasons), after-hours auto-access, kinship placement type restrictions | 2026-01-29 | In Progress | 10 |
| A-078 | Marcus | Prepare field-definitions Excel template (tab per screen, field names, dropdown values, rules column) | 2026-01-29 | Open | 10 |
| A-079 | Barry / Bev | Provide exact Sage 300 version/build number for integration documentation | 2026-01-29 | Open | 10 |
| A-082 | Marcus | Establish revised target dates; prepare status update for Jaren and Rob with technical challenges and revised timeline | 2026-02-12 | Open | 9 |
| A-083 | Marcus / Varun | Complete Iteration 1 development; dev walkthrough completed 2026-02-24; development actively underway; client+family data module UAT-ready as of May 11 | 2026-02-12 | In Progress | 9 |
| A-104 | Christine | Consult Kinship department and QA to ensure licensing and placement info accurately represented in system design | 2026-03-26 | Open | 6 |
| A-105 | Marcus / Ross | Determine agency email account for external notification sends (Microsoft REST API integration) | 2026-03-26 | Open | 6 |
| A-106 | Marcus | Implement address-based search tab (search address fields on existing records; show associated individuals/cases, prioritized by open status) | 2026-03-26 | Open | 6 |
| A-107 | Marcus | Consult after-hours team to capture any additional requirements for address-based search feature | 2026-03-26 | Open | 6 |
| A-109 | Clemene | Provide Marcus with finance contact email for follow-up | 2026-04-07 | Open | 5 |
| A-110 | Christine | Send recurring calendar invite for biweekly in-person meetings (all relevant participants) | 2026-04-07 | Open | 5 |
| A-112 | Clemene / Rob | Review contract and create a revised, clean project timeline and implementation schedule | 2026-04-07 | Open | 5 |
| A-114 | Ken Jacobs / Antonio Faiazza | Complete Azure post-setup: verify .onmicrosoft tenant access and permissions; share SQL DB credentials via secure private link; provide IDFusion office static IP for whitelisting; fine-tune RBAC group assignments | 2026-04-09 | In Progress | 4 |
| A-115 | Ken Jacobs / Marcus | Deploy Wabanong application code to Azure dev environment (PHP backend to App Service + React frontend to Web App) | 2026-04-23 | In Progress | 4 |
| A-116 | Marcus | Document Azure infrastructure recap (high-level) for Clemene; store in SharePoint | 2026-04-09 | Open | 4 |
| A-118 | Marcus / Gabrielle | Design and implement finance dashboard for finance users: track finance sheet requests, in-app notifications + email notifications for pending approvals | 2026-04-23 | In Progress | 4 |
| A-119 | Marcus | Spec cleanup: drop-downs only (remove buttons/radio buttons), update pronoun field to free-form, update person record spec (address tab, save button, genogram search clarity) | 2026-04-23 | In Progress | 4 |
| A-120 | Marcus | Clarify with Ross: (a) multiple open intakes per person permitted (confirmed warn/don't block), (b) task assignment confirmed as queue model, (c) status terminology confirmed Open/Closed only | 2026-04-23 | Complete | 4 |
| A-123 | Marcus | Define and document formal UAT sign-off procedure with IDFusion | 2026-04-30 | In Progress | 3 |
| A-124 | Kelvin / Clemene | Send abuse program forms and Excel template (PII removed) to IDFusion for requirements mapping; blank/redacted forms still needed (see A-154) | 2026-04-28 | In Progress | 3 |
| A-125 | Marcus | Share IDFusion's current abuse-related resources/forms with team; identify requirement gaps | 2026-04-28 | In Progress | 3 |
| A-127 | Christine / Clemene | Provide IDFusion with complete list and definitions of all legal terms used by agency (SSG, agreements with minors, temporary/permanent orders, customary acceptance, etc.) | 2026-05-07 | Open | 3 |
| A-128 | Marcus / Clemene | Cross-reference agency law/regulations with system terminology to ensure consistency; Manitoba CFS Act vs Peguis legislation discussed Apr 28 | 2026-05-07 | In Progress | 3 |
| A-129 | IDFusion / Kelvin | Set up alpha testing access for Kelvin, Christine, and Darryl; UAT tester list prepared (A-167); UAT walkthrough completed (A-175); formal sign-off procedure still pending | 2026-05-07 | In Progress | 3 |
| A-130 | Marcus | Translate project timeline into Outlook calendar invites for key testing/review milestones | 2026-04-28 | Open | 3 |
| A-131 | IDFusion dev | Implement Apr 13 demo feedback items: fix Peguis footer typo; gender to Male/Female/Two-Spirit/Non-binary; add Child profile type option; auto age-18 profile upgrade; ID lookup table; abuse investigation tab with RBAC; address history with start/end dates + ordinary residence flag; reserve/non-reserve auto-populate; CEFAS copy report; finance processing buttons | 2026-04-30 | Open | 3 |
| A-135 | IDFusion / Rob / Ross | Define post-go-live support tiers (bronze/silver/gold) and SLAs (e.g., 1-hour response for finance emergencies) | 2026-05-28 | Open | 3 |
| A-136 | Bev / Christine / Barry / Clemene | Send all finance templates and forms (headers only, no PII); RBC CSV headers still needed (see A-158) | 2026-04-28 | In Progress | 3 |
| A-137 | Bev | Send Sage 300 chart of accounts and all GL codes to Marcus/Gabrielle/Christine for integration mapping; GL codes received May 5 | 2026-04-28 | Complete | 3 |
| A-138 | Marcus | Compile list of finance documents already received from Haley to avoid duplicate submissions | 2026-04-28 | Open | 3 |
| A-140 | Ross | Send abuse program master spreadsheet to Marcus/Gabrielle/Clemene/Christine | 2026-04-28 | Open | 3 |
| A-141 | Ross | Book Eagle Boardroom for IDFusion every Tuesday; send Teams invites for standing finance and ongoing services slots; Outlook/Teams invites to Bev/Barry for Tuesday finance slot still pending | 2026-04-25 | In Progress | 3 |
| A-142 | Gabrielle | Follow up with Sherry to confirm she has started testing | 2026-04-23 | Open | 3 |
| A-143 | Marcus | Add ClickUp task for address note field (ordinary residence complexity) | 2026-04-23 | Open | 3 |
| A-144 | Marcus | Spec update: remove "new task" button from person record; task creation only available in intake/case records | 2026-04-28 | Open | 3 |
| A-145 | Marcus | Validate case file wireframes/specs; CRD walkthrough completed Apr 29; May 6 session 2 completed; wireframe updates done (A-163, A-164, A-165 resolved) | 2026-04-28 | In Progress | 3 |
| A-146 | Marcus | Create/update spec for case-specific documents tab (aligned with person record documents tab logic) | 2026-04-28 | Open | 3 |
| A-148 | Marcus | Send finance/placements flow documentation to Gabrielle in advance of next finance requirements session | 2026-04-23 | Open | 3 |
| A-149 | Marcus / Gabrielle | Produce detailed wireframes for finance dashboard (PO queue, credit card queue, aging/timer displays) and share with Bev/Barry for review | 2026-05-21 | Open | 2 |
| A-150 | Marcus / Gabrielle | Update finance PO workflow wireframes: worker request → supervisor approval → finance review → PO generation → receipt attachment → Sage export | 2026-05-21 | Open | 2 |
| A-151 | Marcus / Gabrielle | Update abuse module wireframes: redesign as intake-form wizard per May 11 reset decision; specific items include correct conclusion terminology, 'notice to provide information' step, 3 form routing options, 'Other' free-text for evidence categories, timer logic for business hours/holidays (see A-170) | 2026-05-21 | In Progress | 2 |
| A-152 | Ross / IDFusion | Implement global holiday calendar in Wabanong system settings to support business-hour timer calculations for finance and abuse workflows | 2026-05-21 | Open | 2 |
| A-153 | Kelvin (PCFS) | Send finalized abuse investigation conclusion terminology (Valid Incident / Abuse Did Not Occur / Inconclusive + any others) to Ross/Marcus for implementation | 2026-05-21 | Open | 2 |
| A-154 | Kelvin (PCFS) | Provide blank/redacted provincial abuse investigation form fields to IDFusion for copy-assist screen field mapping | 2026-05-21 | Open | 2 |
| A-155 | Marcus | Follow up with intake team re: adding missing Manitoba CFS Act abuse issue categories to Wabanong intake form; Darryl to provide full list (see A-161) | 2026-05-21 | In Progress | 2 |
| A-156 | Marcus | Clarify with ongoing services/intake team how "parenting time" is determined for case anchoring when both parents are Peguis members | 2026-05-21 | Open | 2 |
| A-157 | Marcus / Gabrielle | Update ongoing services wireframes: add in-home/out-of-home toggle per person on case; rename "New Admission Checklist" to "Mandatory Child Services Checklist"; add director reference to case assignment view; IRAP rate sheet trigger (placement change → worker task → CRD approval); confirm face sheet as manual Finance tab button | 2026-05-21 | In Progress | 2 |
| A-158 | Bev / Barry (PCFS) | Send RBC bank export file column headers (CSV format) to IDFusion for building the Wabanong credit card import template | 2026-05-21 | Open | 2 |
| A-159 | Marcus | Schedule follow-up ongoing services wireframe review meeting with CRD team after wireframe revisions completed | 2026-05-21 | Open | 2 |
| A-160 | Ross (IDFusion) | Document "Finance Assigner" role in Wabanong role architecture: define queue visibility and task assignment capabilities | 2026-05-21 | Open | 2 |
| A-161 | Darryl Boulanger (PCFS) | Provide complete issue categories and subcategories list from provincial IM form (with timeframes per category) to IDFusion for intake form update | 2026-05-21 | Open | 1 |
| A-162 | Marcus / Gabrielle | Update intake wireframes: expand issue categories to two-level selection (category → subcategory with timeframes), update actions-taken section, add document types (Receipts/Legal/Safety/Other) to upload modal | 2026-05-21 | Complete | 1 |
| A-163 | Gabrielle | Update case file wireframes: restrict legal doc upload to legal team/supervisors/directors; legal order expiry notifications (40/30/14-day escalation); EPR 90-day tracker; remove "Change Case Type" modal; update Restrict Case UI (2 reasons + searchable viewer add + after-hours auto-access); remove legal agreement drop-down from placement tab | 2026-06-04 | Complete | 1 |
| A-164 | Gabrielle | Update placement wireframes: kinship-only placement types, "Generate Face Sheet" button on Finance tab, IRAP rate sheet trigger tasks (new placement and change of placement workflows) | 2026-06-04 | Complete | 1 |
| A-165 | Gabrielle | Update Signs of Safety wireframes: multiple harm matrices with history; harm matrix triggers risk assessment task; risk ≥6 triggers safety plan task; safety plan active/inactive status + final option; supervisor review cadence (quarterly default, weekly at risk ≥9) | 2026-06-04 | Complete | 1 |
| A-166 | Ross / Campfire | Configure Azure UAT environment: set up temporary Entra/conditional access accounts for all testers (PCFS + IDFusion team) with expiry | 2026-05-21 | Complete | 1 |
| A-167 | Ross / Kelvin / Christina | Compile UAT tester list (name, role, contact info) and draft anonymized testing scenarios for client+family data module | 2026-05-21 | Complete | 1 |
| A-168 | Ross / Campfire | Investigate FamCare SQL database (1–1.5 year old version) as migration data source; confirm structure and availability | 2026-06-04 | Complete | 1 |
| A-169 | Ross | Complete Varun Mehra's vulnerable sector check before granting any access to FamCare data | 2026-06-04 | Complete | 1 |
| A-170 | Marcus / Gabrielle | Redesign abuse module as intake-form wizard (step-based entry matching current paper form workflow); produce initial wireframes for next Kelvin review session | 2026-06-04 | In Progress | 1 |
| A-171 | Marcus (Rob) | Send updated PCFS status report: revised go-live end of July 2026, abuse as separate iteration, updated meeting cadence | 2026-05-21 | Open | 1 |
| A-172 | Kelvin (PCFS) | Reach out to service delivery team to confirm availability for case file automated task assignments form review | 2026-05-21 | Complete | 1 |
| A-173 | Marcus / Gabrielle | Update case notes spec: tighten intro, consolidate document types list (3 occurrences → single source), fix supervision tag (filterable but not creatable by workers), remove visits category forward reference, clarify document upload behavior; add standard logging definition at top of all spec docs | 2026-05-21 | Complete | 1 |
| A-174 | Gabrielle / Varun | Set up Freshdesk UAT feedback triage: devteam@idfusion.com → Freshdesk → ClickUp; configure reporting for Ross (open/closed/backlog per ticket) | 2026-05-21 | Complete | 1 |
| A-175 | Marcus | Run UAT kickoff walkthrough for client+family data module with PCFS testers (~1 hour); record session for absent testers | 2026-05-21 | Complete | 1 |
| A-176 | Marcus | Clarify with finance team which budget pool covers intake-related purchases (operations vs. prevention/family service budget) | 2026-05-21 | Open | 1 |

---
## Issues and Risks

| ID | Description | Severity | Owner | Due Date | Status | Periods Open |
|----|-------------|---------|-------|----------|--------|-------------|
| I-018 | Finance/Sage integration requirements incomplete — Sage 300 PO module specifics not yet clarified; PO workflow and credit card reconciliation substantially documented; formal receipt and integration design not yet started | Medium | Hailey / Marcus | 2026-01-29 | Open | 11 |
| I-029 | Timeline slippage — go-live revised to end of July 2026 at May 11 reset meeting; all key stakeholders aligned; formal contract re-baselining still pending (A-112) | High | Marcus | 2026-02-12 | Open | 9 |
| I-032 | Development timeline at risk — client+family data module now UAT-ready; Azure Entra environment resolved; intake and notifications in late dev/QA; demo environment instability from Apr 28 substantially resolved | High | Marcus | 2026-03-12 | Open | 7 |
| I-033 | Address-based search confirmed as new development requirement — adds scope to constrained timeline; iteration sequencing impact not yet assessed | Medium | Marcus | 2026-03-26 | Open | 6 |
| I-034 | Client-side continuity risk — Haley absent 3+ months; Clemene covering; abuse program clerk Alice approaching retirement (noted by Kelvin Apr 28) | Medium | Marcus / Ross | 2026-04-07 | Open | 5 |
| I-035 | Abuse program — May 11 decision carved out as separate wizard-style iteration; approach clarified; initial wireframes in progress (A-170); specific form details (A-153, A-154) still pending | Medium | Marcus / Kelvin / Clemene | 2026-04-30 | Open | 3 |
| I-036 | UAT now active — process formally defined (Freshdesk → ClickUp pipeline); tester list prepared; client+family data module UAT walkthrough completed; Freshdesk triage operational | Low | Gabrielle | 2026-04-30 | Open | 3 |
| I-037 | Demo environment crash at Apr 28 finance meeting — UAT environment now set up in PCFS Azure; risk substantially reduced | Medium | Ross / IDFusion | 2026-05-21 | Open | 2 |
| I-038 | Wabanong intake form incomplete — current form missing mandatory Manitoba CFS Act abuse issue categories required for provincial reporting; Darryl to provide full list (A-161) | Medium | Marcus | 2026-05-21 | Open | 2 |
| I-039 | Holiday calendar missing — Wabanong timer logic does not yet account for observed holidays; required for accurate SLA tracking in finance and abuse workflows | Medium | Ross / IDFusion | 2026-05-21 | Open | 2 |
| I-040 | Azure Entra/conditional access setup delayed UAT kickoff — tester accounts could not be created until Entra configuration resolved; resolved via A-166 | Medium | Ross / Campfire | 2026-05-21 | Resolved | 1 |

---
## Active Return to Green Plans

### Overall - Red (first flagged: 2025-W48)
- Complete client+family data UAT cycle within W23 and begin triage of feedback via Freshdesk → ClickUp pipeline
- Deliver abuse module redesign wireframes (A-170) and schedule Kelvin review session to keep the separate abuse iteration moving
- Maintain new weekly Marcus/Ross/Christina cadence; bring Kelvin in only for specific module reviews

### Schedule - Red (first flagged: 2025-W48)
- Send updated PCFS status report communicating July end-of-month target (A-171); ensure Clemene has formal acknowledgment
- Formally re-baseline contract timeline (A-112) — all key stakeholders aligned on July; no signed-off schedule exists yet
- Complete client+family data UAT cycle in W23 to measure actual velocity before scheduling remaining module iterations

### Scope - Yellow (first flagged: 2025-W50)
- Signs of Safety additions from May 6 confirmed in-scope; wireframe updates completed (A-163–A-165) — developers can now begin implementation
- Skabe Support V2 deferral agreed at May 11 — communicate formally to stakeholders to prevent scope re-entry
- Abuse iteration scope to be locked before wireframe kickoff (A-170 in progress); route all new requests through agreed roadmap framework

### Budget - Yellow (first flagged: 2025-W50)
- Abuse as separate iteration may require contract amendment — flag to Rob and Clemene when sending updated status report (A-171)
- No new cost exposures this period; monitor Azure environment costs as UAT and production environments come online
- Confirm whether intake category additions (A-161) and holiday calendar (A-152) create out-of-scope development costs

### Client's Feeling - Yellow (first flagged: 2026-W13)
- May 11 reset meeting had constructive, collaborative tone; Kelvin and Christina actively engaged; maintain this momentum
- Send updated status report promptly (A-171) before client starts wondering about the July timeline commitment
- Monitor Clemene's engagement; July target needs formal acknowledgment at leadership level

---
## Period History (rolling 4-week window)
_2025-W48, 2025-W50, 2025-W52/2026-W02, 2026-W05, 2026-W07, 2026-W09, 2026-W11, 2026-W13, 2026-W15, 2026-W17, and 2026-W19 trimmed: all period ends are outside the 4-week window from today (2026-06-25). Full records in their respective status-reports/ .qmd files._

### 2026-W21 (2026-05-08 → 2026-05-21)
- **Health:** Overall/Schedule Red; Scope/Budget/Client's Feeling Yellow
- **Report:** `status-reports/2026-W21.qmd`
- **Summary:** Formal project reset at May 11 aligned PCFS leadership on a July end-of-month go-live target, carving the abuse module out as a separate iteration and resetting the weekly stakeholder cadence to Marcus/Ross/Christina. Case file and intake wireframe reviews were completed (May 5–6, late W19 meetings), client and family data module UAT was launched, and the Freshdesk feedback pipeline was established — marking the start of structured user testing.
