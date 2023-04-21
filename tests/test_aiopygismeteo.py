from __future__ import annotations

from aiohttp import ClientSession

from aiopygismeteo import Gismeteo


async def test_aiopygismeteo() -> None:
    async with ClientSession() as session:
        gm = Gismeteo(session=session)
        assert gm.session is session
        await gm.current.by_id(4368)
        await gm.current.by_coordinates(54.35, 52.52)

        await gm.step3.by_id(4368, days=10)
        await gm.step3.by_coordinates(54.35, 52.52, days=10)

        await gm.step6.by_id(4368, days=10)
        await gm.step6.by_coordinates(54.35, 52.52, days=10)

        await gm.step24.by_id(4368, days=10)
        await gm.step24.by_coordinates(54.35, 52.52, days=10)

        await gm.search.by_query("lond")
        await gm.search.by_coordinates(54.35, 52.52, limit=36)

    assert gm.lang is None
    gm.lang = "en"
    assert gm.lang == "en"

    gm.session = None
    assert gm.session is None

    await gm.search.by_ip("8.8.8.8")

    assert gm.token is None
    gm.token = ""
    assert gm.token == ""  # noqa: PLC1901
