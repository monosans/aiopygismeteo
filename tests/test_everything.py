from aiohttp import ClientSession

from aiopygismeteo import Gismeteo


async def test_everything() -> None:
    async with ClientSession() as s:
        g = Gismeteo(session=s)
        await g.current.by_id(4368)
        await g.current.by_coordinates(54.35, 52.52)

        await g.step3.by_id(4368, days=10)
        await g.step3.by_coordinates(54.35, 52.52, days=10)

        await g.step6.by_id(4368, days=10)
        await g.step6.by_coordinates(54.35, 52.52, days=10)

        await g.step24.by_id(4368, days=10)
        await g.step24.by_coordinates(54.35, 52.52, days=10)

        await g.search.by_query("lond")
        await g.search.by_coordinates(54.35, 52.52, limit=36)

    assert g.lang is None
    g.lang = "en"
    assert g.lang == "en"

    assert isinstance(g.session, ClientSession)
    g.session = None
    assert g.session is None

    await g.search.by_ip("8.8.8.8")

    assert g.token is None
    g.token = ""
    assert g.token == ""
