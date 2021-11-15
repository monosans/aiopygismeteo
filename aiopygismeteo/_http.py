# -*- coding: utf-8 -*-
from typing import Optional

from aiohttp import ClientSession


class HTTPSession:
    def __init__(self, session: Optional[ClientSession]) -> None:
        self.session = session

    @staticmethod
    async def fetch(session: ClientSession, endpoint: str) -> bytes:
        async with session.get(
            f"https://gismeteo.ru{endpoint}",
            headers={
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64)"
                + " AppleWebKit/537.36 (KHTML, like Gecko)"
                + " Chrome/95.0.4638.69 Safari/537.36"
            },
        ) as r:
            return await r.read()

    async def req(self, endpoint: str) -> bytes:
        if self.session:
            return await self.fetch(self.session, endpoint)
        async with ClientSession() as session:
            return await self.fetch(session, endpoint)
