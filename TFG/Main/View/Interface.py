from kivy.app import App
from kivy.uix.treeview import TreeView
from kivy.uix.scrollview import ScrollView
from View.CustomTreeNode import CustomTreeNode
from Model.Nodo import Nodo


tree = Nodo()
tv = TreeView(
    root_options=dict(text='Tree One'),
    hide_root=True,
    indent_level=20
)


def populate_tree_view(parent, node):
    if parent is None:
        tree_node = tv.add_node(CustomTreeNode(
            is_open=True
        ))
    else:
        tree_node = tv.add_node(CustomTreeNode(
            is_open=True
        ), parent)

    for child_node in node.hijos:
        populate_tree_view(tree_node, child_node)


def buildStringNameLabel(node):
    nameLabel = node.getNombre()
    nameLabel += ' ( )\n'

    nameLabel += '  Parámetros entrada:\n'
    for key, value in node.getParamsEntrada().items():
        nameLabel += '      - ' + str(key) + ': ' + str(value) + '\n'

    if len(node.getParamsEntrada()) >= 1:
        nameLabel = nameLabel[:-1]

    nameLabel += '\n  Parámetros salida:\n'

    for key, value in node.getParamsMods().items():
        nameLabel += '      - ' + str(key) + ': ' + str(value) + '\n'

    return nameLabel


class InterfaceApp(App):
    title = "Buggy debugger"

    def __init__(self, **kwargs):
        super(InterfaceApp, self).__init__(**kwargs)

    def build(self):
        tv.size_hint = 1, None
        tv.bind(minimum_height=tv.setter('height'))
        root = ScrollView(pos=(0, 0))
        populate_tree_view(None, tree)
        root.add_widget(tv)
        return root


def initGUI(arbol):
    global tree
    tree = arbol
    ia = InterfaceApp()
    ia.run()
