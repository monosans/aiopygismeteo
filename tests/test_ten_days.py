# -*- coding: utf-8 -*-
import pytest
from utils import check_dict

from aiopygismeteo import gismeteo


@pytest.mark.asyncio
async def test_ten_days() -> None:
    gm = await gismeteo("weather-moscow-4368")
    ten_days = await gm.ten_days()
    for attr in (
        ten_days.status,
        ten_days.max_temperature,
        ten_days.min_temperature,
        ten_days.precipitation,
        ten_days.temperature,
        ten_days.wind_speed,
        ten_days.wind_direction,
        ten_days.gusts,
        ten_days.max_pressure,
        ten_days.min_pressure,
        ten_days.humidity,
        ten_days.gm_activity,
        ten_days.ultraviolet_index,
        ten_days.falling_snow,
        ten_days.snow_depth,
    ):
        check_dict(attr, 10)
