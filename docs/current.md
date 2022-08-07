# Атрибут current

## Метод by_id

Текущая погода по ID географического объекта.

Принимает 1 аргумент:

- id (int) - ID географического объекта (получить можно через [Поиск](search.md)).

## Метод by_coordinates

Текущая погода по координатам.

Принимает 2 аргумента:

- latitude (float) - широта (от -90 до 90).
- longitude (float) - долгота (от -180 до 180).

## Возвращаемый объект

Оба метода возвращают `pygismeteo_base.models.current.Model`.

## Пример

Выводит температуру в Москве сейчас.

```python
import asyncio

from aiopygismeteo import Gismeteo


async def main():
    gismeteo = Gismeteo()
    search_results = await gismeteo.search.by_query("Москва")
    city_id = search_results[0].id
    current = await gismeteo.current.by_id(city_id)
    print(current.temperature.air.c)


asyncio.run(main())
```
