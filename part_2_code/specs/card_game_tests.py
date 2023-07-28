import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card_game = CardGame()
        self.card1 = Card("Hearts", 1)
        self.card2 = Card("Spades", 5)
        self.cards = [self.card1, self.card2]

    def test_can_check_for_ace(self):
        result1 = self.card_game.check_for_ace(self.card1)
        result2 = self.card_game.check_for_ace(self.card2)
        self.assertEqual(True, result1)
        self.assertEqual(False, result2)

    def test_can_find_highest_card(self):
        result = self.card_game.highest_card(self.card1, self.card2)
        self.assertEqual(self.card2, result)

    def test_can_find_total_value_of_cards(self):
        result = self.card_game.cards_total(self.cards)
        self.assertEqual("You have a total of 6", result)
