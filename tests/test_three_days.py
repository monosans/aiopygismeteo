# -*- coding: utf-8 -*-
import pytest
from utils import check_dict

import aiopygismeteo


@pytest.mark.asyncio()
async def test_three_days() -> None:
    gm = await aiopygismeteo.by_url("weather-moscow-4368")
    three_days = await gm.three_days()
    for time in (
        three_days.night,
        three_days.morning,
        three_days.afternoon,
        three_days.evening,
    ):
        for attr in (
            time.status,
            time.temperature,
            time.gusts,
            time.precipitation,
            time.wind_speed,
            time.wind_direction,
            time.falling_snow,
            time.snow_depth,
            time.pressure,
            time.humidity,
            time.ultraviolet_index,
            time.gm_activity,
        ):
            check_dict(attr, 3)
