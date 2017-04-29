"""CP1404 Prac 07 Exercise - Classes. Person Class"""

__author__ = 'Mitch Hardy'

class Person:
    """Person Class."""

    def __init__(self, first_name="", last_name="", age=""):
        """Initialise a Person instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        """Return basic string about person. """
        return "Person: {} {}, is {} years old".format(self.first_name, self.last_name, self.age)
