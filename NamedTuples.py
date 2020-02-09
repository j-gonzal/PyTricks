# Using namedtuple is way shorter than
# defining a class manually
from collections import namedtuple
Car = namedtuple('Car', 'color mileage')

# Our new car class works as expected:
my_car = Car('red', 3812.4)
my_car.color
my_car.mileage

# We get a nice string repr for free:
my_car

# Like tuples, namedtuples are immutable:
my_car.color = 'blue'