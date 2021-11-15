# -*- coding: utf-8 -*-
from typing import Dict, Optional

from lxml.html import fromstring

from aiopygismeteo._dates import xpaths
from aiopygismeteo._dates.abc import ABCDate
from aiopygismeteo._utils import normalize_strs, strip_strs


class OneDay(ABCDate):
    """Класс, от которого наследуются однодневные классы."""

    def __init__(self, html: bytes) -> None:
        self._tree = fromstring(html)
        self._TIME = strip_strs(
            self._tree.xpath(
                xpaths.get_ancestor("forecast")
                + '//div[@class="w_time"]/span/text()'
            )
        )

    @property
    def status(self) -> Dict[str, str]:
        """Ясно, пасмурно, сильный дождь и т. д."""
        return self._build_result(*xpaths.STATUS)

    @property
    def temperature(self) -> Dict[str, str]:
        """Температура, °C."""
        return self._build_result(*xpaths.TEMPERATURE)

    @property
    def wind_speed(self) -> Dict[str, str]:
        """Скорость ветра, м/с."""
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
    def road_condition(self) -> Dict[str, str]:
        """Погода на дорогах."""
        return self._build_result(*xpaths.ROAD_CONDITION)

    @property
    def pressure(self) -> Dict[str, str]:
        """Давление, мм рт. ст."""
        return self._build_result(*xpaths.PRESSURE)

    @property
    def humidity(self) -> Dict[str, str]:
        """Влажность, %."""
        return self._build_result(*xpaths.HUMIDITY)

    @property
    def visibility(self) -> Dict[str, str]:
        """Видимость, км."""
        return {
            **dict(zip(self._TIME, ("Неизвестно",) * len(self._TIME))),
            **self._build_result(*xpaths.VISIBILITY),
        }

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
            )
            if (
                self._tree.xpath(parent_container)
                and (not check_absence or not self._tree.xpath(check_absence))
            )
            else (default_value,) * len(self._TIME)
        )
        return dict(zip(self._TIME, elements))


class Today(OneDay):
    """Возвращается методом today() класса Gismeteo."""


class Tomorrow(OneDay):
    """Возвращается методом tomorrow() класса Gismeteo."""


class In3Days(OneDay):
    """Возвращается методом in3_days() класса Gismeteo."""


class In4Days(OneDay):
    """Возвращается методом in4_days() класса Gismeteo."""


class In5Days(OneDay):
    """Возвращается методом in5_days() класса Gismeteo."""


class In6Days(OneDay):
    """Возвращается методом in6_days() класса Gismeteo."""


class In7Days(OneDay):
    """Возвращается методом in7_days() класса Gismeteo."""


class In8Days(OneDay):
    """Возвращается методом in8_days() класса Gismeteo."""


class In9Days(OneDay):
    """Возвращается методом in9_days() класса Gismeteo."""


class In10Days(OneDay):
    """Возвращается методом in10_days() класса Gismeteo."""
