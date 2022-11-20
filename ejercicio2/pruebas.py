import pandas as pd
from arbol import *
from sklearn.preprocessing import LabelEncoder

pokemon = pd.read_csv("ejercicio2\pokemons.csv")

pokemon["NationalNumber"] = pokemon["NationalNumber"].str.replace("#","")
pokemon["NationalNumber"] = pd.to_numeric(pokemon["NationalNumber"], downcast = "integer")
pokemon["Type_2"] = pokemon["Type_2"].fillna("")
pokemon["Type"] = pokemon["Type_1"] + pokemon["Type_2"]
print(pokemon.head())
print(pokemon.info())

label_encoder = LabelEncoder()
pokemon['Pokemon']= label_encoder.fit_transform(pokemon['Pokemon'])
pokemon["Type"] = label_encoder.fit_transform(pokemon['Type'])


print(pokemon.head())
