from kivy.uix.boxlayout import BoxLayout
from kivy.uix.treeview import TreeViewNode
from Model.Answer import Answer


class CustomTreeNode(BoxLayout, TreeViewNode):

    def __init__(self, controller, node, **kwargs):
        super(CustomTreeNode, self).__init__(**kwargs)

        self.controller = controller
        self.node = node
        self.nodeId = node.id
        self.ids.labelName.text = node.getNombre() + " " + str(node.getParamsEntrada())
        self.ids.labelReturn.text += str(node.getValor())
        self.ids.labelState.text = str(node.estado)

        self.ids.buttonYes.bind(on_press=self.buttonYesAction)
        self.ids.buttonNo.bind(on_press=self.buttonNoAction)
        self.ids.buttonTrust.bind(on_press=self.buttonTrustAction)
        self.ids.buttonUnacceptable.bind(on_press=self.buttonUnacceptableAction)
        self.ids.buttonDontKnow.bind(on_press=self.buttonDontKnowAction)

    def updateNode(self):
        self.ids.labelState.text = str(self.node.estado)

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
