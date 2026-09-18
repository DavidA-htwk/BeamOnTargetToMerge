# SPDX-FileCopyrightText: 2025-2026 ITER Organization
# SPDX-License-Identifier: LGPL-3.0-only
#
# This file is part of BeamOnTarget. See LICENSE (GNU LGPL v3) and GPLv3.txt.
"""Helpers to locate repository root resources from package modules."""

from __future__ import annotations

from pathlib import Path
import sys


def get_project_root() -> Path:
    """Return the repository root where config/assets/data folders live."""
    if getattr(sys, "frozen", False):
        return Path(sys.executable).resolve().parent
    # paths.py lives at src/beamontarget/paths.py -> repo root is parents[2]
    return Path(__file__).resolve().parents[2]


def project_path(*parts: str) -> Path:
    """Return an absolute path under the repository root."""
    return get_project_root().joinpath(*parts)
