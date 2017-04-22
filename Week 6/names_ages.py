"""CP1404 Practical exercise, dynamically generated kivy GUI
with buttons for persons loaded from a file. """


from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty

__author__ = 'Mitch Hardy'


class NamesAgesApp(App):
    """Main Program"""
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        # Create dictionary of names and ages from file
        self.names_ages_dict = self.create_dict()

    def create_dict(self):
        """"Create dictionary of names and ages from file"""
        names_ages_dict = {}
        with open('names_ages.txt', mode='r', newline='') as in_file:
            for line in in_file:
                k, v = line.strip("\r\n").split(",")
                names_ages_dict[k] = v
        in_file.close()
        return names_ages_dict

    def build(self):
        """
        Build the Kivy GUI,
        call create_widgets() to populate buttons in the GUI from the names in the file.
        """
        status_text = StringProperty()
        self.title = "Names & Ages"
        self.root = Builder.load_file('names_ages.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create a button for each Name"""
        for name in self.names_ages_dict:
            temp_button = Button(text=name)
            temp_button.bind(on_release=self.press_entry)
            self.root.ids.entriesBox.add_widget(temp_button)

    def press_entry(self, instance):
        """
        Handler for pressing entry buttons
         """
        name = instance.text
        self.status_text = "{}'s age is {}".format(name, self.names_ages_dict[name])

    def clear_all(self):
        """
        Clear all of the widgets in "entriesBox" layout widget
        """
        self.root.ids.entriesBox.clear_widgets()

NamesAgesApp().run()


