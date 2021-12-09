# Метод three_days()

Данный метод класса `Gismeteo` позволяет получать данные с вкладки ["3 дня"](https://gismeteo.ru/weather-moscow-4368/3-days/).

## Пример, выводящий температуру в Москве на 3 дня

```python
import asyncio

import aiopygismeteo


async def main():
    moscow = await aiopygismeteo.by_url(
        "https://gismeteo.ru/weather-moscow-4368/"
    )
    three_days = await moscow.three_days()

    # Ночь
    night = three_days.night
    print(night.temperature)

    # Утро
    morning = three_days.morning
    print(morning.temperature)

    # День
    afternoon = three_days.afternoon
    print(afternoon.temperature)

    # Вечер
    evening = three_days.evening
    print(evening.temperature)


asyncio.run(main())
```

## Атрибуты

Данный метод класса `Gismeteo` особенный. Атрибуты возвращаемого объекта сами являются объектами:

| Атрибут   | Описание |
| --------- | -------- |
| night     | Ночь     |
| morning   | Утро     |
| afternoon | День     |
| evening   | Вечер    |

Каждый из этих 4 атрибутов, в свою очередь, имеет следующие атрибуты вида `{'день': 'значение'}`:

| Атрибут           | Описание                              |
| ----------------- | ------------------------------------- |
| status            | Ясно, пасмурно, сильный дождь и т. д. |
| temperature       | Средняя температура, °C               |
| gusts             | Порывы, м/с                           |
| precipitation     | Сумма осадков, мм                     |
| wind_speed        | Скорость ветра, м/с                   |
| wind_direction    | Направление ветра                     |
| falling_snow      | Выпадающий снег, см                   |
| snow_depth        | Высота снежного покрова, см           |
| pressure          | Давление, мм рт. ст.                  |
| humidity          | Влажность, %                          |
| ultraviolet_index | Ультрафиолетовый индекс, баллы        |
| gm_activity       | Геомагнитная активность, Кп-индекс    |
