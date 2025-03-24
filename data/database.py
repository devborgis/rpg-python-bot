import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Carregar .env
load_dotenv()

# Montar URL de conexão MongoDB
MONGO_URL = (
  f"mongodb+srv://{os.getenv('MONGO_USER')}:{os.getenv('MONGO_PASSWORD')}"
  f"@{os.getenv('MONGO_CLUSTER')}/?retryWrites=true&w=majority&appName=Cluster0"
)

# Conectar ao Mongo
client = MongoClient(MONGO_URL)

# Definindo Banco de dados e as collections
db = client[os.getenv("MONGO_DB")]

# Testar Conexão
def TestarMongo():
  try:
      client.admin.command("ping")
      print("Conectado ao mongoDB, Sucesso")
  except Exception as e:
      print(f"Erro ao conectar mongoDB: {e}")