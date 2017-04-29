"""CP1404 Prac 07 Exercise - Classes. PersonList Class"""

__author__ = 'Mitch Hardy'

class PersonList:
    """Class to handle Person Objects"""

    def __init__(self):
        """Initialise a Person List Object"""
        self.persons = []

    def __str__(self):
        """Print basic string for each person showing first, last names and age"""
        for i, person in enumerate(self.persons):
            print("Person {}: {} {}, is {} years old"
                  .format(i + 1, person.first_name, person.last_name, person.age))

    def add_person(self, new_person):
        """Add a peson object to persons list."""
        self.persons.append(new_person)
