# -*- coding: utf-8 -*-
import pytest

from aiopygismeteo import gismeteo
from aiopygismeteo.exceptions import InvalidLocalityID, LocalityNotFound


@pytest.mark.asyncio
async def test_invalid_locality_id() -> None:
    with pytest.raises(InvalidLocalityID):
        await gismeteo("moscow-weather-4368")


@pytest.mark.asyncio
async def test_locality_not_found() -> None:
    with pytest.raises(LocalityNotFound):
        await gismeteo("волыфдаловыфалдоыфва")
