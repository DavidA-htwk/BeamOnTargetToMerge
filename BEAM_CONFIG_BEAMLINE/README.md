# `BEAM_CONFIG_BEAMLINE` — beamline example particle source

`beamontarget-run` batches over every `.bl` file in the folder named by
`PARTICLE_SOURCE_DIR` in `config.json`, running one simulation per file.

This folder belongs to `config_beamline_example.json`, the second shipped
example. Run it with:

```bash
beamontarget-run -i config_beamline_example.json
```

For the small default example see `BEAM_CONFIG_EXAMPLE/`.

## Shipped example

`example_bl_config.bl` is a worked example, provided so that a fresh checkout
exercises the beamline geometry in `NEU/`, `RID/` and `CAL/`.

It describes a nominal, unsteered beam: 1280 beamlets on a 20 x 64 grid, all
parallel, with every aiming angle zeroed apart from a uniform design
inclination. That inclination is expressed in the file as the direction
component `DirZ = -0.0492`, which corresponds to 49.22 mrad (2.820 deg)
downward — `DirZ` is a unit-vector component, not an angle in mrad.

| | |
|---|---|
| Particles | H-, 870 keV, monoenergetic |
| Divergence | 3 mrad core, 30 mrad halo, halo fraction 0.15 |
| Beamlet size | sigma_y = sigma_z = 0.1 mm |
| Current density | 233.454317 A/m^2 per beamlet |
| Source plane | x = 0, y in [-0.28, 0.28] m, z in [-0.759, 0.759] m |

The file's header comments repeat this. Copy it and edit the columns to
describe your own beam.

## File format

Whitespace-separated columns with a header row; lines beginning with `#` are
ignored. One row per beamlet.

| Column | Meaning |
|---|---|
| `Index` | Beamlet identifier, carried through to per-source output |
| `CenterX/Y/Z` | Beamlet origin (m) |
| `DirX/Y/Z` | Unit direction vector |
| `SigmaY_m`, `SigmaZ_m` | Beamlet spot size (m) |
| `DeltaY_rad`, `DeltaZ_rad` | Core divergence, e-folding half-angle |
| `DeltaHY_rad`, `DeltaHZ_rad` | Halo divergence, e-folding half-angle |
| `HaloFraction` | Fraction of beamlet current carried by the halo |
| `Mass_kg`, `Charge_e` | Particle mass and charge state |
| `CurrentDensity_A_m2` | Current density; multiplied by the beamlet area |
| `MinEnergy_eV`, `MaxEnergy_eV` | Energy range (equal values give a monoenergetic beam) |

Divergences are converted from e-folding to sigma internally (divided by
`sqrt(2)`), and the core is built as a `GaussianTwissBeam`.

## Adding your own

`*.bl` is listed in `.gitignore`, with an exception for the shipped
`example_*.bl` files. Beam
configurations describe a specific machine and are treated as input data, not
source code — so your own files stay out of the repository by default. Check
your licensing and export-control obligations before committing any.
