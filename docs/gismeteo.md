# Класс Gismeteo

Всё взаимодействие с библиотекой осуществляется через класс Gismeteo:

```python
import aiopygismeteo

gm = aiopygismeteo.Gismeteo(token="56b30cb255.3443075")
```

## Создание экземпляра класса Gismeteo

При инициализации класс Gismeteo принимает 1 обязательный именованный аргумент:

- token: X-Gismeteo-Token. Запросить можно по электронной почте <mailto:b2b@gismeteo.ru>.

и 2 необязательных именованных аргумента:

- lang: Язык. По умолчанию "ru".
- session: Экземпляр aiohttp.ClientSession. Подробнее см. [Свой экземпляр aiohttp.ClientSession](session.md).
