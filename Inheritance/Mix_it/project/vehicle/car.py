from .vehicle import Vehicle


class Car(Vehicle):

    def __init__(self, available_seats, fuel_tank, fuel_consumption, fuel):
        super().__init__(available_seats)
        self.fuel_tank = fuel_tank
        self.fuel_consumption = fuel_consumption
        self.__fuel = fuel if fuel <= self.fuel_tank else self.fuel_tank

    @property
    def fuel(self):
        return self.__fuel

    @fuel.setter
    def fuel(self, fuel):
        self.__fuel = fuel if fuel <= self.fuel_tank else self.fuel_tank

    def drive(self, distance):
        consumed_fuel = distance * self.fuel_consumption
        if consumed_fuel < self.__fuel:
            self.__fuel -= consumed_fuel
            return " We've enjoyed the travel!"

    def refuel(self, liters):
        if self.__fuel + liters <= self.fuel_tank:
            self.__fuel += liters
            return self.__fuel
        else:
            self.__fuel = self.fuel_tank
            return "Capacity reached!"
