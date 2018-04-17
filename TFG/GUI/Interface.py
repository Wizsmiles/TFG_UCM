'''
Created on 5 abr. 2018

@author: Handsome Jack
'''
import kivy

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty
from kivy.config import Config

Config.set('graphics', 'width', 1080)
Config.set('graphics', 'height', 720)

#Frame principal que contiene la vista azul y el scrollview de la derecha con el gridlayout
class MainFrame(BoxLayout):
    def __init__(self):
        super(MainFrame,self).__init__()
        aux = 5
        for i in range(3):
            node = NodeBox()
            node.setSpace(aux)
            self.ids.nodeContainer.add_widget(node)
            aux += 30
            
#Box que contiene lo verde. Se inserta en el gridLayout de MainFram
#En mi ejemplo le muevo el spacing para simular tabulacion de hijos
class NodeBox(BoxLayout):
    V_space = NumericProperty(0)
    
    def setSpace(self,space):
        self.V_space = space
    
class InterfaceApp(App):
    title = "Buggy depurer"
    def build(self):
        return MainFrame()
    
if __name__ == '__main__':
    InterfaceApp().run()
    