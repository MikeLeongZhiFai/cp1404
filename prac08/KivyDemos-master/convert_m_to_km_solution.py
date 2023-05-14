"""
CP1404 Week 11 Workshop - GUI program to convert miles to kilometres
Lindsay Ward, IT@JCU
06/10/2015
"""

from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.60934


class ConvertMilesToKilometer(App):
    """Converting Miles to Kilometer App Using Kivy"""

    def build(self):
        """Constructing Kivy app"""
        self.title = "Convert Miles to Kilometer"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def handle_update(self, amount):
        """Updating the miles amount based on the button that pressed"""
        value = self.get_valid_value() + amount
        self.root.ids.input_miles_amount.text = str(value)
        self.calculate_value()

    def get_valid_value(self):
        """Verify input is a valid miles float"""
        try:
            value = float(self.root.ids.input_miles_amount.text)
            return value
        except ValueError:
            return 0

    def calculate_value(self):
        """Calculating value from miles to kilometer"""
        value = self.get_valid_value()
        result = value * MILES_TO_KM
        self.root.ids.output_kilometer.text = str(result)


ConvertMilesToKilometer().run()