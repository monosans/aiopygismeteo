# Атрибут search

## Метод by_query

Поиск по строке.

Принимает 1 обязательный аргумент:

- query (str): Город, район, область, страна или аэропорт.

и 1 необязательный именованный аргумент:

- as_list (bool): Вернуть `tuple[aiopygismeteo.models.search_by_query.ModelItem, ...]` вместо `aiopygismeteo.models.search_by_query.Model`. По умолчанию True.

## Метод by_coordinates

Поиск по координатам.

Принимает 3 обязательных аргумента:

- latitude (-90 ≤ float ≤ 90): Широта.
- longitude (-180 ≤ float ≤ 180): Долгота.
- limit (1 ≤ int ≤ 36): Ограничение количества результатов.

и 1 необязательный именованный аргумент:

- as_list (bool): Вернуть `tuple[aiopygismeteo.models.search_by_coordinates.ModelItem, ...]` вместо `aiopygismeteo.models.search_by_coordinates_Model`. По умолчанию True.

## Метод by_ip

Поиск по IPv4-адресу.

Принимает 1 аргумент:

- ip (ipaddress.IPv4Address | str): IPv4-адрес.

Возвращает `aiopygismeteo.models.search_by_ip.Model`.

## Пример

Выводит ID Москвы.

```python
import asyncio

import aiopygismeteo


async def main():
    gm = aiopygismeteo.Gismeteo(token="56b30cb255.3443075")
    search_results = await gm.search.by_query("Москва")
    city_id = search_results[0].id
    print(city_id)


asyncio.run(main())
```
