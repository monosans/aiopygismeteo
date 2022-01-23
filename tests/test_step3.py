# -*- coding: utf-8 -*-
import pytest

from aiopygismeteo import Gismeteo


@pytest.mark.asyncio()
async def test_step3() -> None:
    await Gismeteo().step3(4368, days="3")
