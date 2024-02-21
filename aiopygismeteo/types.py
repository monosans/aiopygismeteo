"""Может пригодиться для типизации кода, использующего библиотеку."""

from __future__ import annotations

from pygismeteo_base.types import (
    Lang,
    Latitude,
    LocalityID,
    Longitude,
    SearchLimit,
    Step3Days,
    Step6Days,
    Step24Days,
)

from ._current import Current
from ._search import Search
from ._step_n import Step3, Step6, Step24

__all__ = (
    "Current",
    "Lang",
    "Latitude",
    "LocalityID",
    "Longitude",
    "Search",
    "SearchLimit",
    "Step3",
    "Step3Days",
    "Step6",
    "Step6Days",
    "Step24",
    "Step24Days",
)
