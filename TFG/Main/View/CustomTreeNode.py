# from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.treeview import TreeViewNode
# from kivy.uix.widget import Widget
# from kivy.uix.label import Label


class CustomTreeNode(BoxLayout, TreeViewNode):
    pass


# class InterfaceApp(App):
#     title = "Buggy debugger"
#
#     def build(self):
#         layout = BoxLayout()
#         layout.add_widget(CustomTreeNode())
#         return layout
#
#
# if __name__ == '__main__':
#     InterfaceApp().run()
