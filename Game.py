from Card import *


class Game:
    game = []

    def __init__(self, player1, player2, pack):
        self.player = player1
        self.bot = player2
        self.pack = pack

    def get_cards(self):
        self.player.cards.extend(self.pack.cards[:6])
        self.pack.cards = self.pack.cards[6:]
        self.bot.cards.extend(self.pack.cards[:6])
        self.pack.cards = self.pack.cards[6:]

    def print_info(self):
        # print('pack', self.pack.cards)
        print('main type', Card.main_type)
        print('pack size', len(self.pack.cards))
        print('bot has', len(self.bot.cards), 'cards')
        print('your cards')
        print(*self.player.cards)
        print('  ', end='')
        print(*[i + 1 for i in range(len(self.player.cards))], sep='     ')
        # print('bot', self.bot.cards)
        if len(self.game) % 2 == 0:
            for i in range(0, len(self.game), 2):
                print(self.game[i], '-->', self.game[i + 1])
        else:
            for i in range(0, len(self.game) - 1, 2):
                print(self.game[i], '-->', self.game[i + 1])
            print(self.game[-1], '-->')

    def add_new_cards(self):
        length1 = 6 - len(self.player.cards)
        length2 = 6 - len(self.bot.cards)
        if length1 > 0:
            self.player.cards.extend(self.pack.cards[:length1])
            self.pack.cards = self.pack.cards[length1:]
        if length2 > 0:
            self.bot.cards.extend(self.pack.cards[:length2])
            self.pack.cards = self.pack.cards[length2:]

    def find_min_rank_of_players(self):
        min_rank_player1 = min(
            list(map(lambda y: y.rank, filter(lambda x: x.type == self.pack.cards[-1].type, self.player.cards))) + [15])
        # 15 is necessary, because min() except error if gets 0 arguments
        min_rank_player2 = min(
            list(map(lambda y: y.rank, filter(lambda x: x.type == self.pack.cards[-1].type, self.bot.cards))) + [15])
        if min_rank_player2 == min_rank_player1:  # start new game, if all players haven't main type
            self.pack.cards.extend(self.player.cards)
            self.pack.cards.extend(self.bot.cards)
            self.player.cards.clear()
            self.player.cards.clear()
            self.get_cards()
            self.find_min_rank_of_players()
        else:
            self.process(min_rank_player1 < min_rank_player2)

    def process(self, player1_starts: bool):
        print(player1_starts)
        number1 = -1
        number2 = -1
        while (len(self.player.cards) > 0 and len(self.player.cards) > 0) or len(self.pack.cards) > 0:
            while number1 != 0 and number2 != 0 and (len(self.player.cards) > 0 and len(self.player.cards) > 0 or len(self.pack.cards) > 0):
                if player1_starts:  # player attack
                    print("\n" * 100)
                    self.print_info()
                    number1 = self.player.choose_card()
                    if number1 != 0:
                        self.game.append(self.player.cards[number1 - 1])
                        del self.player.cards[number1 - 1]
                        print("\n" * 100)
                        self.print_info()
                    else:
                        number1 = -1
                        player1_starts = not player1_starts
                        self.game.clear()
                        self.add_new_cards()
                        break
                    number2 = self.bot.defend_bot()
                    if number2 != 0:
                        self.game.append(self.bot.cards[number2 - 1])
                        del self.bot.cards[number2 - 1]
                        print("\n" * 100)
                        self.print_info()
                    else:
                        number2 = -1
                        self.bot.cards.extend(self.game[:])
                        self.game.clear()
                        self.add_new_cards()
                else:  # bot attack
                    print("\n" * 100)
                    self.print_info()
                    number2 = self.bot.choose_card_bot()
                    if number2 != 0:
                        self.game.append(self.bot.cards[number2 - 1])
                        del self.bot.cards[number2 - 1]
                        print("\n" * 100)
                        self.print_info()
                    else:
                        number2 = -1
                        player1_starts = not player1_starts
                        self.game.clear()
                        self.add_new_cards()
                        break
                    number1 = self.player.defend()
                    if number1 != 0:
                        self.game.append(self.player.cards[number1 - 1])
                        del self.player.cards[number1 - 1]
                        print("\n" * 100)
                        self.print_info()
                    else:
                        number1 = -1
                        self.player.cards.extend(self.game[:])
                        self.game.clear()
                        self.add_new_cards()

    def winner(self):
        if len(self.player.cards) == 0 and len(self.bot.cards) == 0:
            return 'Nobody won'
        elif len(self.player.cards) == 0:
            return 'Player won'
        else:
            return 'Bot won'
