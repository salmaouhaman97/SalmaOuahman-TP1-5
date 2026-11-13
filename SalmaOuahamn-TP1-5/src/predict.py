#!/usr/bin/env python
"""Compatibilité historique pour le dépôt TP2/TP4/TP5.

Le code métier vivant dans `sentiment_app.predict` est importé ici pour ne pas
casser l'ancien `from predict import predict` dans les tests et scripts du dépôt.
"""
from __future__ import annotations

import sys

from sentiment_app.predict import MODELE, charger_modele, predict


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    resultat = predict(" ".join(sys.argv[1:]))
    print(f"{resultat['label']} (confiance {resultat['score']:.0%})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
