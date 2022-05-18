import Game
from Pack import *
from Game import *


class Player:
    def __init__(self):
        self.cards = []

    def __repr__(self):
        return f"{self.cards}"

    def choose_card(self) -> int:
        print('your choice, player')
        number = int(input())
        if len(Game.game) == 0:
            while number <= 0 or number > len(self.cards):
                number = int(input())
        else:
            while number < 0 or number > len(self.cards) or self.is_in_game(number) == False:
                number = int(input())
        return number

    def is_in_game(self, number) -> bool:
        return number == 0 or self.cards[number - 1].rank in map(lambda x: x.rank, Game.game)

    def defend(self) -> int:
        print('your defend, player')
        number = int(input())
        while number < 0 or number > len(self.cards) or self.correct_defend(number) == False:
            number = int(input())
        return number

    def correct_defend(self, number) -> bool:
        return number == 0 or self.cards[number - 1] > Game.game[-1]
