from __future__ import annotations

from typing import AsyncIterator, Tuple

import pydantic.v1 as pydantic
import pytest
from aiohttp import ClientSession

from aiopygismeteo import Gismeteo


@pytest.fixture()
async def http_session() -> AsyncIterator[ClientSession]:
    async with ClientSession() as s:
        yield s


@pytest.fixture()
def gismeteo_token() -> str:
    return "56b30cb255.3443075"


@pytest.fixture()
def location_id() -> int:
    # Moscow
    return 4368


@pytest.fixture()
def coordinates() -> Tuple[float, float]:
    # Moscow
    return 55.7522200, 37.6155600


@pytest.fixture()
def search_query() -> str:
    return "mosc"


@pytest.fixture()
def ipv4_address() -> str:
    return "8.8.8.8"


@pytest.fixture()
def gismeteo(gismeteo_token: str, http_session: ClientSession) -> Gismeteo:
    return Gismeteo(token=gismeteo_token, session=http_session)


@pytest.fixture()
def _pydantic_ignore_extra(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(pydantic.BaseConfig, "extra", pydantic.Extra.ignore)


@pytest.fixture(autouse=True)
def _pydantic_strict(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(pydantic.BaseConfig, "extra", pydantic.Extra.forbid)
    monkeypatch.setattr(pydantic.BaseConfig, "validate_all", True)
    monkeypatch.setattr(pydantic.BaseConfig, "validate_assignment", True)
