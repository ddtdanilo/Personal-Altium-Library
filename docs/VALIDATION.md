# Validation Policy

Validation has two layers: automated repository-integrity checks and manual
engineering review in Altium Designer. Both are required for a library change.

## Automated validation

Run:

```bash
python3 scripts/validate_repository.py
git diff --check
```

The validator checks:

- required project and community files;
- compound-file signatures for both Altium libraries;
- exact file size and SHA-256 metadata from `library-manifest.json`;
- declared symbol and footprint counts;
- local Markdown links;
- common generated or backup files that must not be committed.

CI runs the same checks on every pull request and default-branch push.

To refresh integrity metadata after an intentional binary change:

```bash
python3 scripts/update_manifest.py
python3 scripts/validate_repository.py
```

Review the resulting checksum and size diff. An unexpected binary change must
never be accepted only because the manifest was regenerated.

## Manual Altium validation

### Library integrity

- Open both source libraries without conversion or repair warnings.
- Compile or run the available library checks.
- Confirm that the edited entries can be opened and saved normally.
- Verify that only intended library files changed.

### Schematic review

- Compare every pin number, name, type, and unit with the datasheet.
- Confirm hidden pins and power pins are intentional.
- Check default designators, comments, parameters, and footprint links.
- Verify readability on the standard grid.

### Footprint review

- Compare pad geometry with the manufacturer's recommended land pattern.
- Check pad numbering, plated status, drills, slots, and thermal pads.
- Inspect copper, solder-mask, paste, silkscreen, assembly, and courtyard layers.
- Check the origin, rotation, pin-1 indicator, component height, and 3D model.
- Apply the project's fabrication tolerances and density-level requirements.

### Integration review

- Place the component in a temporary schematic.
- Transfer it to a temporary PCB.
- Confirm all pin-to-pad mappings.
- Run electrical and PCB design-rule checks.
- Inspect both sides in 2D and 3D.

## Evidence expected in a pull request

- exact component and footprint names;
- manufacturer and full ordering code;
- datasheet URL and revision/date;
- Altium Designer version;
- screenshots of the symbol, footprint, and 3D view when relevant;
- a concise record of automated and manual checks.

Automated success does not certify a component for fabrication.
