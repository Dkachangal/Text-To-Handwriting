from kivymd.app import MDApp
# from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFlatButton
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.uix.filechooser import FileChooserListView
from kivymd.uix.button import MDRectangleFlatButton
from kivy.uix.scrollview import ScrollView


Window.size = (360, 640)  # width x height in pixels

class TextToHandWriting(MDApp):
    def build(self):
        pass
        """
        # Root screen
        screen = MDScreen()
        # Soft beige background (hex converted to RGBA)
        screen.md_bg_color = get_color_from_hex("FDFCF0")  # soft beige/off-white

        # Title label
        # title = MDLabel(
        #     text="Text to Handwriting",
        #     halign="center",
        #     # font_name="FrankRuhl",
        #     bold=True,
        #     font_style="H3",
        #     pos_hint={"center_y": 0.85}
        # )
        # screen.add_widget(title)


        # add image
        addImages = MDRectangleFlatButton(
            text = "CLick to Add Images",

            halign="center",
            font_style="H5",
            pos_hint={"center_y": 0.6, 'center_x': 0.5},
            on_release = self.addImage,


        )
        screen.add_widget(addImages)
        
        # Text input
        self.text_input = MDTextField(
            hint_text="Type your text here",
            size_hint_x=0.8,
            pos_hint={"center_x": 0.5, "center_y": 0.3},
            multiline=True
        )

        screen.add_widget(self.text_input)


        # Proceed button
        proceed_btn = MDFillRoundFlatButton(
            text="Proceed",
            pos_hint={"center_x": 0.5, "center_y": 0.1},
            on_release=self.on_proceed
        )
        screen.add_widget(proceed_btn)

        # Placeholder for gallery button (optional)
        gallery_btn = MDFillRoundFlatButton(
            text="Load Character Images",
            pos_hint={"center_x": 0.5, "center_y": 0.05},
            on_release=self.on_gallery
        )
        screen.add_widget(gallery_btn)

        return screen

    def on_proceed(self, instance):
        text = self.text_input.text
        print("Text to convert:", text)
        # Here you will process the text to generate handwriting

    def on_gallery(self, instance):
        print("Gallery button pressed")
        # Here you can open a file chooser to select character images
        """
        # pass

class Home(Screen):
    pass


class Manager(ScreenManager):
    pass

class ImageInsert(Screen):
    pass

class TextInput(Screen):
    pass

class ShowOutput(Screen):
    pass


if __name__ == "__main__":
    TextToHandWriting().run()
