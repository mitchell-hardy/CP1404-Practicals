__author__ = 'Mitch Hardy'

"""
CP1404/CP5632 - Practical
Random word generator - based on format of words
(Another way to get just consonants would be to use string.ascii_lowercase (all letters) and remove the vowels)
"""

def main():


    import random

    VOWELS = "aeiou"
    CONSONANTS = "bcdfghjklmnpqrstvwxyz"
    valid_format = False
    while not valid_format:
        word_format = str(input( "Please enter the word format you would like\nUse 'c' for consonants and 'v' for vowels - example - 'ccvcvvc'\n>>>"))
        valid_format = is_valid_format(word_format)
    word = ""
    for kind in word_format:
        if kind == "c":
            word += random.choice(CONSONANTS)
        else:
            word += random.choice(VOWELS)
    print(word)



def is_valid_format(word_format):

    for character in word_format:
        print(character)
        if character == "c" or character == "v":
            return True


main()

