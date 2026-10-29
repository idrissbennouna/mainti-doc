from __future__ import annotations

from fastapi import Depends, FastAPI, HTTPException, status

from manti_doc.auth.access import DocumentAccessDenied, assert_can_access_document, filter_documents
from manti_doc.config import Settings, get_settings
from manti_doc.corpus.catalog import get_document, load_documents
from manti_doc.logging_config import configure_logging
from manti_doc.models.document import Document
from manti_doc.models.user import User
from manti_doc.api.deps import current_user
from manti_doc.untrusted import as_untrusted_data


def create_app(settings: Settings | None = None) -> FastAPI:
    resolved = settings or get_settings()
    configure_logging(resolved)
    app = FastAPI(
        title=resolved.app_name,
        version="0.1.0",
        description=(
            "Prototype phase 1 : santé et ACL documentaire. "
            "Aide documentaire uniquement — aucune création de ticket."
        ),
    )

    @app.get("/health")
    def health() -> dict[str, str]:
        return {
            "status": "ok",
            "service": resolved.app_name,
            "environment": resolved.environment,
            "phase": "1",
        }

    @app.get("/v1/me")
    def me(user: User = Depends(current_user)) -> User:
        return user

    @app.get("/v1/documents")
    def list_documents(user: User = Depends(current_user)) -> list[Document]:
        visible = filter_documents(user, load_documents())
        return visible

    @app.get("/v1/documents/{document_id}")
    def read_document(
        document_id: str, user: User = Depends(current_user)
    ) -> dict[str, object]:
        document = get_document(document_id)
        if document is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="inconnu")
        try:
            assert_can_access_document(user, document)
        except DocumentAccessDenied as exc:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="accès documentaire refusé",
            ) from exc
        return {
            "document": document,
            "untrusted_body": as_untrusted_data(document.body),
        }

    return app


app = create_app()
