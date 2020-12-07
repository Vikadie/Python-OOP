import unittest

from project.card.magic_card import MagicCard
from project.controller import Controller
from project.player.beginner import Beginner


class TestControllers(unittest.TestCase):
    def setUp(self):
        self.c = Controller()

    def test_proper_initialization(self):
        self.assertEqual("PlayerRepository", self.c.player_repository.__class__.__name__)
        self.assertEqual("CardRepository", self.c.card_repository.__class__.__name__)

    def test_add_player_method(self):
        self.assertEqual("Successfully added player of type Beginner with username: nameBeginner",
                         self.c.add_player("Beginner", 'nameBeginner'))

    def test_add_card_method(self):
        self.assertEqual("Successfully added card of type MagicCard with name: magicName",
                         self.c.add_card("Magic", 'magicName'))

    def test_add_player_card(self):
        self.c.add_player("Beginner", 'nameBeginner')
        self.c.add_card("Magic", 'magicName')
        self.assertEqual("Successfully added card: magicName to user: nameBeginner",
                         self.c.add_player_card('nameBeginner', 'magicName'))

    def test_fight_method(self):
        self.c.add_player("Beginner", 'nameBeginner')
        self.c.add_player("Advanced", 'nameAdvanced')
        self.assertEqual("Attack user health 90 - Enemy user health 250",
                         self.c.fight('nameBeginner', 'nameAdvanced'))

    def test_report_method(self):
        self.c.add_player("Beginner", 'nameBeginner')
        self.assertEqual("Username: nameBeginner - Health: 50 - Cards 0\n", self.c.report())




if __name__ == '__main__':
    unittest.main()