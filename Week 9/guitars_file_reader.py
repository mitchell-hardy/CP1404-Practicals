"""
CP1404/CP5632 Practical - guitars tuple file read example
"""


import csv
from collections import namedtuple
__author__ = "Mitchell Hardy"


def main():
    """Use csv and namedtuple to read data from a csv file and store in a list as named tuples."""
    guitars = []
    in_file = open('guitars.csv', 'r', newline='')
    Guitar = namedtuple('Guitar', 'name, year, cost')
    reader = csv.reader(in_file)
    for row in reader:
        guitars.append(Guitar._make(row))
    in_file.close()
    for guitar in guitars:
        print(guitar)



main()
