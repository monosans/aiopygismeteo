# -*- coding: utf-8 -*-
from lxml.html import fromstring

from aiopygismeteo._dates.abc import ABCDate
from aiopygismeteo._utils import normalize_str


class Now(ABCDate):
    """Возвращается методом now() класса Gismeteo."""

    def __init__(self, html: bytes) -> None:
        self._tree = fromstring(html)

    @property
    def status(self) -> str:
        """Ясно, пасмурно, сильный дождь и т. д."""
        return self._build_result(
            '//div[contains(@class,"now__desc")]//text()'
        )

    @property
    def temperature(self) -> str:
        """Температура, °C."""
        return self._build_result(
            '//div[contains(@class,"now__weather")]'
            + '//span[contains(@class,"unit_temperature_c")]//text()'
        )

    @property
    def real_feel(self) -> str:
        """Температура по ощущению, °C."""
        return self._build_result(
            '//div[contains(@class,"now__feel")]'
            + '/span[contains(@class,"unit_temperature_c")]/text()'
        )

    @property
    def sunrise(self) -> str:
        """Заход."""
        return self._build_result(
            '//div[contains(@class,"nowastro__item_sunrise")]'
            + '/div[contains(@class,"nowastro__time")]/text()'
        )

    @property
    def sunset(self) -> str:
        """Восход."""
        return self._build_result(
            '//div[contains(@class,"nowastro__item_sunset")]'
            + '/div[contains(@class,"nowastro__time")]/text()'
        )

    @property
    def wind_speed(self) -> str:
        """Скорость ветра, м/с."""
        return self._build_result(
            '//div[contains(@class,"unit_wind_m_s")]'
            + '//div[contains(@class,"nowinfo__value")]/text()'
        )

    @property
    def wind_direction(self) -> str:
        """Направление ветра."""
        return self._build_result(
            '//div[contains(@class,"unit_wind_m_s")]'
            + '//div[contains(@class,"nowinfo__measure")]/text()[last()]'
        )

    @property
    def pressure(self) -> str:
        """Давление, мм рт. ст."""
        return self._build_result(
            '//div[contains(@class,"unit_pressure_mm_hg_atm")]'
            + '//div[contains(@class,"nowinfo__value")]/text()'
        )

    @property
    def humidity(self) -> str:
        """Влажность, %."""
        return self._build_result(
            '//div[contains(@class,"nowinfo__item_humidity")]'
            + '//div[contains(@class,"nowinfo__value")]/text()'
        )

    @property
    def gm_activity(self) -> str:
        """Геомагнитная активность, Кп-индекс."""
        return self._build_result(
            '//div[contains(@class,"nowinfo__item_gm")]'
            + '//div[contains(@class,"nowinfo__value")]/text()'
        )

    @property
    def water(self) -> str:
        """Температура воды, °C."""
        return self._build_result(
            '//div[contains(@class,"nowinfo__item_water")]'
            + '//div[contains(@class,"unit_temperature_c")]'
            + '/div[contains(@class,"nowinfo__value")]/text()'
        )

    def _build_result(self, xpath: str) -> str:
        return "".join(normalize_str(el) for el in self._tree.xpath(xpath))
