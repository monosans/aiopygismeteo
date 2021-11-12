# Метод month()

Данный метод класса `Gismeteo` позволяет получать данные с вкладки ["Месяц"](https://gismeteo.ru/weather-moscow-4368/month/).

## Пример, выводящий максимальную температуру в Москве на месяц

```python
import asyncio

from aiopygismeteo import gismeteo


async def main():
    moscow = await gismeteo("https://gismeteo.ru/weather-moscow-4368/")
    month = await moscow.month()
    print(month.max_temperature)


asyncio.run(main())
```

## Атрибуты

Атрибуты возвращаемого объекта имеют вид `{'день': 'значение'}`.

Полный список атрибутов:

| Атрибут         | Описание                              |
| --------------- | ------------------------------------- |
| status          | Ясно, пасмурно, сильный дождь и т. д. |
| max_temperature | Макс. температура, °C                 |
| min_temperature | Мин. температура, °C                  |
