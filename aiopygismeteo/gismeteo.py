# -*- coding: utf-8 -*-
from re import findall
from typing import Optional

from aiohttp import ClientSession
from lxml.html import fromstring

from aiopygismeteo.exceptions import InvalidLocalityID, LocalityNotFound
from aiopygismeteo.http import HTTPSession
from aiopygismeteo.main_class import Gismeteo


async def gismeteo(
    locality: str, *, session: Optional[ClientSession] = None
) -> Gismeteo:
    """Фабрика для Gismeteo.

    Args:
        locality (str): Населённый пункт.
            Может быть ссылкой на сайт типа gismeteo.ru/weather-moscow-4368/
            или названием населённого пункта, например, Москва.
        session (Optional[ClientSession], optional): Экземпляр
            aiohttp.ClientSession, если нужно использовать свой.
            Defaults to None.

    Raises:
        InvalidLocalityID: Указана неверная ссылка.
        LocalityNotFound: Населённый пункт не найден.

    Returns:
        Gismeteo: Экземпляр класса Gismeteo.
    """

    sess = HTTPSession(session)
    if "weather-" in locality:
        endpoint = findall(r".*(weather-.*-\d+).*", locality)
        if len(endpoint) != 1:
            raise InvalidLocalityID()
        return Gismeteo(f"/{endpoint[0]}/", sess)
    r = await sess.req(f"/search/{locality}")
    tree = fromstring(r)
    localities = tree.xpath(
        '//section[contains(@class,"section-catalog")]'
        + '/section[last()]//a[contains(@class,"link-item")]/@href'
    )
    if not localities:
        raise LocalityNotFound()
    return Gismeteo(localities[0], sess)
