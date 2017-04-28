"""Cp1404 Prac 7 Exercise - car driving simulation (using Car class)."""

__author__ = 'Mitch Hardy'

from car import Car


def driving_sim():
    """Sim to create, drive and refuel a vehicle. Using Car Class for object control"""
    MENU_CHOICES = ["d", "r", "q"]
    print("Let's drive!")
    vehicle = Car(input("Enter your car name: "))
    print(vehicle, "Menu:\n d) drive\n r) refuel\n q) quit")
    menu_selection = input(str.lower("Enter your choice: "))
    while menu_selection != "q":
        if menu_selection == "d":
            Car.drive(vehicle)
        elif menu_selection == "r":
            Car.add_fuel(vehicle)
        else:
            print("Invalid choice: ")
        print(vehicle, "Menu:\n d) drive\n r) refuel\n q) quit")
        menu_selection = input(str.lower("Enter your choice: "))
    print("Goodbye {}'s driver".format(vehicle.name))

driving_sim()
