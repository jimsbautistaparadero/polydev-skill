#!/usr/bin/env python3
"""Create a starter research workspace from the bundled templates.

Existing files are preserved by default. With --overwrite, matching paths are
replaced. No user files outside the destination are modified.
"""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Copy the bundled workspace-starter structure to a project directory."
    )
    parser.add_argument("destination", type=Path, help="New or existing research workspace path")
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Replace starter files that already exist (use carefully; user changes may be lost).",
    )
    args = parser.parse_args()

    skill_root = Path(__file__).resolve().parents[1]
    source = skill_root / "templates" / "workspace-starter"
    destination = args.destination.expanduser().resolve()

    if not source.is_dir():
        print(f"ERROR: Starter templates are missing: {source}", file=sys.stderr)
        return 2

    destination.mkdir(parents=True, exist_ok=True)
    copied = 0
    preserved = 0

    for source_file in sorted(source.rglob("*")):
        if not source_file.is_file():
            continue
        relative = source_file.relative_to(source)
        target_file = destination / relative
        target_file.parent.mkdir(parents=True, exist_ok=True)
        if target_file.exists() and not args.overwrite:
            preserved += 1
            continue
        shutil.copy2(source_file, target_file)
        copied += 1

    print(f"Workspace: {destination}")
    print(f"Starter files copied/replaced: {copied}")
    print(f"Existing files preserved: {preserved}")
    print("Next: complete the study brief, then run validate_research_workspace.py on this directory.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
