# aiopygismeteo

[![Build Status](https://github.com/monosans/aiopygismeteo/workflows/test/badge.svg?branch=main&event=push)](https://github.com/monosans/aiopygismeteo/actions?query=workflow%3Atest)
[![codecov](https://codecov.io/gh/monosans/aiopygismeteo/branch/main/graph/badge.svg)](https://codecov.io/gh/monosans/aiopygismeteo)
[![Python Version](https://img.shields.io/pypi/pyversions/aiopygismeteo.svg)](https://pypi.org/project/aiopygismeteo/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/monosans/aiopygismeteo/blob/main/LICENSE)

Асинхронная обёртка для [Gismeteo.ru](https://gismeteo.ru).

Синхронная версия [здесь](https://github.com/monosans/pygismeteo).

## Установка

```sh
pip install -U aiopygismeteo
```

## Документация

Для текущей релизной версии - https://aiopygismeteo.readthedocs.io

Для git версии - https://aiopygismeteo.readthedocs.io/ru/latest

## Пример, выводящий температуру в Москве сейчас

```python
import asyncio

import aiopygismeteo


async def main():
    moscow = await aiopygismeteo.by_name("Москва")
    now = await moscow.now()
    print(now.temperature)


asyncio.run(main())
```
