# Исключения (exceptions)

При вызове функции `gismeteo` могут возникнуть 2 вида исключений:

1. `InvalidLocalityID` - возникает при передаче неверной ссылки на населённый пункт, например:
   ```python
   gm = await aiopygismeteo.by_url("https://gismeteo.ru/moscow-weather-4368/")
   ```
   Правильно должно быть так:
   ```python
   gm = await aiopygismeteo.by_url("https://gismeteo.ru/weather-moscow-4368/")
   ```
2. `LocalityNotFound` - возникает при указании названия населённого пункта, который отсутствует в Gismeteo.
   ```python
   gm = await aiopygismeteo.by_name("алыфдаождваолыфволадф")
   ```
   В этом случае будет вызвано исключение.

## Пример обработки исключений

В данном примере пользователь вводит название населённого пункта или ссылку на него, и программа выводит температуру на данный момент в указанном населённом пункте. Если пользователь введёт неверное значение, он получит сообщение об этом.

```python
import aiopygismeteo
from aiopygismeteo.exceptions import InvalidLocalityID, LocalityNotFound


async def main():
    locality = input("Название населённого пункта или ссылка на gismeteo.ru: ")
    try:
        gm = await aiopygismeteo.by_name(locality)
    except LocalityNotFound:
        print("Населённый пункт не найден")
    except InvalidLocalityID:
        print("Неправильная ссылка на gismeteo.ru")
    else:
        now = await gm.now()
        print(now.temperature)


asyncio.run(main())
```
