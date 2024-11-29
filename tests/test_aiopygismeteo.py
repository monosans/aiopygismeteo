from __future__ import annotations

from ipaddress import IPv4Address
from typing import Union

import pytest
from aiohttp import ClientResponseError

from aiopygismeteo import Gismeteo, models


@pytest.mark.xfail(raises=ClientResponseError)
async def test_current_by_id(gismeteo_token: str, location_id: int) -> None:
    gismeteo = Gismeteo(lang="en", token=gismeteo_token)
    r = await gismeteo.current.by_id(location_id)
    assert isinstance(r, models.current.Model)


@pytest.mark.xfail(raises=ClientResponseError)
async def test_current_by_coordinates(
    gismeteo: Gismeteo, coordinates: tuple[float, float]
) -> None:
    r = await gismeteo.current.by_coordinates(*coordinates)
    assert isinstance(r, models.current.Model)


@pytest.mark.xfail(raises=ClientResponseError)
@pytest.mark.parametrize("as_list", [True, False])
async def test_step3_by_id(
    gismeteo: Gismeteo, location_id: int, as_list: bool
) -> None:
    r = await gismeteo.step3.by_id(location_id, days=10, as_list=as_list)
    if as_list:
        assert isinstance(r, tuple)
    else:
        assert isinstance(r, models.step3.Model)
        assert isinstance(r.root, tuple)


@pytest.mark.xfail(raises=ClientResponseError)
@pytest.mark.parametrize("as_list", [True, False])
async def test_step3_by_coordinates(
    gismeteo: Gismeteo, coordinates: tuple[float, float], as_list: bool
) -> None:
    r = await gismeteo.step3.by_coordinates(
        *coordinates, days=10, as_list=as_list
    )
    if as_list:
        assert isinstance(r, tuple)
    else:
        assert isinstance(r, models.step3.Model)
        assert isinstance(r.root, tuple)


@pytest.mark.xfail(raises=ClientResponseError)
@pytest.mark.parametrize("as_list", [True, False])
async def test_step6_by_id(
    gismeteo: Gismeteo, location_id: int, as_list: bool
) -> None:
    r = await gismeteo.step6.by_id(location_id, days=10, as_list=as_list)
    if as_list:
        assert isinstance(r, tuple)
    else:
        assert isinstance(r, models.step6.Model)
        assert isinstance(r.root, tuple)


@pytest.mark.xfail(raises=ClientResponseError)
@pytest.mark.parametrize("as_list", [True, False])
async def test_step6_by_coordinates(
    gismeteo: Gismeteo, coordinates: tuple[float, float], as_list: bool
) -> None:
    r = await gismeteo.step6.by_coordinates(
        *coordinates, days=10, as_list=as_list
    )
    if as_list:
        assert isinstance(r, tuple)
    else:
        assert isinstance(r, models.step6.Model)
        assert isinstance(r.root, tuple)


@pytest.mark.xfail(raises=ClientResponseError)
@pytest.mark.parametrize("as_list", [True, False])
async def test_step24_by_id(
    gismeteo: Gismeteo, location_id: int, as_list: bool
) -> None:
    r = await gismeteo.step24.by_id(location_id, days=10, as_list=as_list)
    if as_list:
        assert isinstance(r, tuple)
    else:
        assert isinstance(r, models.step24.Model)
        assert isinstance(r.root, tuple)


@pytest.mark.xfail(raises=ClientResponseError)
@pytest.mark.parametrize("as_list", [True, False])
async def test_step24_by_coordinates(
    gismeteo: Gismeteo, coordinates: tuple[float, float], as_list: bool
) -> None:
    r = await gismeteo.step24.by_coordinates(
        *coordinates, days=10, as_list=as_list
    )
    if as_list:
        assert isinstance(r, tuple)
    else:
        assert isinstance(r, models.step24.Model)
        assert isinstance(r.root, tuple)


@pytest.mark.xfail(raises=ClientResponseError)
@pytest.mark.usefixtures("_pydantic_ignore_extra")
@pytest.mark.parametrize("as_list", [True, False])
async def test_search_by_query(
    gismeteo: Gismeteo, search_query: str, as_list: bool
) -> None:
    r = await gismeteo.search.by_query(search_query, as_list=as_list)
    if as_list:
        assert isinstance(r, tuple)
    else:
        assert isinstance(r, models.search_by_query.Model)
        assert isinstance(r.root, tuple)


@pytest.mark.xfail(raises=ClientResponseError)
@pytest.mark.usefixtures("_pydantic_ignore_extra")
@pytest.mark.parametrize("as_list", [True, False])
async def test_search_by_coordinates(
    gismeteo: Gismeteo, coordinates: tuple[float, float], as_list: bool
) -> None:
    r = await gismeteo.search.by_coordinates(
        *coordinates, limit=36, as_list=as_list
    )
    if as_list:
        assert isinstance(r, tuple)
    else:
        assert isinstance(r, models.search_by_coordinates.Model)
        assert isinstance(r.root, tuple)


@pytest.mark.xfail(raises=ClientResponseError)
@pytest.mark.usefixtures("_pydantic_ignore_extra")
@pytest.mark.parametrize("type_", [str, IPv4Address])
async def test_search_by_ip(
    gismeteo: Gismeteo, ipv4_address: str, type_: type[Union[str, IPv4Address]]
) -> None:
    r = await gismeteo.search.by_ip(type_(ipv4_address))
    assert isinstance(r, models.search_by_ip.Model)


@pytest.mark.parametrize("property_", ["token", "lang", "session"])
def test_immutable_properties(gismeteo: Gismeteo, property_: str) -> None:
    with pytest.raises(
        AttributeError,
        match=f"property '{property_}' of 'Gismeteo' object has no setter",
    ):
        setattr(gismeteo, property_, None)
