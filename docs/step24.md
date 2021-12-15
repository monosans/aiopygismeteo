# Функция step24

Данная функция позволяет получить прогноз погоды с шагом 24 часа.

## Аргументы

Принимает 2 обязательных аргумента:

- id - ID населённого пункта. О том, как получить ID по названию населённого пункта, см. [Поиск](search.md).
- days - на какое количество дней нужно получить прогноз (от 3 до 10).

и 3 необязательных аргумента:

- lang - язык. По умолчанию "ru".
- token - X-Gismeteo-Token, если используемый по умолчанию перестал работать.
- session - экземпляр aiohttp.ClientSession, если нужно использовать свой.

## Пример

Выводит температуру послезавтра.

```python
import asyncio

import aiopygismeteo


async def main():
    city_id = await aiopygismeteo.search.id_by_query("Москва")
    gm = await aiopygismeteo.step24(city_id, days=3)
    print(gm[2].temperature.air.c)


asyncio.run(main())
```
