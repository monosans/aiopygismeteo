from __future__ import annotations

from pygismeteo_base import models, types
from pygismeteo_base.endpoints.step6 import Step6Base

from aiopygismeteo._http import AiohttpClient


class Step6(Step6Base[AiohttpClient]):
    """Погода с шагом 6 часов."""

    __slots__ = ()

    async def by_coordinates(
        self,
        latitude: types.Latitude,
        longitude: types.Longitude,
        *,
        days: types.Step6Days,
    ) -> models.step6.Model:
        """По координатам.

        Args:
            latitude: Широта.
            longitude: Долгота.
            days: Количество дней.
        """
        url, params = self._get_params_by_coordinates(
            latitude, longitude, days=days
        )
        return await self._get_result(url, params=params)

    async def by_id(
        self, id_: types.LocalityID, /, *, days: types.Step6Days
    ) -> models.step6.Model:
        """По ID географического объекта.

        Args:
            id_: ID географического объекта. Получить можно через поиск.
            days: Количество дней.
        """
        url, params = self._get_params_by_id(id_, days=days)
        return await self._get_result(url, params=params)

    async def _get_result(
        self, url: str, /, *, params: types.Params
    ) -> models.step6.Model:
        return models.step6.Response.model_validate_json(
            await self._session.get_response(url, params=params)
        ).response
