from __future__ import annotations

from pygismeteo_base import models, types
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
        """
        url, params = self._get_params_by_coordinates(latitude, longitude)
        return await self._get_result(url, params=params)

    async def by_id(self, id_: types.LocalityID, /) -> models.current.Model:
        """По ID географического объекта.

        Args:
            id_: ID географического объекта. Получить можно через поиск.
        """
        url, params = self._get_params_by_id(id_)
        return await self._get_result(url, params=params)

    async def _get_result(
        self, url: str, /, *, params: types.Params
    ) -> models.current.Model:
        response = await self._session.get_response(url, params=params)
        model = models.current.Response.model_validate_json(response)
        return model.response
