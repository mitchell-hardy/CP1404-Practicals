__author__ = 'Mitch Hardy'


from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button






    self.eye_colours = {"Mitch": "Brown", "Bob": "Blue", "George": "Green"}


    def build(self):
        """Build main App"""
        self.title = "Dynamic Widgets Test"
        self.root = Builder.load_file('dynamic_widgets.kv')

        return self.root




