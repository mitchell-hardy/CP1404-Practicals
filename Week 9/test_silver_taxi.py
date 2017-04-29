"""CP1404 Prac 08 Exercise - Car and Taxi Class Inheritance"""

__author__ = 'Mitch Hardy'

from Taxi import SilverServiceTaxi

def test_silver_taxi():
    flash_taxi = SilverServiceTaxi("Mercedes", 100, 2)
    SilverServiceTaxi.start_fare(flash_taxi)
    SilverServiceTaxi.drive(flash_taxi, 10)
    print(flash_taxi)


test_silver_taxi()

