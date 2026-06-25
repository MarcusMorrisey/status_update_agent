# Project State - Custom-CMS
**Last Updated:** 2026-06-25
**Last Completed Period:** 2026-W27 (2026-06-19 → 2026-07-02)
**Periods Completed:** 15
**Next Action Item ID:** A-189
**Next Issue ID:** I-042

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

---
## Action Items

| ID | Owner | Item | Due Date | Status | Periods Open |
|----|-------|------|----------|--------|-------------|
| A-104 | Christine | Consult Kinship department and QA to ensure licensing and placement info accurately represented in system design | 2026-03-26 | Open | 8 |
| A-118 | Marcus / Gabrielle | Design and implement finance dashboard for finance users: track finance sheet requests, in-app notifications + email notifications for pending approvals; GL mapping, PO flow, and summary view approach confirmed in June 19 session | 2026-04-23 | In Progress | 6 |
| A-127 | Christine / Clemene | Provide IDFusion with complete list and definitions of all legal terms used by agency (SSG, agreements with minors, temporary/permanent orders, customary acceptance, etc.) | 2026-05-07 | Open | 5 |
| A-128 | Marcus / Clemene | Cross-reference agency law/regulations with system terminology to ensure consistency; Manitoba CFS Act vs Peguis legislation discussed Apr 28 | 2026-05-07 | In Progress | 5 |
| A-129 | IDFusion / Kelvin | Set up alpha testing access for Kelvin, Christine, and Darryl; client+family data UAT walkthrough completed (A-175); intake module UAT walkthrough completed June 16; formal sign-off procedure still pending | 2026-05-07 | In Progress | 5 |
| A-130 | Marcus | Translate project timeline into Outlook calendar invites for key testing/review milestones | 2026-04-28 | Open | 5 |
| A-131 | IDFusion dev | Implement Apr 13 demo feedback items: fix Peguis footer typo; gender to Male/Female/Two-Spirit/Non-binary; add Child profile type option; auto age-18 profile upgrade; ID lookup table; abuse investigation tab with RBAC; address history with start/end dates + ordinary residence flag; reserve/non-reserve auto-populate; CEFAS copy report; finance processing buttons | 2026-04-30 | Open | 5 |
| A-135 | IDFusion / Rob / Ross | Define post-go-live support tiers (bronze/silver/gold) and SLAs (e.g., 1-hour response for finance emergencies) | 2026-05-28 | Open | 5 |
| A-136 | Bev / Christine / Barry / Clemene | Send all finance templates and forms (headers only, no PII); Bev's GL code / chart of accounts reviewed June 19; RBC CSV headers still needed (see A-158) | 2026-04-28 | In Progress | 5 |
| A-150 | Marcus / Gabrielle | Update finance PO workflow wireframes: button on intake/case → itemized form → auto GL mapping (determined by address and intake type) → Sage export; design approach confirmed June 19 | 2026-05-21 | In Progress | 4 |
| A-151 | Marcus / Gabrielle | Update abuse module wireframes: redesign as intake-form wizard per May 11 reset decision; specific items include correct conclusion terminology, 'notice to provide information' step, 3 form routing options, 'Other' free-text for evidence categories, timer logic for business hours/holidays (see A-170) | 2026-05-21 | In Progress | 4 |
| A-152 | Ross / IDFusion | Implement global holiday calendar in Wabanong system settings to support business-hour timer calculations for finance and abuse workflows | 2026-05-21 | Open | 4 |
| A-153 | Kelvin (PCFS) | Send finalized abuse investigation conclusion terminology (Valid Incident / Abuse Did Not Occur / Inconclusive + any others) to Ross/Marcus for implementation | 2026-05-21 | Open | 4 |
| A-154 | Kelvin (PCFS) | Provide blank/redacted provincial abuse investigation form fields to IDFusion for copy-assist screen field mapping | 2026-05-21 | Open | 4 |
| A-155 | Marcus | Follow up with intake team re: adding missing Manitoba CFS Act abuse issue categories to Wabanong intake form; Darryl to provide full list (see A-161) | 2026-05-21 | In Progress | 4 |
| A-156 | Marcus | Clarify with ongoing services/intake team how "parenting time" is determined for case anchoring when both parents are Peguis members | 2026-05-21 | Open | 4 |
| A-157 | Marcus / Gabrielle | Update ongoing services wireframes: add in-home/out-of-home toggle per person on case; rename "New Admission Checklist" to "Mandatory Child Services Checklist"; add director reference to case assignment view; IRAP rate sheet trigger (placement change → worker task → CRD approval); confirm face sheet as manual Finance tab button | 2026-05-21 | In Progress | 4 |
| A-158 | Bev / Barry (PCFS) | Send RBC bank export file column headers (CSV format) to IDFusion for building the Wabanong credit card import template | 2026-05-21 | Open | 4 |
| A-159 | Marcus | Schedule follow-up ongoing services wireframe review meeting with CRD team after wireframe revisions completed | 2026-05-21 | Open | 4 |
| A-160 | Ross (IDFusion) | Document "Finance Assigner" role in Wabanong role architecture: define queue visibility and task assignment capabilities | 2026-05-21 | Open | 4 |
| A-161 | Darryl Boulanger (PCFS) | Provide complete issue categories and subcategories list from provincial IM form (with timeframes per category) to IDFusion for intake form update | 2026-05-21 | Open | 3 |
| A-170 | Marcus / Gabrielle | Redesign abuse module as intake-form wizard (step-based entry matching current paper form workflow); produce initial wireframes for next Kelvin review session | 2026-06-04 | In Progress | 3 |
| A-171 | Marcus (Rob) | Send updated PCFS status report: revised go-live end of July 2026, abuse as separate iteration, updated meeting cadence | 2026-05-21 | Open | 3 |
| A-176 | Marcus | Clarify with finance team which budget pool covers intake-related purchases (operations vs. prevention/family service budget) | 2026-05-21 | Open | 3 |
| A-177 | Gabrielle | Implement dual supervisor task assignment in intake task modal: default to general pool with option for specific supervisor assignment | 2026-07-02 | Open | 2 |
| A-178 | Gabrielle | Add optional case synopsis/summary field at end of intake form; carry over to case file (visible if populated, hidden if empty) | 2026-07-02 | Open | 2 |
| A-179 | Gabrielle | Submit development ticket for issue categories expansion to full CFIS list (all subcategories); confirmed must-have before go-live | 2026-07-02 | Open | 2 |
| A-180 | Ross / Darryl | Schedule follow-up intake practice run sessions for PCFS team; use real-world scenarios with anonymized data; coordinate with Marcus/Gabrielle for follow-up review meetings | 2026-07-02 | Open | 2 |
| A-181 | Ross / Gabrielle / Marcus | Define and implement intake supervisor finance permissions: read + ability to change family budgets; include after-hours access; review scope with Darryl in upcoming finance module session | 2026-07-02 | Open | 2 |
| A-182 | Marcus | Activate UAT accounts for newly added team members following June 16 meeting | 2026-06-18 | Open | 2 |
| A-183 | Marcus | Send UAT session summary to all June 16 participants: role assignments chart + feedback submission instructions (devteam@idfusion.com + cc Ross/Kelvin/Christina) | 2026-06-18 | Open | 2 |
| A-184 | Gabrielle | Create/confirm bug ticket for "open services" not showing in person search results when initiating a new intake | 2026-06-18 | Open | 2 |
| A-187 | Rob | Review all shared finance documentation (GL codes, funding streams, PO forms, process maps); compile requirements summary for finance module data entry screens | 2026-07-02 | Open | 1 |
| A-188 | Marcus / Gabrielle | Schedule follow-up finance design session with Rob after documentation review | 2026-07-02 | Open | 1 |
| A-185 | Marcus | Identify past finance team meeting dates and share locations in meeting notes folder with Rob | 2026-06-25 | Complete | 1 |
| A-186 | Marcus | Share Egnyte folder links for finance forms/face sheets and policy manual with Rob | 2026-06-25 | Complete | 1 |

