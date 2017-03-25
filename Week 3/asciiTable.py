__author__ = 'Mitch Hardy'


def main():

    NUMBER_MINIMUM = 33
    NUMBER_MAXIMUM = 127
    # get a number from the user (ASCII) and print the corresponding character.
    user_number = get_number(NUMBER_MINIMUM, NUMBER_MAXIMUM)
    # get a character from the user and print the corresponding ASCII key
    print("The character for {} is {}".format(user_number, chr(user_number)))
    user_character = str(input("Enter a character: "))
    print("The ASCII code for {} is {}".format(user_character,ord(user_character)))
    for i in range(NUMBER_MINIMUM, NUMBER_MAXIMUM):
        print("{:^10d}{:^10s}".format(i, chr(i)))


# Get a number from the user, error check and return to main.
def get_number(NUMBER_MINIMUM, NUMBER_MAXIMUM):

    number = int(input("Enter a number between {} and {}: ".format(NUMBER_MINIMUM, NUMBER_MAXIMUM)))
    while number < NUMBER_MINIMUM or number > NUMBER_MAXIMUM:
        try:
            print("Invalid number, please choose from between {} and {}:".format(NUMBER_MINIMUM, NUMBER_MAXIMUM))
            number = int(input("Enter a number between {} and {}: ".format(NUMBER_MINIMUM, NUMBER_MAXIMUM)))
        except:
            number = ValueError
            number = 0
            print("Please only enter numbers!")
    return number


main()


