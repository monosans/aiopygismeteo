# Метод current

Данный метод позволяет получить текущую погоду.

## Аргументы

Принимает 1 обязательный аргумент:

- id - ID населённого пункта. О том, как получить ID по названию населённого пункта, см. [Метод get_id_by_query](get_id_by_query.md).

## Пример

Выводит температуру в Москве сейчас.

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
