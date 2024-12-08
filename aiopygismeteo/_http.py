from __future__ import annotations

from aiohttp import ClientSession
from pygismeteo_base import types
from pygismeteo_base.http import BaseHttpClient


class AiohttpClient(BaseHttpClient[ClientSession]):
    __slots__ = ()

    async def get_response(
        self, endpoint: str, /, *, params: types.Params
    ) -> str:
        params, headers = self._get_params_and_headers(params)
        if self.session is None:
            self.session = ClientSession()
        async with self.session.get(
            f"{self.base_url}/{endpoint}/",
            params=params,
            headers=headers,
            raise_for_status=True,
        ) as response:
            await response.read()
        return await response.text()
