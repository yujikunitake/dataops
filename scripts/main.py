import pandas as pd


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

