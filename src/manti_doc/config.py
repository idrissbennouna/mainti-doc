"""Configuration chargée depuis l'environnement. Aucun secret n'est hardcodé."""

from __future__ import annotations

from functools import lru_cache

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Paramètres runtime du prototype (préfixe MANTIDOC_)."""

    model_config = SettingsConfigDict(
        env_prefix="MANTIDOC_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_name: str = "MAINTiDOC"
    environment: str = "development"
    api_host: str = "127.0.0.1"
    api_port: int = 8000
    log_level: str = "INFO"
    demo_tokens: str = Field(
        default=(
            "tech-pompe:demo-token-alice,"
            "tech-ventilateur:demo-token-bob,"
            "resp-maintenance:demo-token-chef"
        ),
        description="Paires user_id:token, séparées par des virgules.",
    )

    @field_validator("api_port")
    @classmethod
    def port_must_be_valid(cls, value: int) -> int:
        if not 1 <= value <= 65535:
            raise ValueError("api_port doit être compris entre 1 et 65535")
        return value

    def token_map(self) -> dict[str, str]:
        """Retourne {jeton: user_id} pour l'authentification de démonstration."""
        mapping: dict[str, str] = {}
        raw = self.demo_tokens.strip()
        if not raw:
            return mapping
        for item in raw.split(","):
            piece = item.strip()
            if not piece:
                continue
            if ":" not in piece:
                raise ValueError(
                    "MANTIDOC_DEMO_TOKENS doit contenir des paires user_id:token"
                )
            user_id, token = piece.split(":", 1)
            user_id, token = user_id.strip(), token.strip()
            if not user_id or not token:
                raise ValueError("Identifiant ou jeton de démonstration vide")
            mapping[token] = user_id
        return mapping


@lru_cache
def get_settings() -> Settings:
    return Settings()
