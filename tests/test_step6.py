# -*- coding: utf-8 -*-
import pytest

from aiopygismeteo import Gismeteo


@pytest.mark.asyncio()
async def test_step6() -> None:
    await Gismeteo().step6(4368, days="3")
