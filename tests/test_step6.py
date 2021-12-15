# -*- coding: utf-8 -*-
import pytest

import aiopygismeteo


@pytest.mark.asyncio()
async def test_step6() -> None:
    await aiopygismeteo.step6(4368, days="3")
