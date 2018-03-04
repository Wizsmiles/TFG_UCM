import Nodo
from enum import Enum
import sys

class Estrategia(Enum):
    TOPDOWN = 1
    HEAVIESTFIRST = 2

class Recorrido():
    def __init__(self, tree):
        self.arbol = tree
        self.estrategia = Estrategia.HEAVIESTFIRST
        self.arbol.estado = Nodo.Estado.ERROR
        self.errores = []
        self.buggy = False

    def inicializarTD(self):
        self.topDown(self.arbol)

    def topDown(self, nodo):
        if len(nodo.hijos) != 0:
            validos = 0
            for i in nodo.hijos:
                if i.estado == Nodo.Estado.INDEFINIDO:
                    self.ask(i)
                    if(i.estado == Nodo.Estado.ERROR):
                        break
        else:
            self.buggy = True

    def inicializarHF(self):
        self.heaviestFirst(self.arbol)

    def heaviestFirst(self, nodo):
        if len(nodo.hijos) != 0:
            descendientes = []
            validos = 0
            for i in nodo.hijos:
                if i.estado == Nodo.Estado.INDEFINIDO:
                    descendientes.append(i.nNodos)
                elif i.estado == Nodo.Estado.VALIDO:
                    validos = validos+1
            if len(nodo.hijos) == validos:
                self.buggy = True
            elif len(descendientes)!=0:
                found = False
                j=0
                while(found==False):
                    if nodo.hijos[j].nNodos == max(descendientes) and nodo.hijos[j].estado == Nodo.Estado.INDEFINIDO:
                        print(descendientes)
                        found = True
                        self.ask(nodo.hijos[j])
                        if(nodo.hijos[j].estado == Nodo.Estado.VALIDO):
                            self.heaviestFirst(nodo)
                    j=j+1;
        else:
            self.buggy = True;

    def ask(self, nodo):
            print("Soy la funcion:", nodo.getNombre())
            #print("Mi Id es:", self.id)
            print("Num hijos de '"+nodo.getNombre()+"' es:", nodo.nNodos)
            print("El estado de '"+nodo.getNombre()+"' es:", nodo.estado)
            print("Valor retornado por '"+nodo.getNombre()+"' es:", nodo.getValor())
            nb=""
            while(nb!="y" and nb!="n"):
                nb = input("It's correct?(y/n)")
                print(nb)

            if(nb == "y"):
                nodo.estado = Nodo.Estado.VALIDO
            else:
                nodo.estado = Nodo.Estado.ERROR
                ##Aqui debería ir un switch con el tipo de estrategia a seguir
                #Decidir si el id debe ir dentro del else o ejecutarse siempre

                error = Error(nodo.getNombre())
                #valor ahora es solo el return pero deberia contemplar excepciones y efectos laterales(parametros de entrada, etc)
                error.addValor(nodo.getValor())
                self.errores.append(error)
                if(self.estrategia == Estrategia.TOPDOWN):
                    self.topDown(nodo)
                if(self.estrategia == Estrategia.HEAVIESTFIRST):
                    self.heaviestFirst(nodo)
            if(self.buggy):
                print("Buggy en la función:", nodo.getNombre())
                print("Valor retornado es:", nodo.getValor())


##clase error deberia ser un diccionario para buscar la key y añadir el error o generar un error nuevo

class Error():

    def __init__(self, nombre):
        self.nombre = nombre
        self.valor = []

    def addValor(self, valor):
        self.valor.append(valor)
