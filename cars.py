# -*- coding: utf-8 -*-

'''
This file presents two approaches to manipulate sets of data in native Python:
- an approach based on the use of data structures
- an object-oriented approach with a class and two 'instances' of that class
'''

cars = [
    {'x': 10, 'y': 10, 'name': 'Car0'},
    {'x': 20, 'y': 20, 'name': 'Car1'},
]


def move(car_number, dx, dy):
    cars[car_number]['x'] += dx
    cars[car_number]['y'] += dy
    
# the move function needs to receive the index of the car in addition to movement
move(0, 5, 0)
move(1, 100, 100)

print(cars)


# --- object oriented version

class Car:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

car0 = Car(10, 10, 'Car0')
car1 = Car(20, 20, 'Car1')

# note the move function is called on the 'car' object
car0.move(5, 0)
car1.move(100, 100)

print(car0.name, car0.x, car0.y)
print(car1.name, car1.x, car1.y)
