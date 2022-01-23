# Метод get_id_by_query

Вспомогательный метод, позволяющий получить ID по названию населённого пункта.

При поиске может возникнуть исключение `LocalityNotFound`. Подробнее см. [Исключения](exceptions.md).

## Пример

В этом примере `city_id` - ID Москвы.

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
