# `GEOMETRY_EXAMPLE` — default example geometry

This folder holds the geometry used by the default `config.json`: two primitive
bodies, deliberately trivial, so that a fresh checkout produces a result in a
few seconds.

| File | Shape | Extent | Faces (as shipped) |
|---|---|---|---|
| `cube.stl` | 1 m cube | x, z in [-0.5, 0.5]; y in [-1.25, -0.25] | 12 |
| `sphere.stl` | sphere, r = 0.75 m | x, z in [-0.75, 0.75]; y in [0.10, 1.60] | 320 |

The two bodies sit **side by side in y**, both centred on z = 0, with a gap
between them. The example beam travels along +x, so roughly a third of the
beamlets strike the cube, a third the sphere, and a third pass between — which
is why the reported deposited power is less than the total beam power.

`config.json` sets `"target_length": 0.1`, so both meshes are subdivided on load
to a maximum edge length of 0.1 m: 3072 cells on the cube and 5120 on the
sphere. That is fine enough to show a readable power-density pattern while still
loading in well under a second. The refined copies are cached in
`geometry_cache_example/`.

Expect the sphere's power *density* to peak near the edge of the illuminated
cap, where the beam strikes at grazing incidence and the same power lands on a
smaller projected area. That is physically correct, not an artifact.

## Regenerating

Both meshes come from `trimesh` primitives:

```python
import trimesh
cube = trimesh.creation.box(extents=[1.0, 1.0, 1.0])
cube.apply_translation([0.0, -0.75, 0.0])
cube.export("GEOMETRY_EXAMPLE/cube.stl")

sphere = trimesh.creation.icosphere(subdivisions=2, radius=0.75)
sphere.apply_translation([0.0, 0.85, 0.0])
sphere.export("GEOMETRY_EXAMPLE/sphere.stl")
```

They are committed rather than generated at run time so that a fresh clone can
be validated, previewed with `--view-setup` and browsed in the GUI before
anything is run, and so the example stays identical across `trimesh` versions.

Not to be confused with `DUMMY/`, which `create_dummy_meshes()` writes into the
working directory on every run and which is gitignored.
