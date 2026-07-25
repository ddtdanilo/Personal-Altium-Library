# Usage Guide

## Requirements

- Altium Designer with support for file-based schematic and PCB libraries.
- A local copy of this repository.

The libraries are binary Altium files. GitHub can store and distribute them, but
cannot render or validate their graphical contents.

## Install the libraries

1. Clone the repository or download the latest release archive.
2. In Altium Designer, open the **Components** panel.
3. Open the panel menu and select **File-based Libraries Preferences**.
4. Choose **Install**.
5. Select:
   - `AltiumLibraryDDT.SchLib`
   - `AltiumLibraryDDT.PcbLib`
6. Confirm that both files appear in the installed library list.

Menu names can vary slightly between Altium releases. Search Altium's
preferences for **File-based Libraries** if the panel option is not visible.

## Use a component

1. Search the Components panel by manufacturer part number or library name.
2. Review the symbol pins and linked footprint before placement.
3. Place the symbol on the schematic.
4. Transfer the design to the PCB.
5. Confirm that every symbol pin maps to the intended footprint pad.
6. Run electrical and design-rule checks.

The [inventory](INVENTORY.md) contains the exact entry names currently declared
by the libraries.

## Update an existing installation

```bash
git pull --ff-only
```

If Altium has cached an older revision, remove and reinstall both library files,
or restart Altium Designer. Review the changelog before updating an active
production design.

Pin a known repository revision for reproducible projects:

```bash
git checkout <commit-or-tag>
```

Do not assume that a later library revision is a drop-in replacement for a
component already placed in a released design.

## Verify before fabrication

For every used entry, compare the symbol and footprint with the exact ordering
code and revision of the current manufacturer datasheet. Pay special attention
to:

- mirrored connector pin numbering;
- module variants with similar names;
- thermal pads and exposed copper;
- polarity and pin-1 markings;
- through-hole drill tolerances;
- solder-mask and paste settings;
- 3D-body orientation and maximum height.

Follow the complete [validation policy](VALIDATION.md) for changes or production
use.

## Troubleshooting

### The component is not visible

- Confirm that the schematic library is installed and enabled.
- Search by a shorter fragment of the entry name.
- Remove and reinstall the library if Altium cached an older file.

### The footprint is missing

- Install the PCB library as well as the schematic library.
- Open the symbol's model properties and confirm the referenced footprint name.
- Report a broken mapping through the component issue form.

### Git reports a binary conflict

Do not attempt to merge binary library content. Choose the correct complete
version, reopen it in Altium Designer, reapply the other change manually, and
repeat all validation checks.
