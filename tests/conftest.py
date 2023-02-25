from __future__ import annotations

import pytest
from pydantic import BaseConfig


@pytest.fixture(autouse=True)
def _pydantic_strict(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(BaseConfig, "validate_all", True)
    monkeypatch.setattr(BaseConfig, "validate_assignment", True)
