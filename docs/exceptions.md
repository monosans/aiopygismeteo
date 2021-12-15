# Исключения (exceptions)

При вызове функции `aiopygismeteo.search.id_by_query` может возникнуть исключение `LocalityNotFound`, если населённый пункт не был найден.

Пример, при котором возникнет исключение:

```python
city_id = await aiopygismeteo.search.id_by_query("алыфдаождваолыфволадф")
```

## Пример обработки исключений

В этом примере пользователь вводит название населённого пункта, и программа выводит температуру на данный момент в введённом населённом пункте. Если пользователь введёт неверное название, он получит сообщение об этом.

```python
import asyncio

import aiopygismeteo
from aiopygismeteo.exceptions import LocalityNotFound


async def main():
    locality = input("Название населённого пункта: ")
    try:
        city_id = await aiopygismeteo.search.id_by_query(locality)
    except LocalityNotFound:
        print("Населённый пункт не найден")
    else:
        gm = await aiopygismeteo.current(city_id)
        print(gm.temperature.air.c)


asyncio.run(main())
```
