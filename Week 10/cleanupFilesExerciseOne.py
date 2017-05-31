"""
CP1404/CP5632 Practical
File renaming and os examples
"""
import os


__author__ = 'Mitchell Hardy'

def cleanup_files():
    """Cleanup filenames in directory files"""
    os.chdir('Lyrics/Christmas')
    for filename in os.listdir('.'):
        split_filename = filename.split(".")  # Split filename to remove extension.
        first_edit_filename = insert_spaces_capitals(split_filename[0])
        second_edit_filename = first_edit_filename.split(" ")  # Split the filename by spaces
        third_edit_filename = filename_capitalize_underscore(second_edit_filename)
        # Add extension back onto string in lower case
        new_filename = third_edit_filename + "." + split_filename[1].lower()
        os.rename(filename, new_filename)


def insert_spaces_capitals(filename):
    """Insert spaces in the front of Capital letters in the filename and return new string."""
    changed_filename = ""
    for character in filename:
        if character.isupper():
            changed_filename += " " + character
        else:
            changed_filename += character
    return changed_filename


def filename_capitalize_underscore(filename):
    """Capitalize the split strings and add underscores on the end of each word."""
    changed_filename = ""
    for word in filename:
        if word == "":
            pass
        else:
            word = word.capitalize()
            if word == "(":
                changed_filename += word
            else:
                changed_filename += word + "_"
    changed_filename = changed_filename[:-1]  # Remove _ from end of changed filename.
    return changed_filename


cleanup_files()
