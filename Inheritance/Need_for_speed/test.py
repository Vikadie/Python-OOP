from project.sport_car import SportCar
from project.race_motorcycle import RaceMotorcycle
from project.car import Car


sp = SportCar(22.2, 150)
print(sp.fuel)
sp.drive(10)
print(sp.DEFAULT_FUEL_CONSUMPTION)
print(sp.fuel)
print(sp.horse_power)
print("========")
rm = RaceMotorcycle(30, 260)
print(rm.fuel)
rm.drive(10)
print(rm.DEFAULT_FUEL_CONSUMPTION)
print(rm.fuel)
print(rm.horse_power)
print("========")
c = Car(10, 100)
print(c.fuel)
c.drive(10)
print(c.DEFAULT_FUEL_CONSUMPTION)
print(c.fuel)
print(c.horse_power)
print("========")
print(sp.fuel)