from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

uri = os.getenv("MONGO_URI")
print(f"🔐 URI utilisée : {uri}")


client = MongoClient(os.getenv("MONGO_URI"))
db = client[os.getenv("MONGO_DB")]
collection = db[os.getenv("MONGO_COLLECTION")]

print("✅ Connexion réussie.")
print("📄 Exemple :", collection.find_one())
