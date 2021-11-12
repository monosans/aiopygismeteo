# -*- coding: utf-8 -*-
from aiohttp import ClientSession


async def req(endpoint: str) -> bytes:
    async with ClientSession() as s:
        async with s.get(
            f"https://gismeteo.ru{endpoint}",
            headers={
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
                + " (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
            },
        ) as r:
            return await r.read()
