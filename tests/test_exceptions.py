# -*- coding: utf-8 -*-
import pytest

import aiopygismeteo
from aiopygismeteo.exceptions import LocalityError


@pytest.mark.asyncio()
async def test_by_url() -> None:
    with pytest.raises(LocalityError):
        await aiopygismeteo.by_url("moscow-weather-4368")


@pytest.mark.asyncio()
async def test_by_name() -> None:
    with pytest.raises(LocalityError):
        await aiopygismeteo.by_name("волыфдаловыфалдоыфва")
