from __future__ import annotations

from typing import Generic, List, Union

from pygismeteo_base import models
from pygismeteo_base.step_n import mixins
from pygismeteo_base.step_n.abc import StepNABC
from pygismeteo_base.types import (
    Params,
    Step3Days,
    Step6Days,
    Step24Days,
    TDays,
    TStepNModel,
    TStepNModelItem,
)
from typing_extensions import Literal, overload

from ._http import AiohttpClient


class StepN(
    Generic[TDays, TStepNModel, TStepNModelItem], StepNABC[AiohttpClient]
):
    __slots__ = ()

    @overload
    async def by_coordinates(
        self,
        latitude: float,
        longitude: float,
        days: TDays,
        *,
        as_list: Literal[True] = ...,
    ) -> List[TStepNModelItem]:
        ...

    @overload
    async def by_coordinates(
        self,
        latitude: float,
        longitude: float,
        days: TDays,
        *,
        as_list: Literal[False],
    ) -> TStepNModel:
        ...

    @overload
    async def by_coordinates(
        self, latitude: float, longitude: float, days: TDays, *, as_list: bool
    ) -> Union[List[TStepNModelItem], TStepNModel]:
        ...

    async def by_coordinates(
        self,
        latitude: float,
        longitude: float,
        days: TDays,
        *,
        as_list: bool = True,
    ) -> Union[List[TStepNModelItem], TStepNModel]:
        """По координатам.

        Args:
            latitude (-90 ≤ float ≤ 90):
                Широта.
            longitude (-180 ≤ float ≤ 180):
                Долгота.
            days (
                step3:  1 ≤ int ≤ 10,
                step6:  3 ≤ int ≤ 10,
                step24: 3 ≤ int ≤ 10,
            ):
                Количество дней.
            as_list (bool):
                Вернуть Model.__root__ (list[ModelItem]) вместо Model.
                По умолчанию True.
        """
        url, params = self._get_params_by_coordinates(
            latitude, longitude, days=days
        )
        return await self._get_result(url, params=params, as_list=as_list)

    @overload
    async def by_id(
        self,
        id: int,  # noqa: A002
        days: TDays,
        *,
        as_list: Literal[True] = ...,
    ) -> List[TStepNModelItem]:
        ...

    @overload
    async def by_id(
        self, id: int, days: TDays, *, as_list: Literal[False]  # noqa: A002
    ) -> TStepNModel:
        ...

    @overload
    async def by_id(
        self, id: int, days: TDays, *, as_list: bool  # noqa: A002
    ) -> Union[List[TStepNModelItem], TStepNModel]:
        ...

    async def by_id(
        self, id: int, days: TDays, *, as_list: bool = True  # noqa: A002
    ) -> Union[List[TStepNModelItem], TStepNModel]:
        """По ID географического объекта.

        Args:
            id (int ≥ 1):
                ID географического объекта. Получить можно через поиск.
            days (
                step3:  1 ≤ int ≤ 10,
                step6:  3 ≤ int ≤ 10,
                step24: 3 ≤ int ≤ 10,
            ):
                Количество дней.
            as_list (bool):
                Вернуть Model.__root__ (list[ModelItem]) вместо Model.
                По умолчанию True.
        """
        url, params = self._get_params_by_id(id, days=days)
        return await self._get_result(url, params=params, as_list=as_list)

    @overload
    async def _get_result(
        self, url: str, *, params: Params, as_list: Literal[True]
    ) -> List[TStepNModelItem]:
        ...

    @overload
    async def _get_result(
        self, url: str, *, params: Params, as_list: Literal[False]
    ) -> TStepNModel:
        ...

    @overload
    async def _get_result(
        self, url: str, *, params: Params, as_list: bool
    ) -> Union[List[TStepNModelItem], TStepNModel]:
        ...

    async def _get_result(
        self, url: str, *, params: Params, as_list: bool
    ) -> Union[List[TStepNModelItem], TStepNModel]:
        response = await self._session.get_response(url, params=params)
        model = self._model.parse_obj(response)
        return (
            model.__root__ if as_list else model  # type: ignore[return-value]
        )


class Step3(
    mixins.Step3Mixin,
    StepN[Step3Days, models.step3.Model, models.step3.ModelItem],
):
    """Погода с шагом 3 часа."""

    __slots__ = ()


class Step6(
    mixins.Step6Mixin,
    StepN[Step6Days, models.step6.Model, models.step6.ModelItem],
):
    """Погода с шагом 6 часов."""

    __slots__ = ()


class Step24(
    mixins.Step24Mixin,
    StepN[Step24Days, models.step24.Model, models.step24.ModelItem],
):
    """Погода с шагом 24 часа."""

    __slots__ = ()
