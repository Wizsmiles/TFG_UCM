from kivy.uix.boxlayout import BoxLayout


class Menu(BoxLayout):

    def __init__(self, controller, **kwargs):
        super(Menu, self).__init__(**kwargs)
        self.control = controller
        self.ids.buttonGo.bind(on_press=self.buttonGoAction)
        self.ids.buttonExit.bind(on_release=self.buttonExitAction)

    def buttonGoAction(self, instance):
        self.control.startDebugging()

    def buttonExitAction(self, instance):
        exit()
