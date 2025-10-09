"""Асинхронная обёртка для Gismeteo API.

Examples:
    ```python
    async with aiopygismeteo.Gismeteo(token="56b30cb255.3443075") as gismeteo:
        search_results = await gismeteo.search.by_query("Москва")
        city_id = search_results[0].id
        current = await gismeteo.current.by_id(city_id)
    print(current)
    ```

    Кастомный базовый URL:

    ```python
    async with aiopygismeteo.Gismeteo(
        token=..., base_url=pydantic.AnyHttpUrl("https://api.example.com/v1")
    ) as gismeteo:
        ...
    ```

    Другой язык:

    ```python
    async with aiopygismeteo.Gismeteo(
        token=..., lang=aiopygismeteo.Lang.EN
    ) as gismeteo:
        ...
    ```

    Кастомная aiohttp.ClientSession:

    ```python
    async with aiohttp.ClientSession(
        timeout=aiohttp.ClientTimeout(total=60, connect=5)
    ) as session:
        gismeteo = aiopygismeteo.Gismeteo(token=..., session=session)
        ...
    ```
"""

from __future__ import annotations

from pygismeteo_base import models

from aiopygismeteo import types
from aiopygismeteo._gismeteo import Gismeteo

__version__ = "7.0.2"
__all__ = ("Gismeteo", "models", "types")
