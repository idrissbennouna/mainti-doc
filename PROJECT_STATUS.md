# PROJECT_STATUS — MAINTiDOC

Dernière mise à jour : 2026-10-29. Ce fichier est la source de mémoire principale.
Détails : `TASKS.md`, `DECISIONS.md`, `CHANGELOG.md`, `docs/phases/`.

## 1. Nom et objectif

**MAINTiDOC** : assistant documentaire multimodal et agentique pour la
maintenance. Aide à la recherche sourcée, analyse d’image, consultation
d’historique et préparation de tickets. Pas de pilotage d’équipement.

## 2. Cahier des charges

- PDF : `docs/cahier_des_charges.pdf` (référence)
- Synthèse : `docs/cahier_des_charges.md`

## 3. Architecture technique actuelle

Phase 1 uniquement :

- Package `manti_doc` (src layout, uv)
- FastAPI : santé + documents filtrés par groupes
- Utilisateurs et jetons de démonstration via l’environnement
- Corpus Markdown synthétique chargé en mémoire
- Pas de Qdrant, VLM, LangGraph, MCP, Streamlit, Postgres, MinIO, MLflow

Architecture **cible** : voir le CDC et `docs/phases/phase_01_cadrage_architecture.md`.

## 4. État réel des fonctionnalités

| Fonctionnalité CDC | État |
|---|---|
| Cadrage / mémoire / squelette | Testée (phase 1) |
| Auth / ACL documentaire minimale | Testée sur corpus fictif |
| Ingestion PDF / OCR | Non commencée |
| RAG texte / visuel | Non commencée |
| VLM et citations | Non commencée |
| LangGraph | Non commencée |
| MCP + HITL tickets | Non commencée (modèle brouillon seulement) |
| Reranker / éval / MLflow | Non commencée |
| Docker / Streamlit | Non commencée |

## 5. Phase actuelle

- **Phase 1 — Fondations** : implémentée dans cette session, à considérer
  **testée et validée** si les commandes de la section 8 ont réussi.
- Phases 2–8 : non commencées.

## 6. Avancement global et méthode

Poids (livrables **testés**) :

| Phase | Poids | Comptabilisé |
|---|---:|---:|
| 1 Fondations | 18 % | 18 % si tests OK |
| 2 Ingestion | 12 % | 0 |
| 3 RAG multimodal | 14 % | 0 |
| 4 VLM / sorties | 12 % | 0 |
| 5 LangGraph / MCP / HITL | 16 % | 0 |
| 6 Reranker / éval / MLflow | 12 % | 0 |
| 7 Sécurité avancée | 8 % | 0 |
| 8 Déploiement / rapport final | 8 % | 0 |

**Estimation : 18 %** après phase 1 validée par pytest (une fonctionnalité non
testée ne compterait que la moitié). Avant phase 1 le dépôt était ~2 %.

## 7. Fichiers créés ou modifiés (phase 1)

Voir `CHANGELOG.md` et le rapport de phase.

## 8. Tests et lancement

```bash
uv python install 3.13
uv sync --group dev
uv run pytest
uv run manti-doc
```

Résultats pytest : à renseigner avec la sortie réelle en fin de session
(section mise à jour après exécution).

## 9. Versions

- Projet : 0.1.0
- Python exigé : >= 3.13 (uv)
- Python hôte observé au cadrage : 3.12.7
- uv observé : 0.12.23

## 10–13. Décisions, erreurs, essais

Voir `DECISIONS.md`. GPU 24 Go **non vérifié**. Pas de secret dans ce fichier.

## 14. Dernière étape réellement terminée

Cadrage section 15 + implémentation phase 1 (fondations).

## 15. Dernière étape partielle

Aucune si pytest est vert.

## 16. Prochaine tâche exacte

**Attendre l’approbation explicite** avant la phase 2 (ingestion PDF/OCR et
stockage métadonnées/fichiers).

## 17. Critères d’acceptation restants (projet global)

Tous les critères CDC hors phase 1 : RAG sourcé, VLM, MCP HITL, éval 150
scénarios, démo soutenance, etc.

## 18. Rapports de phase

- `docs/phases/phase_01_cadrage_architecture.md`

## 19. Points théoriques à maîtriser (phase 1)

ACL, séparation config/code, schémas Pydantic, untrusted data, uv/packaging.

## 20. Risques

Python hôte ≠ 3.13 ; GPU/VLM non prouvés ; périmètre CDC large pour un
développeur seul ; mémoire ne doit jamais inventer des tests.
