import Model.Recorridos as Recorridos


class Controller:

    def __init__(self, tree, graphics):
        self.tree = tree
        self.graphics = graphics

    def run(self):
        if self.graphics:
            import View.Interface as Interface
            Interface.initGUI(self.tree, self)
        else:
            recorrido = Recorridos.Recorrido(self.tree, self.graphics, self)
            recorrido.inicializarDQ()

    def startDebugging(self):
        recorrido = Recorridos.Recorrido(self.tree, self.graphics, self)
        recorrido.inicializarDQ()
