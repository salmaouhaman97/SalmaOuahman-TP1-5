#!/usr/bin/env python
"""Interface en ligne de commande du paquet sentiment_app."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from sentiment_app import __version__
from sentiment_app.predict import predict


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog="sentiment", description="Outils de classification de sentiment.")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    subparsers = parser.add_subparsers(dest="commande", required=True)

    predict_parser = subparsers.add_parser("predict", help="Prédire le sentiment d'un texte")
    predict_parser.add_argument("texte", nargs="+", help="Texte à analyser")

    serve_parser = subparsers.add_parser("serve", help="Démarrer l'API FastAPI")
    serve_parser.add_argument("--host", default="127.0.0.1")
    serve_parser.add_argument("--port", type=int, default=8000)

    ui_parser = subparsers.add_parser("ui", help="Démarrer l'interface Streamlit")
    ui_parser.add_argument("--host", default="127.0.0.1")
    ui_parser.add_argument("--port", type=int, default=8501)

    return parser.parse_args()


def main() -> int:
    args = _parse_args()

    if args.commande == "predict":
        texte = " ".join(args.texte)
        resultat = predict(texte)
        print(f"{resultat['label']} (confiance {resultat['score']:.0%})")
        return 0

    if args.commande == "serve":
        import uvicorn
        uvicorn.run("api.main:app", host=args.host, port=args.port, log_level="info")
        return 0

    if args.commande == "ui":
        import subprocess
        app_path = Path(__file__).resolve().parents[1] / "ui" / "app.py"
        return subprocess.call([sys.executable, "-m", "streamlit", "run", str(app_path), "--server.address", args.host, "--server.port", str(args.port)])

    raise ValueError(f"Commande inconnue : {args.commande}")


if __name__ == "__main__":
    raise SystemExit(main())
