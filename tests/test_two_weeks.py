# -*- coding: utf-8 -*-
import pytest
from utils import check_dict

import aiopygismeteo


@pytest.mark.asyncio
async def test_two_weeks() -> None:
    gm = await aiopygismeteo.by_url("weather-moscow-4368")
    two_weeks = await gm.two_weeks()
    for attr in (
        two_weeks.status,
        two_weeks.max_temperature,
        two_weeks.min_temperature,
        two_weeks.gusts,
        two_weeks.precipitation,
        two_weeks.temperature,
        two_weeks.wind_speed,
        two_weeks.wind_direction,
        two_weeks.max_pressure,
        two_weeks.min_pressure,
        two_weeks.humidity,
        two_weeks.gm_activity,
    ):
        check_dict(attr, 14)
