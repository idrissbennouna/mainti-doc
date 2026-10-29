from manti_doc.config import get_settings


def main() -> None:
    import uvicorn

    settings = get_settings()
    uvicorn.run(
        "manti_doc.api.app:app",
        host=settings.api_host,
        port=settings.api_port,
        reload=False,
    )
