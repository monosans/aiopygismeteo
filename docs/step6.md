# Атрибут step6

## Метод by_id

Погода с шагом 6 часов по ID географического объекта.

Принимает 2 обязательных аргумента:

- id (int ≥ 1): ID географического объекта. Получить можно через [Поиск](search.md).
- days (3 ≤ int ≤ 10): Количество дней.

и 1 необязательный именованный аргумент:

- as_list (bool): Вернуть `tuple[aiopygismeteo.models.step6.ModelItem, ...]` вместо `aiopygismeteo.models.step6.Model`. По умолчанию True.

## Метод by_coordinates

Погода с шагом 6 часов по координатам.

Принимает 3 обязательных аргумента:

- latitude (-90 ≤ int | float ≤ 90): Широта.
- longitude (-180 ≤ int | float ≤ 180): Долгота.
- days (3 ≤ int ≤ 10): Количество дней.

и 1 необязательный именованный аргумент:

- as_list (bool): Вернуть `tuple[aiopygismeteo.models.step6.ModelItem, ...]` вместо `aiopygismeteo.models.step6.Model`. По умолчанию True.

## Длина возвращаемого списка

За каждый день, указанный в аргументах, в возвращаемый список добавляется 4 элемента. Например, если days=3, список будет состоять из 4\*3=12 элементов.

## Пример

Выводит температуру в Москве послезавтра в 09:00 часов.

```python
import asyncio

import aiopygismeteo


async def main():
    gm = aiopygismeteo.Gismeteo(token="56b30cb255.3443075")
    search_results = await gm.search.by_query("Москва")
    city_id = search_results[0].id
    step6 = await gm.step6.by_id(city_id, days=3)
    print(step6[9].temperature.air.c)


asyncio.run(main())
```
