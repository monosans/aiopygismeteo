# Функция current

Данная функция позволяет получить текущую погоду.

## Аргументы

Принимает 1 обязательный аргумент:

- id - ID населённого пункта. О том, как получить ID по названию населённого пункта, см. [Поиск](search.md).

и 3 необязательных аргумента:

- lang - язык. По умолчанию "ru".
- token - X-Gismeteo-Token, если используемый по умолчанию перестал работать.
- session - экземпляр aiohttp.ClientSession, если нужно использовать свой.

## Пример

Выводит текущую погоду в населённом пункте с ID 4368 (Москва).

```python
import asyncio

import aiopygismeteo


async def main():
    city_id = await aiopygismeteo.search.id_by_query("Москва")
    gm = await aiopygismeteo.current(city_id)
    print(gm.temperature.air.c)


asyncio.run(main())
```
