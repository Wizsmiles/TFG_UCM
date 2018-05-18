from kivy.app import App
from kivy.uix.treeview import TreeView
from kivy.uix.scrollview import ScrollView
from View.CustomTreeNode import CustomTreeNode
from View.Menu import Menu
from Model.Nodo import Nodo
from Model.Nodo import Estado
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
from kivy.uix.popup import Popup
from kivy.uix.label import Label


Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '900')


tree = Nodo()
tv = TreeView(
    root_options=dict(text='Tree One'),
    hide_root=True,
    indent_level=20
)


def populate_tree_view(parent, node):
    global controller

    if parent is None:
        auxNode = CustomTreeNode(controller, node, is_open=True)
        tree_node = tv.add_node(auxNode)

    else:
        auxNode = CustomTreeNode(controller, node, is_open=True)
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


def searchNode(node):
    for ctn in tv.iterate_all_nodes(tv.root):
        if isinstance(ctn, CustomTreeNode):
            if ctn.node == node:
                return ctn


def setSelected(node):
    auxNode = searchNode(node)
    if auxNode is not None:
        tv.select_node(auxNode)
        auxNode.ids.buttonYes.disabled = False
        auxNode.ids.buttonNo.disabled = False
        auxNode.ids.buttonTrust.disabled = False
        auxNode.ids.buttonDontKnow.disabled = False
        auxNode.ids.buttonUnacceptable.disabled = False


def setUnselected(node):
    auxNode = searchNode(node)
    if auxNode is not None:
        tv.select_node(auxNode)
        auxNode.ids.buttonYes.disabled = True
        auxNode.ids.buttonNo.disabled = True
        auxNode.ids.buttonTrust.disabled = True
        auxNode.ids.buttonDontKnow.disabled = True
        auxNode.ids.buttonUnacceptable.disabled = True


def updateNodes():
    for ctn in tv.iterate_all_nodes(tv.root):
        if isinstance(ctn, CustomTreeNode):
            ctn.updateNode()
            if ctn.is_open and (ctn.node.estado == Estado.VALIDO or ctn.node.estado == Estado.CONFIAR or ctn.node.estado == Estado.INACEPTABLE):
                tv.toggle_node(ctn)


class DKPopup(GridLayout):

	def __init__(self,**kwargs):
		self.register_event_type('on_answer')
		super(DKPopup,self).__init__(**kwargs)

	def on_answer(self, *args):
		pass


def askDK():
    content = DKPopup()
    popup = Popup(title="Answer Question",
							content=content,
							size_hint=(None, None),
							size=(480,400),
							auto_dismiss= False)
    popup.open()


def initGUI(arbol, controlador):
    global tree, controller
    tree = arbol
    controller = controlador
    ia = InterfaceApp()
    ia.run()
