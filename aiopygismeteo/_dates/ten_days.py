# -*- coding: utf-8 -*-
from typing import Dict

from aiopygismeteo._dates import xpaths
from aiopygismeteo._dates.two_weeks import TwoWeeksBase


class TenDays(TwoWeeksBase):
    """Возвращается методом ten_days() класса Gismeteo."""

    @property
    def ultraviolet_index(self) -> Dict[str, str]:
        """Ультрафиолетовый индекс, баллы."""
        return self._build_result(*xpaths.ULTRAVIOLET_INDEX)

    @property
    def falling_snow(self) -> Dict[str, str]:
        """Выпадающий снег, см."""
        return self._build_result(*xpaths.FALLING_SNOW)

    @property
    def snow_depth(self) -> Dict[str, str]:
        """Высота снежного покрова, см."""
        return self._build_result(*xpaths.SNOW_DEPTH)
