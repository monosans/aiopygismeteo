# Руководство

Примеры запускаются как есть, нужен только [токен](index.md). В примерах стоит образец токена, замените его своим. Пример с `base_url` требует ещё адрес вашего прокси.

## Найти город по названию

[`search.by_query`][aiopygismeteo.types.Search.by_query] ищет города, районы, страны и аэропорты. Если ничего не найдено, вернётся пустой кортеж.

```python
import asyncio

import aiopygismeteo


async def main() -> None:
    async with aiopygismeteo.Gismeteo(token="56b30cb255.3443075") as gismeteo:
        results = await gismeteo.search.by_query("Москва")

    for place in results:
        print(place.id, place.name, place.country.name)


asyncio.run(main())
```

`id` из результата нужен для запросов погоды по ID.

## Найти места рядом с точкой

[`search.by_coordinates`][aiopygismeteo.types.Search.by_coordinates] возвращает ближайшие к точке географические объекты, не больше `limit` (от 1 до 36).

```python
import asyncio

import aiopygismeteo


async def main() -> None:
    async with aiopygismeteo.Gismeteo(token="56b30cb255.3443075") as gismeteo:
        results = await gismeteo.search.by_coordinates(
            55.75222, 37.61556, limit=5
        )

    for place in results:
        print(place.name, place.distance)


asyncio.run(main())
```

## Определить город по IP

```python
import asyncio
from ipaddress import IPv4Address

import aiopygismeteo


async def main() -> None:
    async with aiopygismeteo.Gismeteo(token="56b30cb255.3443075") as gismeteo:
        place = await gismeteo.search.by_ip(IPv4Address("8.8.8.8"))

    print(place.id, place.name, place.country.name)


asyncio.run(main())
```

## Текущая погода

[`current.by_id`][aiopygismeteo.types.Current.by_id] принимает ID из поиска, а [`current.by_coordinates`][aiopygismeteo.types.Current.by_coordinates] принимает широту и долготу.

```python
import asyncio

import aiopygismeteo


async def main() -> None:
    async with aiopygismeteo.Gismeteo(token="56b30cb255.3443075") as gismeteo:
        current = await gismeteo.current.by_id(4368)  # Москва

    print(current.description.full)
    print("Температура:", current.temperature.air.c, "°C")
    print("Ощущается как:", current.temperature.comfort.c, "°C")
    print("Ветер:", current.wind.speed.m_s, "м/с")
    print("Влажность:", current.humidity.percent, "%")
    print("Давление:", current.pressure.mm_hg_atm, "мм рт. ст.")


asyncio.run(main())
```

Все поля ответа описаны в [`models.current.Model`][aiopygismeteo.models.current.Model].

## Прогноз по дням

[`step24`][aiopygismeteo.types.Step24] даёт прогноз на срок от 3 до 10 дней, по элементу на сутки с суточными минимумами и максимумами.

```python
import asyncio

import aiopygismeteo


async def main() -> None:
    async with aiopygismeteo.Gismeteo(token="56b30cb255.3443075") as gismeteo:
        forecast = await gismeteo.step24.by_id(4368, days=3)

    for day in forecast:
        air = day.temperature.air
        print(day.date.local, air.min.c, air.max.c, day.description.full)


asyncio.run(main())
```

## Прогноз по часам

[`step3`][aiopygismeteo.types.Step3] даёт прогноз с шагом 3 часа на срок от 1 до 10 дней, а [`step6`][aiopygismeteo.types.Step6] с шагом 6 часов на срок от 3 до 10 дней. Ответы у них устроены одинаково.

```python
import asyncio

import aiopygismeteo


async def main() -> None:
    async with aiopygismeteo.Gismeteo(token="56b30cb255.3443075") as gismeteo:
        forecast = await gismeteo.step3.by_id(4368, days=1)

    for item in forecast:
        print(item.date.local, item.temperature.air.c, item.description.full)


asyncio.run(main())
```

## Несколько запросов одновременно

Запросы через один клиент можно выполнять параллельно с [`asyncio.gather`][asyncio.gather].

```python
import asyncio

import aiopygismeteo


async def main() -> None:
    async with aiopygismeteo.Gismeteo(token="56b30cb255.3443075") as gismeteo:
        current, forecast = await asyncio.gather(
            gismeteo.current.by_id(4368), gismeteo.step24.by_id(4368, days=3)
        )

    print(current.description.full)
    for day in forecast:
        print(day.date.local, day.description.full)


asyncio.run(main())
```

## Облачность, осадки и ветер словами

