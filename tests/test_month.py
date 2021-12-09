# -*- coding: utf-8 -*-
import pytest
from utils import check_dict

import aiopygismeteo


@pytest.mark.asyncio
async def test_month() -> None:
    gm = await aiopygismeteo.by_url("weather-moscow-4368")
    month = await gm.month()
    for attr in (month.status, month.max_temperature, month.min_temperature):
        check_dict(attr, 21, 31)
