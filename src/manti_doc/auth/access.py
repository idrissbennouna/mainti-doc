"""Contrôle d'accès documentaire : intersection des groupes, refus par défaut."""

from __future__ import annotations

from manti_doc.models.document import Document
from manti_doc.models.user import User


class DocumentAccessDenied(PermissionError):
    def __init__(self, user_id: str, document_id: str) -> None:
        super().__init__(
            f"accès refusé user={user_id} document={document_id}"
        )
        self.user_id = user_id
        self.document_id = document_id


def can_access_document(user: User, document: Document) -> bool:
    user_groups = set(user.access_groups)
    doc_groups = set(document.access_groups)
    if not user_groups or not doc_groups:
        return False
    return not user_groups.isdisjoint(doc_groups)


def filter_documents(user: User, documents: list[Document]) -> list[Document]:
    return [document for document in documents if can_access_document(user, document)]


def assert_can_access_document(user: User, document: Document) -> None:
    if not can_access_document(user, document):
        raise DocumentAccessDenied(user.id, document.id)
