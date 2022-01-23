# -*- coding: utf-8 -*-
import pytest

from aiopygismeteo import Gismeteo


@pytest.mark.asyncio()
async def test_current() -> None:
    await Gismeteo().current(4368)
