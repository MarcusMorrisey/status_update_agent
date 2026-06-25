"""
Writes meeting-notes-current.md for W19 (2026-04-24 → 2026-05-07).
Run from agent root — writes output to project directory.
"""
import zipfile, re, pathlib

def extract_docx(path):
    try:
        with zipfile.ZipFile(str(path)) as z:
            xml = z.open('word/document.xml').read().decode('utf-8', errors='replace')
        # Convert paragraph and line-break tags to newlines before stripping
        xml = re.sub(r'<w:p[ >]', '\n<w:p>', xml)
        xml = re.sub(r'</w:p>', '\n', xml)
        xml = re.sub(r'<w:br[^/]*/>', '\n', xml)
        text = re.sub(r'<[^>]+>', '', xml)
        text = re.sub(r'\n{3,}', '\n\n', text)
        return text.strip()
    except Exception as e:
        return f"[Error extracting {path}: {e}]"

def read_txt(path):
    try:
        return pathlib.Path(path).read_text(encoding='utf-8', errors='replace').strip()
    except Exception as e:
        return f"[Error reading {path}: {e}]"

BASE = pathlib.Path(r'C:/ClaudeProjects/status_update_agent/project/01. Meeting Minutes')
OUT  = pathlib.Path(r'C:/ClaudeProjects/status_update_agent/project/meeting-notes-current.md')

meetings = [
    ('2026-04-24', BASE / '2026-04-24' / '2026-04-24_Finance Review Transcript.docx',         'docx'),
    ('2026-04-28', BASE / '2026-04-28' / '2026-04-28_Finance transcript.txt',                  'txt'),
    ('2026-04-28', BASE / '2026-04-28' / '2026-04-28_abuse_investigations_transcript.txt',     'txt'),
    ('2026-04-28', BASE / '2026-04-28' / '2026-04-28_abuse investigations part 2_transcript.txt', 'txt'),
    ('2026-04-29', BASE / '2026-04-29' / '2026-04-29_ongoing services part 1_trasncript.docx', 'docx'),
    ('2026-04-29', BASE / '2026-04-29' / '2026-04-29_ongoing services part 2_transcript.docx', 'docx'),
]

HEADER = """\
# Meeting Notes — Custom-CMS
**Period:** 2026-W19 (2026-04-24 → 2026-05-07)
**Generated:** 2026-05-25
**Meetings:** 0 internal, 6 external

---
"""

parts = [HEADER]
for date, path, ftype in meetings:
    rel = path.relative_to(BASE.parent)
    parts.append(f'## External Meeting — {date}\n**File:** {rel}\n\n')
    if ftype == 'docx':
        content = extract_docx(path)
    else:
        content = read_txt(path)
    parts.append(content)
    parts.append('\n\n---\n\n')

full = ''.join(parts)
OUT.write_text(full, encoding='utf-8')
print(f'Written {OUT.stat().st_size:,} bytes ({len(full):,} chars) to {OUT}')
for date, path, _ in meetings:
    print(f'  {date}: {path.name}')
