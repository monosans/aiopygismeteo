# Типизация

Для типизации вашего кода надо импортировать `pygismeteo_base`:

```python
import pygismeteo_base
```

В модуле `pygismeteo_base.models` содержатся все нужные для типизации модели.

## Соответствие функций возвращаемым моделям

| Функция | Модель                                          |
| ------- | ----------------------------------------------- |
| current | pygismeteo_base.models.current.Model            |
| step3   | List[pygismeteo_base.models.step3or6.ModelItem] |
| step6   | List[pygismeteo_base.models.step3or6.ModelItem] |
| step24  | List[pygismeteo_base.models.step24.ModelItem]   |
