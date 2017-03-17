__author__ = 'Mitch Hardy'

def main():
#Take 5 user inputs into a list and print formatting baes information.
    user_numbers = get_numbers()
    print_numbers(user_numbers)


def get_numbers():
    #Get number inputs from user
    numbers = []
    for number in range(0,5):
        input_number = int(input("Number: "))
        numbers.append(input_number)
    return numbers

def print_numbers(user_numbers):
    #Print required values to user
    print("The first number is {}.".format(user_numbers[0]))
    print("The last number is {}.".format(user_numbers[-1]))
    print("The smallest number is {}.".format(min(user_numbers)))
    print("The largest number is {}.".format(max(user_numbers)))
    print("The average of the numbers is {}.".format(float(sum(user_numbers))/(len(user_numbers))))



main()
