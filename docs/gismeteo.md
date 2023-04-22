# Класс Gismeteo

Всё взаимодействие с библиотекой осуществляется через класс Gismeteo:

```python
import aiopygismeteo

gm = aiopygismeteo.Gismeteo()
```

## Создание экземпляра класса Gismeteo

При инициализации класс Gismeteo принимает 3 необязательных аргумента:

- lang: Язык. По умолчанию "ru".
- token: X-Gismeteo-Token, если используемый по умолчанию перестал работать.
- session: Экземпляр aiohttp.ClientSession. Подробнее см. [Свой экземпляр aiohttp.ClientSession](session.md).
