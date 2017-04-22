__author__ = 'Mitch Hardy'

from car import Car

def main():
    bus = Car("bus", 180)
    bus.drive(30)
    # print("fuel =", bus.fuel)
    # print("odo =", bus.odometer)
    limo = Car("limo", 100)
    limo.add_fuel(20)
    # print("fuel =", limo.fuel)
    limo.drive(115)
    # print("odo =", limo.odometer)
    Car.__str__(bus)
    Car.__str__(limo)





main()