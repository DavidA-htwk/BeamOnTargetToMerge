# `CAL` — calorimeter (default geometry)

This folder ships the default calorimeter target used by `config.json`:
`BENCHMARK.stl`, a single flat plane normal to the beam axis.

| | |
|---|---|
| Position along beam (x) | 7.750 m |
| Size | 0.800 m (y) x 1.700 m (z) |
| Tessellation | 131 072 triangles |

It is a **plane, not a model of any particular calorimeter** — a benchmark
surface for checking total intercepted power and power density profiles against
an analytic expectation. The high triangle count gives fine power-density
resolution across the beam footprint; reduce it if you want faster runs and
coarser output.

Every `.stl` in this folder is loaded as part of the `CAL` group and inherits
that group's settings from `config.json`.

`.stl` files here are **not** ignored by git. Check your licensing and
export-control obligations before committing geometry of your own.

## Which config uses this

This folder is geometry for `config_beamline_example.json`, not for the
default `config.json`. Run it with
`beamontarget-run -i config_beamline_example.json`. The default example uses
the cube and sphere in `GEOMETRY_EXAMPLE/` instead.
