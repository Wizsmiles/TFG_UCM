from kivy.app import App
from kivy.uix.treeview import TreeView
from kivy.uix.scrollview import ScrollView
from View.CustomTreeNode import CustomTreeNode
from View.Menu import Menu
from Model.Nodo import Nodo
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from Controller import Controller


Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '900')


tree = Nodo()
tv = TreeView(
    root_options=dict(text='Tree One'),
    hide_root=True,
    indent_level=20
)


def populate_tree_view(parent, node):
    if parent is None:
        auxNode = CustomTreeNode(is_open=True)
        auxNode.buildNode(node.id,
                          node.getNombre(),
                          str(node.getParamsEntrada()),
                          str(node.estado))

        tree_node = tv.add_node(auxNode)

    else:
        auxNode = CustomTreeNode(is_open=True)
        auxNode.buildNode(node.id,
                          node.getNombre(),
                          str(node.getParamsEntrada()),
                          str(node.estado))

        tree_node = tv.add_node(auxNode, parent)

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


class MainFrame(BoxLayout):
    def __init__(self, **kwargs):
        super(MainFrame, self).__init__(**kwargs)
        self.orientation = 'vertical'
        tv.size_hint = 1, None
        tv.bind(minimum_height=tv.setter('height'))
        sv = ScrollView(pos=(0, 0))
        populate_tree_view(None, tree)
        sv.add_widget(tv)
        self.add_widget(sv)
        self.add_widget(Menu(controller))


class InterfaceApp(App):
    title = "Buggy debugger"

    def __init__(self, **kwargs):
        super(InterfaceApp, self).__init__(**kwargs)

    def build(self):
        return MainFrame()


def initGUI(arbol, controlador):
    global tree, controller
    tree = arbol
    controller = controlador
    ia = InterfaceApp()
    ia.run()
    print("hola")
