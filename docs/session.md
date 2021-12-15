# Свой экземпляр aiohttp.ClientSession

Данный пример выводит текущую температуру в населённом пункте с ID 4368 (Москва).

```python
import asyncio

import aiopygismeteo
from aiohttp import ClientSession


async def main():
    async with ClientSession() as s:
        gm = await aiopygismeteo.current(4368, session=s)
    print(gm.temperature.air.c)


asyncio.run(main())
```
