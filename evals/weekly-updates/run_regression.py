#!/usr/bin/env python3
"""
run_regression.py — Regression test for the weekly update conversion pipeline.

Converts a known draft using scripts/convert.py, then runs scripts/qa_check.py
against the output and compares it structurally to the approved May 2026 fixture.

The fixture (outputs/peguis-cfs/Waabanong Weekly Update - Week of 2026-05-18.docx)
is the accepted client deliverable from May 25, 2026 — the canonical reference for
correct document structure (grey table headers, Section/list1 styles, I5 A + I5 B).

Usage:
    python evals/weekly-updates/run_regression.py

Exit code: 0 = all checks pass, 1 = failure
"""

import sys
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent.parent
FIXTURE = REPO_ROOT / "outputs" / "peguis-cfs" / "Waabanong Weekly Update - Week of 2026-05-18.docx"
TEST_DRAFT_WEEK = "2026-06-22"
# The extracted image from the fixture, used as a placeholder during regression testing.
# In production, a real updated roadmap PNG is always supplied.
TEST_IMAGE = REPO_ROOT / "outputs" / "peguis-cfs" / "extracted_image_0.png"
OUTPUT_PATH = REPO_ROOT / "outputs" / "weekly-updates" / f"Waabanong Weekly Update - Week of {TEST_DRAFT_WEEK}.docx"


def run(cmd: list, label: str) -> bool:
    """Run a subprocess command, print output, return True if it succeeded."""
    print(f"\n--- {label} ---")
    result = subprocess.run(
        [sys.executable] + cmd,
        capture_output=False,
        cwd=str(REPO_ROOT)
    )
    return result.returncode == 0


def main():
    print("=== Weekly Update Regression Test ===")
    print(f"Draft:   {TEST_DRAFT_WEEK}-draft.md")
    print(f"Fixture: {FIXTURE.name}")

    if not FIXTURE.exists():
        print(f"\nERROR: Fixture not found: {FIXTURE}")
        print("  Ensure outputs/peguis-cfs/ contains the May 2026 accepted deliverable.")
        sys.exit(1)

    if not TEST_IMAGE.exists():
        print(f"\nERROR: Test image not found: {TEST_IMAGE}")
        print("  Run: python -c \"import docx; ...\" to extract it (see scripts/convert.py header)")
        sys.exit(1)

    draft_path = REPO_ROOT / "outputs" / "weekly-updates" / f"{TEST_DRAFT_WEEK}-draft.md"
    if not draft_path.exists():
        print(f"\nERROR: Draft not found: {draft_path}")
        sys.exit(1)

    # Step 1: Convert
    convert_ok = run(
        ["scripts/convert.py", TEST_DRAFT_WEEK, "--image", str(TEST_IMAGE)],
        "Step 1: Convert draft to .docx"
    )

    if not convert_ok:
        print("\n[FAIL] Conversion failed.")
        sys.exit(1)

    # Step 2: QA check with fixture comparison
    qa_ok = run(
        ["scripts/qa_check.py", str(OUTPUT_PATH), "--fixture", str(FIXTURE)],
        "Step 2: Structural QA + fixture comparison"
    )

    print("\n" + "=" * 50)
    if qa_ok:
        print("[PASS] Regression test passed.")
    else:
        print("[FAIL] Regression test failed -- check QA output above.")

    sys.exit(0 if qa_ok else 1)


if __name__ == "__main__":
    main()
