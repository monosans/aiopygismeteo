# -*- coding: utf-8 -*-
import pytest

from aiopygismeteo import gismeteo


@pytest.mark.asyncio
async def test_now() -> None:
    moscow = await gismeteo("weather-moscow-4368")
    now = await moscow.now()
    for attr in (
        now.status,
        now.temperature,
        now.real_feel,
        now.sunrise,
        now.sunset,
        now.wind_speed,
        now.wind_direction,
        now.pressure,
        now.humidity,
        now.gm_activity,
        now.water,
    ):
        assert isinstance(attr, str) and attr
