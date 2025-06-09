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
        print(long_name)

    def read_odomoter(self):
        """ Function to track miles """
        print(f"This car has {self.odometer_reading} miles on it")
    
    def update_mileage(self, mileage):
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

class ElectricCar(Car):
    """ Creating electric cars to save the planet """
    def __init__(self, make, model, year):
        """ Initialize attributes of a car """
        super().__init__(make, model, year)
    
electric_car = ElectricCar("Nissan", "Leaf", 2018)
electric_car.get_descriptive_name()