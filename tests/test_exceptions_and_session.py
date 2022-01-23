# -*- coding: utf-8 -*-
import pytest
from aiohttp import ClientSession

from aiopygismeteo import Gismeteo, LocalityNotFound


@pytest.mark.asyncio()
async def test_locality_not_found() -> None:
    async with ClientSession() as s:
        with pytest.raises(LocalityNotFound):
            await Gismeteo(session=s).get_id_by_query("волыфдаловыфалдоыфва")
