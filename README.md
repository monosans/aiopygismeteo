# aiopygismeteo

[![Build Status](https://github.com/monosans/aiopygismeteo/workflows/test/badge.svg?branch=main&event=push)](https://github.com/monosans/aiopygismeteo/actions?query=workflow%3Atest)
[![codecov](https://codecov.io/gh/monosans/aiopygismeteo/branch/main/graph/badge.svg)](https://codecov.io/gh/monosans/aiopygismeteo)
[![Python Version](https://img.shields.io/pypi/pyversions/aiopygismeteo.svg)](https://pypi.org/project/aiopygismeteo/)

Асинхронная обёртка для [Gismeteo.ru](https://gismeteo.ru).

Синхронная версия [здесь](https://github.com/monosans/pygismeteo).

## Установка

```sh
python -m pip install -U aiopygismeteo
```

## Документация

https://aiopygismeteo.readthedocs.io

## Пример, выводящий температуру в Москве сейчас

```python
import asyncio

from aiopygismeteo import gismeteo


async def main():
    moscow = await gismeteo("Москва")
    now = await moscow.now()
    print(now.temperature)


asyncio.run(main())
```

## License / Лицензия

[MIT](LICENSE)
