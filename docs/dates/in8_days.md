# Метод in8_days()

Данный метод класса `Gismeteo` позволяет получать погоду [через 8 дней](https://gismeteo.ru/weather-moscow-4368/8-day/).

## Пример, выводящий температуру в Москве через 8 дней

```python
import asyncio

from aiopygismeteo import gismeteo


async def main():
    moscow = await gismeteo("https://gismeteo.ru/weather-moscow-4368/")
    in8_days = await moscow.in8_days()
    print(in8_days.temperature)


asyncio.run(main())
```

## Атрибуты

Атрибуты возвращаемого объекта идентичны атрибутам [Today](today.md).
