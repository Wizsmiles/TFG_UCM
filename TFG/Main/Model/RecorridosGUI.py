from Model.Nodo import Nodo
from Model.Nodo import Estado

class RecorridoGUI():

    def __init__(self):
        self.buggy = False
        self.buggyNode = Nodo()
        self.desconocidos = []

    def topDown(self, nodo):
        if len(nodo.hijos) != 0 and nodo.estado != Estado.VALIDO and nodo.estado != Estado.CONFIAR and nodo.estado != Estado.INACEPTABLE:
            for i in nodo.hijos:
                if i.estado == Estado.INDEFINIDO:
                    return i
                if i.estado == Estado.ERROR:
                    self.topDown(i)

        if nodo.estado == Estado.ERROR:
            self.buggy = True
            self.buggyNode = nodo

        elif nodo.estado == Estado.DESCONOCIDO:
            self.buggyNode = nodo
            return self.topDown(nodo.padre)
