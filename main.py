"""Pipeline ETL Ventes & Marketing."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "src"))

from generate import generer_ventes
from extract import extraire
from transform import transformer
from load import initialiser_base, charger


CSV_PATH = Path(__file__).parent / "data" / "ventes_brutes.csv"
DB_PATH = Path(__file__).parent / "data" / "ventes.db"


def afficher_indicateurs(conn):
    print("\n=== Indicateurs clés ===")

    ca = conn.execute("SELECT ROUND(SUM(montant), 2) FROM ventes").fetchone()[0]
    print(f"Chiffre d'affaires total : {ca} €")

    print("\nCA par catégorie :")
    for row in conn.execute("""
        SELECT categorie, ROUND(SUM(montant), 2) AS ca
        FROM ventes
        GROUP BY categorie
        ORDER BY ca DESC
    """):
        print(f"  {row[0]:15} {row[1]} €")

    print("\nTop 3 produits :")
    for row in conn.execute("""
        SELECT produit, ROUND(SUM(montant), 2) AS ca
        FROM ventes
        GROUP BY produit
        ORDER BY ca DESC
        LIMIT 3
    """):
        print(f"  {row[0]:20} {row[1]} €")

    print("\nCA par région :")
    for row in conn.execute("""
        SELECT region, ROUND(SUM(montant), 2) AS ca
        FROM ventes
        GROUP BY region
        ORDER BY ca DESC
    """):
        print(f"  {row[0]:15} {row[1]} €")


def main():
    print("=== Pipeline ETL Ventes & Marketing ===\n")

    generer_ventes(500, CSV_PATH)

    brut = extraire(CSV_PATH)
    print(f"Lignes extraites : {len(brut)}")

    propres = transformer(brut)
    print(f"Lignes après nettoyage : {len(propres)}")

    conn = initialiser_base(DB_PATH)
    nb = charger(conn, propres)
    print(f"Lignes chargées dans {DB_PATH} : {nb}")

    afficher_indicateurs(conn)

    conn.close()
    print("\nPipeline terminé.")


if __name__ == "__main__":
    main()
