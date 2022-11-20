import pandas as pd
from arbol import *


pokemon = pd.read_csv("ejercicio2\pokemons.csv")

#limpieza dataset
pokemon["NationalNumber"] = pokemon["NationalNumber"].str.replace("#","")
pokemon["NationalNumber"] = pd.to_numeric(pokemon["NationalNumber"], downcast = "integer")


pokemon["Type_2"] = pokemon["Type_2"].fillna("")
pokemon["Type"] = pokemon["Type_1"] + pokemon["Type_2"]


print(pokemon.head())
print(pokemon.info())

class Pokemon():
    def __init__(self, nombre, numero, tipo):
        self.nombre = nombre
        self.numero = numero
        self.tipo = tipo

    def __str__(self):
        print(f"Nombre: {self.nombre} ")



def crear_arbol_numero(pokemon):
    raiz = nodoArbol(pokemon["NationalNumber"][0], Pokemon(pokemon["Pokemon"][0], pokemon["NationalNumber"][0], pokemon["Type"][0]))
    for elemento in pokemon:
        insertarnodo(raiz, elemento["NationalNumber"], Pokemon(elemento["Pokemon"], elemento["NationalNumber"], elemento["Type"]))
    return raiz

def crear_arbol_nombre(pokemon):
    pass

raiz = crear_arbol_numero(pokemon)

