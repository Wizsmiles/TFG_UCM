from kivy.app import App
from kivy.uix.treeview import TreeView
from kivy.uix.treeview import TreeViewLabel
from kivy.uix.floatlayout import FloatLayout


def populate_tree_view(tree_view, parent, node):
    if parent is None:
        tree_node = tree_view.add_node(TreeViewLabel(text=node.getNombre(),
                                                     is_open=True))
    else:
        tree_node = tree_view.add_node(TreeViewLabel(text=node.getNombre(),
                                                     is_open=True), parent)

    for child_node in node.hijos:
        populate_tree_view(tree_view, tree_node, child_node)


class TreeWidget(FloatLayout):
    def __init__(self, **kwargs):
        super(TreeWidget, self).__init__(**kwargs)

    def populate(self, arbol):
        tv = TreeView(root_options=dict(text='Tree One'),
                      hide_root=False,
                      indent_level=4)

        populate_tree_view(tv, None, arbol)

        self.add_widget(tv)


class InterfaceApp(App):
    title = "Buggy debugger"

    def __init__(self, **kwargs):
        super(InterfaceApp, self).__init__(**kwargs)
        self.treeWidget = TreeWidget()

    def build(self):
        return self.treeWidget

    def populate(self, arbol):
        self.treeWidget.populate(arbol)


def initGUI(arbol):
    ia = InterfaceApp()
    ia.populate(arbol)
    ia.run()
