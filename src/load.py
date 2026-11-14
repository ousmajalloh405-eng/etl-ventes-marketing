"""Chargement des ventes nettoyées dans SQLite."""

import sqlite3
from pathlib import Path
from typing import List, Dict


def initialiser_base(db_path: Path) -> sqlite3.Connection:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS ventes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            produit TEXT,
            categorie TEXT,
            quantite INTEGER,
            prix_unitaire REAL,
            montant REAL,
            region TEXT,
            canal TEXT
        )
    """)
    conn.execute("CREATE INDEX IF NOT EXISTS idx_date ON ventes(date)")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_categorie ON ventes(categorie)")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_region ON ventes(region)")
    conn.commit()
    return conn


def charger(conn: sqlite3.Connection, ventes: List[Dict]) -> int:
    conn.execute("DELETE FROM ventes")
    for v in ventes:
        conn.execute(
            """INSERT INTO ventes 
               (date, produit, categorie, quantite, prix_unitaire, montant, region, canal)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
            (v["date"], v["produit"], v["categorie"], v["quantite"],
             v["prix_unitaire"], v["montant"], v["region"], v["canal"]),
        )
    conn.commit()
    return len(ventes)
