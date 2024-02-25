from __future__ import annotations

from typing import Generic, Tuple, Union

from pygismeteo_base import models, types
from pygismeteo_base.step_n import mixins
from pygismeteo_base.step_n.abc import StepNABC
from typing_extensions import Literal, overload

from ._http import AiohttpClient


class StepN(
    Generic[types.TStepNDays, types.TStepNModel, types.TStepNModelItem],
    StepNABC[AiohttpClient],
):
    __slots__ = ()

    @overload
    async def by_coordinates(
        self,
        latitude: types.Latitude,
        longitude: types.Longitude,
        days: types.TStepNDays,
        *,
        as_list: Literal[True] = ...,
    ) -> Tuple[types.TStepNModelItem, ...]: ...

    @overload
    async def by_coordinates(
        self,
        latitude: types.Latitude,
        longitude: types.Longitude,
        days: types.TStepNDays,
        *,
        as_list: Literal[False],
    ) -> types.TStepNModel: ...

    @overload
    async def by_coordinates(
        self,
        latitude: types.Latitude,
        longitude: types.Longitude,
        days: types.TStepNDays,
        *,
        as_list: bool,
    ) -> Union[Tuple[types.TStepNModelItem, ...], types.TStepNModel]: ...

    async def by_coordinates(
        self,
        latitude: types.Latitude,
        longitude: types.Longitude,
        days: types.TStepNDays,
        *,
        as_list: bool = True,
    ) -> Union[Tuple[types.TStepNModelItem, ...], types.TStepNModel]:
        """По координатам.

        Args:
            latitude (-90 ≤ int | float ≤ 90):
                Широта.
            longitude (-180 ≤ int | float ≤ 180):
                Долгота.
            days (
                step3:  1 ≤ int ≤ 10,
                step6:  3 ≤ int ≤ 10,
                step24: 3 ≤ int ≤ 10,
            ):
                Количество дней.
            as_list (bool):
                Вернуть Model.root (tuple[ModelItem, ...]) вместо Model.
                По умолчанию True.
        """
        url, params = self._get_params_by_coordinates(
            latitude, longitude, days=days
        )
        return await self._get_result(url, params=params, as_list=as_list)

    @overload
    async def by_id(
        self,
        id: types.LocalityID,  # noqa: A002
        days: types.TStepNDays,
        *,
        as_list: Literal[True] = ...,
    ) -> Tuple[types.TStepNModelItem, ...]: ...

    @overload
    async def by_id(
        self,
        id: types.LocalityID,  # noqa: A002
        days: types.TStepNDays,
        *,
        as_list: Literal[False],
    ) -> types.TStepNModel: ...

    @overload
    async def by_id(
        self,
        id: types.LocalityID,  # noqa: A002
        days: types.TStepNDays,
        *,
        as_list: bool,
    ) -> Union[Tuple[types.TStepNModelItem, ...], types.TStepNModel]: ...

    async def by_id(
        self,
        id: types.LocalityID,  # noqa: A002
        days: types.TStepNDays,
        *,
        as_list: bool = True,
    ) -> Union[Tuple[types.TStepNModelItem, ...], types.TStepNModel]:
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
                Вернуть Model.root (tuple[ModelItem, ...]) вместо Model.
                По умолчанию True.
        """
        url, params = self._get_params_by_id(id, days=days)
        return await self._get_result(url, params=params, as_list=as_list)

    @overload
    async def _get_result(
        self, url: str, *, params: types.Params, as_list: Literal[True]
    ) -> Tuple[types.TStepNModelItem, ...]: ...

    @overload
    async def _get_result(
        self, url: str, *, params: types.Params, as_list: Literal[False]
    ) -> types.TStepNModel: ...

    @overload
    async def _get_result(
        self, url: str, *, params: types.Params, as_list: bool
    ) -> Union[Tuple[types.TStepNModelItem, ...], types.TStepNModel]: ...

    async def _get_result(
        self, url: str, *, params: types.Params, as_list: bool
    ) -> Union[Tuple[types.TStepNModelItem, ...], types.TStepNModel]:
        response = await self._session.get_response(url, params=params)
        model = self._model().model_validate_json(response)
        return (
            model.response.root  # type: ignore[return-value]
            if as_list
            else model.response
        )


class Step3(
    mixins.Step3Mixin,
    StepN[types.Step3Days, models.step3.Model, models.step3.ModelItem],
):
    """Погода с шагом 3 часа."""

    __slots__ = ()


class Step6(
    mixins.Step6Mixin,
    StepN[types.Step6Days, models.step6.Model, models.step6.ModelItem],
):
    """Погода с шагом 6 часов."""

    __slots__ = ()


class Step24(
    mixins.Step24Mixin,
    StepN[types.Step24Days, models.step24.Model, models.step24.ModelItem],
):
    """Погода с шагом 24 часа."""

    __slots__ = ()
