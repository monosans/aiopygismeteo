from __future__ import annotations

from typing import Optional

from aiohttp import ClientSession
from pygismeteo_base.types import Lang
from pygismeteo_base.validators import Settings

from ._current import Current
from ._http import AiohttpClient
from ._search import Search
from ._step_n import Step3, Step6, Step24


class Gismeteo:
    """Асинхронная обёртка для Gismeteo API."""

    __slots__ = (
        "_settings",
        "_session",
        "_current",
        "_step3",
        "_step6",
        "_step24",
        "_search",
    )

    def __init__(
        self,
        *,
        lang: Optional[Lang] = None,
        token: Optional[str] = None,
        session: Optional[ClientSession] = None,
    ) -> None:
        """Асинхронная обёртка для Gismeteo API.

        Args:
            lang: язык. По умолчанию "ru".
            token: X-Gismeteo-Token,
                если используемый по умолчанию перестал работать.
            session: экземпляр aiohttp.ClientSession.
                По умолчанию для каждого запроса создаётся новый экземпляр.
        """
        self._settings = Settings(lang=lang, token=token)
        self._session = AiohttpClient(session, self._settings)
        self._current = Current(self._session)
        self._step3 = Step3(self._session)
        self._step6 = Step6(self._session)
        self._step24 = Step24(self._session)
        self._search = Search(self._session)

    @property
    def session(self) -> Optional[ClientSession]:
        return self._session.session

    @session.setter
    def session(self, session: Optional[ClientSession]) -> None:
        self._session.session = session

    @property
    def lang(self) -> Optional[Lang]:
        """Язык."""
        return self._settings.lang

    @lang.setter
    def lang(self, lang: Optional[Lang]) -> None:
        self._settings.lang = lang

    @property
    def token(self) -> Optional[str]:
        """X-Gismeteo-Token."""
        return self._settings.token

    @token.setter
    def token(self, token: Optional[str]) -> None:
        self._settings.token = token

    @property
    def current(self) -> Current:
        """Текущая погода."""
        return self._current

    @property
    def step3(self) -> Step3:
        """Погода с шагом 3 часа."""
        return self._step3

    @property
    def step6(self) -> Step6:
        """Погода с шагом 6 часов."""
        return self._step6

    @property
    def step24(self) -> Step24:
        """Погода с шагом 24 часа."""
        return self._step24

    @property
    def search(self) -> Search:
        """Поиск."""
        return self._search
