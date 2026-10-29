# MAINTiDOC

Assistant documentaire multimodal et agentique destiné à la maintenance.
Le système aide un technicien à interroger des manuels, procédures, schémas et
photographies. Il ne pilote aucun équipement, ne garantit pas un diagnostic et
ne remplace pas les procédures de sécurité ni un technicien habilité.

Référence fonctionnelle : [`docs/cahier_des_charges.pdf`](docs/cahier_des_charges.pdf)
(synthèse : [`docs/cahier_des_charges.md`](docs/cahier_des_charges.md)).

## État actuel (phase 1)

Fondations uniquement : configuration, modèles de données, API FastAPI (`/health`
et consultation ACL d’un corpus fictif), tests. **Pas encore** de RAG, de modèle
vision-langage, de LangGraph, d’outils MCP ni d’interface Streamlit.

La mémoire du projet est dans [`PROJECT_STATUS.md`](PROJECT_STATUS.md).

## Prérequis

- [uv](https://docs.astral.sh/uv/) (le dépôt est un projet uv)
- Python **3.13** (fichier `.python-version`). L’interpréteur système de la
  machine de développement peut être plus ancien : `uv` installe et utilise 3.13.

```bash
uv python install 3.13
uv sync --group dev
copy .env.example .env
```

Sous Linux/macOS, remplacer `copy` par `cp .env.example .env`.

## Lancer l’API de démonstration

```bash
uv run manti-doc
```

Vérifications manuelles :

```bash
curl http://127.0.0.1:8000/health
curl -H "Authorization: Bearer demo-token-alice" http://127.0.0.1:8000/v1/documents
```

- `demo-token-alice` : groupe `pompe_centrifuge`
- `demo-token-bob` : groupe `ventilateur_industriel`
- `demo-token-chef` : les deux familles

## Tests

```bash
uv run pytest
```

## Sécurité

- Aucun secret dans Git. Utiliser `.env` (ignoré) à partir de `.env.example`.
- Les documents du corpus sont des **données**, jamais des instructions.
- Aucune création de ticket de maintenance n’est exposée à ce stade (brouillon
  de modèle uniquement).
