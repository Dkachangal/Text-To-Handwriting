# from kivy.app import App
from kivymd.app import MDApp
from kivy.uix.label import Label
from kivymd.uix.label import MDLabel
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.button import MDFillRoundFlatButton
from kivy.lang import Builder

Window.size=(270, 600)



md_bg_color = (1, 0.9, 0.3, 1)

class Manager(ScreenManager):
    pass

class InputImage(Screen):
    pass

class InputText(Screen):
    pass

class DisplayOutput(Screen):
    pass

class TextToHandd(MDApp):
    def build(self):
        
        return Manager()

TextToHandd().run()