class nodoArbol:
    def __init__(self, info, datos):
        self.izquierda = None
        self.derecha = None
        self.datos = datos
        self.info = info
        self.altura = 0

def altura(raiz):
    if raiz is None:
        return -1
    else:
        return raiz.altura

def actualizar_altura(raiz):
    if raiz is not None:
        altura_izquierda = altura(raiz.izquierda)
        altura_derecha = altura(raiz.derecha)
        raiz.altura = (altura_izquierda if altura_izquierda > altura_derecha else altura_derecha) +1

#control:True    ROTACIÓN DERECHA
def rotar_simple(raiz, control):
    if control:
        aux = raiz.izquierda
        raiz.izquierda = aux.derecha
        aux.derecha = raiz
    else:
        aux = raiz.derecha
        raiz.derecha = aux.izquierda
        aux.izquierda = raiz

def rotar_doble(raiz, control):
    if control:
        raiz.izquierda = rotar_simple(raiz.izquierda, False)
        raiz = rotar_simple(raiz, True)
    else:
        raiz.derecha = rotar_simple(raiz.derecha, True)
        raiz = rotar_simple(raiz, False)
    return raiz

def balancear(raiz):
    if raiz is not None:
        if (altura(raiz.izquierda)-altura(raiz.derecha)) == 2:
            if altura(raiz.izquierda.izquierda) >= altura(raiz.izquierda.derecha):
                raiz = rotar_simple(raiz, True)
            else: 
                raiz = rotar_doble(raiz, True)
        elif(altura(raiz.derecha)-altura(raiz.izquierda)) == 2:
            if altura(raiz.derecha.derecha) >= altura(raiz.derecha.derecha):
                raiz = rotar_simple(raiz, False)
            else: 
                raiz = rotar_doble(raiz, False)
    return raiz

def insertarnodo(raiz,dato, datos):
    if raiz == None:
        print("el nodo es la raiz")
        raiz = nodoArbol(dato, datos)
    else:

        while True:
            if dato<raiz.info:
                if raiz.izquierda is None:
                    raiz.izquierda = nodoArbol(dato, datos)
                    raiz.izquierda.padre = raiz
                    break
                else:
                    raiz = raiz.izquierda
            else:
                if raiz.derecha is None:
                    raiz.derecha = nodoArbol(dato, datos)
                    raiz.derecha.padre = raiz
                    break
                else:
                    raiz = raiz.derecha
    raiz = balancear(raiz)
    actualizar_altura(raiz)
    return raiz

def reemplazar(raiz):
    #aux es donde guardamos la raiz a reemplazar
    aux = None
    # si no hay raiz derecha, reemplazamos directamente por la raiz izquierda y el arbol sigue funcionando igual
    if raiz.derecha is None:
        aux = raiz
        raiz = raiz.izquierda
    #si hay raiz derecha 
    else: 
        raiz.derecha, aux = reemplazar(raiz.derecha)
    return raiz, aux

def eliminar_nodo(raiz, clave):
    x = None
    if (raiz is not None):
        raiz.izquierda, x = eliminar_nodo(raiz.izquierda, clave)
    elif(clave > raiz.info):
        raiz.derecha, x = eliminar_nodo(raiz.derecha, clave)
    else:
        x = raiz.info
        if raiz.izquierda is None:
            raiz = raiz.derecha
        elif raiz.derecha is None:
            raiz = raiz.izquierda
        else:
            raiz.izquierda, aux = reemplazar(raiz.izquierda)
    raiz = balancear(raiz)
    actualizar_altura(raiz)
    return raiz, x

def buscar(raiz, clave):
    pos = None
    if raiz is not None:
        if(raiz.info == clave):
            pos = raiz
        elif clave < raiz.info:
            pos = buscar(raiz.izquierda, clave)
        else:
            pos = buscar(raiz.derecha, clave)
    return pos


