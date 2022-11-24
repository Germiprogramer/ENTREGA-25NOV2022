from creacion_grafos import grafo_naturales, grafo_arquitectonicas
from grafo import intentodeprim, comun_listas, settear_listar


#grafos de expansion

grafo_minimo_n = intentodeprim(grafo_naturales)
grafo_minimo_a = intentodeprim(grafo_arquitectonicas)

#determinar si existen paises que dispongas de maravillas arquitectonicas y naturales

def paises_con_ambas(a, b):
    lista_n = []
    lista_a = []
    for i in a.vertices:
        lista_n.append(i.info.pais)
    for j in b.vertices:
        lista_a.append(j.info.pais)
    lista_n = settear_listar(lista_n)
    lista_a = settear_listar(lista_a)
    elementos_comun = comun_listas(lista_n, lista_a)
    return elementos_comun

print(paises_con_ambas(grafo_naturales, grafo_arquitectonicas))

#determinar si existen paises que tengan mas de una maravilla

def masdeunamar(a,b):
    listarepes = []
    lista_n = []
    lista_a = []
    for i in a.vertices:
        lista_n.append(i.info.pais)
    for j in b.vertices:
        lista_a.append(j.info.pais)
    for a in lista_a:
        lista_a.remove(a)
        if a in lista_a:
            listarepes.append(a)
    for b in lista_n:
        lista_n.remove(b)
        if b in lista_n:
            listarepes.append(b)
    return listarepes

print(masdeunamar(grafo_naturales, grafo_arquitectonicas))




