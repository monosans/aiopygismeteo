# Метод ten_days()

Данный метод класса `Gismeteo` позволяет получать данные с вкладки ["10 дней"](https://gismeteo.ru/weather-moscow-4368/10-days/).

## Пример, выводящий температуру в Москве на 10 дней

```python
import asyncio

from aiopygismeteo import gismeteo


async def main():
    moscow = await gismeteo("https://gismeteo.ru/weather-moscow-4368/")
    ten_days = await moscow.ten_days()
    print(ten_days.temperature)


asyncio.run(main())
```

## Атрибуты

Атрибуты возвращаемого объекта имеют вид `{'день': 'значение'}`.

Полный список атрибутов:

| Атрибут           | Описание                              |
| ----------------- | ------------------------------------- |
| status            | Ясно, пасмурно, сильный дождь и т. д. |
| max_temperature   | Макс. температура, °C                 |
| min_temperature   | Мин. температура, °C                  |
| precipitation     | Сумма осадков, мм                     |
| temperature       | Средняя температура, °C               |
| wind_speed        | Скорость ветра, м/с                   |
| wind_direction    | Направление ветра                     |
| gusts             | Порывы, м/с                           |
| max_pressure      | Макс. давление, мм рт. ст.            |
| min_pressure      | Мин. давление, мм рт. ст.             |
| humidity          | Влажность, %                          |
| gm_activity       | Геомагнитная активность, Кп-индекс    |
| ultraviolet_index | Ультрафиолетовый индекс, баллы        |
| falling_snow      | Выпадающий снег, см                   |
| snow_depth        | Высота снежного покрова, см           |
