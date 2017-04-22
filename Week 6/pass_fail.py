"""
Kivy app which displays a pass/fail result depending on input value.
"""

__author__ = 'Mitch Hardy'

from kivy.app import App
from kivy.lang import Builder


class passFailExercise(App):
    """Build the kivy app"""
    def build(self):
        self.title = "Pass/Fail Exercise"
        self.root = Builder.load_file('pass_fail.kv')
        return self.root

    def check_score(self):
        """Check that score is an integer and return, return 0 if not."""
        try:
            score = int(self.root.ids.score_input.text)
            return score
        except ValueError:
            return 0

    def handle_calculation(self):
        """Calculate the users grade base on the score input."""
        user_score = self.check_score()
        if user_score < 50:
            self.root.ids.result_output.text = str("Fail")
        elif user_score >= 50 and user_score < 65:
            self.root.ids.result_output.text = str("Pass")
        elif user_score >= 65 and user_score < 75:
            self.root.ids.result_output.text = str("Credit")
        elif user_score >= 75 and user_score < 85:
            self.root.ids.result_output.text = str("Distinction")
        elif user_score >= 85:
            self.root.ids.result_output.text = str("High Distinction")

passFailExercise().run()