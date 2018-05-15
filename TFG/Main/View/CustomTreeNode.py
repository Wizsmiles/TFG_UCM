from kivy.uix.boxlayout import BoxLayout
from kivy.uix.treeview import TreeViewNode


class CustomTreeNode(BoxLayout, TreeViewNode):

    def buildNode(self, id, name, params, state):
        self.nodeId = id
        self.ids.labelName.text = name
        self.ids.labelParams.text = params
        self.ids.labelState.text = state
