'''
Created on 3 ene. 2018
@author: Jose J. Escudero Gomez
'''

import sys
import time
import Recorridos
import Nodo
import View
import Ejemplos

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

def h(hello, hola):
    f()
    return hello
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
    h("hello", "hola")
    return c() + 5


#Prueba parametros de entrada a una funcion
def j(holita):
    h()


wait = False
def trace_calls(frame, event, arg):
    global wait
    co = frame.f_code
    f_name = co.co_name
    
    if not wait: #Cuando se devuelve una excepcion, la funcion retorna mas de una cosa y desborda el arbol, esto lo controla
        if event == "return" or event == "exception":

            if f_name != "_ag" and f_name != "encode":
                
                if event == "exception":
                    arg = arg[1]
                    wait = True
                 
                paramsMods = frame.f_locals
                arbol.insertarValor(arg,contador.valor())
                arbol.insertarParamsMods(paramsMods, contador.valor())
                contador.restar()
    
        if event == "call":
            
            if f_name != "_ag" and f_name != "encode":
                
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

    else:
        wait = True
        
    return trace_calls
    

tr = sys.gettrace()  #Guardo la traza original del programa
sys.settrace(trace_calls) #Traceo la ejecucion del programa

Ejemplos.ejemplo3()

sys.settrace(tr) #Cargo la traza original guardada


arbol.fusionNodos()
arbol.calcularPeso() # Tras retornar la traza original del programa calculo el nNodos de cada nodo


View.TreeView.show(arbol)

recorrido = Recorridos.Recorrido(arbol)
recorrido.inicializarDQ()
# arbol.preorden() #Compruebo que los datos almacenados estan bien

View.TreeView.show(arbol)
