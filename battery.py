"""Modeling a car batter"""

class Battery:

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