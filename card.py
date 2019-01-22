from enum import Enum

import unittest


class Suit(Enum):
    ORO = 0
    COPA = 1
    ESPADA = 2
    BASTO = 3


class Card:
    def __init__(self, suit, pip):
        self.suit = suit
        self.pip = pip

    def rank(self):
        if self.suit == Suit.ESPADA and self.pip == 1:
            return 1
        elif self.suit == Suit.BASTO and self.pip == 1:
            return 2
        elif self.suit == Suit.ESPADA and self.pip == 7:
            return 3
        elif self.suit == Suit.ORO and self.pip == 7:
            return 4
        elif self.pip == 3:
            return 5
        elif self.pip == 2:
            return 6
        elif self.pip == 1 and (self.suit == Suit.COPA or self.suit == Suit.ORO):
            return 7
        elif self.pip == 12:
            return 8
        elif self.pip == 11:
            return 9
        elif self.pip == 10:
            return 10
        elif self.pip == 7 and (self.suit == Suit.BASTO or self.suit == Suit.COPA):
            return 11
        elif self.pip == 6:
            return 12
        elif self.pip == 5:
            return 13
        else:
            return 14

    def envido_points(self):
        if self.pip < 10:
            return self.pip
        else:
            return 0

    def __str__(self):
        return 'Card({},pip={},rank={},envido={})'.format(self.suit, self.pip, self.rank(), self.envido_points())

    def __repr__(self):
        return self.__str__()


def create_deck():
    deck = []
    for suit in Suit:
        for pip in range(1, 13):
            if pip not in [8, 9]:
                deck.append(Card(suit, pip))
    return deck


class TestCards(unittest.TestCase):
    def test_deck_count(self):
        deck = create_deck()
        self.assertEqual(40, len(deck))

    def test_deck_envido(self):
        deck = create_deck()

        expected_total_envido = 28 * 4
        calculated_total_envido = sum([c.envido_points() for c in deck])

        self.assertEqual(expected_total_envido, calculated_total_envido)

    def test_deck_rank(self):
        deck = create_deck()

        expected_total_rank = 354
        calculated_total_rank = sum([c.rank() for c in deck])

        self.assertEqual(expected_total_rank, calculated_total_rank)

    def test_deck_rank_individually(self):
        deck = create_deck()

        expected_total_rank_espada = 81
        expected_total_rank_basto = 90
        expected_total_rank_copa = 95
        expected_total_rank_oro = 88

        calculated_total_rank_espada = sum([c.rank() for c in deck if c.suit == Suit.ESPADA])
        calculated_total_rank_basto = sum([c.rank() for c in deck if c.suit == Suit.BASTO])
        calculated_total_rank_copa = sum([c.rank() for c in deck if c.suit == Suit.COPA])
        calculated_total_rank_oro = sum([c.rank() for c in deck if c.suit == Suit.ORO])

        self.assertEqual(expected_total_rank_espada, calculated_total_rank_espada)
        self.assertEqual(expected_total_rank_basto, calculated_total_rank_basto)
        self.assertEqual(expected_total_rank_copa, calculated_total_rank_copa)
        self.assertEqual(expected_total_rank_oro, calculated_total_rank_oro)


if __name__ == '__main__':
    unittest.main()
