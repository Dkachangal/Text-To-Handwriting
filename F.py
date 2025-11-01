from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivy.lang import Builder
from plyer import filechooser
from PIL import Image
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

class FontSelector(Screen):
    def pre_font_Dk(self):
        charactersDK = {}
        jpgimgpath = Path('characters')
        global preFont
        preFont = True
        str = 'abcdefghijklmnopqrstuvwxyz'

        for i in str:
            new = jpgimgpath/f'{i}1.png'
            img = Image.open(new)
            charactersDK[i] = img
            print(charactersDK[i])
        spcPath = jpgimgpath/'space.png'
        space = Image.open(spcPath)

        pagePath = jpgimgpath/'Pagenew.jpg'
        popen = Image.open(pagePath)
        charactersDK["page"] = popen
        charactersDK[" "] = space

        return charactersDK


# ---------- SCREEN 2: File Picker ----------
# class FilePickerScreen(Screen):
#     pass



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
    preFont = False
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
        global preFont
        if not selection:
            print("⚠️ File selection cancelled.")
            return

# TO WORK ON :
# TO MAKE THE FN SUCH THAT ON CLICKING DK FONT, THE PAGE AUTOMATICALLY GETS SELECTED
        if preFont == True:
            dkPage = FontSelector()
            openPage = dkPage.pre_font_Dk()
            selected_file = openPage["page"]
            page['page'] = selected_file
            print(f"✅ Pre-inserted font page selected: {page['page']}")

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
        global preFont
        """When user presses the pencil button."""
        if preFont == False:
            if 'page' not in page:
                print("⚠️ Please select a page first!")
                return
            
        if preFont == False:
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

        if preFont == False:
            jpg2png(characters)
            # Step 2: Load PNGs
            chars = createDict("DKChars")
        dkFont = FontSelector()

        chars = dkFont.pre_font_Dk()
        # Step 3: Generate final handwritten page
        iterateUserStr(user_data, chars, page['page'])

        print("✅ Process completed successfully.")
        return user_data

# select pre inserted font







# ---------- RUN ----------
if __name__ == "__main__":
    TextToHandd().run()
