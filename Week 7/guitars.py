"""
Guitar Test Program. Using Guitar class - CP1404 Prac 07 Exercise.
Use class to display information about guitars.
"""
__author__ = 'Mitch Hardy'

from Guitar import Guitar
from GuitarList import GuitarList


def guitars_classes_prac():
    """Get Guitar Name, Year and Cost from user and use classes to handle object.
    Add guitar to list. When no further guitars on empty input for name, print all guitars."""

    my_guitars = GuitarList()
    guitar_name = input("Name: ")
    while guitar_name != "":
        guitar_year = int(input("Year: "))
        guitar_cost = float(input("Cost: "))
        new_guitar = Guitar(guitar_name, guitar_year, guitar_cost)
        my_guitars.add_guitar(new_guitar)
        guitar_name = input("Name: ")
    GuitarList.print_guitar_info(my_guitars)


guitars_classes_prac()
