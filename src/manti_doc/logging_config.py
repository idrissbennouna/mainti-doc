"""Journalisation : métadonnées techniques, pas de contenu documentaire brut."""

from __future__ import annotations

import logging

from manti_doc.config import Settings


def configure_logging(settings: Settings) -> None:
    level = getattr(logging, settings.log_level.upper(), logging.INFO)
    logging.basicConfig(
        level=level,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
        force=True,
    )
    logging.getLogger("manti_doc").debug(
        "journalisation initialisée env=%s", settings.environment
    )
