from project import *

import unittest


class VehicleTest(unittest.TestCase):
    # check the class is abstract (no instantiation possible)
    def test_abstract_class(self):
        with self.assertRaises(TypeError):
            Vehicle(1, 1)


if __name__ == '__main__':
    unittest.main()
