from kivy.uix.boxlayout import BoxLayout
from kivy.uix.treeview import TreeViewNode


class CustomTreeNode(BoxLayout, TreeViewNode):

    def buildNode(self, id, name, params, value, state):
        self.nodeId = id
        self.ids.labelName.text = name + " " + params
        self.ids.labelReturn.text += value
        self.ids.labelState.text = state
