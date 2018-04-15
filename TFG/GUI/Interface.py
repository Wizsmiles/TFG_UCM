'''
Created on 5 abr. 2018

@author: Handsome Jack
'''
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.config  import Config

class Contenedor(BoxLayout):
    None
    
class InterfaceApp(App):
    title = "Hola mundo"
    def build(self):
        return Contenedor()
    
if __name__ == '__main__':
    InterfaceApp().run()
    