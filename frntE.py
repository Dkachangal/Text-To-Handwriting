from kivy.app import App
from kivy.core import text
from kivy.uix.label import Label
from kivy.core.window import Window

from kivy.uix.button import Button

from kivy.uix.image import Image

from kivy.uix.boxlayout import BoxLayout

Window.clearcolor = (0, 10, 20, 30)

class txttoHand(App):
    # i = 0
    def btnClick(self, btn):
        # global i
        # print(f"{i} times pressed")
        # i+=1
        print("Hello World")
    def btnRel(self, btn):
        print("Realesed")

    def build(self):

        x = Label(text="Divyansh Kachangal", font_size="90", bold=True)
        y = Label(text = "Helloo", color=(40,0,0,1), font_size="90")

        btn = Button(text = "Click me", size_hint = (0.05, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.5}, font_size="30", color=(0, 3, 4, 2), on_press=self.btnClick, on_release=self.btnRel)

        img = Image(source = "Characters.jpg", size_hint=(0.9, 0.9), pos_hint={'center_x': 0.5, 'center_y': 0.5})

        layOut = BoxLayout(orientation="vertical")

        layOut.add_widget(img)
        layOut.add_widget(x)
        layOut.add_widget(btn)
        

        return layOut

        # return y
    
    

txttoHand().run()