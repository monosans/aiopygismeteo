from __future__ import annotations

from pygismeteo_base import models
from pygismeteo_base.periods import mixins
from pygismeteo_base.types import Params, Step3Days, Step6or24Days

from ._abc import Period, StepN


class Current(mixins.CurrentMixin, Period):
    __slots__ = ()

    async def by_coordinates(
        self, latitude: float, longitude: float
    ) -> models.current.Model:
        """По координатам.

        Args:
            latitude: Широта (от -90 до 90).
            longitude: Долгота (от -180 до 180).
        """
        url, params = self._get_params_by_coordinates(latitude, longitude)
        return await self._get_result(url, params=params)

    async def by_id(
        self,
        # pylint: disable-next=invalid-name,redefined-builtin
        id: int,
    ) -> models.current.Model:
        """По ID географического объекта.

        Args:
            id: ID географического объекта. Получить можно через поиск.
        """
        url, params = self._get_params_by_id(id)
        return await self._get_result(url, params=params)

    async def _get_result(
        self, url: str, *, params: Params = None
    ) -> models.current.Model:
        response = await self._session.get_response(url, params=params)
        return self._model.parse_obj(response)


# pylint: disable-next=too-many-ancestors
class Step3(
    mixins.Step3Mixin,
    StepN[Step3Days, models.step3.Model, models.step3.ModelItem],
):
    __slots__ = ()


# pylint: disable-next=too-many-ancestors
class Step6(
    mixins.Step6Mixin,
    StepN[Step6or24Days, models.step6.Model, models.step6.ModelItem],
):
    __slots__ = ()


# pylint: disable-next=too-many-ancestors
class Step24(
    mixins.Step24Mixin,
    StepN[Step6or24Days, models.step24.Model, models.step24.ModelItem],
):
    __slots__ = ()
