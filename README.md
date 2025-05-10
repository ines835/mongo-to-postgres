
# Migration de MongoDB Atlas vers PostgreSQL – dockerisé et prêt à l’emploi.

Transfère une collection MongoDB hébergée sur Atlas vers une base PostgreSQL — utile pour de l’analyse, un audit ou une intégration Power BI.

##  Prérequis

- [Docker Desktop](https://www.docker.com/products/docker-desktop)
- [Python 3.10+](https://www.python.org/downloads/)
- Un compte MongoDB Atlas (avec un utilisateur et un cluster configuré)

## Installation

```bash
git clone https://github.com/ines835/mongo-to-postgres.git
cd mongo-to-postgres
copy .env.example .env  # (sous Windows)

```

## Lancer la migration

Sous windows
```bash
start run.bat
```
Ce script :
se connecte à MongoDB Atlas
crée la table si besoin dans PostgreSQL
copie les données de la collection dans la table

## Intégration dans Power BI Desktop 

Dans Power BI, choisis :
Source de données > PostgreSQL

Serveur : localhost:5432 
Base de données : mongodata

(tes identifiants)
Utilisateur : pguser 
Mot de passe : pgpass

Puis sélectionne la table définie dans .env (PG_TABLE).

