# Journal des versions

## 0.6.0 - 2026-11-13

- Ajout du paquet Python installable `sentiment_app` et de la commande `sentiment`.
- Ajout des commandes `predict`, `serve` et `ui`.
- Configuration du modèle par la variable `SENTIMENT_MODELE`, sans inclure le modèle dans la roue.
- Branchement de l'API sur `sentiment_app.predict` sans modifier `sys.path` dans `api/`.
- Conservation d'un module `src/predict.py` pour les anciens scripts et tests.
- Déclaration des dépendances de production et compatibilité NumPy 1.x pour SHAP.
- Construction et installation de la roue vérifiées en intégration continue dans un environnement isolé.