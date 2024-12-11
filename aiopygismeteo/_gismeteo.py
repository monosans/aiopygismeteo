from __future__ import annotations

from typing import Final, Optional

from aiohttp import ClientSession
from pydantic import AnyHttpUrl, validate_call
from pygismeteo_base.types import Lang
from typing_extensions import Self, final

from aiopygismeteo._endpoints.current import Current
from aiopygismeteo._endpoints.search import Search
from aiopygismeteo._endpoints.step3 import Step3
from aiopygismeteo._endpoints.step6 import Step6
from aiopygismeteo._endpoints.step24 import Step24
from aiopygismeteo._http import AiohttpClient


@final
class Gismeteo:
    """Асинхронная обёртка для Gismeteo API.

    Examples:
        ```python
        async with aiopygismeteo.Gismeteo(
            token="56b30cb255.3443075"
        ) as gismeteo:
            search_results = await gismeteo.search.by_query("Москва")
            city_id = search_results[0].id
            current = await gismeteo.current.by_id(city_id)
        print(current)
        ```

        Кастомный базовый URL:

        ```python
        async with aiopygismeteo.Gismeteo(
            token=...,
            base_url=pydantic.AnyHttpUrl("https://api.example.com/v1"),
        ) as gismeteo:
            ...
        ```

        Другой язык:

        ```python
        async with aiopygismeteo.Gismeteo(
            token=..., lang=aiopygismeteo.Lang.EN
        ) as gismeteo:
            ...
        ```

        Кастомная aiohttp.ClientSession:

        ```python
        async with aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(total=60, connect=5)
        ) as session:
            gismeteo = aiopygismeteo.Gismeteo(token=..., session=session)
            ...
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
        session: Optional[ClientSession] = None,
    ) -> None:
        """Асинхронная обёртка для Gismeteo API.

        Args:
            token:
                X-Gismeteo-Token.
                Запросить можно по электронной почте
                [b2b@gismeteo.ru](mailto:b2b@gismeteo.ru).

        Examples:
            ```python
            async with aiopygismeteo.Gismeteo(
                token="56b30cb255.3443075"
            ) as gismeteo:
                search_results = await gismeteo.search.by_query("Москва")
                city_id = search_results[0].id
                current = await gismeteo.current.by_id(city_id)
            print(current)
            ```

            Кастомный базовый URL:

            ```python
            async with aiopygismeteo.Gismeteo(
                token=...,
                base_url=pydantic.AnyHttpUrl("https://api.example.com/v1"),
            ) as gismeteo:
                ...
            ```

            Другой язык:

            ```python
            async with aiopygismeteo.Gismeteo(
                token=..., lang=aiopygismeteo.Lang.EN
            ) as gismeteo:
                ...
            ```

            Кастомная aiohttp.ClientSession:

            ```python
            async with aiohttp.ClientSession(
                timeout=aiohttp.ClientTimeout(total=60, connect=5)
            ) as session:
                gismeteo = aiopygismeteo.Gismeteo(token=..., session=session)
                ...
            ```
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
        """Поиск."""
        return self._search

    @property
    def step3(self) -> Step3:
        """Погода с шагом 3 часа."""
        return self._step3

    @property
    def step6(self) -> Step6:
        """Погода с шагом 6 часа."""
        return self._step6

    @property
    def step24(self) -> Step24:
        """Погода с шагом 24 часов."""
        return self._step24

    @property
    def token(self) -> str:
        """X-Gismeteo-Token."""
        return self._session.token.get_secret_value()

    @property
    def base_url(self) -> AnyHttpUrl:
        return self._session.base_url

    @property
    def lang(self) -> Lang:
        return self._session.lang

    @property
    def session(self) -> Optional[ClientSession]:
        return self._session.session

    async def close(self) -> None:
        """Закрыть HTTP сессию."""
        if self._session.session is not None:
            await self._session.session.close()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, *_: object) -> None:
        await self.close()