---
## Issues and Risks

| ID | Description | Severity | Owner | Due Date | Status | Periods Open |
|----|-------------|---------|-------|----------|--------|-------------|
| I-018 | Finance/Sage integration requirements incomplete — June 19 session advanced funding stream mapping, GL code structure, and PO workflow design; formal data entry screen design and Sage integration still pending | Medium | Hailey / Marcus | 2026-01-29 | Open | 13 |
| I-029 | Timeline slippage — go-live revised to end of July 2026 at May 11 reset meeting; M-03 estimated end updated to 2026-07-25; formal contract re-baselining still pending | High | Marcus | 2026-02-12 | Open | 11 |
| I-032 | Development timeline at risk — intake module UAT underway; finance module in early design; case file and abuse iterations still ahead | High | Marcus | 2026-03-12 | Open | 9 |
| I-033 | Address-based search confirmed as new development requirement — moved to roadmap (A-106, A-107 resolved); iteration sequencing impact to be assessed at roadmap review | Medium | Marcus | 2026-03-26 | Open | 8 |
| I-034 | Client-side continuity risk — Haley absent 3+ months; Clemene covering; abuse program clerk Alice approaching retirement (noted by Kelvin Apr 28) | Medium | Marcus / Ross | 2026-04-07 | Open | 7 |
| I-035 | Abuse program — May 11 decision carved out as separate wizard-style iteration; approach clarified; initial wireframes in progress (A-170); specific form details (A-153, A-154) still pending | Medium | Marcus / Kelvin / Clemene | 2026-04-30 | Open | 5 |
| I-036 | UAT pipeline fully operational — Freshdesk → ClickUp triage active; client+family data module UAT complete; intake module UAT walkthrough completed June 16 with full PCFS team | Low | Gabrielle | 2026-04-30 | Open | 5 |
| I-037 | Demo environment crash at Apr 28 finance meeting — UAT environment now set up in PCFS Azure; risk substantially reduced | Medium | Ross / IDFusion | 2026-05-21 | Open | 4 |
| I-038 | Wabanong intake form incomplete — full CFIS issue categories expansion confirmed as mandatory pre-go-live requirement at June 16 UAT session; development ticket submitted (A-179); Darryl's source list still pending (A-161) | Medium | Marcus | 2026-05-21 | Open | 4 |
| I-039 | Holiday calendar missing — Wabanong timer logic does not yet account for observed holidays; required for accurate SLA tracking in finance and abuse workflows | Medium | Ross / IDFusion | 2026-05-21 | Open | 4 |
| I-041 | UAT bug: "open services" not showing in person search results — when initiating a new intake, existing open case files should be surfaced in search; currently not working as expected; Gabrielle created ticket during June 16 session | Low | Gabrielle | 2026-06-18 | Open | 2 |

