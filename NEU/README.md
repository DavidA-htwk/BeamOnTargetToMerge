# `NEU` — neutraliser panels (default geometry)

This folder ships the default neutraliser geometry used by `config.json`:
`NEU1.stl` to `NEU5.stl`, five axis-aligned rectangular slabs forming a channel
the beam passes through.

| | |
|---|---|
| Extent along beam (x) | 1.900 m to 4.900 m |
| Height (z) | 1.700 m |
| Panel spacing (y) | five slabs between y = -0.318 m and y = +0.319 m |
| Tessellation | 24 576 triangles per panel |

These are **generic blocks**, not machine design data. They exist so that a
fresh checkout runs out of the box and so that results can be compared against
a known, simple configuration. The fine tessellation is deliberate: deposited
power density is reported per mesh cell, so cell size sets the resolution of
the result.

Replace them with your own `.stl` files, or point `GEOMETRY_FOLDERS` in
`config.json` at a different folder. Every `.stl` in this folder is loaded as
part of the `NEU` group and inherits that group's settings (`scale`,
`target_length`, `save_details`, `is_diagnostic`, `save_impact_data`,
`show_in_plot`).

`.stl` files here are **not** ignored by git. Check your licensing and
export-control obligations before committing geometry of your own.

## Which config uses this

This folder is geometry for `config_beamline_example.json`, not for the
default `config.json`. Run it with
`beamontarget-run -i config_beamline_example.json`. The default example uses
the cube and sphere in `GEOMETRY_EXAMPLE/` instead.
