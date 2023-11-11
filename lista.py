class nodoListaSimple(object):
    info, siguiente = None, None

class Lista(object):
    def __init__(self):
        self.inicio = None
        self.tamanio = 0

class nodoArbol(object):
    def __init__(self, info):
        self.izq = None
        self.der = None
        self.info = info

def insertar(lista, info):
    nodo = nodoListaSimple()
    nodo.info = info
    if lista.inicio is None:
        nodo.siguiente = lista.inicio
        lista.inicio = nodo
    else:
        actual = lista.inicio
        siguiente = lista.inicio.siguiente
        while siguiente is not None:
            actual = actual.siguiente
            siguiente = siguiente.siguiente
        nodo.siguiente = siguiente
        actual.siguiente = nodo
    lista.tamanio += 1

def pop(lista,ind):
    contador = 0
    data = None
    if(contador == ind):
        data = lista.inicio.info
        lista.inicio = lista.inicio.siguiente
        lista.tamanio -= 1
        return data
    else:      
        actual = lista.inicio
        siguiente = lista.inicio.siguiente
        while (siguiente is not None and ind != contador +1):
            actual = actual.siguiente
            siguiente = siguiente.siguiente
            contador += 1
        if(siguiente is not None):
            data = siguiente.info
            actual.siguiente = siguiente.siguiente
            lista.tamanio -= 1
            return data

def imprimir(lista):
    actual = lista.inicio
    while actual is not None:
        print(actual.info)
        actual = actual.siguiente

def tamanio(lista):
    return lista.tamanio