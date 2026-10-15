from __future__ import annotations

from ipaddress import IPv4Address

from pygismeteo_base import models, responses, types
from pygismeteo_base.endpoints.search import SearchBase

from aiopygismeteo._http import AiohttpClient


class Search(SearchBase[AiohttpClient]):
    """Поиск географических объектов."""

    __slots__ = ()

    async def by_coordinates(
        self,
        latitude: types.Latitude,
        longitude: types.Longitude,
        *,
        limit: types.SearchLimit,
    ) -> models.search_by_coordinates.Model:
        """Найти ближайшие к точке объекты.

        Args:
            latitude: Широта.
            longitude: Долгота.
            limit: Сколько объектов вернуть, от 1 до 36.

        Examples:
            ```python
            search_results = await gismeteo.search.by_coordinates(
                55.75222, 37.61556, limit=36
            )
            print(search_results)
            ```
        """
        url, params = self._get_params_by_coordinates(
            latitude=latitude, longitude=longitude, limit=limit
        )
        return responses.search_by_coordinates.validate_json(
            await self._session.get_response(url, params=params)
        )["response"]

    async def by_ip(self, ip: IPv4Address, /) -> models.search_by_ip.Model:
        """Определить объект по IPv4-адресу.

        Args:
            ip: IPv4-адрес.

        Examples:
            ```python
            from ipaddress import IPv4Address

            search_results = await gismeteo.search.by_ip(IPv4Address("8.8.8.8"))
            print(search_results)
            ```
        """
        url, params = self._get_params_by_ip(ip)
        return responses.search_by_ip.validate_json(
            await self._session.get_response(url, params=params)
        )["response"]

    async def by_query(self, query: str, /) -> models.search_by_query.Model:
        """Найти объекты по названию.

        Args:
            query: Город, район, область, страна или аэропорт.

        Returns:
            Найденные объекты или пустой кортеж.

        Examples:
            ```python
            search_results = await gismeteo.search.by_query("Москва")
            print(search_results)
            ```
        """
        url, params = self._get_params_by_query(query)
        return responses.search_by_query.validate_json(
            await self._session.get_response(url, params=params)
        )["response"]["items"]
