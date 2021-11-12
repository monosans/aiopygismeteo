# -*- coding: utf-8 -*-
import pytest

from aiopygismeteo import gismeteo


@pytest.mark.asyncio
async def test_locality_id() -> None:
    moscow = await gismeteo("https://www.gismeteo.ru/weather-moscow-4368/")
    assert moscow._base_endpoint == "/weather-moscow-4368/"


@pytest.mark.asyncio
async def test_locality_name() -> None:
    moscow = await gismeteo("Москва")
    assert moscow._base_endpoint == "/weather-moscow-4368/"
