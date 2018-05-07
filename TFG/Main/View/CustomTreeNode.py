from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class CustomTreeNode(BoxLayout):
    pass


class CustomApp(App):

    def build(self):
        return CustomTreeNode()


if __name__ == '__main__':
    CustomApp().run()
