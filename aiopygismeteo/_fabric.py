# -*- coding: utf-8 -*-
from re import findall
from typing import Optional

from aiohttp import ClientSession
from lxml.html import fromstring
from pygismeteo_base.constants import URL_REGEX

from aiopygismeteo._class import Gismeteo
from aiopygismeteo._http import HTTPSession
from aiopygismeteo.exceptions import LocalityError


async def by_name(
    locality: str, *, session: Optional[ClientSession] = None
) -> Gismeteo:
    """Создание экземпляра Gismeteo по названию населённого пункта.

    Args:
        locality (str): Название населённого пункта.
        session (Optional[ClientSession], optional): Экземпляр
            aiohttp.ClientSession, если нужно использовать свой.
            Defaults to None.

    Raises:
        LocalityError: Населённый пункт не найден.

    Returns:
        Gismeteo: Экземпляр класса Gismeteo.

    Examples:
        >>> gm = await aiopygismeteo.by_name("Москва")
        ... now = await gm.now()
        ... print(now.temperature)

        >>> gm = await aiopygismeteo.by_name("Kazan")
        ... today = await gm.today()
        ... print(today.wind_speed)
    """
    sess = HTTPSession(session)
    r = await sess.req(f"/search/{locality}")
    tree = fromstring(r)
    localities = tree.xpath(
        '//section[contains(@class,"section-catalog")]'
        + '/section[last()]//a[contains(@class,"link-item")]/@href'
    )
    if not localities:
        raise LocalityError("Населённый пункт не найден.")
    return Gismeteo(localities[0], sess)


async def by_url(
    locality: str, *, session: Optional[ClientSession] = None
) -> Gismeteo:
    """Создание экземпляра Gismeteo по ссылке на населённый пункт.

    Args:
        locality (str): Ссылка на населённый пункт.
        session (Optional[ClientSession], optional): Экземпляр
            aiohttp.ClientSession, если нужно использовать свой.
            Defaults to None.

    Raises:
        LocalityError: Количество ссылок не равно 1.

    Returns:
        Gismeteo: Экземпляр класса Gismeteo.

    Examples:
        >>> gm = await aiopygismeteo.by_url(
        ...     "https://gismeteo.ru/weather-moscow-4368/"
        ... )
        ... now = await gm.now()
        ... print(now.temperature)

        >>> gm = await aiopygismeteo.by_url("gismeteo.ru/weather-kazan-4364/")
        ... month = await gm.month()
        ... print(month.status)

        >>> gm = await aiopygismeteo.by_url("weather-sankt-peterburg-4079")
        ... today = await gm.today()
        ... print(today.wind_speed)
    """
    endpoint = findall(URL_REGEX, locality)
    if len(endpoint) != 1:
        raise LocalityError("Количество ссылок не равно 1.")
    return Gismeteo(f"/{endpoint[0]}/", HTTPSession(session))
