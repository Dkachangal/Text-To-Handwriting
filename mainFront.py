from kivymd.app import MDApp
from kivy.uix.label import Label
from kivymd.uix.label import MDLabel
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.button import MDIconButton
from kivy.uix.button import Button
from kivy.lang import Builder
from plyer import filechooser
from PIL import Image
from kivymd.uix.textfield import MDTextField
from kivy.uix.textinput import TextInput
import os



Window.size=(270, 600)

page = {}
characters = {}
# user_data = []


# md_bg_color = (1, 0.9, 0.3, 1)

class Manager(ScreenManager):
    pass

class InputImage(Screen):
    def getChar(self):
        charByUser = self.ids.userChar.text
        # img = Image.open(tmep)
        
        characters[charByUser] = charByUser 
        return charByUser

class FilePickerScreen(Screen):
    pass

class InputText(Screen):
    def getText(self):
        dta = self.ids.data.text
        return dta
    
class DisplayOutput(Screen):
    pass

class TextToHandd(MDApp):
    def build(self):
        
        return Manager()
    
    
    def open_file_picker(self, source):
        filechooser.open_file(
            title="Select an image",
            filters=[("Image files", "*.png;*.jpg;*.jpeg")],
            on_selection=lambda selection: self.file_selected(selection, source),
            
        )

    def call_getChar(self):
    
        input_screen = self.root.get_screen("inputimg")
        char = input_screen.getChar()  
        print("Character from InputImage:", char)
        return char
    
    def call_inpTxt(self):
    
        input_screen = self.root.get_screen("inputtext")
        user_data = input_screen.getText()  
        print(user_data)
        return user_data    
    
    def file_selected(self, selection, source):
        if selection:
            selected_file = selection[0]

            if source == "page":
                path = os.path.normpath(selected_file)
                x = Image.open(path)
                page['page'] = x
                for i in page:
                    print(i)

            elif source == "character":
                print(type(selected_file))
                ch = self.call_getChar()
                path = os.path.normpath(selected_file)
                x = Image.open(path)
                characters[ch] = x

        else:
            print("cancelled")

TextToHandd().run()