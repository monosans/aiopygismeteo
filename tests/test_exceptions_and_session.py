# -*- coding: utf-8 -*-
import pytest
from aiohttp import ClientSession

import aiopygismeteo
from aiopygismeteo.exceptions import LocalityNotFound


@pytest.mark.asyncio()
async def test_locality_not_found() -> None:
    async with ClientSession() as s:
        with pytest.raises(LocalityNotFound):
            await aiopygismeteo.search.id_by_query(
                "волыфдаловыфалдоыфва", session=s
            )
