# Pipeline ETL Ventes & Marketing

> Pipeline ETL simple pour analyser des données de ventes et de marketing.

**Statut** : 🟢 Réalisé  
**Catégorie** : ⚙️ Création de pipelines ETL  
**Portfolio** : [Profil GitHub](https://github.com/ousmajalloh405-eng)

---

## 1. Problème métier

Une entreprise souhaite analyser ses ventes pour comprendre :
- Le chiffre d’affaires global et par catégorie
- Les produits les plus performants
- La répartition géographique des ventes

## 2. Architecture ETL

```
generate.py → ventes_brutes.csv
      │
      ▼
 extract.py → transform.py → load.py → ventes.db
                                      │
                                      ▼
                               Indicateurs (CA, top produits…)
```

## 3. Structure du projet

```
etl-ventes-marketing/
├── src/
│   ├── generate.py    # Génération de données fictives
│   ├── extract.py     # Lecture CSV
│   ├── transform.py   # Nettoyage + calcul montant
│   └── load.py        # Insertion SQLite
├── data/
│   ├── ventes_brutes.csv
│   └── ventes.db
├── main.py
└── README.md
```

## 4. Technologies

- Python 3
- Bibliothèque standard (`csv`, `sqlite3`, `datetime`)
- SQLite

## 5. Installation et exécution

```bash
git clone https://github.com/ousmajalloh405-eng/etl-ventes-marketing.git
cd etl-ventes-marketing
python3 main.py
```

Le script :
1. Génère 500 lignes de ventes fictives
2. Les nettoie (valeurs manquantes, calcul du montant)
3. Les charge dans SQLite
4. Affiche les indicateurs clés

## 6. Indicateurs produits

- Chiffre d’affaires total
- CA par catégorie
- Top 3 produits
- CA par région

## 7. Compétences pour le CV

Développement d’un pipeline ETL Python (génération, extraction, transformation, chargement SQLite) avec calcul d’indicateurs de vente.

---

*Projet réalisé dans le cadre de la formation Data — Sonatel Academy.*
