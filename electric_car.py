"""A set of classes that can be used to represent electric cars."""

from car import Car

class Battery:
    """Modeling a car batter"""

    def __init__(self, battery_size=40):
        """Initialize the batter attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Show batter size"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")
        

class ElectricCar(Car):
    """ Creating electric cars to save the planet """
    def __init__(self, make, model, year):
        """ Initialize attributes of a car """
        super().__init__(make, model, year)
        self.battery = Battery()
    
electric_car = ElectricCar("Nissan", "Leaf", 2018)
electric_car.get_descriptive_name()
electric_car.battery.describe_battery()
electric_car.battery.upgrade_battery()
electric_car.battery.describe_battery()