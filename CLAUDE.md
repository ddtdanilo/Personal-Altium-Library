# CLAUDE.md

Follow [`AGENTS.md`](AGENTS.md) as the authoritative instructions for work in
this repository.

Before proposing a change, inspect the relevant library, manifest, inventory,
validation policy, and recent changelog entries. Keep repository-facing content
in English and never guess electrical or mechanical component data.

Required automated checks:

```bash
python3 scripts/validate_repository.py
git diff --check
```

Binary `.SchLib` and `.PcbLib` changes additionally require the manual Altium
Designer review described in [`docs/VALIDATION.md`](docs/VALIDATION.md).
