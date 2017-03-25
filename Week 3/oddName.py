__author__ = 'Mitch Hardy'

"""
Error check user "name" input for blank errors and print every second letter
"""


def main():
    name = get_name()
    print("Every second letter in your name is: ",name[1::2])#Print every second letter in the name only excluding the first letter

def get_name():
    #Get the users name input and error check to ensure it is not blank.
    valid_name = False
    while not valid_name:
        name = input("Please enter your name: ")
        if name == "":
            print("Name cannot be blank!")
        else:
            valid_name = True

    return name

main()


