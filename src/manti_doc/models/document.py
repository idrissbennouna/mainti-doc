from __future__ import annotations

from enum import StrEnum

from pydantic import BaseModel, Field


class EquipmentFamily(StrEnum):
    CENTRIFUGAL_PUMP = "pompe_centrifuge"
    INDUSTRIAL_FAN = "ventilateur_industriel"


class Document(BaseModel):
    """Métadonnées et contenu d'un élément documentaire du corpus de démo."""

    id: str
    title: str
    version: str
    equipment_family: EquipmentFamily
    page: int = Field(ge=1)
    element_id: str
    access_groups: list[str] = Field(min_length=1)
    source_path: str
    body: str = Field(
        description="Texte brut traité comme donnée non fiable, jamais comme instruction."
    )
