from __future__ import annotations

import pytest
from fastapi.testclient import TestClient

from manti_doc.api.app import create_app
from manti_doc.config import Settings, get_settings


@pytest.fixture
def settings() -> Settings:
    get_settings.cache_clear()
    return Settings(
        environment="test",
        demo_tokens=(
            "tech-pompe:demo-token-alice,"
            "tech-ventilateur:demo-token-bob,"
            "resp-maintenance:demo-token-chef"
        ),
    )


@pytest.fixture
def client(settings: Settings) -> TestClient:
    app = create_app(settings)
    return TestClient(app)
