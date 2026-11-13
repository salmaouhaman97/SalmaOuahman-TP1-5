"""Raccord entre l'API et le modèle entraîné au TP2.

Le modèle est maintenant exposé par le paquet `sentiment_app` et le dépôt conserve
une compatibilité avec l'ancien module `src/predict.py`.
"""
from __future__ import annotations

from sentiment_app.predict import MODELE, charger_modele, predict as _predict

SEUIL_ABSTENTION = 0.60


class SentimentClassifier:
    """Enveloppe du modèle TP2 avec l'interface attendue par l'API."""

    model_name = "tfidf-logreg (TP2, models/sentiment.joblib)"

    def __init__(self) -> None:
        if not MODELE.exists():
            raise FileNotFoundError(f"Modèle absent : {MODELE}. Lancez python src/train.py")
        charger_modele()  # lève FileNotFoundError si absent

    def predict(self, text: str) -> dict:
        """Renvoie {'label': 'POSITIVE'|'NEGATIVE'|'INDETERMINE', 'score': float, 'text': aperçu}."""
        r = _predict(text)  # lève ValueError si texte vide
        score = float(r["score"])
        if score < SEUIL_ABSTENTION:
            label = "INDETERMINE"
        else:
            label = r["label"].upper()
        return {"label": label, "score": score, "text": text[:100]}


def load_model() -> SentimentClassifier:
    """Construit le classifier (le cache de chargement est dans src/predict.py)."""
    return SentimentClassifier()

