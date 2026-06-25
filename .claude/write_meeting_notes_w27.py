"""
Writes meeting-notes-current.md for W27 (2026-06-19 → 2026-07-02).
One internal meeting: June 19 finance session, extracted to _tmp_ingest/m619_finance.txt.
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

m619 = read_txt(TMP / 'm619_finance.txt')

HEADER = """\
# Meeting Notes — Custom-CMS (Wabanong)
**Period:** 2026-W27 (2026-06-19 → 2026-07-02)
**Generated:** 2026-06-25
**Meetings:** 1 internal, 0 external

---
"""

M619_SECTION = f"""\
## Internal Meeting — 2026-06-19
**File:** Z:\\Shared\\3_Client Projects\\Peguis CFS\\Projects\\PD25-1186-CO - Custom CMS\\4. Controlling\\01. Meeting Minutes\\internal\\2026.06.19 Internal Finance Meeting\\Discuss PCFS Finance Summ and Transcript.docx
**Extracted to:** _tmp_ingest/m619_finance.txt

{m619}

---
"""

full = HEADER + M619_SECTION
OUT.write_text(full, encoding='utf-8')
print(f'Written {OUT.stat().st_size:,} bytes to {OUT}')
print('  2026-06-19: Internal — Finance module discussion (1h 4m)')
