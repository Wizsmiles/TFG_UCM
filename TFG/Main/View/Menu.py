from kivy.uix.boxlayout import BoxLayout
from Model.Recorridos import Estrategia


class Menu(BoxLayout):

    def __init__(self, controller, **kwargs):
        super(Menu, self).__init__(**kwargs)
        self.control = controller

        self.ids.spinnerEstrategia.text = 'Estrategias'
        self.ids.spinnerEstrategia.values = ('Top-Down','Heaviest First','Half Down')

        self.ids.buttonGo.bind(on_press=self.buttonGoAction)
        self.ids.buttonExit.bind(on_release=self.buttonExitAction)
        self.ids.spinnerEstrategia.bind(text=self.spinnerEstrategiaAction)

    def buttonGoAction(self, instance):
        self.control.startDebugging()
        self.ids.buttonGo.disabled = True

    def buttonExitAction(self, instance):
        exit()

    def spinnerEstrategiaAction(self, instance, text):
        if text == 'Top-Down':
            self.control.swapStrategy(Estrategia.TOPDOWN)
        elif text == 'Heaviest First':
            self.control.swapStrategy(Estrategia.HEAVIESTFIRST)
        elif text == 'Half Down':
            self.control.swapStrategy(Estrategia.HALFDOWN)
