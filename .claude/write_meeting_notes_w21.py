"""
Writes meeting-notes-current.md for W21 (2026-05-08 → 2026-05-21).
Includes late-W19 meetings (May 5 × 2 sessions, May 6) with caveat note.
Run from agent root — writes output to project directory.
"""
import pathlib

TMP   = pathlib.Path(r'C:/ClaudeProjects/status_update_agent/_tmp_ingest')
SRC06 = pathlib.Path(r'Z:/Shared/3_Client Projects/Peguis CFS/Projects/PD25-1186-CO - Custom CMS/4. Controlling/01. Meeting Minutes/2026-05-06/Case File Wireframe Review -Session 2.txt')
OUT   = pathlib.Path(r'C:/ClaudeProjects/status_update_agent/project/meeting-notes-current.md')

def read_txt(path):
    try:
        return pathlib.Path(path).read_text(encoding='utf-8', errors='replace').strip()
    except Exception as e:
        return f"[Error reading {path}: {e}]"

# Read m505_intake.txt — contains two sessions concatenated
m505_full = read_txt(TMP / 'm505_intake.txt')

# Split on the second session header
SPLIT_MARKER = 'Tuesday at 10_36_07 am'
split_idx = m505_full.find(SPLIT_MARKER)
if split_idx != -1:
    m505_s1 = m505_full[:split_idx].strip()
    m505_s2 = m505_full[split_idx:].strip()
else:
    m505_s1 = m505_full
    m505_s2 = '[Session 2 marker not found — full file in Session 1 above]'

m506 = read_txt(SRC06)
m511 = read_txt(TMP / 'm511_reset.txt')
m513 = read_txt(TMP / 'm513_feedback.txt')

HEADER = """\
# Meeting Notes — Custom-CMS (Wabanong)
**Period:** 2026-W21 (2026-05-08 → 2026-05-21)
**Generated:** 2026-06-25
**Meetings:** 1 internal, 4 external
**Note:** Meetings dated 2026-05-05 and 2026-05-06 fall within the prior period
(2026-W19, 2026-04-24 → 2026-05-07) but were not ingested in that cycle.
They are included here with this caveat so no meeting content is lost.

---
"""

sections = [
    ('External Meeting', '2026-05-05', 'Session 1 — Intake Wireframe Review (09:18)',
     'Z:\\Shared\\...\\2026-05-05 (Otter AI transcript — extracted to _tmp_ingest/m505_intake.txt)',
     m505_s1, '⚠ Late W19 — meeting date falls in prior period (2026-W19)'),

    ('External Meeting', '2026-05-05', 'Session 2 — Intake Wireframe Review (10:36)',
     'Z:\\Shared\\...\\2026-05-05 (Otter AI transcript — extracted to _tmp_ingest/m505_intake.txt)',
     m505_s2, '⚠ Late W19 — meeting date falls in prior period (2026-W19)'),

    ('External Meeting', '2026-05-06', 'Case File Wireframe Review — Session 2',
     r'Z:\Shared\3_Client Projects\Peguis CFS\Projects\PD25-1186-CO - Custom CMS\4. Controlling\01. Meeting Minutes\2026-05-06\Case File Wireframe Review -Session 2.txt',
     m506, '⚠ Late W19 — meeting date falls in prior period (2026-W19)'),

    ('External Meeting', '2026-05-11', 'PCFS Reset Meeting',
     r'Z:\Shared\...\ (extracted to _tmp_ingest/m511_reset.txt)',
     m511, None),

    ('Internal Meeting', '2026-05-13', 'Feedback on Specs and UAT Process',
     r'Z:\Shared\...\ (extracted to _tmp_ingest/m513_feedback.txt)',
     m513, None),
]

GITHUB_SUPPLEMENT = """\
## Supplementary — GitHub Development Activity (2026-05-08 → 2026-05-21)
**Source:** https://github.com/ID-Fusion/PCFS (GitHub API)
**Note:** Activity reviewed as of 2026-06-25. W21-specific PR/commit counts are a
subset of the full period totals (22 PRs merged 2026-05-07 → 2026-06-25; 664+
commits total across vmehra, awaisamir123, omerfayyaz). The development team was
actively merging pull requests throughout this period. Specific W21 PR titles and
dates were reviewed during ingest — full detail available via GitHub PR API.

Key observations for W21 timeframe (2026-05-08 → 2026-05-21):
- Active development sprint corresponding to case management and intake modules
- Three active contributors: Varun Mehra (vmehra), Awais Amir (awaisamir123),
  Omer Fayyaz (omerfayyaz)
- Azure deployment pipeline (Campfire / Azure DevOps) in active use
- Development aligned with UAT preparation activities discussed in May 11 and
  May 13 meetings

---
"""

parts = [HEADER]
for meeting_type, date, title, filepath, content, caveat in sections:
    parts.append(f'## {meeting_type} — {date}\n')
    parts.append(f'**Title:** {title}\n')
    parts.append(f'**File:** {filepath}\n')
    if caveat:
        parts.append(f'**{caveat}**\n')
    parts.append('\n')
    parts.append(content)
    parts.append('\n\n---\n\n')

parts.append(GITHUB_SUPPLEMENT)

full = ''.join(parts)
OUT.write_text(full, encoding='utf-8')
print(f'Written {OUT.stat().st_size:,} bytes ({len(full):,} chars) to {OUT}')
for meeting_type, date, title, _, _, caveat in sections:
    flag = ' [LATE W19]' if caveat else ''
    print(f'  {date}: {title}{flag}')
