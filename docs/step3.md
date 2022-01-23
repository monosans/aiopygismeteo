# Метод step3

Данный метод позволяет получить прогноз погоды с шагом 3 часа.

## Аргументы

Принимает 2 обязательных аргумента:

- id - ID населённого пункта. О том, как получить ID по названию населённого пункта, см. [Метод get_id_by_query](get_id_by_query.md).
- days - на какое количество дней нужно получить прогноз (от 1 до 10). За каждый день в возвращаемый список добавляется 8 элементов. Например, если days=3, то список будет состоять из 8\*3=24 элементов.

## Пример

Выводит температуру в Москве послезавтра в 06:00 часов.

```python
import asyncio

from aiopygismeteo import Gismeteo


async def main():
    gm = Gismeteo()
    city_id = await gm.get_id_by_query("Москва")
    step3 = await gm.step3(city_id, days=3)
    print(step3[18].temperature.air.c)


asyncio.run(main())
```
