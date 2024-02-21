from __future__ import annotations

from typing import Final, Optional

from aiohttp import ClientSession
from pygismeteo_base.types import Lang
from pygismeteo_base.validators import Settings
from typing_extensions import final

from ._current import Current
from ._http import AiohttpClient
from ._search import Search
from ._step_n import Step3, Step6, Step24


@final
class Gismeteo:
    """Асинхронная обёртка для Gismeteo API."""

    __slots__ = (
        "_session",
        "_settings",
        "current",
        "search",
        "step3",
        "step6",
        "step24",
    )

    def __init__(
        self,
        *,
        lang: Optional[Lang] = None,
        session: Optional[ClientSession] = None,
        token: str,
    ) -> None:
        """Асинхронная обёртка для Gismeteo API.

        Args:
            lang:
                Язык. По умолчанию "ru".
            session:
                Экземпляр aiohttp.ClientSession.
                По умолчанию для каждого запроса создаётся новый экземпляр.
            token:
                X-Gismeteo-Token.
                Запросить можно по электронной почте b2b@gismeteo.ru.
        """
        self._settings = Settings(lang=lang, token=token)
        self._session = AiohttpClient(session, self._settings)
        self.current: Final = Current(self._session)
        """Текущая погода."""
        self.search: Final = Search(self._session)
        """Поиск."""
        self.step3: Final = Step3(self._session)
        """Погода с шагом 3 часа."""
        self.step6: Final = Step6(self._session)
        """Погода с шагом 6 часов."""
        self.step24: Final = Step24(self._session)
        """Погода с шагом 24 часа."""

    @property
    def lang(self) -> Optional[Lang]:
        """Язык."""
        return self._settings.lang

    @lang.setter
    def lang(self, lang: Optional[Lang]) -> None:
        self._settings.lang = lang

    @property
    def session(self) -> Optional[ClientSession]:
        return self._session.session

    @session.setter
    def session(self, session: Optional[ClientSession]) -> None:
        self._session.session = session

    @property
    def token(self) -> str:
        """X-Gismeteo-Token."""
        return self._settings.token

    @token.setter
    def token(self, token: str) -> None:
        self._settings.token = token
