# -*- coding: utf-8 -*-
import pytest

from aiopygismeteo import Gismeteo


@pytest.mark.asyncio()
async def test_search_and_session() -> None:
    assert await Gismeteo().get_id_by_query("Москва") == 4368
