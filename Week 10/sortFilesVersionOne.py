"""
CP1404/CP5632 Practical
File renaming and os examples
"""
import os, shutil

__author__ = 'Mitchell Hardy'


def sort_files():
    """Sort through files in directory, create additional
    directories for each type and move file into directory"""
    os.chdir('FilesToSort')
    extensions = get_extensions()
    create_directories(extensions)
    move_files()


def move_files():
    """Move files into associated directory."""
    for filename in os.listdir("."):
        if os.path.isdir(filename):
            pass
        else:
            split_filename_extension = filename.split(".")
            if os.path.isdir(split_filename_extension[1]):
                shutil.move(filename, split_filename_extension[1])


def create_directories(extensions):
    """Create directories for each type of file. """
    for extension in extensions:
        try:
            os.mkdir(extension)
        except FileExistsError:
            pass


def get_extensions():
    """Return a list of file extensions for files in directory"""
    extensions = []
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            pass
        else:
            split_filename = filename.split('.')
            if split_filename[1] not in extensions:
                extensions.append(split_filename[1])

    return extensions

sort_files()
