#!/usr/bin/pyhton3

class Vehicle:
    def move(self):
        pass

# Define different vehicle classes with their own move() implementation
class Car(Vehicle):
    def move(self):
        print("🚗 Driving on the road!")

class Plane(Vehicle):
    def move(self):
        print("✈️ Flying in the sky!")

class Boat(Vehicle):
    def move(self):
        print("🛥️ Sailing on the water!")

class Bicycle(Vehicle):
    def move(self):
        print("🚴 Pedaling along the path!")


vehicles = [Car(), Plane(), Boat(), Bicycle()]

for vehicle in vehicles:
    vehicle.move()

