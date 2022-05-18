import Game
from Game import *
import Card


class Bot:
    def __init__(self):
        self.cards = []

    def __repr__(self):
        return f"{self.cards}"

    def choose_card_bot(self) -> int:
        number = -1
        if len(Game.game) == 0:
            min_rank = 15
            for i in range(len(self.cards)):
                if self.cards[i].type != Card.Card.main_type and self.cards[i].rank < min_rank:
                    min_rank = self.cards[i].rank
                    number = i + 1
            if min_rank == 15:
                self.cards.sort()
                number = 1
        else:
            min_rank = 10
            # if len(Game.get_pack()) > 17:
            #     min_rank = 10
            # elif len(Game.get_pack()) > 13:
            #     min_rank = 11
            # elif len(Game.get_pack()) > 9:
            #     min_rank = 12
            # elif len(Game.get_pack()) > 6:
            #     min_rank = 13
            # elif len(Game.get_pack()) > 3:
            #     min_rank = 14
            # else:
            #     min_rank = 15
            for i in range(len(self.cards)):
                if self.cards[i].rank in map(lambda x: x.rank, Game.game):
                    if self.cards[i].type != Card.Card.main_type and self.cards[i].rank < min_rank:
                        min_rank = self.cards[i].rank
                        number = i + 1
            if number == -1:
                number = 0
        return number

    def defend_bot(self) -> int:
        number = 0
        number2 = 0
        min_rank = 15
        min_main_rank_type = 12
        # if 13 < Game.get_len_pack() <= 17:
        #     min_main_rank_type = 11
        # elif 9 < Game.get_len_pack() <= 13:
        #     min_main_rank_type = 12
        # elif 6 < Game.get_len_pack() <= 9:
        #     min_main_rank_type = 13
        # elif 3 < Game.get_len_pack() <= 6:
        #     min_main_rank_type = 14
        # else:
        #     min_main_rank_type = 15
        for i in range(len(self.cards)):
            if self.cards[i] > Game.game[-1]:
                if self.cards[i].type != Card.Card.main_type and self.cards[i].rank < min_rank:
                    min_rank = self.cards[i].rank
                    number = i + 1
                elif self.cards[i].type == Card.Card.main_type and self.cards[i].rank < min_main_rank_type:
                    min_main_rank_type = self.cards[i].rank
                    number2 = i + 1
        if number == 0:
            number = number2
        if len(Game.game) == 1 and Game.game[-1].type == Card.Card.main_type:
            number = 0
        return number
