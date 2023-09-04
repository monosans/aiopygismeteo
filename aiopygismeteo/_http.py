from __future__ import annotations

from aiohttp import ClientResponse, ClientSession
from pygismeteo_base.http import BaseHttpClient
from pygismeteo_base.types import Headers, Params
from typing_extensions import Any


class AiohttpClient(BaseHttpClient[ClientSession]):
    __slots__ = ()

    async def get_response(
        self, endpoint: str, *, params: Params = None
    ) -> Any:
        response = await self._get_json(endpoint, params=params)
        return response["response"]

    async def _get_json(self, endpoint: str, *, params: Params = None) -> Any:
        params, headers = self._get_params_and_headers(params)
        if isinstance(self.session, ClientSession) and not self.session.closed:
            response = await self._fetch(
                endpoint, params=params, headers=headers, session=self.session
            )
        else:
            async with ClientSession() as session:
                response = await self._fetch(
                    endpoint, params=params, headers=headers, session=session
                )
        return await response.json()

    async def _fetch(
        self,
        endpoint: str,
        *,
        params: Params,
        headers: Headers,
        session: ClientSession,
    ) -> ClientResponse:
        async with session.get(
            f"https://api.gismeteo.net/v2/{endpoint}/",
            params=params,
            headers=headers,
            raise_for_status=True,
        ) as response:
            await response.read()
        return response
