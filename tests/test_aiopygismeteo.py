from __future__ import annotations

from ipaddress import IPv4Address

import pytest
from aiohttp import ClientResponseError

import aiopygismeteo


@pytest.mark.xfail(raises=ClientResponseError)
async def test_current_by_id(gismeteo_token: str, location_id: int) -> None:
    async with aiopygismeteo.Gismeteo(token=gismeteo_token) as gismeteo:
        r = await gismeteo.current.by_id(location_id)
    assert isinstance(r, aiopygismeteo.models.current.Model)


@pytest.mark.xfail(raises=ClientResponseError)
async def test_current_by_coordinates(
    gismeteo: aiopygismeteo.Gismeteo, coordinates: tuple[float, float]
) -> None:
    r = await gismeteo.current.by_coordinates(*coordinates)
    assert isinstance(r, aiopygismeteo.models.current.Model)


@pytest.mark.xfail(raises=ClientResponseError)
async def test_step3_by_id(
    gismeteo: aiopygismeteo.Gismeteo, location_id: int
) -> None:
    r = await gismeteo.step3.by_id(location_id, days=10)
    assert isinstance(r, aiopygismeteo.models.step3.Model)


@pytest.mark.xfail(raises=ClientResponseError)
async def test_step3_by_coordinates(
    gismeteo: aiopygismeteo.Gismeteo, coordinates: tuple[float, float]
) -> None:
    r = await gismeteo.step3.by_coordinates(*coordinates, days=10)
    assert isinstance(r, aiopygismeteo.models.step3.Model)


@pytest.mark.xfail(raises=ClientResponseError)
async def test_step6_by_id(
    gismeteo: aiopygismeteo.Gismeteo, location_id: int
) -> None:
    r = await gismeteo.step6.by_id(location_id, days=10)
    assert isinstance(r, aiopygismeteo.models.step6.Model)


@pytest.mark.xfail(raises=ClientResponseError)
async def test_step6_by_coordinates(
    gismeteo: aiopygismeteo.Gismeteo, coordinates: tuple[float, float]
) -> None:
    r = await gismeteo.step6.by_coordinates(*coordinates, days=10)
    assert isinstance(r, aiopygismeteo.models.step6.Model)


@pytest.mark.xfail(raises=ClientResponseError)
async def test_step24_by_id(
    gismeteo: aiopygismeteo.Gismeteo, location_id: int
) -> None:
    r = await gismeteo.step24.by_id(location_id, days=10)
    assert isinstance(r, aiopygismeteo.models.step24.Model)


@pytest.mark.xfail(raises=ClientResponseError)
async def test_step24_by_coordinates(
    gismeteo: aiopygismeteo.Gismeteo, coordinates: tuple[float, float]
) -> None:
    r = await gismeteo.step24.by_coordinates(*coordinates, days=10)
    assert isinstance(r, aiopygismeteo.models.step24.Model)


@pytest.mark.xfail(raises=ClientResponseError)
@pytest.mark.usefixtures("_pydantic_ignore_extra")
async def test_search_by_query(
    gismeteo: aiopygismeteo.Gismeteo, search_query: str
) -> None:
    r = await gismeteo.search.by_query(search_query)
    assert isinstance(r, aiopygismeteo.models.search_by_query.Model)


@pytest.mark.xfail(raises=ClientResponseError)
@pytest.mark.usefixtures("_pydantic_ignore_extra")
async def test_search_by_coordinates(
    gismeteo: aiopygismeteo.Gismeteo, coordinates: tuple[float, float]
) -> None:
    r = await gismeteo.search.by_coordinates(*coordinates, limit=36)
    assert isinstance(r, aiopygismeteo.models.search_by_coordinates.Model)


@pytest.mark.xfail(raises=ClientResponseError)
@pytest.mark.usefixtures("_pydantic_ignore_extra")
async def test_search_by_ip(
    gismeteo: aiopygismeteo.Gismeteo, ipv4_address: IPv4Address
) -> None:
    r = await gismeteo.search.by_ip(ipv4_address)
    assert isinstance(r, aiopygismeteo.models.search_by_ip.Model)
