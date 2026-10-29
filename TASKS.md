# Tâches — MAINTiDOC

## Terminées (phase 1)

- [x] Lire le cahier des charges PDF et produire une synthèse Markdown.
- [x] Inspecter le dépôt réel (squelette uv, mémoire vide).
- [x] Découper le projet en 8 phases et figer les poids d’avancement.
- [x] Remplir `PROJECT_STATUS.md`, `DECISIONS.md`, `CHANGELOG.md`, `README.md`.
- [x] Modèles Pydantic (utilisateur, document, citation, ticket brouillon, réponse).
- [x] Configuration par variables d’environnement.
- [x] Corpus fictif à deux familles d’équipements + ACL.
- [x] API FastAPI `/health` et listage/lecture de documents filtrés.
- [x] Tests unitaires et d’API.
- [x] Rapport `docs/phases/phase_01_cadrage_architecture.md`.
- [x] Copie de la règle Cursor vers `.cursor/rules/maintidoc.mdc`.

## En cours

- Aucune (phase 1 close après validation des tests et du rapport).

## À faire — phase 2 (non autorisée tant que non approuvée)

- [ ] Ingestion PDF réelle (PyMuPDF) et OCR local.
- [ ] Métadonnées persistantes (PostgreSQL ou justification d’un écart).
- [ ] Stockage fichiers (MinIO ou justification d’un écart).
- [ ] ACL appliquée au chargement disque, pas seulement au corpus mémoire.

## Plus tard (phases 3–8)

- [ ] Qdrant, embeddings, recherche visuelle, RRF.
- [ ] VLM, prompts versionnés, vérification des citations.
- [ ] LangGraph, serveur MCP, HITL, idempotence des tickets.
- [ ] Reranker, jeu d’évaluation, MLflow.
- [ ] Tests d’injection, quotas.
- [ ] Docker Compose, Streamlit, rapport final.
