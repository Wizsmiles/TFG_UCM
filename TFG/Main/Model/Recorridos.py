import Model.Nodo as Nodo
from enum import Enum
import sys
import View.View as View

class Estrategia(Enum):
    TOPDOWN = 1
    HEAVIESTFIRST = 2
    DIVIDEANDQUERY = 3

class Recorrido():
    def __init__(self, tree, graphics, controller):
        self.arbol = tree
        self.estrategia = Estrategia.TOPDOWN
        self.arbol.estado = Nodo.Estado.ERROR
        self.desconocidos = []
        self.ended = False
        self.buggy = False
        self.buggyDN = False
        self.nodoBuggy = Nodo.Nodo()
        self.graphics = graphics
        self.controller = controller

        #####################TOPDOWN###################

    def inicializarTD(self):
        self.estrategia = Estrategia.TOPDOWN
        return self.topDown(self.arbol)
        self.ended = True
        print(self.graphics)

    def topDown(self, nodo):
        if len(nodo.hijos) != 0 and nodo.estado != Nodo.Estado.VALIDO and nodo.estado != Nodo.Estado.CONFIAR and nodo.estado != Nodo.Estado.INACEPTABLE:
            validos = 0


            ##Primer blucle recorre todos los nodos hijos para establecer un valor distinto de INDEFINIDO
            for i in nodo.hijos:
                if i.estado == Nodo.Estado.VALIDO or i.estado == Nodo.Estado.CONFIAR or i.estado == Nodo.Estado.INACEPTABLE:
                    validos = validos+1
                elif i.estado == Nodo.Estado.ERROR:
                    self.topDown(i)
                    break
                ##elif i.estado == Nodo.Estado.DESCONOCIDO:
                elif i.estado == Nodo.Estado.INDEFINIDO:
                    self.ask(i)
                    if i.estado == Nodo.Estado.DESCONOCIDO:
                        self.desconocidos.append(i)
                    elif(i.estado == Nodo.Estado.ERROR):
                        break
                    elif i.estado == Nodo.Estado.VALIDO or i.estado == Nodo.Estado.CONFIAR or i.estado == Nodo.Estado.INACEPTABLE:
                        validos = validos+1

           #if len(nodo.hijos) == validos:
            if len(nodo.hijos) == validos and nodo.estado != Nodo.Estado.DESCONOCIDO:
                self.nodoBuggy = nodo
                self.buggy = True
                self.buggyMsj()


            elif len(nodo.hijos) == validos and nodo.estado == Nodo.Estado.DESCONOCIDO:
                # if nodo.padre.nNodos == 0:
                if self.arbol.nNodos == 1:
                    self.nodoBuggy = nodo
                    self.buggy = True
                    self.buggyMsj()


            else:
                ##Una vez finalizado el primer bucle, si el n�mero de validos es inferior al numero de hijos significa que 1 o m�s son DESCONOCIDO y se proceder� a recorrerlos con la estrategia establecida
                for i in nodo.hijos:
                    if i.estado == Nodo.Estado.DESCONOCIDO:
                        self.topDown(i)

                self.buggy = True

        else:
            self.buggy = True



        ################################HEAVIESTFIRST####################################

    def inicializarHF(self):
        self.estrategia = Estrategia.HEAVIESTFIRST
        return self.heaviestFirst(self.arbol)
        self.ended = True

    def heaviestFirst(self, nodo):
        if len(nodo.hijos) != 0:
            descendientes = []
            validos = 0

            for i in nodo.hijos:

                if i.estado == Nodo.Estado.INDEFINIDO:
                    descendientes.append(i.nNodos)

            ##    elif i.estado == Nodo.Estado.DESCONOCIDO:
            ##        if self.ended:
            ##            descendientes.append(i.nNodos)

                elif i.estado == Nodo.Estado.VALIDO or i.estado == Nodo.Estado.CONFIAR or i.estado == Nodo.Estado.INACEPTABLE:
                    validos = validos+1

            if len(nodo.hijos) == validos and nodo.estado != Nodo.Estado.DESCONOCIDO:
                self.nodoBuggy = nodo
                self.buggy = True
                self.buggyMsj()


            elif len(nodo.hijos) == validos and nodo.estado == Nodo.Estado.DESCONOCIDO:
                if self.arbol.nNodos == 1:
                    self.nodoBuggy = nodo
                    self.buggy = True
                    self.buggyMsj()

            elif len(descendientes)!=0:
                found = False
                j=0
                while(found==False):
                    if nodo.hijos[j].nNodos == max(descendientes) and nodo.hijos[j].estado == Nodo.Estado.INDEFINIDO:
                        found = True
                        if(not self.graphics):
                            self.ask(nodo.hijos[j])
                        else:
                            return self.askGUI(nodo.hijos[j])
                        if nodo.hijos[j].estado == Nodo.Estado.DESCONOCIDO:
                            self.desconocidos.append(nodo.hijos[j])

                        if(nodo.hijos[j].estado == Nodo.Estado.VALIDO or nodo.hijos[j].estado == Nodo.Estado.CONFIAR or nodo.hijos[j].estado == Nodo.Estado.INACEPTABLE or nodo.hijos[j].estado == Nodo.Estado.DESCONOCIDO):
                            self.heaviestFirst(nodo)
                        else:
                            self.nodoBuggy = nodo
                            self.buggy = True
                            self.buggyMsj()
                    j=j+1;
            else:
                ##Una vez finalizado el primer bucle, si el número de validos es inferior al numero de hijos y no hay descendientes significa que 1 o más son DESCONOCIDO y se procederá a recorrerlos con la estrategia establecida
                descendientes = []
                for i in nodo.hijos:
                    if i.estado == Nodo.Estado.DESCONOCIDO:
                        descendientes.append(i.nNodos)
                found = False
                j=0
                while(found==False):
                    if nodo.hijos[j].nNodos == max(descendientes) and nodo.hijos[j].estado == Nodo.Estado.DESCONOCIDO:
                        found = True
                        self.heaviestFirst(nodo.hijos[j])
                        if self.arbol.nNodos == 1:
                            self.nodoBuggy = nodo.hijos[j]
                            self.buggy = True
                            self.buggyMsj()
                        else:
                            print(self.arbol.nNodos)
                            self.heaviestFirst(self.arbol)
                        # if(self.buggy == False):
                            # self.heaviestFirst(nodo)
                        # else:
                            # self.nodoBuggy = nodo
                            # self.buggy = True
                            # self.buggyMsj()
                    j=j+1;
        else:
            self.nodoBuggy = nodo
            self.buggy = True
            self.buggyMsj()





