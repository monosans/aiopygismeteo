# Типизация

Для типизации вашего кода надо импортировать `pygismeteo_base`:

```python
import pygismeteo_base
```

В модуле `pygismeteo_base.models` содержатся все нужные для типизации модели.

## Соответствие методов класса Gismeteo возвращаемым моделям

| Метод   | Модель                                |
| ------- | ------------------------------------- |
| current | pygismeteo_base.models.current.Model  |
| step3   | pygismeteo_base.models.step3or6.Model |
| step6   | pygismeteo_base.models.step3or6.Model |
| step24  | pygismeteo_base.models.step24.Model   |
