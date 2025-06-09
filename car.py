"""A class that can be used to represent gas and electric cars."""

class Car:
    """ Build a simple car """
    
    def __init__(self, make, model, year):
        """ Initialize values for car """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """ Return formatted string for car info """
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()

    def read_odomoter(self):
        """ Function to track miles """
        print(f"This car has {self.odometer_reading} miles on it")
    
    def update_odometer(self, mileage):
        """ Set odometer"""
        if self.odometer_reading > mileage:
            print("You cant roll back an odometer!")
        else:
            self.odometer_reading = mileage
    
    def increment_miles(self, mileage):
        """ Increment car mileague """
        if mileage < 0:
            print("You cannot remove miles from the car")
        else:
            self.odometer_reading += mileage

class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):
    """Models aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()