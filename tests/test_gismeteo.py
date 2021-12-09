# -*- coding: utf-8 -*-
import pytest

import aiopygismeteo


@pytest.mark.asyncio
async def test_locality_id() -> None:
    moscow = await aiopygismeteo.by_url(
        "https://www.gismeteo.ru/weather-moscow-4368/"
    )
    assert moscow._BASE_ENDPOINT == "/weather-moscow-4368/"


@pytest.mark.asyncio
async def test_locality_name() -> None:
    moscow = await aiopygismeteo.by_name("Москва")
    assert moscow._BASE_ENDPOINT == "/weather-moscow-4368/"
