from Model.Nodo import Nodo
from Model.Nodo import Estado

class RecorridoGUI():

    def __init__(self):
        self.dk = False
        self.buggy = False
        self.buggyNode = Nodo()
        self.desconocidos = []
        self.buggyDKNode = Nodo()

    def topDown(self, nodo):
        validos = 0
        if len(nodo.hijos) != 0 and (nodo.estado == Estado.ERROR or nodo.estado == Estado.DESCONOCIDO):
            for i in nodo.hijos:
                if i.estado == Estado.INDEFINIDO:
                    return i
                if i.estado == Estado.ERROR:
                    self.topDown(i)
                    break
                if i.estado == Estado.VALIDO:
                    validos = validos + 1

        if nodo.estado == Estado.ERROR:
            self.buggyNode = nodo
            if validos == len(nodo.hijos):
                self.buggy = True

        elif nodo.estado == Estado.DESCONOCIDO:
            if validos == len(nodo.hijos):
                self.dk = True
            return self.topDown(nodo.padre)

    def revisarDK(self):
        self.buggy = False
        j = 0

        for i in self.desconocidos:
            if i.estado == Estado.DESCONOCIDO:
                if i.padre.estado == Estado.VALIDO or i.padre.estado == Estado.CONFIAR or i.padre.estado == Estado.INACEPTABLE:
                    #Hereda el estado del padre, para indicar que no tiene que avanzar más
                    i.estado = i.padre.estado
                    self.desconocidos.pop(j)
                else :
                    return i
            j = j+1

        self.buggy = True


    def getDeepestError(self, node):
        if node.estado == Estado.ERROR:
            self.buggyNode = node
            for i in node.hijos:
                if i.estado == Estado.ERROR:
                    self.getDeepestError(i)

    def getDeepestDK(self, node):
        if node.estado == Estado.DESCONOCIDO or node.estado == Estado.ERROR:
            self.buggyDKNode = node
            for i in node.hijos:
                print(i.getNombre())
                if i.estado == Estado.DESCONOCIDO:
                    self.getDeepestDK(i)
