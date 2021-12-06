# -*- coding: utf-8 -*-
from typing import Dict, Optional


def check_dict(
    d: Dict[str, str], length: int, max_length: Optional[int] = None
) -> None:
    if max_length:
        assert length <= len(d) <= max_length
    else:
        assert len(d) == length
    for key, value in d.items():
        for i in (key, value):
            assert isinstance(i, str) and i
