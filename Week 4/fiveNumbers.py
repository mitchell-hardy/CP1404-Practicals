__author__ = 'Mitch Hardy'

def main():

    user_numbers = get_numbers()
    print_numbers(user_numbers)


def get_numbers():
    numbers = []
    for number in range(0,5):
        number_input = float(input("{}---Please enter number: ".format(number+1)))
        numbers.append(number_input)

    return numbers

def print_numbers(user_numbers):
    print("The first number is {}.".format(user_numbers[0]))
    print("The last number is {}.".format(user_numbers[-1]))
    print("The smallest number is {}.".format(min(user_numbers)))
    print("The largest number is {}.".format(max(user_numbers)))
    print(sum(user_numbers))
    print("The average of the numbers is {}.".format(float(sum(user_numbers))/(len(user_numbers))))



main()
