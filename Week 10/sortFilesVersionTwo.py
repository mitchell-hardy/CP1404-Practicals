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
    categories = create_categories(extensions)
    create_directories(categories)
    move_files(categories)


def create_categories(extensions):
    """Create categories for file associations from users inputs."""
    categories = {}
    for file_type in extensions:
        user_category = input("What category would you like to sort {} files into?"
                              .format(file_type))
        if user_category not in categories:
            categories[user_category] = [file_type]
        else:
            categories[user_category].append(file_type)
    print(categories)
    return categories


def move_files(categories):
    """Move files into associated directory."""
    for filename in os.listdir("."):
        if os.path.isdir(filename):
            pass
        else:
            split_filename_extension = filename.split(".")
            for category, extensions in categories.items():
                if split_filename_extension[1] in extensions:
                    shutil.move(filename, category)


def create_directories(categories):
    """Create directories for each category defined by the user. """
    for category in categories:
        try:
            os.mkdir(category)
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
