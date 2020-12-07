from project.player.beginner import Beginner

import unittest


class TestPlayerBeginner(unittest.TestCase):

    def setUp(self):
        self.player = Beginner("BeginnerPlayer")

    def test_setUp_class_attributes_and_properties(self):
        self.assertEqual(self.player.username, 'BeginnerPlayer')
        self.assertEqual(self.player.health, 50)
        self.assertEqual("CardRepository", self.player.card_repository.__class__.__name__)

    def test_health_cannot_go_under_zero(self):
        with self.assertRaises(ValueError) as exc:
            self.player.health = -10
        self.assertEqual("Player's health bonus cannot be less than zero.", str(exc.exception))

    def test_username_cannot_be_empty(self):
        with self.assertRaises(ValueError) as exc:
            pl = Beginner('')
        self.assertEqual("Player's username cannot be an empty string.", str(exc.exception))

    def test_is_dead_return_True_is_health_below_zero(self):
        self.assertEqual(False, self.player.is_dead)
        self.player.health = 0
        self.assertEqual(True, self.player.is_dead)

    def test_take_damage_func_works(self):
        self.player.take_damage(10)
        self.assertEqual(40, self.player.health)
        with self.assertRaises(ValueError) as exc:
            self.player.take_damage(-200)
        self.assertEqual("Damage points cannot be less than zero.", str(exc.exception))



if __name__ == '__main__':
    unittest.main()