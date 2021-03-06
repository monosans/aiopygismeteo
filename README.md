# aiopygismeteo

[![test](https://github.com/monosans/aiopygismeteo/actions/workflows/test.yml/badge.svg?branch=main&event=push)](https://github.com/monosans/aiopygismeteo/actions/workflows/test.yml)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/monosans/aiopygismeteo/main.svg)](https://results.pre-commit.ci/latest/github/monosans/aiopygismeteo/main)
[![codecov](https://codecov.io/gh/monosans/aiopygismeteo/branch/main/graph/badge.svg)](https://codecov.io/gh/monosans/aiopygismeteo)

Асинхронная обёртка для [Gismeteo API](https://gismeteo.ru/api/).

Синхронная версия [здесь](https://github.com/monosans/pygismeteo).

## Установка

```bash
python -m pip install -U aiopygismeteo
```

## Документация

[aiopygismeteo.readthedocs.io](https://aiopygismeteo.readthedocs.io/)

## Пример, выводящий температуру в Москве сейчас

```python
import asyncio

from aiopygismeteo import Gismeteo


async def main():
    gm = Gismeteo()
    search_results = await gm.search.by_query("Москва")
    city_id = search_results[0].id
    current = await gm.current.by_id(city_id)
    print(current.temperature.air.c)


asyncio.run(main())
```

## License / Лицензия

[MIT](https://github.com/monosans/aiopygismeteo/blob/main/LICENSE)
