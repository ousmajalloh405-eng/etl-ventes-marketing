"""Extraction des données de ventes depuis le CSV."""

import csv
from pathlib import Path
from typing import List, Dict


def extraire(fichier: Path) -> List[Dict]:
    """Lit le CSV brut et retourne une liste de dictionnaires."""
    lignes = []
    with open(fichier, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            lignes.append(row)
    return lignes
