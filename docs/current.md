# Атрибут current

## Метод by_id

Текущая погода по ID географического объекта.

Принимает 1 аргумент:

- id (int ≥ 1): ID географического объект. Получить можно через [Поиск](search.md).

Возвращает `aiopygismeteo.models.current.Model`.

## Метод by_coordinates

Текущая погода по координатам.

Принимает 2 аргумента:

- latitude (-90 ≤ float ≤ 90): Широта.
- longitude (-180 ≤ float ≤ 180): Долгота.

Возвращает `aiopygismeteo.models.current.Model`.

## Пример

Выводит температуру в Москве сейчас.

```python
import asyncio

import aiopygismeteo


async def main():
    gm = aiopygismeteo.Gismeteo()
    search_results = await gm.search.by_query("Москва")
    city_id = search_results[0].id
    current = await gm.current.by_id(city_id)
    print(current.temperature.air.c)


asyncio.run(main())
```
