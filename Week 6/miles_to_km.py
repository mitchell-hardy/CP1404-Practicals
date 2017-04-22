"""
CP1404 Practical 06 Exercise
Kivy GUI program to convert miles to kms
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Mitchell Hardy'

MILES_TO_KM = 1.60934

class miles_to_km_app(App):
    def build(self):
        """Build the kivy app from the kv file"""
        Window.size = (300, 200)
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('miles_to_kms.kv')
        return self.root

    def get_miles(self):
        """Get input from the user, convert to float. If input invalid, return 0"""
        try:
            miles = float(self.root.ids.input_number.text)
            return miles
        except ValueError:
            return 0

    def handle_increment(self, value_modify):
        """Increment the input number by 1 or -1 with restropective buttons up or down."""
        new_value = self.get_miles() + value_modify
        self.root.ids.input_number.text = str(new_value)
        self.handle_conversion()


    def handle_conversion(self):
        """Convert the input value to miles"""
        miles_to_convert = self.get_miles()
        result = miles_to_convert * MILES_TO_KM
        self.root.ids.output_label.text = str(result)


miles_to_km_app().run()
