"""
CP1404 Practical 06 Exercise
Kivy GUI program to convert miles to kms
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Mitchell Hardy'


class miles_to_km_app(App):
    def build(self):
        Window.size = (300, 200)
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('miles_to_kms.kv')
        return self.root

    def get_miles(self):
        try:
            miles = float(self.root.ids.input_number.text)
            return miles
        except ValueError:
            return 0

    def handle_increment(self, value_modify):
        new_value = self.get_miles() + value_modify
        self.root.ids.input_number.text = str(new_value)
        self.handle_conversion()


    def handle_conversion(self):
        miles_to_convert = self.get_miles()
        result = miles_to_convert * 1.609344
        self.root.ids.output_label.text = str(result)


miles_to_km_app().run()