У значений облачности, осадков, направления ветра и других [перечислений][aiopygismeteo.models.enums] есть поле `description` с описанием на русском и английском.

```python
import asyncio

import aiopygismeteo


async def main() -> None:
    async with aiopygismeteo.Gismeteo(token="56b30cb255.3443075") as gismeteo:
        current = await gismeteo.current.by_id(4368)

    print(current.cloudiness.type.description.ru)
    print(current.precipitation.type.description.ru)
    print(current.gm.description.en)
    if current.wind.direction.scale_8 is not None:
        print(current.wind.direction.scale_8.description.ru)


asyncio.run(main())
```

## Язык ответов

По умолчанию названия и описания приходят на русском. Другой язык задаёт [`Lang`][aiopygismeteo.types.Lang].

```python
import asyncio

import aiopygismeteo


async def main() -> None:
    async with aiopygismeteo.Gismeteo(
        token="56b30cb255.3443075", lang=aiopygismeteo.types.Lang.EN
    ) as gismeteo:
        current = await gismeteo.current.by_id(4368)

    print(current.description.full)


asyncio.run(main())
```

## Таймауты и своя HTTP-сессия

Своя [`aiohttp.ClientSession`][aiohttp.ClientSession] нужна, чтобы задать таймауты или прокси. По умолчанию общий таймаут 60 секунд, на подключение 5 секунд.

```python
import asyncio

import aiohttp

import aiopygismeteo


async def main() -> None:
    async with aiohttp.ClientSession(
        timeout=aiohttp.ClientTimeout(total=10, connect=3)
    ) as session:
        gismeteo = aiopygismeteo.Gismeteo(
            token="56b30cb255.3443075", session=session
        )
        current = await gismeteo.current.by_id(4368)

    print(current.description.full)


asyncio.run(main())
```

!!! warning

    [`Gismeteo.close`][aiopygismeteo.Gismeteo.close] и выход из `async with aiopygismeteo.Gismeteo(...)` закрывают и переданную сессию. Если она нужна дальше, не используйте `Gismeteo` как контекстный менеджер.

## Другой адрес API

Параметр `base_url` пригодится, если перед API стоит ваш прокси. Замените `https://api.example.com/v2` в примере его адресом. По умолчанию используется `https://api.gismeteo.net/v2`.

```python
import asyncio

import pydantic

import aiopygismeteo


async def main() -> None:
    async with aiopygismeteo.Gismeteo(
        token="56b30cb255.3443075",
        base_url=pydantic.AnyHttpUrl("https://api.example.com/v2"),
    ) as gismeteo:
        current = await gismeteo.current.by_id(4368)

    print(current.description.full)


asyncio.run(main())
```

## Обработка ошибок

Если API ответил кодом ошибки, поднимается [`aiohttp.ClientResponseError`][aiohttp.ClientResponseError]. При сбое сети поднимается [`aiohttp.ClientError`][aiohttp.ClientError], при таймауте [`TimeoutError`][TimeoutError]. Аргументы вне допустимых границ и ответ неожиданной формы приводят к [`pydantic.ValidationError`][pydantic_core.ValidationError].

```python
import asyncio

import aiohttp
import pydantic

import aiopygismeteo


async def main() -> None:
    async with aiopygismeteo.Gismeteo(token="56b30cb255.3443075") as gismeteo:
        try:
            forecast = await gismeteo.step24.by_id(4368, days=10)
        except aiohttp.ClientResponseError as e:
            print("Ошибка API:", e.status)
        except (aiohttp.ClientError, TimeoutError) as e:
            print("Сеть недоступна:", e)
        except pydantic.ValidationError as e:
            print("Неверные данные:", e)
        else:
            print(len(forecast), "дней")


asyncio.run(main())
```

## Аннотации типов

Модели ответов лежат в `aiopygismeteo.models`, например [`models.current.Model`][aiopygismeteo.models.current.Model]. Типы аргументов лежат в `aiopygismeteo.types`, например [`LocalityID`][aiopygismeteo.types.LocalityID]. Модели неизменяемые и хешируемые.

```python
import asyncio

import aiopygismeteo


def summary(weather: aiopygismeteo.models.current.Model) -> str:
    return f"{weather.temperature.air.c} °C, {weather.description.full}"


async def fetch(city_id: aiopygismeteo.types.LocalityID) -> str:
    async with aiopygismeteo.Gismeteo(token="56b30cb255.3443075") as gismeteo:
        return summary(await gismeteo.current.by_id(city_id))


print(asyncio.run(fetch(4368)))
```
