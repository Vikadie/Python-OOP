from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        fuel_needed = distance * self.fuel_consumption
        if fuel_needed <= self.fuel_quantity:
            self.fuel_quantity -= fuel_needed

    @abstractmethod
    def refuel(self, fuel):
        pass
