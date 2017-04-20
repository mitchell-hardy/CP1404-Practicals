"""
Greeter program for CP1404 Practical. Modified from previous box_layout file for changes in GUI layout.
"""

__author__ = "Mitchell Hardy"


from kivy.app import App
from kivy.lang import Builder



class BoxLayoutDemo(App):
    def build(self):
        self.title = "Greeter Modified (From Previous Box Layout)"
        self.root = Builder.load_file('greeter_modified.kv')
        return self.root

    def handle_greet(self):
        self.root.ids.output_label.text = "Hello " + self.root.ids.input_name.text

    def clear_button_reset(self):
        self.root.ids.output_label.text = "Greet"



BoxLayoutDemo().run()
