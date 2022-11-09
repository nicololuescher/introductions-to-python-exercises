# Design and implement a class Car with the following functionalities:
# A car has a certain gas consumption (measured on liters/100km),
# A car's tank has a certain gas level (measured in liters). Most cars have a tank size of 30 l.
# The gas consumption is specified in the constructor, whereas the tank is initially empty. Provide methods to:
# Fill up the tank (liters),
# Drive a certain distance (km),
# Return the current amount of gas (liters).


class Car:
    def __init__(self, consumption, tankSize=30):
        self.consumption = consumption
        self.tankSize = tankSize
        self.fuel = 0

    def fill(self):
        self.fuel = self.tankSize

    def drive(self, km):
        self.fuel -= km / 100 * self.consumption

    def checkFuelLevel(self):
        return self.fuel
