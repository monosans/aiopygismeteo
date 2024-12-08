from __future__ import annotations

from ipaddress import IPv4Address

from pygismeteo_base import models, types
from pygismeteo_base.endpoints.search import SearchBase

from aiopygismeteo._http import AiohttpClient


class Search(SearchBase[AiohttpClient]):
    """Поиск."""

    __slots__ = ()

    async def by_coordinates(
        self,
        latitude: types.Latitude,
        longitude: types.Longitude,
        *,
        limit: types.SearchLimit,
    ) -> models.search_by_coordinates.Model:
        """По координатам.

        Args:
            latitude: Широта.
            longitude: Долгота.
            limit: Ограничение количества результатов.
        """
        url, params = self._get_params_by_coordinates(
            latitude=latitude, longitude=longitude, limit=limit
        )
        return models.search_by_coordinates.Response.model_validate_json(
            await self._get_response(url, params=params)
        ).response

    async def by_ip(self, ip: IPv4Address, /) -> models.search_by_ip.Model:
        """По IPv4-адресу.

        Args:
            ip: IPv4-адрес.
        """
        url, params = self._get_params_by_ip(ip)
        return models.search_by_ip.Response.model_validate_json(
            await self._get_response(url, params=params)
        ).response

    async def by_query(self, query: str, /) -> models.search_by_query.Model:
        """По строке.

        Args:
            query: Город, район, область, страна или аэропорт.
        """
        url, params = self._get_params_by_query(query)
        return models.search_by_query.Response.model_validate_json(
            await self._get_response(url, params=params)
        ).response.items

    async def _get_response(self, url: str, /, *, params: types.Params) -> str:
        return await self._session.get_response(url, params=params)
