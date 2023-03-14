from __future__ import annotations

from aiohttp import ClientSession

from aiopygismeteo import Gismeteo


async def test_aiopygismeteo() -> None:
    async with ClientSession() as session:
        gismeteo = Gismeteo(session=session)
        assert gismeteo.session is session
        await gismeteo.current.by_id(4368)
        await gismeteo.current.by_coordinates(54.35, 52.52)

        await gismeteo.step3.by_id(4368, days=10)
        await gismeteo.step3.by_coordinates(54.35, 52.52, days=10)

        await gismeteo.step6.by_id(4368, days=10)
        await gismeteo.step6.by_coordinates(54.35, 52.52, days=10)

        await gismeteo.step24.by_id(4368, days=10)
        await gismeteo.step24.by_coordinates(54.35, 52.52, days=10)

        await gismeteo.search.by_query("lond")
        await gismeteo.search.by_coordinates(54.35, 52.52, limit=36)

    assert gismeteo.lang is None
    gismeteo.lang = "en"
    assert gismeteo.lang == "en"

    gismeteo.session = None
    assert gismeteo.session is None

    await gismeteo.search.by_ip("8.8.8.8")

    assert gismeteo.token is None
    gismeteo.token = ""
    assert gismeteo.token == ""  # noqa: PLC1901
