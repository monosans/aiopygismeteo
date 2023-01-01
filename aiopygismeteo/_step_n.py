from __future__ import annotations

from typing import Generic, List

from pygismeteo_base import models
from pygismeteo_base.step_n import mixins
from pygismeteo_base.step_n.abc import StepNABC
from pygismeteo_base.types import (
    Params,
    Step3Days,
    Step6or24Days,
    TDays,
    TStepNModelItem,
)

from ._http import AiohttpClient


# pylint: disable-next=abstract-method
class StepN(Generic[TDays, TStepNModelItem], StepNABC[AiohttpClient]):
    __slots__ = ()

    async def by_coordinates(
        self, latitude: float, longitude: float, days: TDays
    ) -> List[TStepNModelItem]:
        """По координатам.

        Args:
            latitude: Широта (от -90 до 90).
            longitude: Долгота (от -180 до 180).
            days: Количество дней
                (с шагом 3 часа - от 1 до 10, с шагом 6 или 24 - от 3 до 10).
        """
        url, params = self._get_params_by_coordinates(
            latitude, longitude, days=days
        )
        return await self._get_result(url, params=params)

    async def by_id(
        self,
        # pylint: disable-next=invalid-name,redefined-builtin
        id: int,
        days: TDays,
    ) -> List[TStepNModelItem]:
        """По ID географического объекта.

        Args:
            id: ID географического объекта. Получить можно через поиск.
            days: Количество дней
                (с шагом 3 часа - от 1 до 10, с шагом 6 или 24 - от 3 до 10).
        """
        url, params = self._get_params_by_id(id, days=days)
        return await self._get_result(url, params=params)

    async def _get_result(
        self, url: str, *, params: Params
    ) -> List[TStepNModelItem]:
        response = await self._session.get_response(url, params=params)
        model = self._model.parse_obj(response)
        return model.__root__  # type: ignore[return-value]


class Step3(mixins.Step3Mixin, StepN[Step3Days, models.step3.ModelItem]):
    """Погода с шагом 3 часа."""

    __slots__ = ()


class Step6(mixins.Step6Mixin, StepN[Step6or24Days, models.step6.ModelItem]):
    """Погода с шагом 6 часов."""

    __slots__ = ()


class Step24(
    mixins.Step24Mixin, StepN[Step6or24Days, models.step24.ModelItem]
):
    """Погода с шагом 24 часа."""

    __slots__ = ()
