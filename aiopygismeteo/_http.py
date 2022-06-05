from typing import Any, Optional

from aiohttp import ClientSession
from pygismeteo_base.http import BaseHttpClient
from pygismeteo_base.types import Params
from pygismeteo_base.validators import Settings


class AiohttpClient(BaseHttpClient):
    __slots__ = ("session",)

    def __init__(
        self, session: Optional[ClientSession], settings: Settings
    ) -> None:
        super().__init__(settings)
        self.session = session

    async def get_response(
        self, endpoint: str, *, params: Params = None
    ) -> Any:
        r = await self._get_json(endpoint, params=params)
        return r["response"]

    async def _get_json(self, endpoint: str, *, params: Params = None) -> Any:
        if isinstance(self.session, ClientSession) and not self.session.closed:
            return await self._fetch(
                endpoint, params=params, session=self.session
            )
        async with ClientSession() as session:
            return await self._fetch(endpoint, params=params, session=session)

    async def _fetch(
        self, endpoint: str, *, params: Params, session: ClientSession
    ) -> Any:
        params, headers = self._get_params_and_headers(params)
        async with session.get(
            f"https://api.gismeteo.net/v2/{endpoint}/",
            params=params,
            headers=headers,
            raise_for_status=True,
        ) as r:
            return await r.json()
