# Получение ID населённого пункта по названию

При поиске может возникнуть исключение `LocalityNotFound`. Подробнее см. [Исключения](exceptions.md)

В этом примере `city_id` - ID Москвы.

```python
import asyncio

import aiopygismeteo


async def main():
    city_id = await aiopygismeteo.search.id_by_query("Москва")
    gm = await aiopygismeteo.current(city_id)
    print(gm.temperature.air.c)


asyncio.run(main())
```
