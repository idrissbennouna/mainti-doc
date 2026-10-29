from __future__ import annotations

from enum import StrEnum

from pydantic import BaseModel, Field

from manti_doc.models.citation import Citation
from manti_doc.models.ticket import TicketDraft


class ResponseStatus(StrEnum):
    ANSWERED = "answered"
    NEEDS_CLARIFICATION = "needs_clarification"
    ABSTAIN = "abstain"


class AssistantResponse(BaseModel):
    """Sortie structurée cible (CDC §7). Pas encore produite par un LLM."""

    status: ResponseStatus
    answer: str
    citations: list[Citation] = Field(default_factory=list)
    uncertainties: list[str] = Field(default_factory=list)
    clarification_question: str | None = None
    proposed_action: TicketDraft | None = None
