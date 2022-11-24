class Maravilla():
    def __init__(self, nombre, pais, tipo):
        self.nombre = nombre
        self.pais = pais
        self.tipo = tipo

#creamos las maravillas, cada una de ellas será un vértice

estatuadeZeus = Maravilla("Estatua de Zeus", "Grecia", "Natural")
templodeArtemisa = Maravilla("Templo de Artemisa", "Turquia", "Natural")
mausoleo_halicarnaso = Maravilla("Mausoleo Halicarnaso", "Turquia", "Natural")
jardines_colgantes = Maravilla("Jardines colgantes", "Irak", "Natural")
coloso_rodas = Maravilla("Coloso de Rodas", "Grecia", "Natural")
faro_alejandria = Maravilla("Faro de Alejandria", "Egipto", "Natural")
piramide = Maravilla("Piramide de Guiza", "Egipto", "Natural")

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

#creacion del grafo

grafo = Grafo(False)

insertar_vertice(grafo, estatuadeZeus)
insertar_vertice(grafo, templodeArtemisa)
insertar_vertice(grafo, mausoleo_halicarnaso)
insertar_vertice(grafo, jardines_colgantes)
insertar_vertice(grafo, coloso_rodas)
insertar_vertice(grafo, faro_alejandria)
insertar_vertice(grafo, piramide)

insertar_arista(grafo, 1000, "Estatua de Zeus", "Templo de Artemisa")
insertar_arista(grafo, 2000, "Estatua de Zeus", "Mausoleo Halicarnaso")
insertar_arista(grafo, 3000, "Estatua de Zeus", "Jardines colgantes")
insertar_arista(grafo, 4000, "Estatua de Zeus", "Coloso de Rodas")
insertar_arista(grafo, 5000, "Estatua de Zeus", "Faro de Alejandria")
insertar_arista(grafo, 6000, "Estatua de Zeus", "Piramide de Guiza")

insertar_arista(grafo, 3000, "Templo de Artemisa", "Mausoleo Halicarnaso")
insertar_arista(grafo, 3000, "Templo de Artemisa", "Jardines colgantes")
insertar_arista(grafo, 5000, "Templo de Artemisa", "Coloso de Rodas")
insertar_arista(grafo, 5000, "Templo de Artemisa", "Faro de Alejandria")
insertar_arista(grafo, 7000, "Templo de Artemisa", "Piramide de Guiza")

insertar_arista(grafo, 4000, "Mausoleo Halicarnaso", "Jardines colgantes")
insertar_arista(grafo, 1000, "Mausoleo Halicarnaso", "Coloso de Rodas")
insertar_arista(grafo, 2000, "Mausoleo Halicarnaso", "Faro de Alejandria")
insertar_arista(grafo, 3000, "Mausoleo Halicarnaso", "Piramide de Guiza")

insertar_arista(grafo, 2000, "Jardines colgantes", "Coloso de Rodas")
insertar_arista(grafo, 5000, "Jardines colgantes", "Faro de Alejandria")
insertar_arista(grafo, 2000, "Jardines colgantes", "Piramide de Guiza")

insertar_arista(grafo, 8000, "Coloso de Rodas", "Faro de Alejandria")
insertar_arista(grafo, 1000, "Coloso de Rodas", "Piramide de Guiza")

insertar_arista(grafo, 1000, "Faro de Alejandria", "Piramide de Guiza")



grafo.print_vertices()

#print(grafo.llamar_vertice("Coloso de Rodas").info.pais)
print(grafo.vertices[0].adyacentes)

#grafo.vertices[0].adyacentes.printear_aristas()