###################################DIVIDEANDQUERY############################
    def inicializarDQ(self):
        self.estrategia = Estrategia.DIVIDEANDQUERY
        return self.divideAndQuery(self.arbol)
        self.ended = True

    def divideAndQuery(self, nodo):
        if len(nodo.hijos) != 0:
            descendientes = []
            validos = 0

            for i in nodo.hijos:
                if i.estado == Nodo.Estado.INDEFINIDO:
                    descendientes.append(abs(nodo.nNodos/2 - i.nNodos))
                elif i.estado == Nodo.Estado.VALIDO or i.estado == Nodo.Estado.CONFIAR or i.estado == Nodo.Estado.INACEPTABLE:
                    validos = validos + 1



            if len(nodo.hijos) == validos and nodo.estado != Nodo.Estado.DESCONOCIDO:
                self.nodoBuggy = nodo
                self.buggy = True
                self.buggyMsj()


            elif len(nodo.hijos) == validos and nodo.estado == Nodo.Estado.DESCONOCIDO:
                if self.arbol.nNodos == 1:
                    self.nodoBuggy = nodo
                    self.buggy = True
                    self.buggyMsj()

            elif len(descendientes) != 0:
                found = False
                j = 0

                while (not found):
                    n = abs(nodo.nNodos/2 - nodo.hijos[j].nNodos)

                    if n == min(descendientes) and nodo.hijos[j].estado == Nodo.Estado.INDEFINIDO:
                        found = True
                        if(not self.graphics):
                            self.ask(nodo.hijos[j])
                        else:
                            return self.askGUI(nodo.hijos[j])
                        if nodo.hijos[j].estado == Nodo.Estado.DESCONOCIDO:
                            self.desconocidos.append(nodo.hijos[j])

                        if(nodo.hijos[j].estado == Nodo.Estado.VALIDO or nodo.hijos[j].estado == Nodo.Estado.CONFIAR or nodo.hijos[j].estado == Nodo.Estado.INACEPTABLE or nodo.hijos[j].estado == Nodo.Estado.DESCONOCIDO):
                            self.divideAndQuery(nodo)
                        else:
                            self.nodoBuggy = nodo
                            self.buggy = True
                            self.buggyMsj()

                    j = j + 1
            else:
                ##Una vez finalizado el primer bucle, si el número de validos es inferior al numero de hijos y no hay descendientes significa que 1 o más son DESCONOCIDO y se procederá a recorrerlos con la estrategia establecida
                descendientes = []
                for i in nodo.hijos:
                    if i.estado == Nodo.Estado.DESCONOCIDO:
                        descendientes.append(abs(nodo.nNodos/2 - i.nNodos))
                found = False
                j = 0

                while (not found):
                    n = abs(nodo.nNodos/2 - nodo.hijos[j].nNodos)
                    if n == min(descendientes) and nodo.hijos[j].estado == Nodo.Estado.DESCONOCIDO:
                        found = True
                        self.divideAndQuery(nodo.hijos[j])
                        if self.arbol.nNodos == 1:
                            self.nodoBuggy = nodo.hijos[j]
                            self.buggy = True
                            self.buggyMsj()
                        else:
                            print(self.arbol.nNodos)
                            self.divideAndQuery(self.arbol)

                        # if(self.buggy == False):
                            # self.divideAndQuery(nodo)
                        # else:
                        #     self.nodoBuggy = nodo
                        #     self.buggy = True
                        #     self.buggyMsj()
                    j = j + 1
        else:
            self.nodoBuggy = nodo
            self.buggy = True
            self.buggyMsj()


    def ask(self, nodo):

            nb=""
            while(nb!="y" and nb!="n" and nb!="t"  and nb!="i"  and nb!="d"):
                View.TreeView.show(self.arbol)
                print("Soy la funcion:", nodo.getNombre())
                print("Mi Id es:", nodo.id)
                print("Num hijos de '"+nodo.getNombre()+"' es:", nodo.nNodos)
                print("El estado de '"+nodo.getNombre()+"' es:", nodo.estado)
                print("Valor retornado por '"+nodo.getNombre()+"' es:", nodo.getValor())
                nb = input("It's correct?(y/n) (press t/i/d --- t for trust/i for unnacceptable/d for don't know): \n (You can swap your strategy pressing e)")
                print(nb)
                if(nb == "e"):
                    while(nb!="td" and nb!="hf" and nb!="dq"):
                        nb = input("Select your strategy td(TOPDOWN)/hf(HEAVIESTFIRST)/dq(DIVIDEANDQUERY)")
                        print(nb)
                    if(nb == "td"):
                        self.estrategia = Estrategia.TOPDOWN
                        self.topDown(nodo.padre)

                    elif(nb == "hf"):
                        self.estrategia = Estrategia.HEAVIESTFIRST
                        self.heaviestFirst(nodo.padre)

                    elif(nb == "dq"):
                        self.estrategia = Estrategia.DIVIDEANDQUERY
                        self.divideAndQuery(nodo.padre)

            if(nb == "y"):
                nodo.estado = Nodo.Estado.VALIDO
                self.arbol.recorrerNodos(nodo);
            elif(nb == "t"):
                nodo.estado = Nodo.Estado.CONFIAR
                self.arbol.recorrerNodos(nodo);
            elif(nb == "i"):
                nodo.estado = Nodo.Estado.INACEPTABLE
                self.arbol.recorrerNodos(nodo);
            elif(nb == "d"):
                nodo.estado = Nodo.Estado.DESCONOCIDO
                self.arbol.recorrerNodos(nodo);
            elif(nb == "n"):
                nodo.estado = Nodo.Estado.ERROR
                #Decidir si el id debe ir dentro del else o ejecutarse siempre
                self.arbol.recorrerNodos(nodo);

                if(self.estrategia == Estrategia.TOPDOWN):
                    self.topDown(nodo)
                if(self.estrategia == Estrategia.HEAVIESTFIRST):
                    self.heaviestFirst(nodo)
                if(self.estrategia == Estrategia.DIVIDEANDQUERY):
                    self.divideAndQuery(nodo)

            #if(self.buggy):
            #    self.nodoBuggy = nodo
            #    self.buggyMsj()

    def askGUI(self, nodo):
        return nodo

    def buggyMsj(self):
        if self.nodoBuggy.estado == Nodo.Estado.DESCONOCIDO:
            print("Hay una alta posibilidad de que el nodo buggy sea:", self.nodoBuggy.getNombre())
            print("Su valor retornado es:", self.nodoBuggy.getValor())
            View.TreeView.show(self.arbol)
            nb=""
            while(nb!="y" and nb!="n"):
                nb = input("¿Quieres revisar los nodos Desconocidos?(y/n)")
                print(nb)
                if(nb == "y"):
                    while(len(self.desconocidos) > 0):
                        self.revisarDK()
                elif(nb == "n"):
                    sys.exit()


        else:
            print("Buggy en la funcion:", self.nodoBuggy.getNombre())
            print("Valor retornado es:", self.nodoBuggy.getValor())
            View.TreeView.show(self.arbol)
            sys.exit()

    def revisarDK(self):
        self.buggy = False
        j = 0

        for i in self.desconocidos:
            if i.estado == Nodo.Estado.DESCONOCIDO:
                if i.padre.estado == Nodo.Estado.VALIDO or i.padre.estado == Nodo.Estado.CONFIAR or i.padre.estado == Nodo.Estado.INACEPTABLE:
                    #Hereda el estado del padre, para indicar que no tiene que avanzar más
                    i.estado = i.padre.estado
                    self.desconocidos.pop(j)
                else :
                    if(not self.graphics):
                        self.ask(i)
                    else:
                        return self.askGUI(i)
                    if i.estado == Nodo.Estado.VALIDO or i.estado == Nodo.Estado.CONFIAR or i.estado == Nodo.Estado.INACEPTABLE:
                        self.desconocidos.pop(j)
                        if(self.estrategia == Estrategia.TOPDOWN):
                            self.topDown(self.arbol)
                        if(self.estrategia == Estrategia.HEAVIESTFIRST):
                            self.heaviestFirst(self.arbol)
                        if(self.estrategia == Estrategia.DIVIDEANDQUERY):
                            self.divideAndQuery(self.arbol)
            j = j+1
