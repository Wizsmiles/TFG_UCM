from kivy.app import App
from kivy.uix.treeview import TreeView
from kivy.uix.scrollview import ScrollView
from View.CustomTreeNode import CustomTreeNode
from View.Menu import Menu
from Model.Nodo import Nodo
from Model.Nodo import Estado
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from kivy.uix.popup import Popup
from View.DKPopup import DKPopup


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
        

class MainFrame(BoxLayout):
    def __init__(self, **kwargs):
        global menu
        menu = Menu(controller)

        super(MainFrame, self).__init__(**kwargs)
        self.orientation = 'vertical'
        tv.size_hint = 1, None
        tv.bind(minimum_height=tv.setter('height'))
        sv = ScrollView(pos=(0, 0))
        populate_tree_view(None, tree)
        sv.add_widget(tv)
        self.add_widget(sv)
        self.add_widget(menu)


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



def askDK():
    global popup
    content = DKPopup(controller)
    popup = Popup(title="Nodos DESCONOCIDOS",
							content=content,
							size_hint=(None, None),
							size=(520,200),
							auto_dismiss= False)
    content.ids.labelInfoDK.text = 'Todav\u00eda quedan nodos con estado DESCONOCIDO.\n'
    content.ids.labelInfoDK.text += 'Hay una alta probabilidad de que el nodo buggy se encuentre entre ellos.\n'
    content.ids.labelInfoDK.text += '¿Le gustaría volver a revisarlos?'

    popup.open()


def dismissDK():
    global popup
    popup.dismiss()


def showBuggyFunction(name, params, namedk, paramsdk):
    menu.ids.labelBuggyFunction.text += name + ' ' + params.replace('{','( ').replace('}',' )')
    if namedk != None:
        menu.ids.labelBuggyFunction.text += '\nPero hay una alta probabilidad de que tambien lo sea: '
        menu.ids.labelBuggyFunction.text += namedk + ' ' + paramsdk.replace('{','( ').replace('}',' )')


def initGUI(arbol, controlador):
    global tree, controller
    tree = arbol
    controller = controlador
    ia = InterfaceApp()
    ia.run()
