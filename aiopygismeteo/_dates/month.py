# -*- coding: utf-8 -*-
from typing import Dict

from lxml.html import fromstring

from aiopygismeteo._dates.abc import ABCDate
from aiopygismeteo._utils import normalize_strs, strip_strs


class Month(ABCDate):
    """Возвращается методом month() класса Gismeteo."""

    def __init__(self, html: bytes) -> None:
        self._tree = fromstring(html)
        self._TIME = strip_strs(
            self._tree.xpath(
                '//div[@data-text]//div[contains(@class,"date")]//text()'
            )
        )

    @property
    def status(self) -> Dict[str, str]:
        """Ясно, пасмурно, сильный дождь и т. д."""
        return self._build_result("//div/@data-text")

    @property
    def max_temperature(self) -> Dict[str, str]:
        """Макс. температура, °C."""
        return self._build_result(
            '//div[@data-text]//div[contains(@class,"temp_max")]'
            + '//span[contains(@class,"unit_temperature_c")]/text()'
        )

    @property
    def min_temperature(self) -> Dict[str, str]:
        """Мин. температура, °C."""
        return self._build_result(
            '//div[@data-text]//div[contains(@class,"temp_max")]'
            + '//span[contains(@class,"unit_temperature_c")]/text()'
        )

    def _build_result(
        self, xpath: str, *, default_value: str = "Неизвестно"
    ) -> Dict[str, str]:
        elements = normalize_strs(self._tree.xpath(xpath), default_value)
        return dict(zip(self._TIME, elements))
