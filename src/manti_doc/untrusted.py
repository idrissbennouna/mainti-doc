"""Les documents, OCR et sorties d'outils sont des données, pas des instructions."""

from __future__ import annotations

UNTRUSTED_PREFIX = "[DONNEE_DOCUMENTAIRE_NON_FIABLE]\n"


def as_untrusted_data(text: str) -> str:
    """ marquer un texte issu du corpus avant tout usage dans un prompt futur."""
    return UNTRUSTED_PREFIX + text
