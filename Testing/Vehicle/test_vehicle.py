from vehicle import Vehicle, Car, Truck

import unittest


class TestVehicle(unittest.TestCase):

    def setUp(self):
        self.c = Car(20, 5)
        self.t = Truck(20, 5)

    def vehicle_is_abstract_class(self):
        with self.assertRaises(TypeError) as exc:
            Vehicle(20, 5)

    def test_drive_car_enough_fuel(self):
        expected = self.c.fuel_quantity - 3 * (5 + 0.9)
        self.c.drive(3)
        self.assertEqual(self.c.fuel_quantity, expected)

    def test_drive_car_not_enough_fuel(self):
        expected = self.c.fuel_quantity
        self.c.drive(100)
        self.assertEqual(self.c.fuel_quantity, expected)

    def test_drive_car_0km_no_change(self):
        expected = 0
        old_fuel_q = self.c.fuel_quantity
        self.c.drive(0)
        self.assertEqual(self.c.fuel_quantity - old_fuel_q, expected)

    def test_drive_truck_enough_fuel(self):
        expected = self.t.fuel_quantity - 3 * (5 + 1.6)
        self.t.drive(3)
        self.assertEqual(self.t.fuel_quantity, expected)

    def test_drive_truck_not_enough_fuel(self):
        expected = self.t.fuel_quantity
        self.t.drive(100)
        self.assertEqual(self.t.fuel_quantity, expected)

    def test_different_consumption_rate(self):
        self.c.drive(3)
        self.t.drive(3)
        self.assertNotEqual(self.c.fuel_quantity, self.t.fuel_quantity)

    def test_refuel_car(self):
        added_fuel = 20
        expected = self.c.fuel_quantity + added_fuel
        self.c.refuel(added_fuel)
        self.assertEqual(self.c.fuel_quantity, expected)

    def test_refuel_truck(self):
        added_fuel = 20
        expected = self.t.fuel_quantity + added_fuel * 0.95
        self.t.refuel(added_fuel)
        self.assertEqual(self.t.fuel_quantity, expected)


if __name__ == '__main__':
    unittest.main()