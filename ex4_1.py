# Number of cars
cars = 100
# Number of passangers in one car
space_in_car = 4.0
# Number of drivers
drivers = 30
# Number of passangers
passangers = 90
# Cars without drivers
cars_not_driven = cars - drivers
# Cars with drivers
cars_driven = drivers
# Number of passangers that can be transported
carpool_capacity = cars_driven * space_in_car
# Number of passangers in each car
average_passengers_per_car = passangers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers availalbe."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passangers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."