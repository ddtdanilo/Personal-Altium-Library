# AGENTS.md

## Purpose

This repository contains binary Altium Designer library sources plus supporting
documentation and validation tooling. Changes must preserve library integrity
and make component provenance and verification easy to audit.

## Repository map

- `AltiumLibraryDDT.SchLib`: authoritative schematic-symbol library.
- `AltiumLibraryDDT.PcbLib`: authoritative PCB-footprint library.
- `library-manifest.json`: checksums, sizes, and declared entry counts.
- `docs/INVENTORY.md`: human-readable component inventory.
- `scripts/validate_repository.py`: dependency-free repository checks.
- `.github/`: contribution templates and CI configuration.

## Working rules

1. Read `README.md`, `CONTRIBUTING.md`, and `docs/VALIDATION.md` before editing.
2. Treat `.SchLib` and `.PcbLib` files as binary. Never reformat, merge, or
   partially rewrite them outside Altium Designer.
3. Do not invent component data. Use the current manufacturer datasheet and
   record its URL in the pull request.
4. Make symbol and footprint changes together when their mapping is affected.
5. Update `docs/INVENTORY.md`, `library-manifest.json`, and `CHANGELOG.md` when
   library contents change.
6. Do not commit Altium history, backup, preview, output, or workspace files.
7. Keep all repository-facing prose in English.
8. Keep changes focused; do not mix library modifications with unrelated
   repository maintenance.

## Validation

Run before every commit:

```bash
python3 scripts/validate_repository.py
git diff --check
```

For a library change, also complete the manual Altium checks documented in
`docs/VALIDATION.md`. CI cannot inspect graphical correctness or manufacturer
conformance.

## Pull requests

- Use a descriptive title and explain user-visible impact.
- Identify every affected symbol and footprint.
- Link authoritative datasheets.
- Include screenshots for graphical or mechanical changes.
- State the Altium Designer version used.
- Complete the pull request checklist without marking unperformed checks.

## Safety boundaries

- Never commit credentials, proprietary component libraries, or restricted
  datasheets.
- Never replace a source library with an exported or flattened derivative.
- Never change license terms or repository security settings as a side effect.
- If binary integrity is uncertain, stop and request an Altium review.
