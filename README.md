# Personal Altium Library

[![Repository checks](https://github.com/ddtdanilo/Personal-Altium-Library/actions/workflows/quality.yml/badge.svg)](https://github.com/ddtdanilo/Personal-Altium-Library/actions/workflows/quality.yml)
[![License: CERN-OHL-P-2.0](https://img.shields.io/badge/license-CERN--OHL--P--2.0-00629B.svg)](LICENSE)
[![Altium Designer](https://img.shields.io/badge/Altium%20Designer-library-A5915F.svg)](https://www.altium.com/altium-designer)
[![Components](https://img.shields.io/badge/schematic%20symbols-81-2F80ED.svg)](docs/INVENTORY.md)
[![Footprints](https://img.shields.io/badge/PCB%20footprints-106-27AE60.svg)](docs/INVENTORY.md)

A curated collection of reusable schematic symbols and PCB footprints for
Altium Designer, assembled from real hardware projects over several years.

The library covers common passives, connectors, development boards, power
modules, wireless modules, sensors, relays, and integrated circuits. It is
intended to provide a practical starting point—not a substitute for checking
the latest manufacturer documentation.

## Library at a glance

| File | Purpose | Entries |
| --- | --- | ---: |
| [`AltiumLibraryDDT.SchLib`](AltiumLibraryDDT.SchLib) | Schematic symbols | 81 |
| [`AltiumLibraryDDT.PcbLib`](AltiumLibraryDDT.PcbLib) | PCB footprints | 106 |

See the [complete inventory](docs/INVENTORY.md) for every available symbol and
footprint.

## Quick start

1. Download or clone this repository.
2. Open your Altium Designer project.
3. Choose **Panels → Components**, then open the panel menu.
4. Select **File-based Libraries Preferences**.
5. Install `AltiumLibraryDDT.SchLib` and `AltiumLibraryDDT.PcbLib`.
6. Search for a component and place it in your design.

Detailed installation, update, and verification guidance is available in the
[usage guide](docs/USAGE.md).

```bash
git clone https://github.com/ddtdanilo/Personal-Altium-Library.git
```

## Important engineering notice

Every symbol, pin assignment, pad stack, courtyard, 3D body, and mechanical
dimension must be verified against the current manufacturer datasheet before
fabrication. Naming conventions and design rules may differ from your
organization's standards. The repository is supplied without a guarantee of
fitness for a particular design.

At minimum, verify:

- symbol pin numbers, names, types, and hidden power pins;
- footprint pad numbers, pitch, hole sizes, and polarity/orientation marks;
- solder-mask, paste, courtyard, assembly, and component-clearance geometry;
- the manufacturer's recommended land pattern and your fabricator's rules;
- the symbol-to-footprint mapping in your project.

## Contributing

Corrections and well-documented additions are welcome. Read
[`CONTRIBUTING.md`](CONTRIBUTING.md) before opening an issue or pull request.
New components should include the manufacturer part number, datasheet source,
symbol and footprint checks, and a clear description of what changed.

Repository automation verifies file integrity, inventory metadata, documentation
links, and contribution hygiene. Altium-specific visual and electrical review
still requires Altium Designer.

## Documentation

- [Usage and installation](docs/USAGE.md)
- [Component inventory](docs/INVENTORY.md)
- [Validation policy](docs/VALIDATION.md)
- [Contributing](CONTRIBUTING.md)
- [Security policy](SECURITY.md)
- [Support](SUPPORT.md)
- [Changelog](CHANGELOG.md)

## License

The library design files and documentation are licensed under the
[CERN Open Hardware Licence Version 2 – Permissive](LICENSE). By contributing,
you agree that your contribution is made available under the same license.

Copyright © 2019–2026 Danilo Duarte and contributors.
