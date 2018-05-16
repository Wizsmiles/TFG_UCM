from kivy.uix.boxlayout import BoxLayout


class Menu(BoxLayout):

    def __init__(self, controller, **kwargs):
        super(Menu, self).__init__(**kwargs)
        self.control = controller
        self.ids.buttonGo.bind(on_press=self.buttonGoAction)

    def buttonGoAction(self, instance):
        self.control.startDebugging()
