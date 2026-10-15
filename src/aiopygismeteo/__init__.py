"""Асинхронная обёртка для Gismeteo API.

Документация: <https://monosans.github.io/aiopygismeteo>.

Examples:
    ```python
    async with aiopygismeteo.Gismeteo(token="56b30cb255.3443075") as gismeteo:
        city = (await gismeteo.search.by_query("Москва"))[0]
        current = await gismeteo.current.by_id(city.id)
    print(current.temperature.air.c)
    ```
"""

from __future__ import annotations

from pygismeteo_base import models

from aiopygismeteo import types
from aiopygismeteo._gismeteo import Gismeteo

__version__ = "7.0.5"
__all__ = ("Gismeteo", "models", "types")
