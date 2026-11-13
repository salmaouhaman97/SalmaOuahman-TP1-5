# Semaine 6 : packager l'application

## 1. Pourquoi le modèle n'est-il pas inclus dans la roue ?

La roue contient le code et ses dépendances, mais pas les données d'entraînement ni le modèle `.joblib`. Le modèle est un artefact qui possède son propre cycle de vie : on peut le réentraîner ou le remplacer sans republier le code. L'application le localise avec `SENTIMENT_MODELE`, ce qui rend le chemin explicite sur une machine qui ne contient pas le dépôt.

## 2. Comment l'API trouve-t-elle la prédiction après le packaging ?

`api/model.py` importe `MODELE`, `charger_modele` et `predict` depuis `sentiment_app.predict`. Il n'ajoute pas `src/` à `sys.path`. Le module `src/predict.py` reste uniquement comme passerelle de compatibilité pour les anciens tests et scripts du dépôt.

## 3. Quelle est la différence entre l'installation editable et la roue ?

`pip install -e .` relie l'environnement de développement au code source courant : les changements de code sont visibles sans réinstaller le paquet. La roue est une archive construite à une version donnée et installée comme un paquet normal. Le test hors dépôt crée donc un nouvel environnement, installe la roue et vérifie que `sentiment --version` et `sentiment predict` fonctionnent avec un chemin de modèle fourni par `SENTIMENT_MODELE`.

## Vérifications

- Suite locale : `python -m pytest -q`.
- CLI en développement : `sentiment --version`, `sentiment predict "Livraison rapide, très satisfait"`.
- CI : construction de `sentiment_app-0.6.0-py3-none-any.whl`, installation dans un environnement neuf et vérification des commandes CLI.
- Le tag Git `v0.6.0` doit être créé et poussé après le commit de livraison sur `main`.