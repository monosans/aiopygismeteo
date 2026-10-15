from __future__ import annotations

from typing import Final, Self, final

from aiohttp import ClientSession
from pydantic import AnyHttpUrl, validate_call
from pygismeteo_base.types import Lang

from aiopygismeteo._endpoints.current import Current
from aiopygismeteo._endpoints.search import Search
from aiopygismeteo._endpoints.step3 import Step3
from aiopygismeteo._endpoints.step6 import Step6
from aiopygismeteo._endpoints.step24 import Step24
from aiopygismeteo._http import AiohttpClient


@final
class Gismeteo:
    """Асинхронный клиент Gismeteo API.

    Используйте как асинхронный контекстный менеджер: на выходе
    закрывается HTTP-сессия.

    Examples:
        ```python
        async with aiopygismeteo.Gismeteo(
            token="56b30cb255.3443075"
        ) as gismeteo:
            city = (await gismeteo.search.by_query("Москва"))[0]
            current = await gismeteo.current.by_id(city.id)
        print(current.temperature.air.c)
        ```
    """

    __slots__ = (
        "_current",
        "_search",
        "_session",
        "_step3",
        "_step6",
        "_step24",
    )

    @validate_call(config={"arbitrary_types_allowed": True})
    def __init__(
        self,
        *,
        token: str,
        base_url: AnyHttpUrl = AnyHttpUrl.build(  # noqa: B008
            scheme="https", host="api.gismeteo.net", path="v2"
        ),
        lang: Lang = Lang.RU,
        session: ClientSession | None = None,
    ) -> None:
        """Создать клиент.

        Args:
            token: X-Gismeteo-Token. Выдают по запросу на
                [b2b@gismeteo.ru](mailto:b2b@gismeteo.ru).
            base_url: Адрес API.
            lang: Язык названий и описаний в ответах.
            session: Своя HTTP-сессия, например с другими таймаутами.
                Без неё сессия создаётся при первом запросе.
                [`close`][aiopygismeteo.Gismeteo.close] закрывает и переданную
                сессию.
        """
        self._session: Final = AiohttpClient(
            token=token, base_url=base_url, lang=lang, session=session
        )
        self._current: Final = Current(self._session)
        self._search: Final = Search(self._session)
        self._step3: Final = Step3(self._session)
        self._step6: Final = Step6(self._session)
        self._step24: Final = Step24(self._session)

    @property
    def current(self) -> Current:
        """Текущая погода."""
        return self._current

    @property
    def search(self) -> Search:
        """Поиск географических объектов."""
        return self._search

    @property
    def step3(self) -> Step3:
        """Прогноз с шагом 3 часа."""
        return self._step3

    @property
    def step6(self) -> Step6:
        """Прогноз с шагом 6 часов."""
        return self._step6

    @property
    def step24(self) -> Step24:
        """Прогноз с шагом 24 часа."""
        return self._step24

    @property
    def token(self) -> str:
        """X-Gismeteo-Token."""
        return self._session.token.get_secret_value()

    @property
    def base_url(self) -> AnyHttpUrl:
        """Адрес API."""
        return self._session.base_url

    @property
    def lang(self) -> Lang:
        """Язык ответов."""
        return self._session.lang

    @property
    def session(self) -> ClientSession | None:
        """HTTP-сессия: переданная или созданная при первом запросе."""
        return self._session.session

    async def close(self) -> None:
        """Закрыть HTTP-сессию, в том числе переданную в `session`."""
        if self._session.session is not None:
            await self._session.session.close()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, *_: object) -> None:
        await self.close()
