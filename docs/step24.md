# Атрибут step24

## Метод by_id

Погода с шагом 24 часа по ID географического объекта.

Принимает 2 аргумента:

- id (int) - ID географического объекта (получить можно через [Поиск](search.md))
- days (int) - количество дней (от 3 до 10).

## Метод by_coordinates

Погода с шагом 24 часа по координатам.

Принимает 3 аргумента:

- latitude (float) - широта (от -90 до 90).
- longitude (float) - долгота (от -180 до 180).
- days (int) - количество дней (от 3 до 10).

## Возвращаемый объект

Оба метода возвращают `List[pygismeteo_base.models.step24.ModelItem]`.

## Пример

Выводит среднюю температуру в Москве послезавтра.

```python
import asyncio

from aiopygismeteo import Gismeteo


async def main():
    gm = Gismeteo()
    search_results = await gm.search.by_query("Москва")
    city_id = search_results[0].id
    step24 = await gm.step24.by_id(city_id, days=3)
    print(step24[2].temperature.air.avg.c)


asyncio.run(main())
```
