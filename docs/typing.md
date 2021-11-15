# Типизация

Для типизации вашего кода надо импортировать нужные классы из `pygismeteo.types`, например:

```python
from aiopygismeteo.types import Gismeteo, In5Days, Month, Now, Today, TwoWeeks
```

## Полный список классов для типизации

| Класс     | Описание                                                               |
| --------- | ---------------------------------------------------------------------- |
| Gismeteo  | Возвращается фабрикой gismeteo()                                       |
| ABCDate   | Абстрактный класс даты, от которого наследуются все последующие классы |
| Now       | Возвращается методом now() класса Gismeteo                             |
| ThreeDays | Возвращается методом three_days() класса Gismeteo                      |
| TenDays   | Возвращается методом ten_days() класса Gismeteo                        |
| TwoWeeks  | Возвращается методом two_weeks() класса Gismeteo                       |
| Month     | Возвращается методом month() класса Gismeteo                           |
| OneDay    | Класс, от которого наследуются все последующие классы                  |
| Today     | Возвращается методом today() класса Gismeteo                           |
| Tomorrow  | Возвращается методом tomorrow() класса Gismeteo                        |
| In3Days   | Возвращается методом in3_days() класса Gismeteo                        |
| In4Days   | Возвращается методом in4_days() класса Gismeteo                        |
| In5Days   | Возвращается методом in5_days() класса Gismeteo                        |
| In6Days   | Возвращается методом in6_days() класса Gismeteo                        |
| In7Days   | Возвращается методом in7_days() класса Gismeteo                        |
| In8Days   | Возвращается методом in8_days() класса Gismeteo                        |
| In9Days   | Возвращается методом in9_days() класса Gismeteo                        |
| In10Days  | Возвращается методом in10_days() класса Gismeteo                       |
