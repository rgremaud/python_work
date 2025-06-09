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

my_truck = Car("Toyota", "Tacoma", 2017)
my_truck.get_descriptive_name()
my_truck.odometer_reading = 17
my_truck.read_odomoter()
my_truck.update_mileage(150)
my_truck.read_odomoter()
my_truck.increment_miles(-2)
my_truck.increment_miles(300)
my_truck.read_odomoter()