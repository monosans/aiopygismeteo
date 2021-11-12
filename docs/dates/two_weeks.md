# Метод two_weeks()

Данный метод класса `Gismeteo` позволяет получать данные с вкладки ["2 недели"](https://gismeteo.ru/weather-moscow-4368/2-weeks/).

## Пример, выводящий температуру в Москве на 2 недели

```python
import asyncio

from aiopygismeteo import gismeteo


async def main():
    moscow = await gismeteo("https://gismeteo.ru/weather-moscow-4368/")
    two_weeks = await moscow.two_weeks()
    print(two_weeks.temperature)


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
| gusts           | Порывы, м/с                           |
| precipitation   | Сумма осадков, мм                     |
| temperature     | Средняя температура, °C               |
| wind_speed      | Скорость ветра, м/с                   |
| wind_direction  | Направление ветра                     |
| max_pressure    | Макс. давление, мм рт. ст.            |
| min_pressure    | Мин. давление, мм рт. ст.             |
| humidity        | Влажность, %                          |
| gm_activity     | Геомагнитная активность, Кп-индекс    |
