# -*- coding: utf-8 -*-
import pytest

import aiopygismeteo


@pytest.mark.asyncio()
async def test_step24() -> None:
    await aiopygismeteo.step24(4368, days="3")
