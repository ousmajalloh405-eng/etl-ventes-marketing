"""Transformation et nettoyage des données de ventes."""

from typing import List, Dict
from datetime import datetime


def transformer(lignes: List[Dict]) -> List[Dict]:
    """Nettoie les données et calcule le montant."""
    propres = []
    for ligne in lignes:
        try:
            quantite = int(ligne["quantite"]) if ligne["quantite"] else 0
            if quantite <= 0:
                continue
            prix = float(ligne["prix_unitaire"])
            montant = round(quantite * prix, 2)
            date = datetime.strptime(ligne["date"], "%Y-%m-%d").date()
            propres.append({
                "date": date.isoformat(),
                "produit": ligne["produit"].strip(),
                "categorie": ligne["categorie"].strip(),
                "quantite": quantite,
                "prix_unitaire": prix,
                "montant": montant,
                "region": ligne["region"].strip(),
                "canal": ligne["canal"].strip(),
            })
        except (ValueError, KeyError):
            continue
    return propres
