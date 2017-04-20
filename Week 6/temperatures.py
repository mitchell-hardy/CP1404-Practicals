"""
CP1404/CP5632 - Practical
Kivy App for for temperature conversion
"""

from kivy.app import App
from kivy.lang import Builder

__author__ = 'Mitchell Hardy'


class TempConverterApp(App):
    """Build the Kivy App"""
    def build(self):
        self.title = "Temperature Converter"
        self.root = Builder.load_file('temperatures.kv')
        return self.root

    def get_number(self):
        """Get input from the user and error check. If invalid input return 0."""
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0

    def handle_conversion(self, conversion_id):
        """Depending on user selection, undertake the conversion using the value associated to the button."""

        user_value = self.get_number()
        if user_value != 0:
            if conversion_id == "C":
                fahrenheit = user_value * 9.0 / 5 + 32
                self.root.ids.result_output.text = str("{} Celsius = {} Fahrenheit".format(user_value, fahrenheit))

                return fahrenheit
            elif conversion_id == "F":
                celsius = (5 / 9 * (user_value - 32))
                self.root.ids.result_output.text = str("{} Fahrenheit = {} Celsius".format(user_value, celsius))
        else:
            self.root.ids.result_output.text = str("Please only enter numbers, try again. ")

TempConverterApp().run()
