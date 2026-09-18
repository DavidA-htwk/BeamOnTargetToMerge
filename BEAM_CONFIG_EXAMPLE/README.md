# `BEAM_CONFIG_EXAMPLE` — default example beam

`example_simple.bl` is the particle source used by the default `config.json`.
It pairs with the cube and sphere in `GEOMETRY_EXAMPLE/`.

| | |
|---|---|
| Beamlets | 50, randomly placed on the source plane x = -3.0 m |
| Particles | H-, 100 keV, monoenergetic |
| Direction | +x, with ~2 mrad Gaussian jitter in y and z |
| Divergence | 5 mrad core, 30 mrad halo, halo fraction 0.1 |
| Beamlet size | sigma_y = sigma_z = 1 mm |
| Spread | y in [-1.25, 1.60] m, z in [-0.50, 0.50] m |
| Beam power | exactly 1 kW per beamlet, **50 kW total** |

The current density is `100/pi = 31.830988618379067` A/m^2, which with
`BEAMLET_RADIUS_M = 0.01` in `config.json` gives exactly 0.01 A and so exactly
1 kW per beamlet. That makes the total a round number you can check the output
against: with `NUM_PARTICLES_PER_BEAMLET = 10000` the run deposits about 37 kW
of the 50 kW incident, the rest passing between the two bodies.

Positions are drawn from `numpy.random.default_rng(20260918)`, so the file is
reproducible. The header comments record the full recipe.

## File format

Whitespace-separated columns with a header row; lines beginning with `#` are
ignored. One row per beamlet. See `BEAM_CONFIG_BEAMLINE/README.md` for the full
column reference.

## Adding your own

`*.bl` is gitignored except for the shipped `example_*.bl` files, so your own
beam configurations stay out of the repository by default.

Note that **every** `.bl` file in the folder named by `PARTICLE_SOURCE_DIR`
becomes a separate full simulation run. Drop a second file in here and the
example takes twice as long.
