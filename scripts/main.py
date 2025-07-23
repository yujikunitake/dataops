import pandas as pd
from pymongo import MongoClient


# Criar dataframes
df_carros = pd.DataFrame([
    {"Carro": "Onix", "Cor": "Prata", "Montadora": "Chevrolet"},
    {"Carro": "Polo", "Cor": "Branco", "Montadora": "Volkswagen"},
    {"Carro": "Sandero", "Cor": "Prata", "Montadora": "Renault"},
    {"Carro": "Fiesta", "Cor": "Vermelho", "Montadora": "Ford"},
    {"Carro": "City", "Cor": "Preto", "Montadora": "Honda"}
])

df_montadoras = pd.DataFrame([
    {"Montadora": "Chevrolet", "País": "EUA"},
    {"Montadora": "Volkswagen", "País": "Alemanha"},
    {"Montadora": "Renault", "País": "França"},
    {"Montadora": "Ford", "País": "EUA"},
    {"Montadora": "Honda", "País": "Japão"}
])

# Conectar com MongoDB
client = MongoClient("mongodb://localhost:27017")
db = client["dataops_db"]

# Limpar collections antes de inserir (evitando duplicação)
db["Carros"].delete_many({})
db["Montadoras"].delete_many({})

# Inserir no MongoDB
db["Carros"].insert_many(df_carros.to_dict("records"))
db["Montadoras"].insert_many(df_montadoras.to_dict("records"))

print("Dados inseridos com sucesso no MongoDB.")
