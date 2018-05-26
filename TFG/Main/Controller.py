import Model.Recorridos as Recorridos
import View.Interface as Interface
from Model.Answer import Answer
from Model.Recorridos import Estrategia
from Model.Nodo import Estado
from Model.RecorridosGUI import RecorridoGUI

class Controller:

    def __init__(self, tree, graphics):
        self.tree = tree
        self.tree.estado = Estado.ERROR
        self.graphics = graphics
        self.estrategia = Estrategia.TOPDOWN
        self.revisarDK = False

    def run(self):
        if self.graphics:
            Interface.initGUI(self.tree, self)
        else:
            print(self.graphics)
            recorrido = Recorridos.Recorrido(self.tree)
            recorrido.inicializarTD()

    def startDebugging(self):
        self.recorrido = RecorridoGUI()
        Interface.updateNodes()
        if(self.estrategia == Estrategia.TOPDOWN):
            Interface.setSelected(self.recorrido.topDown(self.tree))
        elif(self.estrategia == Estrategia.HEAVIESTFIRST):
            Interface.setSelected(self.recorrido.heaviestFirst(self.tree))
        elif(self.estrategia == Estrategia.DIVIDEHALF):
            Interface.setSelected(self.recorrido.divideHalf(self.tree))

    def answerGUI(self, node, answer):
        estado = Estado.INDEFINIDO
        nextNode = node

        if answer == Answer.YES:
            estado = Estado.VALIDO
            nextNode = node.padre
        elif answer == Answer.NO:
            estado = Estado.ERROR
        elif answer == Answer.TRUST:
            estado = Estado.CONFIAR
            nextNode = node.padre
        elif answer == Answer.UNACCEPTABLE:
            estado = Estado.INACEPTABLE
            nextNode = node.padre
        elif answer == Answer.DONTKNOW:
            estado = Estado.DESCONOCIDO
            self.recorrido.desconocidos.append(node)

        node.estado = estado
        self.tree.recorrerNodos(node)
        Interface.updateNodes()
        Interface.setUnselected(node)

        if self.revisarDK:
            self.handleDK(True)
        else:
            if(self.estrategia == Estrategia.TOPDOWN):
                nodeToSelect = self.recorrido.topDown(nextNode)
            elif(self.estrategia == Estrategia.HEAVIESTFIRST):
                nodeToSelect = self.recorrido.heaviestFirst(nextNode)
            elif(self.estrategia == Estrategia.DIVIDEHALF):
                nodeToSelect = self.recorrido.divideHalf(nextNode)

        if self.recorrido.buggy:
            self.recorrido.getDeepestError(self.tree)
            Interface.showBuggyFunction(self.recorrido.buggyNode.getNombre(), str(self.recorrido.buggyNode.getParamsEntrada()), None, None)
        elif self.recorrido.dk and not self.isLastBuggy() and not self.revisarDK:
            Interface.askDK()
        elif not self.revisarDK:
            Interface.setSelected(nodeToSelect)


    def isLastBuggy(self):
        buggy = True

        for i in self.recorrido.buggyNode.hijos:
            if i.estado == Estado.DESCONOCIDO:
                buggy = False

        return buggy

    def handleDK(self, boolean):
        Interface.dismissDK()
        if boolean:
            self.revisarDK = True
            Interface.setSelected(self.recorrido.revisarDK())
        else:
            self.recorrido.getDeepestError(self.tree)
            self.recorrido.getDeepestDK(self.recorrido.buggyNode)

            buggyNode = self.recorrido.buggyNode
            buggyDKNode = self.recorrido.buggyDKNode

            Interface.showBuggyFunction(buggyNode.getNombre(), str(buggyNode.getParamsEntrada()), buggyDKNode.getNombre(), str(buggyDKNode.getParamsEntrada()))

    def swapStrategy(self, strategy):
        self.estrategia = strategy
