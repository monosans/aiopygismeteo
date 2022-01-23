# aiopygismeteo

[![Build Status](https://github.com/monosans/aiopygismeteo/workflows/test/badge.svg?branch=main&event=push)](https://github.com/monosans/aiopygismeteo/actions?query=workflow%3Atest)
[![codecov](https://codecov.io/gh/monosans/aiopygismeteo/branch/main/graph/badge.svg)](https://codecov.io/gh/monosans/aiopygismeteo)
[![Python Version](https://img.shields.io/pypi/pyversions/aiopygismeteo.svg)](https://pypi.org/project/aiopygismeteo/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/monosans/aiopygismeteo/blob/main/LICENSE)

Асинхронная обёртка для [Gismeteo.ru API](https://gismeteo.ru/api).

Синхронная версия [здесь](https://github.com/monosans/pygismeteo).

## Установка

```bash
python -m pip install -U aiopygismeteo
```

## Документация

Релизная версия - <https://aiopygismeteo.readthedocs.io>

Git версия - <https://aiopygismeteo.readthedocs.io/ru/latest>

## Пример, выводящий температуру в Москве сейчас

```python
import asyncio

from aiopygismeteo import Gismeteo


async def main():
    gm = Gismeteo()
    city_id = await gm.get_id_by_query("Москва")
    current = await gm.current(city_id)
    print(current.temperature.air.c)


asyncio.run(main())
```
