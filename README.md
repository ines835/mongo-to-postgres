##  Prérequis

- [Docker Desktop](https://www.docker.com/products/docker-desktop)
- [Python 3.10+](https://www.python.org/downloads/)

## Installation

Cloner le dépôt 

```bash
git clone https://github.com/ines835/mongo-to-postgres.git
cd mongo-to-postgres
```


## Configurer les variables d'env

copy .env.example .env


## Lancer le script auto

run.bat


## Dans Power BI Desktop :

Source de données : PostgreSQL

Serveur : localhost:5433

Base : mongodata

Utilisateur : pguser

Mot de passe : pgpass

Charger la table spécifiée dans .env (PG_TABLE)