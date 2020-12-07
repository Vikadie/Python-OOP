from project.rooms.room import Room
# from project.people.child import Child
# from project.appliances.tv import TV
# from project.appliances.fridge import Fridge
# from project.appliances.laptop import Laptop
# from project.rooms.young_couple import YoungCouple
# from project.rooms.young_couple_with_children import YoungCoupleWithChildren


import unittest


class TestsRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room('room_name', 1000, 4)

    def test_class_attributes_existence_upon_initialization(self):
        self.assertEqual(self.room.family_name, 'room_name')
        self.assertEqual(self.room.budget, 1000)
        self.assertEqual(self.room.members_count, 4)
        self.assertEqual(self.room.children, [])

    def test_expenses_is_property(self):
        self.assertEqual(self.room.expenses, 0)

    def test_set_expenses_to_positive_value_OK(self):
        self.room.expenses = 10
        self.assertEqual(self.room.expenses, 10)

    def test_set_expenses_to_negative_value_NOK(self):
        with self.assertRaises(ValueError) as exc:
            self.room.expenses = -10
        self.assertEqual(str(exc.exception), "Expenses cannot be negative")

    def test_calculate_expenses_with_zero_arguments(self):
        lst = []
        self.room.calculate_expenses(*lst)
        self.assertEqual(self.room.expenses, 0)

    # def test_calculate_expenses_with_young_couple_not_children(self):
    #     yc = YoungCouple('yc', 100, 100)
    #     expected_expenses = 1.5 * 2 + 1 * 2 + 1.2 * 2
    #     self.assertEqual(yc.expenses, expected_expenses)
    #
    # def test_calculate_expenses_with_young_couple_with_2_children(self):
    #     child_one = Child(2, 1)
    #     child_two = Child(3, 1, 2, 1)
    #     young_couple_with_children = YoungCoupleWithChildren("Peterson", 600, 520, child_one, child_two)
    #     expected_expenses = TV().cost * 4 + Fridge().cost * 4 + Laptop().cost * 4 + child_one.cost + child_two.cost
    #     self.assertAlmostEqual(young_couple_with_children.expenses, expected_expenses)

if __name__ == '__main__':
    unittest.main()