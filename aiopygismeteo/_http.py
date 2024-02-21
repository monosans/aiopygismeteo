from __future__ import annotations

from typing import Mapping, Optional

from aiohttp import ClientResponse, ClientSession
from pygismeteo_base import types
from pygismeteo_base.http import BaseHttpClient


class AiohttpClient(BaseHttpClient[ClientSession]):
    __slots__ = ()

    async def get_response(
        self, endpoint: str, *, params: types.Params = None
    ) -> str:
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
        return await response.text()

    async def _fetch(  # noqa: PLR6301
        self,
        endpoint: str,
        *,
        params: Optional[Mapping[str, str]],
        headers: Mapping[str, str],
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
