"""CP1404 Prac 08 Do from scratch Exercise. Taxi Simulator using classes."""
__author__ = 'Mitch Hardy'

from TaxiSimulator import Taxi
from TaxiSimulator import SilverServiceTaxi

def taxi_simulator_program():
    """Main program for Taxi simulator. User chooses vehicle and drives desired distance."""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    taxi_choice = ""
    bill = 0.0
    print("Let's Drive!")
    menu_selection = input("q)uit, c)hoose taxi, d)rive\n>>>").lower()
    while menu_selection != "q":
        if menu_selection == "c":
            taxi_choice = choose_taxi(bill, taxis)
        if menu_selection == "d":
            bill = drive_taxi(bill, taxi_choice)
        menu_selection = input("q)uit, c)hoose taxi, d)rive\n>>>").lower()
    print("Total trip cost: {:.2f}".format(bill))
    print("Taxis are now: ")
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


def choose_taxi(bill, taxis):
    """Method for user to choose taxi to be driven in."""
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))
    taxi_choice = taxis[int(input("Choose Taxi: "))]
    print("Bill to date: ${:.2f}".format(bill))
    return taxi_choice


def drive_taxi(bill, taxi_choice):
    """Method for user to input and drive taxi a distance."""
    distance = int(input("Drive how far? "))
    taxi_choice.drive(distance)
    print("Your {} trip cost you ${:.2f}".format(taxi_choice.name, taxi_choice.get_fare()))
    bill += taxi_choice.get_fare()
    print("Bill to date: ${:.2f}".format(bill))
    return bill




taxi_simulator_program()
