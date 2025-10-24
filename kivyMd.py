from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDFillRoundFlatButton


class txtHndw(MDApp):
    def submit(self, btn):
        print(f"The email is {text}")
    def build(self):
        btn= MDFillRoundFlatButton(text="Submit", on_press='submit')
        text = MDTextField(text = "Enter your email", pos_hint={'center_x': 0.5, 'center_y': 0.5}, )
        return text
        # return MDLabel(text="Hello World")

txtHndw().run()