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
from pathlib import Path
import os

# backend functions
from B import jpg2png, createDict, iterateUserStr

Window.size = (270, 600)

# global storages
page = {}
characters = {}


# ---------- SCREEN MANAGER ----------
class Manager(ScreenManager):
    pass


# ---------- SCREEN 1: Character input ----------
class InputImage(Screen):
    def getChar(self):
        charByUser = self.ids.userChar.text.strip().lower()
        if not charByUser:
            print("⚠️ Please enter a character before selecting an image.")
            return None
        return charByUser


# ---------- SCREEN 2: File Picker ----------
class FilePickerScreen(Screen):
    pass


# ---------- SCREEN 3: Input text ----------
class InputText(Screen):
    def getText(self):
        dta = self.ids.data.text.strip()
        return dta


# ---------- SCREEN 4: Output screen ----------
class DisplayOutput(Screen):
    pass


# ---------- MAIN APP ----------
class TextToHandd(MDApp):
    def build(self):
        # Load KV file
        Builder.load_file("texttohandd.kv")
        # Return actual root widget (important!)
        return Manager()

    # ----------- File Chooser -----------
    def open_file_picker(self, source):
        filechooser.open_file(
            title="Select an image",
            filters=[("Image files", "*.png;*.jpg;*.jpeg")],
            on_selection=lambda selection: self.file_selected(selection, source),
        )

    def file_selected(self, selection, source):
        if not selection:
            print("⚠️ File selection cancelled.")
            return

        selected_file = os.path.normpath(selection[0])

        if source == "page":
            page['page'] = selected_file
            print(f"✅ Page selected: {selected_file}")

        elif source == "character":
            input_screen = self.root.get_screen("inputimg")
            ch = input_screen.getChar()
            if ch:
                characters[ch] = selected_file
                print(f"✅ Character '{ch}' mapped to {selected_file}")
            else:
                print("⚠️ No character entered!")

    # ----------- Character Mapping -----------
    def call_getChar(self):
        input_screen = self.root.get_screen("inputimg")
        char = input_screen.getChar()
        print("Character from InputImage:", char)
        return char

    # ----------- Generate Output -----------
    def call_inpTxt(self):
        """When user presses the pencil button."""
        if 'page' not in page:
            print("⚠️ Please select a page first!")
            return
        if not characters:
            print("⚠️ Please select character images first!")
            return

        input_screen = self.root.get_screen("inputtext")
        user_data = input_screen.getText()

        if not user_data:
            print("⚠️ Please enter text before proceeding!")
            return

        print(f"📝 User text: {user_data}")

        # Step 1: Convert JPG → transparent PNG
        jpg2png(characters)

        # Step 2: Load PNGs
        chars = createDict("DKChars")

        # Step 3: Generate final handwritten page
        iterateUserStr(user_data, chars, page['page'])

        print("✅ Process completed successfully.")
        return user_data


# ---------- RUN ----------
if __name__ == "__main__":
    TextToHandd().run()
