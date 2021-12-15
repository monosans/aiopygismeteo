# -*- coding: utf-8 -*-
from typing import Any, Dict, Optional

import pygismeteo_base
from aiohttp import ClientSession


async def _fetch(
    endpoint: str, params: Dict[str, Any], token: str, session: ClientSession
) -> Dict[str, Any]:
    async with session.get(
        f"https://api.gismeteo.net/v2/{endpoint}",
        params=params,
        headers={"X-Gismeteo-Token": token},
    ) as r:
        return dict(await r.json())


async def get_json(
    endpoint: str,
    params: Dict[str, Any],
    *,
    token: str = pygismeteo_base.constants.DEFAULT_TOKEN,
    session: Optional[ClientSession] = None,
) -> Dict[str, Any]:
    if session:
        return await _fetch(endpoint, params, token, session)
    async with ClientSession() as s:
        return await _fetch(endpoint, params, token, s)


async def get_response(
    endpoint: str,
    params: Dict[str, Any],
    *,
    token: str = pygismeteo_base.constants.DEFAULT_TOKEN,
    session: Optional[ClientSession] = None,
) -> Dict[str, Any]:
    return (
        await get_json(endpoint, params, token=token, session=session)
    ).get("response", {})
