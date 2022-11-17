from funciones import nodoHuffman, crear_arbol, inorden

if __name__ == "__main__":
    #apartado A
    listanodos = [nodoHuffman("A", 0.2), nodoHuffman("F", 0.17), nodoHuffman("1", 0.13), nodoHuffman("3", 0.21), nodoHuffman("0",0.05), nodoHuffman("M",0.09), nodoHuffman("T",0.15)]
    raiz = crear_arbol(listanodos)
    inorden(raiz)