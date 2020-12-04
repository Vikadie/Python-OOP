from project import Vehicle


class Truck(Vehicle):
    fuel_quantity: float
    fuel_consumption: float

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)
        self.fuel_consumption += 1.6

    def refuel(self, fuel):
        self.fuel_quantity += 0.95 * fuel
