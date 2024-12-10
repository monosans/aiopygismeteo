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

from aiopygismeteo._endpoints.current import Current
from aiopygismeteo._endpoints.search import Search
from aiopygismeteo._endpoints.step3 import Step3
from aiopygismeteo._endpoints.step6 import Step6
from aiopygismeteo._endpoints.step24 import Step24

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
