# -*- coding: utf-8 -*-
def get_ancestor(data_widget_id: str) -> str:
    return f'//div[@data-widget-id="{data_widget_id}"]'


AVERAGE_TEMP = (
    get_ancestor("averageTemp"),
    '//span[contains(@class,"unit_temperature_c")]/text()',
)
FALLING_SNOW = (
    get_ancestor("snow"),
    '//div[contains(@class,"w_snow__value")]/text()',
)
GEOMAGNETIC_ACTIVITY = (
    get_ancestor("gm"),
    '//div[contains(@class,"widget__value")]//text()',
)
HUMIDITY = (
    get_ancestor("humidity"),
    '//div[contains(@class,"w-humidity")]/text()',
)
MAX_PRESSURE = (
    get_ancestor("pressure"),
    '//div[contains(@class,"maxt")]'
    + '//span[contains(@class,"unit_pressure_mm_hg_atm")]/text()',
)
MAX_TEMPERATURE = (
    get_ancestor("forecast"),
    '//div[contains(@class,"maxt")]'
    + '//span[contains(@class,"unit_temperature_c")]/text()',
)
MIN_PRESSURE = (
    get_ancestor("pressure"),
    '//div[contains(@class,"mint")]'
    + '//span[contains(@class,"unit_pressure_mm_hg_atm")]/text()',
)
MIN_TEMPERATURE = (
    get_ancestor("forecast"),
    '//div[contains(@class,"mint")]'
    + '//span[contains(@class,"unit_temperature_c")]/text()',
)
PRECIPITATION = (
    get_ancestor("forecast"),
    '//div[contains(@class,"w_prec__value")]/text()',
)
PRESSURE = (
    get_ancestor("pressure"),
    '//div[contains(@class,"value")]'
    + '//span[contains(@class,"unit_pressure_mm_hg_atm")]/text()',
)
ROAD_CONDITION = (
    get_ancestor("roadcondition"),
    '//div[contains(@class,"w_roadcondition__description")]/text()',
)
SNOW_DEPTH = (
    get_ancestor("snow"),
    '//span[contains(@class,"unit_snow")]/text()',
)
STATUS = (
    get_ancestor("forecast"),
    '//span[contains(@class,"tooltip")]/@data-text',
)
TEMPERATURE = (
    get_ancestor("forecast"),
    '//span[contains(@class,"unit_temperature_c")]/text()',
)
ULTRAVIOLET_INDEX = (
    get_ancestor("uvb"),
    '//div[contains(@class,"widget__value")]/text()',
)
VISIBILITY = (
    get_ancestor("visibility"),
    '//div[contains(@class,"w_visibility__value")]'
    + '//span[contains(@class,"unit_visibility_m")]/text()',
)
WIND_DIRECTION = (
    get_ancestor("wind"),
    '//div[contains(@class,"w_wind__direction")]/text()',
)
WIND_OR_GUST_SPEED = (
    get_ancestor("forecast"),
    '//div[contains(@class,"w_wind")]'
    + '//span[contains(@class,"unit_wind_m_s")]/text()',
)
WIND_SPEED = (
    get_ancestor("wind"),
    '//div[contains(@class,"widget__row_wind")]'
    + '//span[contains(@class,"unit_wind_m_s")]/text()',
)
