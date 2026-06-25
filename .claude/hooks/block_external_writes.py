#!/usr/bin/env python3
"""PreToolUse hook: block writes outside the repo root.

Reads the hook event JSON from stdin and emits a permission decision on stdout.
Allows reads anywhere; blocks Write/Edit/MultiEdit and Bash write operations
(cp/mv/mkdir/rm/tee/redirects, plus PowerShell write cmdlets) when any target
path resolves outside the repo or the allowed temp directories.

To bypass once: the user must explicitly grant the operation.
To bypass permanently for a path: add it to ALLOWED_PREFIXES below.
"""

import json
import os
import re
import sys

# Allowed absolute path prefixes (all normalized: lowercase, forward slashes).
# Add explicit allow-throughs here when you need persistent exceptions.
REPO_ROOT_RAW = r"C:\ClaudeProjects\status_update_agent"

# Permanent extra allowed paths (outside the repo).
EXTRA_ALLOWED_RAW = []


def normalize(path: str) -> str:
    """Normalize a path string to a canonical lowercase forward-slash form."""
    if not path:
        return ""
    p = path.replace("\\", "/").strip()
    while p.startswith("//"):
        p = p[1:]
    m = re.match(r"^([A-Za-z]):/?(.*)$", p)
    if m:
        drive = m.group(1).lower()
        rest = m.group(2)
        p = f"/{drive}/{rest}" if rest else f"/{drive}"
    p = p.rstrip("/")
    return p.lower()


REPO_ROOT = normalize(REPO_ROOT_RAW)

_temp_candidates = [
    os.environ.get("TEMP"),
    os.environ.get("TMP"),
    os.environ.get("TMPDIR"),
    "/tmp",
    "/var/tmp",
    r"C:\Users\marcu\AppData\Local\Temp",
]
ALLOWED_PREFIXES = {REPO_ROOT}
for t in _temp_candidates:
    if t:
        ALLOWED_PREFIXES.add(normalize(t))
for p in EXTRA_ALLOWED_RAW:
    ALLOWED_PREFIXES.add(normalize(p))


def is_allowed_path(path: str) -> bool:
    n = normalize(path)
    if not n:
        return True
    for prefix in ALLOWED_PREFIXES:
        if n == prefix or n.startswith(prefix + "/"):
            return True
    return False


WRITE_VERBS = {
    "cp", "mv", "rm", "mkdir", "rmdir", "tee", "touch", "chmod", "chown",
    "ln", "install", "dd", "rsync",
    "copy-item", "move-item", "remove-item", "new-item", "set-content",
    "out-file", "add-content", "set-itemproperty", "write-file",
    "copy", "move", "del", "ren", "md", "rd", "erase",
}

ABS_PATH_PATTERN = re.compile(
    r"""
    (?:
        [A-Za-z]:[/\\][^\s'";|&]+   |
        //[A-Za-z]/[^\s'";|&]+      |
        /[A-Za-z]/[^\s'";|&]+       |
        /(?:tmp|var|home|root|opt|etc|usr|srv|mnt)/[^\s'";|&]*
    )
    """,
    re.VERBOSE,
)

REDIRECT_PATTERN = re.compile(r"(?:^|[^>])(\d*&?>{1,2})\s*([^\s|;&]+)")


def bash_has_write_op(cmd: str) -> bool:
    if REDIRECT_PATTERN.search(cmd):
        return True
    tokens = re.split(r"[\s|;&()`]+", cmd)
    for tok in tokens:
        if not tok:
            continue
        bare = tok.lstrip("\"'$").lower()
        bare = bare.rsplit("/", 1)[-1].rsplit("\\", 1)[-1]
        if bare in WRITE_VERBS:
            return True
    return False


def disallowed_paths_in_bash(cmd: str) -> list[str]:
    bad = []
    for m in ABS_PATH_PATTERN.finditer(cmd):
        candidate = m.group(0).strip().strip("\"'")
        if not is_allowed_path(candidate):
            bad.append(candidate)
    return bad


def decide(event: dict) -> dict | None:
    tool = event.get("tool_name", "")
    tin = event.get("tool_input", {}) or {}

    if tool in ("Write", "Edit", "MultiEdit", "NotebookEdit"):
        path = tin.get("file_path") or tin.get("notebook_path") or ""
        if not is_allowed_path(path):
            return deny_response(path, tool)
        return None

    if tool == "Bash":
        cmd = tin.get("command", "") or ""
        if not bash_has_write_op(cmd):
            return None
        bad = disallowed_paths_in_bash(cmd)
        if bad:
            return deny_response(", ".join(bad), tool, snippet=cmd[:160])
        return None

    return None


def deny_response(path: str, tool: str, snippet: str = "") -> dict:
    extra = f"  Command: {snippet}" if snippet else ""
    reason = (
        f"Blocked: {tool} would write outside the repo.\n"
        f"  Target: {path}\n"
        f"{extra}\n"
        f"  Repo root: {REPO_ROOT_RAW}\n\n"
        f"Project rule: writes are confined to the repo. "
        f"Either redirect the operation inside the repo, or ask the user "
        f"for explicit permission before proceeding."
    )
    return {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": reason,
        }
    }


def main() -> int:
    try:
        event = json.load(sys.stdin)
    except Exception as e:
        print(json.dumps({"systemMessage": f"block_external_writes hook: bad input ({e})"}))
        return 0
    result = decide(event)
    if result is not None:
        print(json.dumps(result))
    return 0


if __name__ == "__main__":
    sys.exit(main())
