# Метод in5_days()

Данный метод класса `Gismeteo` позволяет получать погоду [через 5 дней](https://gismeteo.ru/weather-moscow-4368/5-day/).

## Пример, выводящий температуру в Москве через 5 дней

```python
import asyncio

import aiopygismeteo


async def main():
    moscow = await aiopygismeteo.by_url(
        "https://gismeteo.ru/weather-moscow-4368/"
    )
    in5_days = await moscow.in5_days()
    print(in5_days.temperature)


asyncio.run(main())
```

## Атрибуты

Атрибуты возвращаемого объекта идентичны атрибутам [Today](today.md).
