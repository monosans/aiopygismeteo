# -*- coding: utf-8 -*-
import pytest
from aiohttp import ClientSession

import aiopygismeteo
from aiopygismeteo.exceptions import LocalityNotFound


@pytest.mark.asyncio()
async def test_locality_not_found() -> None:
    with pytest.raises(LocalityNotFound):
        async with ClientSession() as s:
            await aiopygismeteo.search.id_by_query(
                "волыфдаловыфалдоыфва", session=s
            )
