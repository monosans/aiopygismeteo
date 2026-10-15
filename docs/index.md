# aiopygismeteo

Асинхронная обёртка для [Gismeteo API](https://gismeteo.ru/api/) на Python с типизированными ответами. Синхронная версия — [pygismeteo](https://monosans.github.io/pygismeteo).

!!! warning "Разработка приостановлена"

    У разработчика нет токена Gismeteo API, поэтому библиотека не проверяется на реальном API и модели ответов могут устареть. Токен выдают по запросу на [b2b@gismeteo.ru](mailto:b2b@gismeteo.ru). Погода без токена — в [aiopywttr](https://github.com/monosans/aiopywttr).

## Установка

=== "uv"

    ```bash
    uv add aiopygismeteo pygismeteo-base
    ```

=== "pip"

    ```bash
    pip install -U aiopygismeteo pygismeteo-base
    ```

## Быстрый старт

```python
import asyncio

import aiopygismeteo


async def main() -> None:
    async with aiopygismeteo.Gismeteo(token="56b30cb255.3443075") as gismeteo:
        city = (await gismeteo.search.by_query("Москва"))[0]
        current = await gismeteo.current.by_id(city.id)
    print(current.temperature.air.c, current.description.full)


asyncio.run(main())
```

## Куда дальше

- [Руководство](guide.md) — примеры по задачам: найти город, текущая погода, прогнозы, ошибки, своя HTTP-сессия.
- [API Reference](api.md) — все классы, методы и поля ответов.
