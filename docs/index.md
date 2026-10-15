# aiopygismeteo

Асинхронная обёртка для [Gismeteo API](https://gismeteo.ru/api/) на Python с типизированными ответами. Синхронная версия называется [pygismeteo](https://monosans.github.io/pygismeteo).

!!! warning "Разработка приостановлена"

    Работает с Gismeteo API v2. Новая [v4](https://docs.gismeteo.net/v4/weather/) не поддерживается.

    У разработчика нет токена Gismeteo API, поэтому библиотека не проверяется на реальном API и модели ответов могут устареть. Погоду без токена можно получить через [aiopywttr](https://github.com/monosans/aiopywttr).

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

В примере стоит образец токена. Свой выдают по запросу на [b2b@gismeteo.ru](mailto:b2b@gismeteo.ru).

## Куда дальше

- [Руководство](guide.md) с примерами по задачам: найти город, текущая погода, прогнозы, ошибки, своя HTTP-сессия.
- [Справочник API](api.md) со всеми классами, методами и полями ответов.
