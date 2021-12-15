# -*- coding: utf-8 -*-
import pytest

import aiopygismeteo


@pytest.mark.asyncio()
async def test_search_and_session() -> None:
    assert await aiopygismeteo.search.id_by_query("Москва") == 4368
