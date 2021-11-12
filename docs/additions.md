# Дополнительные возможности

## Свой экземпляр aiohttp.ClientSession

Данный пример выводит температуру в Москве сегодня.

```python
import asyncio

from aiohttp import ClientSession
from aiopygismeteo import gismeteo


async def main():
    async with ClientSession() as s:
        moscow = await gismeteo(
            "https://gismeteo.ru/weather-moscow-4368/", session=s
        )
        today = await moscow.today()
    print(today.temperature)


asyncio.run(main())
```
