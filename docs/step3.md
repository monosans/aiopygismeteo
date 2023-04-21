# Атрибут step3

## Метод by_id

Погода с шагом 3 часа по ID географического объекта.

Принимает 2 аргумента:

- id (int) - ID географического объекта (получить можно через [Поиск](search.md)).
- days (int) - количество дней (от 1 до 10).

## Метод by_coordinates

Погода с шагом 3 часа по координатам.

Принимает 3 аргумента:

- latitude (float) - широта (от -90 до 90).
- longitude (float) - долгота (от -180 до 180).
- days (int) - количество дней (от 1 до 10).

## Возвращаемый объект

Оба метода возвращают `list[aiopygismeteo.models.step3.ModelItem]`. За каждый день, указанный в аргументах, в возвращаемый список добавляется 8 элементов. Например, если days=3, список будет состоять из 8\*3=24 элементов.

## Пример

Выводит температуру в Москве послезавтра в 06:00 часов.

```python
import asyncio

import aiopygismeteo


async def main():
    gm = aiopygismeteo.Gismeteo()
    search_results = await gm.search.by_query("Москва")
    city_id = search_results[0].id
    step3 = await gm.step3.by_id(city_id, days=3)
    print(step3[18].temperature.air.c)


asyncio.run(main())
```
