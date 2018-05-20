from kivy.uix.boxlayout import BoxLayout
from kivy.uix.treeview import TreeViewNode
from Model.Answer import Answer
from Model.Nodo import Estado
from kivy.properties import ListProperty


class CustomTreeNode(BoxLayout, TreeViewNode):
    trust = ListProperty([0/255,174/255,219/255,1])
    yes = ListProperty([142/255,193/255,39/255,1])
    no = ListProperty([212/255,18/255,67/255,1])
    unac = ListProperty([244/255,120/255,53/255,1])
    dontk = ListProperty([255/255,196/255,37/255,1])

    def __init__(self, controller, node, **kwargs):
        super(CustomTreeNode, self).__init__(**kwargs)

        self.controller = controller
        self.node = node
        self.nodeId = node.id
        self.ids.labelName.text = '\n' + node.getNombre() + self.paramsToString()
        self.ids.labelReturn.text += str(node.getValor())
        self.ids.labelState.text = node.estado.name

        self.ids.buttonYes.bind(on_press=self.buttonYesAction)
        self.ids.buttonNo.bind(on_press=self.buttonNoAction)
        self.ids.buttonTrust.bind(on_press=self.buttonTrustAction)
        self.ids.buttonUnacceptable.bind(on_press=self.buttonUnacceptableAction)
        self.ids.buttonDontKnow.bind(on_press=self.buttonDontKnowAction)

    def paramsToString(self):
        st = " (\n"
        cont = 0

        paramsEntrada = self.node.getParamsEntrada()
        paramsSalida = self.node.getParamsMods()

        for i in paramsEntrada.keys():
            st += "     " + i + ": " + str(paramsEntrada[i]) + " -> " + str(paramsSalida[i]) + "\n"
            cont += 1
        st += ")"

        if cont == 0:
            st = st.replace("\n", " ")

        return st

    def updateNode(self):
        self.ids.labelState.text = self.node.estado.name
        self.updateColor()

    def updateColor(self):
        if self.node.estado != Estado.INDEFINIDO:
            if self.node.estado == Estado.ERROR:
                color = self.no
            elif self.node.estado == Estado.VALIDO:
                color = self.yes
            elif self.node.estado == Estado.CONFIAR:
                color = self.trust
            elif self.node.estado == Estado.INACEPTABLE:
                color = self.unac
            elif self.node.estado == Estado.DESCONOCIDO:
                color = self.dontk

            self.ids.labelName.color = color
            self.ids.labelReturn.color = color
            self.ids.labelState.color = color

    def buttonYesAction(self, instance):
        self.controller.answerGUI(self.node, Answer.YES)

    def buttonNoAction(self, instance):
        self.controller.answerGUI(self.node, Answer.NO)

    def buttonTrustAction(self, instance):
        self.controller.answerGUI(self.node, Answer.TRUST)

    def buttonUnacceptableAction(self, instance):
        self.controller.answerGUI(self.node, Answer.UNACCEPTABLE)

    def buttonDontKnowAction(self, instance):
        self.controller.answerGUI(self.node, Answer.DONTKNOW)
