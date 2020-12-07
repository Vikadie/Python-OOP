import unittest

from project.card.trap_card import TrapCard


class TestTrapCard(unittest.TestCase):

    def setUp(self):
        self.tc = TrapCard('name')

    def test_correct_initialization(self):
        self.assertEqual('name', self.tc.name)
        self.assertEqual(120, self.tc.damage_points)
        self.assertEqual(5, self.tc.health_points)

    def test_name_cannot_be_empty(self):
        with self.assertRaises(ValueError) as exc:
            tc1 = TrapCard('')
        self.assertEqual("Card's name cannot be an empty string.", str(exc.exception))

    def test_damage_points_cannot_be_below_zero(self):
        with self.assertRaises(ValueError) as exc:
            self.tc.damage_points = -1
        self.assertEqual("Card's damage points cannot be less than zero.", str(exc.exception))

    def test_health_points_cannot_be_below_zero(self):
        with self.assertRaises(ValueError) as exc:
            self.tc.health_points = -1
        self.assertEqual("Card's HP cannot be less than zero.", str(exc.exception))


if __name__ == '__main__':
    unittest.main()