# Contributing

Thank you for helping improve the Personal Altium Library. Contributions should
make the library safer, easier to verify, and more useful to other designers.

## Before you start

- Search open issues and pull requests for related work.
- Use an issue for a substantial addition or uncertain design decision.
- Base component data on the current manufacturer's documentation.
- Do not contribute proprietary, confidential, or redistribution-restricted
  material.

## Development workflow

1. Fork the repository and create a focused branch from the default branch.
2. Edit library files in Altium Designer.
3. Verify the symbol and footprint using the checklist below.
4. Update `docs/INVENTORY.md` if entries were added, renamed, or removed.
5. Update `library-manifest.json` after any library binary changes:

   ```bash
   python3 scripts/update_manifest.py
   ```

6. Add an entry under `Unreleased` in `CHANGELOG.md`.
7. Run the automated checks:

   ```bash
   python3 scripts/validate_repository.py
   git diff --check
   ```

8. Open a pull request and complete its checklist.

## Component acceptance checklist

### Schematic symbol

- Pin designators match the datasheet.
- Pin names and electrical types are correct.
- Power, ground, no-connect, and hidden pins are intentional.
- Multi-part units and pin swaps are documented.
- The symbol is legible on the standard grid.

### PCB footprint

- The manufacturer land pattern and package revision are identified.
- Pad numbers map exactly to the symbol.
- Pitch, pad dimensions, drill sizes, and plated-hole settings are verified.
- Pin 1, polarity, and orientation marks are unambiguous.
- Silkscreen does not overlap exposed copper or pads.
- Assembly, courtyard, body, and height information is checked.
- Paste and solder-mask expansions are intentional.
- Any 3D model has the correct origin, rotation, scale, and license.

### Final review

- Run Altium's library/component checks.
- Place the component in a temporary schematic and PCB.
- Confirm the schematic-to-PCB update maps every pin and pad.
- Inspect the result in 2D and 3D.
- Record the Altium version and datasheet URL in the pull request.

## Commit and pull request guidance

Use short, imperative commit subjects, such as:

```text
Add JST B2B-XH connector footprint
Correct ACS758 pin mapping
Document Altium library installation
```

Keep binary library changes separate from unrelated cleanup. Pull requests must
explain what changed, why it changed, how it was validated, and which entries
are affected. Screenshots are expected for graphical or mechanical changes.

## Community standards

Participation in this project is governed by
[`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md). By contributing, you agree that your
work may be distributed under the repository's CERN-OHL-P-2.0 license.
