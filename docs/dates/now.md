# Метод now()

Данный метод класса `Gismeteo` позволяет получать данные с вкладки ["Сейчас"](https://gismeteo.ru/weather-moscow-4368/now/).

## Пример, выводящий температуру в Москве сейчас

```python
import asyncio

from aiopygismeteo import gismeteo


async def main():
    moscow = await gismeteo("https://gismeteo.ru/weather-moscow-4368/")
    now = await moscow.now()
    print(now.temperature)


asyncio.run(main())
```

## Атрибуты

Атрибуты возвращаемого объекта имеют тип `str`.

Полный список атрибутов:

| Атрибут        | Описание                              |
| -------------- | ------------------------------------- |
| status         | Ясно, пасмурно, сильный дождь и т. д. |
| temperature    | Температура, °C                       |
| real_feel      | Температура по ощущению, °C           |
| sunrise        | Заход                                 |
| sunset         | Восход                                |
| wind_speed     | Скорость ветра, м/с                   |
| wind_direction | Направление ветра                     |
| pressure       | Давление, мм рт. ст.                  |
| humidity       | Влажность, %                          |
| gm_activity    | Геомагнитная активность, Кп-индекс    |
| water          | Температура воды, °C                  |
