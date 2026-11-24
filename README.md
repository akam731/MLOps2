# API de scoring — MLOps 2

Ce dépôt expose une API FastAPI minimale avec `GET /health` et fournit une classe Python pour charger le modèle de scoring existant. Le modèle est chargé à la première prédiction; le démarrage de l’API ne le charge pas. Aucune route de prédiction n’est exposée.

## Roadmap

- [ ] Étape 1 : Mettez en place le contrôle de version et le dépôt.
- [ ] Étape 2 : Déployez le modèle via une API et automatisez avec CI/CD.
- [ ] Étape 3 : Implémentez le stockage et l'analyse des données de production.
- [ ] Étape 4 : Analysez et optimisez les performances du modèle.
- [ ] Étape 5 : Réalisez la documentation.

## Prérequis

- Python 3.14 (version sélectionnée par `.python-version`)
- [uv](https://docs.astral.sh/uv/)

## Installer les dépendances

Depuis la racine du dépôt :

```shell
uv sync
```

## Lancer l’API

```shell
uv run uvicorn app:app --reload
```

La route de santé est disponible sur `http://127.0.0.1:8000/health` et renvoie `{"status":"ok"}`.

## Lancer les tests

```shell
uv run pytest
```

Le rapport est disponible dans `tests/htmlcov/index.html` après l'exécution des tests.

### Voir le rapport HTML de couverture

```shell
start .\tests\htmlcov\index.html
```
