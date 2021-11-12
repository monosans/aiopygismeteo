# -*- coding: utf-8 -*-
from typing import Iterable, Tuple


def strip_strs(iterable: Iterable[str]) -> Tuple[str, ...]:
    return tuple(string.strip().split()[0] for string in iterable)


def normalize_str(string: str, default_value: str = "Неизвестно") -> str:
    return (
        string.replace("\xa0", " ")
        .replace("\xad", "")
        .replace("<nobr>", "")
        .replace("</nobr>", "")
        .strip()
        .strip("—")
        or default_value
    )


def normalize_strs(
    iterable: Iterable[str], default_value: str = "Неизвестно"
) -> Tuple[str, ...]:
    return tuple(normalize_str(string, default_value) for string in iterable)
