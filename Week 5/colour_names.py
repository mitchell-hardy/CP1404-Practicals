"""
CP1404 Practical Exercise
Colour names Dictionary
"""
__author__ = 'Mitch Hardy'


def colour_codes():

    """
    Get a colour from the user and prints its colour code.
    """

    COLOUR_CODES = {"aliceblue": "#f0f8ff", "black": "#000000", "burlywood": "#deb887",
                    "cadetblue": "#5f9ea0", "coral": "#ff7f50", "darkgreen": "#006400",
                    "darkorchid": "#9932cc", "darkviolet": "#9400d3", "firebrick": "#b22222",
                    "forestgreen": "#228b22"}

    user_colour = ""

    while user_colour != "q":
        print("This dictionary has codes for these colours: ")
        for key in COLOUR_CODES:
            print(key)
        user_colour = input("Please type the colour you would like to know the code for,"
                            "\nor q to quit>>>").lower()
        if user_colour in COLOUR_CODES:
            print("The code for {} is {}".format(user_colour, (COLOUR_CODES[user_colour])))
        elif user_colour == "q":
            pass
        else:
            print("Invalid selection, please choose from the list!")

    print("Thanks for learning!")

colour_codes()
