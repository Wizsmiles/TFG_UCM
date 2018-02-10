'''
Created on 3 ene. 2018 
@author: Jose J. Escudero Gomez
'''

import sys
import time
from enum import Enum

class Estado(Enum):
    INDEFINIDO = 1
    VALIDO = 2
    ERROR = 3
    
class Nodo():
    #Constructor
    def __init__(self):
        self.nFuncion = None
        self.valor = None
        self.hijos = []
        self.id = None
        self.estado = Estado.INDEFINIDO
        
    #Gestion del valor del nodo
    def setValor(self, valor):
        self.valor = valor
        
    def getValor(self):
        return self.valor
        
    def insertarValor(self, valor, nivel):
        self.insertarValores(valor, nivel, 1)
        
    def insertarValores(self, valor, nivel, nActual):
        if nActual == nivel:
            self.setValor(valor)
        else:
            aux = self.hijos[len(self.hijos)-1]
            aux.insertarValores(valor, nivel, nActual + 1)
    
    #Gestion del nombre de la funcion del nodo
    def setNombre(self, nombre):
        self.nFuncion = nombre
        self.id =  cId.valor()
        cId.sumar()
        
    def getNombre(self):
        return self.nFuncion
    
    #Gestion de los hijos del nodo    
    def setHijo(self, nodo):
        self.hijos.append(nodo)
    
    def insertar(self, nodo, nivel):
        self.insertarHijo(nodo,nivel,1)
        
    def insertarHijo(self, nodo, nivel, nActual):
        if nActual == nivel-1:
            self.setHijo(nodo)
        else:
            aux = self.hijos[len(self.hijos)-1]
            aux.insertarHijo(nodo, nivel, nActual+1)
    
    #Recorre el arbol
    def preorden(self):
        print("Soy la funcion:", self.getNombre())
        #print("Mi Id es:", self.id)
        print("El estado de '"+self.getNombre()+"' es:", self.estado)
        time.sleep(1)
        if len(self.hijos) != 0:
            for i in self.hijos:
                i.preorden()
        print("Valor retornado por '"+self.getNombre()+"' es:", self.getValor())
        time.sleep(1)
    
class MiContador():
    count = 0
    
    def sumar(self):
        self.count += 1
        #print("Valor contador:", self.count)
    def restar(self):
        self.count -= 1
        #print("Valor contador:", self.count)
    def valor(self):
        return self.count

class nContador():
    count = 1
    
    def sumar(self):
        self.count += 1

    def valor(self):
        return self.count

arbol = Nodo()
contador = MiContador()
cId = nContador()

def h():
    return "Hola"
def f():
    "hola"      
def a():
    f()
    return 6
def b():
    return 2 + a()
def c():
    return b() + b() + a() + 3
def d():
    h()
    return c() + 5

def trace_calls(frame, event, arg):
    
    if event == "return":
        arbol.insertarValor(arg,contador.valor())
        contador.restar()
            
    if event == "call":
        co = frame.f_code
        f_name = co.co_name
        if f_name != "_ag":
            contador.sumar()
            if contador.valor() == 1:
                arbol.setNombre(f_name)
            else:
                hijo = Nodo()
                hijo.setNombre(f_name)
                arbol.insertar(hijo, contador.valor())
                
    return trace_calls
tr = sys.gettrace()   
sys.settrace(trace_calls)

d()
sys.settrace(tr)

def aux(frame, event, arg):
    return

sys.settrace(aux)

arbol.preorden()