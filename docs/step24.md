# Метод step24

Данный метод позволяет получить прогноз погоды с шагом 24 часа.

## Аргументы

Принимает 2 обязательных аргумента:

- id - ID населённого пункта. О том, как получить ID по названию населённого пункта, см. [Метод get_id_by_query](get_id_by_query.md).
- days - на какое количество дней нужно получить прогноз (от 3 до 10).

## Пример

Выводит температуру в Москве послезавтра.

```python
import asyncio

from aiopygismeteo import Gismeteo


async def main():
    gm = Gismeteo()
    city_id = await gm.get_id_by_query("Москва")
    step24 = await gm.step24(city_id, days=3)
    print(step24[2].temperature.air.c)


asyncio.run(main())
```
