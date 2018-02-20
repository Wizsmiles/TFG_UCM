'''
Created on 3 ene. 2018
@author: Jose J. Escudero Gomez
'''

import sys
import time
import Recorridos
import Nodo
import View

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

arbol = Nodo.Nodo()

contador = MiContador()

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


#Prueba parametros de entrada a una funcion
def j(holita):
    h()


def trace_calls(frame, event, arg):

    co = frame.f_code
    f_name = co.co_name
    
    if event == "return":
        if f_name != "_ag" and f_name != "encode":
            arbol.insertarValor(arg,contador.valor())
            contador.restar()
                
    if event == "call":
        if f_name != "_ag" and f_name != "encode":
            # Guarda un diccionario con los parametros de entrada de la funcion llamada, si no hay params el diccionario esta vacio
            paramsEntrada = frame.f_locals
            contador.sumar()
            
            if contador.valor() == 1:
                arbol.setNombre(f_name)
                arbol.setParamsEntrada(paramsEntrada)
                
            else:
                hijo = Nodo.Nodo()
                hijo.setNombre(f_name)
                hijo.setParamsEntrada(paramsEntrada)
                arbol.insertar(hijo, contador.valor())

    return trace_calls

tr = sys.gettrace()  #Guardo la traza original del programa
sys.settrace(trace_calls) #Traceo la ejecucion del programa
d() #Ejecuto el programa de prueba
#j("ey")
sys.settrace(tr) #Cargo la traza original guardada
arbol.calcularPeso() # Tras retornar la traza original del programa calculo el nNodos de cada nodo
recorrido = Recorridos.Recorrido(arbol)
recorrido.inicializarHF()
# arbol.preorden() #Compruebo que los datos almacenados estan bien
View.TreeView.show(arbol)
