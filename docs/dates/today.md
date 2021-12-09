# Метод today()

Данный метод класса `Gismeteo` позволяет получать данные с вкладки ["Сегодня"](https://gismeteo.ru/weather-moscow-4368/today/).

## Пример, выводящий температуру в Москве сегодня

```python
import asyncio

import aiopygismeteo


async def main():
    moscow = await aiopygismeteo.by_url(
        "https://gismeteo.ru/weather-moscow-4368/"
    )
    today = await moscow.today()
    print(today.temperature)


asyncio.run(main())
```

## Атрибуты

Атрибуты возвращаемого объекта имеют вид `{'время': 'значение'}`.

Полный список атрибутов:

| Атрибут           | Описание                              |
| ----------------- | ------------------------------------- |
| status            | Ясно, пасмурно, сильный дождь и т. д. |
| temperature       | Температура, °C                       |
| wind_speed        | Скорость ветра, м/с                   |
| precipitation     | Сумма осадков, мм                     |
| wind_direction    | Направление ветра                     |
| falling_snow      | Выпадающий снег, см                   |
| snow_depth        | Высота снежного покрова, см           |
| road_condition    | Погода на дорогах                     |
| pressure          | Давление, мм рт. ст.                  |
| humidity          | Влажность, %                          |
| visibility        | Видимость, км                         |
| ultraviolet_index | Ультрафиолетовый индекс, баллы        |
| gm_activity       | Геомагнитная активность, Кп-индекс    |
