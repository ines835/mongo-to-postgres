import os
import psycopg2
from pymongo import MongoClient
from dotenv import load_dotenv

# On charge les variables d'environnement depuis .env
load_dotenv()

# Connexion MongoDB 
mongo_uri = os.getenv("MONGO_URI")
mongo_db = os.getenv("MONGO_DB")
mongo_collection = os.getenv("MONGO_COLLECTION")

client = MongoClient(mongo_uri)
collection = client[mongo_db][mongo_collection]
cursor = collection.find(batch_size=500)

# On récupère le premier document pour analyser sa structure
first_doc = next(cursor, None)

# Si la connexion est vide exit
if not first_doc:
    print("Aucun document trouvé dans la collection MongoDB.")
    exit()

columns = list(first_doc.keys())
columns_str = ", ".join([f"{col} TEXT" for col in columns])
placeholders = ", ".join(["%s"] * len(columns))

# Connexion Postgresql 
pg_conn = psycopg2.connect(
    host=os.getenv("PG_HOST"),
    port=os.getenv("PG_PORT"),
    user=os.getenv("PG_USER"),
    password=os.getenv("PG_PASSWORD"),
    dbname=os.getenv("PG_DB")
)
pg_cursor = pg_conn.cursor()

# Création propre de la table cible
pg_table = os.getenv("PG_TABLE")
pg_cursor.execute(f"DROP TABLE IF EXISTS {pg_table};")
pg_cursor.execute(f"CREATE TABLE {pg_table} ({columns_str});")

# On commence avec le premier document déja lu et on prépare la première insertion
total_inserted = 0
batch = [[str(first_doc.get(col, "")) for col in columns]]

for i, doc in enumerate(cursor, start=1):
    values = [str(doc.get(col, "")) for col in columns]
    batch.append(values)

    if len(batch) >= 500:
        pg_cursor.executemany(
            f"INSERT INTO {pg_table} ({', '.join(columns)}) VALUES ({placeholders});",
            batch
        )
        total_inserted += len(batch)
        print(f"{total_inserted} documents insérés...")
        batch = []

#  Insère les derniers documents s’il en reste après la boucle principale
if batch:
    pg_cursor.executemany(
        f"INSERT INTO {pg_table} ({', '.join(columns)}) VALUES ({placeholders});",
        batch
    )
    total_inserted += len(batch)

# Commit et fermeture des connexions
pg_conn.commit()
pg_cursor.close()
pg_conn.close()

print(f"Import terminé : {total_inserted} documents insérés dans PostgreSQL => table `{pg_table}`.")
