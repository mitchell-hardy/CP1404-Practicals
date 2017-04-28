__author__ = 'Mitch Hardy'

"""CP1404/CP5632 Practical - Car class example."""


class Car:
    """Car class demo."""

    def __init__(self, name='', fuel=100):
        """Initialise a Car instance.
        fuel: float, one unit of fuel drives one kilometre
        """
        self.name = name
        self.fuel = fuel
        self.odometer = 0

    def __str__(self):
        # defined string print to format required.
        return "{}, fuel={}, odometer={}".format(self.name, self.fuel, self.odometer)

    def add_name(self, vehicle_name):
        """Add name of vehicle."""
        self.name = vehicle_name

    def add_fuel(self):
        """Add amount to the car's fuel."""
        amount = 0
        valid_fuel = False
        while not valid_fuel:
            try:
                amount = float(input("How many units of fuel do you want to add to the car?"))
                if amount < 0:
                    print("Fuel amount must be >= 0")
                else:
                    valid_fuel = True
            except ValueError:
                print("Fuel amount must be >= 0")

        self.fuel += amount
        print("Added {} units of fuel".format(self.fuel))

    def drive(self):
        """Drive the car a given distance.
        Drive given distance if car has enough fuel
        or drive until fuel runs out print the distance actually driven.
        """
        distance = 0
        valid_distance = False
        while not valid_distance:
            try:
                distance = float(input("How many km do you wish to drive? "))
                if distance < 0:
                    print("Distance must be >= 0")
                else:
                    valid_distance = True
            except ValueError:
                print("Distance must be >= 0")

        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
            print("You ran out of fuel after {} kms".format(distance))
        else:
            self.fuel -= distance
        self.odometer += distance
        print("{} drove {}km.".format(self.name, distance))

