# Атрибут step24

## Метод by_id

Погода с шагом 24 часа по ID географического объекта.

Принимает 2 обязательных аргумента:

- id (int ≥ 1): ID географического объект. Получить можно через [Поиск](search.md).
- days (3 ≤ int ≤ 10): Количество дней.

и 1 необязательный именованный аргумент:

- as_list (bool): Вернуть `list[aiopygismeteo.models.step24.ModelItem]` вместо `aiopygismeteo.models.step24.Model`. По умолчанию True.

## Метод by_coordinates

Погода с шагом 24 часа по координатам.

Принимает 3 обязательных аргумента:

- latitude (-90 ≤ float ≤ 90): Широта.
- longitude (-180 ≤ float ≤ 180): Долгота.
- days (3 ≤ int ≤ 10): Количество дней.

и 1 необязательный именованный аргумент:

- as_list (bool): Вернуть `list[aiopygismeteo.models.step24.ModelItem]` вместо `aiopygismeteo.models.step24.Model`. По умолчанию True.

## Пример

Выводит среднюю температуру в Москве послезавтра.

```python
import asyncio

import aiopygismeteo


async def main():
    gm = aiopygismeteo.Gismeteo()
    search_results = await gm.search.by_query("Москва")
    city_id = search_results[0].id
    step24 = await gm.step24.by_id(city_id, days=3)
    print(step24[2].temperature.air.avg.c)


asyncio.run(main())
```
