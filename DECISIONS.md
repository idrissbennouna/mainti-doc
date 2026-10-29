# Décisions d’architecture — MAINTiDOC

Les décisions ci-dessous concernent la phase 1, sauf mention contraire.
Les technologies du cahier des charges restent la référence pour les phases
ultérieures. Un écart n’est adopté que s’il est justifié ici.

## D1 — Python 3.13 via uv (phase 1)

- **Décision** : conserver `requires-python = ">=3.13"` et `.python-version`.
- **Raison** : le squelette initial du dépôt était déjà piné 3.13 ; uv gère
  l’interpréteur du projet indépendamment de Python 3.12.7 éventuellement
  présent sur le PATH hôte.
- **Alternative écartée** : baisser le pin à 3.12 pour coller à l’hôte — cela
  masque un écart au lieu de le traiter.
- **Statut** : appliquée.

## D2 — Fondations sans RAG ni VLM (phase 1)

- **Décision** : n’introduire ni LangChain, ni Qdrant, ni PyTorch, ni client MCP.
- **Raison** : le périmètre 15–18 % doit poser une base testable (config, ACL,
  schémas) avant des dépendances lourdes et du matériel GPU non vérifié.
- **Statut** : appliquée.

## D3 — FastAPI dès la phase 1, Streamlit plus tard

- **Décision** : exposer une API HTTP minimale (`/health`, documents filtrés).
- **Raison** : le cahier des charges prévoit FastAPI pour l’auth et l’autorisation ;
  un contrat HTTP testable sert toutes les phases suivantes. Streamlit n’apporte
  pas de valeur tant que le graphe agentique n’existe pas.
- **Statut** : appliquée.

## D4 — Authentification de démonstration par jeton Bearer statique

- **Décision** : correspondance jeton → utilisateur fictif via
  `MANTIDOC_DEMO_TOKENS`. Pas de JWT, pas d’IdP.
- **Raison** : suffisamment pour tester l’ACL documentaire. Un vrai fournisseur
  d’identité sera évalué quand l’auth de production sera au programme.
- **Limite** : inacceptable hors prototype.
- **Statut** : appliquée.

## D5 — Corpus fictif en fichiers Markdown, en mémoire au runtime

- **Décision** : deux familles d’équipements, métadonnées d’accès dans le code
  de chargement, pas PostgreSQL ni MinIO en phase 1.
- **Raison** : le CDC autorise des documents synthétiques ; reporter le stockage
  objet/SQL à la phase d’ingestion évite une infra prématurée.
- **Statut** : appliquée.

## D6 — Ticket = modèle de brouillon uniquement

- **Décision** : schéma `TicketDraft` sans endpoint de création et sans MCP.
- **Raison** : contrainte de validation humaine du CDC ; aucune action sensible
  ne doit exister avant LangGraph + HITL.
- **Statut** : appliquée.

## D7 — Règle Cursor dupliquée sous `.cursor/rules/`

- **Décision** : conserver `docs/cursor/rules/maintidoc.mdc` et copier vers
  `.cursor/rules/maintidoc.mdc` pour que l’éditeur l’applique.
- **Raison** : le prompt maître n’était pas au chemin attendu par Cursor.
- **Statut** : appliquée en phase 1.

## Décisions reportées

- Qdrant vs autre store vectoriel, BGE-M3 vs autre embedding, Qwen2.5-VL vs
  alternative, vLLM vs Transformers, GPU 24 Go : **phase 3–4**, après mesure.
- PostgreSQL + MinIO : **phase 2**.
- Fine-tuning du reranker : **phase 6**. Le VLM reste gelé au début, conformément
  au CDC.
