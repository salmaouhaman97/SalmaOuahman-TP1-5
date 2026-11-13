#!/usr/bin/env python
"""Prédiction unitaire du modèle de sentiment.

Le modèle est chargé depuis la variable d'environnement SENTIMENT_MODELE.
Si elle est absente, on utilise le modèle du dépôt dans `models/sentiment.joblib`.
"""
from __future__ import annotations

import os
import sys
from functools import lru_cache
from pathlib import Path

import joblib

RACINE = Path(__file__).resolve().parents[1]
DEFAULT_MODELE = RACINE / "models" / "sentiment.joblib"
MODELE = Path(os.environ.get("SENTIMENT_MODELE", str(DEFAULT_MODELE)))


@lru_cache(maxsize=1)
def charger_modele():
    """Charge le modèle une seule fois par processus."""
    if not MODELE.exists():
        raise FileNotFoundError(
            f"Modèle introuvable : {MODELE}. Définissez SENTIMENT_MODELE ou lancez python src/train.py"
        )
    return joblib.load(MODELE)


def predict(texte: str) -> dict:
    """Renvoie {'label': 'positive'|'negative', 'score': float}."""
    if not isinstance(texte, str) or not texte.strip():
        raise ValueError("texte vide")
    pipeline = charger_modele()
    etiquette = pipeline.predict([texte])[0]
    score = float(pipeline.predict_proba([texte]).max())
    return {"label": etiquette, "score": round(score, 4)}


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: sentiment predict <texte>")
        return 2
    resultat = predict(" ".join(sys.argv[1:]))
    print(f"{resultat['label']} (confiance {resultat['score']:.0%})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
