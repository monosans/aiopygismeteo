# aiopygismeteo

[![CI](https://github.com/monosans/aiopygismeteo/actions/workflows/ci.yml/badge.svg)](https://github.com/monosans/aiopygismeteo/actions/workflows/ci.yml)
[![PyPI Downloads](https://img.shields.io/pypi/dm/aiopygismeteo?logo=pypi)](https://pypi.org/project/aiopygismeteo/)

Асинхронная обёртка для [Gismeteo API](https://gismeteo.ru/api/).

Синхронная версия [здесь](https://github.com/monosans/pygismeteo).

## Установка

```bash
python -m pip install -U aiopygismeteo pygismeteo-base
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
