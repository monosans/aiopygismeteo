# -*- coding: utf-8 -*-
from typing import Dict, Optional

from lxml.html import fromstring

from aiopygismeteo._dates import xpaths
from aiopygismeteo._dates.abc import ABCDate
from aiopygismeteo._utils import normalize_strs, strip_strs


class TwoWeeksBase(ABCDate):
    def __init__(self, html: bytes) -> None:
        self._tree = fromstring(html)
        self._TIME = strip_strs(
            self._tree.xpath(
                xpaths.get_ancestor("forecast")
                + '//span[contains(@class,"w_date__date")]/text()'
            )
        )

    @property
    def status(self) -> Dict[str, str]:
        """Ясно, пасмурно, сильный дождь и т. д."""
        return self._build_result(*xpaths.STATUS)

    @property
    def max_temperature(self) -> Dict[str, str]:
        """Макс. температура, °C."""
        return self._build_result(*xpaths.MAX_TEMPERATURE)

    @property
    def min_temperature(self) -> Dict[str, str]:
        """Мин. температура, °C."""
        return self._build_result(*xpaths.MIN_TEMPERATURE)

    @property
    def gusts(self) -> Dict[str, str]:
        """Порывы, м/с."""
        return self._build_result(*xpaths.WIND_OR_GUST_SPEED)

    @property
    def precipitation(self) -> Dict[str, str]:
        """Сумма осадков, мм."""
        return self._build_result(
            *xpaths.PRECIPITATION,
            check_absence='//div[@class="w_prec__without"]',
            default_value="0",
        )

    @property
    def temperature(self) -> Dict[str, str]:
        """Средняя температура, °C."""
        return self._build_result(*xpaths.AVERAGE_TEMP)

    @property
    def wind_speed(self) -> Dict[str, str]:
        """Скорость ветра, м/с."""
        return self._build_result(*xpaths.WIND_SPEED)

    @property
    def wind_direction(self) -> Dict[str, str]:
        """Направление ветра."""
        return self._build_result(*xpaths.WIND_DIRECTION)

    @property
    def max_pressure(self) -> Dict[str, str]:
        """Макс. давление, мм рт. ст."""
        return self._build_result(*xpaths.MAX_PRESSURE)

    @property
    def min_pressure(self) -> Dict[str, str]:
        """Мин. давление, мм рт. ст."""
        return self._build_result(*xpaths.MIN_PRESSURE)

    @property
    def humidity(self) -> Dict[str, str]:
        """Влажность, %."""
        return self._build_result(*xpaths.HUMIDITY)

    @property
    def gm_activity(self) -> Dict[str, str]:
        """Геомагнитная активность, Кп-индекс."""
        return self._build_result(*xpaths.GEOMAGNETIC_ACTIVITY)

    def _build_result(
        self,
        parent_container: str,
        xpath: str,
        *,
        check_absence: Optional[str] = None,
        default_value: str = "Неизвестно",
    ) -> Dict[str, str]:
        elements = (
            normalize_strs(
                self._tree.xpath(f"{parent_container}{xpath}"), default_value
            )
            if (
                self._tree.xpath(parent_container)
                and (not check_absence or not self._tree.xpath(check_absence))
            )
            else (default_value,) * len(self._TIME)
        )
        return dict(zip(self._TIME, elements))


class TwoWeeks(TwoWeeksBase):
    """Возвращается методом two_weeks() класса Gismeteo."""
