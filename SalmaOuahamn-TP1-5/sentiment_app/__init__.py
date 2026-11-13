"""Paquet d'installation du modèle de sentiment."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("sentiment_app")
except PackageNotFoundError:  # pragma: no cover
    __version__ = "0.6.0"
