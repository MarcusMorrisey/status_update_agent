"""
Writes meeting-notes-current.md for W25 (2026-06-05 → 2026-06-18).
June 9 meeting has no transcript (mp4 only — noted inline).
June 17 UAT walkthrough already extracted to _tmp_ingest/m617_uat.txt.
Run from agent root — writes output to project directory.
"""
import pathlib

TMP = pathlib.Path(r'C:/ClaudeProjects/status_update_agent/_tmp_ingest')
OUT = pathlib.Path(r'C:/ClaudeProjects/status_update_agent/project/meeting-notes-current.md')

def read_txt(path):
    try:
        return pathlib.Path(path).read_text(encoding='utf-8', errors='replace').strip()
    except Exception as e:
        return f"[Error reading {path}: {e}]"

m617 = read_txt(TMP / 'm617_uat.txt')

HEADER = """\
# Meeting Notes — Custom-CMS (Wabanong)
**Period:** 2026-W25 (2026-06-05 → 2026-06-18)
**Generated:** 2026-06-25
**Meetings:** 0 internal, 1 external (1 additional meeting has no transcript)

---
"""

NO_TRANSCRIPT = """\
## External Meeting — 2026-06-09
**File:** Z:\\Shared\\3_Client Projects\\Peguis CFS\\Projects\\PD25-1186-CO - Custom CMS\\4. Controlling\\01. Meeting Minutes\\2026-06-09\\2026-06-09_10-30-18.mp4
**Note:** No transcript available — folder contains only a video recording (.mp4). Meeting content not ingested.

---

"""

M617_SECTION = f"""\
## External Meeting — 2026-06-17
**File:** Z:\\Shared\\3_Client Projects\\Peguis CFS\\Projects\\PD25-1186-CO - Custom CMS\\4. Controlling\\01. Meeting Minutes\\2026-06-17\\User Acceptance Testing_ Intake Module Walkthrough.docx
**Extracted to:** _tmp_ingest/m617_uat.txt

{m617}

---
"""

full = HEADER + NO_TRANSCRIPT + M617_SECTION
OUT.write_text(full, encoding='utf-8')
print(f'Written {OUT.stat().st_size:,} bytes to {OUT}')
print('  2026-06-09: External [NO TRANSCRIPT — mp4 only]')
print('  2026-06-17: External — UAT Intake Module Walkthrough')
