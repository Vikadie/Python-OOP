import unittest

from project.battle_field import BattleField
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner


class TestBattleField(unittest.TestCase):
    def setUp(self):
        self.attacker = Advanced('I am attacker')
        mc = MagicCard('carte non-magique')
        self.attacker.card_repository.add(mc)
        self.enemy = Beginner('I am enemy')
        mc1 = MagicCard('catre magique')
        self.enemy.card_repository.add(mc1)
        self.battlefield = BattleField()

    def test_fight_when_one_of_them_is_dead(self):
        self.attacker.health = 0
        with self.assertRaises(ValueError) as exc:
            self.battlefield.fight(self.attacker, self.enemy)
        self.assertEqual("Player is dead!", str(exc.exception))

    def test_normal_fight(self):
        self.battlefield.fight(self.attacker, self.enemy)
        # attacker is Advanced (health = 250) magic_card (damage_points=5, health_points=80)
        # enemy is Beginner (health = 50) magic_card (damage_points=5, health_points=80)
        # before the fight : attacker_health = 330, enemy_health = 50 + 40 + 80 = 170;
        # before the fight: attacker_damage = 5, enemy_damage = 35
        # after the fight: attacker_health = 295, enemy_health = 165
        self.assertEqual(330 - 35, self.attacker.health)
        self.assertEqual(170 - 5, self.enemy.health) # if same card added for both players, any change will reflect in
        # opponents card change too
        self.assertEqual(5, sum([card.damage_points for card in self.attacker.card_repository.cards]))
        self.assertEqual(35, sum([card.damage_points for card in self.enemy.card_repository.cards]))
        # before the fight: attacker_health = 295 + 80, enemy_health = 165 + 40 + 80
        # before the fight: attacker_damage = 5, enemy_damage = 35 + 30
        self.battlefield.fight(self.attacker, self.enemy)
        # before the fight: attacker_health = 295 + 80, enemy_health = 165 + 40 + 80
        # before the fight: attacker_damage = 5, enemy_damage = 35 + 30
        self.assertEqual(375 - 65, self.attacker.health)
        self.assertEqual(285 - 5, self.enemy.health)

    def test_normal_fight_when_one_of_them_die(self):
        tc = TrapCard('tc')
        tc.damage_points += 400
        self.enemy.card_repository.add(tc)
        with self.assertRaises(ValueError) as exc:
            self.battlefield.fight(self.attacker, self.enemy)
        self.assertEqual("Player's health bonus cannot be less than zero.", str(exc.exception))



if __name__ == "__main__":
    unittest.main()