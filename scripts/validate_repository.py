#!/usr/bin/env python3
"""Run dependency-free integrity and documentation checks."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
COMPOUND_FILE_SIGNATURE = bytes.fromhex("D0CF11E0A1B11AE1")
REQUIRED_FILES = {
    ".editorconfig",
    ".gitattributes",
    ".github/CODEOWNERS",
    ".github/workflows/quality.yml",
    "AGENTS.md",
    "CHANGELOG.md",
    "CITATION.cff",
    "CLAUDE.md",
    "CODE_OF_CONDUCT.md",
    "CONTRIBUTING.md",
    "LICENSE",
    "NOTICE",
    "README.md",
    "SECURITY.md",
    "SUPPORT.md",
    "docs/INVENTORY.md",
    "docs/USAGE.md",
    "docs/VALIDATION.md",
    "library-manifest.json",
}
FORBIDDEN_PATTERNS = (
    re.compile(r"(^|/)History/"),
    re.compile(r"(^|/)__Previews/"),
    re.compile(r"\.SchDocPreview$"),
    re.compile(r"\.PrjPcbStructure$"),
    re.compile(r"\.~"),
)
INVENTORY_SECTIONS = {
    "schematic-inventory": 81,
    "footprint-inventory": 106,
}
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*]\(([^)]+)\)")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def tracked_files() -> list[str]:
    result = subprocess.run(
        ["git", "ls-files"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.splitlines()


def validate_manifest(errors: list[str]) -> None:
    manifest_path = ROOT / "library-manifest.json"
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"Invalid library-manifest.json: {exc}")
        return

    if manifest.get("schema_version") != 1:
        errors.append("library-manifest.json must use schema_version 1")

    records = manifest.get("files")
    if not isinstance(records, list) or len(records) != 2:
        errors.append("library-manifest.json must declare exactly two libraries")
        return

    for record in records:
        relative = record.get("path", "")
        path = ROOT / relative
        if not path.is_file():
            errors.append(f"Manifest library does not exist: {relative}")
            continue
        with path.open("rb") as stream:
            if stream.read(8) != COMPOUND_FILE_SIGNATURE:
                errors.append(f"{relative} is not an OLE compound document")
        actual_size = path.stat().st_size
        if record.get("bytes") != actual_size:
            errors.append(
                f"{relative} size mismatch: manifest={record.get('bytes')}, "
                f"actual={actual_size}"
            )
        actual_hash = sha256(path)
        if record.get("sha256") != actual_hash:
            errors.append(f"{relative} SHA-256 does not match the manifest")
        if not isinstance(record.get("entries"), int) or record["entries"] <= 0:
            errors.append(f"{relative} must declare a positive entry count")


def validate_inventory(errors: list[str]) -> None:
    inventory = (ROOT / "docs/INVENTORY.md").read_text(encoding="utf-8")
    for marker, expected in INVENTORY_SECTIONS.items():
        pattern = re.compile(
            rf"<!-- {marker}:start -->\n(.*?)<!-- {marker}:end -->",
            re.DOTALL,
        )
        match = pattern.search(inventory)
        if not match:
            errors.append(f"Missing {marker} markers in docs/INVENTORY.md")
            continue
        entries = re.findall(r"^- `.+`$", match.group(1), re.MULTILINE)
        if len(entries) != expected:
            errors.append(
                f"{marker} has {len(entries)} entries; expected {expected}"
            )


def validate_markdown_links(errors: list[str]) -> None:
    for document in ROOT.rglob("*.md"):
        if ".git" in document.parts:
            continue
        text = document.read_text(encoding="utf-8")
        for raw_target in MARKDOWN_LINK.findall(text):
            target = raw_target.strip().strip("<>").split(maxsplit=1)[0]
            if (
                not target
                or target.startswith(("#", "http://", "https://", "mailto:"))
            ):
                continue
            target = unquote(target.split("#", 1)[0].split("?", 1)[0])
            resolved = (document.parent / target).resolve()
            if not resolved.exists():
                errors.append(
                    f"Broken local link in {document.relative_to(ROOT)}: {target}"
                )


def main() -> int:
    errors: list[str] = []

    for relative in sorted(REQUIRED_FILES):
        if not (ROOT / relative).is_file():
            errors.append(f"Missing required file: {relative}")

    tracked = tracked_files()
    for relative in tracked:
        if any(pattern.search(relative) for pattern in FORBIDDEN_PATTERNS):
            errors.append(f"Generated or backup file is tracked: {relative}")

    validate_manifest(errors)
    validate_inventory(errors)
    validate_markdown_links(errors)

    if errors:
        print("Repository validation failed:", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
        return 1

    print("Repository validation passed.")
    print("Verified 81 schematic symbols and 106 PCB footprints.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
