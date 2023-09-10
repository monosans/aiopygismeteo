from __future__ import annotations

import asyncio
from typing import AsyncIterator, Iterator, Tuple

import pydantic.v1 as pydantic
import pytest
from aiohttp import ClientSession

from aiopygismeteo import Gismeteo


@pytest.fixture(scope="session")
def event_loop() -> Iterator[asyncio.AbstractEventLoop]:
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
async def http_session() -> AsyncIterator[ClientSession]:
    async with ClientSession() as s:
        yield s


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
def gismeteo(http_session: ClientSession) -> Gismeteo:
    return Gismeteo(session=http_session)


@pytest.fixture()
def _pydantic_ignore_extra(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(pydantic.BaseConfig, "extra", pydantic.Extra.ignore)


@pytest.fixture(autouse=True)
def _pydantic_strict(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(pydantic.BaseConfig, "extra", pydantic.Extra.forbid)
    monkeypatch.setattr(pydantic.BaseConfig, "validate_all", True)
    monkeypatch.setattr(pydantic.BaseConfig, "validate_assignment", True)
