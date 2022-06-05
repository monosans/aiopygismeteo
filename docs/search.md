# Атрибут search

## Метод by_query

Поиск по строке.

Принимает 1 аргумент:

- query (str) - город, район, область, страна или аэропорт.

Возвращает `List[pygismeteo_base.models.search_by_query.ModelItem]`.

## Метод by_coordinates

Поиск по координатам.

Принимает 2 обязательных аргумента:

- latitude (float) - широта (от -90 до 90).
- longitude (float) - долгота (от -180 до 180).

и 1 необязательный:

- limit (int) - ограничение количества (от 1 до 36).

Возвращает `List[pygismeteo_base.models.search_by_coordinates.ModelItem]`.

## Метод by_ip

Поиск по IP-адресу.

Принимает 1 аргумент:

ip (str) - IP-адрес.

Возвращает `pygismeteo_base.models.search_by_ip.Model`.

## Пример

Выводит ID Москвы.

```python
import asyncio

from aiopygismeteo import Gismeteo


async def main():
    gm = Gismeteo()
    search_results = await gm.search.by_query("Москва")
    city_id = search_results[0].id
    print(city_id)


asyncio.run(main())
```
