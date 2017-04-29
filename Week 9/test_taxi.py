"""CP1404 Prac 08 Exercise - Car and Taxi Class Inheritance"""

__author__ = 'Mitch Hardy'

from Taxi import Car
from Taxi import Taxi

def test_taxi_program():
    taxi = Taxi("Prius 1", 200)
    Taxi.start_fare(taxi)
    Taxi.drive(taxi, 40)
    print(taxi, Taxi.get_fare(taxi))
    Taxi.start_fare(taxi)
    Taxi.drive(taxi, 100)
    print(taxi, Taxi.get_fare(taxi))



test_taxi_program()