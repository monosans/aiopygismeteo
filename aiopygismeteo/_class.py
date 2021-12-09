# -*- coding: utf-8 -*-
from pygismeteo_base.dates.month import Month
from pygismeteo_base.dates.now import Now
from pygismeteo_base.dates.one_day import OneDay
from pygismeteo_base.dates.ten_days import TenDays
from pygismeteo_base.dates.three_days import ThreeDays
from pygismeteo_base.dates.two_weeks import TwoWeeks

from aiopygismeteo._http import HTTPSession


class Gismeteo:
    """Возвращается фабрикой gismeteo()."""

    def __init__(self, base_endpoint: str, session: HTTPSession) -> None:
        self._BASE_ENDPOINT = base_endpoint
        self._session = session

    async def now(self) -> Now:
        """Сейчас."""
        return Now(await self._session.req(f"{self._BASE_ENDPOINT}now/"))

    async def today(self) -> OneDay:
        """Сегодня."""
        return OneDay(await self._session.req(self._BASE_ENDPOINT))

    async def tomorrow(self) -> OneDay:
        """Завтра."""
        return OneDay(
            await self._session.req(f"{self._BASE_ENDPOINT}tomorrow/")
        )

    async def in3_days(self) -> OneDay:
        """Через 3 дня (послезавтра)."""
        return OneDay(await self._session.req(f"{self._BASE_ENDPOINT}3-day/"))

    async def in4_days(self) -> OneDay:
        """Через 4 дня."""
        return OneDay(await self._session.req(f"{self._BASE_ENDPOINT}4-day/"))

    async def in5_days(self) -> OneDay:
        """Через 5 дней."""
        return OneDay(await self._session.req(f"{self._BASE_ENDPOINT}5-day/"))

    async def in6_days(self) -> OneDay:
        """Через 6 дней."""
        return OneDay(await self._session.req(f"{self._BASE_ENDPOINT}6-day/"))

    async def in7_days(self) -> OneDay:
        """Через 7 дней."""
        return OneDay(await self._session.req(f"{self._BASE_ENDPOINT}7-day/"))

    async def in8_days(self) -> OneDay:
        """Через 8 дней."""
        return OneDay(await self._session.req(f"{self._BASE_ENDPOINT}8-day/"))

    async def in9_days(self) -> OneDay:
        """Через 9 дней."""
        return OneDay(await self._session.req(f"{self._BASE_ENDPOINT}9-day/"))

    async def in10_days(self) -> OneDay:
        """Через 10 дней."""
        return OneDay(await self._session.req(f"{self._BASE_ENDPOINT}10-day/"))

    async def three_days(self) -> ThreeDays:
        """3 дня."""
        return ThreeDays(
            await self._session.req(f"{self._BASE_ENDPOINT}3-days/")
        )

    async def ten_days(self) -> TenDays:
        """10 дней."""
        return TenDays(
            await self._session.req(f"{self._BASE_ENDPOINT}10-days/")
        )

    async def two_weeks(self) -> TwoWeeks:
        """2 недели."""
        return TwoWeeks(
            await self._session.req(f"{self._BASE_ENDPOINT}2-weeks/")
        )

    async def month(self) -> Month:
        """Месяц."""
        return Month(await self._session.req(f"{self._BASE_ENDPOINT}month/"))
