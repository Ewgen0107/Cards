from Pack import *


class Card:
    main_type = '♥'

    def __init__(self, type: str, rank=0):
        assert rank >= 0, f"Power {rank} less than zero"
        self.type = type
        self.rank = rank

    def __repr__(self):
        if self.rank <= 10:
            return f"[{self.type}|{self.rank}]"
        elif self.rank == 11:
            return f"[{self.type}|J]"
        elif self.rank == 12:
            return f"[{self.type}|Q]"
        elif self.rank == 13:
            return f"[{self.type}|K]"
        elif self.rank == 14:
            return f"[{self.type}|A]"

    def __lt__(self, other):
        if self.type == other.type:
            return self.rank < other.rank
        elif self.type == Card.main_type:
            return False
        elif other.type == Card.main_type:
            return True
        else:
            return self.type < other.type

    def __gt__(self, other):
        if self.type == other.type:
            return self.rank > other.rank
        else:
            return self.type == Card.main_type

    def __eq__(self, other):
        return self.rank == other.rank and self.type == other.type
