# -*- coding: utf-8 -*-
from typing import Any, Dict, Optional, Union

import pygismeteo_base
from aiohttp import ClientSession

from aiopygismeteo._exceptions import LocalityNotFound


class Gismeteo:
    def __init__(
        self,
        *,
        lang: pygismeteo_base.types.LANG = "ru",
        token: str = pygismeteo_base.constants.DEFAULT_TOKEN,
        session: Optional[ClientSession] = None,
    ) -> None:
        self.lang = lang.strip()
        self.token = token.strip()
        self._session = session

    async def current(self, id: int) -> pygismeteo_base.models.current.Model:
        return pygismeteo_base.models.current.Model.parse_obj(
            await self._get_response(f"weather/current/{id}")
        )

    async def step3(
        self, id: int, days: pygismeteo_base.types.STEP3_DAYS
    ) -> pygismeteo_base.models.step3or6.Model:
        return pygismeteo_base.models.step3or6.Model.parse_obj(
            await self._get_response(f"weather/forecast/{id}", {"days": days})
        )

    async def step6(
        self, id: int, days: pygismeteo_base.types.DAYS
    ) -> pygismeteo_base.models.step3or6.Model:
        return pygismeteo_base.models.step3or6.Model.parse_obj(
            await self._get_response(
                f"weather/forecast/by_day_part/{id}", {"days": days}
            )
        )

    async def step24(
        self, id: int, days: pygismeteo_base.types.DAYS
    ) -> pygismeteo_base.models.step24.Model:
        return pygismeteo_base.models.step24.Model.parse_obj(
            await self._get_response(
                f"weather/forecast/aggregate/{id}", {"days": days}
            )
        )

    async def get_id_by_query(self, query: str) -> int:
        r = await self._get_response("search/cities", {"query": query})
        items = r["items"]
        if not items:
            raise LocalityNotFound("Населённый пункт не найден.")
        return int(items[0]["id"])

    async def _fetch(
        self,
        endpoint: str,
        params: Optional[Dict[str, Union[str, int]]],
        session: ClientSession,
    ) -> Any:
        async with session.get(
            f"https://api.gismeteo.net/v2/{endpoint}",
            params={"lang": self.lang, **(params or {})},
            headers={"X-Gismeteo-Token": self.token},
            raise_for_status=True,
        ) as r:
            return await r.json()

    async def _get_json(
        self,
        endpoint: str,
        params: Optional[Dict[str, Union[str, int]]] = None,
    ) -> Any:
        if (
            isinstance(self._session, ClientSession)
            and not self._session.closed
        ):
            return await self._fetch(endpoint, params, self._session)
        async with ClientSession() as session:
            return await self._fetch(endpoint, params, session)

    async def _get_response(
        self,
        endpoint: str,
        params: Optional[Dict[str, Union[str, int]]] = None,
    ) -> Any:
        return (await self._get_json(endpoint, params))["response"]
