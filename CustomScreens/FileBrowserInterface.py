from kivy.uix.screenmanager import Screen

"""
Parent class for file browser screen

"""

class FileBrowserInterface(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

    def select(self, *args):
        try:
            self.label.text = args[1][0]
        except:
            pass

    def ok_click(self):
        pass

    def back_click(self):
        pass