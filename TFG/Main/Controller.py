import Model.Recorridos as Recorridos
import View.Interface as Interface
from Model.Answer import Answer
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
            recorrido.inicializarDQ()

    def startDebugging(self):
        recorrido = Recorridos.Recorrido(self.tree, self.graphics, self)
        Interface.updateNodes()
        Interface.setSelected(recorrido.inicializarDQ())

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
