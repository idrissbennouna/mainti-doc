from __future__ import annotations

from enum import StrEnum

from pydantic import BaseModel, Field


class UserRole(StrEnum):
    TECHNICIAN = "technician"
    SUPERVISOR = "supervisor"


class User(BaseModel):
    """Utilisateur fictif du prototype. Le jeton n'est jamais stocké ici."""

    id: str
    display_name: str
    role: UserRole
    access_groups: list[str] = Field(min_length=1)
