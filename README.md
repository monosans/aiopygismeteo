# aiopygismeteo

[![CI](https://github.com/monosans/aiopygismeteo/actions/workflows/ci.yml/badge.svg?branch=main&event=push)](https://github.com/monosans/aiopygismeteo/actions/workflows/ci.yml?query=event%3Apush+branch%3Amain)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/monosans/aiopygismeteo/main.svg)](https://results.pre-commit.ci/latest/github/monosans/aiopygismeteo/main)
[![Coverage](https://img.shields.io/codecov/c/github/monosans/aiopygismeteo/main?logo=codecov)](https://codecov.io/gh/monosans/aiopygismeteo)
[![PyPI Downloads](https://img.shields.io/pypi/dm/aiopygismeteo?logo=pypi)](https://pypi.org/project/aiopygismeteo/)

Асинхронная обёртка для [Gismeteo API](https://gismeteo.ru/api/).

Синхронная версия [здесь](https://github.com/monosans/pygismeteo).

## Установка

```bash
python -m pip install -U aiopygismeteo
```

## Документация

<https://aiopygismeteo.readthedocs.io/>

## Пример, выводящий температуру в Москве сейчас

```python
import asyncio

import aiopygismeteo


async def main():
    gm = aiopygismeteo.Gismeteo()
    search_results = await gm.search.by_query("Москва")
    city_id = search_results[0].id
    current = await gm.current.by_id(city_id)
    print(current.temperature.air.c)


asyncio.run(main())
```

## License / Лицензия

[MIT](https://github.com/monosans/aiopygismeteo/blob/main/LICENSE)
