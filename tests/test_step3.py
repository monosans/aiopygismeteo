# -*- coding: utf-8 -*-
import pytest

import aiopygismeteo


@pytest.mark.asyncio()
async def test_step3() -> None:
    await aiopygismeteo.step3(4368, days="3")
