# Project State - Custom-CMS
**Last Updated:** 2026-08-19
**Last Completed Period:** 2026-W33 (2026-07-31 → 2026-08-06)
**Periods Completed:** 20
**Next Action Item ID:** A-223
**Next Issue ID:** I-044

---
## Milestones
> Baseline End is immutable - agent proposes changes; user must confirm before state is updated.

| ID | Milestone | Baseline End | Estimated End | Status | Variance |
|----|-----------|-------------|---------------|--------|----------|
| M-01 | Stage 1 - Discovery and Requirements complete | 2025-12-22 | 2026-03-26 | Delayed | +94d |
| M-02 | Stage 2 - Solution Design complete | 2026-01-31 | 2026-03-26 | Delayed | +54d |
| M-03 | Stage 3 - All 9 iterations complete / system ready | 2026-03-31 | 2026-07-25 | Delayed | +116d |
| M-04 | Go-Live | 2026-03-31 | 2026-07-31 | Delayed | +122d |
| M-05 | Stage 4 - Post-launch support complete | 2026-04-30 | 2026-08-28 | Delayed | +120d |

> Note: M-04's Estimated End (2026-07-31) is now overdue with no go-live. No new estimate proposed this period — evidence didn't supply one. Revisit once A-220 (contingency-budget/timeline update from Rob's team) lands.

---
## Action Items

| ID | Owner | Item | Due Date | Status | Periods Open |
|----|-------|------|----------|--------|-------------|
| A-104 | Christine | Consult Kinship department and QA to ensure licensing and placement info accurately represented in system design | 2026-03-26 | Open | 13 |
| A-118 | Marcus / Gabrielle | Design and implement finance dashboard for finance users: track finance sheet requests, in-app notifications + email notifications for pending approvals; GL mapping, PO flow, and summary view approach confirmed in June 19 session | 2026-04-23 | In Progress | 11 |
| A-127 | Christine / Clemene / Marcus | Provide IDFusion with complete list and definitions of all legal terms used by agency (SSG, agreements with minors, temporary/permanent orders, customary acceptance, etc.), then cross-reference agency law/regulations with system terminology to ensure consistency (Manitoba CFS Act vs Peguis legislation discussed Apr 28) | 2026-05-07 | In Progress | 10 |
| A-129 | IDFusion / Kelvin | Set up alpha testing access for Kelvin, Christine, and Darryl; client+family data UAT walkthrough completed (A-175); intake module UAT walkthrough completed June 16; formal sign-off procedure still pending | 2026-05-07 | In Progress | 10 |
| A-130 | Marcus | Translate project timeline into Outlook calendar invites for key testing/review milestones | 2026-04-28 | Open | 10 |
| A-131 | IDFusion dev | Implement Apr 13 demo feedback items: fix Peguis footer typo; gender to Male/Female/Two-Spirit/Non-binary; add Child profile type option; auto age-18 profile upgrade; ID lookup table; abuse investigation tab with RBAC; address history with start/end dates + ordinary residence flag; reserve/non-reserve auto-populate; CEFAS copy report; finance processing buttons | 2026-04-30 | Open | 10 |
| A-135 | IDFusion / Rob / Ross | Define post-go-live support tiers (bronze/silver/gold) and SLAs (e.g., 1-hour response for finance emergencies) | 2026-05-28 | Open | 10 |
| A-136 | Bev / Christine / Barry / Clemene | Send all finance templates and forms (headers only, no PII); Bev's GL code / chart of accounts reviewed June 19; RBC bank export file column headers (CSV format) still needed for building the Wabanong credit card import template | 2026-04-28 | In Progress | 10 |
| A-150 | Marcus / Gabrielle | Update finance PO workflow wireframes: button on intake/case → itemized form → auto GL mapping (determined by address and intake type) → Sage export; reviewed live with client July 3; per that review also apply: custom date-range filter, rename "Source" column to "Source reference", add "Funding category" column, add "Export to PDF" button, add "Reset view" button | 2026-05-21 | In Progress | 9 |
| A-151 | Marcus / Gabrielle | Redesign abuse module as intake-form wizard per May 11 reset decision (step-based entry matching current paper form workflow); specific items include correct conclusion terminology, 'notice to provide information' step, 3 form routing options, 'Other' free-text for evidence categories, timer logic for business hours/holidays; produce wireframes for Kelvin review session | 2026-05-21 | In Progress | 9 |
| A-152 | Ross / IDFusion | Implement global holiday calendar in Wabanong system settings to support business-hour timer calculations for finance and abuse workflows | 2026-05-21 | Open | 9 |
| A-153 | Kelvin (PCFS) | Send finalized abuse investigation conclusion terminology (Valid Incident / Abuse Did Not Occur / Inconclusive + any others) to Ross/Marcus, and provide blank/redacted provincial abuse investigation form fields to IDFusion for copy-assist screen field mapping | 2026-05-21 | Open | 9 |
| A-155 | Marcus / Darryl Boulanger (PCFS) | Follow up with intake team re: adding missing Manitoba CFS Act abuse issue categories to Wabanong intake form; Darryl to provide complete issue categories/subcategories list from provincial IM form (with timeframes per category) | 2026-05-21 | In Progress | 9 |
| A-156 | Marcus | Clarify with ongoing services/intake team how "parenting time" is determined for case anchoring when both parents are Peguis members | 2026-05-21 | Open | 9 |
| A-157 | Marcus / Gabrielle | Update ongoing services wireframes: add in-home/out-of-home toggle per person on case; rename "New Admission Checklist" to "Mandatory Child Services Checklist"; add director reference to case assignment view; IRAP rate sheet trigger (placement change → worker task → CRD approval); confirm face sheet as manual Finance tab button — then schedule follow-up review meeting with CRD team | 2026-05-21 | In Progress | 9 |
| A-160 | Ross (IDFusion) | Document "Finance Assigner" role in Wabanong role architecture: define queue visibility and task assignment capabilities | 2026-05-21 | Open | 9 |
| A-171 | Marcus (Rob) | Send updated PCFS status report: revised go-live end of July 2026, abuse as separate iteration, updated meeting cadence | 2026-05-21 | Open | 8 |
| A-176 | Marcus | Clarify with finance team which budget pool covers intake-related purchases (operations vs. prevention/family service budget) | 2026-05-21 | Open | 8 |
| A-177 | Gabrielle | Implement dual supervisor task assignment in intake task modal: default to general pool with option for specific supervisor assignment | 2026-07-02 | Open | 7 |
| A-178 | Gabrielle | Add optional case synopsis/summary field at end of intake form; carry over to case file (visible if populated, hidden if empty) | 2026-07-02 | Open | 7 |
| A-179 | Gabrielle | Submit development ticket for issue categories expansion to full CFIS list (all subcategories); confirmed must-have before go-live | 2026-07-02 | Open | 7 |
| A-180 | Ross / Darryl | Schedule follow-up intake practice run sessions for PCFS team; use real-world scenarios with anonymized data; coordinate with Marcus/Gabrielle for follow-up review meetings | 2026-07-02 | Open | 7 |
| A-181 | Ross / Gabrielle / Marcus | Define and implement intake supervisor finance permissions: read + ability to change family budgets; include after-hours access; review scope with Darryl in upcoming finance module session | 2026-07-02 | Open | 7 |
| A-182 | Marcus | Following June 16 meeting: activate UAT accounts for newly added team members, and send UAT session summary to all participants (role assignments chart + feedback submission instructions, devteam@idfusion.com + cc Ross/Kelvin/Christina) | 2026-06-18 | Open | 7 |
| A-184 | Gabrielle | Create/confirm bug ticket for "open services" not showing in person search results when initiating a new intake | 2026-06-18 | Open | 7 |
| A-187 | Rob / Marcus / Gabrielle | Review all shared finance documentation (GL codes, funding streams, PO forms, process maps); compile requirements summary for finance module data entry screens, then schedule a follow-up finance design session with Rob | 2026-07-02 | Open | 6 |
| A-189 | Marcus / Ross / Varun | Obtain access to live (scrubbed) FAMCare production data for IDFusion — needed to confirm what data PCFS actually uses before finalizing migration scripts. Varun to review Data Veil (and Ken's input) for production-data anonymization, finalize tool/approach, and confirm which data fields migrate from FAMCare. Due date passed 2026-07-15 without resolution. | 2026-07-15 | Open | 6 |
| A-197 | Ross / Marcus / Gabrielle | Schedule and hold a meeting with Barry, Calvin, and other relevant staff to align frontline and finance terminology (prevention/protection, maintenance), and document which roles are responsible for deciding whether expenses are federally or provincially funded | 2026-07-09 | Open | 5 |
| A-201 | IDFusion dev | Implement "Complete Task" button (replacing "Edit Task") with Yes/No confirmation dialog | 2026-07-09 | Open | 5 |
| A-202 | Marcus | Compile and send Ross a consolidated go-live readiness update covering: training-video documentation scope/approach (after circling back with Rob), go-live order-of-operations/timeline for FamCare rollover, switch-over/AMS support agreement details, and next-priority roadmap planning (events, Community Circle of Care); internally discussed/drafted Jul 17, still not sent to Ross — increasingly overdue given the confirmed timeline slip | 2026-07-16 | Open | 4 |
| A-205 | Ross | Pre-identify key test cases and perform side-by-side checks after DB import to confirm data migrated correctly with no sensitive data exposed | 2026-07-16 | Open | 4 |
| A-206 | Ross / Varun | Schedule pre-go-live stress test (simultaneous login load test) as part of go-live activities; reconfirmed as a firm Ross request during cutover-plan review (Jul 21–22) | 2026-07-16 | Open | 4 |
| A-208 | Marcus | Check with Gabrielle on current state of service-referral functionality (Rainbow Lodge/Sun Lodge-type referrals) | 2026-07-16 | Open | 4 |
| A-209 | Varun | Review the revised data migration/cutover plan; confirm test-environment access and whether PHP needs to be installed there for migration scripts | 2026-07-27 | Open | 3 |
| A-210 | Marcus | Reconcile signed-SOW status with Rob — a signed copy was already sent to Ross on Jul 15; confirm with Rob/Ross that a copy is on file | 2026-07-23 | Open | 3 |
| A-212 | Gabrielle | Review the finance process for ongoing services with Ross's team (session planned Jul 23) | 2026-07-23 | Open | 3 |
| A-213 | Marcus / Rob | Assess whether a change request and contingency budget are needed to handle FAMCare's database structure during migration scripting — confirmed by Rob (Jul 30) as needed; amount still TBD pending further data assessment | 2026-07-27 | Open | 3 |
| A-214 | IDFusion dev | Send Rupen and Leanne the test-environment access email and a cheat sheet for logging tickets | 2026-07-30 | Open | 2 |
| A-215 | Ross | Pull the organizational chart from Bamboo and send CRD/supervisor/worker names to IDFusion so test users and reporting lines can be set up | 2026-08-06 | Open | 2 |
| A-216 | Ross | Coordinate a pretest session with CRDs and supervisors to validate worker/supervisor/director views, and send the meeting invite for the testing session (targeting Aug 7) | 2026-08-07 | Open | 2 |
| A-217 | IDFusion dev | Fix two case-file bugs surfaced during the Jul 28 UAT walkthrough: (1) child-in-care cases currently open under the parent instead of the child — needs a case-creation dropdown to select the child; (2) reassigning a case's supervisor incorrectly also changed the assigned director | 2026-08-06 | Open | 2 |
| A-218 | IDFusion dev / Ross | Correct the placement-type dropdown list (current list doesn't match required types) and create a "Wabanong admin" role with placement-creation permissions (equivalent to today's FamCare admin, e.g. for Hope) before case file UAT resumes | 2026-08-06 | Open | 2 |
| A-219 | Marcus / Varun / Ross / Rob | Meet with Campfire Help Desk to begin building the Waabanong production environment — kickoff meeting held Aug 4; Ross expected the build completed that week | 2026-07-31 | Open | 2 |
| A-220 | Rob / Varun | Provide an updated contingency-budget usage estimate and revised project timeline once FAMCare database access is obtained and assessed | 2026-08-13 | Open | 1 |
| A-221 | Ross | Relay Rob's UAT-pacing context to PCFS staff and keep expectations aligned as staggered module-by-module testing continues | 2026-08-06 | Open | 1 |
| A-222 | Varun | Once the production environment build completes, begin working with a copy of the FAMCare database for the data migration | 2026-08-06 | Open | 1 |

---
## Issues and Risks

| ID | Description | Severity | Owner | Due Date | Status | Periods Open |
|----|-------------|---------|-------|----------|--------|-------------|
| I-018 | Finance/Sage integration requirements incomplete — June 19 session advanced funding stream mapping, GL code structure, and PO workflow design; formal data entry screen design and Sage integration still pending | Medium | Hailey / Marcus | 2026-01-29 | Open | 18 |
| I-029 | Timeline slippage — go-live revised to end of July 2026 at May 11 reset meeting; formal contract re-baselining still pending. Rob explicitly confirmed (Jul 30) the go-live timeline is slipping again, citing two named causes: slower-than-expected live-data access, and staggered UAT delaying reporting/dashboard module design. | High | Marcus | 2026-02-12 | Open | 16 |
| I-032 | Development timeline at risk — intake module UAT underway; finance module in early design; case file and abuse iterations still ahead | High | Marcus | 2026-03-12 | Open | 14 |
| I-033 | Address-based search confirmed as new development requirement — moved to roadmap (A-106, A-107 resolved); iteration sequencing impact to be assessed at roadmap review | Medium | Marcus | 2026-03-26 | Open | 13 |
| I-034 | Client-side continuity risk — Haley absent 3+ months; Clemene covering; abuse program clerk Alice approaching retirement (noted by Kelvin Apr 28) | Medium | Marcus / Ross | 2026-04-07 | Open | 12 |
| I-035 | Abuse program — May 11 decision carved out as separate wizard-style iteration; approach clarified; initial wireframes in progress (A-151); specific form details still pending (A-153). Internal testing just started (per Jul 22 update); UAT not expected ready until week of Aug 3. | Medium | Marcus / Kelvin / Clemene | 2026-04-30 | Open | 10 |
| I-036 | UAT pipeline fully operational — Freshdesk → ClickUp triage active; client+family data module UAT complete; intake module UAT walkthrough completed June 16 | Low | Gabrielle | 2026-04-30 | Open | 10 |
| I-037 | Demo environment crash at Apr 28 finance meeting — UAT environment now set up in PCFS Azure; risk substantially reduced | Medium | Ross / IDFusion | 2026-05-21 | Open | 9 |
| I-038 | Wabanong intake form incomplete — full CFIS issue categories expansion confirmed as mandatory pre-go-live requirement at June 16 UAT session; development ticket submitted (A-179); Darryl's source list still pending (A-161) | Medium | Marcus | 2026-05-21 | Open | 9 |
| I-039 | Holiday calendar missing — Wabanong timer logic does not yet account for observed holidays; required for accurate SLA tracking in finance and abuse workflows | Medium | Ross / IDFusion | 2026-05-21 | Open | 9 |
| I-041 | UAT bug: "open services" not showing in person search results — when initiating a new intake, existing open case files should be surfaced in search; currently not working as expected; Gabrielle created ticket during June 16 session | Low | Gabrielle | 2026-06-18 | Open | 7 |
| I-042 | FAMCare live schema diverges significantly from the test snapshot (89 additional tables, 28 tables with column changes) — risks inaccurate migration scripts if not resolved before finalizing FAMCare→Wabanong migration; anonymization approach still being scoped (Data Veil evaluation underway, see A-189). Contingency-budget need confirmed as real by Rob (Jul 30) — no longer just a possibility; amount still unknown pending further data assessment. | Medium-High | Varun / Marcus | 2026-07-09 | Open | 5 |
| I-043 | Client requesting event management (Category E) and Community Circle of Care functionality be pulled into near-term planning; IDFusion team has no capacity within current schedule — risk of scope-expectation mismatch if not managed via clear roadmap conversation. Marcus's Jul 15 email to Ross independently corroborates that protection services/CCC were never in the original Hailey-scoped requirements, strengthening the case for holding the phase-one scope line. | Medium | Marcus | 2026-07-16 | Open | 4 |

---
## Active Return to Green Plans

### Overall - Red (first flagged: 2025-W48)
- Complete intake UAT cycle (A-180); triage all feedback through Freshdesk → ClickUp pipeline
- Advance finance module from design to wireframes (A-150) and get client sign-off before finance UAT
- Build the production environment with Campfire (A-219)
- Fix the case-reference and director-reassignment bugs before broader case file testing continues (A-217); correct the placement-type list and stand up the Wabanong admin role (A-218)
- Resolve production-data anonymization approach so scrubbed FAMCare data becomes available for migration testing (A-189, I-042) — due date already passed
- Deliver the consolidated go-live readiness update to Ross — now more urgent given the confirmed timeline slip (A-202)
- Get the updated contingency-budget usage and revised timeline from Rob's team once DB access is obtained (A-220)
- Begin FAMCare data migration work once the production environment build completes (A-222)

### Schedule - Red (first flagged: 2025-W48)
- Formally re-baseline contract timeline with Clemene/Rob — July 31 go-live target needs a signed-off schedule
- Identify critical path: intake UAT → case file UAT → finance UAT → abuse UAT → go-live; confirm each module's UAT readiness date
- Schedule pre-go-live stress test as part of go-live activities (A-206)
- Get Varun's sign-off on the revised cutover plan and resolve test-environment/PHP access (A-209)
- Hold the CRD/supervisor pretest session targeting Aug 7 (A-216)

### Scope - Yellow (first flagged: 2025-W50)
- Finance scope now partially locked; complete scope definition after Rob's documentation review (A-187)
- Align frontline/finance terminology and funding-determination role ownership (A-197)
- Hold roadmap/capacity conversation on event management (Category E) and Community Circle of Care to manage scope-expectation risk (I-043)
- Confirm service-referral functionality status with Gabrielle before committing to any scope changes (A-208)

### Budget - Yellow (first flagged: 2025-W50)
- Finance module design underway; confirm scope limits with Rob and Clemene before full design begins
- Abuse contract amendment still outstanding (A-171); include in next PCFS status report
- Assess FAMCare CR/contingency-budget need before it becomes a blocker on migration scripting (A-213)

---
## Period History (rolling 4-week window)

### 2026-W31 (2026-07-17 → 2026-07-23)
- **Health:** Overall/Schedule Red; Scope/Budget Yellow; Client's Feeling Green
- **Report:** `status-reports/2026-W31.qmd`
- **Summary:** Cutover planning advanced — a data migration/cutover brief was drafted, circulated, and revised per Rob's feedback, and Rob flagged that FAMCare's poor database structure may require a change request and contingency-budget spend to complete migration scripting. Case file functionality was opened early to unblock UAT testing. Client engagement rebounded to Green after last period's capacity friction — Ross and team were cooperative and accommodating despite a busy Treaty Days week. Five new action items were opened, including reconciling a signed-SOW mixup with Rob and scheduling the still-pending case management UAT walkthrough.

### 2026-W32 (2026-07-24 → 2026-07-30)
- **Health:** Overall/Schedule Red; Scope/Budget Yellow; Client's Feeling Green
- **Report:** `status-reports/2026-W32.qmd`
- **Summary:** Real forward momentum — Ross confirmed readiness to begin building the Waabanong production environment (Campfire kickoff planned for the following week), and case file UAT formally launched with a full walkthrough that brought two new CRD testers (Rupen, Leanne) into the pool. The walkthrough surfaced two concrete bugs (case-reference structure for child-in-care cases, and a director field incorrectly changing on supervisor reassignment) that need fixing before broader testing continues, plus follow-up work to correct the placement-type list and stand up a dedicated "Wabanong admin" role. A-211 (hold the UAT walkthrough) closed out complete.

### 2026-W33 (2026-07-31 → 2026-08-06)
- **Health:** Overall/Schedule Red; Scope/Budget Yellow; Client's Feeling Green
- **Report:** `status-reports/2026-W33.qmd`
- **Summary:** Rob confirmed (relayed via Ross's Aug 4 reply) that FAMCare's source data is rougher than expected and the project's contingency budget will be drawn on for migration cleanup — exact amount still being assessed. The go-live timeline is confirmed slipping again, for two named reasons: slower-than-expected live-data access, and staggered UAT delaying reporting/dashboard module design. Ross reconfirmed his preference for accuracy over deadline and personally kicked off the production-environment build with IDFusion and PCFS's IT provider. Client engagement remained strongly positive despite the schedule news.
