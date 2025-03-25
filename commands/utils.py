# Buscar Campanha Ativa MongoDB
def search_campanha(server_id, db):
  return db.campanhas.find_one({"server_id": server_id, "status": "ativa"})
