# Déployez et monitorez votre modèle de scoring

 L'objectif est de reprendre un modèle de scoring déjà entrainé, de l'exposer via une API conteneurisée et de suivre son comportement en production.

> **État actuel :** ce dépôt est une base de travail. Le modèle, l'API, les tests, le conteneur et le monitoring restent à intégrer. `uv sync` permet de préparer l'environnement ; la commande de démarrage de l'API sera ajoutée quand elle existera.


## Roadmap

- [ ] Étape 1 : Mettez en place le contrôle de version et le dépôt.
- [ ] Étape 2 : Déployez le modèle via une API et automatisez avec CI/CD.
- [ ] Étape 3 : Implémentez le stockage et l'analyse des données de production.
- [ ] Étape 4 : Analysez et optimisez les performances du modèle.
- [ ] Étape 5 : Réalisez la documentation.

## Structure du projet

```text
.
├── .venv                   # Dépendances du projets
├── .gitignore              # Fichiers et dossiers ignorés par Git
├── .python-version         # Version de Python utilisée : 3.14
├── pyproject.toml          # Métadonnées et dépendances du projet
├── README.md               # Présentation, roadmap et instructions
└── uv.lock                 # Versions des dépendances résolues par uv
```

## Lancer le projet

Prérequis : avoir installé `uv`. Depuis la racine du dépôt, exécuter :

```bash
uv sync
```

Cette commande prépare l'environnement virtuel `.venv` avec la version de Python et les dépendances définies par le projet. À ce stade, elle ne démarre aucune application : l'API n'est pas encore implémentée.