---
## Active Return to Green Plans

### Overall - Red (first flagged: 2025-W48)
- Complete intake UAT cycle (A-180); triage all feedback through Freshdesk → ClickUp pipeline
- Advance finance module from design (A-187, A-188) to wireframes (A-150) and begin UAT planning
- Schedule case file and abuse module UAT sessions to close remaining iteration gaps before July 31

### Schedule - Red (first flagged: 2025-W48)
- M-03 estimated end updated to 2026-07-25 to reflect actual project state; communicate revised milestone picture to PCFS (A-171)
- Formally re-baseline contract timeline with Clemene/Rob — July 31 go-live target needs a signed-off schedule
- Identify critical path: intake UAT → case file UAT → finance UAT → abuse UAT → go-live; confirm each module's UAT readiness date

### Scope - Yellow (first flagged: 2025-W50)
- Finance scope now partially locked (kinship out; PO flow + GL auto-mapping in); complete scope definition after Rob's documentation review (A-187)
- Remaining open scope items (family budget planning amounts, agreement types) require direct finance team input — schedule a client-side finance team session
- Ensure all June 16 UAT feedback items (A-177–A-179, A-184) are confirmed in-scope before development begins

### Budget - Yellow (first flagged: 2025-W50)
- Finance module design underway; scope partially defined but agreement-type budget data still unclear — confirm scope limits with Rob and Clemene before full design begins
- Abuse contract amendment still outstanding (A-171); include in next PCFS status report
- No new cost concerns this period

### Client's Feeling - Yellow (first flagged: 2026-W13)
- No client signal this period (internal meeting only); maintain momentum from positive June 16 UAT session
- Send PCFS status report (A-171) promptly to keep Clemene informed of progress and July target
- Deliver intake UAT feedback items quickly to reinforce client confidence before next external session

---
## Period History (rolling 4-week window)

### 2026-W23 (2026-05-22 → 2026-06-04)
- **Health:** N/A — no meetings this period
- **Report:** none
- **Summary:** Empty period — no meetings held or transcripts available. Null rollover to advance period counter.

### 2026-W25 (2026-06-05 → 2026-06-18)
- **Health:** Overall/Schedule Red; Scope/Budget/Client's Feeling Yellow
- **Report:** `status-reports/2026-W25.qmd`
- **Summary:** The intake module UAT walkthrough was completed June 16 with strong PCFS stakeholder engagement — new testers were onboarded, nine workflow decisions were confirmed (including supervisor task assignment pools and a case synopsis field), and a search bug was identified and immediately ticketed. Twenty-five existing action items were closed this period, with eight new items added to track UAT feedback implementation and finance access requirements surfaced by Darryl.

### 2026-W27 (2026-06-19 → 2026-07-02)
- **Health:** Overall/Schedule Red; Scope/Budget/Client's Feeling Yellow
- **Report:** `status-reports/2026-W27.qmd`
- **Summary:** An internal finance module requirements session (June 19) established the design approach for the Wabanong PO workflow and Finance tab — funding stream GL mapping was clarified, auto-categorization from intake fields was confirmed, and kinship payment tracking was scoped out. M-03 (all iterations complete) estimated end was updated from June 30 to July 25, reflecting the pace of UAT and remaining module design work.
