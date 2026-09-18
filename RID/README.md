# `RID` — residual ion dump panels (default geometry)

This folder ships the default residual ion dump geometry used by `config.json`:
`RID1.stl` to `RID5.stl`, five axis-aligned rectangular slabs.

| | |
|---|---|
| Extent along beam (x) | 5.400 m to 7.200 m |
| Height (z) | 1.700 m |
| Panel spacing (y) | five slabs between y = -0.263 m and y = +0.263 m |
| Tessellation | 12 288 triangles per panel |

The x extent matches the `EXTERNAL_FIELD` → `Ey` → `rid_ey` region in
`config.json` (`x_min_m: 5.4`, `x_max_m: 7.2`), so the default deflecting field
acts exactly over the length of these panels. If you replace this geometry,
update that field region to match.

These are **generic blocks**, not machine design data. Every `.stl` in this
folder is loaded as part of the `RID` group and inherits that group's settings
from `config.json`.

`.stl` files here are **not** ignored by git. Check your licensing and
export-control obligations before committing geometry of your own.

## Which config uses this

This folder is geometry for `config_beamline_example.json`, not for the
default `config.json`. Run it with
`beamontarget-run -i config_beamline_example.json`. The default example uses
the cube and sphere in `GEOMETRY_EXAMPLE/` instead.
