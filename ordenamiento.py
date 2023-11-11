import time
import random
from lista import *

def crearlista(n):
    lista = Lista()
    while lista.tamanio != n:
        numero = random.randint(1,100000)
        insertar(lista, numero)
    return lista

def buscar_index(lista, pos):
    contador = 0
    actual = lista.inicio
    while actual is not None:
        if contador == pos:
            return actual.info
        actual = actual.siguiente
        contador += 1

def remplazar(lista,info,pos):
    contador = 0
    actual = lista.inicio
    while actual is not None:
        if contador == pos:
            actual.info = info
            break
        actual = actual.siguiente
        contador += 1

def burbuja(lista):
    for i in range(0, lista.tamanio - 1):
        for j in range(0, lista.tamanio - i - 1):
            a = buscar_index(lista, j)
            b = buscar_index(lista,j+1)
            if a > b:
                remplazar(lista, b, j)
                remplazar(lista,a,j+1)

def burbujaMejorada(lista):
    i = 0
    control = True
    while (i <= lista.tamanio - 2) and control:
        control = False
        for j in range(0, lista.tamanio - i - 1):
            a = buscar_index(lista, j)
            b = buscar_index(lista,j+1)
            if a > b:
                remplazar(lista,b,j)
                remplazar(lista,a,j+1)
                control = True
        i = i + 1

def burbujaBidireccional(lista):
    izquierda = 0
    derecha = lista.tamanio - 1
    control = True
    while (izquierda < derecha) and control:
        control = False
        for i in range(izquierda, derecha):
            a = buscar_index(lista, i)
            b = buscar_index(lista,i+1)
            if a > b:
                remplazar(lista,b,i)
                remplazar(lista,a,i + 1)
                control = True
        derecha -= 1
        for j in range(derecha, izquierda, -1):
            c = buscar_index(lista, j)
            d = buscar_index(lista,j-1)
            if c < d:
                remplazar(lista,d,j)
                remplazar(lista,c,j-1)
                control = True
        izquierda += 1

def seleccion(lista):
    for i in range(0, lista.tamanio-1):
        minimo = i
        for j in range(i+1, lista.tamanio):
            b = buscar_index(lista, j)
            c = buscar_index(lista,minimo)
            if b < c:
                minimo = j
        c = buscar_index(lista,minimo)
        a = buscar_index(lista, i)
        remplazar(lista,c,i)
        remplazar(lista,a,minimo)

def insercion(lista):
    for i in range(1, lista.tamanio + 1):
        k = i - 1
        a = buscar_index(lista,k)
        b = buscar_index(lista,k-1)
        while (k > 0) and a < b:
            remplazar(lista,b,k)
            remplazar(lista,a,k-1)
            k -= 1
            a = buscar_index(lista,k)
            b = buscar_index(lista,k-1)

def ordenamientoRapido(lista, primero, ultimo):
    izquierda = primero
    derecha = ultimo - 1
    pivote = ultimo
    while izquierda < derecha:
        a = buscar_index(lista,izquierda)
        b = buscar_index(lista,derecha)
        c = buscar_index(lista,pivote)
        while a < c and izquierda <= derecha:
            izquierda += 1
            a = buscar_index(lista,izquierda)
            b = buscar_index(lista,derecha)
            c = buscar_index(lista,pivote)
        while b > c and derecha >= izquierda:
            derecha -= 1
            a = buscar_index(lista,izquierda)
            b = buscar_index(lista,derecha)
            c = buscar_index(lista,pivote)
        if izquierda < derecha:
            a = buscar_index(lista,izquierda)
            b = buscar_index(lista,derecha)
            remplazar(lista,b,izquierda)
            remplazar(lista,a,derecha)
    a = buscar_index(lista,izquierda)
    b = buscar_index(lista,derecha)
    c = buscar_index(lista,pivote)
    if c < a:
        remplazar(lista,c,izquierda)
        remplazar(lista,a,pivote)
    if primero < izquierda:
        ordenamientoRapido(lista, primero, izquierda - 1)
    if ultimo > izquierda:
        ordenamientoRapido(lista, izquierda + 1, ultimo)

def ordenamientoMezcla(lista):
    izquierda = Lista()
    derecha = Lista()
    if lista.tamanio <= 1:
        return lista
    else:
        medio = lista.tamanio // 2
        for i in range(0, medio):
            insertar(izquierda,buscar_index(lista,i))
        for i in range(medio, lista.tamanio):
            insertar(derecha,buscar_index(lista,i))
        izquierda = ordenamientoMezcla(izquierda)
        derecha = ordenamientoMezcla(derecha)
        if buscar_index(izquierda,medio - 1) <= buscar_index(derecha,0):
            actual = derecha.inicio
            while actual is not None:
                insertar(izquierda,actual.info)
                actual = actual.siguiente
            return izquierda
        resultado = mezcla(izquierda, derecha)
        return resultado

def mezcla(izquierda, derecha):
    lista_mezclada = Lista()
    while izquierda.tamanio > 0 and (derecha.tamanio > 0):
        a = buscar_index(izquierda,0)
        b = buscar_index(derecha,0)
        if a < b:
            insertar(lista_mezclada,pop(izquierda,0))
        else:
            insertar(lista_mezclada,pop(derecha,0))
    if izquierda.tamanio > 0:
        actual = izquierda.inicio
        while actual is not None:
            insertar(lista_mezclada,actual.info)
            actual = actual.siguiente
    if derecha.tamanio > 0:
        actual = derecha.inicio
        while actual is not None:
            insertar(lista_mezclada,actual.info)
            actual = actual.siguiente
    return lista_mezclada

def insertarNodo(raiz, info):
    if(raiz is None):
        raiz = nodoArbol(info)
    elif(info < raiz.info):
        raiz.izq = insertarNodo(raiz.izq,info)
    else:
        raiz.der = insertarNodo(raiz.der,info)
    return raiz

def arbolVacio(raiz):
    return raiz is None

def ordenar_arbol(lista,num):
    raiz = None
    contador = 0
    actual = lista.inicio
    while contador < num:
        raiz = insertarNodo(raiz, actual.info)
        actual = actual.siguiente
        contador += 1
    return raiz

def imprimirInOrden(raiz):
    if(raiz is not None):
        imprimirInOrden(raiz.izq)
        print(raiz.info)
        imprimirInOrden(raiz.der)

def calcular_time(lista):
    inicio = time.time()
    ordenar_arbol(lista,lista.tamanio)
    fin = time.time()
    print(fin-inicio)

def main():
    n = 50000
    lista = crearlista(n)
    print(n,":")
    calcular_time(lista)

if __name__ == "__main__":
    main()