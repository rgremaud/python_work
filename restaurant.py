"""Class to create a restaurant"""

class Restaurant:
    def __init__(self, name, type):
        """ Initialize values for restaurant """
        self.name = name
        self.type = type
        self.customers_served = 0
    
    def describe(self):
        """ Print a restaurant description """
        print(f"Welcome to {self.name}.")
        print(f"Please enjoy our {self.type} food.")

    def open_restaurant(self):
        """ Open up! """ 
        print(f"{self.name} is open for business!")

    def set_number_served(self, customers):
        """ Set number of customers served """
        if customers >= 0:
            self.customers_served = customers
        else: 
            print("no negative values!")
    
    def increment_number_served(self, customers):
        """ Increment number of customers served """
        if customers >= 0:
            self.customers_served += customers
        else: 
            print("no negative values!")
    
    def customers(self):
        """ Print number of customers served """
        print(f"This restaurant has served {self.customers_served} total customers")
    
