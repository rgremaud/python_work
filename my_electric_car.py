import car

my_leaf = car.ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()

my_mustang = car.Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())