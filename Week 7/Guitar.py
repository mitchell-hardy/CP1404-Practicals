"""CP1404 Prac 07 Exercise - Guitar Program using Class."""

__author__ = 'Mitch Hardy'


class Guitar:
    """Guitar class for exercise"""
    CURRENT_YEAR = 2017

    def __init__(self, name='', year=0, cost=0.0):
        """Initialise a Guitar Instance"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : ${}".format(self.name, self.year, self.cost)

    def print_age(self):
        return "The {} is {}-{} = {}".format(self.name, self.CURRENT_YEAR, self.year, self.get_age())

    def get_age(self):
        guitar_age = self.CURRENT_YEAR - self.year
        return guitar_age

    def is_vintage(self):
        if self.get_age() >= 50:
            return "(vintage)"
        else:
            return ""

