# Основной раздел (класс Gismeteo)

Чтобы начать работу с библиотекой, импортируем функцию `gismeteo`:

```python
from aiopygismeteo import gismeteo
```

## Создание экземпляра класса Gismeteo

Функция `gismeteo` возвращает экземпляр класса `Gismeteo`. При вызове функции надо указать населённый пункт, погоду в котором нужно узнать.

Есть 2 способа указать населенный пункт:

1. Через ссылку (рекомендуемый способ):
   ```python
   moscow = await gismeteo("https://gismeteo.ru/weather-moscow-4368/")
   ```
   Ссылку также можно указывать без `https://gismeteo.ru/`.
2. Через название населённого пункта:
   ```python
   moscow = await gismeteo("Москва")
   ```

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

## Методы

Названия методов кликабельны и переносят на соответствующую часть документации. Ссылки в правом столбике ведут на соответствующую страницу на Gismeteo.ru.

| Метод                               | Описание                                                                    |
| ----------------------------------- | --------------------------------------------------------------------------- |
| [now()](dates/now.md)               | [Сейчас](https://gismeteo.ru/weather-moscow-4368-now/)                      |
| [today()](dates/today.md)           | [Сегодня](https://gismeteo.ru/weather-moscow-4368/)                         |
| [tomorrow()](dates/tomorrow.md)     | [Завтра](https://gismeteo.ru/weather-moscow-4368/tomorrow/)                 |
| [in3_days()](dates/in3_days.md)     | [Через 3 дня (послезавтра)](https://gismeteo.ru/weather-moscow-4368/3-day/) |
| [in4_days()](dates/in4_days.md)     | [Через 4 дня](https://gismeteo.ru/weather-moscow-4368/4-day/)               |
| [in5_days()](dates/in5_days.md)     | [Через 5 дней](https://gismeteo.ru/weather-moscow-4368/5-day/)              |
| [in6_days()](dates/in6_days.md)     | [Через 6 дней](https://gismeteo.ru/weather-moscow-4368/6-day/)              |
| [in7_days()](dates/in7_days.md)     | [Через 7 дней](https://gismeteo.ru/weather-moscow-4368/7-day/)              |
| [in8_days()](dates/in8_days.md)     | [Через 8 дней](https://gismeteo.ru/weather-moscow-4368/8-day/)              |
| [in9_days()](dates/in9_days.md)     | [Через 9 дней](https://gismeteo.ru/weather-moscow-4368/9-day/)              |
| [in10_days()](dates/in10_days.md)   | [Через 10 дней](https://gismeteo.ru/weather-moscow-4368/10-day/)            |
| [three_days()](dates/three_days.md) | [3 дня](https://gismeteo.ru/weather-moscow-4368/3-days/)                    |
| [ten_days()](dates/ten_days.md)     | [10 дней](https://gismeteo.ru/weather-moscow-4368/10-days/)                 |
| [two_weeks()](dates/two_weeks.md)   | [2 недели](https://gismeteo.ru/weather-moscow-4368/2-weeks/)                |
| [month()](dates/month.md)           | [Месяц](https://gismeteo.ru/weather-moscow-4368/month/)                     |
