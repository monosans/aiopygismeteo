# -*- coding: utf-8 -*-
from typing import Optional as _Optional

import pygismeteo_base as _pygismeteo_base
from aiohttp import ClientSession as _ClientSession

from aiopygismeteo._http import get_json as _get_json
from aiopygismeteo.exceptions import LocalityNotFound as _LocalityNotFound


async def id_by_query(
    query: str,
    *,
    lang: _pygismeteo_base.types.LANG = "ru",
    token: str = _pygismeteo_base.constants.DEFAULT_TOKEN,
    session: _Optional[_ClientSession] = None,
) -> int:
    r = await _get_json(
        "search/cities",
        params={"lang": lang, "query": query},
        token=token,
        session=session,
    )
    items = r["response"]["items"]
    if not items:
        raise _LocalityNotFound("Населённый пункт не найден.")
    return int(items[0]["id"])
