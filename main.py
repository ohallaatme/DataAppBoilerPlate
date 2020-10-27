""" Boilerplate code for Kivy Data Applications """

# imports and settings

## kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.checkbox import CheckBox
from kivy.uix.dropdown import DropDown
from kivy.factory import Factory
from kivy import utils
## custom screen
from CustomScreens.FileBrowserInterface import FileBrowserInterface

""" Define Screens"""

# Menu
class MenuScreen(Screen):
    def hit_sub_menu_one(self):
        sm.current = "ExcelFileBrowser"

    def hit_sub_menu_two(self):
        pass

    def hit_sub_menu_three(self):
        pass

    def hit_sub_menu_four(self):
        pass

class SubMenuScreen(Screen):
    pass

# File Browser
class ExcelFileBrowser(FileBrowserInterface):
    def __init__(self, **kw):
        super().__init__(**kw)

    def select(self, *args):
        try:
            self.label.text = args[1][0]
        except:
            pass

    # TODO - look up interfaces in python to require 
    # the methods defined in parent FileBrowser
    def ok_click(self):
        pass

    def back_click(self):
        pass

# set up ScreenManager
class WindowManager(ScreenManager):
    pass

# create instance of WindowManager class to manage screens
sm = WindowManager()

# load UI
kv = Builder.load_file("Data.kv")

# list of screens 
screens = [MenuScreen(name="MenuScreen"), ExcelFileBrowser(name="ExcelFileBrowser")]

# add screens to screen manager
for screen in screens:
    sm.add_widget(screen)

# set menu screen as current screen on launch
sm.current = "MenuScreen"

# build the data app
class DataApp(App):
    def build(self):
        return sm

if __name__ == '__main__':
    DataApp().run()