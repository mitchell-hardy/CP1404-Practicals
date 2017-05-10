"""CP1404 Prac 08 Exercise - Car and Taxi Class Inheritance"""

__author__ = 'Mitch Hardy'

from Taxi import UnreliableCar


def test_unreliable_car():
    car = UnreliableCar("Hilux", 100, 50)
    UnreliableCar.drive(car, 49)
    print(car)
    UnreliableCar.drive(car, 51)
    print(car)
test_unreliable_car()
