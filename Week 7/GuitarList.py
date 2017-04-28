"""CP1404 Prac 07 Exercise - Guitar Program using Class."""

__author__ = 'Mitch Hardy'

from Guitar import Guitar


class GuitarList:
    """Class to keep track of Guitar Objects"""

    def __init__(self):
        """Initialise a Guitar List Instance"""
        self.guitars = []

    def add_guitar(self, guitar):
        """Add guitar from program to the list"""
        self.guitars.append(guitar)

    def __str__(self):
        """Return string of data for guitar in guitar list"""
        return str([str(guitar) for guitar in self.guitars])

    def print_guitar_info(self):
        """Print statement for each guitar in the list. Guitar.is_vintage return string if guitar is a vintage"""
        print("These are my guitars:")
        for i, guitar in enumerate(self.guitars):
            print("Guitar {}: {:>20} ({}), worth ${:10,.2f} {}"
                  .format(i + 1, guitar.name, guitar.year, guitar.cost, Guitar.is_vintage(guitar)))
