from typing import Any, List

from pygismeteo_base import models, search
from pygismeteo_base.types import Params, SearchLimit

from aiopygismeteo._http import AiohttpClient


class Search(search.Search):
    __slots__ = ("_session",)

    def __init__(self, session: AiohttpClient) -> None:
        self._session = session

    async def by_coordinates(
        self, latitude: float, longitude: float, *, limit: SearchLimit
    ) -> List[models.search_by_coordinates.ModelItem]:
        """Поиск по координатам.

        Args:
            latitude: Широта (от -90 до 90).
            longitude: Долгота (от -180 до 180).
            limit: Ограничение количества (от 1 до 36).
        """
        params = self._get_params_by_coordinates(
            latitude=latitude, longitude=longitude, limit=limit
        )
        r = await self._get_response(params)
        model = models.search_by_coordinates.Model.parse_obj(r)
        return model.__root__

    async def by_ip(self, ip: str) -> models.search_by_ip.Model:
        """Поиск по IP-адресу.

        Args:
            ip: IP-адрес.
        """
        params = self._get_params_by_ip(ip)
        r = await self._get_response(params)
        return models.search_by_ip.Model.parse_obj(r)

    async def by_query(
        self, query: str
    ) -> List[models.search_by_query.ModelItem]:
        """Поиск по строке.

        Args:
            query: Город, район, область, страна или аэропорт.
        """
        params = self._get_params_by_query(query)
        r = await self._get_response(params)
        model = models.search_by_query.Model.parse_obj(r["items"])
        return model.__root__

    async def _get_response(self, params: Params) -> Any:
        return await self._session.get_response(self._endpoint, params=params)
