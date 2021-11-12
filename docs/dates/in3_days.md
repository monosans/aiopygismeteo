# Метод in3_days()

Данный метод класса `Gismeteo` позволяет получать погоду [через 3 дня (послезавтра)](https://gismeteo.ru/weather-moscow-4368/3-day/).

## Пример, выводящий температуру в Москве через 3 дня

```python
import asyncio

from aiopygismeteo import gismeteo


async def main():
    moscow = await gismeteo("https://gismeteo.ru/weather-moscow-4368/")
    in3_days = await moscow.in3_days()
    print(in3_days.temperature)


asyncio.run(main())
```

## Атрибуты

Атрибуты возвращаемого объекта идентичны атрибутам [Today](today.md).
