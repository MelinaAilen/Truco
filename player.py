import random
from pprint import pprint


class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.played_cards = []

    def pick_cards(self, deck):
        self.cards = []
        random.shuffle(deck)

        for _ in range(3):
            self.cards.append(deck.pop())

    def play_card(self):
        print("\n{} which card do you want to play? ".format(self.name))
        print("\nThese are your cards:")
        pprint(self.cards)
        index = input("\nEnter the card index {}: ".format(str(list(range(len(self.cards))))))

        played_card = self.cards.pop(int(index))
        self.played_cards.append(played_card)
        print("\n{} have just played {}".format(self.name, played_card))

    def __str__(self):
        return 'player name: {}, cards: {}'.format(self.name, self.cards)

    def __repr__(self):
        return self.__str__()
