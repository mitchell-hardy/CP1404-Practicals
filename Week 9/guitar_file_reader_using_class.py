"""
CP1404/CP5632 Practical - guitars tuple file read example
"""

from Guitar import Guitar

__author__ = "Mitchell Hardy"


def main():
    my_guitars = []
    """Use csv and namedtuple to read data from a csv file and store in a list as named tuples."""
    in_file = open('guitars.csv', 'r', newline='')
    for line in in_file:
        guitar_data = line.strip().split(',')
        guitar = Guitar(guitar_data[0], guitar_data[1], guitar_data[2])
        my_guitars.append(guitar)
    in_file.close()
    for guitar in my_guitars:
        print(guitar)


main()
