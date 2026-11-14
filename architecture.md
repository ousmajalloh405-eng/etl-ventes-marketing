# Architecture — ETL Ventes & Marketing

## Flux

```
┌──────────────┐
│ generate.py  │  →  data/ventes_brutes.csv
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  extract.py  │  Lecture du CSV
└──────┬───────┘
       │
       ▼
┌──────────────┐
│ transform.py │  Nettoyage + calcul montant
└──────┬───────┘
       │
       ▼
┌──────────────┐
│   load.py    │  →  data/ventes.db (SQLite)
└──────┬───────┘
       │
       ▼
   Indicateurs
   (CA, top produits, régions)
```

## Tables

**ventes**
- date, produit, categorie, quantite, prix_unitaire, montant, region, canal

## Index

- Sur `date`, `categorie`, `region`
