# Метод in9_days()

Данный метод класса `Gismeteo` позволяет получать погоду [через 9 дней](https://gismeteo.ru/weather-moscow-4368/9-day/).

## Пример, выводящий температуру в Москве через 9 дней

```python
import asyncio

import aiopygismeteo


async def main():
    moscow = await aiopygismeteo.by_url(
        "https://gismeteo.ru/weather-moscow-4368/"
    )
    in9_days = await moscow.in9_days()
    print(in9_days.temperature)


asyncio.run(main())
```

## Атрибуты

Атрибуты возвращаемого объекта идентичны атрибутам [Today](today.md).
