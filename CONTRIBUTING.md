# Contributing to BeamOnTarget

Thanks for your interest in BeamOnTarget. This document explains how to set up a
development environment, what we expect from a change, and how contributions are
licensed.

---

## Getting set up

```bash
git clone https://github.com/iterorganization/BeamOnTarget.git
cd BeamOnTarget
python3 -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -e .
```

On Linux you need a C compiler, because `pyembree` / `embreex` are built from
source. On Debian/Ubuntu, `python3-tk` is also required for the GUI.

Check the install:

```bash
python -c "import beamontarget; print(beamontarget.__file__)"
beamontarget                      # launches the GUI
beamontarget-run --help           # command-line entry point
```

---

## Making a change

1. **Open an issue first** for anything larger than a bug fix, so the approach
   can be agreed before you spend time on it.
2. **Branch from `main`.** Use a short descriptive branch name, e.g.
   `fix/smoother-normals` or `feature/gaussian-source`.
3. **Keep the change focused.** One logical change per pull request. Unrelated
   reformatting makes review much harder.
4. **Describe the physics.** If your change affects results — cross sections,
   field handling, tracking, deposition — say in the pull request what changes
   numerically and how you checked it.

Every push and pull request runs the CI workflow in
`.github/workflows/ci.yml`: it installs the package from a clean checkout on
Python 3.10 and 3.12, imports every module, checks the console entry points
resolve, validates the shipped `config.json`, and builds the distributions.
Please make sure it is green before asking for review.

---

## Code conventions

- Target **Python 3.10-3.12**; do not use syntax newer than 3.10.
- Follow the surrounding style. The codebase uses 4-space indentation, snake
  case, type hints on new public functions, and NumPy-style docstrings.
- **Units are SI unless the name says otherwise**, and names carry their unit
  as a suffix (`energy_ev`, `radius_m`, `v_rid_v`). Keep that convention.
- Prefer vectorised NumPy over Python loops in anything on the per-particle
  path — the engine routinely handles billions of particles.
- No site-specific absolute paths, hostnames, usernames or institutional
  directory layouts in committed files. Anything environment-dependent belongs
  in `config.json` with a portable default.
- Do not commit input data, geometry, field maps, or simulation output. See
  `.gitignore`.

Every source file carries an SPDX header. Copy it into new files:

```python
# SPDX-FileCopyrightText: 2025-2026 ITER Organization
# SPDX-License-Identifier: LGPL-3.0-only
#
# This file is part of BeamOnTarget. See LICENSE (GNU LGPL v3) and GPLv3.txt.
```

---

## Reporting bugs

Open an issue including:

- what you ran (command, or GUI actions), and the relevant part of your
  `config.json`;
- what you expected and what happened instead;
- the full traceback, if there is one;
- your OS, Python version, and BeamOnTarget version.

A minimal geometry and beam configuration that reproduces the problem is the
single most useful thing you can provide. Please make sure anything you attach
is yours to share.

---

## Licensing of contributions

BeamOnTarget is released under the **GNU Lesser General Public License v3**
(`LGPL-3.0-only`). By contributing, you agree that your contribution is licensed
under the same terms.

Sign off each commit to certify the
[Developer Certificate of Origin](https://developercertificate.org/):

```bash
git commit -s -m "Your commit message"
```

This appends a `Signed-off-by:` line using your `user.name` and `user.email`.

Please add yourself to the **Contributors** section of [AUTHORS](AUTHORS) in the
same pull request as your first contribution.
