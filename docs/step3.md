# Атрибут step3

## Метод by_id

Погода с шагом 3 часа по ID географического объекта.

Принимает 2 обязательных аргумента:

- id (int ≥ 1): ID географического объекта. Получить можно через [Поиск](search.md).
- days (1 ≤ int ≤ 10): Количество дней.

и 1 необязательный именованный аргумент:

- as_list (bool): Вернуть `tuple[aiopygismeteo.models.step3.ModelItem, ...]` вместо `aiopygismeteo.models.step3.Model`. По умолчанию True.

## Метод by_coordinates

Погода с шагом 3 часа по координатам.

Принимает 3 обязательных аргумента:

- latitude (-90 ≤ int | float ≤ 90): Широта.
- longitude (-180 ≤ int | float ≤ 180): Долгота.
- days (1 ≤ int ≤ 10): Количество дней.

и 1 необязательный именованный аргумент:

- as_list (bool): Вернуть `tuple[aiopygismeteo.models.step3.ModelItem, ...]` вместо `aiopygismeteo.models.step3.Model`. По умолчанию True.

## Длина возвращаемого списка

За каждый день, указанный в аргументах, в возвращаемый tuple добавляется 8 элементов. Например, если days=3, tuple будет состоять из 8\*3=24 элементов.

## Пример

Выводит температуру в Москве послезавтра в 06:00 часов.

```python
import asyncio

import aiopygismeteo


async def main():
    gm = aiopygismeteo.Gismeteo(token="56b30cb255.3443075")
    search_results = await gm.search.by_query("Москва")
    city_id = search_results[0].id
    step3 = await gm.step3.by_id(city_id, days=3)
    print(step3[18].temperature.air.c)


asyncio.run(main())
```
