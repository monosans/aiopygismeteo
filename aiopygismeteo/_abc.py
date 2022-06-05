from abc import abstractmethod
from typing import Generic, List, Type

from pygismeteo_base.periods.abc import PeriodABC, StepNABC
from pygismeteo_base.types import Params, TDays, TStepNModel, TStepNModelItem

from aiopygismeteo._http import AiohttpClient


class Period(PeriodABC):
    __slots__ = ("_session",)

    def __init__(self, session: AiohttpClient) -> None:
        self._session = session


class StepN(Generic[TDays, TStepNModel, TStepNModelItem], StepNABC, Period):
    __slots__ = ()

    async def by_coordinates(
        self, latitude: float, longitude: float, *, days: TDays
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

    async def by_id(self, id: int, *, days: TDays) -> List[TStepNModelItem]:
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
        r = await self._session.get_response(url, params=params)
        model = self._model.parse_obj(r)
        return model.__root__  # type: ignore[return-value]

    @property
    @abstractmethod
    def _model(self) -> Type[TStepNModel]:
        pass
