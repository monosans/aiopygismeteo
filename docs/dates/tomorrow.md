# Метод tomorrow()

Данный метод класса `Gismeteo` позволяет получать данные с вкладки ["tomorrow"](https://gismeteo.ru/weather-moscow-4368/tomorrow/).

## Пример, выводящий температуру в Москве завтра

```python
import asyncio

import aiopygismeteo


async def main():
    moscow = await aiopygismeteo.by_url(
        "https://gismeteo.ru/weather-moscow-4368/"
    )
    tomorrow = await moscow.tomorrow()
    print(tomorrow.temperature)


asyncio.run(main())
```

## Атрибуты

Атрибуты возвращаемого объекта идентичны атрибутам [Today](today.md).
