#!/usr/bin/env python3
"""Refresh size and SHA-256 fields after an intentional library edit."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "library-manifest.json"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    for record in manifest["files"]:
        library = ROOT / record["path"]
        if not library.is_file():
            raise SystemExit(f"Missing library: {record['path']}")
        record["bytes"] = library.stat().st_size
        record["sha256"] = sha256(library)

    MANIFEST_PATH.write_text(
        json.dumps(manifest, indent=2, sort_keys=False) + "\n",
        encoding="utf-8",
    )
    print("Updated library-manifest.json")


if __name__ == "__main__":
    main()
