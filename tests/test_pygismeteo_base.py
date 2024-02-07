from __future__ import annotations


def test_typing_compat() -> None:
    from pygismeteo_base.typing_compat import (  # noqa: F401, PLC0415
        Literal,
        TypeAlias,
    )
