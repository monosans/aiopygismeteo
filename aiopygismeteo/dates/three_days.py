# -*- coding: utf-8 -*-
from typing import Dict, Optional, Tuple

from lxml.html import fromstring

from aiopygismeteo.dates import xpaths
from aiopygismeteo.utils import normalize_strs


class Night:
    _start = 0

    def __init__(self, tree, time: Tuple[str, ...]) -> None:
        self._tree = tree
        self._TIME = time

    @property
    def status(self) -> Dict[str, str]:
        """Ясно, пасмурно, сильный дождь и т. д."""
        return self._build_result(*xpaths.STATUS)

    @property
    def temperature(self) -> Dict[str, str]:
        """Средняя температура, °C."""
        return self._build_result(*xpaths.TEMPERATURE)

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
    def wind_speed(self) -> Dict[str, str]:
        """Скорость ветра, м/с."""
        return self._build_result(*xpaths.WIND_SPEED)

    @property
    def wind_direction(self) -> Dict[str, str]:
        """Направление ветра."""
        return self._build_result(*xpaths.WIND_DIRECTION)

    @property
    def falling_snow(self) -> Dict[str, str]:
        """Выпадающий снег, см."""
        return self._build_result(*xpaths.FALLING_SNOW)

    @property
    def snow_depth(self) -> Dict[str, str]:
        """Высота снежного покрова, см."""
        return self._build_result(*xpaths.SNOW_DEPTH)

    @property
    def pressure(self) -> Dict[str, str]:
        """Давление, мм рт. ст."""
        return self._build_result(*xpaths.PRESSURE)

    @property
    def humidity(self) -> Dict[str, str]:
        """Влажность, %."""
        return self._build_result(*xpaths.HUMIDITY)

    @property
    def ultraviolet_index(self) -> Dict[str, str]:
        """Ультрафиолетовый индекс, баллы."""
        return self._build_result(*xpaths.ULTRAVIOLET_INDEX)

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
            )[self._start :: 4]
            if (
                self._tree.xpath(parent_container)
                and (not check_absence or not self._tree.xpath(check_absence))
            )
            else (default_value,) * 3
        )
        return dict(zip(self._TIME, elements))


class Morning(Night):
    _start = 1


class Afternoon(Night):
    _start = 2


class Evening(Night):
    _start = 3


class ThreeDays:
    def __init__(self, html: bytes) -> None:
        tree = fromstring(html)
        time = tuple(
            day.split()[1].strip()
            for day in tree.xpath(
                f"{xpaths.get_ancestor('forecast')}//div[@data-index]//text()"
            )
        )
        self._ARGS = (tree, time)

    @property
    def night(self) -> Night:
        return Night(*self._ARGS)

    @property
    def morning(self) -> Morning:
        return Morning(*self._ARGS)

    @property
    def afternoon(self) -> Afternoon:
        return Afternoon(*self._ARGS)

    @property
    def evening(self) -> Evening:
        return Evening(*self._ARGS)
