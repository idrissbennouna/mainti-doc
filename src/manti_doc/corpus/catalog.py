"""Catalogue de démonstration : utilisateurs fictifs et documents synthétiques."""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path

from manti_doc.models.document import Document, EquipmentFamily
from manti_doc.models.user import User, UserRole

REPO_ROOT = Path(__file__).resolve().parents[3]
CORPUS_DIR = REPO_ROOT / "data" / "corpus"

_USERS: tuple[User, ...] = (
    User(
        id="tech-pompe",
        display_name="Alice Martin",
        role=UserRole.TECHNICIAN,
        access_groups=["pompe_centrifuge"],
    ),
    User(
        id="tech-ventilateur",
        display_name="Bob Leroy",
        role=UserRole.TECHNICIAN,
        access_groups=["ventilateur_industriel"],
    ),
    User(
        id="resp-maintenance",
        display_name="Chloé Durand",
        role=UserRole.SUPERVISOR,
        access_groups=["pompe_centrifuge", "ventilateur_industriel"],
    ),
)


def load_users() -> dict[str, User]:
    return {user.id: user for user in _USERS}


def _read(name: str) -> str:
    path = CORPUS_DIR / name
    return path.read_text(encoding="utf-8")


@lru_cache
def load_documents() -> list[Document]:
    return [
        Document(
            id="manuel_pompe_a",
            title="Manuel pompe centrifuge A",
            version="1",
            equipment_family=EquipmentFamily.CENTRIFUGAL_PUMP,
            page=12,
            element_id="voyant_orange_coffret",
            access_groups=["pompe_centrifuge"],
            source_path=str(CORPUS_DIR / "manuel_pompe_a.md"),
            body=_read("manuel_pompe_a.md"),
        ),
        Document(
            id="procedure_pompe_n12",
            title="Procédure N-12 graissage",
            version="1",
            equipment_family=EquipmentFamily.CENTRIFUGAL_PUMP,
            page=3,
            element_id="procedure_n12",
            access_groups=["pompe_centrifuge"],
            source_path=str(CORPUS_DIR / "procedure_pompe_graissage.md"),
            body=_read("procedure_pompe_graissage.md"),
        ),
        Document(
            id="manuel_ventilateur_b",
            title="Manuel ventilateur industriel B",
            version="1",
            equipment_family=EquipmentFamily.INDUSTRIAL_FAN,
            page=7,
            element_id="voyant_orange_variateur",
            access_groups=["ventilateur_industriel"],
            source_path=str(CORPUS_DIR / "manuel_ventilateur_b.md"),
            body=_read("manuel_ventilateur_b.md"),
        ),
    ]


def get_document(document_id: str) -> Document | None:
    for document in load_documents():
        if document.id == document_id:
            return document
    return None
