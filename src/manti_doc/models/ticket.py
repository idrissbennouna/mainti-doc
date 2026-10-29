from __future__ import annotations

from pydantic import BaseModel, Field


class TicketDraft(BaseModel):
    """Brouillon uniquement. Aucune création MCP n'est implémentée en phase 1."""

    equipment_id: str
    title: str = Field(min_length=3, max_length=120)
    description: str = Field(min_length=10, max_length=4000)
    approved: bool = False
    approval_token: str | None = None
