from __future__ import annotations

from pydantic import BaseModel, Field


class Citation(BaseModel):
    """Référence vers un élément réellement récupéré (pas une page inventée)."""

    document_id: str
    page: int = Field(ge=1)
    element_id: str
    supports_claim: bool | None = None
