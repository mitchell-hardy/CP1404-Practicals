"""CP1404 Exercise. Using Date class to handle date object."""

__author__ = 'Mitch Hardy'

from Date import Date

def date_test_program():
    """Simple program to use a calss to handle a date object.
    Note - minimal functionality as python already has a datetime module.
    """
    day = int(input("Enter day: "))
    month = int(input("Enter month: "))
    year = int(input("Enter year: "))
    date = Date(day, month, year)
    print(date)
    add_days = int(input("How many days to add:"))
    Date.add_days(date, add_days)
    print(date)

date_test_program()