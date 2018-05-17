import Model.Recorridos as Recorridos
import View.Interface as Interface
from Model.Answer import Answer
from Model.Recorridos import Estrategia
from Model.Nodo import Estado


class Controller:

    def __init__(self, tree, graphics):
        self.tree = tree
        self.graphics = graphics

    def run(self):
        if self.graphics:
            Interface.initGUI(self.tree, self)
        else:
            recorrido = Recorridos.Recorrido(self.tree, self.graphics, self)
            recorrido.inicializarTD()

    def startDebugging(self):
        self.recorrido = Recorridos.Recorrido(self.tree, self.graphics, self)
        Interface.updateNodes()
        Interface.setSelected(self.recorrido.inicializarTD())

    def answerGUI(self, node, answer):
        estado = Estado.INDEFINIDO

        if answer == Answer.YES:
            estado = Estado.VALIDO
        elif answer == Answer.NO:
            estado = Estado.ERROR
        elif answer == Answer.TRUST:
            estado = Estado.CONFIAR
        elif answer == Answer.UNACCEPTABLE:
            estado = Estado.INACEPTABLE
        elif answer == Answer.DONTKNOW:
            estado = Estado.DESCONOCIDO

        node.estado = estado
        self.tree.recorrerNodos(node)
        Interface.updateNodes()
        Interface.setUnselected(node)

        if node.estado == Estado.VALIDO or node.estado == Estado.CONFIAR or node.estado == Estado.INACEPTABLE:
            nextNode = self.tree
        else:
            nextNode = node

        if(self.recorrido.estrategia == Estrategia.TOPDOWN):
            Interface.setSelected(self.recorrido.topDown(nextNode))
        elif(self.recorrido.estrategia == Estrategia.HEAVIESTFIRST):
            Interface.setSelected(self.recorrido.heaviestFirst(nextNode))
        elif(self.recorrido.estrategia == Estrategia.DIVIDEANDQUERY):
            Interface.setSelected(self.recorrido.divideAndQuery(nextNode))
