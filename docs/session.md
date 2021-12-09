# Свой экземпляр aiohttp.ClientSession

Данный пример выводит температуру в Москве сегодня.

```python
import asyncio

import aiopygismeteo
from aiohttp import ClientSession


async def main():
    async with ClientSession() as s:
        moscow = await aiopygismeteo.by_url(
            "https://gismeteo.ru/weather-moscow-4368/", session=s
        )
        today = await moscow.today()
    print(today.temperature)


asyncio.run(main())
```
