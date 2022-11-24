class Maravilla():
    def __init__(self, nombre, pais, tipo):
        self.nombre = nombre
        self.pais = pais
        self.tipo = tipo

class nodoVertice():
    def __init__(self, info):
        self.info = info
        self.visitado = False
        self.sig = None #aqui ira un nodoarista
        self.adyacentes = lista_Aristas()

class nodoArista():
    def __init__(self, distancia, destino):
        self.distancia = distancia
        self.destino = destino
        self.sig = None

class lista_Aristas():
    def __init__(self):
        self.aristas= []
        self.tamanio = len(self.aristas)
    def printear_aristas(self):
        for i in self.aristas:
            print(f"la distancia a {i.destino.info.nombre} es {i.distancia}")



class Grafo():
    def __init__(self, dirigido = True):
        self.vertices = []
        self.dirigido = dirigido
        self.tamanio = 0

    def print_vertices(self):
        for i in self.vertices:
            print(i.info.nombre)

    def llamar_vertice(self, nombre):
        for i in self.vertices:
            if i.info.nombre == nombre:
                return i
            else: 
                pass
    
    def print_vertices_aristas(self):
        for i in self.vertices:
            print(f"las aristas de {i.info.nombre}son:  ")
            i.adyacentes.printear_aristas()

def insertar_vertice(grafo, dato):
    #hacemos que la clase Maravilla sea el dato
    aux = nodoVertice(dato)
    dato = aux
    grafo.vertices.append(dato)

def insertar_arista(grafo, dato, origen, destino):
    o = False
    d = False
    for i in grafo.vertices:
        if origen == i.info.nombre:
            o = True 
            origen = i
        else: 
            pass
        if destino == i.info.nombre:
            d = True
            destino = i
        else: 
            pass
    if o is True and d is True:
        agregar_arista(origen, dato, destino)
        if not grafo.dirigido:
            agregar_arista(destino, dato, origen)
    else:
        print("Uno de los dos vértices no está en el grafo")

def agregar_arista(origen, dato, destino):
    nodo = nodoArista(dato, destino)
    origen.adyacentes.aristas.append(nodo)



#grafo.print_vertices()

#print(grafo.llamar_vertice("Coloso de Rodas").info.pais)
#print(grafo.vertices[0].adyacentes)

#grafo.vertices[0].adyacentes.printear_aristas()

def intentodeprim(grafo):
    aux = grafo
    vertice = aux.vertices[0]
    distancia_total = 0
    while True:
        vertice.visitado = True
        distancia = 1000000000
        for i in vertice.adyacentes.aristas:
            if i.distancia < distancia and i.destino.visitado is False:
                vertice_dist_min = i.destino.info.nombre
                distancia = i.distancia
                arista = i
            
            #eliminar las aristas que no hemos seleccionado
        vertice.adyacentes.aristas = [arista]

        vertice = aux.llamar_vertice(vertice_dist_min)
            
        if distancia == 1000000000:
            
            break
        else:
            
            distancia_total+=distancia
    return aux
        
def comun_listas(a, b):
    lista_final = []
    for i in a:
        if (i not in lista_final) and (i in b):
            lista_final.append(i)
    return lista_final

#print(intentodeprim(grafo))
#grafo.print_vertices_aristas()

def settear_listar(lista):
    lista = set(lista)
    lista = list(lista)
    return lista

print(settear_listar([1,2,2,3,4,3]))








