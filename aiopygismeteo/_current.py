from __future__ import annotations

from pygismeteo_base import models
from pygismeteo_base.current import CurrentBase
from pygismeteo_base.types import Params

from ._http import AiohttpClient


class Current(CurrentBase[AiohttpClient]):
    """Текущая погода."""

    __slots__ = ()

    async def by_coordinates(
        self, latitude: float, longitude: float
    ) -> models.current.Model:
        """По координатам.

        Args:
            latitude (-90 ≤ float ≤ 90):
                Широта.
            longitude (-180 ≤ float ≤ 180):
                Долгота.
        """
        url, params = self._get_params_by_coordinates(latitude, longitude)
        return await self._get_result(url, params=params)

    async def by_id(self, id: int) -> models.current.Model:  # noqa: A002
        """По ID географического объекта.

        Args:
            id (int ≥ 1):
                ID географического объекта. Получить можно через поиск.
        """
        url, params = self._get_params_by_id(id)
        return await self._get_result(url, params=params)

    async def _get_result(
        self, url: str, *, params: Params = None
    ) -> models.current.Model:
        response = await self._session.get_response(url, params=params)
        return models.current.Model.parse_obj(response)
