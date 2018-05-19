from kivy.uix.gridlayout import GridLayout


class DKPopup(GridLayout):

    def __init__(self, controller, **kwargs):
        super(DKPopup,self).__init__(**kwargs)
        self.controller = controller
        self.ids.buttonAccept.bind(on_release=self.buttonAcceptAction)
        self.ids.buttonCancel.bind(on_release=self.buttonCancelAction)

    def buttonAcceptAction(self, instance):
        self.controller.handleDK(True)

    def buttonCancelAction(self, instance):
        self.controller.handleDK(False)
