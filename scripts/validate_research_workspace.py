#!/usr/bin/env python3
"""Audit the structure and basic metadata of a research workspace.

This script does not assess scholarly quality, validate citations against the
internet, approve research ethics, or certify that data are genuine.
It uses only Python's standard library.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path
from typing import Iterable

REQUIRED_FILES = (
    "00-study-brief.md",
    "01-master-plan.md",
    "02-problem-and-questions.md",
    "03-literature-review/search-strategy.md",
    "03-literature-review/source-log.csv",
    "03-literature-review/evidence-matrix.csv",
    "03-literature-review/synthesis.md",
    "04-framework-and-methods/framework.md",
    "04-framework-and-methods/methodology.md",
    "04-framework-and-methods/instruments.md",
    "04-framework-and-methods/analysis-plan.md",
    "05-ethics-and-governance.md",
    "decisions.md",
    "risks.csv",
    "progress.md",
)

CSV_REQUIRED_FIELDS = {
    "source-log.csv": {"source_id", "title", "authors", "year", "doi", "url", "access_status"},
    "evidence-matrix.csv": {"source_id", "full_citation", "study_purpose", "study_design", "key_findings", "relevance_to_current_study"},
    "risks.csv": {"risk_id", "risk_description", "likelihood_1_to_5", "impact_1_to_5", "prevention_or_mitigation"},
}

PLACEHOLDER_PATTERNS = (
    re.compile(r"\[[^\]]{2,}\]"),
    re.compile(r"\b(TODO|TBD|TO BE CONFIRMED|INSERT HERE)\b", re.IGNORECASE),
)


def read_csv_header(path: Path) -> list[str]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.reader(handle)
        try:
            return next(reader)
        except StopIteration:
            return []


def inspect_workspace(root: Path) -> tuple[list[str], list[str], dict[str, int]]:
    errors: list[str] = []
    warnings: list[str] = []
    metrics: dict[str, int] = {"required_files": len(REQUIRED_FILES), "missing_files": 0, "placeholder_matches": 0}

    if not root.exists():
        return [f"Workspace does not exist: {root}"], warnings, metrics
    if not root.is_dir():
        return [f"Workspace path is not a directory: {root}"], warnings, metrics

    for relative in REQUIRED_FILES:
        path = root / relative
        if not path.is_file():
            errors.append(f"Missing required file: {relative}")
            metrics["missing_files"] += 1

    for relative, expected_fields in CSV_REQUIRED_FIELDS.items():
        candidates = [root / "03-literature-review" / relative, root / relative]
        path = next((candidate for candidate in candidates if candidate.is_file()), None)
        if path is None:
            continue
        try:
            header = set(read_csv_header(path))
        except (OSError, UnicodeError, csv.Error) as exc:
            errors.append(f"Cannot read CSV header in {path.relative_to(root)}: {exc}")
            continue
        missing_fields = sorted(expected_fields - header)
        if missing_fields:
            errors.append(
                f"{path.relative_to(root)} is missing expected columns: {', '.join(missing_fields)}"
            )

    markdown_files = list(root.rglob("*.md"))
    for path in markdown_files:
        try:
            content = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            warnings.append(f"Could not inspect {path.relative_to(root)}: {exc}")
            continue
        for pattern in PLACEHOLDER_PATTERNS:
            count = len(pattern.findall(content))
            metrics["placeholder_matches"] += count
    if metrics["placeholder_matches"]:
        warnings.append(
            f"Found {metrics['placeholder_matches']} possible template placeholders. Review them; not all bracketed text is incomplete."
        )

    # Check source IDs and duplicate DOI values without claiming that sources are real.
    source_candidates = [root / "03-literature-review" / "source-log.csv", root / "source-log.csv"]
    source_path = next((candidate for candidate in source_candidates if candidate.is_file()), None)
    if source_path:
        try:
            with source_path.open("r", encoding="utf-8-sig", newline="") as handle:
                reader = csv.DictReader(handle)
                seen_ids: set[str] = set()
                seen_dois: dict[str, int] = {}
                for line_number, row in enumerate(reader, start=2):
                    source_id = (row.get("source_id") or "").strip()
                    doi = (row.get("doi") or "").strip().lower()
                    if source_id and source_id in seen_ids:
                        errors.append(f"Duplicate source_id '{source_id}' at {source_path.relative_to(root)}:{line_number}")
                    elif source_id:
                        seen_ids.add(source_id)
                    if doi:
                        if doi in seen_dois:
                            warnings.append(
                                f"Repeated DOI '{doi}' in source log rows {seen_dois[doi]} and {line_number}; check for duplicate records."
                            )
                        else:
                            seen_dois[doi] = line_number
        except (OSError, UnicodeError, csv.Error) as exc:
            errors.append(f"Could not inspect source log: {exc}")

    return errors, warnings, metrics


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Check research workspace structure, CSV metadata columns, and common placeholders."
    )
    parser.add_argument("workspace", type=Path, help="Path to the research/ workspace directory")
    parser.add_argument("--strict", action="store_true", help="Return non-zero when warnings are present")
    args = parser.parse_args(argv)

    errors, warnings, metrics = inspect_workspace(args.workspace.resolve())
    print(f"Workspace: {args.workspace.resolve()}")
    print(
        "Files: {}/{} required present; possible placeholders: {}".format(
            metrics["required_files"] - metrics["missing_files"],
            metrics["required_files"],
            metrics["placeholder_matches"],
        )
    )

    if errors:
        print("\nERRORS:")
        for item in errors:
            print(f"- {item}")
    if warnings:
        print("\nWARNINGS:")
        for item in warnings:
            print(f"- {item}")
    if not errors and not warnings:
        print("\nStructural checks passed. This is not certification of research quality or source accuracy.")

    if errors or (args.strict and warnings):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
