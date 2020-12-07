import unittest

from project.player.advanced import Advanced
from project.player.player_repository import PlayerRepository


class TestPlayerRepository(unittest.TestCase):
    def setUp(self):
        self.pr = PlayerRepository()

    def test_correct_init_with_emplty_list_of_players_and_count_equal_zero(self):
        self.assertEqual(0, self.pr.count)
        self.assertEqual([], self.pr.players)

    def test_adding_player_to_players_list(self):
        player = Advanced('player')
        self.pr.add(player)
        self.assertEqual(1, self.pr.count)
        self.assertEqual([player], self.pr.players)
        # check adding same player returns ValueError
        with self.assertRaises(ValueError) as exc:
            self.pr.add(player)
        self.assertEqual("Player player already exists!", str(exc.exception))

    def test_remove_player_as_string(self):
        player = Advanced('player')
        self.pr.add(player)
        self.assertEqual(1, self.pr.count)
        self.assertEqual([player], self.pr.players)
        # trial to remove with player with empty string leading to errors
        with self.assertRaises(ValueError) as exc:
            self.pr.remove('')
        self.assertEqual("Player cannot be an empty string!", str(exc.exception))
        # correct removal of player with name 'player'
        self.pr.remove('player')
        self.assertEqual(0, self.pr.count)
        self.assertEqual([], self.pr.players)

    def test_find_player_by_name_returns_the_object_of_player(self):
        player = Advanced('player')
        player1 = Advanced('player1')
        self.pr.add(player)
        self.pr.add(player1)
        self.assertEqual(2, self.pr.count)
        self.assertEqual([player, player1], self.pr.players)
        self.assertEqual(player1, self.pr.find('player1'))
        self.assertEqual(player, self.pr.find('player'))


if __name__ == "__main__":
    unittest.main()