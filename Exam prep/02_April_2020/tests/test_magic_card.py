
import unittest

from project.card.magic_card import MagicCard


class TestMagicCard(unittest.TestCase):
    def setUp(self):
        self.mg = MagicCard('name')

    def test_correct_initialization(self):
        self.assertEqual(5, self.mg.damage_points)
        self.assertEqual(80, self.mg.health_points)
        self.assertEqual('name', self.mg.name)

    def test_name_cannot_be_empty(self):
        with self.assertRaises(ValueError) as exc:
            mg1 = MagicCard('')
        self.assertEqual("Card's name cannot be an empty string.", str(exc.exception))

    def test_damage_points_cannot_be_below_zero(self):
        with self.assertRaises(ValueError) as exc:
            self.mg.damage_points = -1
        self.assertEqual("Card's damage points cannot be less than zero.", str(exc.exception))

    def test_health_points_cannot_be_below_zero(self):
        with self.assertRaises(ValueError) as exc:
            self.mg.health_points = -1
        self.assertEqual("Card's HP cannot be less than zero.", str(exc.exception))


if __name__ == '__main__':
    unittest.main()