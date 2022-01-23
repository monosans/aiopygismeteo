# -*- coding: utf-8 -*-
import pytest

from aiopygismeteo import Gismeteo


@pytest.mark.asyncio()
async def test_step24() -> None:
    await Gismeteo().step24(4368, days="3")
