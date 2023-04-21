# Свой экземпляр aiohttp.ClientSession

Классу `Gismeteo` можно передать экземпляр `aiohttp.ClientSession`.

Если его не передать, то для каждого запроса будет создаваться новый `aiohttp.ClientSession`.

## Пример

Выводит текущую температуру в географическом объекте с ID 4368 (Москва), используя свой экземпляр `aiohttp.ClientSession`.

```python
import asyncio

import aiopygismeteo
from aiohttp import ClientSession


async def main():
    async with ClientSession() as session:
        gm = aiopygismeteo.Gismeteo(session=session)
        current = await gm.current.by_id(4368)
    print(current.temperature.air.c)


asyncio.run(main())
```
