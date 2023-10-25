from __future__ import annotations

from ipaddress import IPv4Address
from typing import List, Union

from pygismeteo_base import models
from pygismeteo_base.search import SearchBase
from pygismeteo_base.types import Params, SearchLimit
from typing_extensions import Any, Literal, overload

from ._http import AiohttpClient


class Search(SearchBase[AiohttpClient]):
    """Поиск."""

    __slots__ = ()

    @overload
    async def by_coordinates(
        self,
        latitude: float,
        longitude: float,
        limit: SearchLimit,
        *,
        as_list: Literal[True] = ...,
    ) -> List[models.search_by_coordinates.ModelItem]:
        ...

    @overload
    async def by_coordinates(
        self,
        latitude: float,
        longitude: float,
        limit: SearchLimit,
        *,
        as_list: Literal[False],
    ) -> models.search_by_coordinates.Model:
        ...

    @overload
    async def by_coordinates(
        self,
        latitude: float,
        longitude: float,
        limit: SearchLimit,
        *,
        as_list: bool,
    ) -> Union[
        List[models.search_by_coordinates.ModelItem],
        models.search_by_coordinates.Model,
    ]:
        ...

    async def by_coordinates(
        self,
        latitude: float,
        longitude: float,
        limit: SearchLimit,
        *,
        as_list: bool = True,
    ) -> Union[
        List[models.search_by_coordinates.ModelItem],
        models.search_by_coordinates.Model,
    ]:
        """По координатам.

        Args:
            latitude (-90 ≤ float ≤ 90):
                Широта.
            longitude (-180 ≤ float ≤ 180):
                Долгота.
            limit (1 ≤ int ≤ 36):
                Ограничение количества результатов.
            as_list (bool):
                Вернуть Model.__root__ (list[ModelItem]) вместо Model.
                По умолчанию True.
        """
        params = self._get_params_by_coordinates(
            latitude=latitude, longitude=longitude, limit=limit
        )
        response = await self._get_response(params)
        model = models.search_by_coordinates.Model.parse_obj(response)
        return model.__root__ if as_list else model

    async def by_ip(
        self, ip: Union[IPv4Address, str]
    ) -> models.search_by_ip.Model:
        """По IPv4-адресу.

        Args:
            ip (ipaddress.IPv4Address | str):
                IPv4-адрес.
        """
        params = self._get_params_by_ip(ip)
        response = await self._get_response(params)
        return models.search_by_ip.Model.parse_obj(response)

    @overload
    async def by_query(
        self, query: str, *, as_list: Literal[True] = ...
    ) -> List[models.search_by_query.ModelItem]:
        ...

    @overload
    async def by_query(
        self, query: str, *, as_list: Literal[False]
    ) -> models.search_by_query.Model:
        ...

    @overload
    async def by_query(
        self, query: str, *, as_list: bool
    ) -> Union[
        List[models.search_by_query.ModelItem], models.search_by_query.Model
    ]:
        ...

    async def by_query(
        self, query: str, *, as_list: bool = True
    ) -> Union[
        List[models.search_by_query.ModelItem], models.search_by_query.Model
    ]:
        """По строке.

        Args:
            query (str):
                Город, район, область, страна или аэропорт.
            as_list (bool):
                Вернуть Model.__root__ (list[ModelItem]) вместо Model.
                По умолчанию True.
        """
        params = self._get_params_by_query(query)
        response = await self._get_response(params)
        items = response.get("items", [])
        model = models.search_by_query.Model.parse_obj(items)
        return model.__root__ if as_list else model

    async def _get_response(self, params: Params) -> Any:
        return await self._session.get_response(self._endpoint, params=params)
