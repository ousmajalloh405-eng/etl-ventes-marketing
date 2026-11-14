"""Génération de données fictives de ventes."""

import csv
import random
from datetime import datetime, timedelta
from pathlib import Path

PRODUITS = [
    ("Laptop", "Informatique", 850),
    ("Smartphone", "Informatique", 420),
    ("Casque audio", "Accessoires", 89),
    ("Livre Python", "Livres", 35),
    ("Chaise bureau", "Mobilier", 150),
    ("Café premium", "Alimentation", 12),
    ("T-shirt", "Mode", 25),
    ("Montre connectée", "Accessoires", 199),
]

REGIONS = ["Dakar", "Thiès", "Saint-Louis", "Ziguinchor", "Kaolack"]


def generer_ventes(n: int = 500, fichier: Path = Path("data/ventes_brutes.csv")) -> None:
    fichier.parent.mkdir(parents=True, exist_ok=True)
    debut = datetime(2026, 1, 1)
    with open(fichier, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["date", "produit", "categorie", "quantite", "prix_unitaire", "region", "canal"])
        for _ in range(n):
            produit, categorie, prix = random.choice(PRODUITS)
            date = debut + timedelta(days=random.randint(0, 300))
            quantite = random.randint(1, 8)
            region = random.choice(REGIONS)
            canal = random.choice(["en ligne", "magasin", "partenaire"])
            if random.random() < 0.03:
                quantite = ""
            writer.writerow([
                date.strftime("%Y-%m-%d"),
                produit,
                categorie,
                quantite,
                prix,
                region,
                canal,
            ])
    print(f"{n} lignes générées dans {fichier}")
