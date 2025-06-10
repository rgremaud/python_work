"""A set of classes that can be used to represent electric cars."""

from car import Car
from battery import Battery

class ElectricCar(Car):
    """ Creating electric cars to save the planet """
    def __init__(self, make, model, year):
        """ Initialize attributes of a car """
        super().__init__(make, model, year)
        self.battery = Battery()
