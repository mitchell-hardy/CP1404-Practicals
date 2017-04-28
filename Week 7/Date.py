"""CP1404 Prac 07 Exercise - Date Class"""

__author__ = 'Mitch Hardy'

from datetime import date

class Date:
    """Instance class for exercise."""
    def __init__(self, day=00, month=00, year=0000):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return "{}/{}/{}".format(self.day, self.month, self.year)

    def add_days(self, days):
        self.day += days


