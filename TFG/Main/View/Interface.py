from kivy.app import App
from kivy.uix.treeview import TreeView
from kivy.uix.treeview import TreeViewLabel
from kivy.uix.scrollview import ScrollView


def populate_tree_view(tree_view, parent, node):
    if parent is None:
        tree_node = tree_view.add_node(TreeViewLabel(
            text=buildStringNameLabel(node),
            is_open=True
        ))
    else:
        tree_node = tree_view.add_node(TreeViewLabel(
            text=buildStringNameLabel(node),
            is_open=True
        ), parent)

    for child_node in node.hijos:
        populate_tree_view(tree_view, tree_node, child_node)


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
        self.tv = TreeView(root_options=dict(text='Tree One'),
                           hide_root=True,
                           indent_level=10)

    def build(self):
        self.tv.size_hint = 1, None
        self.tv.bind(minimum_height=self.tv.setter('height'))
        root = ScrollView(pos=(0, 0))
        root.add_widget(self.tv)
        return root

    def populate(self, arbol):
        populate_tree_view(self.tv, None, arbol)


def initGUI(arbol):
    ia = InterfaceApp()
    ia.populate(arbol)
    ia.run()
