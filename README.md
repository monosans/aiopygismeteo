# aiopygismeteo

[![CI](https://github.com/monosans/aiopygismeteo/actions/workflows/ci.yml/badge.svg)](https://github.com/monosans/aiopygismeteo/actions/workflows/ci.yml)
[![Downloads](https://static.pepy.tech/badge/aiopygismeteo)](https://pepy.tech/project/aiopygismeteo)

Асинхронная обёртка для [Gismeteo API](https://gismeteo.ru/api/).

Синхронная версия [здесь](https://github.com/monosans/pygismeteo).

## Разработка приостановлена

Для использования библиотеки нужен API токен, который можно запросить по электронной почте [b2b@gismeteo.ru](mailto:b2b@gismeteo.ru).

В настоящее время у разработчика отсутствует API токен, что делает невозможными тестирование и дальнейшую разработку.

Если вам нужна погодная библиотека без API токена, можете рассмотреть <https://github.com/monosans/aiopywttr>.

## Установка

```bash
pip install -U aiopygismeteo pygismeteo-base
```

## Документация

<https://aiopygismeteo.readthedocs.io>

## Пример

```python
async with aiopygismeteo.Gismeteo(token="56b30cb255.3443075") as gismeteo:
    search_results = await gismeteo.search.by_query("Москва")
    city_id = search_results[0].id
    current = await gismeteo.current.by_id(city_id)
print(current)
```

## License / Лицензия

[MIT](https://github.com/monosans/aiopygismeteo/blob/main/LICENSE)
