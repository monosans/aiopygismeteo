from __future__ import annotations

import pytest

try:
    from pydantic.v1 import BaseConfig
except ImportError:
    from pydantic import BaseConfig  # type: ignore[assignment]


@pytest.fixture(autouse=True)
def _pydantic_strict(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(BaseConfig, "validate_all", True)
    monkeypatch.setattr(BaseConfig, "validate_assignment", True)
