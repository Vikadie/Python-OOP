# from project import *
from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @property
    @abstractmethod
    def _CONST_CONSUMPTION(self):
        pass

    def drive(self, distance):
        fuel_needed = distance * (self.fuel_consumption + self._CONST_CONSUMPTION)
        if fuel_needed <= self.fuel_quantity:
            self.fuel_quantity -= fuel_needed

    @abstractmethod
    def refuel(self, fuel):
        raise NotImplementedError


class Car(Vehicle):
    _CONST_CONSUMPTION = 0.9

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    _CONST_CONSUMPTION = 1.6

    def refuel(self, fuel):
        self.fuel_quantity += 0.95 * fuel


# car = Car(20, 5)
# car.drive(3)
# print(car.fuel_quantity)
# car.refuel(10)
# print(car.fuel_quantity)
#
# truck = Truck(100, 15)
# truck.drive(5)
# print(truck.fuel_quantity)
# truck.refuel(50)
# print(truck.fuel_quantity)