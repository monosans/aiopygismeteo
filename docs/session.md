# Свой экземпляр aiohttp.ClientSession

Классу `Gismeteo` можно передать экземпляр `aiohttp.ClientSession`.

Если его не передать, то для каждого запроса будет создаваться новый `aiohttp.ClientSession`, что понижает производительность.

## Пример

Выводит текущую температуру в географическом объекте с ID 4368 (Москва), используя свой экземпляр `aiohttp.ClientSession`.

```python
import asyncio

from aiohttp import ClientSession
from aiopygismeteo import Gismeteo


async def main():
    async with ClientSession() as s:
        gm = Gismeteo(session=s)
        current = await gm.current.by_id(4368)
    print(current.temperature.air.c)


asyncio.run(main())
```
