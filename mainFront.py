from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout


Window.clearcolor = (1, 0.9, 0.3, 0.6)

class Manager(ScreenManager):
    pass

class inputImage(Screen):
    pass

class inputText(Screen):
    pass

class displayOutput(Screen):
    pass

class TextToHandd(App):
    def build(self):
        
        return Manager()
TextToHandd().run()