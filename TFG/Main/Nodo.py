from enum import Enum
from copy import deepcopy
import sys
import time


contador = 1

class Estado(Enum):
    INDEFINIDO = 1
    VALIDO = 2
    ERROR = 3
    CONFIAR = 4
    INACEPTABLE = 5
    DESCONOCIDO = 6

class Nodo():
    #Constructor

    def __init__(self):
        global contador
            
        self.id = contador
        contador += 1
        self.nFuncion = None
        self.valor = None
        self.padre = None
        self.hijos = []
        self.nNodos = 1
        self.estado = Estado.INDEFINIDO
        self.paramsEntrada = None

    #Gestion de los parametros de entradas de cada funcion
    def setParamsEntrada(self, params):
        self.paramsEntrada = deepcopy(params)

    def getParamsEntrada(self):
        return self.paramsEntrada

    #Gestion del valor del nodo
    def setValor(self, valor):
        self.valor = deepcopy(valor)

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

    def getNombre(self):
        return self.nFuncion

    #Gestion de los hijos del nodo
    def setHijo(self, nodo):
        nodo.padre = self
        self.hijos.append(nodo)

    def insertar(self, nodo, nivel):
        self.insertarHijo(nodo,nivel,1)

    def insertarHijo(self, nodo, nivel, nActual):
        if nActual == nivel-1:
            self.setHijo(nodo)
        else:
            aux = self.hijos[len(self.hijos)-1]
            aux.insertarHijo(nodo, nivel, nActual+1)

    #Calcula el num nodos asociados a un padre
    def calcularPeso(self):
        if len(self.hijos) != 0:
            for i in self.hijos:
                self.nNodos += i.calcularPeso()

        return self.nNodos

    #Recorre el arbol. Actualmente solo sirve para comprobar que los datos estan OK
    def preorden(self):
        print("Soy la funcion:", self.getNombre())
        #print("Mi Id es:", self.id)
        print("El estado de '"+self.getNombre()+"' es:", self.estado)
        print("Los parametros de entrada de '"+self.getNombre()+"' son:", self.paramsEntrada)
        print("Num hijos de '"+self.getNombre()+"' es:", self.nNodos)
        time.sleep(1)
        if len(self.hijos) != 0:
            for i in self.hijos:
                i.preorden()
        print("Valor retornado por '"+self.getNombre()+"' es:", self.getValor())
        time.sleep(1)

    # Cada vez que el user marca como VALIDO/CONFIAR un nodo, se recorre todo el arbol buscando otros iguales para marcarlos tambien
    def recorrerNodos(self, nodoBusqueda):

        ret = 0

        if nodoBusqueda.estado == Estado.CONFIAR and nodoBusqueda.getNombre() == self.getNombre():
            self.estado = Estado.CONFIAR

        elif len(nodoBusqueda.paramsEntrada) == len(self.paramsEntrada) and nodoBusqueda.getValor() == self.getValor() and nodoBusqueda.getNombre() == self.getNombre():
            ok = True
            if len(nodoBusqueda.paramsEntrada) > 0 :
                for clave in nodoBusqueda.paramsEntrada:
                    print(self.paramsEntrada)
                    print(self.paramsEntrada.get(clave))
                    if clave in self.paramsEntrada :
                        if self.paramsEntrada.get(clave) != nodoBusqueda.paramsEntrada.get(clave):
                            ok = False
                    else:
                        ok = False

            if ok:
                self.estado = nodoBusqueda.estado

        if self.estado == Estado.ERROR or self.estado == Estado.INDEFINIDO:
            ret = 1

        if len(self.hijos) != 0:
            for i in self.hijos:
                ret += i.recorrerNodos(nodoBusqueda)

        self.nNodos = ret

        return ret

    # PENDIENTE DE REVISION POR SERGIO
    # Una vez creado el arbol, se recorre buscando nodos con hijos recursivos para fusionarlos y reducir el tamanyo final
    def fusionNodos(self):
        if len(self.hijos) != 0:
            for i in self.hijos:
                if i.getNombre() == self.getNombre():
                    self.cambiarNodo(i)
                    self.fusionNodos()
                else:
                    i.fusionNodos()

    # Cambia el valor de un nodo por otro
    def cambiarNodo(self, nodo):
        self.padre = nodo.padre
        self.nFuncion = deepcopy(nodo.nFuncion)
        self.valor = deepcopy(nodo.valor)
        self.nNodos = deepcopy(nodo.nNodos)
        self.estado = deepcopy(nodo.estado)
        self.paramsEntrada = deepcopy(nodo.paramsEntrada)
        self.hijos = deepcopy(nodo.hijos)
