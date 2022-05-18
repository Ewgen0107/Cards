from Card import *
from random import shuffle


class Pack:
    def __init__(self):
        self.cards = []
        for i in range(6, 15):
            self.cards.append(Card('♥', i))
            self.cards.append(Card('♦', i))
            self.cards.append(Card('♣', i))
            self.cards.append(Card('♠', i))
        shuffle(self.cards)
        Card.main_type = self.cards[-1].type

    def __repr__(self):
        return f"{self.cards}"
