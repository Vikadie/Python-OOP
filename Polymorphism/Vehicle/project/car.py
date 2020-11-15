from project import Vehicle


class Car(Vehicle):
    fuel_quantity: float
    fuel_consumption: float

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)
        self.fuel_consumption += 0.9

    def refuel(self, fuel):
        self.fuel_quantity += fuel
