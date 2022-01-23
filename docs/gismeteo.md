# Класс Gismeteo

Чтобы начать работу с библиотекой, делаем следующий импорт:

```python
from aiopygismeteo import Gismeteo
```

## Создание экземпляра класса Gismeteo

При инициализации класс Gismeteo принимает 3 необязательных аргумента:

- lang - язык. По умолчанию "ru".
- token - X-Gismeteo-Token, если используемый по умолчанию перестал работать.
- session - экземпляр aiohttp.ClientSession, если нужно использовать свой. Иначе для каждого запроса будет создаваться новый экземпляр aiohttp.ClientSession.
