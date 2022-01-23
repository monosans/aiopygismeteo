# Исключения (exceptions)

При вызове метода `get_id_by_query` может возникнуть исключение `LocalityNotFound`, если населённый пункт не был найден.

Пример, при котором возникнет исключение:

```python
gm = Gismeteo()
city_id = await gm.get_id_by_query("алыфдаождваолыфволадф")
```

## Пример

В этом примере пользователь вводит название населённого пункта, и программа выводит температуру на данный момент в введённом населённом пункте. Если пользователь введёт неверное название, он получит сообщение об этом.

```python
import asyncio

from aiopygismeteo import Gismeteo, LocalityNotFound


async def main():
    locality = input("Название населённого пункта: ")
    gm = Gismeteo()
    try:
        city_id = await gm.get_id_by_query(locality)
    except LocalityNotFound:
        print("Населённый пункт не найден")
        return
    current = await gm.current(city_id)
    print(current.temperature.air.c)


asyncio.run(main())
```
