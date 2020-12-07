import unittest

from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard


class TestCardRepository(unittest.TestCase):
    def setUp(self):
        self.cr = CardRepository()

    def test_correct_initialization_zero_count_empty_cards_list(self):
        self.assertEqual([], self.cr.cards)
        self.assertEqual(0, self.cr.count)

    def test_add_method_with_card(self):
        card = MagicCard('card')
        self.cr.add(card)
        self.assertEqual([card], self.cr.cards)
        self.assertEqual(1, self.cr.count)

    def test_add_method_adding_same_card_more_than_once_resulting_in_value_error(self):
        card = MagicCard('card')
        self.cr.add(card)
        self.assertEqual([card], self.cr.cards)
        self.assertEqual(1, self.cr.count)
        with self.assertRaises(ValueError) as exc:
            self.cr.add(card)
        self.assertEqual(f"Card card already exists!", str(exc.exception))

    def test_remove_card(self):
        card = MagicCard('card')
        self.cr.add(card)
        self.assertEqual([card], self.cr.cards)
        self.assertEqual(1, self.cr.count)
        with self.assertRaises(ValueError) as exc:  # Value error if card.name = ''
            self.cr.remove('')
        self.assertEqual("Card cannot be an empty string!", str(exc.exception))
        # correctly removing the card
        self.cr.remove('card')
        self.assertEqual([], self.cr.cards)
        self.assertEqual(0, self.cr.count)

    def test_find_card(self):
        card = MagicCard('card')
        self.cr.add(card)
        self.assertEqual([card], self.cr.cards)
        self.assertEqual(1, self.cr.count)
        self.assertEqual(card, self.cr.find('card'))




if __name__ == "__main__":
    unittest.main()