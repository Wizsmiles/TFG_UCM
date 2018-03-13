'''
Created on 13 mar. 2018

@author: Jose J. Escudero Gomez
'''

# Codigo ejemplo 1 - Retornos de funciones anidadas

def h(param1, param2):
    f()
    return param1

def f():
    "hola"
    
def a():
    f()
    return 6

def b():
    return 2 + a()

def c():
    return b() + b() + a() + 3

def ejemplo1():
    h("hello", "hola")
    return c() + 5


# Codigo ejemplo 2 - Modificacion de listas

def ejemplo2_1(lista):
    lista.append("2")
    return lista

def ejemplo2_2(lista, str):
    lista.pop()
    lista.append(str)
    return lista
    
def ejemplo2_3(lista):
    lista.append("4")
    return lista

def ejemplo2():
    lista = []
    lista.append("1");
    ejemplo2_1(lista)
    ejemplo2_2(lista, "3")
    ejemplo2_3(lista)