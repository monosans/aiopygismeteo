# -*- coding: utf-8 -*-
import pytest

import aiopygismeteo


@pytest.mark.asyncio()
async def test_current() -> None:
    await aiopygismeteo.current(4368)
