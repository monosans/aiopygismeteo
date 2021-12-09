# Исключения (exceptions)

При вызове функций `aiopygismeteo.by_name` или `aiopygismeteo.by_url` может возникнуть исключение `LocalityError`.

1. При использовании `by_name` исключение возникает, если указан несуществующий населённый пункт, например:
   ```python
   gm = await aiopygismeteo.by_name("алыфдаождваолыфволадф")
   ```
2. При использовании `by_url` исключение возникает, если количество ссылок не равно `1`, например:
   ```python
   gm = await aiopygismeteo.by_url("алыфдаождваолыфволадф")
   ```

## Пример обработки исключений

В этом примере пользователь вводит название населённого пункта, и программа выводит температуру на данный момент в указанном населённом пункте. Если пользователь введёт неверное название, он получит сообщение об этом.

```python
import asyncio

import aiopygismeteo
from aiopygismeteo.exceptions import LocalityError


async def main():
    locality = input("Название населённого пункта: ")
    try:
        gm = await aiopygismeteo.by_name(locality)
    except LocalityError:
        print("Населённый пункт не найден")
    else:
        now = await gm.now()
        print(now.temperature)


asyncio.run(main())
```
