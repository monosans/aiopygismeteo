<img src="https://raw.githubusercontent.com/monosans/aiopygismeteo/main/docs/assets/logo.svg" alt="" width="96" align="right">

# aiopygismeteo

[![Downloads](https://static.pepy.tech/badge/aiopygismeteo)](https://pepy.tech/project/aiopygismeteo)

Асинхронная обёртка для [Gismeteo API](https://gismeteo.ru/api/) на Python с типизированными ответами. Синхронная версия называется [pygismeteo](https://github.com/monosans/pygismeteo).

Разработка приостановлена: у разработчика нет токена Gismeteo API, поэтому библиотека не проверяется на реальном API. Работает с Gismeteo API v2, новая v4 не поддерживается. Погоду без токена можно получить через [aiopywttr](https://github.com/monosans/aiopywttr).

## Установка

```bash
uv add aiopygismeteo pygismeteo-base
# или
pip install -U aiopygismeteo pygismeteo-base
```

## Пример

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

## Документация

<https://monosans.github.io/aiopygismeteo>

## License / Лицензия

[MIT](https://github.com/monosans/aiopygismeteo/blob/main/LICENSE)
