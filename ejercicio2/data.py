import pandas as pd
from arbol import *

pokemon = pd.read_csv("ejercicio2\pokemons.csv")

pokemon["NationalNumber"] = pokemon["NationalNumber"].str.replace("#","")
pokemon["NationalNumber"] = pd.to_numeric(pokemon["NationalNumber"], downcast = "integer")
print(pokemon.head())
print(pokemon.info())

class Pokemon():
    def __init__(self, nombre, numero, tipo):
        self.nombre = nombre
        self.numero = numero
        self.tipo = tipo



#def crear_arbol_numero(pokemon):
    #raiz = None
    #for elemento in pokemon:
        #insertarnodo(raiz, elemento[])

