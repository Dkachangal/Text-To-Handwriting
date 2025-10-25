from kivy.app import App
from kivy.core import text
from kivy.uix.label import Label
from kivy.core.window import Window

from kivy.uix.button import Button

from kivy.uix.image import Image

from kivy.uix.boxlayout import BoxLayout

from kivy.uix.gridlayout import GridLayout

from kivy.uix.textinput import TextInput

from kivy.uix.screenmanager import Screen, ScreenManager

Window.clearcolor = (1, 90, 3, 6)



class Manager(ScreenManager):
    pass

class HomeScreen(Screen):
    pass

class FirstScreen(Screen):
    pass

class txttoHand(App):
    
    # def btnClick(self, btn):
    #     # global i
    #     # print(f"{i} times pressed")
    #     # i+=1
    #     print("Hello World")
    # def btnRel(self, btn):
    #     print("Realesed")

    # def printFromBtn(self, btnSubmit):
    #     print(f"The txt1Bx has {self.txtBx1.text}")
    #     print(f"The txtbx2 has {self.txtBx2.text}")

    def build(self):
        
        """
        x = Label(text="Divyansh Kachangal", font_size="90", bold=True)
        y = Label(text = "Helloo", color=(40,0,0,1), font_size="90")

        btn = Button(text = "Click me", size_hint = (0.05, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.5}, font_size="30", color=(0, 3, 4, 2), on_press=self.btnClick, on_release=self.btnRel)

        img = Image(source = "Characters.jpg", size_hint=(0.9, 0.9), pos_hint={'center_x': 0.5, 'center_y': 0.5})

        # Box Layout

        layOut = BoxLayout(orientation="vertical", padding=100, spacing = 100)

        # layOut.add_widget(img)
        # layOut.add_widget(x)
        # layOut.add_widget(btn)

        # Grid Layout
        grdLayout = GridLayout(rows =2, cols=2, padding=150, spacing=30)

        # grdLayout.add_widget(img)
        # grdLayout.add_widget(btn)
        # grdLayout.add_widget(y)


        # Text Box
        self.btnSubmit = Button(text = "CLICK TO SUBMIT", font_size=30, on_release=self.printFromBtn)
        self.txtBx1 = TextInput(text = 'Enter some text')
        self.txtBx2 = TextInput(text="Enter some more text")

        # grdLayout.add_widget(self.txtBx1)
        # grdLayout.add_widget(self.txtBx2)
        # grdLayout.add_widget(self.btnSubmit)

        bx1 = BoxLayout(orientation="horizontal")
        bx2 = BoxLayout(orientation="horizontal")
        # bx2.add_widget(grdLayout)

        # GridLayout
        # |
        # V
        # BoxLayout

        # FLOAT LAYOUT -> USES pos_hint
        # grdLayout.add_widget(bx1)

        return grdLayout
"""

txttoHand().run()