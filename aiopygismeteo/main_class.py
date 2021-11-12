# -*- coding: utf-8 -*-
from aiopygismeteo.dates.month import Month
from aiopygismeteo.dates.now import Now
from aiopygismeteo.dates.one_day import OneDay
from aiopygismeteo.dates.ten_days import TenDays
from aiopygismeteo.dates.three_days import ThreeDays
from aiopygismeteo.dates.two_weeks import TwoWeeks
from aiopygismeteo.http import HTTPSession


class Gismeteo:
    def __init__(self, base_endpoint: str, session: HTTPSession) -> None:
        self._base_endpoint = base_endpoint
        self._session = session

    async def now(self) -> Now:
        """Сейчас."""
        return Now(await self._session.req(f"{self._base_endpoint}now/"))

    async def today(self) -> OneDay:
        """Сегодня."""
        return OneDay(await self._session.req(self._base_endpoint))

    async def tomorrow(self) -> OneDay:
        """Завтра."""
        return OneDay(
            await self._session.req(f"{self._base_endpoint}tomorrow/")
        )

    async def in3_days(self) -> OneDay:
        """Через 3 дня (послезавтра)."""
        return OneDay(await self._session.req(f"{self._base_endpoint}3-day/"))

    async def in4_days(self) -> OneDay:
        """Через 4 дня."""
        return OneDay(await self._session.req(f"{self._base_endpoint}4-day/"))

    async def in5_days(self) -> OneDay:
        """Через 5 дней."""
        return OneDay(await self._session.req(f"{self._base_endpoint}5-day/"))

    async def in6_days(self) -> OneDay:
        """Через 6 дней."""
        return OneDay(await self._session.req(f"{self._base_endpoint}6-day/"))

    async def in7_days(self) -> OneDay:
        """Через 7 дней."""
        return OneDay(await self._session.req(f"{self._base_endpoint}7-day/"))

    async def in8_days(self) -> OneDay:
        """Через 8 дней."""
        return OneDay(await self._session.req(f"{self._base_endpoint}8-day/"))

    async def in9_days(self) -> OneDay:
        """Через 9 дней."""
        return OneDay(await self._session.req(f"{self._base_endpoint}9-day/"))

    async def in10_days(self) -> OneDay:
        """Через 10 дней."""
        return OneDay(await self._session.req(f"{self._base_endpoint}10-day/"))

    async def three_days(self) -> ThreeDays:
        """3 дня."""
        return ThreeDays(
            await self._session.req(f"{self._base_endpoint}3-days/")
        )

    async def ten_days(self) -> TenDays:
        """10 дней."""
        return TenDays(
            await self._session.req(f"{self._base_endpoint}10-days/")
        )

    async def two_weeks(self) -> TwoWeeks:
        """2 недели."""
        return TwoWeeks(
            await self._session.req(f"{self._base_endpoint}2-weeks/")
        )

    async def month(self) -> Month:
        """Месяц."""
        return Month(await self._session.req(f"{self._base_endpoint}month/"))
