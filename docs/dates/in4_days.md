# Метод in4_days()

Данный метод класса `Gismeteo` позволяет получать погоду [через 4 дня](https://gismeteo.ru/weather-moscow-4368/4-day/).

## Пример, выводящий температуру в Москве через 4 дня

```python
import asyncio

import aiopygismeteo


async def main():
    moscow = await aiopygismeteo.by_url(
        "https://gismeteo.ru/weather-moscow-4368/"
    )
    in4_days = await moscow.in4_days()
    print(in4_days.temperature)


asyncio.run(main())
```

## Атрибуты

Атрибуты возвращаемого объекта идентичны атрибутам [Today](today.md).
