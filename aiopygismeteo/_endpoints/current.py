from __future__ import annotations

from pygismeteo_base import models, responses, types
from pygismeteo_base.endpoints.current import CurrentBase

from aiopygismeteo._http import AiohttpClient


class Current(CurrentBase[AiohttpClient]):
    """Текущая погода."""

    __slots__ = ()

    async def by_coordinates(
        self, latitude: types.Latitude, longitude: types.Longitude
    ) -> models.current.Model:
        """По координатам.

        Args:
            latitude: Широта.
            longitude: Долгота.

        Examples:
            ```python
            current = await gismeteo.current.by_coordinates(55.75222, 37.61556)
            print(current)
            ```
        """
        url, params = self._get_params_by_coordinates(latitude, longitude)
        return await self._get_result(url, params=params)

    async def by_id(self, id_: types.LocalityID, /) -> models.current.Model:
        """По ID географического объекта.

        Args:
            id_: ID географического объекта. Получить можно через поиск.

        Examples:
            ```python
            search_results = await gismeteo.search.by_query("Москва")
            city_id = search_results[0].id
            current = await gismeteo.current.by_id(city_id)
            print(current)
            ```
        """
        url, params = self._get_params_by_id(id_)
        return await self._get_result(url, params=params)

    async def _get_result(
        self, url: str, /, *, params: types.Params
    ) -> models.current.Model:
        return responses.current.validate_json(
            await self._session.get_response(url, params=params)
        )["response"]
