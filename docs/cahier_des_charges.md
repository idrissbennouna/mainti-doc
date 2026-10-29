# MAINTiDOC — Synthèse du cahier des charges

Ce fichier est une **synthèse de travail**, pas une copie intégrale.
La référence reste [`cahier_des_charges.pdf`](cahier_des_charges.pdf)
(*Projet intégrateur d’IA générative multi modale*, v2).

## Objectif

Assistant pour techniciens et responsables de maintenance. Il exploite manuels,
procédures, schémas et photographies, consulte un historique d’interventions
(via MCP) et peut **préparer** un ticket. La **création effective** exige une
validation humaine du contenu exact.

Hors périmètre : pilotage de machines, diagnostic garanti, interventions autonomes.

## Cadrage

| Élément | Périmètre proposé |
|---|---|
| Utilisateurs | Techniciens et responsables (fictifs dans le prototype) |
| Corpus | 30 à 50 documents, deux familles d’équipements |
| Entrées | Questions en français, photos, PDF |
| Sorties | Réponses sourcées, clarifications, brouillons de tickets |
| Outil externe | Service de maintenance de démonstration via MCP |

## Architecture cible (non implémentée en phase 1)

Interface Streamlit → API FastAPI (authz) → workflow LangGraph → RAG multimodal
+ VLM + client MCP → vérification des références → réponse / clarification /
validation humaine.

Stack de référence : Qwen2.5-VL-7B-Instruct, Transformers (vLLM si compatible),
LangChain/LangGraph, Qdrant, BGE-M3, encodeur texte-image type CLIP, PyMuPDF +
OCR, PostgreSQL, MinIO, MLflow, Docker Compose.

## RAG et citations

Ingestion en passages et éléments visuels avec identifiant document, version,
page, type d’équipement, groupes d’accès. Recherche texte + visuelle, fusion
(RRF), reranker, puis VLM. Une citation doit pointer vers un élément réellement
récupéré **et** soutenir l’affirmation.

## Fine-tuning ciblé

Petit reranker multilingue (800–1500 triplets). Le VLM reste inchangé dans le
périmètre initial. Métriques : nDCG@5, MRR@10, qualité des réponses.

## MCP

- `get_equipment_history(equipment_id)`
- `get_open_tickets(equipment_id)`
- `create_ticket(..., approval_token)` — uniquement après HITL ; idempotence.

## Sorties structurées

Prompts versionnés sous `prompts/`. Schéma Pydantic illustratif : `status`,
`answer`, `citations`, `uncertainties`, `clarification_question`,
`proposed_action`.

## Incertitude et sécurité

Clarifier ou s’abstenir si image illisible, sources absentes/contradictoires, ou
demande hors rôle documentaire. Pas de pourcentage de confiance inventé.
Secrets hors Git ; ACL avant retrieval et à l’affichage ; documents et outils =
données non fiables ; tests d’injection ; budgets (3 MCP, 6 appels modèle, 60 s).

## Évaluation et livrables

Environ 150 scénarios (documentaire, image, MCP, sources manquantes, ACL/HITL,
injections). Livrables : cadrage, dépôt, prototype, évaluation, fiche de limites,
démonstration de soutenance.
